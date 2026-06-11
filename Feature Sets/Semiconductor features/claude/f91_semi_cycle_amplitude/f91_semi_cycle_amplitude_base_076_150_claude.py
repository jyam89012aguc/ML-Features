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
def _f91ca_rev_amp(s, n=252):
    mp = max(1, n // 2)
    return (s.rolling(n, min_periods=mp).max() - s.rolling(n, min_periods=mp).min()) / s.rolling(n, min_periods=mp).mean().replace(0, np.nan)


def _f91ca_capex_amp(s, n=252):
    mp = max(1, n // 2)
    return (s.rolling(n, min_periods=mp).max() - s.rolling(n, min_periods=mp).min()) / s.rolling(n, min_periods=mp).mean().replace(0, np.nan)


def _f91ca_combined(rev, cx, n=252):
    mp = max(1, n // 2)
    ra = (rev.rolling(n, min_periods=mp).max() - rev.rolling(n, min_periods=mp).min()) / rev.rolling(n, min_periods=mp).mean().replace(0, np.nan)
    ca = (cx.rolling(n, min_periods=mp).max() - cx.rolling(n, min_periods=mp).min()) / cx.rolling(n, min_periods=mp).mean().replace(0, np.nan)
    return ra + ca


# 21d conditional mean of core on secondary>0
def f91ca_f91_semi_cycle_amplitude_condup_21d_base_v076_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d conditional mean of core on secondary>0
def f91ca_f91_semi_cycle_amplitude_condup_63d_base_v077_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d conditional mean of core on secondary>0
def f91ca_f91_semi_cycle_amplitude_condup_126d_base_v078_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d conditional mean of core on secondary>0
def f91ca_f91_semi_cycle_amplitude_condup_252d_base_v079_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d conditional mean of core on secondary>0
def f91ca_f91_semi_cycle_amplitude_condup_504d_base_v080_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d conditional mean of core on secondary<0
def f91ca_f91_semi_cycle_amplitude_conddn_21d_base_v081_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d conditional mean of core on secondary<0
def f91ca_f91_semi_cycle_amplitude_conddn_63d_base_v082_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d conditional mean of core on secondary<0
def f91ca_f91_semi_cycle_amplitude_conddn_126d_base_v083_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d conditional mean of core on secondary<0
def f91ca_f91_semi_cycle_amplitude_conddn_252d_base_v084_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d conditional mean of core on secondary<0
def f91ca_f91_semi_cycle_amplitude_conddn_504d_base_v085_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x.where(y < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of core
def f91ca_f91_semi_cycle_amplitude_cum_21d_base_v086_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of core
def f91ca_f91_semi_cycle_amplitude_cum_63d_base_v087_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of core
def f91ca_f91_semi_cycle_amplitude_cum_126d_base_v088_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of core
def f91ca_f91_semi_cycle_amplitude_cum_252d_base_v089_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of core
def f91ca_f91_semi_cycle_amplitude_cum_504d_base_v090_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d drawdown of cumulative core from peak
def f91ca_f91_semi_cycle_amplitude_cumdd_21d_base_v091_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    cum = x.rolling(21, min_periods=10).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d drawdown of cumulative core from peak
def f91ca_f91_semi_cycle_amplitude_cumdd_63d_base_v092_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    cum = x.rolling(63, min_periods=31).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d drawdown of cumulative core from peak
def f91ca_f91_semi_cycle_amplitude_cumdd_126d_base_v093_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    cum = x.rolling(126, min_periods=63).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d drawdown of cumulative core from peak
def f91ca_f91_semi_cycle_amplitude_cumdd_252d_base_v094_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    cum = x.rolling(252, min_periods=126).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d drawdown of cumulative core from peak
def f91ca_f91_semi_cycle_amplitude_cumdd_504d_base_v095_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    cum = x.rolling(504, min_periods=252).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# core minus its 63d mean (21d horizon)
def f91ca_f91_semi_cycle_amplitude_rel21v63_n_base_v096_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x - _mean(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# core minus its 126d mean (63d horizon)
def f91ca_f91_semi_cycle_amplitude_rel63v126_n_base_v097_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x - _mean(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# core minus its 252d mean (126d horizon)
def f91ca_f91_semi_cycle_amplitude_rel126v252_n_base_v098_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x - _mean(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# core minus its 504d mean (252d horizon)
def f91ca_f91_semi_cycle_amplitude_rel252v504_n_base_v099_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x - _mean(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# core minus its 756d mean (504d horizon)
def f91ca_f91_semi_cycle_amplitude_rel504v756_n_base_v100_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = x - _mean(x, 756)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean of core divided by 21d mean
def f91ca_f91_semi_cycle_amplitude_ratio5v21_n_base_v101_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _mean(x, 5) / _mean(x, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of core divided by 63d mean
def f91ca_f91_semi_cycle_amplitude_ratio21v63_n_base_v102_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _mean(x, 21) / _mean(x, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of core divided by 126d mean
def f91ca_f91_semi_cycle_amplitude_ratio63v126_n_base_v103_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _mean(x, 63) / _mean(x, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of core divided by 252d mean
def f91ca_f91_semi_cycle_amplitude_ratio126v252_n_base_v104_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _mean(x, 126) / _mean(x, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of core divided by 504d mean
def f91ca_f91_semi_cycle_amplitude_ratio252v504_n_base_v105_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _mean(x, 252) / _mean(x, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of secondary series
def f91ca_f91_semi_cycle_amplitude_seczscore_21d_base_v106_signal(revenue, capex, closeadj):
    y = _f91ca_rev_amp(revenue, 252)
    result = _z(y, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of secondary series
def f91ca_f91_semi_cycle_amplitude_seczscore_63d_base_v107_signal(revenue, capex, closeadj):
    y = _f91ca_rev_amp(revenue, 252)
    result = _z(y, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of secondary series
def f91ca_f91_semi_cycle_amplitude_seczscore_126d_base_v108_signal(revenue, capex, closeadj):
    y = _f91ca_rev_amp(revenue, 252)
    result = _z(y, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of secondary series
def f91ca_f91_semi_cycle_amplitude_seczscore_252d_base_v109_signal(revenue, capex, closeadj):
    y = _f91ca_rev_amp(revenue, 252)
    result = _z(y, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of secondary series
def f91ca_f91_semi_cycle_amplitude_seczscore_504d_base_v110_signal(revenue, capex, closeadj):
    y = _f91ca_rev_amp(revenue, 252)
    result = _z(y, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of (secondary - core)
def f91ca_f91_semi_cycle_amplitude_secdiff_21d_base_v111_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(y - x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of (secondary - core)
def f91ca_f91_semi_cycle_amplitude_secdiff_63d_base_v112_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(y - x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of (secondary - core)
def f91ca_f91_semi_cycle_amplitude_secdiff_126d_base_v113_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(y - x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of (secondary - core)
def f91ca_f91_semi_cycle_amplitude_secdiff_252d_base_v114_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(y - x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of (secondary - core)
def f91ca_f91_semi_cycle_amplitude_secdiff_504d_base_v115_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(y - x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling covariance of core and secondary
def f91ca_f91_semi_cycle_amplitude_cov_21d_base_v116_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(21, min_periods=10).cov(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling covariance of core and secondary
def f91ca_f91_semi_cycle_amplitude_cov_63d_base_v117_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(63, min_periods=31).cov(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling covariance of core and secondary
def f91ca_f91_semi_cycle_amplitude_cov_126d_base_v118_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(126, min_periods=63).cov(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling covariance of core and secondary
def f91ca_f91_semi_cycle_amplitude_cov_252d_base_v119_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(252, min_periods=126).cov(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling covariance of core and secondary
def f91ca_f91_semi_cycle_amplitude_cov_504d_base_v120_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(504, min_periods=252).cov(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling correlation of core and secondary
def f91ca_f91_semi_cycle_amplitude_corr_21d_base_v121_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(21, min_periods=10).corr(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling correlation of core and secondary
def f91ca_f91_semi_cycle_amplitude_corr_63d_base_v122_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(63, min_periods=31).corr(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling correlation of core and secondary
def f91ca_f91_semi_cycle_amplitude_corr_126d_base_v123_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(126, min_periods=63).corr(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling correlation of core and secondary
def f91ca_f91_semi_cycle_amplitude_corr_252d_base_v124_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(252, min_periods=126).corr(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling correlation of core and secondary
def f91ca_f91_semi_cycle_amplitude_corr_504d_base_v125_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = x.rolling(504, min_periods=252).corr(y)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of core mean to secondary mean
def f91ca_f91_semi_cycle_amplitude_coresecratio_21d_base_v126_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x, 21) / _mean(y, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of core mean to secondary mean
def f91ca_f91_semi_cycle_amplitude_coresecratio_63d_base_v127_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x, 63) / _mean(y, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of core mean to secondary mean
def f91ca_f91_semi_cycle_amplitude_coresecratio_126d_base_v128_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of core mean to secondary mean
def f91ca_f91_semi_cycle_amplitude_coresecratio_252d_base_v129_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x, 252) / _mean(y, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of core mean to secondary mean
def f91ca_f91_semi_cycle_amplitude_coresecratio_504d_base_v130_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    result = _mean(x, 504) / _mean(y, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# short-horizon composite z (21+63+126)
def f91ca_f91_semi_cycle_amplitude_compshort_n_base_v131_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _z(x, 21) + _z(x, 63) + _z(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# mid-horizon composite z (63+126+252)
def f91ca_f91_semi_cycle_amplitude_compmid_n_base_v132_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _z(x, 63) + _z(x, 126) + _z(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# long-horizon composite z (126+252+504)
def f91ca_f91_semi_cycle_amplitude_complong_n_base_v133_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _z(x, 126) + _z(x, 252) + _z(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# mixed-horizon composite z (21+126+504)
def f91ca_f91_semi_cycle_amplitude_compmixed_n_base_v134_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _z(x, 21) + _z(x, 126) + _z(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# wide-horizon composite z (63+252+504)
def f91ca_f91_semi_cycle_amplitude_compwide_n_base_v135_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    result = _z(x, 63) + _z(x, 252) + _z(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# regime divergence: sign(ema21-ema63) - sign(ema126-ema252)
def f91ca_f91_semi_cycle_amplitude_regime_2163_126252_n_base_v136_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    short_ = np.sign(x.ewm(span=21, adjust=False).mean() - x.ewm(span=63, adjust=False).mean())
    long_ = np.sign(x.ewm(span=126, adjust=False).mean() - x.ewm(span=252, adjust=False).mean())
    result = pd.Series(short_ - long_, index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)

# regime divergence: sign(ema5-ema63) - sign(ema126-ema504)
def f91ca_f91_semi_cycle_amplitude_regime_563_126504_n_base_v137_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    short_ = np.sign(x.ewm(span=5, adjust=False).mean() - x.ewm(span=63, adjust=False).mean())
    long_ = np.sign(x.ewm(span=126, adjust=False).mean() - x.ewm(span=504, adjust=False).mean())
    result = pd.Series(short_ - long_, index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)

# regime divergence: sign(ema21-ema63) - sign(ema252-ema504)
def f91ca_f91_semi_cycle_amplitude_regime_2163_252504_n_base_v138_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    short_ = np.sign(x.ewm(span=21, adjust=False).mean() - x.ewm(span=63, adjust=False).mean())
    long_ = np.sign(x.ewm(span=252, adjust=False).mean() - x.ewm(span=504, adjust=False).mean())
    result = pd.Series(short_ - long_, index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)

# regime divergence: sign(ema5-ema21) - sign(ema63-ema252)
def f91ca_f91_semi_cycle_amplitude_regime_521_63252_n_base_v139_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    short_ = np.sign(x.ewm(span=5, adjust=False).mean() - x.ewm(span=21, adjust=False).mean())
    long_ = np.sign(x.ewm(span=63, adjust=False).mean() - x.ewm(span=252, adjust=False).mean())
    result = pd.Series(short_ - long_, index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)

# regime divergence: sign(ema63-ema126) - sign(ema252-ema504)
def f91ca_f91_semi_cycle_amplitude_regime_63126_252504_n_base_v140_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    short_ = np.sign(x.ewm(span=63, adjust=False).mean() - x.ewm(span=126, adjust=False).mean())
    long_ = np.sign(x.ewm(span=252, adjust=False).mean() - x.ewm(span=504, adjust=False).mean())
    result = pd.Series(short_ - long_, index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d quality composite (z * hit ratio)
def f91ca_f91_semi_cycle_amplitude_quality_21d_base_v141_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 21)
    hit = (x > 0).astype(float).rolling(21, min_periods=10).mean()
    result = zsc * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 63d quality composite (z * hit ratio)
def f91ca_f91_semi_cycle_amplitude_quality_63d_base_v142_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 63)
    hit = (x > 0).astype(float).rolling(63, min_periods=31).mean()
    result = zsc * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 126d quality composite (z * hit ratio)
def f91ca_f91_semi_cycle_amplitude_quality_126d_base_v143_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 126)
    hit = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = zsc * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 252d quality composite (z * hit ratio)
def f91ca_f91_semi_cycle_amplitude_quality_252d_base_v144_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 252)
    hit = (x > 0).astype(float).rolling(252, min_periods=126).mean()
    result = zsc * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 504d quality composite (z * hit ratio)
def f91ca_f91_semi_cycle_amplitude_quality_504d_base_v145_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 504)
    hit = (x > 0).astype(float).rolling(504, min_periods=252).mean()
    result = zsc * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 21d extreme indicator (z clipped to +/-3)
def f91ca_f91_semi_cycle_amplitude_extreme_21d_base_v146_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 21)
    result = zsc.clip(lower=-3.0, upper=3.0)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d extreme indicator (z clipped to +/-3)
def f91ca_f91_semi_cycle_amplitude_extreme_63d_base_v147_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 63)
    result = zsc.clip(lower=-3.0, upper=3.0)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d extreme indicator (z clipped to +/-3)
def f91ca_f91_semi_cycle_amplitude_extreme_126d_base_v148_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 126)
    result = zsc.clip(lower=-3.0, upper=3.0)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d extreme indicator (z clipped to +/-3)
def f91ca_f91_semi_cycle_amplitude_extreme_252d_base_v149_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 252)
    result = zsc.clip(lower=-3.0, upper=3.0)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d extreme indicator (z clipped to +/-3)
def f91ca_f91_semi_cycle_amplitude_extreme_504d_base_v150_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    zsc = _z(x, 504)
    result = zsc.clip(lower=-3.0, upper=3.0)
    return result.replace([np.inf, -np.inf], np.nan)
