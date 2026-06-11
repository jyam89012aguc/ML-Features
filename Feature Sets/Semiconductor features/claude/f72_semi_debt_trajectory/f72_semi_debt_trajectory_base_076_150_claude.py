import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


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


# ===== folder domain primitives =====
def _f72_debt_yoy(debt):
    return debt.pct_change(periods=252)


# 21d rolling median of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_median_21d_base_v076_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_median_63d_base_v077_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling median of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_median_126d_base_v078_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_median_252d_base_v079_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_median_504d_base_v080_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 75th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q75_21d_base_v081_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 75th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q75_63d_base_v082_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 75th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q75_126d_base_v083_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 75th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q75_252d_base_v084_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 75th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q75_504d_base_v085_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 25th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q25_21d_base_v086_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 25th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q25_63d_base_v087_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 25th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q25_126d_base_v088_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 25th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q25_252d_base_v089_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 25th percentile of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_q25_504d_base_v090_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d IQR of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_iqr_21d_base_v091_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).quantile(0.75) - r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d IQR of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_iqr_63d_base_v092_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).quantile(0.75) - r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d IQR of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_iqr_126d_base_v093_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).quantile(0.75) - r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_iqr_252d_base_v094_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).quantile(0.75) - r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_iqr_504d_base_v095_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).quantile(0.75) - r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dyoy minus its rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_devmean_21d_base_v096_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dyoy minus its rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_devmean_63d_base_v097_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dyoy minus its rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_devmean_126d_base_v098_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dyoy minus its rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_devmean_252d_base_v099_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dyoy minus its rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_devmean_504d_base_v100_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dyoy ratio to rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_ratiomean_21d_base_v101_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r / _mean(r, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dyoy ratio to rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_ratiomean_63d_base_v102_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r / _mean(r, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dyoy ratio to rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_ratiomean_126d_base_v103_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r / _mean(r, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dyoy ratio to rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_ratiomean_252d_base_v104_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r / _mean(r, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dyoy ratio to rolling mean
def f72dt_f72_semi_debt_trajectory_dyoy_ratiomean_504d_base_v105_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r / _mean(r, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days dyoy above rolling 90th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_topq_21d_base_v106_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(21, min_periods=11).quantile(0.90)
    result = (r > q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days dyoy above rolling 90th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_topq_63d_base_v107_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(63, min_periods=32).quantile(0.90)
    result = (r > q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days dyoy above rolling 90th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_topq_126d_base_v108_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(126, min_periods=63).quantile(0.90)
    result = (r > q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days dyoy above rolling 90th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_topq_252d_base_v109_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(252, min_periods=126).quantile(0.90)
    result = (r > q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days dyoy above rolling 90th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_topq_504d_base_v110_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(504, min_periods=252).quantile(0.90)
    result = (r > q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days dyoy below rolling 10th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_botq_21d_base_v111_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(21, min_periods=11).quantile(0.10)
    result = (r < q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days dyoy below rolling 10th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_botq_63d_base_v112_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(63, min_periods=32).quantile(0.10)
    result = (r < q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days dyoy below rolling 10th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_botq_126d_base_v113_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(126, min_periods=63).quantile(0.10)
    result = (r < q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days dyoy below rolling 10th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_botq_252d_base_v114_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(252, min_periods=126).quantile(0.10)
    result = (r < q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days dyoy below rolling 10th percentile
def f72dt_f72_semi_debt_trajectory_dyoy_botq_504d_base_v115_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    q = r.rolling(504, min_periods=252).quantile(0.10)
    result = (r < q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorrelation of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_acf1_21d_base_v116_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorrelation of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_acf1_63d_base_v117_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorrelation of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_acf1_126d_base_v118_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorrelation of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_acf1_252d_base_v119_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorrelation of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_acf1_504d_base_v120_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling correlation of dyoy with closeadj
def f72dt_f72_semi_debt_trajectory_dyoy_corrpx_21d_base_v121_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of dyoy with closeadj
def f72dt_f72_semi_debt_trajectory_dyoy_corrpx_63d_base_v122_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of dyoy with closeadj
def f72dt_f72_semi_debt_trajectory_dyoy_corrpx_126d_base_v123_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of dyoy with closeadj
def f72dt_f72_semi_debt_trajectory_dyoy_corrpx_252d_base_v124_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of dyoy with closeadj
def f72dt_f72_semi_debt_trajectory_dyoy_corrpx_504d_base_v125_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d diff of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_diff_21d_base_v126_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d diff of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_diff_63d_base_v127_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d diff of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_diff_126d_base_v128_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - r.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d diff of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_diff_252d_base_v129_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - r.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d diff of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_diff_504d_base_v130_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r - r.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d percent change of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_pct_21d_base_v131_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d percent change of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_pct_63d_base_v132_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percent change of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_pct_126d_base_v133_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percent change of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_pct_252d_base_v134_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percent change of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_pct_504d_base_v135_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_21d_base_v136_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_63d_base_v137_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_126d_base_v138_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_252d_base_v139_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_504d_base_v140_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional mean of dyoy when close above 200d MA
def f72dt_f72_semi_debt_trajectory_dyoy_condbull_21d_base_v141_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional mean of dyoy when close above 200d MA
def f72dt_f72_semi_debt_trajectory_dyoy_condbull_63d_base_v142_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional mean of dyoy when close above 200d MA
def f72dt_f72_semi_debt_trajectory_dyoy_condbull_126d_base_v143_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional mean of dyoy when close above 200d MA
def f72dt_f72_semi_debt_trajectory_dyoy_condbull_252d_base_v144_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional mean of dyoy when close above 200d MA
def f72dt_f72_semi_debt_trajectory_dyoy_condbull_504d_base_v145_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite (21+63+126 z) of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rsh_base_v146_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 21) + _z(r, 63) + _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite (63+126+252 z) of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rlg_base_v147_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 63) + _z(r, 126) + _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# very-long composite (126+252+504 z) of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rxl_base_v148_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 126) + _z(r, 252) + _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minus 252d z divergence of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_qul_base_v149_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = (_z(r, 63) - _z(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d minus 504d z divergence of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_qxl_base_v150_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = (_z(r, 126) - _z(r, 504))
    return result.replace([np.inf, -np.inf], np.nan)
