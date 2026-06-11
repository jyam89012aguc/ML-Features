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


# 21d acceleration of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_accel_21d_3d_v001_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_accel_63d_3d_v002_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_accel_126d_3d_v003_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_accel_252d_3d_v004_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_accel_21d_3d_v005_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_accel_63d_3d_v006_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_accel_126d_3d_v007_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_accel_252d_3d_v008_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_accel_21d_3d_v009_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_accel_63d_3d_v010_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_accel_126d_3d_v011_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_accel_252d_3d_v012_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_accel_21d_3d_v013_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_accel_63d_3d_v014_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_accel_126d_3d_v015_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_accel_252d_3d_v016_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_accel_21d_3d_v017_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_accel_63d_3d_v018_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_accel_126d_3d_v019_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_accel_252d_3d_v020_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_accel_21d_3d_v021_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_accel_63d_3d_v022_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_accel_126d_3d_v023_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_accel_252d_3d_v024_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_accel_21d_3d_v025_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_accel_63d_3d_v026_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_accel_126d_3d_v027_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_accel_252d_3d_v028_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slopez_21d_z126_3d_v029_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slopez_63d_z252_3d_v030_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slopez_126d_z252_3d_v031_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_slopez_252d_z504_3d_v032_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slopez_21d_z126_3d_v033_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slopez_63d_z252_3d_v034_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slopez_126d_z252_3d_v035_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_slopez_252d_z504_3d_v036_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slopez_21d_z126_3d_v037_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slopez_63d_z252_3d_v038_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slopez_126d_z252_3d_v039_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_slopez_252d_z504_3d_v040_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slopez_21d_z126_3d_v041_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slopez_63d_z252_3d_v042_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slopez_126d_z252_3d_v043_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_slopez_252d_z504_3d_v044_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slopez_21d_z126_3d_v045_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slopez_63d_z252_3d_v046_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slopez_126d_z252_3d_v047_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_slopez_252d_z504_3d_v048_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slopez_21d_z126_3d_v049_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slopez_63d_z252_3d_v050_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slopez_126d_z252_3d_v051_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_slopez_252d_z504_3d_v052_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slopez_21d_z126_3d_v053_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slopez_63d_z252_3d_v054_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slopez_126d_z252_3d_v055_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_slopez_252d_z504_3d_v056_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_jerk_21d_3d_v057_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_jerk_63d_3d_v058_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_jerk_126d_3d_v059_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_jerk_21d_3d_v060_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_jerk_63d_3d_v061_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_jerk_126d_3d_v062_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_jerk_21d_3d_v063_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_jerk_63d_3d_v064_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_jerk_126d_3d_v065_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_jerk_21d_3d_v066_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_jerk_63d_3d_v067_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_jerk_126d_3d_v068_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_jerk_21d_3d_v069_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_jerk_63d_3d_v070_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_jerk_126d_3d_v071_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_jerk_21d_3d_v072_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_jerk_63d_3d_v073_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_jerk_126d_3d_v074_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_jerk_21d_3d_v075_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_jerk_63d_3d_v076_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_jerk_126d_3d_v077_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_to_ocf smoothed over 252d
def f050rvq_f050_revenue_quality_rev_to_ocf_smoothaccel_63d_sm252_3d_v078_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_to_ocf smoothed over 504d
def f050rvq_f050_revenue_quality_rev_to_ocf_smoothaccel_252d_sm504_3d_v079_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_rev smoothed over 252d
def f050rvq_f050_revenue_quality_ocf_to_rev_smoothaccel_63d_sm252_3d_v080_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_rev smoothed over 504d
def f050rvq_f050_revenue_quality_ocf_to_rev_smoothaccel_252d_sm504_3d_v081_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rcv_growth_to_rev smoothed over 252d
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_smoothaccel_63d_sm252_3d_v082_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rcv_growth_to_rev smoothed over 504d
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_smoothaccel_252d_sm504_3d_v083_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drev_chg smoothed over 252d
def f050rvq_f050_revenue_quality_drev_chg_smoothaccel_63d_sm252_3d_v084_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drev_chg smoothed over 504d
def f050rvq_f050_revenue_quality_drev_chg_smoothaccel_252d_sm504_3d_v085_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rcv_to_rev_lvl smoothed over 252d
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_smoothaccel_63d_sm252_3d_v086_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rcv_to_rev_lvl smoothed over 504d
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_smoothaccel_252d_sm504_3d_v087_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drev_to_rev smoothed over 252d
def f050rvq_f050_revenue_quality_drev_to_rev_smoothaccel_63d_sm252_3d_v088_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drev_to_rev smoothed over 504d
def f050rvq_f050_revenue_quality_drev_to_rev_smoothaccel_252d_sm504_3d_v089_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_ex_drev smoothed over 252d
def f050rvq_f050_revenue_quality_rev_ex_drev_smoothaccel_63d_sm252_3d_v090_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_ex_drev smoothed over 504d
def f050rvq_f050_revenue_quality_rev_ex_drev_smoothaccel_252d_sm504_3d_v091_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_accelz_21d_z252_3d_v092_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_accelz_63d_z504_3d_v093_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_accelz_21d_z252_3d_v094_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_accelz_63d_z504_3d_v095_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_accelz_21d_z252_3d_v096_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_accelz_63d_z504_3d_v097_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_accelz_21d_z252_3d_v098_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_accelz_63d_z504_3d_v099_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_accelz_21d_z252_3d_v100_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_accelz_63d_z504_3d_v101_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_accelz_21d_z252_3d_v102_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_accelz_63d_z504_3d_v103_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_accelz_21d_z252_3d_v104_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_accelz_63d_z504_3d_v105_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_to_ocf (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rev_to_ocf_signflip_63d_3d_v106_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_to_ocf (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rev_to_ocf_signflip_252d_3d_v107_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_rev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_ocf_to_rev_signflip_63d_3d_v108_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_rev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_ocf_to_rev_signflip_252d_3d_v109_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rcv_growth_to_rev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_signflip_63d_3d_v110_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rcv_growth_to_rev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_signflip_252d_3d_v111_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drev_chg (raw count, no price scaling)
def f050rvq_f050_revenue_quality_drev_chg_signflip_63d_3d_v112_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drev_chg (raw count, no price scaling)
def f050rvq_f050_revenue_quality_drev_chg_signflip_252d_3d_v113_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rcv_to_rev_lvl (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_signflip_63d_3d_v114_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rcv_to_rev_lvl (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_signflip_252d_3d_v115_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drev_to_rev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_drev_to_rev_signflip_63d_3d_v116_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drev_to_rev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_drev_to_rev_signflip_252d_3d_v117_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_ex_drev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rev_ex_drev_signflip_63d_3d_v118_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_ex_drev (raw count, no price scaling)
def f050rvq_f050_revenue_quality_rev_ex_drev_signflip_252d_3d_v119_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_to_ocf normalized by 252d range
def f050rvq_f050_revenue_quality_rev_to_ocf_rngaccel_63d_r252_3d_v120_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_to_ocf normalized by 504d range
def f050rvq_f050_revenue_quality_rev_to_ocf_rngaccel_252d_r504_3d_v121_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_rev normalized by 252d range
def f050rvq_f050_revenue_quality_ocf_to_rev_rngaccel_63d_r252_3d_v122_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_rev normalized by 504d range
def f050rvq_f050_revenue_quality_ocf_to_rev_rngaccel_252d_r504_3d_v123_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_growth_to_rev normalized by 252d range
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_rngaccel_63d_r252_3d_v124_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_growth_to_rev normalized by 504d range
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_rngaccel_252d_r504_3d_v125_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_chg normalized by 252d range
def f050rvq_f050_revenue_quality_drev_chg_rngaccel_63d_r252_3d_v126_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_chg normalized by 504d range
def f050rvq_f050_revenue_quality_drev_chg_rngaccel_252d_r504_3d_v127_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_to_rev_lvl normalized by 252d range
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_rngaccel_63d_r252_3d_v128_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_to_rev_lvl normalized by 504d range
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_rngaccel_252d_r504_3d_v129_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_to_rev normalized by 252d range
def f050rvq_f050_revenue_quality_drev_to_rev_rngaccel_63d_r252_3d_v130_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_to_rev normalized by 504d range
def f050rvq_f050_revenue_quality_drev_to_rev_rngaccel_252d_r504_3d_v131_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_ex_drev normalized by 252d range
def f050rvq_f050_revenue_quality_rev_ex_drev_rngaccel_63d_r252_3d_v132_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_ex_drev normalized by 504d range
def f050rvq_f050_revenue_quality_rev_ex_drev_rngaccel_252d_r504_3d_v133_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_cumslope_21d_3d_v134_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_cumslope_63d_3d_v135_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_cumslope_252d_3d_v136_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_cumslope_21d_3d_v137_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_cumslope_63d_3d_v138_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_cumslope_252d_3d_v139_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_cumslope_21d_3d_v140_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_cumslope_63d_3d_v141_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_cumslope_252d_3d_v142_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_cumslope_21d_3d_v143_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_cumslope_63d_3d_v144_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_cumslope_252d_3d_v145_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_cumslope_21d_3d_v146_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_cumslope_63d_3d_v147_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_cumslope_252d_3d_v148_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_cumslope_21d_3d_v149_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_cumslope_63d_3d_v150_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

