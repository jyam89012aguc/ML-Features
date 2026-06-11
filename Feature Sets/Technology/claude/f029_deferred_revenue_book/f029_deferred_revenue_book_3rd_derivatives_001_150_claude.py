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
def _f029_drev_to_rev(deferredrev, revenue):
    return deferredrev / revenue.abs().replace(0, np.nan)


# 21d acceleration of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_accel_21d_3d_v001_signal(deferredrev, closeadj):
    base = deferredrev
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_accel_63d_3d_v002_signal(deferredrev, closeadj):
    base = deferredrev
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_accel_126d_3d_v003_signal(deferredrev, closeadj):
    base = deferredrev
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_accel_252d_3d_v004_signal(deferredrev, closeadj):
    base = deferredrev
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_accel_21d_3d_v005_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_accel_63d_3d_v006_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_accel_126d_3d_v007_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_accel_252d_3d_v008_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_accel_21d_3d_v009_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_accel_63d_3d_v010_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_accel_126d_3d_v011_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_accel_252d_3d_v012_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_accel_21d_3d_v013_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_accel_63d_3d_v014_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_accel_126d_3d_v015_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_accel_252d_3d_v016_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_accel_21d_3d_v017_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_accel_63d_3d_v018_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_accel_126d_3d_v019_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_accel_252d_3d_v020_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_accel_21d_3d_v021_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_accel_63d_3d_v022_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_accel_126d_3d_v023_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_accel_252d_3d_v024_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_accel_21d_3d_v025_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_accel_63d_3d_v026_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_accel_126d_3d_v027_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_accel_252d_3d_v028_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slopez_21d_z126_3d_v029_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slopez_63d_z252_3d_v030_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slopez_126d_z252_3d_v031_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slopez_252d_z504_3d_v032_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slopez_21d_z126_3d_v033_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slopez_63d_z252_3d_v034_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slopez_126d_z252_3d_v035_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slopez_252d_z504_3d_v036_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slopez_21d_z126_3d_v037_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slopez_63d_z252_3d_v038_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slopez_126d_z252_3d_v039_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slopez_252d_z504_3d_v040_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slopez_21d_z126_3d_v041_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slopez_63d_z252_3d_v042_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slopez_126d_z252_3d_v043_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slopez_252d_z504_3d_v044_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slopez_21d_z126_3d_v045_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slopez_63d_z252_3d_v046_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slopez_126d_z252_3d_v047_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slopez_252d_z504_3d_v048_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slopez_21d_z126_3d_v049_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slopez_63d_z252_3d_v050_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slopez_126d_z252_3d_v051_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slopez_252d_z504_3d_v052_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slopez_21d_z126_3d_v053_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slopez_63d_z252_3d_v054_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slopez_126d_z252_3d_v055_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slopez_252d_z504_3d_v056_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_jerk_21d_3d_v057_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_jerk_63d_3d_v058_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_jerk_126d_3d_v059_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_jerk_21d_3d_v060_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_jerk_63d_3d_v061_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_jerk_126d_3d_v062_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_jerk_21d_3d_v063_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_jerk_63d_3d_v064_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_jerk_126d_3d_v065_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_jerk_21d_3d_v066_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_jerk_63d_3d_v067_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_jerk_126d_3d_v068_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_jerk_21d_3d_v069_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_jerk_63d_3d_v070_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_jerk_126d_3d_v071_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_jerk_21d_3d_v072_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_jerk_63d_3d_v073_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_jerk_126d_3d_v074_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_jerk_21d_3d_v075_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_jerk_63d_3d_v076_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_jerk_126d_3d_v077_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drev_lvl smoothed over 252d
def f029drb_f029_deferred_revenue_book_drev_lvl_smoothaccel_63d_sm252_3d_v078_signal(deferredrev, closeadj):
    base = deferredrev
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drev_lvl smoothed over 504d
def f029drb_f029_deferred_revenue_book_drev_lvl_smoothaccel_252d_sm504_3d_v079_signal(deferredrev, closeadj):
    base = deferredrev
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drev_to_rev smoothed over 252d
def f029drb_f029_deferred_revenue_book_drev_to_rev_smoothaccel_63d_sm252_3d_v080_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drev_to_rev smoothed over 504d
def f029drb_f029_deferred_revenue_book_drev_to_rev_smoothaccel_252d_sm504_3d_v081_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drev_to_liab smoothed over 252d
def f029drb_f029_deferred_revenue_book_drev_to_liab_smoothaccel_63d_sm252_3d_v082_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drev_to_liab smoothed over 504d
def f029drb_f029_deferred_revenue_book_drev_to_liab_smoothaccel_252d_sm504_3d_v083_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drev_growth smoothed over 252d
def f029drb_f029_deferred_revenue_book_drev_growth_smoothaccel_63d_sm252_3d_v084_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drev_growth smoothed over 504d
def f029drb_f029_deferred_revenue_book_drev_growth_smoothaccel_252d_sm504_3d_v085_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of billings_proxy smoothed over 252d
def f029drb_f029_deferred_revenue_book_billings_proxy_smoothaccel_63d_sm252_3d_v086_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of billings_proxy smoothed over 504d
def f029drb_f029_deferred_revenue_book_billings_proxy_smoothaccel_252d_sm504_3d_v087_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of billings_growth smoothed over 252d
def f029drb_f029_deferred_revenue_book_billings_growth_smoothaccel_63d_sm252_3d_v088_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of billings_growth smoothed over 504d
def f029drb_f029_deferred_revenue_book_billings_growth_smoothaccel_252d_sm504_3d_v089_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ndr_proxy smoothed over 252d
def f029drb_f029_deferred_revenue_book_ndr_proxy_smoothaccel_63d_sm252_3d_v090_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ndr_proxy smoothed over 504d
def f029drb_f029_deferred_revenue_book_ndr_proxy_smoothaccel_252d_sm504_3d_v091_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_accelz_21d_z252_3d_v092_signal(deferredrev, closeadj):
    base = deferredrev
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_accelz_63d_z504_3d_v093_signal(deferredrev, closeadj):
    base = deferredrev
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_accelz_21d_z252_3d_v094_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_accelz_63d_z504_3d_v095_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_accelz_21d_z252_3d_v096_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_accelz_63d_z504_3d_v097_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_accelz_21d_z252_3d_v098_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_accelz_63d_z504_3d_v099_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_accelz_21d_z252_3d_v100_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_accelz_63d_z504_3d_v101_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_accelz_21d_z252_3d_v102_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_accelz_63d_z504_3d_v103_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_accelz_21d_z252_3d_v104_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_accelz_63d_z504_3d_v105_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drev_lvl (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_lvl_signflip_63d_3d_v106_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drev_lvl (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_lvl_signflip_252d_3d_v107_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drev_to_rev (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_to_rev_signflip_63d_3d_v108_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drev_to_rev (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_to_rev_signflip_252d_3d_v109_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drev_to_liab (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_to_liab_signflip_63d_3d_v110_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drev_to_liab (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_to_liab_signflip_252d_3d_v111_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drev_growth (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_growth_signflip_63d_3d_v112_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drev_growth (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_drev_growth_signflip_252d_3d_v113_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in billings_proxy (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_billings_proxy_signflip_63d_3d_v114_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in billings_proxy (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_billings_proxy_signflip_252d_3d_v115_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in billings_growth (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_billings_growth_signflip_63d_3d_v116_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in billings_growth (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_billings_growth_signflip_252d_3d_v117_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ndr_proxy (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_ndr_proxy_signflip_63d_3d_v118_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ndr_proxy (raw count, no price scaling)
def f029drb_f029_deferred_revenue_book_ndr_proxy_signflip_252d_3d_v119_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_lvl normalized by 252d range
def f029drb_f029_deferred_revenue_book_drev_lvl_rngaccel_63d_r252_3d_v120_signal(deferredrev, closeadj):
    base = deferredrev
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_lvl normalized by 504d range
def f029drb_f029_deferred_revenue_book_drev_lvl_rngaccel_252d_r504_3d_v121_signal(deferredrev, closeadj):
    base = deferredrev
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_to_rev normalized by 252d range
def f029drb_f029_deferred_revenue_book_drev_to_rev_rngaccel_63d_r252_3d_v122_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_to_rev normalized by 504d range
def f029drb_f029_deferred_revenue_book_drev_to_rev_rngaccel_252d_r504_3d_v123_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_to_liab normalized by 252d range
def f029drb_f029_deferred_revenue_book_drev_to_liab_rngaccel_63d_r252_3d_v124_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_to_liab normalized by 504d range
def f029drb_f029_deferred_revenue_book_drev_to_liab_rngaccel_252d_r504_3d_v125_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drev_growth normalized by 252d range
def f029drb_f029_deferred_revenue_book_drev_growth_rngaccel_63d_r252_3d_v126_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drev_growth normalized by 504d range
def f029drb_f029_deferred_revenue_book_drev_growth_rngaccel_252d_r504_3d_v127_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of billings_proxy normalized by 252d range
def f029drb_f029_deferred_revenue_book_billings_proxy_rngaccel_63d_r252_3d_v128_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of billings_proxy normalized by 504d range
def f029drb_f029_deferred_revenue_book_billings_proxy_rngaccel_252d_r504_3d_v129_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of billings_growth normalized by 252d range
def f029drb_f029_deferred_revenue_book_billings_growth_rngaccel_63d_r252_3d_v130_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of billings_growth normalized by 504d range
def f029drb_f029_deferred_revenue_book_billings_growth_rngaccel_252d_r504_3d_v131_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ndr_proxy normalized by 252d range
def f029drb_f029_deferred_revenue_book_ndr_proxy_rngaccel_63d_r252_3d_v132_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ndr_proxy normalized by 504d range
def f029drb_f029_deferred_revenue_book_ndr_proxy_rngaccel_252d_r504_3d_v133_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_cumslope_21d_3d_v134_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_cumslope_63d_3d_v135_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_cumslope_252d_3d_v136_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_cumslope_21d_3d_v137_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_cumslope_63d_3d_v138_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_cumslope_252d_3d_v139_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_cumslope_21d_3d_v140_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_cumslope_63d_3d_v141_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_cumslope_252d_3d_v142_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_cumslope_21d_3d_v143_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_cumslope_63d_3d_v144_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_cumslope_252d_3d_v145_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_cumslope_21d_3d_v146_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_cumslope_63d_3d_v147_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_cumslope_252d_3d_v148_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_cumslope_21d_3d_v149_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_cumslope_63d_3d_v150_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

