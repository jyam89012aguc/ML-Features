"""
29_volatility_trend — Base Features 076–150
Domain: directional drift in volatility, fear gauges
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd
from scipy.stats import linregress

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    def _slope(y):
        if len(y) < 2: return np.nan
        x = np.arange(len(y))
        return linregress(x, y).slope
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Distribution of Vol Trends (Ranks)
def vtrd_076_vol_slope_pct_rank_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 63)
    return s.expanding().rank(pct=True)


def vtrd_077_vol_shock_momentum_21d(close: pd.Series) -> pd.Series:
    # ROC of the 2-sigma outlier count
    ret = close.pct_change()
    s = ret.rolling(252).std()
    shock = (ret.abs() > 2 * s).astype(int)
    cnt = shock.rolling(63).sum()
    return cnt.diff(21)


# 091-105: Volatility Curve Shape (Convexity)
def vtrd_091_vol_trend_convexity_score_63d(close: pd.Series) -> pd.Series:
    # 2nd order polyfit on volatility path
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y):
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    return v21.rolling(63).apply(_poly2, raw=True)


def vtrd_092_vol_v_shape_score_63d(close: pd.Series) -> pd.Series:
    # Comparison of vol slope in first vs second half
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    def _vscore(y):
        mid = len(y) // 2
        s1 = linregress(np.arange(mid), y[:mid]).slope
        s2 = linregress(np.arange(mid), y[mid:]).slope
        return s2 - s1
    return v5.rolling(63).apply(_vscore, raw=True)


# 106-125: Specialized Flow Trends (Vol-Price Interactions)
def vtrd_106_vol_weighted_price_drift_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Slope of (Price / Volume)
    pv = close / (volume + _EPS)
    return _safe_div(_rolling_slope(pv, 63), pv.rolling(63).mean())


def vtrd_107_turnover_vol_trend_acceleration_63d(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    v_to = to.pct_change().rolling(21).std()
    return _rolling_slope(v_to, 21).diff(21)


# 126-140: Multi-Horizon Risk Convergence
def vtrd_126_vol_trend_spread_21_252(close: pd.Series) -> pd.Series:
    s21 = vtrd_001_vol_slope_21d(close)
    s252 = vtrd_003_vol_slope_252d(close)
    return s21 - s252


def vtrd_127_vol_trend_break_indicator_21d(close: pd.Series) -> pd.Series:
    # Current vol / (Prior vol trend projection)
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _proj(y):
        if len(y) < 10: return 1.0
        res = linregress(np.arange(len(y)-1), y[:-1])
        p = res.intercept + res.slope * (len(y)-1)
        return _safe_div(pd.Series(y[-1]), pd.Series(p)).iloc[0]
    return v.rolling(21).apply(_proj, raw=True)


# 141-150: Final Volatility Trend composites
def vtrd_141_volatility_exhaustion_momentum_21d(close: pd.Series) -> pd.Series:
    # (Vol Slope) / (Price Velocity) -> higher = fear building with no price progress
    vs = vtrd_001_vol_slope_21d(close)
    pv = np.log(close).diff(5).abs()
    return _safe_div(vs, pv + _EPS)


def vtrd_142_mktcap_weighted_vol_drift(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_m = np.log(mc / mc.shift(1)).rolling(21).std()
    return _safe_div(_rolling_slope(v_m, 63), v_m.rolling(63).mean())


def vtrd_143_consecutive_days_declining_vol_ma(close: pd.Series) -> pd.Series:
    vma = np.log(close / close.shift(1)).rolling(21).std().rolling(21).mean()
    dec = (vma < vma.shift(1)).astype(int)
    return dec.groupby((dec == 0).cumsum()).cumsum()


def vtrd_144_vol_trend_climax_reversal_score(close: pd.Series, low: pd.Series) -> pd.Series:
    # (Vol Slope Change) * (Close from Low)
    vs = vtrd_001_vol_slope_21d(close)
    c_low = _safe_div(close, low)
    return vs.diff(5) * c_low


def vtrd_145_sustained_vol_expansion_index_252d(close: pd.Series) -> pd.Series:
    # Fraction of year with 21d vol slope in highest decile
    vs = vtrd_001_vol_slope_21d(close)
    q90 = vs.rolling(252).quantile(0.9)
    return (vs > q90).rolling(252).mean()


def vtrd_146_years_since_max_vol_slope_ath(close: pd.Series) -> pd.Series:
    vs = vtrd_002_vol_slope_63d(close)
    idx = vs.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vtrd_147_vol_trend_regime_break_63d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    s21 = _rolling_slope(v, 21)
    s63 = _rolling_slope(v, 63)
    return s21 - s63


def vtrd_148_ratio_of_vol_slope_peaks_to_troughs_252d(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    v = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v, 21)
    p = argrelextrema(s.values, np.greater, order=5)[0]
    t = argrelextrema(s.values, np.less, order=5)[0]
    is_p = pd.Series(0, index=close.index); is_p.iloc[p] = 1
    is_t = pd.Series(0, index=close.index); is_t.iloc[t] = 1
    return _safe_div(is_p.rolling(252).sum(), is_t.rolling(252).sum())


def vtrd_149_cumulative_vol_trend_energy_ath(close: pd.Series) -> pd.Series:
    vs = vtrd_001_vol_slope_21d(close)
    return vs.cumsum() / (vs.abs().cumsum() + _EPS)


def vtrd_150_vol_trend_final_fear_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Vol Slope) * (Volume Spike) * (Drawdown Depth)
    vs = vtrd_002_vol_slope_63d(close)
    v_rat = _safe_div(volume, volume.rolling(252).median())
    dd = (close.rolling(252).max() - close) / close.rolling(252).max()
    return vs * v_rat * dd


# ── Registry ──────────────────────────────────────────────────────────────────

V29_REGISTRY = {
    "vtrd_076_vol_slope_pct_rank_ath": {"inputs": ["close"], "func": vtrd_076_vol_slope_pct_rank_ath},
    "vtrd_077_vol_shock_momentum_21d": {"inputs": ["close"], "func": vtrd_077_vol_shock_momentum_21d},
    "vtrd_091_vol_trend_convexity_63d": {"inputs": ["close"], "func": vtrd_091_vol_trend_convexity_score_63d},
    "vtrd_092_vol_v_shape_score_63d": {"inputs": ["close"], "func": vtrd_092_vol_v_shape_score_63d},
    "vtrd_106_vol_weighted_price_drift": {"inputs": ["close", "volume"], "func": vtrd_106_vol_weighted_price_drift_63d},
    "vtrd_107_turnover_vol_trend_accel": {"inputs": ["volume", "sharesbas"], "func": vtrd_107_turnover_vol_trend_acceleration_63d},
    "vtrd_126_vol_trend_spread_21_252": {"inputs": ["close"], "func": vtrd_126_vol_trend_spread_21_252},
    "vtrd_127_vol_trend_break_indicator": {"inputs": ["close"], "func": vtrd_127_vol_trend_break_indicator_21d},
    "vtrd_141_vol_exhaustion_momentum": {"inputs": ["close"], "func": vtrd_141_volatility_exhaustion_momentum_21d},
    "vtrd_142_mktcap_weighted_vol_drift": {"inputs": ["close", "sharesbas"], "func": vtrd_142_mktcap_weighted_vol_drift},
    "vtrd_143_consecutive_days_dec_vol_ma": {"inputs": ["close"], "func": vtrd_143_consecutive_days_declining_vol_ma},
    "vtrd_144_vol_trend_climax_reversal": {"inputs": ["close", "low"], "func": vtrd_144_vol_trend_climax_reversal_score},
    "vtrd_145_sustained_vol_expansion_index": {"inputs": ["close"], "func": vtrd_145_sustained_vol_expansion_index_252d},
    "vtrd_146_years_since_max_vol_slope": {"inputs": ["close"], "func": vtrd_146_years_since_max_vol_slope_ath},
    "vtrd_147_vol_trend_regime_break_63d": {"inputs": ["close"], "func": vtrd_147_vol_trend_regime_break_63d},
    "vtrd_148_ratio_vol_slope_peaks_troughs": {"inputs": ["close"], "func": vtrd_148_ratio_of_vol_slope_peaks_to_troughs_252d},
    "vtrd_149_cumulative_vol_trend_energy": {"inputs": ["close"], "func": vtrd_149_cumulative_vol_trend_energy_ath},
    "vtrd_150_vol_trend_final_fear_index": {"inputs": ["close", "volume"], "func": vtrd_150_vol_trend_final_fear_index},
}
