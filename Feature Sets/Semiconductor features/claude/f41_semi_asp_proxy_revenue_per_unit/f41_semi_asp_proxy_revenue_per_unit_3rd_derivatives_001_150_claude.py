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


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


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


# 5d curvature of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_curv_v001_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_curv_v002_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_curv_v003_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_curv_v004_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of revenue per capex (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_21d_curv_v005_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_curv_v006_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_curv_v007_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_curv_v008_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_curv_v009_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of revenue per capex (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_level_63d_curv_v010_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_curv_v011_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_curv_v012_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_curv_v013_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_curv_v014_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_21d_curv_v015_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_curv_v016_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_curv_v017_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_curv_v018_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_curv_v019_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_63d_curv_v020_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_curv_v021_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_curv_v022_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_curv_v023_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_curv_v024_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_z_126d_curv_v025_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_curv_v026_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_curv_v027_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_curv_v028_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_curv_v029_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_rng_63d_curv_v030_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_curv_v031_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_curv_v032_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_curv_v033_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_curv_v034_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of revenue per capex (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_pos_63d_curv_v035_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_curv_v036_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_curv_v037_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_curv_v038_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_curv_v039_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of revenue per capex (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_dd_63d_curv_v040_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_curv_v041_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_curv_v042_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_curv_v043_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_curv_v044_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of revenue per capex (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_up_63d_curv_v045_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_curv_v046_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_curv_v047_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_curv_v048_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_curv_v049_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_std_63d_curv_v050_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_curv_v051_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_curv_v052_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_curv_v053_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_curv_v054_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_ema_63d_curv_v055_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_curv_v056_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_curv_v057_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_curv_v058_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_curv_v059_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive revenue per capex (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_hit_63d_curv_v060_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_curv_v061_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_curv_v062_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_curv_v063_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_curv_v064_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_cumsign_63d_curv_v065_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_curv_v066_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_curv_v067_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_curv_v068_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_curv_v069_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_robustz_63d_curv_v070_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_curv_v071_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_curv_v072_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_curv_v073_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_curv_v074_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of revenue per capex (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpc_skew_63d_curv_v075_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_capex(revenue, capex)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_curv_v076_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_curv_v077_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_curv_v078_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_curv_v079_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of revenue per PPNE (ASP proxy) (21d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_21d_curv_v080_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_curv_v081_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_curv_v082_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_curv_v083_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_curv_v084_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of revenue per PPNE (ASP proxy) (63d mean-centered)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_level_63d_curv_v085_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_curv_v086_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_curv_v087_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_curv_v088_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_curv_v089_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_21d_curv_v090_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_curv_v091_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_curv_v092_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_curv_v093_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_curv_v094_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_63d_curv_v095_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_curv_v096_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_curv_v097_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_curv_v098_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_curv_v099_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_z_126d_curv_v100_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_curv_v101_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_curv_v102_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_curv_v103_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_curv_v104_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_rng_63d_curv_v105_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_curv_v106_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_curv_v107_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_curv_v108_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_curv_v109_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of revenue per PPNE (ASP proxy) in rolling range
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_pos_63d_curv_v110_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_curv_v111_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_curv_v112_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_curv_v113_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_curv_v114_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of revenue per PPNE (ASP proxy) from peak
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_dd_63d_curv_v115_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_curv_v116_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_curv_v117_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_curv_v118_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_curv_v119_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of revenue per PPNE (ASP proxy) above trough
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_up_63d_curv_v120_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_curv_v121_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_curv_v122_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_curv_v123_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_curv_v124_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_std_63d_curv_v125_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_curv_v126_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_curv_v127_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_curv_v128_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_curv_v129_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_ema_63d_curv_v130_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_curv_v131_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_curv_v132_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_curv_v133_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_curv_v134_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive revenue per PPNE (ASP proxy) changes
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_hit_63d_curv_v135_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_curv_v136_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_curv_v137_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_curv_v138_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_curv_v139_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_cumsign_63d_curv_v140_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_curv_v141_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_curv_v142_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_curv_v143_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_curv_v144_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_robustz_63d_curv_v145_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_curv_v146_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_curv_v147_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_curv_v148_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_curv_v149_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of revenue per PPNE (ASP proxy)
def f41asp_semi_asp_proxy_revenue_per_unit_rpp_skew_63d_curv_v150_signal(revenue, capex, ppne, closeadj):
    m = _f41_rev_per_ppne(revenue, ppne)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
