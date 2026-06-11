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
def _f85_fpe(pe):
    return pe


# 21d rolling median of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_median_21d_base_v076_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(21, min_periods=11).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_median_63d_base_v077_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(63, min_periods=32).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling median of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_median_126d_base_v078_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(126, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_median_252d_base_v079_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(252, min_periods=126).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_median_504d_base_v080_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(504, min_periods=252).median()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 75th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q75_21d_base_v081_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(21, min_periods=11).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 75th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q75_63d_base_v082_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(63, min_periods=32).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 75th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q75_126d_base_v083_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(126, min_periods=63).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 75th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q75_252d_base_v084_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(252, min_periods=126).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 75th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q75_504d_base_v085_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(504, min_periods=252).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling 25th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q25_21d_base_v086_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling 25th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q25_63d_base_v087_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling 25th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q25_126d_base_v088_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling 25th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q25_252d_base_v089_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling 25th percentile of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_q25_504d_base_v090_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d IQR of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_iqr_21d_base_v091_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(21, min_periods=11).quantile(0.75) - r.rolling(21, min_periods=11).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d IQR of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_iqr_63d_base_v092_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(63, min_periods=32).quantile(0.75) - r.rolling(63, min_periods=32).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d IQR of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_iqr_126d_base_v093_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(126, min_periods=63).quantile(0.75) - r.rolling(126, min_periods=63).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_iqr_252d_base_v094_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(252, min_periods=126).quantile(0.75) - r.rolling(252, min_periods=126).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_iqr_504d_base_v095_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(504, min_periods=252).quantile(0.75) - r.rolling(504, min_periods=252).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fpe minus its rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_devmean_21d_base_v096_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fpe minus its rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_devmean_63d_base_v097_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fpe minus its rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_devmean_126d_base_v098_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fpe minus its rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_devmean_252d_base_v099_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fpe minus its rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_devmean_504d_base_v100_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fpe ratio to rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_ratiomean_21d_base_v101_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r / _mean(r, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fpe ratio to rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_ratiomean_63d_base_v102_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r / _mean(r, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fpe ratio to rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_ratiomean_126d_base_v103_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r / _mean(r, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fpe ratio to rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_ratiomean_252d_base_v104_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r / _mean(r, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fpe ratio to rolling mean
def f85fpe_f85_semi_fwd_pe_reset_fpe_ratiomean_504d_base_v105_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r / _mean(r, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days fpe above rolling 90th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_topq_21d_base_v106_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(21, min_periods=11).quantile(0.90)
    result = (r > q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days fpe above rolling 90th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_topq_63d_base_v107_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(63, min_periods=32).quantile(0.90)
    result = (r > q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days fpe above rolling 90th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_topq_126d_base_v108_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(126, min_periods=63).quantile(0.90)
    result = (r > q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days fpe above rolling 90th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_topq_252d_base_v109_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(252, min_periods=126).quantile(0.90)
    result = (r > q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days fpe above rolling 90th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_topq_504d_base_v110_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(504, min_periods=252).quantile(0.90)
    result = (r > q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days fpe below rolling 10th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_botq_21d_base_v111_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(21, min_periods=11).quantile(0.10)
    result = (r < q).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days fpe below rolling 10th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_botq_63d_base_v112_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(63, min_periods=32).quantile(0.10)
    result = (r < q).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days fpe below rolling 10th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_botq_126d_base_v113_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(126, min_periods=63).quantile(0.10)
    result = (r < q).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days fpe below rolling 10th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_botq_252d_base_v114_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(252, min_periods=126).quantile(0.10)
    result = (r < q).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days fpe below rolling 10th percentile
def f85fpe_f85_semi_fwd_pe_reset_fpe_botq_504d_base_v115_signal(pe, closeadj):
    r = _f85_fpe(pe)
    q = r.rolling(504, min_periods=252).quantile(0.10)
    result = (r < q).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorrelation of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_acf1_21d_base_v116_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(21, min_periods=11).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorrelation of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_acf1_63d_base_v117_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(63, min_periods=32).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorrelation of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_acf1_126d_base_v118_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorrelation of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_acf1_252d_base_v119_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorrelation of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_acf1_504d_base_v120_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling correlation of fpe with closeadj
def f85fpe_f85_semi_fwd_pe_reset_fpe_corrpx_21d_base_v121_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(21, min_periods=11).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of fpe with closeadj
def f85fpe_f85_semi_fwd_pe_reset_fpe_corrpx_63d_base_v122_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(63, min_periods=32).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of fpe with closeadj
def f85fpe_f85_semi_fwd_pe_reset_fpe_corrpx_126d_base_v123_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(126, min_periods=63).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of fpe with closeadj
def f85fpe_f85_semi_fwd_pe_reset_fpe_corrpx_252d_base_v124_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(252, min_periods=126).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of fpe with closeadj
def f85fpe_f85_semi_fwd_pe_reset_fpe_corrpx_504d_base_v125_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.rolling(504, min_periods=252).corr(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d diff of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_diff_21d_base_v126_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d diff of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_diff_63d_base_v127_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d diff of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_diff_126d_base_v128_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - r.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d diff of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_diff_252d_base_v129_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - r.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d diff of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_diff_504d_base_v130_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r - r.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d percent change of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_pct_21d_base_v131_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d percent change of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_pct_63d_base_v132_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percent change of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_pct_126d_base_v133_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percent change of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_pct_252d_base_v134_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percent change of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_pct_504d_base_v135_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_ema_21d_base_v136_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_ema_63d_base_v137_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_ema_126d_base_v138_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_ema_252d_base_v139_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_ema_504d_base_v140_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional mean of fpe when close above 200d MA
def f85fpe_f85_semi_fwd_pe_reset_fpe_condbull_21d_base_v141_signal(pe, closeadj):
    r = _f85_fpe(pe)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional mean of fpe when close above 200d MA
def f85fpe_f85_semi_fwd_pe_reset_fpe_condbull_63d_base_v142_signal(pe, closeadj):
    r = _f85_fpe(pe)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional mean of fpe when close above 200d MA
def f85fpe_f85_semi_fwd_pe_reset_fpe_condbull_126d_base_v143_signal(pe, closeadj):
    r = _f85_fpe(pe)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional mean of fpe when close above 200d MA
def f85fpe_f85_semi_fwd_pe_reset_fpe_condbull_252d_base_v144_signal(pe, closeadj):
    r = _f85_fpe(pe)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional mean of fpe when close above 200d MA
def f85fpe_f85_semi_fwd_pe_reset_fpe_condbull_504d_base_v145_signal(pe, closeadj):
    r = _f85_fpe(pe)
    ma = closeadj.rolling(200, min_periods=100).mean()
    mask = closeadj > ma
    result = _mean(r.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite (21+63+126 z) of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_rsh_base_v146_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = _z(r, 21) + _z(r, 63) + _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite (63+126+252 z) of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_rlg_base_v147_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = _z(r, 63) + _z(r, 126) + _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# very-long composite (126+252+504 z) of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_rxl_base_v148_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = _z(r, 126) + _z(r, 252) + _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minus 252d z divergence of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_qul_base_v149_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = (_z(r, 63) - _z(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d minus 504d z divergence of fpe
def f85fpe_f85_semi_fwd_pe_reset_fpe_qxl_base_v150_signal(pe, closeadj):
    r = _f85_fpe(pe)
    result = (_z(r, 126) - _z(r, 504))
    return result.replace([np.inf, -np.inf], np.nan)
