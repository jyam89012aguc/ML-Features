"""
19_volume_trend — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volume trend acceleration (jerk)
def vtr_drv3_001_volume_slope_21d_jerk(volume: pd.Series) -> pd.Series:
    # Rate of change of volume slope velocity
    s = _safe_div(_rolling_slope(volume, 21), _rolling_mean(volume, 21))
    vel = s.diff(5)
    return vel.diff(5)


def vtr_drv3_002_volume_slope_63d_jerk(volume: pd.Series) -> pd.Series:
    s = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    vel = s.diff(5)
    return vel.diff(5)


def vtr_drv3_003_volume_rsq_63d_jerk(volume: pd.Series) -> pd.Series:
    def _rsq(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = volume.rolling(63).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)


def vtr_drv3_004_volume_ma_cross_jerk(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(21).mean()
    v63 = volume.rolling(63).mean()
    ratio = _safe_div(v21, v63) - 1.0
    vel = ratio.diff(5)
    return vel.diff(5)


def vtr_drv3_005_volume_price_divergence_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    ps = _safe_div(_rolling_slope(close, 63), _rolling_mean(close, 63))
    div = vs - ps
    vel = div.diff(5)
    return vel.diff(5)


def vtr_drv3_006_obv_slope_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _safe_div(_rolling_slope(obv, 63), obv.abs().rolling(63).mean())
    vel = os.diff(5)
    return vel.diff(5)


def vtr_drv3_007_chaikin_ad_slope_jerk(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ad = _safe_div((close - low) - (high - close), high - low) * volume
    ad_sum = ad.cumsum()
    asl = _safe_div(_rolling_slope(ad_sum, 21), volume.rolling(21).mean())
    vel = asl.diff(5)
    return vel.diff(5)


def vtr_drv3_008_volume_trend_climax_jerk(volume: pd.Series) -> pd.Series:
    s = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    def _rsq(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = volume.rolling(63).apply(_rsq, raw=True)
    score = s * r2
    vel = score.diff(5)
    return vel.diff(5)


def vtr_drv3_009_volume_trend_accel_jerk(volume: pd.Series) -> pd.Series:
    s = _safe_div(_rolling_slope(volume, 21), _rolling_mean(volume, 21))
    acc = s.diff(5)
    vel = acc.diff(5)
    return vel.diff(5)


def vtr_drv3_010_mktcap_volume_trend_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    vs = _safe_div(_rolling_slope(volume, 63), _rolling_mean(volume, 63))
    ms = _safe_div(_rolling_slope(mc, 63), _rolling_mean(mc, 63))
    div = vs - ms
    vel = div.diff(5)
    return vel.diff(5)


def vtr_drv3_011_volume_trend_se_jerk(volume: pd.Series) -> pd.Series:
    def _se(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).stderr
    se = volume.rolling(63).apply(_se, raw=True) / (_rolling_mean(volume, 63) + _EPS)
    vel = se.diff(5)
    return vel.diff(5)


def vtr_drv3_012_accumulation_climax_velocity_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _rolling_slope(obv, 21)
    prox = _safe_div(close, close.rolling(252).min())
    score = os * (1.0 / prox)
    vel = score.diff(5)
    return vel.diff(5)


def vtr_drv3_013_volume_log_trend_velocity_jerk(volume: pd.Series) -> pd.Series:
    v = np.log(volume + 1.0).diff(21) / 21.0
    vel = v.diff(5)
    return vel.diff(5)


def vtr_drv3_014_volume_drift_zscore_jerk(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    drift = v21.diff(63)
    z = (drift - drift.rolling(252).mean()) / (drift.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vtr_drv3_015_volume_slope_rank_jerk(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 63)
    rank = s.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vtr_drv3_016_obv_trend_stability_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    def _rsq(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = obv.rolling(63).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)


def vtr_drv3_017_volume_trend_break_jerk(volume: pd.Series) -> pd.Series:
    def _proj_ratio(y):
        if len(y) < 10: return 1.0
        res = linregress(np.arange(len(y)-1), y[:-1])
        proj = res.intercept + res.slope * (len(y)-1)
        return _safe_div(pd.Series(y[-1]), pd.Series(proj)).iloc[0]
    rat = volume.rolling(21).apply(_proj_ratio, raw=True)
    vel = rat.diff(5)
    return vel.diff(5)


def vtr_drv3_018_volume_drift_efficiency_jerk(volume: pd.Series) -> pd.Series:
    net_s = volume.diff(63)
    path_len = volume.diff().abs().rolling(63).sum()
    eff = _safe_div(net_s, path_len)
    vel = eff.diff(5)
    return vel.diff(5)


def vtr_drv3_019_mktcap_obv_slope_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _safe_div(_rolling_slope(obv, 63), obv.abs().rolling(63).mean() + _EPS)
    vel = os.diff(5)
    return vel.diff(5)


def vtr_drv3_020_volume_trend_convexity_jerk(volume: pd.Series) -> pd.Series:
    vi = volume.cumsum()
    s = _rolling_slope(volume, 252)
    tri = 0.5 * s * (252**2)
    conv = _safe_div(vi.diff(252), tri + _EPS)
    vel = conv.diff(5)
    return vel.diff(5)


def vtr_drv3_021_volume_trend_entropy_jerk(volume: pd.Series) -> pd.Series:
    s = _rolling_slope(volume, 5)
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y[~np.isnan(y)], bins=5, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    e = s.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def vtr_drv3_022_final_vtr_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vtr_075_volume_trend_final_composite(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vtr_drv3_023_turnover_trend_slope_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    s = _safe_div(_rolling_slope(to, 252), _rolling_mean(to, 252) + _EPS)
    vel = s.diff(5)
    return vel.diff(5)


def vtr_drv3_024_volume_ema_slope_jerk(volume: pd.Series) -> pd.Series:
    v_ema = volume.ewm(span=21).mean()
    s = _safe_div(_rolling_slope(v_ema, 21), v_ema + _EPS)
    vel = s.diff(5)
    return vel.diff(5)


def vtr_drv3_025_consecutive_volume_inc_ma_jerk(volume: pd.Series) -> pd.Series:
    vma = volume.rolling(21).mean()
    inc = (vma > vma.shift(1)).astype(int)
    streak = inc.groupby((inc == 0).cumsum()).cumsum()
    vel = streak.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V19_A_REGISTRY = {
    "vtr_drv3_001_volume_slope_21d_jerk": {"inputs": ["volume"], "func": vtr_drv3_001_volume_slope_21d_jerk},
    "vtr_drv3_002_volume_slope_63d_jerk": {"inputs": ["volume"], "func": vtr_drv3_002_volume_slope_63d_jerk},
    "vtr_drv3_003_volume_rsq_63d_jerk": {"inputs": ["volume"], "func": vtr_drv3_003_volume_rsq_63d_jerk},
    "vtr_drv3_004_volume_ma_cross_jerk": {"inputs": ["volume"], "func": vtr_drv3_004_volume_ma_cross_jerk},
    "vtr_drv3_005_volume_price_divergence_jerk": {"inputs": ["close", "volume"], "func": vtr_drv3_005_volume_price_divergence_jerk},
    "vtr_drv3_006_obv_slope_jerk": {"inputs": ["close", "volume"], "func": vtr_drv3_006_obv_slope_jerk},
    "vtr_drv3_007_chaikin_ad_slope_jerk": {"inputs": ["volume", "high", "low", "close"], "func": vtr_drv3_007_chaikin_ad_slope_jerk},
    "vtr_drv3_008_volume_trend_climax_jerk": {"inputs": ["volume"], "func": vtr_drv3_008_volume_trend_climax_jerk},
    "vtr_drv3_009_volume_trend_accel_jerk": {"inputs": ["volume"], "func": vtr_drv3_009_volume_trend_accel_jerk},
    "vtr_drv3_010_mktcap_volume_trend_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vtr_drv3_010_mktcap_volume_trend_jerk},
    "vtr_drv3_011_volume_trend_se_jerk": {"inputs": ["volume"], "func": vtr_drv3_011_volume_trend_se_jerk},
    "vtr_drv3_012_accumulation_climax_velocity_jerk": {"inputs": ["close", "volume"], "func": vtr_drv3_012_accumulation_climax_velocity_jerk},
    "vtr_drv3_013_volume_log_trend_velocity_jerk": {"inputs": ["volume"], "func": vtr_drv3_013_volume_log_trend_velocity_jerk},
    "vtr_drv3_014_volume_drift_zscore_jerk": {"inputs": ["volume"], "func": vtr_drv3_014_volume_drift_zscore_jerk},
    "vtr_drv3_015_volume_slope_rank_jerk": {"inputs": ["volume"], "func": vtr_drv3_015_volume_slope_rank_jerk},
    "vtr_drv3_016_obv_trend_stability_jerk": {"inputs": ["close", "volume"], "func": vtr_drv3_016_obv_trend_stability_jerk},
    "vtr_drv3_017_volume_trend_break_jerk": {"inputs": ["volume"], "func": vtr_drv3_017_volume_trend_break_jerk},
    "vtr_drv3_018_volume_drift_efficiency_jerk": {"inputs": ["volume"], "func": vtr_drv3_018_volume_drift_efficiency_jerk},
    "vtr_drv3_019_mktcap_obv_slope_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vtr_drv3_019_mktcap_obv_slope_jerk},
    "vtr_drv3_020_volume_trend_convexity_jerk": {"inputs": ["volume"], "func": vtr_drv3_020_volume_trend_convexity_jerk},
    "vtr_drv3_021_volume_trend_entropy_jerk": {"inputs": ["volume"], "func": vtr_drv3_021_volume_trend_entropy_jerk},
    "vtr_drv3_022_final_vtr_composite_jerk": {"inputs": ["close", "volume"], "func": vtr_drv3_022_final_vtr_composite_jerk},
    "vtr_drv3_023_turnover_trend_slope_jerk": {"inputs": ["volume", "sharesbas"], "func": vtr_drv3_023_turnover_trend_slope_jerk},
    "vtr_drv3_024_volume_ema_slope_jerk": {"inputs": ["volume"], "func": vtr_drv3_024_volume_ema_slope_jerk},
    "vtr_drv3_025_consecutive_volume_inc_ma_jerk": {"inputs": ["volume"], "func": vtr_drv3_025_consecutive_volume_inc_ma_jerk},
}
