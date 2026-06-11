"""
29_volatility_trend — 3rd Derivatives
Domain: rate of change of 2nd derivatives — captures exhaustion/inflection of acceleration
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

# 25 features capturing exhaustion/inflection of volatility trend acceleration (jerk)
def vtrd_drv3_001_vol_slope_21d_jerk(close: pd.Series) -> pd.Series:
    # Rate of change of volatility slope velocity
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    s = _safe_div(_rolling_slope(v5, 21), v5.rolling(21).mean())
    vel = s.diff(5)
    return vel.diff(5)


def vtrd_drv3_002_vol_slope_63d_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    vel = s.diff(5)
    return vel.diff(5)


def vtrd_drv3_003_vol_rsq_63d_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = v21.rolling(63).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)


def vtrd_drv3_004_vol_ma_cross_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    v21 = v.rolling(21).mean()
    v63 = v.rolling(63).mean()
    ratio = _safe_div(v21, v63) - 1.0
    vel = ratio.diff(5)
    return vel.diff(5)


def vtrd_drv3_005_vol_price_trend_div_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    ps = _safe_div(_rolling_slope(close, 63), close.rolling(63).mean())
    div = vs - ps
    vel = div.diff(5)
    return vel.diff(5)


def vtrd_drv3_006_fear_build_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(63).apply(_rsq, raw=True)
    score = s * rs
    vel = score.diff(5)
    return vel.diff(5)


def vtrd_drv3_007_vol_trend_accel_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 21)
    acc = s.diff(5)
    vel = acc.diff(5)
    return vel.diff(5)


def vtrd_drv3_008_mktcap_vol_slope_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    s = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    vel = s.diff(5)
    return vel.diff(5)


def vtrd_drv3_009_vix_proxy_slope_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    s = _rolling_slope(ratio, 63)
    vel = s.diff(5)
    return vel.diff(5)


def vtrd_drv3_010_vol_trend_se_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _se(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).stderr
    se = v21.rolling(63).apply(_se, raw=True) / (v21.rolling(63).mean() + _EPS)
    vel = se.diff(5)
    return vel.diff(5)


def vtrd_drv3_011_vol_exhaustion_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(_rolling_slope(v21, 21), v21.rolling(21).mean())
    pv = np.log(close).diff(5).abs()
    score = _safe_div(vs, pv + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vtrd_drv3_012_vol_climax_drift_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(_rolling_slope(v21, 63), v21.rolling(63).mean())
    v_rat = _safe_div(volume, volume.rolling(252).median())
    vel = (vs * v_rat).diff(5)
    return vel.diff(5)


def vtrd_drv3_013_vol_trend_convexity_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    cv = v21.rolling(63).apply(_poly2, raw=True)
    vel = cv.diff(5)
    return vel.diff(5)


def vtrd_drv3_014_vol_drift_zscore_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    drift = v21.diff(63)
    z = (drift - drift.rolling(252).mean()) / (drift.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vtrd_drv3_015_vol_trend_regime_break_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    s21 = _rolling_slope(v, 21)
    s63 = _rolling_slope(v, 63)
    brk = s21 - s63
    vel = brk.diff(5)
    return vel.diff(5)


def vtrd_drv3_016_consecutive_dec_vol_ma_jerk(close: pd.Series) -> pd.Series:
    vma = np.log(close / close.shift(1)).rolling(21).std().rolling(21).mean()
    dec = (vma < vma.shift(1)).astype(int)
    dur = dec.groupby((dec == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vtrd_drv3_017_vol_shock_momentum_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    shock = (ret.abs() > 2 * s).astype(int)
    cnt = shock.rolling(63).sum()
    vel = cnt.diff(21).diff(5)
    return vel.diff(5)


def vtrd_drv3_018_vol_weighted_price_drift_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = close / (volume + _EPS)
    s = _safe_div(_rolling_slope(pv, 63), pv.rolling(63).mean())
    vel = s.diff(5)
    return vel.diff(5)


def vtrd_drv3_019_vol_trend_stability_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(21).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def vtrd_drv3_020_vol_slope_rank_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 63)
    rank = s.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vtrd_drv3_021_vol_ema_slope_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    v_ema = v.ewm(span=21).mean()
    s = _safe_div(_rolling_slope(v_ema, 21), v_ema)
    vel = s.diff(5)
    return vel.diff(5)


def vtrd_drv3_022_cumulative_vol_trend_energy_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    s = _rolling_slope(v21, 21)
    energy = s.cumsum() / (s.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vtrd_drv3_023_final_vol_trend_fear_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vtrd_150_vol_trend_final_fear_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vtrd_drv3_024_vol_slope_to_atr_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vs = _rolling_slope(v21, 63)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(63).mean() / close.rolling(63).mean()
    ratio = _safe_div(vs, atr)
    vel = ratio.diff(5)
    return vel.diff(5)


def vtrd_drv3_025_vol_trend_final_composite_jerk(close: pd.Series) -> pd.Series:
    score = vtrd_075_volatility_trend_final_composite(close)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V29_A_REGISTRY = {
    "vtrd_drv3_001_vol_slope_21d_jerk": {"inputs": ["close"], "func": vtrd_drv3_001_vol_slope_21d_jerk},
    "vtrd_drv3_002_vol_slope_63d_jerk": {"inputs": ["close"], "func": vtrd_drv3_002_vol_slope_63d_jerk},
    "vtrd_drv3_003_vol_rsq_63d_jerk": {"inputs": ["close"], "func": vtrd_drv3_003_vol_rsq_63d_jerk},
    "vtrd_drv3_004_vol_ma_cross_jerk": {"inputs": ["close"], "func": vtrd_drv3_004_vol_ma_cross_jerk},
    "vtrd_drv3_005_vol_price_trend_div_jerk": {"inputs": ["close"], "func": vtrd_drv3_005_vol_price_trend_div_jerk},
    "vtrd_drv3_006_fear_build_jerk": {"inputs": ["close"], "func": vtrd_drv3_006_fear_build_jerk},
    "vtrd_drv3_007_vol_trend_accel_jerk": {"inputs": ["close"], "func": vtrd_drv3_007_vol_trend_accel_jerk},
    "vtrd_drv3_008_mktcap_vol_slope_jerk": {"inputs": ["close", "sharesbas"], "func": vtrd_drv3_008_mktcap_vol_slope_jerk},
    "vtrd_drv3_009_vix_proxy_slope_jerk": {"inputs": ["close"], "func": vtrd_drv3_009_vix_proxy_slope_jerk},
    "vtrd_drv3_010_vol_trend_se_jerk": {"inputs": ["close"], "func": vtrd_drv3_010_vol_trend_se_jerk},
    "vtrd_drv3_011_vol_exhaustion_jerk": {"inputs": ["close"], "func": vtrd_drv3_011_vol_exhaustion_jerk},
    "vtrd_drv3_012_vol_climax_drift_jerk": {"inputs": ["close", "volume"], "func": vtrd_drv3_012_vol_climax_drift_jerk},
    "vtrd_drv3_013_vol_trend_convexity_jerk": {"inputs": ["close"], "func": vtrd_drv3_013_vol_trend_convexity_jerk},
    "vtrd_drv3_014_vol_drift_zscore_jerk": {"inputs": ["close"], "func": vtrd_drv3_014_vol_drift_zscore_jerk},
    "vtrd_drv3_015_vol_trend_regime_break_jerk": {"inputs": ["close"], "func": vtrd_drv3_015_vol_trend_regime_break_jerk},
    "vtrd_drv3_016_consecutive_dec_vol_ma_jerk": {"inputs": ["close"], "func": vtrd_drv3_016_consecutive_dec_vol_ma_jerk},
    "vtrd_drv3_017_vol_shock_momentum_jerk": {"inputs": ["close"], "func": vtrd_drv3_017_vol_shock_momentum_jerk},
    "vtrd_drv3_018_vol_weighted_price_drift_jerk": {"inputs": ["close", "volume"], "func": vtrd_drv3_018_vol_weighted_price_drift_jerk},
    "vtrd_drv3_019_vol_trend_stability_jerk": {"inputs": ["close"], "func": vtrd_drv3_019_vol_trend_stability_jerk},
    "vtrd_drv3_020_vol_slope_rank_jerk": {"inputs": ["close"], "func": vtrd_drv3_020_vol_slope_rank_jerk},
    "vtrd_drv3_021_vol_ema_slope_jerk": {"inputs": ["close"], "func": vtrd_drv3_021_vol_ema_slope_jerk},
    "vtrd_drv3_022_cumulative_vol_trend_energy_jerk": {"inputs": ["close"], "func": vtrd_drv3_022_cumulative_vol_trend_energy_jerk},
    "vtrd_drv3_023_final_vol_trend_fear_jerk": {"inputs": ["close", "volume"], "func": vtrd_drv3_023_final_vol_trend_fear_jerk},
    "vtrd_drv3_024_vol_slope_to_atr_jerk": {"inputs": ["high", "low", "close"], "func": vtrd_drv3_024_vol_slope_to_atr_jerk},
    "vtrd_drv3_025_vol_trend_final_composite_jerk": {"inputs": ["close"], "func": vtrd_drv3_025_vol_trend_final_composite_jerk},
}
