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


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f97ai_log_ratio(rev, hyp):
    return np.log(rev.replace(0, np.nan).abs() / hyp.replace(0, np.nan).abs())


def _f97ai_ratio(rev, hyp):
    return rev / hyp.replace(0, np.nan)


def _f97ai_log_diff(s, n):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f97ai_roll_corr(a, b, w):
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


def _f97ai_roll_beta(a, b, w):
    cov = a.rolling(w, min_periods=max(2, w // 2)).cov(b)
    var = b.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


# 5d curvature of 21d rolling correlation
def f97ai_f97_semi_ai_compute_demand_proxy_corr_21d_curv_v001_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rolling correlation
def f97ai_f97_semi_ai_compute_demand_proxy_corr_63d_curv_v002_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rolling correlation
def f97ai_f97_semi_ai_compute_demand_proxy_corr_126d_curv_v003_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rolling correlation
def f97ai_f97_semi_ai_compute_demand_proxy_corr_252d_curv_v004_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d rolling correlation
def f97ai_f97_semi_ai_compute_demand_proxy_corr_504d_curv_v005_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d rolling beta
def f97ai_f97_semi_ai_compute_demand_proxy_beta_21d_curv_v006_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rolling beta
def f97ai_f97_semi_ai_compute_demand_proxy_beta_63d_curv_v007_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rolling beta
def f97ai_f97_semi_ai_compute_demand_proxy_beta_126d_curv_v008_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rolling beta
def f97ai_f97_semi_ai_compute_demand_proxy_beta_252d_curv_v009_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d rolling beta
def f97ai_f97_semi_ai_compute_demand_proxy_beta_504d_curv_v010_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_21d_curv_v011_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_63d_curv_v012_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_126d_curv_v013_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_252d_curv_v014_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_ratio_504d_curv_v015_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d log mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_21d_curv_v016_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d log mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_63d_curv_v017_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d log mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_126d_curv_v018_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d log mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_252d_curv_v019_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d log mindshare ratio deviation
def f97ai_f97_semi_ai_compute_demand_proxy_logratio_504d_curv_v020_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _mean(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_21d_curv_v021_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_63d_curv_v022_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_126d_curv_v023_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z-ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_252d_curv_v024_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d z-ratio
def f97ai_f97_semi_ai_compute_demand_proxy_zratio_504d_curv_v025_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-rev (revenue vs hyper baseline)
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_21d_curv_v026_signal(revenue, hyperscaler_capex_index, closeadj):
    m = _mean(hyperscaler_capex_index, 21)
    sd = _std(hyperscaler_capex_index, 21)
    base = (revenue - m) / sd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-rev (revenue vs hyper baseline)
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_63d_curv_v027_signal(revenue, hyperscaler_capex_index, closeadj):
    m = _mean(hyperscaler_capex_index, 63)
    sd = _std(hyperscaler_capex_index, 63)
    base = (revenue - m) / sd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-rev (revenue vs hyper baseline)
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_126d_curv_v028_signal(revenue, hyperscaler_capex_index, closeadj):
    m = _mean(hyperscaler_capex_index, 126)
    sd = _std(hyperscaler_capex_index, 126)
    base = (revenue - m) / sd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z-rev (revenue vs hyper baseline)
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_252d_curv_v029_signal(revenue, hyperscaler_capex_index, closeadj):
    m = _mean(hyperscaler_capex_index, 252)
    sd = _std(hyperscaler_capex_index, 252)
    base = (revenue - m) / sd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d z-rev (revenue vs hyper baseline)
def f97ai_f97_semi_ai_compute_demand_proxy_zrev_504d_curv_v030_signal(revenue, hyperscaler_capex_index, closeadj):
    m = _mean(hyperscaler_capex_index, 504)
    sd = _std(hyperscaler_capex_index, 504)
    base = (revenue - m) / sd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d emafast crossover diff
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_21d_curv_v031_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=5, adjust=False).mean() - revenue.ewm(span=21, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=5, adjust=False).mean() - hyperscaler_capex_index.ewm(span=21, adjust=False).mean()
    base = rev_x - hyp_x
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d emafast crossover diff
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_63d_curv_v032_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=21, adjust=False).mean() - revenue.ewm(span=63, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=21, adjust=False).mean() - hyperscaler_capex_index.ewm(span=63, adjust=False).mean()
    base = rev_x - hyp_x
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d emafast crossover diff
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_126d_curv_v033_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=63, adjust=False).mean() - revenue.ewm(span=126, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=63, adjust=False).mean() - hyperscaler_capex_index.ewm(span=126, adjust=False).mean()
    base = rev_x - hyp_x
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d emafast crossover diff
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_252d_curv_v034_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=126, adjust=False).mean() - revenue.ewm(span=252, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=126, adjust=False).mean() - hyperscaler_capex_index.ewm(span=252, adjust=False).mean()
    base = rev_x - hyp_x
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d emafast crossover diff
def f97ai_f97_semi_ai_compute_demand_proxy_emafast_504d_curv_v035_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_x = revenue.ewm(span=252, adjust=False).mean() - revenue.ewm(span=504, adjust=False).mean()
    hyp_x = hyperscaler_capex_index.ewm(span=252, adjust=False).mean() - hyperscaler_capex_index.ewm(span=504, adjust=False).mean()
    base = rev_x - hyp_x
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d ema diff (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_21d_curv_v036_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=21, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=21, adjust=False).mean()
    base = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d ema diff (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_63d_curv_v037_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=63, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=63, adjust=False).mean()
    base = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d ema diff (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_126d_curv_v038_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=126, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=126, adjust=False).mean()
    base = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ema diff (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_252d_curv_v039_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=252, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=252, adjust=False).mean()
    base = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d ema diff (single span)
def f97ai_f97_semi_ai_compute_demand_proxy_emadiff_504d_curv_v040_signal(revenue, hyperscaler_capex_index, closeadj):
    rev_e = revenue.ewm(span=504, adjust=False).mean()
    hyp_e = hyperscaler_capex_index.ewm(span=504, adjust=False).mean()
    base = np.log(rev_e.replace(0, np.nan).abs() / hyp_e.replace(0, np.nan).abs())
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d revenue YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_21d_curv_v041_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    base = yoy - _mean(yoy, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d revenue YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_63d_curv_v042_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    base = yoy - _mean(yoy, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d revenue YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_126d_curv_v043_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    base = yoy - _mean(yoy, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d revenue YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_252d_curv_v044_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    base = yoy - _mean(yoy, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d revenue YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_revyoy_504d_curv_v045_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    base = yoy - _mean(yoy, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d hyperscaler YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_21d_curv_v046_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    base = yoy - _mean(yoy, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hyperscaler YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_63d_curv_v047_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    base = yoy - _mean(yoy, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d hyperscaler YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_126d_curv_v048_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    base = yoy - _mean(yoy, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d hyperscaler YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_252d_curv_v049_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    base = yoy - _mean(yoy, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d hyperscaler YoY deviation
def f97ai_f97_semi_ai_compute_demand_proxy_hypyoy_504d_curv_v050_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    base = yoy - _mean(yoy, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d yoy hit ratio
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_21d_curv_v051_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    base = pd.Series(hit.values, index=rv.index).rolling(21, min_periods=11).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d yoy hit ratio
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_63d_curv_v052_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    base = pd.Series(hit.values, index=rv.index).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d yoy hit ratio
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_126d_curv_v053_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    base = pd.Series(hit.values, index=rv.index).rolling(126, min_periods=63).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d yoy hit ratio
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_252d_curv_v054_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    base = pd.Series(hit.values, index=rv.index).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d yoy hit ratio
def f97ai_f97_semi_ai_compute_demand_proxy_yoyhit_504d_curv_v055_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    hit = (np.sign(rv) == np.sign(hv)).astype(float)
    base = pd.Series(hit.values, index=rv.index).rolling(504, min_periods=252).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d YoY spread deviation
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_21d_curv_v056_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    base = spread - _mean(spread, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d YoY spread deviation
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_63d_curv_v057_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    base = spread - _mean(spread, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d YoY spread deviation
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_126d_curv_v058_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    base = spread - _mean(spread, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d YoY spread deviation
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_252d_curv_v059_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    base = spread - _mean(spread, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d YoY spread deviation
def f97ai_f97_semi_ai_compute_demand_proxy_yoyspread_504d_curv_v060_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    spread = rv - hv
    base = spread - _mean(spread, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d revenue acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_21d_curv_v061_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d revenue acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_63d_curv_v062_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d revenue acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_126d_curv_v063_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d revenue acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_252d_curv_v064_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d revenue acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelrev_504d_curv_v065_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(revenue, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d hyperscaler acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_21d_curv_v066_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hyperscaler acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_63d_curv_v067_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d hyperscaler acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_126d_curv_v068_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d hyperscaler acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_252d_curv_v069_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d hyperscaler acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_accelhyp_504d_curv_v070_signal(revenue, hyperscaler_capex_index, closeadj):
    yoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    accel = yoy - yoy.shift(63)
    base = accel - _mean(accel, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d conditional acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_21d_curv_v071_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    base = (racc * mask).rolling(21, min_periods=11).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d conditional acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_63d_curv_v072_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    base = (racc * mask).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d conditional acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_126d_curv_v073_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    base = (racc * mask).rolling(126, min_periods=63).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d conditional acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_252d_curv_v074_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    base = (racc * mask).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d conditional acceleration
def f97ai_f97_semi_ai_compute_demand_proxy_condacc_504d_curv_v075_signal(revenue, hyperscaler_capex_index, closeadj):
    ryoy = _f97ai_log_diff(revenue, 252)
    hyoy = _f97ai_log_diff(hyperscaler_capex_index, 252)
    racc = ryoy - ryoy.shift(63)
    hacc = hyoy - hyoy.shift(63)
    mask = (hacc > 0).astype(float)
    base = (racc * mask).rolling(504, min_periods=252).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio drawdown
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_21d_curv_v076_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio drawdown
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_63d_curv_v077_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio drawdown
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_126d_curv_v078_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio drawdown
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_252d_curv_v079_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio drawdown
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_504d_curv_v080_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio runup
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_21d_curv_v081_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio runup
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_63d_curv_v082_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio runup
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_126d_curv_v083_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio runup
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_252d_curv_v084_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio runup
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_504d_curv_v085_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = r - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_21d_curv_v086_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_63d_curv_v087_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_126d_curv_v088_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_252d_curv_v089_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_504d_curv_v090_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio position
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_21d_curv_v091_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 21)
    hi = _max(r, 21)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio position
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_63d_curv_v092_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 63)
    hi = _max(r, 63)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio position
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_126d_curv_v093_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 126)
    hi = _max(r, 126)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio position
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_252d_curv_v094_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 252)
    hi = _max(r, 252)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio position
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_504d_curv_v095_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 504)
    hi = _max(r, 504)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio max
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_21d_curv_v096_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio max
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_63d_curv_v097_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio max
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_126d_curv_v098_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio max
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_252d_curv_v099_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio max
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_504d_curv_v100_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d mindshare ratio min
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_21d_curv_v101_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d mindshare ratio min
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_63d_curv_v102_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mindshare ratio min
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_126d_curv_v103_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d mindshare ratio min
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_252d_curv_v104_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d mindshare ratio min
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_504d_curv_v105_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d tracking volatility
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_21d_curv_v106_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    base = _std(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d tracking volatility
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_63d_curv_v107_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    base = _std(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d tracking volatility
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_126d_curv_v108_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    base = _std(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d tracking volatility
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_252d_curv_v109_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    base = _std(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d tracking volatility
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_504d_curv_v110_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    base = _std(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d rev deviation vs hyper baseline
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_21d_curv_v111_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 21)
    dev = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    result = _curvature(dev, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rev deviation vs hyper baseline
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_63d_curv_v112_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 63)
    dev = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    result = _curvature(dev, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rev deviation vs hyper baseline
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_126d_curv_v113_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 126)
    dev = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    result = _curvature(dev, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rev deviation vs hyper baseline
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_252d_curv_v114_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 252)
    dev = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    result = _curvature(dev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d rev deviation vs hyper baseline
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_504d_curv_v115_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 504)
    dev = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    result = _curvature(dev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d cumulative return diff
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_21d_curv_v116_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    base = diff.rolling(21, min_periods=11).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cumulative return diff
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_63d_curv_v117_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    base = diff.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cumulative return diff
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_126d_curv_v118_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    base = diff.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d cumulative return diff
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_252d_curv_v119_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    base = diff.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d cumulative return diff
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_504d_curv_v120_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    base = diff.rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d tracking error
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_21d_curv_v121_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    base = _std(diff, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d tracking error
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_63d_curv_v122_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    base = _std(diff, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d tracking error
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_126d_curv_v123_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    base = _std(diff, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d tracking error
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_252d_curv_v124_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    base = _std(diff, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d tracking error
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_504d_curv_v125_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    base = _std(diff, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d corr trend
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_21d_curv_v126_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 21)
    base = c - _mean(c, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d corr trend
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_63d_curv_v127_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 63)
    base = c - _mean(c, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d corr trend
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_126d_curv_v128_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 126)
    base = c - _mean(c, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d corr trend
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_252d_curv_v129_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 252)
    base = c - _mean(c, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d corr trend
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_504d_curv_v130_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 504)
    base = c - _mean(c, 756)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d composite signal
def f97ai_f97_semi_ai_compute_demand_proxy_composite_21d_curv_v131_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 21)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 21)
    base = _z(c, 252) + _z(b, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d composite signal
def f97ai_f97_semi_ai_compute_demand_proxy_composite_63d_curv_v132_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 63)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 63)
    base = _z(c, 252) + _z(b, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d composite signal
def f97ai_f97_semi_ai_compute_demand_proxy_composite_126d_curv_v133_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 126)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 126)
    base = _z(c, 252) + _z(b, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d composite signal
def f97ai_f97_semi_ai_compute_demand_proxy_composite_252d_curv_v134_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 252)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 252)
    base = _z(c, 504) + _z(b, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d composite signal
def f97ai_f97_semi_ai_compute_demand_proxy_composite_504d_curv_v135_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 504)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 504)
    base = _z(c, 504) + _z(b, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d robust z
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_21d_curv_v136_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_63d_curv_v137_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d robust z
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_126d_curv_v138_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d robust z
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_252d_curv_v139_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robust z
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_504d_curv_v140_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d yoy sign cumulative
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_21d_curv_v141_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    base = s.rolling(21, min_periods=11).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d yoy sign cumulative
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_63d_curv_v142_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    base = s.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d yoy sign cumulative
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_126d_curv_v143_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    base = s.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d yoy sign cumulative
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_252d_curv_v144_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    base = s.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d yoy sign cumulative
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_504d_curv_v145_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    base = s.rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d regime interaction
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_21d_curv_v146_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 21)
    zh = _z(hyperscaler_capex_index, 21)
    base = zr * zh
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d regime interaction
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_63d_curv_v147_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 63)
    zh = _z(hyperscaler_capex_index, 63)
    base = zr * zh
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d regime interaction
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_126d_curv_v148_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 126)
    zh = _z(hyperscaler_capex_index, 126)
    base = zr * zh
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d regime interaction
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_252d_curv_v149_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 252)
    zh = _z(hyperscaler_capex_index, 252)
    base = zr * zh
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d regime interaction
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_504d_curv_v150_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 504)
    zh = _z(hyperscaler_capex_index, 504)
    base = zr * zh
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)
