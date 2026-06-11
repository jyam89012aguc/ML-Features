"""
19_volume_trend — Base Features 076–150
Domain: directional drift in volume over weeks
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

# 076-090: Distributional Trend Ranks
def vtr_076_volume_slope_pct_rank_ath(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 63)
    return s.expanding().rank(pct=True)


def vtr_077_volume_slope_zscore_252d(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 63)
    return (s - s.rolling(252).mean()) / s.rolling(252).std()


def vtr_078_volume_trend_oscillator_21d(volume: pd.Series) -> pd.Series:
    # 5-day slope vs 21-day slope
    s5 = _rolling_slope(volume, 5)
    s21 = _rolling_slope(volume, 21)
    return s5 - s21


# 091-105: Accumulation / Distribution Slopes (Complex)
def vtr_091_ad_slope_ratio_63d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Chaikin A/D Slope / Volume Slope
    ad = _safe_div((close - low) - (high - close), high - low) * volume
    ad_sum = ad.cumsum()
    ad_slope = _rolling_slope(ad_sum, 63)
    v_slope = _rolling_slope(volume.cumsum(), 63)
    return _safe_div(ad_slope, v_slope)


def vtr_092_volume_weighted_price_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Slope of (Price * Volume)
    pv = close * volume
    return _safe_div(_rolling_slope(pv, 63), pv.rolling(63).mean())


# 106-125: Event and Metric Specific Volume Trends
def vtr_106_mktcap_volume_slope_divergence_252d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ms = _safe_div(_rolling_slope(mc, 252), mc.rolling(252).mean())
    vs = _safe_div(_rolling_slope(volume, 252), volume.rolling(252).mean())
    return vs - ms


def vtr_107_turnover_trend_acceleration_63d(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    s = _rolling_slope(to, 21)
    return s.diff(21)


# 126-140: Multi- Horizon Resistance Trends
def vtr_126_obv_trend_stability_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # R-squared of OBV
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    def _rsq(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    return obv.rolling(63).apply(_rsq, raw=True)


def vtr_127_volume_trend_break_indicator_21d(volume: pd.Series) -> pd.Series:
    # Current volume / (Prior volume trend projection)
    def _proj_ratio(y):
        if len(y) < 10: return 1.0
        res = linregress(np.arange(len(y)-1), y[:-1])
        proj = res.intercept + res.slope * (len(y)-1)
        return _safe_div(pd.Series(y[-1]), pd.Series(proj)).iloc[0]
    return volume.rolling(21).apply(_proj_ratio, raw=True)


# 141-150: Final Volume Trend composites
def vtr_141_volume_drift_efficiency_score(volume: pd.Series) -> pd.Series:
    # Net Slope / Path Length of Volume
    net_s = volume.diff(63)
    path_len = volume.diff().abs().rolling(63).sum()
    return _safe_div(net_s, path_len)


def vtr_142_mktcap_weighted_obv_slope(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.diff()
    obv = (np.sign(ret) * volume).cumsum()
    return _safe_div(_rolling_slope(obv, 63), obv.abs().rolling(63).mean())


def vtr_143_accumulation_climax_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (OBV Slope) * (Price Proximity to Low)
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _rolling_slope(obv, 21)
    prox = _safe_div(close, close.rolling(252).min())
    return os * (1.0 / prox)


def vtr_144_volume_trend_regime_zscore_ath(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 21)
    return (s - s.expanding().mean()) / s.expanding().std()


def vtr_145_consecutive_days_increasing_volume_ma(volume: pd.Series) -> pd.Series:
    vma = volume.rolling(21).mean()
    inc = (vma > vma.shift(1)).astype(int)
    return inc.groupby((inc == 0).cumsum()).cumsum()


def vtr_146_volume_slope_to_atr_ratio_63d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vs = _rolling_slope(volume, 63)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(63).mean() / close.rolling(63).mean()
    return _safe_div(vs, atr)


def vtr_147_volume_trend_convexity_score_252d(volume: pd.Series) -> pd.Series:
    # Ratio of volume integral to triangle area formed by slope
    vi = volume.cumsum()
    s = _rolling_slope(volume, 252)
    tri_area = 0.5 * s * (252**2)
    return _safe_div(vi.diff(252), tri_area)


def vtr_148_obv_relative_to_ath_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    return obv.expanding().rank(pct=True)


def vtr_149_volume_trend_entropy_63d(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 5)
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y[~np.isnan(y)], bins=5, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    return s.rolling(63).apply(_ent, raw=True)


def vtr_150_volume_trend_final_climax_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Volume Slope) * (OBV R-squared) * (Drawdown Velocity)
    vs = vtr_002_volume_slope_63d(volume)
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    def _rsq(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    or2 = obv.rolling(63).apply(_rsq, raw=True)
    dv = np.log(close).diff(5).abs()
    return vs * or2 * dv


# ── Registry ──────────────────────────────────────────────────────────────────

V19_REGISTRY = {
    "vtr_076_volume_slope_pct_rank_ath": {"inputs": ["volume"], "func": vtr_076_volume_slope_pct_rank_ath},
    "vtr_077_volume_slope_zscore_252d": {"inputs": ["volume"], "func": vtr_077_volume_slope_zscore_252d},
    "vtr_078_volume_trend_oscillator_21d": {"inputs": ["volume"], "func": vtr_078_volume_trend_oscillator_21d},
    "vtr_091_ad_slope_ratio_63d": {"inputs": ["volume", "high", "low", "close"], "func": vtr_091_ad_slope_ratio_63d},
    "vtr_092_volume_weighted_price_slope_63d": {"inputs": ["close", "volume"], "func": vtr_092_volume_weighted_price_slope_63d},
    "vtr_106_mktcap_volume_slope_divergence_252d": {"inputs": ["close", "volume", "sharesbas"], "func": vtr_106_mktcap_volume_slope_divergence_252d},
    "vtr_107_turnover_trend_acceleration_63d": {"inputs": ["volume", "sharesbas"], "func": vtr_107_turnover_trend_acceleration_63d},
    "vtr_126_obv_trend_stability_63d": {"inputs": ["close", "volume"], "func": vtr_126_obv_trend_stability_63d},
    "vtr_127_volume_trend_break_indicator_21d": {"inputs": ["volume"], "func": vtr_127_volume_trend_break_indicator_21d},
    "vtr_141_volume_drift_efficiency_score": {"inputs": ["volume"], "func": vtr_141_volume_drift_efficiency_score},
    "vtr_142_mktcap_weighted_obv_slope": {"inputs": ["close", "volume", "sharesbas"], "func": vtr_142_mktcap_weighted_obv_slope},
    "vtr_143_accumulation_climax_velocity_21d": {"inputs": ["close", "volume"], "func": vtr_143_accumulation_climax_velocity_21d},
    "vtr_144_volume_trend_regime_zscore_ath": {"inputs": ["volume"], "func": vtr_144_volume_trend_regime_zscore_ath},
    "vtr_145_consecutive_days_increasing_volume_ma": {"inputs": ["volume"], "func": vtr_145_consecutive_days_increasing_volume_ma},
    "vtr_146_volume_slope_to_atr_ratio_63d": {"inputs": ["volume", "high", "low", "close"], "func": vtr_146_volume_slope_to_atr_ratio_63d},
    "vtr_147_volume_trend_convexity_score_252d": {"inputs": ["volume"], "func": vtr_147_volume_trend_convexity_score_252d},
    "vtr_148_obv_relative_to_ath_rank": {"inputs": ["close", "volume"], "func": vtr_148_obv_relative_to_ath_rank},
    "vtr_149_volume_trend_entropy_63d": {"inputs": ["volume"], "func": vtr_149_volume_trend_entropy_63d},
    "vtr_150_volume_trend_final_climax_index": {"inputs": ["close", "volume"], "func": vtr_150_volume_trend_final_climax_index},
}
