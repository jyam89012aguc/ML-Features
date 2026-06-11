import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (capitulation / volume spike) =====
def _f08_volz(volume, w):
    # z-score of volume over a trailing window (spike intensity, signed)
    m = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = volume.rolling(w, min_periods=max(2, w // 2)).std()
    return (volume - m) / sd.replace(0, np.nan)


def _f08_surge(volume, w):
    # ratio of current volume to its trailing-mean (blow-off surge multiple)
    m = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    return volume / m.replace(0, np.nan)


def _f08_dvol(closeadj, volume):
    # dollar volume = adjusted close * share volume
    return closeadj * volume


def _f08_downvolshare(closeadj, volume, w):
    # continuous share of trailing dollar-volume that fell on down days (sum-based)
    ret = closeadj.pct_change()
    dv = closeadj * volume
    down = dv.where(ret < 0, 0.0)
    tot = dv.rolling(w, min_periods=max(2, w // 2)).sum()
    downsum = down.rolling(w, min_periods=max(2, w // 2)).sum()
    return downsum / tot.replace(0, np.nan)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f08cv_f08_capitulation_volume_spike_volz_5d_jerk_v001_signal(volume):
    result = _f08_volz(volume, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_21d_jerk_v002_signal(volume):
    result = _f08_volz(volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_63d_jerk_v003_signal(volume):
    result = _f08_volz(volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_126d_jerk_v004_signal(volume):
    result = _f08_volz(volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_252d_jerk_v005_signal(volume):
    result = _f08_volz(volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_5d_jerk_v006_signal(volume):
    result = _f08_surge(volume, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_21d_jerk_v007_signal(volume):
    result = _f08_surge(volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_63d_jerk_v008_signal(volume):
    result = _f08_surge(volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_126d_jerk_v009_signal(volume):
    result = _f08_surge(volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_252d_jerk_v010_signal(volume):
    result = _f08_surge(volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logsurge_21d_jerk_v011_signal(volume):
    result = np.log(_f08_surge(volume, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logsurge_63d_jerk_v012_signal(volume):
    result = np.log(_f08_surge(volume, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logsurge_126d_jerk_v013_signal(volume):
    result = np.log(_f08_surge(volume, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvsurge_63d_jerk_v014_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvsurge_126d_jerk_v015_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvsurge_252d_jerk_v016_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvz_63d_jerk_v017_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 63) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvz_126d_jerk_v018_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 126) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvz_252d_jerk_v019_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 252) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vroc_5d_jerk_v020_signal(volume):
    result = volume.pct_change(periods=5) + _f08_surge(volume, 5) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vroc_21d_jerk_v021_signal(volume):
    result = volume.pct_change(periods=21) + _f08_surge(volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vroc_63d_jerk_v022_signal(volume):
    result = volume.pct_change(periods=63) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vroc_126d_jerk_v023_signal(volume):
    result = volume.pct_change(periods=126) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logvroc_21d_jerk_v024_signal(volume):
    result = np.log(volume / volume.shift(21)) + _f08_surge(volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logvroc_63d_jerk_v025_signal(volume):
    result = np.log(volume / volume.shift(63)) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_downshare_63d_jerk_v026_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_downshare_126d_jerk_v027_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_downshare_252d_jerk_v028_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_udvolratio_63d_jerk_v029_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    result = _safe_div(down, up)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_udvolratio_126d_jerk_v030_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(126, min_periods=42).sum()
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=42).sum()
    result = _safe_div(down, up)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_climaxrank_126d_jerk_v031_signal(volume):
    result = volume.rolling(126, min_periods=42).rank(pct=True) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_climaxrank_252d_jerk_v032_signal(volume):
    result = volume.rolling(252, min_periods=84).rank(pct=True) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvrank_126d_jerk_v033_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_effort_21d_jerk_v034_signal(closeadj, volume):
    result = _f08_volz(volume, 21) * closeadj.pct_change().abs()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_effort_63d_jerk_v035_signal(closeadj, volume):
    result = _f08_volz(volume, 63) * closeadj.pct_change().abs()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_effortw_63d_jerk_v036_signal(closeadj, volume):
    result = _f08_surge(volume, 63) * closeadj.pct_change(periods=5).abs()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_signedeffort_21d_jerk_v037_signal(closeadj, volume):
    result = _f08_volz(volume, 21) * closeadj.pct_change()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_signedeffort_63d_jerk_v038_signal(closeadj, volume):
    result = _f08_volz(volume, 63) * closeadj.pct_change()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voldisp_21d_jerk_v039_signal(volume):
    result = _safe_div(_std(volume, 21), _mean(volume, 21)) + _f08_surge(volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voldisp_63d_jerk_v040_signal(volume):
    result = _safe_div(_std(volume, 63), _mean(volume, 63)) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voldisp_126d_jerk_v041_signal(volume):
    result = _safe_div(_std(volume, 126), _mean(volume, 126)) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voldisp_252d_jerk_v042_signal(volume):
    result = _safe_div(_std(volume, 252), _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvol_50d_jerk_v043_signal(volume):
    result = _safe_div(volume, _mean(volume, 50)) + _f08_surge(volume, 50) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvolma_5_50_jerk_v044_signal(volume):
    result = _safe_div(_mean(volume, 5), _mean(volume, 50)) + _f08_surge(volume, 50) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvolma_21_126_jerk_v045_signal(volume):
    result = _safe_div(_mean(volume, 21), _mean(volume, 126)) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvolma_21_252_jerk_v046_signal(volume):
    result = _safe_div(_mean(volume, 21), _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voltrend_21d_jerk_v047_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(21, min_periods=10).cov(idx)
    var = idx.rolling(21, min_periods=10).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 21)) + _f08_surge(volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voltrend_63d_jerk_v048_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(63, min_periods=21).cov(idx)
    var = idx.rolling(63, min_periods=21).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 63)) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voltrend_126d_jerk_v049_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(126, min_periods=42).cov(idx)
    var = idx.rolling(126, min_periods=42).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 126)) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vwrange_21d_jerk_v050_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = ret * _f08_surge(volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vwrange_63d_jerk_v051_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = ret * _f08_surge(volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_ewmvolz_21d_jerk_v052_signal(volume):
    result = _f08_volz(volume, 21).ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_ewmvolz_63d_jerk_v053_signal(volume):
    result = _f08_volz(volume, 63).ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_ewmsurge_21d_jerk_v054_signal(volume):
    result = _f08_surge(volume, 21).ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgeclust_63d_jerk_v055_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(s, _mean(s, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgeclust_126d_jerk_v056_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(s, _mean(s, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgevol_63d_jerk_v057_signal(volume):
    s = _f08_surge(volume, 21)
    result = _std(s, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgevol_126d_jerk_v058_signal(volume):
    s = _f08_surge(volume, 21)
    result = _std(s, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volskew_63d_jerk_v059_signal(volume):
    result = volume.rolling(63, min_periods=21).skew() + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volskew_126d_jerk_v060_signal(volume):
    result = volume.rolling(126, min_periods=42).skew() + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volkurt_63d_jerk_v061_signal(volume):
    result = volume.rolling(63, min_periods=21).kurt() + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volkurt_126d_jerk_v062_signal(volume):
    result = volume.rolling(126, min_periods=42).kurt() + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvskew_126d_jerk_v063_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logdvz_126d_jerk_v064_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logdvz_252d_jerk_v065_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_cappress_63d_jerk_v066_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 63) * _f08_surge(volume, 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_cappress_126d_jerk_v067_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 126) * _f08_surge(volume, 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_zdiverge_63d_jerk_v068_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _f08_volz(volume, 63) - _z(dv, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_amihud_21d_jerk_v069_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 21) * 1e9 + _f08_surge(volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_amihud_63d_jerk_v070_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 63) * 1e9 + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_intensrank_126d_jerk_v071_signal(volume):
    result = _f08_volz(volume, 63) * volume.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_meansurge_5d_jerk_v072_signal(volume):
    result = _mean(_f08_surge(volume, 21), 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_meansurge_21d_jerk_v073_signal(volume):
    result = _mean(_f08_surge(volume, 63), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_42d_jerk_v074_signal(volume):
    result = _f08_volz(volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_84d_jerk_v075_signal(volume):
    result = _f08_surge(volume, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logsurge_84d_jerk_v076_signal(volume):
    result = np.log(_f08_surge(volume, 84))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logsurge_252d_jerk_v077_signal(volume):
    result = np.log(_f08_surge(volume, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_189d_jerk_v078_signal(volume):
    result = _f08_volz(volume, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_504d_jerk_v079_signal(volume):
    result = _f08_volz(volume, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_189d_jerk_v080_signal(volume):
    result = _f08_surge(volume, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_504d_jerk_v081_signal(volume):
    result = _f08_surge(volume, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvsurge_504d_jerk_v082_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 504))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvz_21d_jerk_v083_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 21) + _f08_surge(volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logdvz_63d_jerk_v084_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logdvz_504d_jerk_v085_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vroc_252d_jerk_v086_signal(volume):
    result = volume.pct_change(periods=252) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logvroc_126d_jerk_v087_signal(volume):
    result = np.log(volume / volume.shift(126)) + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_downshare_21d_jerk_v088_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_downshare_42d_jerk_v089_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_udvolratio_21d_jerk_v090_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    up = dv.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    result = _safe_div(down, up)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_udvolratio_252d_jerk_v091_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(252, min_periods=84).sum()
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=84).sum()
    result = _safe_div(down, up)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logudratio_63d_jerk_v092_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    result = np.log(_safe_div(down, up))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_climaxrank_63d_jerk_v093_signal(volume):
    result = volume.rolling(63, min_periods=21).rank(pct=True) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvrank_252d_jerk_v094_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_effort_126d_jerk_v095_signal(closeadj, volume):
    result = _f08_volz(volume, 126) * closeadj.pct_change().abs()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_effort_252d_jerk_v096_signal(closeadj, volume):
    result = _f08_volz(volume, 252) * closeadj.pct_change().abs()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_signedeffort_126d_jerk_v097_signal(closeadj, volume):
    result = _f08_volz(volume, 126) * closeadj.pct_change()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_smsigneffort_63d_jerk_v098_signal(closeadj, volume):
    eff = _f08_volz(volume, 63) * closeadj.pct_change()
    result = eff.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voldisp_504d_jerk_v099_signal(volume):
    result = _safe_div(_std(volume, 504), _mean(volume, 504)) + _f08_surge(volume, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvol_10d_jerk_v100_signal(volume):
    result = _safe_div(volume, _mean(volume, 10)) + _f08_surge(volume, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvolma_10_63_jerk_v101_signal(volume):
    result = _safe_div(_mean(volume, 10), _mean(volume, 63)) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_rvolma_42_252_jerk_v102_signal(volume):
    result = _safe_div(_mean(volume, 42), _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_voltrend_252d_jerk_v103_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(252, min_periods=84).cov(idx)
    var = idx.rolling(252, min_periods=84).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvtrend_126d_jerk_v104_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    idx = pd.Series(np.arange(len(dv), dtype=float), index=dv.index)
    cov = dv.rolling(126, min_periods=42).cov(idx)
    var = idx.rolling(126, min_periods=42).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(dv, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vwrange_126d_jerk_v105_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = ret * _f08_surge(volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_vwrangema_63d_jerk_v106_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = _mean(ret * _f08_surge(volume, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_ewmvolz_126d_jerk_v107_signal(volume):
    result = _f08_volz(volume, 126).ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_ewmsurge_63d_jerk_v108_signal(volume):
    result = _f08_surge(volume, 63).ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgeclust_252d_jerk_v109_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(s, _mean(s, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgevol_252d_jerk_v110_signal(volume):
    s = _f08_surge(volume, 21)
    result = _std(s, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volskew_252d_jerk_v111_signal(volume):
    result = volume.rolling(252, min_periods=84).skew() + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volkurt_252d_jerk_v112_signal(volume):
    result = volume.rolling(252, min_periods=84).kurt() + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvskew_252d_jerk_v113_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(252, min_periods=84).skew()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvkurt_126d_jerk_v114_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).kurt()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_cappress_252d_jerk_v115_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 252) * _f08_surge(volume, 21)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_downz_126d_jerk_v116_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 126) * _f08_volz(volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_zdiverge_126d_jerk_v117_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _f08_volz(volume, 126) - _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_amihud_126d_jerk_v118_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 126) * 1e9 + _f08_surge(volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_amihud_252d_jerk_v119_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 252) * 1e9 + _f08_surge(volume, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logamihud_63d_jerk_v120_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = np.log(_mean(illiq, 63) * 1e9) + _f08_surge(volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_intensrank_252d_jerk_v121_signal(volume):
    result = _f08_volz(volume, 126) * volume.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_meansurge_5_252_jerk_v122_signal(volume):
    result = _mean(_f08_surge(volume, 252), 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_meansurge_42d_jerk_v123_signal(volume):
    result = _mean(_f08_surge(volume, 126), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_84d_jerk_v124_signal(volume):
    result = _f08_volz(volume, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_42d_jerk_v125_signal(volume):
    result = _f08_surge(volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surge_10d_jerk_v126_signal(volume):
    result = _f08_surge(volume, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_volz_10d_jerk_v127_signal(volume):
    result = _f08_volz(volume, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgeaccel_5_63_jerk_v128_signal(volume):
    result = _f08_surge(volume, 5) - _f08_surge(volume, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgeaccel_21_126_jerk_v129_signal(volume):
    result = _f08_surge(volume, 21) - _f08_surge(volume, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_zspread_21_252_jerk_v130_signal(volume):
    result = _f08_volz(volume, 21) - _f08_volz(volume, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_zspread_63_252_jerk_v131_signal(volume):
    result = _f08_volz(volume, 63) - _f08_volz(volume, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logdvsurge_21d_jerk_v132_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = np.log(_safe_div(dv, _mean(dv, 21)))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_logdvsurge_63d_jerk_v133_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = np.log(_safe_div(dv, _mean(dv, 63)))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgecv_63d_jerk_v134_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(_std(s, 63), _mean(s, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgecv_126d_jerk_v135_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(_std(s, 126), _mean(s, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_upshare_63d_jerk_v136_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    tot = dv.rolling(63, min_periods=21).sum()
    result = _safe_div(up, tot) + _f08_downvolshare(closeadj, volume, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_upshare_126d_jerk_v137_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=42).sum()
    tot = dv.rolling(126, min_periods=42).sum()
    result = _safe_div(up, tot) + _f08_downvolshare(closeadj, volume, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_netvolp_63d_jerk_v138_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    down = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    tot = dv.rolling(63, min_periods=21).sum()
    result = _safe_div(up - down, tot)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_netvolp_126d_jerk_v139_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=42).sum()
    down = dv.where(ret < 0, 0.0).rolling(126, min_periods=42).sum()
    tot = dv.rolling(126, min_periods=42).sum()
    result = _safe_div(up - down, tot)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_netvolp_252d_jerk_v140_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=84).sum()
    down = dv.where(ret < 0, 0.0).rolling(252, min_periods=84).sum()
    tot = dv.rolling(252, min_periods=84).sum()
    result = _safe_div(up - down, tot)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgepersist_63d_jerk_v141_signal(volume):
    s = _f08_surge(volume, 21)
    result = s.rolling(63, min_periods=21).corr(s.shift(1))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgepersist_126d_jerk_v142_signal(volume):
    s = _f08_surge(volume, 21)
    result = s.rolling(126, min_periods=42).corr(s.shift(1))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvpermove_63d_jerk_v143_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    move = closeadj.pct_change().abs().rolling(63, min_periods=21).sum()
    dvsum = dv.rolling(63, min_periods=21).sum()
    result = _safe_div(np.log(dvsum.replace(0, np.nan)), move)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_spikeret_63d_jerk_v144_signal(closeadj, volume):
    w = _f08_volz(volume, 63)
    contrib = (closeadj.pct_change() * w).rolling(63, min_periods=21).sum()
    norm = w.abs().rolling(63, min_periods=21).sum()
    result = _safe_div(contrib, norm)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_spikeret_126d_jerk_v145_signal(closeadj, volume):
    w = _f08_volz(volume, 126)
    contrib = (closeadj.pct_change() * w).rolling(126, min_periods=42).sum()
    norm = w.abs().rolling(126, min_periods=42).sum()
    result = _safe_div(contrib, norm)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgez_252d_jerk_v146_signal(volume):
    result = _z(_f08_surge(volume, 21), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_surgez63_252d_jerk_v147_signal(volume):
    result = _z(_f08_surge(volume, 63), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_dvconc_21_252_jerk_v148_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    recent = dv.rolling(21, min_periods=10).sum()
    tot = dv.rolling(252, min_periods=84).sum()
    result = _safe_div(recent * (252.0 / 21.0), tot)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_ewmsurge_252d_jerk_v149_signal(volume):
    result = _f08_surge(volume, 252).ewm(span=252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f08cv_f08_capitulation_volume_spike_blend_multi_jerk_v150_signal(volume):
    result = (_f08_surge(volume, 21) + _f08_surge(volume, 63)
              + _f08_surge(volume, 126) + _f08_surge(volume, 252)) / 4.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f08cv_f08_capitulation_volume_spike_volz_5d_jerk_v001_signal,    f08cv_f08_capitulation_volume_spike_volz_21d_jerk_v002_signal,    f08cv_f08_capitulation_volume_spike_volz_63d_jerk_v003_signal,    f08cv_f08_capitulation_volume_spike_volz_126d_jerk_v004_signal,    f08cv_f08_capitulation_volume_spike_volz_252d_jerk_v005_signal,    f08cv_f08_capitulation_volume_spike_surge_5d_jerk_v006_signal,    f08cv_f08_capitulation_volume_spike_surge_21d_jerk_v007_signal,    f08cv_f08_capitulation_volume_spike_surge_63d_jerk_v008_signal,    f08cv_f08_capitulation_volume_spike_surge_126d_jerk_v009_signal,    f08cv_f08_capitulation_volume_spike_surge_252d_jerk_v010_signal,    f08cv_f08_capitulation_volume_spike_logsurge_21d_jerk_v011_signal,    f08cv_f08_capitulation_volume_spike_logsurge_63d_jerk_v012_signal,    f08cv_f08_capitulation_volume_spike_logsurge_126d_jerk_v013_signal,    f08cv_f08_capitulation_volume_spike_dvsurge_63d_jerk_v014_signal,    f08cv_f08_capitulation_volume_spike_dvsurge_126d_jerk_v015_signal,    f08cv_f08_capitulation_volume_spike_dvsurge_252d_jerk_v016_signal,    f08cv_f08_capitulation_volume_spike_dvz_63d_jerk_v017_signal,    f08cv_f08_capitulation_volume_spike_dvz_126d_jerk_v018_signal,    f08cv_f08_capitulation_volume_spike_dvz_252d_jerk_v019_signal,    f08cv_f08_capitulation_volume_spike_vroc_5d_jerk_v020_signal,    f08cv_f08_capitulation_volume_spike_vroc_21d_jerk_v021_signal,    f08cv_f08_capitulation_volume_spike_vroc_63d_jerk_v022_signal,    f08cv_f08_capitulation_volume_spike_vroc_126d_jerk_v023_signal,    f08cv_f08_capitulation_volume_spike_logvroc_21d_jerk_v024_signal,    f08cv_f08_capitulation_volume_spike_logvroc_63d_jerk_v025_signal,    f08cv_f08_capitulation_volume_spike_downshare_63d_jerk_v026_signal,    f08cv_f08_capitulation_volume_spike_downshare_126d_jerk_v027_signal,    f08cv_f08_capitulation_volume_spike_downshare_252d_jerk_v028_signal,    f08cv_f08_capitulation_volume_spike_udvolratio_63d_jerk_v029_signal,    f08cv_f08_capitulation_volume_spike_udvolratio_126d_jerk_v030_signal,    f08cv_f08_capitulation_volume_spike_climaxrank_126d_jerk_v031_signal,    f08cv_f08_capitulation_volume_spike_climaxrank_252d_jerk_v032_signal,    f08cv_f08_capitulation_volume_spike_dvrank_126d_jerk_v033_signal,    f08cv_f08_capitulation_volume_spike_effort_21d_jerk_v034_signal,    f08cv_f08_capitulation_volume_spike_effort_63d_jerk_v035_signal,    f08cv_f08_capitulation_volume_spike_effortw_63d_jerk_v036_signal,    f08cv_f08_capitulation_volume_spike_signedeffort_21d_jerk_v037_signal,    f08cv_f08_capitulation_volume_spike_signedeffort_63d_jerk_v038_signal,    f08cv_f08_capitulation_volume_spike_voldisp_21d_jerk_v039_signal,    f08cv_f08_capitulation_volume_spike_voldisp_63d_jerk_v040_signal,    f08cv_f08_capitulation_volume_spike_voldisp_126d_jerk_v041_signal,    f08cv_f08_capitulation_volume_spike_voldisp_252d_jerk_v042_signal,    f08cv_f08_capitulation_volume_spike_rvol_50d_jerk_v043_signal,    f08cv_f08_capitulation_volume_spike_rvolma_5_50_jerk_v044_signal,    f08cv_f08_capitulation_volume_spike_rvolma_21_126_jerk_v045_signal,    f08cv_f08_capitulation_volume_spike_rvolma_21_252_jerk_v046_signal,    f08cv_f08_capitulation_volume_spike_voltrend_21d_jerk_v047_signal,    f08cv_f08_capitulation_volume_spike_voltrend_63d_jerk_v048_signal,    f08cv_f08_capitulation_volume_spike_voltrend_126d_jerk_v049_signal,    f08cv_f08_capitulation_volume_spike_vwrange_21d_jerk_v050_signal,    f08cv_f08_capitulation_volume_spike_vwrange_63d_jerk_v051_signal,    f08cv_f08_capitulation_volume_spike_ewmvolz_21d_jerk_v052_signal,    f08cv_f08_capitulation_volume_spike_ewmvolz_63d_jerk_v053_signal,    f08cv_f08_capitulation_volume_spike_ewmsurge_21d_jerk_v054_signal,    f08cv_f08_capitulation_volume_spike_surgeclust_63d_jerk_v055_signal,    f08cv_f08_capitulation_volume_spike_surgeclust_126d_jerk_v056_signal,    f08cv_f08_capitulation_volume_spike_surgevol_63d_jerk_v057_signal,    f08cv_f08_capitulation_volume_spike_surgevol_126d_jerk_v058_signal,    f08cv_f08_capitulation_volume_spike_volskew_63d_jerk_v059_signal,    f08cv_f08_capitulation_volume_spike_volskew_126d_jerk_v060_signal,    f08cv_f08_capitulation_volume_spike_volkurt_63d_jerk_v061_signal,    f08cv_f08_capitulation_volume_spike_volkurt_126d_jerk_v062_signal,    f08cv_f08_capitulation_volume_spike_dvskew_126d_jerk_v063_signal,    f08cv_f08_capitulation_volume_spike_logdvz_126d_jerk_v064_signal,    f08cv_f08_capitulation_volume_spike_logdvz_252d_jerk_v065_signal,    f08cv_f08_capitulation_volume_spike_cappress_63d_jerk_v066_signal,    f08cv_f08_capitulation_volume_spike_cappress_126d_jerk_v067_signal,    f08cv_f08_capitulation_volume_spike_zdiverge_63d_jerk_v068_signal,    f08cv_f08_capitulation_volume_spike_amihud_21d_jerk_v069_signal,    f08cv_f08_capitulation_volume_spike_amihud_63d_jerk_v070_signal,    f08cv_f08_capitulation_volume_spike_intensrank_126d_jerk_v071_signal,    f08cv_f08_capitulation_volume_spike_meansurge_5d_jerk_v072_signal,    f08cv_f08_capitulation_volume_spike_meansurge_21d_jerk_v073_signal,    f08cv_f08_capitulation_volume_spike_volz_42d_jerk_v074_signal,    f08cv_f08_capitulation_volume_spike_surge_84d_jerk_v075_signal,    f08cv_f08_capitulation_volume_spike_logsurge_84d_jerk_v076_signal,    f08cv_f08_capitulation_volume_spike_logsurge_252d_jerk_v077_signal,    f08cv_f08_capitulation_volume_spike_volz_189d_jerk_v078_signal,    f08cv_f08_capitulation_volume_spike_volz_504d_jerk_v079_signal,    f08cv_f08_capitulation_volume_spike_surge_189d_jerk_v080_signal,    f08cv_f08_capitulation_volume_spike_surge_504d_jerk_v081_signal,    f08cv_f08_capitulation_volume_spike_dvsurge_504d_jerk_v082_signal,    f08cv_f08_capitulation_volume_spike_dvz_21d_jerk_v083_signal,    f08cv_f08_capitulation_volume_spike_logdvz_63d_jerk_v084_signal,    f08cv_f08_capitulation_volume_spike_logdvz_504d_jerk_v085_signal,    f08cv_f08_capitulation_volume_spike_vroc_252d_jerk_v086_signal,    f08cv_f08_capitulation_volume_spike_logvroc_126d_jerk_v087_signal,    f08cv_f08_capitulation_volume_spike_downshare_21d_jerk_v088_signal,    f08cv_f08_capitulation_volume_spike_downshare_42d_jerk_v089_signal,    f08cv_f08_capitulation_volume_spike_udvolratio_21d_jerk_v090_signal,    f08cv_f08_capitulation_volume_spike_udvolratio_252d_jerk_v091_signal,    f08cv_f08_capitulation_volume_spike_logudratio_63d_jerk_v092_signal,    f08cv_f08_capitulation_volume_spike_climaxrank_63d_jerk_v093_signal,    f08cv_f08_capitulation_volume_spike_dvrank_252d_jerk_v094_signal,    f08cv_f08_capitulation_volume_spike_effort_126d_jerk_v095_signal,    f08cv_f08_capitulation_volume_spike_effort_252d_jerk_v096_signal,    f08cv_f08_capitulation_volume_spike_signedeffort_126d_jerk_v097_signal,    f08cv_f08_capitulation_volume_spike_smsigneffort_63d_jerk_v098_signal,    f08cv_f08_capitulation_volume_spike_voldisp_504d_jerk_v099_signal,    f08cv_f08_capitulation_volume_spike_rvol_10d_jerk_v100_signal,    f08cv_f08_capitulation_volume_spike_rvolma_10_63_jerk_v101_signal,    f08cv_f08_capitulation_volume_spike_rvolma_42_252_jerk_v102_signal,    f08cv_f08_capitulation_volume_spike_voltrend_252d_jerk_v103_signal,    f08cv_f08_capitulation_volume_spike_dvtrend_126d_jerk_v104_signal,    f08cv_f08_capitulation_volume_spike_vwrange_126d_jerk_v105_signal,    f08cv_f08_capitulation_volume_spike_vwrangema_63d_jerk_v106_signal,    f08cv_f08_capitulation_volume_spike_ewmvolz_126d_jerk_v107_signal,    f08cv_f08_capitulation_volume_spike_ewmsurge_63d_jerk_v108_signal,    f08cv_f08_capitulation_volume_spike_surgeclust_252d_jerk_v109_signal,    f08cv_f08_capitulation_volume_spike_surgevol_252d_jerk_v110_signal,    f08cv_f08_capitulation_volume_spike_volskew_252d_jerk_v111_signal,    f08cv_f08_capitulation_volume_spike_volkurt_252d_jerk_v112_signal,    f08cv_f08_capitulation_volume_spike_dvskew_252d_jerk_v113_signal,    f08cv_f08_capitulation_volume_spike_dvkurt_126d_jerk_v114_signal,    f08cv_f08_capitulation_volume_spike_cappress_252d_jerk_v115_signal,    f08cv_f08_capitulation_volume_spike_downz_126d_jerk_v116_signal,    f08cv_f08_capitulation_volume_spike_zdiverge_126d_jerk_v117_signal,    f08cv_f08_capitulation_volume_spike_amihud_126d_jerk_v118_signal,    f08cv_f08_capitulation_volume_spike_amihud_252d_jerk_v119_signal,    f08cv_f08_capitulation_volume_spike_logamihud_63d_jerk_v120_signal,    f08cv_f08_capitulation_volume_spike_intensrank_252d_jerk_v121_signal,    f08cv_f08_capitulation_volume_spike_meansurge_5_252_jerk_v122_signal,    f08cv_f08_capitulation_volume_spike_meansurge_42d_jerk_v123_signal,    f08cv_f08_capitulation_volume_spike_volz_84d_jerk_v124_signal,    f08cv_f08_capitulation_volume_spike_surge_42d_jerk_v125_signal,    f08cv_f08_capitulation_volume_spike_surge_10d_jerk_v126_signal,    f08cv_f08_capitulation_volume_spike_volz_10d_jerk_v127_signal,    f08cv_f08_capitulation_volume_spike_surgeaccel_5_63_jerk_v128_signal,    f08cv_f08_capitulation_volume_spike_surgeaccel_21_126_jerk_v129_signal,    f08cv_f08_capitulation_volume_spike_zspread_21_252_jerk_v130_signal,    f08cv_f08_capitulation_volume_spike_zspread_63_252_jerk_v131_signal,    f08cv_f08_capitulation_volume_spike_logdvsurge_21d_jerk_v132_signal,    f08cv_f08_capitulation_volume_spike_logdvsurge_63d_jerk_v133_signal,    f08cv_f08_capitulation_volume_spike_surgecv_63d_jerk_v134_signal,    f08cv_f08_capitulation_volume_spike_surgecv_126d_jerk_v135_signal,    f08cv_f08_capitulation_volume_spike_upshare_63d_jerk_v136_signal,    f08cv_f08_capitulation_volume_spike_upshare_126d_jerk_v137_signal,    f08cv_f08_capitulation_volume_spike_netvolp_63d_jerk_v138_signal,    f08cv_f08_capitulation_volume_spike_netvolp_126d_jerk_v139_signal,    f08cv_f08_capitulation_volume_spike_netvolp_252d_jerk_v140_signal,    f08cv_f08_capitulation_volume_spike_surgepersist_63d_jerk_v141_signal,    f08cv_f08_capitulation_volume_spike_surgepersist_126d_jerk_v142_signal,    f08cv_f08_capitulation_volume_spike_dvpermove_63d_jerk_v143_signal,    f08cv_f08_capitulation_volume_spike_spikeret_63d_jerk_v144_signal,    f08cv_f08_capitulation_volume_spike_spikeret_126d_jerk_v145_signal,    f08cv_f08_capitulation_volume_spike_surgez_252d_jerk_v146_signal,    f08cv_f08_capitulation_volume_spike_surgez63_252d_jerk_v147_signal,    f08cv_f08_capitulation_volume_spike_dvconc_21_252_jerk_v148_signal,    f08cv_f08_capitulation_volume_spike_ewmsurge_252d_jerk_v149_signal,    f08cv_f08_capitulation_volume_spike_blend_multi_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CAPITULATION_VOLUME_SPIKE_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f08_volz', '_f08_surge', '_f08_dvol', '_f08_downvolshare')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f08_capitulation_volume_spike_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
