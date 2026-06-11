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
def _f83_pfcf(pfcf):
    return pfcf


# 21d rolling median of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_median_21d_base_v076_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(21, min_periods=11).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_median_63d_base_v077_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(63, min_periods=32).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling median of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_median_126d_base_v078_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(126, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_median_252d_base_v079_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(252, min_periods=126).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_median_504d_base_v080_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(504, min_periods=252).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 75th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q75_21d_base_v081_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(21, min_periods=11).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 75th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q75_63d_base_v082_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(63, min_periods=32).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 75th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q75_126d_base_v083_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(126, min_periods=63).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 75th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q75_252d_base_v084_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(252, min_periods=126).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 75th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q75_504d_base_v085_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(504, min_periods=252).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 25th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q25_21d_base_v086_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 25th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q25_63d_base_v087_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 25th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q25_126d_base_v088_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 25th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q25_252d_base_v089_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 25th percentile of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_q25_504d_base_v090_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d IQR of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_iqr_21d_base_v091_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(21, min_periods=11).quantile(0.75) - r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d IQR of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_iqr_63d_base_v092_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(63, min_periods=32).quantile(0.75) - r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d IQR of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_iqr_126d_base_v093_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(126, min_periods=63).quantile(0.75) - r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_iqr_252d_base_v094_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(252, min_periods=126).quantile(0.75) - r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_iqr_504d_base_v095_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(504, min_periods=252).quantile(0.75) - r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pfc minus its rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_devmean_21d_base_v096_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pfc minus its rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_devmean_63d_base_v097_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pfc minus its rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_devmean_126d_base_v098_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pfc minus its rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_devmean_252d_base_v099_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pfc minus its rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_devmean_504d_base_v100_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pfc ratio to rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_ratiomean_21d_base_v101_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r / _mean(r, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pfc ratio to rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_ratiomean_63d_base_v102_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r / _mean(r, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pfc ratio to rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_ratiomean_126d_base_v103_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r / _mean(r, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pfc ratio to rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_ratiomean_252d_base_v104_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r / _mean(r, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pfc ratio to rolling mean
def f83pfc_f83_semi_pfcf_cohort_pfc_ratiomean_504d_base_v105_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r / _mean(r, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days pfc above rolling 90th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_topq_21d_base_v106_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(21, min_periods=11).quantile(0.90)
    result = (r > q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days pfc above rolling 90th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_topq_63d_base_v107_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(63, min_periods=32).quantile(0.90)
    result = (r > q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days pfc above rolling 90th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_topq_126d_base_v108_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(126, min_periods=63).quantile(0.90)
    result = (r > q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days pfc above rolling 90th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_topq_252d_base_v109_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(252, min_periods=126).quantile(0.90)
    result = (r > q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days pfc above rolling 90th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_topq_504d_base_v110_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(504, min_periods=252).quantile(0.90)
    result = (r > q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days pfc below rolling 10th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_botq_21d_base_v111_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(21, min_periods=11).quantile(0.10)
    result = (r < q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days pfc below rolling 10th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_botq_63d_base_v112_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(63, min_periods=32).quantile(0.10)
    result = (r < q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days pfc below rolling 10th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_botq_126d_base_v113_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(126, min_periods=63).quantile(0.10)
    result = (r < q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days pfc below rolling 10th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_botq_252d_base_v114_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(252, min_periods=126).quantile(0.10)
    result = (r < q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days pfc below rolling 10th percentile
def f83pfc_f83_semi_pfcf_cohort_pfc_botq_504d_base_v115_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    q = r.rolling(504, min_periods=252).quantile(0.10)
    result = (r < q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorrelation of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_acf1_21d_base_v116_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(21, min_periods=11).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorrelation of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_acf1_63d_base_v117_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(63, min_periods=32).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorrelation of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_acf1_126d_base_v118_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorrelation of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_acf1_252d_base_v119_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorrelation of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_acf1_504d_base_v120_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling correlation of pfc with closeadj
def f83pfc_f83_semi_pfcf_cohort_pfc_corrpx_21d_base_v121_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(21, min_periods=11).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of pfc with closeadj
def f83pfc_f83_semi_pfcf_cohort_pfc_corrpx_63d_base_v122_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(63, min_periods=32).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of pfc with closeadj
def f83pfc_f83_semi_pfcf_cohort_pfc_corrpx_126d_base_v123_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(126, min_periods=63).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of pfc with closeadj
def f83pfc_f83_semi_pfcf_cohort_pfc_corrpx_252d_base_v124_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(252, min_periods=126).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of pfc with closeadj
def f83pfc_f83_semi_pfcf_cohort_pfc_corrpx_504d_base_v125_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.rolling(504, min_periods=252).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d diff of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_diff_21d_base_v126_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d diff of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_diff_63d_base_v127_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d diff of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_diff_126d_base_v128_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - r.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d diff of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_diff_252d_base_v129_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - r.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d diff of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_diff_504d_base_v130_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r - r.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d percent change of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_pct_21d_base_v131_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d percent change of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_pct_63d_base_v132_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percent change of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_pct_126d_base_v133_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percent change of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_pct_252d_base_v134_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percent change of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_pct_504d_base_v135_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_ema_21d_base_v136_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_ema_63d_base_v137_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_ema_126d_base_v138_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_ema_252d_base_v139_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_ema_504d_base_v140_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional mean of pfc when close above 200d MA
def f83pfc_f83_semi_pfcf_cohort_pfc_condbull_21d_base_v141_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional mean of pfc when close above 200d MA
def f83pfc_f83_semi_pfcf_cohort_pfc_condbull_63d_base_v142_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional mean of pfc when close above 200d MA
def f83pfc_f83_semi_pfcf_cohort_pfc_condbull_126d_base_v143_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional mean of pfc when close above 200d MA
def f83pfc_f83_semi_pfcf_cohort_pfc_condbull_252d_base_v144_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional mean of pfc when close above 200d MA
def f83pfc_f83_semi_pfcf_cohort_pfc_condbull_504d_base_v145_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite (21+63+126 z) of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_rsh_base_v146_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = _z(r, 21) + _z(r, 63) + _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite (63+126+252 z) of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_rlg_base_v147_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = _z(r, 63) + _z(r, 126) + _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# very-long composite (126+252+504 z) of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_rxl_base_v148_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = _z(r, 126) + _z(r, 252) + _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minus 252d z divergence of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_qul_base_v149_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = (_z(r, 63) - _z(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d minus 504d z divergence of pfc
def f83pfc_f83_semi_pfcf_cohort_pfc_qxl_base_v150_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    result = (_z(r, 126) - _z(r, 504))
    return result.replace([np.inf, -np.inf], np.nan)
