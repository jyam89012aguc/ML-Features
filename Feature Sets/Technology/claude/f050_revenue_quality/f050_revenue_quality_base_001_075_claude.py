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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f050_rev_to_ocf(revenue, ncfo):
    return revenue / ncfo.replace(0, np.nan).abs()


# 21d mean of rev_to_ocf scaled by closeadj
def f050rvq_f050_revenue_quality_rev_to_ocf_mean_21d_base_v001_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_to_ocf scaled by closeadj
def f050rvq_f050_revenue_quality_rev_to_ocf_mean_63d_base_v002_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_to_ocf scaled by closeadj
def f050rvq_f050_revenue_quality_rev_to_ocf_mean_126d_base_v003_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_to_ocf scaled by closeadj
def f050rvq_f050_revenue_quality_rev_to_ocf_mean_252d_base_v004_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_to_ocf scaled by closeadj
def f050rvq_f050_revenue_quality_rev_to_ocf_mean_504d_base_v005_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_ocf_to_rev_mean_21d_base_v006_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_ocf_to_rev_mean_63d_base_v007_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_ocf_to_rev_mean_126d_base_v008_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_ocf_to_rev_mean_252d_base_v009_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_ocf_to_rev_mean_504d_base_v010_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rcv_growth_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_mean_21d_base_v011_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rcv_growth_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_mean_63d_base_v012_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rcv_growth_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_mean_126d_base_v013_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rcv_growth_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_mean_252d_base_v014_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rcv_growth_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_mean_504d_base_v015_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drev_chg scaled by closeadj
def f050rvq_f050_revenue_quality_drev_chg_mean_21d_base_v016_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drev_chg scaled by closeadj
def f050rvq_f050_revenue_quality_drev_chg_mean_63d_base_v017_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drev_chg scaled by closeadj
def f050rvq_f050_revenue_quality_drev_chg_mean_126d_base_v018_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drev_chg scaled by closeadj
def f050rvq_f050_revenue_quality_drev_chg_mean_252d_base_v019_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drev_chg scaled by closeadj
def f050rvq_f050_revenue_quality_drev_chg_mean_504d_base_v020_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rcv_to_rev_lvl scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_mean_21d_base_v021_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rcv_to_rev_lvl scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_mean_63d_base_v022_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rcv_to_rev_lvl scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_mean_126d_base_v023_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rcv_to_rev_lvl scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_mean_252d_base_v024_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rcv_to_rev_lvl scaled by closeadj
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_mean_504d_base_v025_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drev_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_drev_to_rev_mean_21d_base_v026_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drev_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_drev_to_rev_mean_63d_base_v027_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drev_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_drev_to_rev_mean_126d_base_v028_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drev_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_drev_to_rev_mean_252d_base_v029_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drev_to_rev scaled by closeadj
def f050rvq_f050_revenue_quality_drev_to_rev_mean_504d_base_v030_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_ex_drev scaled by closeadj
def f050rvq_f050_revenue_quality_rev_ex_drev_mean_21d_base_v031_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_ex_drev scaled by closeadj
def f050rvq_f050_revenue_quality_rev_ex_drev_mean_63d_base_v032_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_ex_drev scaled by closeadj
def f050rvq_f050_revenue_quality_rev_ex_drev_mean_126d_base_v033_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_ex_drev scaled by closeadj
def f050rvq_f050_revenue_quality_rev_ex_drev_mean_252d_base_v034_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_ex_drev scaled by closeadj
def f050rvq_f050_revenue_quality_rev_ex_drev_mean_504d_base_v035_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_median_63d_base_v036_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_median_252d_base_v037_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_median_504d_base_v038_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_median_63d_base_v039_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_median_252d_base_v040_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_median_504d_base_v041_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_median_63d_base_v042_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_median_252d_base_v043_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_median_504d_base_v044_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_median_63d_base_v045_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_median_252d_base_v046_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_median_504d_base_v047_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_median_63d_base_v048_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_median_252d_base_v049_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_median_504d_base_v050_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_median_63d_base_v051_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_median_252d_base_v052_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_median_504d_base_v053_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_median_63d_base_v054_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_median_252d_base_v055_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_median_504d_base_v056_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_rmax_252d_base_v057_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_rmax_504d_base_v058_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_rmax_252d_base_v059_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_rmax_504d_base_v060_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_rmax_252d_base_v061_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_rmax_504d_base_v062_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_rmax_252d_base_v063_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_rmax_504d_base_v064_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_rmax_252d_base_v065_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_rmax_504d_base_v066_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_rmax_252d_base_v067_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_rmax_504d_base_v068_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_rmax_252d_base_v069_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_rmax_504d_base_v070_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_rmin_252d_base_v071_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_rmin_504d_base_v072_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_rmin_252d_base_v073_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_rmin_504d_base_v074_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_rmin_252d_base_v075_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

