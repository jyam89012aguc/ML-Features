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
def _f80_ee(evebitda):
    return evebitda


# 21d rolling median of eez
def f80ee_f80_semi_ev_ebitda_z_eez_median_21d_base_v076_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of eez
def f80ee_f80_semi_ev_ebitda_z_eez_median_63d_base_v077_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling median of eez
def f80ee_f80_semi_ev_ebitda_z_eez_median_126d_base_v078_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of eez
def f80ee_f80_semi_ev_ebitda_z_eez_median_252d_base_v079_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of eez
def f80ee_f80_semi_ev_ebitda_z_eez_median_504d_base_v080_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 75th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q75_21d_base_v081_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 75th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q75_63d_base_v082_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 75th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q75_126d_base_v083_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 75th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q75_252d_base_v084_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 75th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q75_504d_base_v085_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 25th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q25_21d_base_v086_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 25th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q25_63d_base_v087_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 25th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q25_126d_base_v088_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 25th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q25_252d_base_v089_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 25th percentile of eez
def f80ee_f80_semi_ev_ebitda_z_eez_q25_504d_base_v090_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d IQR of eez
def f80ee_f80_semi_ev_ebitda_z_eez_iqr_21d_base_v091_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).quantile(0.75) - r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d IQR of eez
def f80ee_f80_semi_ev_ebitda_z_eez_iqr_63d_base_v092_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).quantile(0.75) - r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d IQR of eez
def f80ee_f80_semi_ev_ebitda_z_eez_iqr_126d_base_v093_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).quantile(0.75) - r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of eez
def f80ee_f80_semi_ev_ebitda_z_eez_iqr_252d_base_v094_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).quantile(0.75) - r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of eez
def f80ee_f80_semi_ev_ebitda_z_eez_iqr_504d_base_v095_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).quantile(0.75) - r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eez minus its rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_devmean_21d_base_v096_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eez minus its rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_devmean_63d_base_v097_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d eez minus its rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_devmean_126d_base_v098_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eez minus its rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_devmean_252d_base_v099_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eez minus its rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_devmean_504d_base_v100_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eez ratio to rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_ratiomean_21d_base_v101_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r / _mean(r, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eez ratio to rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_ratiomean_63d_base_v102_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r / _mean(r, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d eez ratio to rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_ratiomean_126d_base_v103_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r / _mean(r, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eez ratio to rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_ratiomean_252d_base_v104_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r / _mean(r, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d eez ratio to rolling mean
def f80ee_f80_semi_ev_ebitda_z_eez_ratiomean_504d_base_v105_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r / _mean(r, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days eez above rolling 90th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_topq_21d_base_v106_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(21, min_periods=11).quantile(0.90)
    result = (r > q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days eez above rolling 90th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_topq_63d_base_v107_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(63, min_periods=32).quantile(0.90)
    result = (r > q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days eez above rolling 90th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_topq_126d_base_v108_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(126, min_periods=63).quantile(0.90)
    result = (r > q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days eez above rolling 90th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_topq_252d_base_v109_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(252, min_periods=126).quantile(0.90)
    result = (r > q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days eez above rolling 90th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_topq_504d_base_v110_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(504, min_periods=252).quantile(0.90)
    result = (r > q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days eez below rolling 10th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_botq_21d_base_v111_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(21, min_periods=11).quantile(0.10)
    result = (r < q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days eez below rolling 10th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_botq_63d_base_v112_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(63, min_periods=32).quantile(0.10)
    result = (r < q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days eez below rolling 10th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_botq_126d_base_v113_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(126, min_periods=63).quantile(0.10)
    result = (r < q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days eez below rolling 10th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_botq_252d_base_v114_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(252, min_periods=126).quantile(0.10)
    result = (r < q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days eez below rolling 10th percentile
def f80ee_f80_semi_ev_ebitda_z_eez_botq_504d_base_v115_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    q = r.rolling(504, min_periods=252).quantile(0.10)
    result = (r < q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorrelation of eez
def f80ee_f80_semi_ev_ebitda_z_eez_acf1_21d_base_v116_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorrelation of eez
def f80ee_f80_semi_ev_ebitda_z_eez_acf1_63d_base_v117_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorrelation of eez
def f80ee_f80_semi_ev_ebitda_z_eez_acf1_126d_base_v118_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorrelation of eez
def f80ee_f80_semi_ev_ebitda_z_eez_acf1_252d_base_v119_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorrelation of eez
def f80ee_f80_semi_ev_ebitda_z_eez_acf1_504d_base_v120_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling correlation of eez with closeadj
def f80ee_f80_semi_ev_ebitda_z_eez_corrpx_21d_base_v121_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of eez with closeadj
def f80ee_f80_semi_ev_ebitda_z_eez_corrpx_63d_base_v122_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of eez with closeadj
def f80ee_f80_semi_ev_ebitda_z_eez_corrpx_126d_base_v123_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of eez with closeadj
def f80ee_f80_semi_ev_ebitda_z_eez_corrpx_252d_base_v124_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of eez with closeadj
def f80ee_f80_semi_ev_ebitda_z_eez_corrpx_504d_base_v125_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d diff of eez
def f80ee_f80_semi_ev_ebitda_z_eez_diff_21d_base_v126_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d diff of eez
def f80ee_f80_semi_ev_ebitda_z_eez_diff_63d_base_v127_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d diff of eez
def f80ee_f80_semi_ev_ebitda_z_eez_diff_126d_base_v128_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - r.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d diff of eez
def f80ee_f80_semi_ev_ebitda_z_eez_diff_252d_base_v129_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - r.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d diff of eez
def f80ee_f80_semi_ev_ebitda_z_eez_diff_504d_base_v130_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r - r.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d percent change of eez
def f80ee_f80_semi_ev_ebitda_z_eez_pct_21d_base_v131_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d percent change of eez
def f80ee_f80_semi_ev_ebitda_z_eez_pct_63d_base_v132_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percent change of eez
def f80ee_f80_semi_ev_ebitda_z_eez_pct_126d_base_v133_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percent change of eez
def f80ee_f80_semi_ev_ebitda_z_eez_pct_252d_base_v134_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percent change of eez
def f80ee_f80_semi_ev_ebitda_z_eez_pct_504d_base_v135_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_21d_base_v136_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_63d_base_v137_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_126d_base_v138_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_252d_base_v139_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_504d_base_v140_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional mean of eez when close above 200d MA
def f80ee_f80_semi_ev_ebitda_z_eez_condbull_21d_base_v141_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional mean of eez when close above 200d MA
def f80ee_f80_semi_ev_ebitda_z_eez_condbull_63d_base_v142_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional mean of eez when close above 200d MA
def f80ee_f80_semi_ev_ebitda_z_eez_condbull_126d_base_v143_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional mean of eez when close above 200d MA
def f80ee_f80_semi_ev_ebitda_z_eez_condbull_252d_base_v144_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional mean of eez when close above 200d MA
def f80ee_f80_semi_ev_ebitda_z_eez_condbull_504d_base_v145_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite (21+63+126 z) of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rsh_base_v146_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 21) + _z(r, 63) + _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite (63+126+252 z) of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rlg_base_v147_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 63) + _z(r, 126) + _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# very-long composite (126+252+504 z) of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rxl_base_v148_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 126) + _z(r, 252) + _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minus 252d z divergence of eez
def f80ee_f80_semi_ev_ebitda_z_eez_qul_base_v149_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = (_z(r, 63) - _z(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d minus 504d z divergence of eez
def f80ee_f80_semi_ev_ebitda_z_eez_qxl_base_v150_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = (_z(r, 126) - _z(r, 504))
    return result.replace([np.inf, -np.inf], np.nan)
