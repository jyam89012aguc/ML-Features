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
def _f17_dv(closeadj, volume):
    return closeadj * volume


def _f17_log_dv(closeadj, volume):
    dv = closeadj * volume
    return np.log(dv.replace(0, np.nan).abs())


# 5v21 EMA crossover of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvema_5v21_base_v076_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.ewm(span=5, adjust=False).mean() - s.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvema_21v63_base_v077_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.ewm(span=21, adjust=False).mean() - s.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvema_63v126_base_v078_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.ewm(span=63, adjust=False).mean() - s.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvema_126v252_base_v079_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.ewm(span=126, adjust=False).mean() - s.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvema_252v504_base_v080_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.ewm(span=252, adjust=False).mean() - s.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 ratio of fast vs slow mean of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmeanratio_21v63_base_v081_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _mean(s, 21) / _mean(s, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 ratio of fast vs slow mean of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmeanratio_63v126_base_v082_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _mean(s, 63) / _mean(s, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 ratio of fast vs slow mean of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmeanratio_126v252_base_v083_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _mean(s, 126) / _mean(s, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 ratio of fast vs slow mean of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmeanratio_252v504_base_v084_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _mean(s, 252) / _mean(s, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21v252 ratio of fast vs slow mean of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmeanratio_21v252_base_v085_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _mean(s, 21) / _mean(s, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcum_21d_base_v086_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff()
    result = d.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcum_63d_base_v087_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff()
    result = d.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcum_126d_base_v088_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff()
    result = d.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcum_252d_base_v089_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff()
    result = d.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcum_504d_base_v090_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff()
    result = d.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 95th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp95_21d_base_v091_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(21, min_periods=10).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 95th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp95_63d_base_v092_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(63, min_periods=31).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 95th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp95_126d_base_v093_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(126, min_periods=63).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 95th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp95_252d_base_v094_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(252, min_periods=126).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 95th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp95_504d_base_v095_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(504, min_periods=252).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 5th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp05_21d_base_v096_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(21, min_periods=10).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 5th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp05_63d_base_v097_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(63, min_periods=31).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 5th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp05_126d_base_v098_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(126, min_periods=63).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 5th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp05_252d_base_v099_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(252, min_periods=126).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 5th percentile of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvp05_504d_base_v100_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(504, min_periods=252).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d autocorrelation lag-1 of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvautocorr_21d_base_v101_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(21, min_periods=10).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d autocorrelation lag-1 of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvautocorr_63d_base_v102_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(63, min_periods=31).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d autocorrelation lag-1 of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvautocorr_126d_base_v103_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(126, min_periods=63).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d autocorrelation lag-1 of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvautocorr_252d_base_v104_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(252, min_periods=126).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d autocorrelation lag-1 of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvautocorr_504d_base_v105_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(504, min_periods=252).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcv_21d_base_v106_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _std(s, 21) / _mean(s, 21).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcv_63d_base_v107_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _std(s, 63) / _mean(s, 63).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcv_126d_base_v108_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _std(s, 126) / _mean(s, 126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcv_252d_base_v109_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _std(s, 252) / _mean(s, 252).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcv_504d_base_v110_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _std(s, 504) / _mean(s, 504).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d median of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmedian_21d_base_v111_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(21, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d median of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmedian_63d_base_v112_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(63, min_periods=31).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d median of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmedian_126d_base_v113_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(126, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d median of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmedian_252d_base_v114_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(252, min_periods=126).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d median of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmedian_504d_base_v115_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(504, min_periods=252).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d IQR of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dviqr_21d_base_v116_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(21, min_periods=10).quantile(0.75) - s.rolling(21, min_periods=10).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d IQR of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dviqr_63d_base_v117_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(63, min_periods=31).quantile(0.75) - s.rolling(63, min_periods=31).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d IQR of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dviqr_126d_base_v118_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(126, min_periods=63).quantile(0.75) - s.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dviqr_252d_base_v119_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(252, min_periods=126).quantile(0.75) - s.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dviqr_504d_base_v120_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = s.rolling(504, min_periods=252).quantile(0.75) - s.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of extreme (z>2) days for log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvextreme_21d_base_v121_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 21)
    result = (z > 2).astype(float).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of extreme (z>2) days for log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvextreme_63d_base_v122_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 63)
    result = (z > 2).astype(float).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of extreme (z>2) days for log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvextreme_126d_base_v123_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 126)
    result = (z > 2).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of extreme (z>2) days for log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvextreme_252d_base_v124_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 252)
    result = (z > 2).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of extreme (z>2) days for log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvextreme_504d_base_v125_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 504)
    result = (z > 2).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmaxmean_21d_base_v126_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _max(s, 21) / _mean(s, 21).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmaxmean_63d_base_v127_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _max(s, 63) / _mean(s, 63).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmaxmean_126d_base_v128_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _max(s, 126) / _mean(s, 126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmaxmean_252d_base_v129_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _max(s, 252) / _mean(s, 252).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvmaxmean_504d_base_v130_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _max(s, 504) / _mean(s, 504).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvminmean_21d_base_v131_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _min(s, 21) / _mean(s, 21).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvminmean_63d_base_v132_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _min(s, 63) / _mean(s, 63).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvminmean_126d_base_v133_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _min(s, 126) / _mean(s, 126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvminmean_252d_base_v134_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _min(s, 252) / _mean(s, 252).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min-to-mean ratio of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvminmean_504d_base_v135_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _min(s, 504) / _mean(s, 504).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative absolute change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvabscum_21d_base_v136_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff().abs()
    result = d.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative absolute change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvabscum_63d_base_v137_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff().abs()
    result = d.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative absolute change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvabscum_126d_base_v138_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff().abs()
    result = d.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative absolute change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvabscum_252d_base_v139_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff().abs()
    result = d.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative absolute change in log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvabscum_504d_base_v140_signal(closeadj, volume):
    d = _f17_log_dv(closeadj, volume).diff().abs()
    result = d.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d short composite: 21z + 63z of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcomposite_short_base_v141_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _z(s, 21) + _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d long composite: 63z + 126z + 252z of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvcomposite_long_base_v142_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    result = _z(s, 63) + _z(s, 126) + _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# regime divergence: sign(short EMA gap) - sign(long EMA gap) for log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvregime_divergence_base_v143_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    short = np.sign(s.ewm(span=21, adjust=False).mean() - s.ewm(span=63, adjust=False).mean())
    long = np.sign(s.ewm(span=126, adjust=False).mean() - s.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=s.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed z*sign(ret) of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvsignedz_63d_base_v144_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    ret = closeadj.pct_change()
    result = _z(s, 63) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed z*sign(ret) of log dollar-volume
def f17dv_f17_semi_dollar_volume_dynamics_dvsignedz_252d_base_v145_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    ret = closeadj.pct_change()
    result = _z(s, 252) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of log dollar-volume z > 2
def f17dv_f17_semi_dollar_volume_dynamics_dvextremefrac_21d_base_v146_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 21)
    result = (z > 2).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of log dollar-volume z > 2
def f17dv_f17_semi_dollar_volume_dynamics_dvextremefrac_63d_base_v147_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 63)
    result = (z > 2).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of log dollar-volume z > 2
def f17dv_f17_semi_dollar_volume_dynamics_dvextremefrac_252d_base_v148_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 252)
    result = (z > 2).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality of log dollar-volume: z * hit_ratio
def f17dv_f17_semi_dollar_volume_dynamics_dvquality_63d_base_v149_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 63)
    hit = (z > 1).astype(float).rolling(63, min_periods=32).mean()
    result = z * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality of log dollar-volume: z * hit_ratio
def f17dv_f17_semi_dollar_volume_dynamics_dvquality_252d_base_v150_signal(closeadj, volume):
    s = _f17_log_dv(closeadj, volume)
    z = _z(s, 252)
    hit = (z > 1).astype(float).rolling(252, min_periods=126).mean()
    result = z * hit
    return result.replace([np.inf, -np.inf], np.nan)

