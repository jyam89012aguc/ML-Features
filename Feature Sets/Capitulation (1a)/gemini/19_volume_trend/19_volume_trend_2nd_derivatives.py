"""
19_volume_trend — 2nd Derivatives
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

# 25 features capturing acceleration of volume trend metrics
def vtr_drv2_001_volume_slope_21d_velocity(volume: pd.Series) -> pd.Series:
    # Change in short-term volume slope
    s = _safe_div(_rolling_slope(volume, 21), _rolling_mean(volume, 21))
    return s.diff(5)


def vtr_drv2_002_volume_slope_63d_velocity(volume: pd.Series) -> pd.Series:
    s = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    return s.diff(5)


def vtr_drv2_003_volume_rsq_63d_velocity(volume: pd.Series) -> pd.Series:
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = volume.rolling(63).apply(_rsq, raw=True)
    return r2.diff(5)


def vtr_drv2_004_volume_ma_cross_velocity(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(21).mean()
    v63 = volume.rolling(63).mean()
    ratio = _safe_div(v21, v63) - 1.0
    return ratio.diff(5)


def vtr_drv2_005_volume_price_divergence_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    ps = _safe_div(_rolling_slope(close, 63), _rolling_mean(close, 63))
    div = vs - ps
    return div.diff(5)


def vtr_drv2_006_obv_slope_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _safe_div(_rolling_slope(obv, 63), obv.abs().rolling(63).mean())
    return os.diff(5)


def vtr_drv2_007_chaikin_ad_slope_velocity(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ad = _safe_div((close - low) - (high - close), high - low) * volume
    ad_sum = ad.cumsum()
    asl = _safe_div(_rolling_slope(ad_sum, 21), volume.rolling(21).mean())
    return asl.diff(5)


def vtr_drv2_008_volume_trend_climax_velocity(volume: pd.Series) -> pd.Series:
    s = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = volume.rolling(63).apply(_rsq, raw=True)
    score = s * r2
    return score.diff(5)


def vtr_drv2_009_volume_trend_accel_velocity(volume: pd.Series) -> pd.Series:
    s = _safe_div(_rolling_slope(volume, 21), _rolling_mean(volume, 21))
    acc = s.diff(5)
    return acc.diff(5)


def vtr_drv2_010_mktcap_volume_trend_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    vs = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    ms = _safe_div(_rolling_slope(mc, 63), _rolling_mean(mc, 63))
    div = vs - ms
    return div.diff(5)


def vtr_drv2_011_volume_trend_se_velocity(volume: pd.Series) -> pd.Series:
    def _se(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).stderr
    se = volume.rolling(63).apply(_se, raw=True) / _rolling_mean(volume, 63)
    return se.diff(5)


def vtr_drv2_012_accumulation_climax_velocity_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _rolling_slope(obv, 21)
    prox = _safe_div(close, close.rolling(252).min())
    score = os * (1.0 / prox)
    return score.diff(5)


def vtr_drv2_013_volume_log_trend_velocity_accel(volume: pd.Series) -> pd.Series:
    v = np.log(volume + 1.0).diff(21) / 21.0
    return v.diff(5)


def vtr_drv2_014_volume_drift_zscore_velocity(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    drift = v21.diff(63)
    z = (drift - drift.rolling(252).mean()) / (drift.rolling(252).std() + _EPS)
    return z.diff(5)


def vtr_drv2_015_volume_slope_rank_velocity(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 63)
    rank = s.expanding().rank(pct=True)
    return rank.diff(5)


def vtr_drv2_016_obv_trend_stability_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = obv.rolling(63).apply(_rsq, raw=True)
    return r2.diff(5)


def vtr_drv2_017_volume_trend_break_velocity(volume: pd.Series) -> pd.Series:
    def _proj_ratio(y):
        if len(y) < 10: return 1.0
        from scipy.stats import linregress
        res = linregress(np.arange(len(y)-1), y[:-1])
        proj = res.intercept + res.slope * (len(y)-1)
        return _safe_div(pd.Series(y[-1]), pd.Series(proj)).iloc[0]
    rat = volume.rolling(21).apply(_proj_ratio, raw=True)
    return rat.diff(5)


def vtr_drv2_018_volume_drift_efficiency_velocity(volume: pd.Series) -> pd.Series:
    net_s = volume.diff(63)
    path_len = volume.diff().abs().rolling(63).sum()
    eff = _safe_div(net_s, path_len)
    return eff.diff(5)


def vtr_drv2_019_mktcap_obv_slope_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _safe_div(_rolling_slope(obv, 63), obv.abs().rolling(63).mean())
    return os.diff(5)


def vtr_drv2_020_volume_trend_convexity_velocity(volume: pd.Series) -> pd.Series:
    vi = volume.cumsum()
    s = _rolling_slope(volume, 252)
    tri = 0.5 * s * (252**2)
    conv = _safe_div(vi.diff(252), tri)
    return conv.diff(5)


def vtr_drv2_021_volume_trend_entropy_velocity(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 5)
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y[~np.isnan(y)], bins=5, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    e = s.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vtr_drv2_022_final_vtr_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vtr_075_volume_trend_final_composite(close, volume)
    return score.diff(5)


def vtr_drv2_023_turnover_trend_slope_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    s = _safe_div(_rolling_slope(to, 252), _rolling_mean(to, 252))
    return s.diff(5)


def vtr_drv2_024_volume_ema_slope_velocity(volume: pd.Series) -> pd.Series:
    v_ema = volume.ewm(span=21).mean()
    s = _safe_div(_rolling_slope(v_ema, 21), v_ema)
    return s.diff(5)


def vtr_drv2_025_consecutive_volume_inc_ma_velocity(volume: pd.Series) -> pd.Series:
    vma = volume.rolling(21).mean()
    inc = (vma > vma.shift(1)).astype(int)
    streak = inc.groupby((inc == 0).cumsum()).cumsum()
    return streak.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V19_V_REGISTRY = {
    "vtr_drv2_001_volume_slope_21d_velocity": {"inputs": ["volume"], "func": vtr_drv2_001_volume_slope_21d_velocity},
    "vtr_drv2_002_volume_slope_63d_velocity": {"inputs": ["volume"], "func": vtr_drv2_002_volume_slope_63d_velocity},
    "vtr_drv2_003_volume_rsq_63d_velocity": {"inputs": ["volume"], "func": vtr_drv2_003_volume_rsq_63d_velocity},
    "vtr_drv2_004_volume_ma_cross_velocity": {"inputs": ["volume"], "func": vtr_drv2_004_volume_ma_cross_velocity},
    "vtr_drv2_005_volume_price_divergence_velocity": {"inputs": ["close", "volume"], "func": vtr_drv2_005_volume_price_divergence_velocity},
    "vtr_drv2_006_obv_slope_velocity": {"inputs": ["close", "volume"], "func": vtr_drv2_006_obv_slope_velocity},
    "vtr_drv2_007_chaikin_ad_slope_velocity": {"inputs": ["volume", "high", "low", "close"], "func": vtr_drv2_007_chaikin_ad_slope_velocity},
    "vtr_drv2_008_volume_trend_climax_velocity": {"inputs": ["volume"], "func": vtr_drv2_008_volume_trend_climax_velocity},
    "vtr_drv2_009_volume_trend_accel_velocity": {"inputs": ["volume"], "func": vtr_drv2_009_volume_trend_accel_velocity},
    "vtr_drv2_010_mktcap_volume_trend_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vtr_drv2_010_mktcap_volume_trend_velocity},
    "vtr_drv2_011_volume_trend_se_velocity": {"inputs": ["volume"], "func": vtr_drv2_011_volume_trend_se_velocity},
    "vtr_drv2_012_accumulation_climax_velocity_accel": {"inputs": ["close", "volume"], "func": vtr_drv2_012_accumulation_climax_velocity_accel},
    "vtr_drv2_013_volume_log_trend_velocity_accel": {"inputs": ["volume"], "func": vtr_drv2_013_volume_log_trend_velocity_accel},
    "vtr_drv2_014_volume_drift_zscore_velocity": {"inputs": ["volume"], "func": vtr_drv2_014_volume_drift_zscore_velocity},
    "vtr_drv2_015_volume_slope_rank_velocity": {"inputs": ["volume"], "func": vtr_drv2_015_volume_slope_rank_velocity},
    "vtr_drv2_016_obv_trend_stability_velocity": {"inputs": ["close", "volume"], "func": vtr_drv2_016_obv_trend_stability_velocity},
    "vtr_drv2_017_volume_trend_break_velocity": {"inputs": ["volume"], "func": vtr_drv2_017_volume_trend_break_velocity},
    "vtr_drv2_018_volume_drift_efficiency_velocity": {"inputs": ["volume"], "func": vtr_drv2_018_volume_drift_efficiency_velocity},
    "vtr_drv2_019_mktcap_obv_slope_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vtr_drv2_019_mktcap_obv_slope_velocity},
    "vtr_drv2_020_volume_trend_convexity_velocity": {"inputs": ["volume"], "func": vtr_drv2_020_volume_trend_convexity_velocity},
    "vtr_drv2_021_volume_trend_entropy_velocity": {"inputs": ["volume"], "func": vtr_drv2_021_volume_trend_entropy_velocity},
    "vtr_drv2_022_final_vtr_composite_velocity": {"inputs": ["close", "volume"], "func": vtr_drv2_022_final_vtr_composite_velocity},
    "vtr_drv2_023_turnover_trend_slope_velocity": {"inputs": ["volume", "sharesbas"], "func": vtr_drv2_023_turnover_trend_slope_velocity},
    "vtr_drv2_024_volume_ema_slope_velocity": {"inputs": ["volume"], "func": vtr_drv2_024_volume_ema_slope_velocity},
    "vtr_drv2_025_consecutive_volume_inc_ma_velocity": {"inputs": ["volume"], "func": vtr_drv2_025_consecutive_volume_inc_ma_velocity},
}
