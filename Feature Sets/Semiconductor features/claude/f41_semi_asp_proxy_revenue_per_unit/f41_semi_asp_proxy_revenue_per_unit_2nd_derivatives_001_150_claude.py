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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f41_rev_per_capex(rev, cx):
    return rev / cx.replace(0, np.nan).abs()


def _f41_rev_per_ppne(rev, pp):
    return rev / pp.replace(0, np.nan).abs()


# 5d slope of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_slope_v001_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_slope_v002_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_slope_v003_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_slope_v004_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_slope_v005_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_slope_v006_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_slope_v007_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_slope_v008_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_slope_v009_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_slope_v010_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_slope_v011_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_slope_v012_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_slope_v013_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_slope_v014_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_slope_v015_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_slope_v016_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_slope_v017_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_slope_v018_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_slope_v019_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_slope_v020_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_slope_v021_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_slope_v022_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_slope_v023_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_slope_v024_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_slope_v025_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_slope_v026_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_slope_v027_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_slope_v028_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_slope_v029_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_slope_v030_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_slope_v031_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_slope_v032_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_slope_v033_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_slope_v034_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_slope_v035_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_slope_v036_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_slope_v037_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_slope_v038_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_slope_v039_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_slope_v040_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_slope_v041_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_slope_v042_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_slope_v043_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_slope_v044_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_slope_v045_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_slope_v046_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_slope_v047_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_slope_v048_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_slope_v049_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_slope_v050_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_slope_v051_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_slope_v052_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_slope_v053_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_slope_v054_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_slope_v055_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_slope_v056_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_slope_v057_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_slope_v058_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_slope_v059_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_slope_v060_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_slope_v061_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_slope_v062_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_slope_v063_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_slope_v064_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_slope_v065_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_slope_v066_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_slope_v067_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_slope_v068_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_slope_v069_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_slope_v070_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_slope_v071_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_slope_v072_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_slope_v073_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_slope_v074_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_slope_v075_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_slope_v076_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_slope_v077_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_slope_v078_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_slope_v079_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_slope_v080_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_slope_v081_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_slope_v082_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_slope_v083_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_slope_v084_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_slope_v085_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_slope_v086_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_slope_v087_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_slope_v088_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_slope_v089_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_slope_v090_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_slope_v091_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_slope_v092_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_slope_v093_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_slope_v094_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_slope_v095_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_slope_v096_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_slope_v097_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_slope_v098_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_slope_v099_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_slope_v100_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_slope_v101_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_slope_v102_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_slope_v103_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_slope_v104_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_slope_v105_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_slope_v106_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_slope_v107_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_slope_v108_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_slope_v109_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_slope_v110_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_slope_v111_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_slope_v112_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_slope_v113_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_slope_v114_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_slope_v115_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_slope_v116_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_slope_v117_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_slope_v118_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_slope_v119_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_slope_v120_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_slope_v121_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_slope_v122_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_slope_v123_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_slope_v124_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_slope_v125_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_slope_v126_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_slope_v127_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_slope_v128_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_slope_v129_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_slope_v130_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_slope_v131_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_slope_v132_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_slope_v133_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_slope_v134_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_slope_v135_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_slope_v136_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_slope_v137_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_slope_v138_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_slope_v139_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_slope_v140_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_slope_v141_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_slope_v142_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_slope_v143_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_slope_v144_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_slope_v145_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_slope_v146_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_slope_v147_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_slope_v148_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_slope_v149_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_slope_v150_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
