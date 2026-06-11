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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f050_rev_to_ocf(revenue, ncfo):
    return revenue / ncfo.replace(0, np.nan).abs()


# 21d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slope_21d_2d_v001_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slope_63d_2d_v002_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slope_126d_2d_v003_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slope_252d_2d_v004_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slope_504d_2d_v005_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slope_21d_2d_v006_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slope_63d_2d_v007_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slope_126d_2d_v008_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slope_252d_2d_v009_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slope_504d_2d_v010_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slope_21d_2d_v011_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slope_63d_2d_v012_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slope_126d_2d_v013_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slope_252d_2d_v014_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slope_504d_2d_v015_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slope_21d_2d_v016_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slope_63d_2d_v017_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slope_126d_2d_v018_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slope_252d_2d_v019_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slope_504d_2d_v020_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slope_21d_2d_v021_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slope_63d_2d_v022_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slope_126d_2d_v023_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slope_252d_2d_v024_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slope_504d_2d_v025_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slope_21d_2d_v026_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slope_63d_2d_v027_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slope_126d_2d_v028_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slope_252d_2d_v029_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slope_504d_2d_v030_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slope_21d_2d_v031_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slope_63d_2d_v032_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slope_126d_2d_v033_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slope_252d_2d_v034_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slope_504d_2d_v035_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sm21_sl21_2d_v036_signal(revenue, ncfo, closeadj):
    base = _mean(_f050_rev_to_ocf(revenue, ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sm63_sl21_2d_v037_signal(revenue, ncfo, closeadj):
    base = _mean(_f050_rev_to_ocf(revenue, ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sm63_sl63_2d_v038_signal(revenue, ncfo, closeadj):
    base = _mean(_f050_rev_to_ocf(revenue, ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sm252_sl63_2d_v039_signal(revenue, ncfo, closeadj):
    base = _mean(_f050_rev_to_ocf(revenue, ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sm252_sl126_2d_v040_signal(revenue, ncfo, closeadj):
    base = _mean(_f050_rev_to_ocf(revenue, ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sm21_sl21_2d_v041_signal(ncfo, revenue, closeadj):
    base = _mean(ncfo / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sm63_sl21_2d_v042_signal(ncfo, revenue, closeadj):
    base = _mean(ncfo / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sm63_sl63_2d_v043_signal(ncfo, revenue, closeadj):
    base = _mean(ncfo / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sm252_sl63_2d_v044_signal(ncfo, revenue, closeadj):
    base = _mean(ncfo / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sm252_sl126_2d_v045_signal(ncfo, revenue, closeadj):
    base = _mean(ncfo / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sm21_sl21_2d_v046_signal(receivables, revenue, closeadj):
    base = _mean(receivables.pct_change(periods=252) - revenue.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sm63_sl21_2d_v047_signal(receivables, revenue, closeadj):
    base = _mean(receivables.pct_change(periods=252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sm63_sl63_2d_v048_signal(receivables, revenue, closeadj):
    base = _mean(receivables.pct_change(periods=252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sm252_sl63_2d_v049_signal(receivables, revenue, closeadj):
    base = _mean(receivables.pct_change(periods=252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sm252_sl126_2d_v050_signal(receivables, revenue, closeadj):
    base = _mean(receivables.pct_change(periods=252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sm21_sl21_2d_v051_signal(deferredrev, closeadj):
    base = _mean(deferredrev.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sm63_sl21_2d_v052_signal(deferredrev, closeadj):
    base = _mean(deferredrev.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sm63_sl63_2d_v053_signal(deferredrev, closeadj):
    base = _mean(deferredrev.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sm252_sl63_2d_v054_signal(deferredrev, closeadj):
    base = _mean(deferredrev.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sm252_sl126_2d_v055_signal(deferredrev, closeadj):
    base = _mean(deferredrev.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sm21_sl21_2d_v056_signal(receivables, revenue, closeadj):
    base = _mean(receivables / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sm63_sl21_2d_v057_signal(receivables, revenue, closeadj):
    base = _mean(receivables / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sm63_sl63_2d_v058_signal(receivables, revenue, closeadj):
    base = _mean(receivables / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sm252_sl63_2d_v059_signal(receivables, revenue, closeadj):
    base = _mean(receivables / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sm252_sl126_2d_v060_signal(receivables, revenue, closeadj):
    base = _mean(receivables / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sm21_sl21_2d_v061_signal(deferredrev, revenue, closeadj):
    base = _mean(deferredrev / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sm63_sl21_2d_v062_signal(deferredrev, revenue, closeadj):
    base = _mean(deferredrev / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sm63_sl63_2d_v063_signal(deferredrev, revenue, closeadj):
    base = _mean(deferredrev / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sm252_sl63_2d_v064_signal(deferredrev, revenue, closeadj):
    base = _mean(deferredrev / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sm252_sl126_2d_v065_signal(deferredrev, revenue, closeadj):
    base = _mean(deferredrev / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sm21_sl21_2d_v066_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue - deferredrev.diff(periods=63).fillna(0)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sm63_sl21_2d_v067_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue - deferredrev.diff(periods=63).fillna(0)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sm63_sl63_2d_v068_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue - deferredrev.diff(periods=63).fillna(0)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sm252_sl63_2d_v069_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue - deferredrev.diff(periods=63).fillna(0)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sm252_sl126_2d_v070_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue - deferredrev.diff(periods=63).fillna(0)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_pctslope_21d_2d_v071_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_pctslope_63d_2d_v072_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_pctslope_252d_2d_v073_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_pctslope_21d_2d_v074_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_pctslope_63d_2d_v075_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_pctslope_252d_2d_v076_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_pctslope_21d_2d_v077_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_pctslope_63d_2d_v078_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_pctslope_252d_2d_v079_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_pctslope_21d_2d_v080_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_pctslope_63d_2d_v081_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_pctslope_252d_2d_v082_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_pctslope_21d_2d_v083_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_pctslope_63d_2d_v084_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_pctslope_252d_2d_v085_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_pctslope_21d_2d_v086_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_pctslope_63d_2d_v087_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_pctslope_252d_2d_v088_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_pctslope_21d_2d_v089_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_pctslope_63d_2d_v090_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_pctslope_252d_2d_v091_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sgnslope_21d_2d_v092_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sgnslope_63d_2d_v093_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_sgnslope_252d_2d_v094_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sgnslope_21d_2d_v095_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sgnslope_63d_2d_v096_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_sgnslope_252d_2d_v097_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sgnslope_21d_2d_v098_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sgnslope_63d_2d_v099_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_sgnslope_252d_2d_v100_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sgnslope_21d_2d_v101_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sgnslope_63d_2d_v102_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_sgnslope_252d_2d_v103_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sgnslope_21d_2d_v104_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sgnslope_63d_2d_v105_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_sgnslope_252d_2d_v106_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sgnslope_21d_2d_v107_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sgnslope_63d_2d_v108_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_sgnslope_252d_2d_v109_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sgnslope_21d_2d_v110_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sgnslope_63d_2d_v111_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_sgnslope_252d_2d_v112_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_logmagslope_21d_2d_v113_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_logmagslope_63d_2d_v114_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_logmagslope_252d_2d_v115_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_logmagslope_21d_2d_v116_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_logmagslope_63d_2d_v117_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_logmagslope_252d_2d_v118_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_logmagslope_21d_2d_v119_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_logmagslope_63d_2d_v120_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_logmagslope_252d_2d_v121_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_logmagslope_21d_2d_v122_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_logmagslope_63d_2d_v123_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_logmagslope_252d_2d_v124_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_logmagslope_21d_2d_v125_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_logmagslope_63d_2d_v126_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_logmagslope_252d_2d_v127_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_logmagslope_21d_2d_v128_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_logmagslope_63d_2d_v129_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_logmagslope_252d_2d_v130_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_logmagslope_21d_2d_v131_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_logmagslope_63d_2d_v132_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_logmagslope_252d_2d_v133_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_to_ocf|
def f050rvq_f050_revenue_quality_rev_to_ocf_logslope_63d_2d_v134_signal(revenue, ncfo, closeadj):
    base = np.log((_f050_rev_to_ocf(revenue, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_to_ocf|
def f050rvq_f050_revenue_quality_rev_to_ocf_logslope_252d_2d_v135_signal(revenue, ncfo, closeadj):
    base = np.log((_f050_rev_to_ocf(revenue, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_to_rev|
def f050rvq_f050_revenue_quality_ocf_to_rev_logslope_63d_2d_v136_signal(ncfo, revenue, closeadj):
    base = np.log((ncfo / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_to_rev|
def f050rvq_f050_revenue_quality_ocf_to_rev_logslope_252d_2d_v137_signal(ncfo, revenue, closeadj):
    base = np.log((ncfo / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rcv_growth_to_rev|
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_logslope_63d_2d_v138_signal(receivables, revenue, closeadj):
    base = np.log((receivables.pct_change(periods=252) - revenue.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rcv_growth_to_rev|
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_logslope_252d_2d_v139_signal(receivables, revenue, closeadj):
    base = np.log((receivables.pct_change(periods=252) - revenue.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drev_chg|
def f050rvq_f050_revenue_quality_drev_chg_logslope_63d_2d_v140_signal(deferredrev, closeadj):
    base = np.log((deferredrev.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drev_chg|
def f050rvq_f050_revenue_quality_drev_chg_logslope_252d_2d_v141_signal(deferredrev, closeadj):
    base = np.log((deferredrev.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rcv_to_rev_lvl|
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_logslope_63d_2d_v142_signal(receivables, revenue, closeadj):
    base = np.log((receivables / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rcv_to_rev_lvl|
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_logslope_252d_2d_v143_signal(receivables, revenue, closeadj):
    base = np.log((receivables / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drev_to_rev|
def f050rvq_f050_revenue_quality_drev_to_rev_logslope_63d_2d_v144_signal(deferredrev, revenue, closeadj):
    base = np.log((deferredrev / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drev_to_rev|
def f050rvq_f050_revenue_quality_drev_to_rev_logslope_252d_2d_v145_signal(deferredrev, revenue, closeadj):
    base = np.log((deferredrev / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_ex_drev|
def f050rvq_f050_revenue_quality_rev_ex_drev_logslope_63d_2d_v146_signal(revenue, deferredrev, closeadj):
    base = np.log(((revenue - deferredrev.diff(periods=63).fillna(0))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_ex_drev|
def f050rvq_f050_revenue_quality_rev_ex_drev_logslope_252d_2d_v147_signal(revenue, deferredrev, closeadj):
    base = np.log(((revenue - deferredrev.diff(periods=63).fillna(0))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

