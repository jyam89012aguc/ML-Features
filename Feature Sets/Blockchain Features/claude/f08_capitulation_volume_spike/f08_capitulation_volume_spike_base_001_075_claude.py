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


# ============ FEATURES 001-075 ============

# 5d volume z-score (weekly spike intensity)
def f08cv_f08_capitulation_volume_spike_volz_5d_base_v001_signal(volume):
    result = _f08_volz(volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume z-score (monthly spike intensity)
def f08cv_f08_capitulation_volume_spike_volz_21d_base_v002_signal(volume):
    result = _f08_volz(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume z-score (quarterly spike intensity)
def f08cv_f08_capitulation_volume_spike_volz_63d_base_v003_signal(volume):
    result = _f08_volz(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume z-score (half-year spike intensity)
def f08cv_f08_capitulation_volume_spike_volz_126d_base_v004_signal(volume):
    result = _f08_volz(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume z-score (annual spike intensity)
def f08cv_f08_capitulation_volume_spike_volz_252d_base_v005_signal(volume):
    result = _f08_volz(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_5d_base_v006_signal(volume):
    result = _f08_surge(volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_21d_base_v007_signal(volume):
    result = _f08_surge(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_63d_base_v008_signal(volume):
    result = _f08_surge(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_126d_base_v009_signal(volume):
    result = _f08_surge(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_252d_base_v010_signal(volume):
    result = _f08_surge(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log volume surge multiple 21d (compresses blow-off tail)
def f08cv_f08_capitulation_volume_spike_logsurge_21d_base_v011_signal(volume):
    result = np.log(_f08_surge(volume, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# log volume surge multiple 63d
def f08cv_f08_capitulation_volume_spike_logsurge_63d_base_v012_signal(volume):
    result = np.log(_f08_surge(volume, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# log volume surge multiple 126d
def f08cv_f08_capitulation_volume_spike_logsurge_126d_base_v013_signal(volume):
    result = np.log(_f08_surge(volume, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dollar-volume surge vs 63d mean
def f08cv_f08_capitulation_volume_spike_dvsurge_63d_base_v014_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge vs 126d mean
def f08cv_f08_capitulation_volume_spike_dvsurge_126d_base_v015_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge vs 252d mean
def f08cv_f08_capitulation_volume_spike_dvsurge_252d_base_v016_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z-score over 63d
def f08cv_f08_capitulation_volume_spike_dvz_63d_base_v017_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 63) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z-score over 126d
def f08cv_f08_capitulation_volume_spike_dvz_126d_base_v018_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 126) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z-score over 252d
def f08cv_f08_capitulation_volume_spike_dvz_252d_base_v019_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 252) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d volume rate-of-change
def f08cv_f08_capitulation_volume_spike_vroc_5d_base_v020_signal(volume):
    result = volume.pct_change(periods=5) + _f08_surge(volume, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume rate-of-change
def f08cv_f08_capitulation_volume_spike_vroc_21d_base_v021_signal(volume):
    result = volume.pct_change(periods=21) + _f08_surge(volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume rate-of-change
def f08cv_f08_capitulation_volume_spike_vroc_63d_base_v022_signal(volume):
    result = volume.pct_change(periods=63) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume rate-of-change
def f08cv_f08_capitulation_volume_spike_vroc_126d_base_v023_signal(volume):
    result = volume.pct_change(periods=126) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log volume change 21d (smoother thrust)
def f08cv_f08_capitulation_volume_spike_logvroc_21d_base_v024_signal(volume):
    result = np.log(volume / volume.shift(21)) + _f08_surge(volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log volume change 63d
def f08cv_f08_capitulation_volume_spike_logvroc_63d_base_v025_signal(volume):
    result = np.log(volume / volume.shift(63)) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down-day dollar-volume share (capitulation tilt)
def f08cv_f08_capitulation_volume_spike_downshare_63d_base_v026_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d down-day dollar-volume share
def f08cv_f08_capitulation_volume_spike_downshare_126d_base_v027_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down-day dollar-volume share
def f08cv_f08_capitulation_volume_spike_downshare_252d_base_v028_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# down-vs-up volume ratio 63d (continuous sum-based, capitulation skew)
def f08cv_f08_capitulation_volume_spike_udvolratio_63d_base_v029_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    result = _safe_div(down, up)
    return result.replace([np.inf, -np.inf], np.nan)


# down-vs-up volume ratio 126d
def f08cv_f08_capitulation_volume_spike_udvolratio_126d_base_v030_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(126, min_periods=42).sum()
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=42).sum()
    result = _safe_div(down, up)
    return result.replace([np.inf, -np.inf], np.nan)


# climax volume percentile rank over 126d (where current volume sits in distribution)
def f08cv_f08_capitulation_volume_spike_climaxrank_126d_base_v031_signal(volume):
    result = volume.rolling(126, min_periods=42).rank(pct=True) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# climax volume percentile rank over 252d
def f08cv_f08_capitulation_volume_spike_climaxrank_252d_base_v032_signal(volume):
    result = volume.rolling(252, min_periods=84).rank(pct=True) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume climax rank over 126d
def f08cv_f08_capitulation_volume_spike_dvrank_126d_base_v033_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# effort: volume z-score times absolute return 21d (force of move)
def f08cv_f08_capitulation_volume_spike_effort_21d_base_v034_signal(closeadj, volume):
    result = _f08_volz(volume, 21) * closeadj.pct_change().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# effort: volume z-score times absolute return 63d
def f08cv_f08_capitulation_volume_spike_effort_63d_base_v035_signal(closeadj, volume):
    result = _f08_volz(volume, 63) * closeadj.pct_change().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# effort: surge multiple times absolute weekly return
def f08cv_f08_capitulation_volume_spike_effortw_63d_base_v036_signal(closeadj, volume):
    result = _f08_surge(volume, 63) * closeadj.pct_change(periods=5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# signed effort: volume z-score times signed return 21d (directional pressure)
def f08cv_f08_capitulation_volume_spike_signedeffort_21d_base_v037_signal(closeadj, volume):
    result = _f08_volz(volume, 21) * closeadj.pct_change()
    return result.replace([np.inf, -np.inf], np.nan)


# signed effort 63d
def f08cv_f08_capitulation_volume_spike_signedeffort_63d_base_v038_signal(closeadj, volume):
    result = _f08_volz(volume, 63) * closeadj.pct_change()
    return result.replace([np.inf, -np.inf], np.nan)


# volume dispersion 21d: rolling std of volume scaled by mean (coefficient of variation)
def f08cv_f08_capitulation_volume_spike_voldisp_21d_base_v039_signal(volume):
    result = _safe_div(_std(volume, 21), _mean(volume, 21)) + _f08_surge(volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume dispersion 63d
def f08cv_f08_capitulation_volume_spike_voldisp_63d_base_v040_signal(volume):
    result = _safe_div(_std(volume, 63), _mean(volume, 63)) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume dispersion 126d
def f08cv_f08_capitulation_volume_spike_voldisp_126d_base_v041_signal(volume):
    result = _safe_div(_std(volume, 126), _mean(volume, 126)) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume dispersion 252d
def f08cv_f08_capitulation_volume_spike_voldisp_252d_base_v042_signal(volume):
    result = _safe_div(_std(volume, 252), _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume vs 50d mean (classic RVOL)
def f08cv_f08_capitulation_volume_spike_rvol_50d_base_v043_signal(volume):
    result = _safe_div(volume, _mean(volume, 50)) + _f08_surge(volume, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume: 5d mean vs 50d mean (short-vs-long activity)
def f08cv_f08_capitulation_volume_spike_rvolma_5_50_base_v044_signal(volume):
    result = _safe_div(_mean(volume, 5), _mean(volume, 50)) + _f08_surge(volume, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume: 21d mean vs 126d mean
def f08cv_f08_capitulation_volume_spike_rvolma_21_126_base_v045_signal(volume):
    result = _safe_div(_mean(volume, 21), _mean(volume, 126)) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume: 21d mean vs 252d mean
def f08cv_f08_capitulation_volume_spike_rvolma_21_252_base_v046_signal(volume):
    result = _safe_div(_mean(volume, 21), _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend slope 21d: normalized linear slope of volume (OLS via covariance)
def f08cv_f08_capitulation_volume_spike_voltrend_21d_base_v047_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(21, min_periods=10).cov(idx)
    var = idx.rolling(21, min_periods=10).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 21)) + _f08_surge(volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend slope 63d
def f08cv_f08_capitulation_volume_spike_voltrend_63d_base_v048_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(63, min_periods=21).cov(idx)
    var = idx.rolling(63, min_periods=21).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 63)) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend slope 126d
def f08cv_f08_capitulation_volume_spike_voltrend_126d_base_v049_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(126, min_periods=42).cov(idx)
    var = idx.rolling(126, min_periods=42).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 126)) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted range 21d: high-low range weighted by volume surge (climax range)
def f08cv_f08_capitulation_volume_spike_vwrange_21d_base_v050_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = ret * _f08_surge(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted range 63d
def f08cv_f08_capitulation_volume_spike_vwrange_63d_base_v051_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = ret * _f08_surge(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA of volume z-score (smoothed spike pressure)
def f08cv_f08_capitulation_volume_spike_ewmvolz_21d_base_v052_signal(volume):
    result = _f08_volz(volume, 21).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA of volume z-score
def f08cv_f08_capitulation_volume_spike_ewmvolz_63d_base_v053_signal(volume):
    result = _f08_volz(volume, 63).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA of surge multiple
def f08cv_f08_capitulation_volume_spike_ewmsurge_21d_base_v054_signal(volume):
    result = _f08_surge(volume, 21).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# max-style surge: current surge vs its own 63d mean (surge clustering)
def f08cv_f08_capitulation_volume_spike_surgeclust_63d_base_v055_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(s, _mean(s, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# surge clustering 126d
def f08cv_f08_capitulation_volume_spike_surgeclust_126d_base_v056_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(s, _mean(s, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of surge multiples 63d (surge volatility / cluster intensity)
def f08cv_f08_capitulation_volume_spike_surgevol_63d_base_v057_signal(volume):
    s = _f08_surge(volume, 21)
    result = _std(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of surge multiples 126d
def f08cv_f08_capitulation_volume_spike_surgevol_126d_base_v058_signal(volume):
    s = _f08_surge(volume, 21)
    result = _std(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling skew of volume (right-tailed = blow-off prone)
def f08cv_f08_capitulation_volume_spike_volskew_63d_base_v059_signal(volume):
    result = volume.rolling(63, min_periods=21).skew() + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling skew of volume
def f08cv_f08_capitulation_volume_spike_volskew_126d_base_v060_signal(volume):
    result = volume.rolling(126, min_periods=42).skew() + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling kurtosis of volume (fat spike tail)
def f08cv_f08_capitulation_volume_spike_volkurt_63d_base_v061_signal(volume):
    result = volume.rolling(63, min_periods=21).kurt() + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling kurtosis of volume
def f08cv_f08_capitulation_volume_spike_volkurt_126d_base_v062_signal(volume):
    result = volume.rolling(126, min_periods=42).kurt() + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of dollar volume skew (capitulation asymmetry) over 126d
def f08cv_f08_capitulation_volume_spike_dvskew_126d_base_v063_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log dollar-volume z-score over 126d (scale-robust dollar spike)
def f08cv_f08_capitulation_volume_spike_logdvz_126d_base_v064_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log dollar-volume z-score over 252d
def f08cv_f08_capitulation_volume_spike_logdvz_252d_base_v065_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation pressure: down-share times surge 63d (heavy down-volume blow-off)
def f08cv_f08_capitulation_volume_spike_cappress_63d_base_v066_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 63) * _f08_surge(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation pressure 126d
def f08cv_f08_capitulation_volume_spike_cappress_126d_base_v067_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 126) * _f08_surge(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume z-score relative to dollar-volume z-score (price vs share spike divergence)
def f08cv_f08_capitulation_volume_spike_zdiverge_63d_base_v068_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _f08_volz(volume, 63) - _z(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud-style illiquidity 21d: abs return per dollar volume (continuous)
def f08cv_f08_capitulation_volume_spike_amihud_21d_base_v069_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 21) * 1e9 + _f08_surge(volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud-style illiquidity 63d
def f08cv_f08_capitulation_volume_spike_amihud_63d_base_v070_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 63) * 1e9 + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume z-score scaled by climax rank (intensity weighted by extremity)
def f08cv_f08_capitulation_volume_spike_intensrank_126d_base_v071_signal(volume):
    result = _f08_volz(volume, 63) * volume.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean surge (smoothed weekly spike)
def f08cv_f08_capitulation_volume_spike_meansurge_5d_base_v072_signal(volume):
    result = _mean(_f08_surge(volume, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean surge (smoothed monthly spike)
def f08cv_f08_capitulation_volume_spike_meansurge_21d_base_v073_signal(volume):
    result = _mean(_f08_surge(volume, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d volume z-score
def f08cv_f08_capitulation_volume_spike_volz_42d_base_v074_signal(volume):
    result = _f08_volz(volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_84d_base_v075_signal(volume):
    result = _f08_surge(volume, 84)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cv_f08_capitulation_volume_spike_volz_5d_base_v001_signal,
    f08cv_f08_capitulation_volume_spike_volz_21d_base_v002_signal,
    f08cv_f08_capitulation_volume_spike_volz_63d_base_v003_signal,
    f08cv_f08_capitulation_volume_spike_volz_126d_base_v004_signal,
    f08cv_f08_capitulation_volume_spike_volz_252d_base_v005_signal,
    f08cv_f08_capitulation_volume_spike_surge_5d_base_v006_signal,
    f08cv_f08_capitulation_volume_spike_surge_21d_base_v007_signal,
    f08cv_f08_capitulation_volume_spike_surge_63d_base_v008_signal,
    f08cv_f08_capitulation_volume_spike_surge_126d_base_v009_signal,
    f08cv_f08_capitulation_volume_spike_surge_252d_base_v010_signal,
    f08cv_f08_capitulation_volume_spike_logsurge_21d_base_v011_signal,
    f08cv_f08_capitulation_volume_spike_logsurge_63d_base_v012_signal,
    f08cv_f08_capitulation_volume_spike_logsurge_126d_base_v013_signal,
    f08cv_f08_capitulation_volume_spike_dvsurge_63d_base_v014_signal,
    f08cv_f08_capitulation_volume_spike_dvsurge_126d_base_v015_signal,
    f08cv_f08_capitulation_volume_spike_dvsurge_252d_base_v016_signal,
    f08cv_f08_capitulation_volume_spike_dvz_63d_base_v017_signal,
    f08cv_f08_capitulation_volume_spike_dvz_126d_base_v018_signal,
    f08cv_f08_capitulation_volume_spike_dvz_252d_base_v019_signal,
    f08cv_f08_capitulation_volume_spike_vroc_5d_base_v020_signal,
    f08cv_f08_capitulation_volume_spike_vroc_21d_base_v021_signal,
    f08cv_f08_capitulation_volume_spike_vroc_63d_base_v022_signal,
    f08cv_f08_capitulation_volume_spike_vroc_126d_base_v023_signal,
    f08cv_f08_capitulation_volume_spike_logvroc_21d_base_v024_signal,
    f08cv_f08_capitulation_volume_spike_logvroc_63d_base_v025_signal,
    f08cv_f08_capitulation_volume_spike_downshare_63d_base_v026_signal,
    f08cv_f08_capitulation_volume_spike_downshare_126d_base_v027_signal,
    f08cv_f08_capitulation_volume_spike_downshare_252d_base_v028_signal,
    f08cv_f08_capitulation_volume_spike_udvolratio_63d_base_v029_signal,
    f08cv_f08_capitulation_volume_spike_udvolratio_126d_base_v030_signal,
    f08cv_f08_capitulation_volume_spike_climaxrank_126d_base_v031_signal,
    f08cv_f08_capitulation_volume_spike_climaxrank_252d_base_v032_signal,
    f08cv_f08_capitulation_volume_spike_dvrank_126d_base_v033_signal,
    f08cv_f08_capitulation_volume_spike_effort_21d_base_v034_signal,
    f08cv_f08_capitulation_volume_spike_effort_63d_base_v035_signal,
    f08cv_f08_capitulation_volume_spike_effortw_63d_base_v036_signal,
    f08cv_f08_capitulation_volume_spike_signedeffort_21d_base_v037_signal,
    f08cv_f08_capitulation_volume_spike_signedeffort_63d_base_v038_signal,
    f08cv_f08_capitulation_volume_spike_voldisp_21d_base_v039_signal,
    f08cv_f08_capitulation_volume_spike_voldisp_63d_base_v040_signal,
    f08cv_f08_capitulation_volume_spike_voldisp_126d_base_v041_signal,
    f08cv_f08_capitulation_volume_spike_voldisp_252d_base_v042_signal,
    f08cv_f08_capitulation_volume_spike_rvol_50d_base_v043_signal,
    f08cv_f08_capitulation_volume_spike_rvolma_5_50_base_v044_signal,
    f08cv_f08_capitulation_volume_spike_rvolma_21_126_base_v045_signal,
    f08cv_f08_capitulation_volume_spike_rvolma_21_252_base_v046_signal,
    f08cv_f08_capitulation_volume_spike_voltrend_21d_base_v047_signal,
    f08cv_f08_capitulation_volume_spike_voltrend_63d_base_v048_signal,
    f08cv_f08_capitulation_volume_spike_voltrend_126d_base_v049_signal,
    f08cv_f08_capitulation_volume_spike_vwrange_21d_base_v050_signal,
    f08cv_f08_capitulation_volume_spike_vwrange_63d_base_v051_signal,
    f08cv_f08_capitulation_volume_spike_ewmvolz_21d_base_v052_signal,
    f08cv_f08_capitulation_volume_spike_ewmvolz_63d_base_v053_signal,
    f08cv_f08_capitulation_volume_spike_ewmsurge_21d_base_v054_signal,
    f08cv_f08_capitulation_volume_spike_surgeclust_63d_base_v055_signal,
    f08cv_f08_capitulation_volume_spike_surgeclust_126d_base_v056_signal,
    f08cv_f08_capitulation_volume_spike_surgevol_63d_base_v057_signal,
    f08cv_f08_capitulation_volume_spike_surgevol_126d_base_v058_signal,
    f08cv_f08_capitulation_volume_spike_volskew_63d_base_v059_signal,
    f08cv_f08_capitulation_volume_spike_volskew_126d_base_v060_signal,
    f08cv_f08_capitulation_volume_spike_volkurt_63d_base_v061_signal,
    f08cv_f08_capitulation_volume_spike_volkurt_126d_base_v062_signal,
    f08cv_f08_capitulation_volume_spike_dvskew_126d_base_v063_signal,
    f08cv_f08_capitulation_volume_spike_logdvz_126d_base_v064_signal,
    f08cv_f08_capitulation_volume_spike_logdvz_252d_base_v065_signal,
    f08cv_f08_capitulation_volume_spike_cappress_63d_base_v066_signal,
    f08cv_f08_capitulation_volume_spike_cappress_126d_base_v067_signal,
    f08cv_f08_capitulation_volume_spike_zdiverge_63d_base_v068_signal,
    f08cv_f08_capitulation_volume_spike_amihud_21d_base_v069_signal,
    f08cv_f08_capitulation_volume_spike_amihud_63d_base_v070_signal,
    f08cv_f08_capitulation_volume_spike_intensrank_126d_base_v071_signal,
    f08cv_f08_capitulation_volume_spike_meansurge_5d_base_v072_signal,
    f08cv_f08_capitulation_volume_spike_meansurge_21d_base_v073_signal,
    f08cv_f08_capitulation_volume_spike_volz_42d_base_v074_signal,
    f08cv_f08_capitulation_volume_spike_surge_84d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CAPITULATION_VOLUME_SPIKE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0008, 0.045, n)
    closeadj = pd.Series(50.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name="volume")
    cols = {"closeadj": closeadj, "volume": volume}

    domain_primitives = ("_f08_volz", "_f08_surge", "_f08_dvol", "_f08_downvolshare")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f08_capitulation_volume_spike_base_001_075_claude: {n_features} features pass")
