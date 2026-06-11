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
def _f19_turnover(volume, sharesbas):
    return volume / sharesbas.replace(0, np.nan)


def _f19_log_turnover(volume, sharesbas):
    t = _f19_turnover(volume, sharesbas)
    return np.log(t.replace(0, np.nan).abs() + 1e-30)


# 5v21 EMA crossover of log turnover
def f19tr_f19_semi_turnover_regime_toema_5v21_base_v076_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.ewm(span=5, adjust=False).mean() - s.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of log turnover
def f19tr_f19_semi_turnover_regime_toema_21v63_base_v077_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.ewm(span=21, adjust=False).mean() - s.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of log turnover
def f19tr_f19_semi_turnover_regime_toema_63v126_base_v078_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.ewm(span=63, adjust=False).mean() - s.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of log turnover
def f19tr_f19_semi_turnover_regime_toema_126v252_base_v079_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.ewm(span=126, adjust=False).mean() - s.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of log turnover
def f19tr_f19_semi_turnover_regime_toema_252v504_base_v080_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.ewm(span=252, adjust=False).mean() - s.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 ratio of fast vs slow mean of log turnover
def f19tr_f19_semi_turnover_regime_tomeanratio_21v63_base_v081_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _mean(s, 21) / _mean(s, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 ratio of fast vs slow mean of log turnover
def f19tr_f19_semi_turnover_regime_tomeanratio_63v126_base_v082_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _mean(s, 63) / _mean(s, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 ratio of fast vs slow mean of log turnover
def f19tr_f19_semi_turnover_regime_tomeanratio_126v252_base_v083_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _mean(s, 126) / _mean(s, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 ratio of fast vs slow mean of log turnover
def f19tr_f19_semi_turnover_regime_tomeanratio_252v504_base_v084_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _mean(s, 252) / _mean(s, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21v252 ratio of fast vs slow mean of log turnover
def f19tr_f19_semi_turnover_regime_tomeanratio_21v252_base_v085_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _mean(s, 21) / _mean(s, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tocum_21d_base_v086_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = d.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tocum_63d_base_v087_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = d.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tocum_126d_base_v088_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = d.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tocum_252d_base_v089_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = d.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tocum_504d_base_v090_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = d.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 95th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top95_21d_base_v091_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(21, min_periods=10).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 95th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top95_63d_base_v092_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(63, min_periods=31).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 95th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top95_126d_base_v093_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(126, min_periods=63).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 95th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top95_252d_base_v094_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(252, min_periods=126).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 95th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top95_504d_base_v095_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(504, min_periods=252).quantile(0.95)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 5th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top05_21d_base_v096_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(21, min_periods=10).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 5th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top05_63d_base_v097_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(63, min_periods=31).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 5th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top05_126d_base_v098_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(126, min_periods=63).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 5th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top05_252d_base_v099_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(252, min_periods=126).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 5th percentile of log turnover
def f19tr_f19_semi_turnover_regime_top05_504d_base_v100_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(504, min_periods=252).quantile(0.05)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d autocorrelation lag-1 of log turnover
def f19tr_f19_semi_turnover_regime_toautocorr_21d_base_v101_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(21, min_periods=10).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d autocorrelation lag-1 of log turnover
def f19tr_f19_semi_turnover_regime_toautocorr_63d_base_v102_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(63, min_periods=31).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d autocorrelation lag-1 of log turnover
def f19tr_f19_semi_turnover_regime_toautocorr_126d_base_v103_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(126, min_periods=63).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d autocorrelation lag-1 of log turnover
def f19tr_f19_semi_turnover_regime_toautocorr_252d_base_v104_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(252, min_periods=126).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d autocorrelation lag-1 of log turnover
def f19tr_f19_semi_turnover_regime_toautocorr_504d_base_v105_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(504, min_periods=252).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of log turnover
def f19tr_f19_semi_turnover_regime_tocv_21d_base_v106_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _std(s, 21) / _mean(s, 21).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of log turnover
def f19tr_f19_semi_turnover_regime_tocv_63d_base_v107_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _std(s, 63) / _mean(s, 63).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of log turnover
def f19tr_f19_semi_turnover_regime_tocv_126d_base_v108_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _std(s, 126) / _mean(s, 126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of log turnover
def f19tr_f19_semi_turnover_regime_tocv_252d_base_v109_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _std(s, 252) / _mean(s, 252).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of log turnover
def f19tr_f19_semi_turnover_regime_tocv_504d_base_v110_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _std(s, 504) / _mean(s, 504).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d median of log turnover
def f19tr_f19_semi_turnover_regime_tomedian_21d_base_v111_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(21, min_periods=10).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d median of log turnover
def f19tr_f19_semi_turnover_regime_tomedian_63d_base_v112_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(63, min_periods=31).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d median of log turnover
def f19tr_f19_semi_turnover_regime_tomedian_126d_base_v113_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(126, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d median of log turnover
def f19tr_f19_semi_turnover_regime_tomedian_252d_base_v114_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(252, min_periods=126).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d median of log turnover
def f19tr_f19_semi_turnover_regime_tomedian_504d_base_v115_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(504, min_periods=252).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d IQR of log turnover
def f19tr_f19_semi_turnover_regime_toiqr_21d_base_v116_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(21, min_periods=10).quantile(0.75) - s.rolling(21, min_periods=10).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d IQR of log turnover
def f19tr_f19_semi_turnover_regime_toiqr_63d_base_v117_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(63, min_periods=31).quantile(0.75) - s.rolling(63, min_periods=31).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d IQR of log turnover
def f19tr_f19_semi_turnover_regime_toiqr_126d_base_v118_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(126, min_periods=63).quantile(0.75) - s.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of log turnover
def f19tr_f19_semi_turnover_regime_toiqr_252d_base_v119_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(252, min_periods=126).quantile(0.75) - s.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of log turnover
def f19tr_f19_semi_turnover_regime_toiqr_504d_base_v120_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s.rolling(504, min_periods=252).quantile(0.75) - s.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of extreme (z>2) days for log turnover
def f19tr_f19_semi_turnover_regime_toextreme_21d_base_v121_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 21)
    result = (z > 2).astype(float).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of extreme (z>2) days for log turnover
def f19tr_f19_semi_turnover_regime_toextreme_63d_base_v122_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 63)
    result = (z > 2).astype(float).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of extreme (z>2) days for log turnover
def f19tr_f19_semi_turnover_regime_toextreme_126d_base_v123_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 126)
    result = (z > 2).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of extreme (z>2) days for log turnover
def f19tr_f19_semi_turnover_regime_toextreme_252d_base_v124_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 252)
    result = (z > 2).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of extreme (z>2) days for log turnover
def f19tr_f19_semi_turnover_regime_toextreme_504d_base_v125_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 504)
    result = (z > 2).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tomaxmean_21d_base_v126_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 21) / _mean(s, 21).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tomaxmean_63d_base_v127_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 63) / _mean(s, 63).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tomaxmean_126d_base_v128_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 126) / _mean(s, 126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tomaxmean_252d_base_v129_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 252) / _mean(s, 252).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tomaxmean_504d_base_v130_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 504) / _mean(s, 504).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tominmean_21d_base_v131_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 21) / _mean(s, 21).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tominmean_63d_base_v132_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 63) / _mean(s, 63).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tominmean_126d_base_v133_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 126) / _mean(s, 126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tominmean_252d_base_v134_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 252) / _mean(s, 252).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min-to-mean ratio of log turnover
def f19tr_f19_semi_turnover_regime_tominmean_504d_base_v135_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 504) / _mean(s, 504).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative absolute change in log turnover
def f19tr_f19_semi_turnover_regime_toabscum_21d_base_v136_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff().abs()
    result = d.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative absolute change in log turnover
def f19tr_f19_semi_turnover_regime_toabscum_63d_base_v137_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff().abs()
    result = d.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative absolute change in log turnover
def f19tr_f19_semi_turnover_regime_toabscum_126d_base_v138_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff().abs()
    result = d.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative absolute change in log turnover
def f19tr_f19_semi_turnover_regime_toabscum_252d_base_v139_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff().abs()
    result = d.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative absolute change in log turnover
def f19tr_f19_semi_turnover_regime_toabscum_504d_base_v140_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff().abs()
    result = d.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d short composite: 21z + 63z of log turnover
def f19tr_f19_semi_turnover_regime_tocomposite_short_base_v141_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 21) + _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d long composite: 63z + 126z + 252z of log turnover
def f19tr_f19_semi_turnover_regime_tocomposite_long_base_v142_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 63) + _z(s, 126) + _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# regime divergence: sign(short EMA gap) - sign(long EMA gap) for log turnover
def f19tr_f19_semi_turnover_regime_toregime_divergence_base_v143_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    short = np.sign(s.ewm(span=21, adjust=False).mean() - s.ewm(span=63, adjust=False).mean())
    long = np.sign(s.ewm(span=126, adjust=False).mean() - s.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=s.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed z*sign(ret) of log turnover
def f19tr_f19_semi_turnover_regime_tosignedz_63d_base_v144_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    ret = volume.pct_change()
    result = _z(s, 63) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed z*sign(ret) of log turnover
def f19tr_f19_semi_turnover_regime_tosignedz_252d_base_v145_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    ret = volume.pct_change()
    result = _z(s, 252) * np.sign(ret)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of log turnover z > 2
def f19tr_f19_semi_turnover_regime_toextremefrac_21d_base_v146_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 21)
    result = (z > 2).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of log turnover z > 2
def f19tr_f19_semi_turnover_regime_toextremefrac_63d_base_v147_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 63)
    result = (z > 2).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of log turnover z > 2
def f19tr_f19_semi_turnover_regime_toextremefrac_252d_base_v148_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 252)
    result = (z > 2).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality of log turnover: z * hit_ratio
def f19tr_f19_semi_turnover_regime_toquality_63d_base_v149_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 63)
    hit = (z > 1).astype(float).rolling(63, min_periods=32).mean()
    result = z * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality of log turnover: z * hit_ratio
def f19tr_f19_semi_turnover_regime_toquality_252d_base_v150_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 252)
    hit = (z > 1).astype(float).rolling(252, min_periods=126).mean()
    result = z * hit
    return result.replace([np.inf, -np.inf], np.nan)

