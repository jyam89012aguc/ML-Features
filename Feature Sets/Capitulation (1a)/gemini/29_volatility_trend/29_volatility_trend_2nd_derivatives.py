"""
29_volatility_trend — 2nd Derivatives
Domain: rate of change of base features — captures acceleration of decline/distress
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

# 25 features capturing acceleration of volatility trend metrics
def vtrd_drv2_001_vol_slope_21d_velocity(close: pd.Series) -> pd.Series:
    # Change in short-term vol slope
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    s = _safe_div(_rolling_slope(v5, 21), v5.rolling(21).mean())
    return s.diff(5)


def vtrd_drv2_002_vol_slope_63d_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    return s.diff(5)


def vtrd_drv2_003_vol_rsq_63d_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(63).apply(_rsq, raw=True)
    return rs.diff(5)


def vtrd_drv2_004_vol_ma_cross_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    v21 = v.rolling(21).mean()
    v63 = v.rolling(63).mean()
    ratio = _safe_div(v21, v63) - 1.0
    return ratio.diff(5)


def vtrd_drv2_005_vol_price_trend_div_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    ps = _safe_div(_rolling_slope(close, 63), close.rolling(63).mean())
    div = vs - ps
    return div.diff(5)


def vtrd_drv2_006_fear_build_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(63).apply(_rsq, raw=True)
    score = s * rs
    return score.diff(5)


def vtrd_drv2_007_vol_trend_accel_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 21)
    acc = s.diff(5)
    return acc.diff(5)


def vtrd_drv2_008_mktcap_vol_slope_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    s = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    return s.diff(5)


def vtrd_drv2_009_vix_proxy_slope_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    s = _rolling_slope(ratio, 63)
    return s.diff(5)


def vtrd_drv2_010_vol_trend_se_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _se(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).stderr
    se = v21.rolling(63).apply(_se, raw=True) / (v21.rolling(63).mean() + _EPS)
    return se.diff(5)


def vtrd_drv2_011_vol_exhaustion_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(_rolling_slope(v21, 21), v21.rolling(21).mean())
    pv = np.log(close).diff(5).abs()
    score = _safe_div(vs, pv + _EPS)
    return score.diff(5)


def vtrd_drv2_012_vol_climax_drift_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    v_rat = _safe_div(volume, volume.rolling(252).median())
    return (vs * v_rat).diff(5)


def vtrd_drv2_013_vol_trend_convexity_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    cv = v21.rolling(63).apply(_poly2, raw=True)
    return cv.diff(5)


def vtrd_drv2_014_vol_drift_zscore_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    drift = v21.diff(63)
    z = (drift - drift.rolling(252).mean()) / (drift.rolling(252).std() + _EPS)
    return z.diff(5)


def vtrd_drv2_015_vol_trend_regime_break_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    s21 = _rolling_slope(v, 21)
    s63 = _rolling_slope(v, 63)
    brk = s21 - s63
    return brk.diff(5)


def vtrd_drv2_016_consecutive_dec_vol_ma_velocity(close: pd.Series) -> pd.Series:
    vma = np.log(close / close.shift(1)).rolling(21).std().rolling(21).mean()
    dec = (vma < vma.shift(1)).astype(int)
    dur = dec.groupby((dec == 0).cumsum()).cumsum()
    return dur.diff(5)


def vtrd_drv2_017_vol_shock_momentum_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    shock = (ret.abs() > 2 * s).astype(int)
    cnt = shock.rolling(63).sum()
    return cnt.diff(21).diff(5)


def vtrd_drv2_018_vol_weighted_price_drift_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = close / (volume + _EPS)
    s = _safe_div(_rolling_slope(pv, 63), pv.rolling(63).mean())
    return s.diff(5)


def vtrd_drv2_019_vol_trend_stability_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(21).apply(_rsq, raw=True)
    return rs.diff(5)


def vtrd_drv2_020_vol_slope_rank_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 63)
    rank = s.expanding().rank(pct=True)
    return rank.diff(5)


def vtrd_drv2_021_vol_ema_slope_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    v_ema = v.ewm(span=21).mean()
    s = _safe_div(_rolling_slope(v_ema, 21), v_ema)
    return s.diff(5)


def vtrd_drv2_022_cumulative_vol_trend_energy_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 21)
    energy = s.cumsum() / (s.abs().cumsum() + _EPS)
    return energy.diff(5)


def vtrd_drv2_023_final_vol_trend_fear_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vtrd_150_vol_trend_final_fear_index(close, volume)
    return score.diff(5)


def vtrd_drv2_024_vol_slope_to_atr_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _rolling_slope(v21, 63)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(63).mean() / close.rolling(63).mean()
    ratio = _safe_div(vs, atr)
    return ratio.diff(5)


def vtrd_drv2_025_vol_trend_final_composite_velocity(close: pd.Series) -> pd.Series:
    score = vtrd_075_volatility_trend_final_composite(close)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V29_V_REGISTRY = {
    "vtrd_drv2_001_vol_slope_21d_velocity": {"inputs": ["close"], "func": vtrd_drv2_001_vol_slope_21d_velocity},
    "vtrd_drv2_002_vol_slope_63d_velocity": {"inputs": ["close"], "func": vtrd_drv2_002_vol_slope_63d_velocity},
    "vtrd_drv2_003_vol_rsq_63d_velocity": {"inputs": ["close"], "func": vtrd_drv2_003_vol_rsq_63d_velocity},
    "vtrd_drv2_004_vol_ma_cross_velocity": {"inputs": ["close"], "func": vtrd_drv2_004_vol_ma_cross_velocity},
    "vtrd_drv2_005_vol_price_trend_div_velocity": {"inputs": ["close"], "func": vtrd_drv2_005_vol_price_trend_div_velocity},
    "vtrd_drv2_006_fear_build_velocity": {"inputs": ["close"], "func": vtrd_drv2_006_fear_build_velocity},
    "vtrd_drv2_007_vol_trend_accel_velocity": {"inputs": ["close"], "func": vtrd_drv2_007_vol_trend_accel_velocity},
    "vtrd_drv2_008_mktcap_vol_slope_velocity": {"inputs": ["close", "sharesbas"], "func": vtrd_drv2_008_mktcap_vol_slope_velocity},
    "vtrd_drv2_009_vix_proxy_slope_velocity": {"inputs": ["close"], "func": vtrd_drv2_009_vix_proxy_slope_velocity},
    "vtrd_drv2_010_vol_trend_se_velocity": {"inputs": ["close"], "func": vtrd_drv2_010_vol_trend_se_velocity},
    "vtrd_drv2_011_vol_exhaustion_velocity": {"inputs": ["close"], "func": vtrd_drv2_011_vol_exhaustion_velocity},
    "vtrd_drv2_012_vol_climax_drift_velocity": {"inputs": ["close", "volume"], "func": vtrd_drv2_012_vol_climax_drift_velocity},
    "vtrd_drv2_013_vol_trend_convexity_velocity": {"inputs": ["close"], "func": vtrd_drv2_013_vol_trend_convexity_velocity},
    "vtrd_drv2_014_vol_drift_zscore_velocity": {"inputs": ["close"], "func": vtrd_drv2_014_vol_drift_zscore_velocity},
    "vtrd_drv2_015_vol_trend_regime_break_velocity": {"inputs": ["close"], "func": vtrd_drv2_015_vol_trend_regime_break_velocity},
    "vtrd_drv2_016_consecutive_dec_vol_ma_velocity": {"inputs": ["close"], "func": vtrd_drv2_016_consecutive_dec_vol_ma_velocity},
    "vtrd_drv2_017_vol_shock_momentum_velocity": {"inputs": ["close"], "func": vtrd_drv2_017_vol_shock_momentum_velocity},
    "vtrd_drv2_018_vol_weighted_price_drift_velocity": {"inputs": ["close", "volume"], "func": vtrd_drv2_018_vol_weighted_price_drift_velocity},
    "vtrd_drv2_019_vol_trend_stability_velocity": {"inputs": ["close"], "func": vtrd_drv2_019_vol_trend_stability_velocity},
    "vtrd_drv2_020_vol_slope_rank_velocity": {"inputs": ["close"], "func": vtrd_drv2_020_vol_slope_rank_velocity},
    "vtrd_drv2_021_vol_ema_slope_velocity": {"inputs": ["close"], "func": vtrd_drv2_021_vol_ema_slope_velocity},
    "vtrd_drv2_022_cumulative_vol_trend_energy_velocity": {"inputs": ["close"], "func": vtrd_drv2_022_cumulative_vol_trend_energy_velocity},
    "vtrd_drv2_023_final_vol_trend_fear_velocity": {"inputs": ["close", "volume"], "func": vtrd_drv2_023_final_vol_trend_fear_velocity},
    "vtrd_drv2_024_vol_slope_to_atr_velocity": {"inputs": ["high", "low", "close"], "func": vtrd_drv2_024_vol_slope_to_atr_velocity},
    "vtrd_drv2_025_vol_trend_final_composite_velocity": {"inputs": ["close"], "func": vtrd_drv2_025_vol_trend_final_composite_velocity},
}
