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
def _f97ai_log_ratio(rev, hyp):
    return np.log(rev.replace(0, np.nan).abs() / hyp.replace(0, np.nan).abs())


def _f97ai_ratio(rev, hyp):
    return rev / hyp.replace(0, np.nan)


def _f97ai_log_diff(s, n):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f97ai_pct(s, n):
    return s.pct_change(periods=n)


def _f97ai_roll_corr(a, b, w):
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


def _f97ai_roll_beta(a, b, w):
    cov = a.rolling(w, min_periods=max(2, w // 2)).cov(b)
    var = b.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


# 21d rolling correlation of revenue and hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_corr_21d_base_v001_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of revenue and hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_corr_63d_base_v002_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of revenue and hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_corr_126d_base_v003_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of revenue and hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_corr_252d_base_v004_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of revenue and hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_corr_504d_base_v005_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta of revenue on hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_beta_21d_base_v006_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta of revenue on hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_beta_63d_base_v007_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta of revenue on hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_beta_126d_base_v008_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta of revenue on hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_beta_252d_base_v009_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta of revenue on hyperscaler capex index
def f97ai_f97_semi_ai_compute_demand_proxy_beta_504d_base_v010_signal(revenue, hyperscaler_capex_index, closeadj):
    result = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mindshare ratio revenue / hyperscaler index minus 21d mean
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_21d_base_v011_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mindshare ratio revenue / hyperscaler index minus 63d mean
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_63d_base_v012_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mindshare ratio revenue / hyperscaler index minus 126d mean
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_126d_base_v013_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mindshare ratio revenue / hyperscaler index minus 252d mean
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_252d_base_v014_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mindshare ratio revenue / hyperscaler index minus 504d mean
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_504d_base_v015_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log mindshare ratio minus 21d mean
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_21d_base_v016_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log mindshare ratio minus 63d mean
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_63d_base_v017_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log mindshare ratio minus 126d mean
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_126d_base_v018_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log mindshare ratio minus 252d mean
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_252d_base_v019_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log mindshare ratio minus 504d mean
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_504d_base_v020_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_21d_base_v021_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_63d_base_v022_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_126d_base_v023_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_252d_base_v024_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_504d_base_v025_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of revenue vs trailing-mean baseline of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_21d_base_v026_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 21)
    sd = _std(hyperscaler_capex_index, 21)
    result = (revenue - base) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of revenue vs trailing-mean baseline of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_63d_base_v027_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 63)
    sd = _std(hyperscaler_capex_index, 63)
    result = (revenue - base) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of revenue vs trailing-mean baseline of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_126d_base_v028_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 126)
    sd = _std(hyperscaler_capex_index, 126)
    result = (revenue - base) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of revenue vs trailing-mean baseline of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_252d_base_v029_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 252)
    sd = _std(hyperscaler_capex_index, 252)
    result = (revenue - base) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of revenue vs trailing-mean baseline of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_504d_base_v030_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 504)
    sd = _std(hyperscaler_capex_index, 504)
    result = (revenue - base) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of revenue minus ema crossover of hyperscaler (fast 5 vs span 21)
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_21d_base_v031_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=5, adjust=False).mean() - revenue.ewm(span=21, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=5, adjust=False).mean() - hyperscaler_capex_index.ewm(span=21, adjust=False).mean()
    result = rev_x - hyp_x
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of revenue minus ema crossover of hyperscaler (21 vs 63)
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_63d_base_v032_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=21, adjust=False).mean() - revenue.ewm(span=63, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=21, adjust=False).mean() - hyperscaler_capex_index.ewm(span=63, adjust=False).mean()
    result = rev_x - hyp_x
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of revenue minus ema crossover of hyperscaler (63 vs 126)
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_126d_base_v033_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=63, adjust=False).mean() - revenue.ewm(span=126, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=63, adjust=False).mean() - hyperscaler_capex_index.ewm(span=126, adjust=False).mean()
    result = rev_x - hyp_x
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of revenue minus ema crossover of hyperscaler (126 vs 252)
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_252d_base_v034_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=126, adjust=False).mean() - revenue.ewm(span=252, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=126, adjust=False).mean() - hyperscaler_capex_index.ewm(span=252, adjust=False).mean()
    result = rev_x - hyp_x
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of revenue minus ema crossover of hyperscaler (252 vs 504)
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_504d_base_v035_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=252, adjust=False).mean() - revenue.ewm(span=504, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=252, adjust=False).mean() - hyperscaler_capex_index.ewm(span=504, adjust=False).mean()
    result = rev_x - hyp_x
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema diff of revenue minus ema of hyperscaler (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_21d_base_v036_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=21, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=21, adjust=False).mean()
    result = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema diff of revenue minus ema of hyperscaler (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_63d_base_v037_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=63, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=63, adjust=False).mean()
    result = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema diff of revenue minus ema of hyperscaler (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_126d_base_v038_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=126, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=126, adjust=False).mean()
    result = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema diff of revenue minus ema of hyperscaler (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_252d_base_v039_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=252, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=252, adjust=False).mean()
    result = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema diff of revenue minus ema of hyperscaler (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_504d_base_v040_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=504, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=504, adjust=False).mean()
    result = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_21d_base_v041_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    result = yoy - _mean(yoy, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_63d_base_v042_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    result = yoy - _mean(yoy, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_126d_base_v043_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    result = yoy - _mean(yoy, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_252d_base_v044_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    result = yoy - _mean(yoy, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_504d_base_v045_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    result = yoy - _mean(yoy, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hyperscaler YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_21d_base_v046_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    result = yoy - _mean(yoy, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hyperscaler YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_63d_base_v047_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    result = yoy - _mean(yoy, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hyperscaler YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_126d_base_v048_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    result = yoy - _mean(yoy, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hyperscaler YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_252d_base_v049_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    result = yoy - _mean(yoy, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hyperscaler YoY (252-day) log change
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_504d_base_v050_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    result = yoy - _mean(yoy, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of revenue YoY sign matches hyperscaler YoY sign
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_21d_base_v051_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    result = pd.Series(hit.values, index=rv.index).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of revenue YoY sign matches hyperscaler YoY sign
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_63d_base_v052_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    result = pd.Series(hit.values, index=rv.index).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of revenue YoY sign matches hyperscaler YoY sign
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_126d_base_v053_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    result = pd.Series(hit.values, index=rv.index).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of revenue YoY sign matches hyperscaler YoY sign
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_252d_base_v054_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    result = pd.Series(hit.values, index=rv.index).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of revenue YoY sign matches hyperscaler YoY sign
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_504d_base_v055_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    result = pd.Series(hit.values, index=rv.index).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d YoY spread of revenue YoY minus hyperscaler YoY
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_21d_base_v056_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    result = spread - _mean(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d YoY spread of revenue YoY minus hyperscaler YoY
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_63d_base_v057_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    result = spread - _mean(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d YoY spread of revenue YoY minus hyperscaler YoY
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_126d_base_v058_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    result = spread - _mean(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d YoY spread of revenue YoY minus hyperscaler YoY
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_252d_base_v059_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    result = spread - _mean(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d YoY spread of revenue YoY minus hyperscaler YoY
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_504d_base_v060_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    result = spread - _mean(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_21d_base_v061_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_63d_base_v062_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_126d_base_v063_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_252d_base_v064_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_504d_base_v065_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hyperscaler acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_21d_base_v066_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hyperscaler acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_63d_base_v067_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hyperscaler acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_126d_base_v068_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hyperscaler acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_252d_base_v069_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hyperscaler acceleration (YoY diff over 63d)
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_504d_base_v070_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    result = accel - _mean(accel, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional revenue acceleration when hyperscaler also accelerating
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_21d_base_v071_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    result = (racc * mask).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional revenue acceleration when hyperscaler also accelerating
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_63d_base_v072_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    result = (racc * mask).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional revenue acceleration when hyperscaler also accelerating
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_126d_base_v073_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    result = (racc * mask).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional revenue acceleration when hyperscaler also accelerating
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_252d_base_v074_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    result = (racc * mask).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional revenue acceleration when hyperscaler also accelerating
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_504d_base_v075_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    result = (racc * mask).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)
