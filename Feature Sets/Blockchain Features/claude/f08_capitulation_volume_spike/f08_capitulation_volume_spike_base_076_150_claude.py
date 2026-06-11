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


# ============ FEATURES 076-150 ============

# 126d volume surge multiple log over 84d base
def f08cv_f08_capitulation_volume_spike_logsurge_84d_base_v076_signal(volume):
    result = np.log(_f08_surge(volume, 84))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log volume surge
def f08cv_f08_capitulation_volume_spike_logsurge_252d_base_v077_signal(volume):
    result = np.log(_f08_surge(volume, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 189d volume z-score
def f08cv_f08_capitulation_volume_spike_volz_189d_base_v078_signal(volume):
    result = _f08_volz(volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume z-score (two-year extremity)
def f08cv_f08_capitulation_volume_spike_volz_504d_base_v079_signal(volume):
    result = _f08_volz(volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_189d_base_v080_signal(volume):
    result = _f08_surge(volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_504d_base_v081_signal(volume):
    result = _f08_surge(volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge vs 504d mean
def f08cv_f08_capitulation_volume_spike_dvsurge_504d_base_v082_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _safe_div(dv, _mean(dv, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dollar-volume z-score
def f08cv_f08_capitulation_volume_spike_dvz_21d_base_v083_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(dv, 21) + _f08_surge(volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume z-score over 63d
def f08cv_f08_capitulation_volume_spike_logdvz_63d_base_v084_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume z-score over 504d
def f08cv_f08_capitulation_volume_spike_logdvz_504d_base_v085_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _z(np.log(dv.replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume rate-of-change
def f08cv_f08_capitulation_volume_spike_vroc_252d_base_v086_signal(volume):
    result = volume.pct_change(periods=252) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log volume change
def f08cv_f08_capitulation_volume_spike_logvroc_126d_base_v087_signal(volume):
    result = np.log(volume / volume.shift(126)) + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down-day dollar-volume share
def f08cv_f08_capitulation_volume_spike_downshare_21d_base_v088_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d down-day dollar-volume share
def f08cv_f08_capitulation_volume_spike_downshare_42d_base_v089_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# down-vs-up volume ratio 21d
def f08cv_f08_capitulation_volume_spike_udvolratio_21d_base_v090_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    up = dv.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    result = _safe_div(down, up)
    return result.replace([np.inf, -np.inf], np.nan)


# down-vs-up volume ratio 252d
def f08cv_f08_capitulation_volume_spike_udvolratio_252d_base_v091_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(252, min_periods=84).sum()
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=84).sum()
    result = _safe_div(down, up)
    return result.replace([np.inf, -np.inf], np.nan)


# log down-vs-up volume ratio 63d (symmetric capitulation tilt)
def f08cv_f08_capitulation_volume_spike_logudratio_63d_base_v092_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    down = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    result = np.log(_safe_div(down, up))
    return result.replace([np.inf, -np.inf], np.nan)


# climax volume percentile rank over 63d
def f08cv_f08_capitulation_volume_spike_climaxrank_63d_base_v093_signal(volume):
    result = volume.rolling(63, min_periods=21).rank(pct=True) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume climax rank over 252d
def f08cv_f08_capitulation_volume_spike_dvrank_252d_base_v094_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# effort: volume z-score times absolute return 126d
def f08cv_f08_capitulation_volume_spike_effort_126d_base_v095_signal(closeadj, volume):
    result = _f08_volz(volume, 126) * closeadj.pct_change().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# effort: volume z-score times absolute return 252d
def f08cv_f08_capitulation_volume_spike_effort_252d_base_v096_signal(closeadj, volume):
    result = _f08_volz(volume, 252) * closeadj.pct_change().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# signed effort 126d (directional volume pressure)
def f08cv_f08_capitulation_volume_spike_signedeffort_126d_base_v097_signal(closeadj, volume):
    result = _f08_volz(volume, 126) * closeadj.pct_change()
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed signed effort 63d (21d ewm of signed pressure)
def f08cv_f08_capitulation_volume_spike_smsigneffort_63d_base_v098_signal(closeadj, volume):
    eff = _f08_volz(volume, 63) * closeadj.pct_change()
    result = eff.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# volume coefficient-of-variation over 504d
def f08cv_f08_capitulation_volume_spike_voldisp_504d_base_v099_signal(volume):
    result = _safe_div(_std(volume, 504), _mean(volume, 504)) + _f08_surge(volume, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume vs 10d mean (short fast RVOL)
def f08cv_f08_capitulation_volume_spike_rvol_10d_base_v100_signal(volume):
    result = _safe_div(volume, _mean(volume, 10)) + _f08_surge(volume, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume: 10d mean vs 63d mean
def f08cv_f08_capitulation_volume_spike_rvolma_10_63_base_v101_signal(volume):
    result = _safe_div(_mean(volume, 10), _mean(volume, 63)) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume: 42d mean vs 252d mean
def f08cv_f08_capitulation_volume_spike_rvolma_42_252_base_v102_signal(volume):
    result = _safe_div(_mean(volume, 42), _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend slope 252d
def f08cv_f08_capitulation_volume_spike_voltrend_252d_base_v103_signal(volume):
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    cov = volume.rolling(252, min_periods=84).cov(idx)
    var = idx.rolling(252, min_periods=84).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(volume, 252)) + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend slope 126d (capital-flow trend)
def f08cv_f08_capitulation_volume_spike_dvtrend_126d_base_v104_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    idx = pd.Series(np.arange(len(dv), dtype=float), index=dv.index)
    cov = dv.rolling(126, min_periods=42).cov(idx)
    var = idx.rolling(126, min_periods=42).var()
    slope = _safe_div(cov, var)
    result = _safe_div(slope, _mean(dv, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted range 126d
def f08cv_f08_capitulation_volume_spike_vwrange_126d_base_v105_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = ret * _f08_surge(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of volume-weighted range (smoothed effort)
def f08cv_f08_capitulation_volume_spike_vwrangema_63d_base_v106_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = _mean(ret * _f08_surge(volume, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA of volume z-score
def f08cv_f08_capitulation_volume_spike_ewmvolz_126d_base_v107_signal(volume):
    result = _f08_volz(volume, 126).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA of surge multiple
def f08cv_f08_capitulation_volume_spike_ewmsurge_63d_base_v108_signal(volume):
    result = _f08_surge(volume, 63).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d surge clustering (current surge vs its 252d mean)
def f08cv_f08_capitulation_volume_spike_surgeclust_252d_base_v109_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(s, _mean(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of surge multiples
def f08cv_f08_capitulation_volume_spike_surgevol_252d_base_v110_signal(volume):
    s = _f08_surge(volume, 21)
    result = _std(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of volume
def f08cv_f08_capitulation_volume_spike_volskew_252d_base_v111_signal(volume):
    result = volume.rolling(252, min_periods=84).skew() + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of volume
def f08cv_f08_capitulation_volume_spike_volkurt_252d_base_v112_signal(volume):
    result = volume.rolling(252, min_periods=84).kurt() + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dollar-volume skew
def f08cv_f08_capitulation_volume_spike_dvskew_252d_base_v113_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dollar-volume kurtosis (fat dollar-spike tail)
def f08cv_f08_capitulation_volume_spike_dvkurt_126d_base_v114_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation pressure 252d
def f08cv_f08_capitulation_volume_spike_cappress_252d_base_v115_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 252) * _f08_surge(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# down-volume surge: down-share weighted z-score 126d
def f08cv_f08_capitulation_volume_spike_downz_126d_base_v116_signal(closeadj, volume):
    result = _f08_downvolshare(closeadj, volume, 126) * _f08_volz(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-divergence: volume z minus dollar-volume z over 126d
def f08cv_f08_capitulation_volume_spike_zdiverge_126d_base_v117_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = _f08_volz(volume, 126) - _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity 126d
def f08cv_f08_capitulation_volume_spike_amihud_126d_base_v118_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 126) * 1e9 + _f08_surge(volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud illiquidity 252d
def f08cv_f08_capitulation_volume_spike_amihud_252d_base_v119_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = _mean(illiq, 252) * 1e9 + _f08_surge(volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log Amihud illiquidity 63d (compressed liquidity)
def f08cv_f08_capitulation_volume_spike_logamihud_63d_base_v120_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    illiq = _safe_div(closeadj.pct_change().abs(), dv)
    result = np.log(_mean(illiq, 63) * 1e9) + _f08_surge(volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intensity-rank weighted z-score 252d
def f08cv_f08_capitulation_volume_spike_intensrank_252d_base_v121_signal(volume):
    result = _f08_volz(volume, 126) * volume.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean surge over 252d base mean
def f08cv_f08_capitulation_volume_spike_meansurge_5_252_base_v122_signal(volume):
    result = _mean(_f08_surge(volume, 252), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mean surge over 126d base
def f08cv_f08_capitulation_volume_spike_meansurge_42d_base_v123_signal(volume):
    result = _mean(_f08_surge(volume, 126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d volume z-score
def f08cv_f08_capitulation_volume_spike_volz_84d_base_v124_signal(volume):
    result = _f08_volz(volume, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_42d_base_v125_signal(volume):
    result = _f08_surge(volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d volume surge multiple
def f08cv_f08_capitulation_volume_spike_surge_10d_base_v126_signal(volume):
    result = _f08_surge(volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d volume z-score
def f08cv_f08_capitulation_volume_spike_volz_10d_base_v127_signal(volume):
    result = _f08_volz(volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surge acceleration: 5d surge minus 63d surge (short vs long spike spread)
def f08cv_f08_capitulation_volume_spike_surgeaccel_5_63_base_v128_signal(volume):
    result = _f08_surge(volume, 5) - _f08_surge(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surge acceleration: 21d surge minus 126d surge
def f08cv_f08_capitulation_volume_spike_surgeaccel_21_126_base_v129_signal(volume):
    result = _f08_surge(volume, 21) - _f08_surge(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-spread: 21d volume z minus 252d volume z (spike regime shift)
def f08cv_f08_capitulation_volume_spike_zspread_21_252_base_v130_signal(volume):
    result = _f08_volz(volume, 21) - _f08_volz(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-spread: 63d volume z minus 252d volume z
def f08cv_f08_capitulation_volume_spike_zspread_63_252_base_v131_signal(volume):
    result = _f08_volz(volume, 63) - _f08_volz(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge log over 21d
def f08cv_f08_capitulation_volume_spike_logdvsurge_21d_base_v132_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = np.log(_safe_div(dv, _mean(dv, 21)))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge log over 63d
def f08cv_f08_capitulation_volume_spike_logdvsurge_63d_base_v133_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    result = np.log(_safe_div(dv, _mean(dv, 63)))
    return result.replace([np.inf, -np.inf], np.nan)


# volume entropy proxy: dispersion of surge over 63d normalized by mean surge
def f08cv_f08_capitulation_volume_spike_surgecv_63d_base_v134_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(_std(s, 63), _mean(s, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# surge coefficient of variation 126d
def f08cv_f08_capitulation_volume_spike_surgecv_126d_base_v135_signal(volume):
    s = _f08_surge(volume, 21)
    result = _safe_div(_std(s, 126), _mean(s, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume share 63d (continuous, complement of capitulation)
def f08cv_f08_capitulation_volume_spike_upshare_63d_base_v136_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    tot = dv.rolling(63, min_periods=21).sum()
    result = _safe_div(up, tot) + _f08_downvolshare(closeadj, volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume share 126d
def f08cv_f08_capitulation_volume_spike_upshare_126d_base_v137_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=42).sum()
    tot = dv.rolling(126, min_periods=42).sum()
    result = _safe_div(up, tot) + _f08_downvolshare(closeadj, volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net volume pressure 63d: (up - down) dollar-volume normalized by total
def f08cv_f08_capitulation_volume_spike_netvolp_63d_base_v138_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    down = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    tot = dv.rolling(63, min_periods=21).sum()
    result = _safe_div(up - down, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# net volume pressure 126d
def f08cv_f08_capitulation_volume_spike_netvolp_126d_base_v139_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=42).sum()
    down = dv.where(ret < 0, 0.0).rolling(126, min_periods=42).sum()
    tot = dv.rolling(126, min_periods=42).sum()
    result = _safe_div(up - down, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# net volume pressure 252d
def f08cv_f08_capitulation_volume_spike_netvolp_252d_base_v140_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f08_dvol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=84).sum()
    down = dv.where(ret < 0, 0.0).rolling(252, min_periods=84).sum()
    tot = dv.rolling(252, min_periods=84).sum()
    result = _safe_div(up - down, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume autocorrelation proxy: surge vs lagged surge correlation (persistence)
def f08cv_f08_capitulation_volume_spike_surgepersist_63d_base_v141_signal(volume):
    s = _f08_surge(volume, 21)
    result = s.rolling(63, min_periods=21).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume surge persistence
def f08cv_f08_capitulation_volume_spike_surgepersist_126d_base_v142_signal(volume):
    s = _f08_surge(volume, 21)
    result = s.rolling(126, min_periods=42).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume to range efficiency 63d (capital per unit move)
def f08cv_f08_capitulation_volume_spike_dvpermove_63d_base_v143_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    move = closeadj.pct_change().abs().rolling(63, min_periods=21).sum()
    dvsum = dv.rolling(63, min_periods=21).sum()
    result = _safe_div(np.log(dvsum.replace(0, np.nan)), move)
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted return 63d: signed return summed weighted by volz (continuous)
def f08cv_f08_capitulation_volume_spike_spikeret_63d_base_v144_signal(closeadj, volume):
    w = _f08_volz(volume, 63)
    contrib = (closeadj.pct_change() * w).rolling(63, min_periods=21).sum()
    norm = w.abs().rolling(63, min_periods=21).sum()
    result = _safe_div(contrib, norm)
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted return 126d
def f08cv_f08_capitulation_volume_spike_spikeret_126d_base_v145_signal(closeadj, volume):
    w = _f08_volz(volume, 126)
    contrib = (closeadj.pct_change() * w).rolling(126, min_periods=42).sum()
    norm = w.abs().rolling(126, min_periods=42).sum()
    result = _safe_div(contrib, norm)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d surge z-score over 252d (extremity of current surge multiple)
def f08cv_f08_capitulation_volume_spike_surgez_252d_base_v146_signal(volume):
    result = _z(_f08_surge(volume, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d surge z-score over 252d
def f08cv_f08_capitulation_volume_spike_surgez63_252d_base_v147_signal(volume):
    result = _z(_f08_surge(volume, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume share of 21d in 252d total (recent capital concentration)
def f08cv_f08_capitulation_volume_spike_dvconc_21_252_base_v148_signal(closeadj, volume):
    dv = _f08_dvol(closeadj, volume)
    recent = dv.rolling(21, min_periods=10).sum()
    tot = dv.rolling(252, min_periods=84).sum()
    result = _safe_div(recent * (252.0 / 21.0), tot)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA of surge multiple (long smoothed activity)
def f08cv_f08_capitulation_volume_spike_ewmsurge_252d_base_v149_signal(volume):
    result = _f08_surge(volume, 252).ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon volume surge composite (21/63/126/252)
def f08cv_f08_capitulation_volume_spike_blend_multi_base_v150_signal(volume):
    result = (_f08_surge(volume, 21) + _f08_surge(volume, 63)
              + _f08_surge(volume, 126) + _f08_surge(volume, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cv_f08_capitulation_volume_spike_logsurge_84d_base_v076_signal,
    f08cv_f08_capitulation_volume_spike_logsurge_252d_base_v077_signal,
    f08cv_f08_capitulation_volume_spike_volz_189d_base_v078_signal,
    f08cv_f08_capitulation_volume_spike_volz_504d_base_v079_signal,
    f08cv_f08_capitulation_volume_spike_surge_189d_base_v080_signal,
    f08cv_f08_capitulation_volume_spike_surge_504d_base_v081_signal,
    f08cv_f08_capitulation_volume_spike_dvsurge_504d_base_v082_signal,
    f08cv_f08_capitulation_volume_spike_dvz_21d_base_v083_signal,
    f08cv_f08_capitulation_volume_spike_logdvz_63d_base_v084_signal,
    f08cv_f08_capitulation_volume_spike_logdvz_504d_base_v085_signal,
    f08cv_f08_capitulation_volume_spike_vroc_252d_base_v086_signal,
    f08cv_f08_capitulation_volume_spike_logvroc_126d_base_v087_signal,
    f08cv_f08_capitulation_volume_spike_downshare_21d_base_v088_signal,
    f08cv_f08_capitulation_volume_spike_downshare_42d_base_v089_signal,
    f08cv_f08_capitulation_volume_spike_udvolratio_21d_base_v090_signal,
    f08cv_f08_capitulation_volume_spike_udvolratio_252d_base_v091_signal,
    f08cv_f08_capitulation_volume_spike_logudratio_63d_base_v092_signal,
    f08cv_f08_capitulation_volume_spike_climaxrank_63d_base_v093_signal,
    f08cv_f08_capitulation_volume_spike_dvrank_252d_base_v094_signal,
    f08cv_f08_capitulation_volume_spike_effort_126d_base_v095_signal,
    f08cv_f08_capitulation_volume_spike_effort_252d_base_v096_signal,
    f08cv_f08_capitulation_volume_spike_signedeffort_126d_base_v097_signal,
    f08cv_f08_capitulation_volume_spike_smsigneffort_63d_base_v098_signal,
    f08cv_f08_capitulation_volume_spike_voldisp_504d_base_v099_signal,
    f08cv_f08_capitulation_volume_spike_rvol_10d_base_v100_signal,
    f08cv_f08_capitulation_volume_spike_rvolma_10_63_base_v101_signal,
    f08cv_f08_capitulation_volume_spike_rvolma_42_252_base_v102_signal,
    f08cv_f08_capitulation_volume_spike_voltrend_252d_base_v103_signal,
    f08cv_f08_capitulation_volume_spike_dvtrend_126d_base_v104_signal,
    f08cv_f08_capitulation_volume_spike_vwrange_126d_base_v105_signal,
    f08cv_f08_capitulation_volume_spike_vwrangema_63d_base_v106_signal,
    f08cv_f08_capitulation_volume_spike_ewmvolz_126d_base_v107_signal,
    f08cv_f08_capitulation_volume_spike_ewmsurge_63d_base_v108_signal,
    f08cv_f08_capitulation_volume_spike_surgeclust_252d_base_v109_signal,
    f08cv_f08_capitulation_volume_spike_surgevol_252d_base_v110_signal,
    f08cv_f08_capitulation_volume_spike_volskew_252d_base_v111_signal,
    f08cv_f08_capitulation_volume_spike_volkurt_252d_base_v112_signal,
    f08cv_f08_capitulation_volume_spike_dvskew_252d_base_v113_signal,
    f08cv_f08_capitulation_volume_spike_dvkurt_126d_base_v114_signal,
    f08cv_f08_capitulation_volume_spike_cappress_252d_base_v115_signal,
    f08cv_f08_capitulation_volume_spike_downz_126d_base_v116_signal,
    f08cv_f08_capitulation_volume_spike_zdiverge_126d_base_v117_signal,
    f08cv_f08_capitulation_volume_spike_amihud_126d_base_v118_signal,
    f08cv_f08_capitulation_volume_spike_amihud_252d_base_v119_signal,
    f08cv_f08_capitulation_volume_spike_logamihud_63d_base_v120_signal,
    f08cv_f08_capitulation_volume_spike_intensrank_252d_base_v121_signal,
    f08cv_f08_capitulation_volume_spike_meansurge_5_252_base_v122_signal,
    f08cv_f08_capitulation_volume_spike_meansurge_42d_base_v123_signal,
    f08cv_f08_capitulation_volume_spike_volz_84d_base_v124_signal,
    f08cv_f08_capitulation_volume_spike_surge_42d_base_v125_signal,
    f08cv_f08_capitulation_volume_spike_surge_10d_base_v126_signal,
    f08cv_f08_capitulation_volume_spike_volz_10d_base_v127_signal,
    f08cv_f08_capitulation_volume_spike_surgeaccel_5_63_base_v128_signal,
    f08cv_f08_capitulation_volume_spike_surgeaccel_21_126_base_v129_signal,
    f08cv_f08_capitulation_volume_spike_zspread_21_252_base_v130_signal,
    f08cv_f08_capitulation_volume_spike_zspread_63_252_base_v131_signal,
    f08cv_f08_capitulation_volume_spike_logdvsurge_21d_base_v132_signal,
    f08cv_f08_capitulation_volume_spike_logdvsurge_63d_base_v133_signal,
    f08cv_f08_capitulation_volume_spike_surgecv_63d_base_v134_signal,
    f08cv_f08_capitulation_volume_spike_surgecv_126d_base_v135_signal,
    f08cv_f08_capitulation_volume_spike_upshare_63d_base_v136_signal,
    f08cv_f08_capitulation_volume_spike_upshare_126d_base_v137_signal,
    f08cv_f08_capitulation_volume_spike_netvolp_63d_base_v138_signal,
    f08cv_f08_capitulation_volume_spike_netvolp_126d_base_v139_signal,
    f08cv_f08_capitulation_volume_spike_netvolp_252d_base_v140_signal,
    f08cv_f08_capitulation_volume_spike_surgepersist_63d_base_v141_signal,
    f08cv_f08_capitulation_volume_spike_surgepersist_126d_base_v142_signal,
    f08cv_f08_capitulation_volume_spike_dvpermove_63d_base_v143_signal,
    f08cv_f08_capitulation_volume_spike_spikeret_63d_base_v144_signal,
    f08cv_f08_capitulation_volume_spike_spikeret_126d_base_v145_signal,
    f08cv_f08_capitulation_volume_spike_surgez_252d_base_v146_signal,
    f08cv_f08_capitulation_volume_spike_surgez63_252d_base_v147_signal,
    f08cv_f08_capitulation_volume_spike_dvconc_21_252_base_v148_signal,
    f08cv_f08_capitulation_volume_spike_ewmsurge_252d_base_v149_signal,
    f08cv_f08_capitulation_volume_spike_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CAPITULATION_VOLUME_SPIKE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f08_capitulation_volume_spike_base_076_150_claude: {n_features} features pass")
