import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


# ===== folder domain primitives =====
def _f16_log_vol(volume):
    return np.log(volume.replace(0, np.nan).abs())


def _f16_surge_ratio(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _f16_log_surge(volume, w):
    return np.log(volume.replace(0, np.nan) / _mean(volume, w).replace(0, np.nan))


# 21d hit ratio of surge days
def f16vs_f16_semi_volume_surge_surgefrac_21d_base_v076_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 21)
    result = (ratio > 1.5).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of surge days
def f16vs_f16_semi_volume_surge_surgefrac_63d_base_v077_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 63)
    result = (ratio > 1.5).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of surge days
def f16vs_f16_semi_volume_surge_surgefrac_126d_base_v078_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 126)
    result = (ratio > 1.5).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of surge days
def f16vs_f16_semi_volume_surge_surgefrac_252d_base_v079_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 252)
    result = (ratio > 1.5).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of surge days
def f16vs_f16_semi_volume_surge_surgefrac_504d_base_v080_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 504)
    result = (ratio > 1.5).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative log-volume change
def f16vs_f16_semi_volume_surge_volsigncum_21d_base_v081_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative log-volume change
def f16vs_f16_semi_volume_surge_volsigncum_63d_base_v082_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative log-volume change
def f16vs_f16_semi_volume_surge_volsigncum_126d_base_v083_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative log-volume change
def f16vs_f16_semi_volume_surge_volsigncum_252d_base_v084_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative log-volume change
def f16vs_f16_semi_volume_surge_volsigncum_504d_base_v085_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of log-volume
def f16vs_f16_semi_volume_surge_volema_5v21_base_v086_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.ewm(span=5, adjust=False).mean() - v.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of log-volume
def f16vs_f16_semi_volume_surge_volema_21v63_base_v087_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.ewm(span=21, adjust=False).mean() - v.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of log-volume
def f16vs_f16_semi_volume_surge_volema_63v126_base_v088_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.ewm(span=63, adjust=False).mean() - v.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of log-volume
def f16vs_f16_semi_volume_surge_volema_126v252_base_v089_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.ewm(span=126, adjust=False).mean() - v.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of log-volume
def f16vs_f16_semi_volume_surge_volema_252v504_base_v090_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.ewm(span=252, adjust=False).mean() - v.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d surge conditional on up-day (ret > 0)
def f16vs_f16_semi_volume_surge_surgeup_21d_base_v091_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 21)
    result = _mean(ratio.where(ret > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d surge conditional on up-day
def f16vs_f16_semi_volume_surge_surgeup_63d_base_v092_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 63)
    result = _mean(ratio.where(ret > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d surge conditional on up-day
def f16vs_f16_semi_volume_surge_surgeup_126d_base_v093_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 126)
    result = _mean(ratio.where(ret > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d surge conditional on up-day
def f16vs_f16_semi_volume_surge_surgeup_252d_base_v094_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 252)
    result = _mean(ratio.where(ret > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d surge conditional on up-day
def f16vs_f16_semi_volume_surge_surgeup_504d_base_v095_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 504)
    result = _mean(ratio.where(ret > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d surge conditional on down-day
def f16vs_f16_semi_volume_surge_surgedn_21d_base_v096_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 21)
    result = _mean(ratio.where(ret < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d surge conditional on down-day
def f16vs_f16_semi_volume_surge_surgedn_63d_base_v097_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 63)
    result = _mean(ratio.where(ret < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d surge conditional on down-day
def f16vs_f16_semi_volume_surge_surgedn_126d_base_v098_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 126)
    result = _mean(ratio.where(ret < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d surge conditional on down-day
def f16vs_f16_semi_volume_surge_surgedn_252d_base_v099_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 252)
    result = _mean(ratio.where(ret < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d surge conditional on down-day
def f16vs_f16_semi_volume_surge_surgedn_504d_base_v100_signal(volume, closeadj):
    ret = closeadj.pct_change()
    ratio = _f16_surge_ratio(volume, 504)
    result = _mean(ratio.where(ret < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 95th percentile surge (extreme surge measure)
def f16vs_f16_semi_volume_surge_surgep95_21d_base_v101_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 21)
    result = ratio.rolling(21, min_periods=11).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 95th percentile surge
def f16vs_f16_semi_volume_surge_surgep95_63d_base_v102_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 63)
    result = ratio.rolling(63, min_periods=32).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 95th percentile surge
def f16vs_f16_semi_volume_surge_surgep95_126d_base_v103_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 126)
    result = ratio.rolling(126, min_periods=63).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 95th percentile surge
def f16vs_f16_semi_volume_surge_surgep95_252d_base_v104_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 252)
    result = ratio.rolling(252, min_periods=126).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 95th percentile surge
def f16vs_f16_semi_volume_surge_surgep95_504d_base_v105_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 504)
    result = ratio.rolling(504, min_periods=252).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of dry-up days (volume < 0.5x mean)
def f16vs_f16_semi_volume_surge_dryhits_21d_base_v106_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 21)
    result = (ratio < 0.5).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of dry-up days
def f16vs_f16_semi_volume_surge_dryhits_63d_base_v107_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 63)
    result = (ratio < 0.5).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of dry-up days
def f16vs_f16_semi_volume_surge_dryhits_126d_base_v108_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 126)
    result = (ratio < 0.5).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of dry-up days
def f16vs_f16_semi_volume_surge_dryhits_252d_base_v109_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 252)
    result = (ratio < 0.5).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of dry-up days
def f16vs_f16_semi_volume_surge_dryhits_504d_base_v110_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 504)
    result = (ratio < 0.5).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative log-volume diff (sum of surges)
def f16vs_f16_semi_volume_surge_volcum_21d_base_v111_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = d.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative log-volume diff
def f16vs_f16_semi_volume_surge_volcum_63d_base_v112_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = d.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative log-volume diff
def f16vs_f16_semi_volume_surge_volcum_126d_base_v113_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = d.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative log-volume diff
def f16vs_f16_semi_volume_surge_volcum_252d_base_v114_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = d.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative log-volume diff
def f16vs_f16_semi_volume_surge_volcum_504d_base_v115_signal(volume, closeadj):
    d = _f16_log_vol(volume).diff()
    result = d.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume coefficient of variation
def f16vs_f16_semi_volume_surge_volcv_21d_base_v116_signal(volume, closeadj):
    result = _std(volume, 21) / _mean(volume, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume coefficient of variation
def f16vs_f16_semi_volume_surge_volcv_63d_base_v117_signal(volume, closeadj):
    result = _std(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume coefficient of variation
def f16vs_f16_semi_volume_surge_volcv_126d_base_v118_signal(volume, closeadj):
    result = _std(volume, 126) / _mean(volume, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume coefficient of variation
def f16vs_f16_semi_volume_surge_volcv_252d_base_v119_signal(volume, closeadj):
    result = _std(volume, 252) / _mean(volume, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume coefficient of variation
def f16vs_f16_semi_volume_surge_volcv_504d_base_v120_signal(volume, closeadj):
    result = _std(volume, 504) / _mean(volume, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of fast vs slow mean (21d vs 63d)
def f16vs_f16_semi_volume_surge_volmeanratio_21v63_base_v121_signal(volume, closeadj):
    result = _mean(volume, 21) / _mean(volume, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of fast vs slow mean (63d vs 126d)
def f16vs_f16_semi_volume_surge_volmeanratio_63v126_base_v122_signal(volume, closeadj):
    result = _mean(volume, 63) / _mean(volume, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of fast vs slow mean (126d vs 252d)
def f16vs_f16_semi_volume_surge_volmeanratio_126v252_base_v123_signal(volume, closeadj):
    result = _mean(volume, 126) / _mean(volume, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of fast vs slow mean (252d vs 504d)
def f16vs_f16_semi_volume_surge_volmeanratio_252v504_base_v124_signal(volume, closeadj):
    result = _mean(volume, 252) / _mean(volume, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of fast vs very-slow mean (21d vs 252d)
def f16vs_f16_semi_volume_surge_volmeanratio_21v252_base_v125_signal(volume, closeadj):
    result = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of extreme surge days (z > 2)
def f16vs_f16_semi_volume_surge_extremehits_21d_base_v126_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 63)
    result = (z > 2).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of extreme surge days
def f16vs_f16_semi_volume_surge_extremehits_63d_base_v127_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 63)
    result = (z > 2).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of extreme surge days
def f16vs_f16_semi_volume_surge_extremehits_126d_base_v128_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 126)
    result = (z > 2).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of extreme surge days
def f16vs_f16_semi_volume_surge_extremehits_252d_base_v129_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 252)
    result = (z > 2).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of extreme surge days
def f16vs_f16_semi_volume_surge_extremehits_504d_base_v130_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 504)
    result = (z > 2).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume autocorrelation lag-1
def f16vs_f16_semi_volume_surge_volautocorr_21d_base_v131_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.rolling(21, min_periods=11).corr(v.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume autocorrelation lag-1
def f16vs_f16_semi_volume_surge_volautocorr_63d_base_v132_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.rolling(63, min_periods=32).corr(v.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume autocorrelation lag-1
def f16vs_f16_semi_volume_surge_volautocorr_126d_base_v133_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.rolling(126, min_periods=63).corr(v.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume autocorrelation lag-1
def f16vs_f16_semi_volume_surge_volautocorr_252d_base_v134_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.rolling(252, min_periods=126).corr(v.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume autocorrelation lag-1
def f16vs_f16_semi_volume_surge_volautocorr_504d_base_v135_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v.rolling(504, min_periods=252).corr(v.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of recent surge max vs longer median
def f16vs_f16_semi_volume_surge_surgemaxratio_21d_base_v136_signal(volume, closeadj):
    result = _max(volume, 21) / volume.rolling(252, min_periods=126).median().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of recent surge max vs longer median
def f16vs_f16_semi_volume_surge_surgemaxratio_63d_base_v137_signal(volume, closeadj):
    result = _max(volume, 63) / volume.rolling(252, min_periods=126).median().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of recent surge max vs longer median
def f16vs_f16_semi_volume_surge_surgemaxratio_126d_base_v138_signal(volume, closeadj):
    result = _max(volume, 126) / volume.rolling(504, min_periods=252).median().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of recent surge max vs longer median
def f16vs_f16_semi_volume_surge_surgemaxratio_252d_base_v139_signal(volume, closeadj):
    result = _max(volume, 252) / volume.rolling(504, min_periods=252).median().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of recent surge max vs longer median
def f16vs_f16_semi_volume_surge_surgemaxratio_504d_base_v140_signal(volume, closeadj):
    result = _max(volume, 504) / volume.rolling(756, min_periods=378).median().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: 21d z + 63d z (short-term surge strength)
def f16vs_f16_semi_volume_surge_composite_short_base_v141_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 21) + _z(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: 63d z + 126d z + 252d z
def f16vs_f16_semi_volume_surge_composite_long_base_v142_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 63) + _z(v, 126) + _z(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d regime divergence: sign(short EMA gap) - sign(long EMA gap)
def f16vs_f16_semi_volume_surge_regime_divergence_base_v143_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    short = np.sign(v.ewm(span=21, adjust=False).mean() - v.ewm(span=63, adjust=False).mean())
    long = np.sign(v.ewm(span=126, adjust=False).mean() - v.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=v.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d surge intensity (z * sign of price ret)
def f16vs_f16_semi_volume_surge_signedsurge_21d_base_v144_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    ret = closeadj.pct_change()
    result = _z(v, 21) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d surge intensity (z * sign of price ret)
def f16vs_f16_semi_volume_surge_signedsurge_63d_base_v145_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    ret = closeadj.pct_change()
    result = _z(v, 63) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d surge intensity
def f16vs_f16_semi_volume_surge_signedsurge_126d_base_v146_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    ret = closeadj.pct_change()
    result = _z(v, 126) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d surge intensity
def f16vs_f16_semi_volume_surge_signedsurge_252d_base_v147_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    ret = closeadj.pct_change()
    result = _z(v, 252) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d surge intensity
def f16vs_f16_semi_volume_surge_signedsurge_504d_base_v148_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    ret = closeadj.pct_change()
    result = _z(v, 504) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d surge quality: surge z * hit ratio
def f16vs_f16_semi_volume_surge_surgequality_63d_base_v149_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 63)
    ratio = _f16_surge_ratio(volume, 63)
    hit = (ratio > 1.5).astype(float).rolling(63, min_periods=32).mean()
    result = z * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 252d surge quality
def f16vs_f16_semi_volume_surge_surgequality_252d_base_v150_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    z = _z(v, 252)
    ratio = _f16_surge_ratio(volume, 252)
    hit = (ratio > 1.5).astype(float).rolling(252, min_periods=126).mean()
    result = z * hit
    return result.replace([np.inf, -np.inf], np.nan)
