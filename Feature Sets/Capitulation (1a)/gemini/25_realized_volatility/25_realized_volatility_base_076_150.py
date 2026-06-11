"""
25_realized_volatility — Base Features 076–150
Domain: expansion of price ranges, realized volatility
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd

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


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Volatility Extremes (Rankings)
def rvl_076_realized_vol_zscore_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    return (v - v.expanding().mean()) / (v.expanding().std() + _EPS)


def rvl_077_vol_expansion_regime_shift_63d(close: pd.Series) -> pd.Series:
    # Ratio of 21d vol to 126d vol
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v126 = np.log(close / close.shift(1)).rolling(126).std()
    return _safe_div(v21, v126)


# 091-105: Intraday and Gap Volatility
def rvl_091_intraday_vol_normalized_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # (High - Low) / Close
    r = (high - low) / close
    return r.rolling(21).mean()


def rvl_092_gap_volatility_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    # Standard deviation of overnight gaps
    gap = (open - close.shift(1)) / close.shift(1)
    return gap.rolling(63).std() * np.sqrt(252)


def rvl_093_overnight_to_intraday_vol_ratio_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)) / close.shift(1)
    intra = (close - open) / open
    return _safe_div(gap.rolling(63).std(), intra.rolling(63).std())


# 106-125: Volatility Decay and Persistence
def rvl_106_volatility_mean_reversion_score_21d(close: pd.Series) -> pd.Series:
    # Current 21d vol vs its 252d moving average
    v = np.log(close / close.shift(1)).rolling(21).std()
    return _safe_div(v, v.rolling(252).mean())


def rvl_107_consecutive_vol_expansion_days(close: pd.Series) -> pd.Series:
    # Days in a row 21d vol > previous day 21d vol
    v = np.log(close / close.shift(1)).rolling(21).std()
    inc = (v > v.shift(1)).astype(int)
    return inc.groupby((inc == 0).cumsum()).cumsum()


# 126-140: Multi- Horizon Risk Ratios
def rvl_126_vol_shock_index_21d(close: pd.Series) -> pd.Series:
    # Max daily return magnitude / Realized Vol
    ret = close.pct_change().abs()
    vol = ret.rolling(21).std()
    return _safe_div(ret.rolling(21).max(), vol)


def rvl_127_vol_efficiency_index_63d(close: pd.Series) -> pd.Series:
    # Net move / (Vol * duration)
    net_m = (close / close.shift(63) - 1).abs()
    vol = close.pct_change().rolling(63).std() * np.sqrt(63)
    return _safe_div(net_m, vol)


# 141-150: Final Volatility composites
def rvl_141_volatility_energy_density_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volatility^2 * Volume
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    return (v**2) * v_rat


def rvl_142_mktcap_vol_regime_shift_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    return _safe_div(v21, v252)


def rvl_143_volatility_at_unit_turnover_63d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    to = _safe_div(volume, sharesbas).rolling(21).mean()
    return _safe_div(v, to)


def rvl_144_vol_weighted_drawdown_climax(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return v * dd


def rvl_145_years_since_max_vol_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    idx = v.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def rvl_146_consecutive_days_above_ath_vol_median(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    med = v.expanding().median()
    above = (v > med).astype(int)
    return above.groupby((above == 0).cumsum()).cumsum()


def rvl_147_vol_drift_stability_score_63d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    return v.rolling(63).apply(_rsq, raw=True)


def rvl_148_ratio_of_vol_to_mdd_252d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(252).std()
    h = close.rolling(252).max()
    dd = (h - close) / h
    mdd = dd.rolling(252).max()
    return _safe_div(v, mdd)


def rvl_149_vol_momentum_zscore_63d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    roc = v.diff(21)
    return (roc - roc.rolling(63).mean()) / (roc.rolling(63).std() + _EPS)


def rvl_150_final_fear_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: Volatility * Volume Spike * (1 - Proximity to High)
    v = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(volume, volume.rolling(252).median())
    dist_h = (close.rolling(252).max() - close) / close.rolling(252).max()
    return v * vs * dist_h


# ── Registry ──────────────────────────────────────────────────────────────────

V25_REGISTRY = {
    "rvl_076_realized_vol_zscore_ath": {"inputs": ["close"], "func": rvl_076_realized_vol_zscore_ath},
    "rvl_077_vol_expansion_regime_shift_63d": {"inputs": ["close"], "func": rvl_077_vol_expansion_regime_shift_63d},
    "rvl_091_intraday_vol_normalized_21d": {"inputs": ["high", "low", "close"], "func": rvl_091_intraday_vol_normalized_21d},
    "rvl_092_gap_volatility_63d": {"inputs": ["close", "open"], "func": rvl_092_gap_volatility_63d},
    "rvl_093_overnight_intra_vol_ratio_63d": {"inputs": ["open", "high", "low", "close"], "func": rvl_093_overnight_to_intraday_vol_ratio_63d},
    "rvl_106_vol_mean_reversion_score_21d": {"inputs": ["close"], "func": rvl_106_vol_mean_reversion_score_21d},
    "rvl_107_consecutive_vol_expansion_days": {"inputs": ["close"], "func": rvl_107_consecutive_vol_expansion_days},
    "rvl_126_vol_shock_index_21d": {"inputs": ["close"], "func": rvl_126_vol_shock_index_21d},
    "rvl_127_vol_efficiency_index_63d": {"inputs": ["close"], "func": rvl_127_vol_efficiency_index_63d},
    "rvl_141_vol_energy_density_63d": {"inputs": ["close", "volume"], "func": rvl_141_volatility_energy_density_63d},
    "rvl_142_mktcap_vol_regime_shift_63d": {"inputs": ["close", "sharesbas"], "func": rvl_142_mktcap_vol_regime_shift_63d},
    "rvl_143_vol_at_unit_turnover_63d": {"inputs": ["close", "volume", "sharesbas"], "func": rvl_143_volatility_at_unit_turnover_63d},
    "rvl_144_vol_weighted_dd_climax": {"inputs": ["close"], "func": rvl_144_vol_weighted_drawdown_climax},
    "rvl_145_years_since_max_vol_ath": {"inputs": ["close"], "func": rvl_145_years_since_max_vol_ath},
    "rvl_146_consecutive_days_above_vol_median": {"inputs": ["close"], "func": rvl_146_consecutive_days_above_ath_vol_median},
    "rvl_147_vol_drift_stability_score_63d": {"inputs": ["close"], "func": rvl_147_vol_drift_stability_score_63d},
    "rvl_148_ratio_vol_mdd_252d": {"inputs": ["close"], "func": rvl_148_ratio_of_vol_to_mdd_252d},
    "rvl_149_vol_momentum_zscore_63d": {"inputs": ["close"], "func": rvl_149_vol_momentum_zscore_63d},
    "rvl_150_final_fear_index": {"inputs": ["close", "volume"], "func": rvl_150_final_fear_index},
}
