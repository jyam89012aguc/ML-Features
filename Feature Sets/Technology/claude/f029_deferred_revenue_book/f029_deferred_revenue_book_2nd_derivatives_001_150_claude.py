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


# 21d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slope_21d_2d_v001_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slope_63d_2d_v002_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slope_126d_2d_v003_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slope_252d_2d_v004_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_slope_504d_2d_v005_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slope_21d_2d_v006_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slope_63d_2d_v007_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slope_126d_2d_v008_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slope_252d_2d_v009_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_slope_504d_2d_v010_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slope_21d_2d_v011_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slope_63d_2d_v012_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slope_126d_2d_v013_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slope_252d_2d_v014_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_slope_504d_2d_v015_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slope_21d_2d_v016_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slope_63d_2d_v017_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slope_126d_2d_v018_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slope_252d_2d_v019_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_slope_504d_2d_v020_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slope_21d_2d_v021_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slope_63d_2d_v022_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slope_126d_2d_v023_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slope_252d_2d_v024_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_slope_504d_2d_v025_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slope_21d_2d_v026_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slope_63d_2d_v027_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slope_126d_2d_v028_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slope_252d_2d_v029_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_slope_504d_2d_v030_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slope_21d_2d_v031_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slope_63d_2d_v032_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slope_126d_2d_v033_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slope_252d_2d_v034_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_slope_504d_2d_v035_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sm21_sl21_2d_v036_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sm63_sl21_2d_v037_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sm63_sl63_2d_v038_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sm252_sl63_2d_v039_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sm252_sl126_2d_v040_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sm21_sl21_2d_v041_signal(deferredrev, revenue, closeadj):
    base = _mean(_f029_drev_to_rev(deferredrev, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sm63_sl21_2d_v042_signal(deferredrev, revenue, closeadj):
    base = _mean(_f029_drev_to_rev(deferredrev, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sm63_sl63_2d_v043_signal(deferredrev, revenue, closeadj):
    base = _mean(_f029_drev_to_rev(deferredrev, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sm252_sl63_2d_v044_signal(deferredrev, revenue, closeadj):
    base = _mean(_f029_drev_to_rev(deferredrev, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sm252_sl126_2d_v045_signal(deferredrev, revenue, closeadj):
    base = _mean(_f029_drev_to_rev(deferredrev, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sm21_sl21_2d_v046_signal(deferredrev, liabilities, closeadj):
    base = _mean(deferredrev / liabilities.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sm63_sl21_2d_v047_signal(deferredrev, liabilities, closeadj):
    base = _mean(deferredrev / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sm63_sl63_2d_v048_signal(deferredrev, liabilities, closeadj):
    base = _mean(deferredrev / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sm252_sl63_2d_v049_signal(deferredrev, liabilities, closeadj):
    base = _mean(deferredrev / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sm252_sl126_2d_v050_signal(deferredrev, liabilities, closeadj):
    base = _mean(deferredrev / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sm21_sl21_2d_v051_signal(deferredrev, closeadj):
    base = _mean(deferredrev.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sm63_sl21_2d_v052_signal(deferredrev, closeadj):
    base = _mean(deferredrev.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sm63_sl63_2d_v053_signal(deferredrev, closeadj):
    base = _mean(deferredrev.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sm252_sl63_2d_v054_signal(deferredrev, closeadj):
    base = _mean(deferredrev.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sm252_sl126_2d_v055_signal(deferredrev, closeadj):
    base = _mean(deferredrev.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sm21_sl21_2d_v056_signal(revenue, deferredrev, closeadj):
    base = _mean(revenue + deferredrev.diff(periods=63).fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sm63_sl21_2d_v057_signal(revenue, deferredrev, closeadj):
    base = _mean(revenue + deferredrev.diff(periods=63).fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sm63_sl63_2d_v058_signal(revenue, deferredrev, closeadj):
    base = _mean(revenue + deferredrev.diff(periods=63).fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sm252_sl63_2d_v059_signal(revenue, deferredrev, closeadj):
    base = _mean(revenue + deferredrev.diff(periods=63).fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sm252_sl126_2d_v060_signal(revenue, deferredrev, closeadj):
    base = _mean(revenue + deferredrev.diff(periods=63).fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sm21_sl21_2d_v061_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sm63_sl21_2d_v062_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sm63_sl63_2d_v063_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sm252_sl63_2d_v064_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sm252_sl126_2d_v065_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sm21_sl21_2d_v066_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sm63_sl21_2d_v067_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sm63_sl63_2d_v068_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sm252_sl63_2d_v069_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sm252_sl126_2d_v070_signal(revenue, deferredrev, closeadj):
    base = _mean((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_pctslope_21d_2d_v071_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_pctslope_63d_2d_v072_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_pctslope_252d_2d_v073_signal(deferredrev, closeadj):
    base = deferredrev
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_pctslope_21d_2d_v074_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_pctslope_63d_2d_v075_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_pctslope_252d_2d_v076_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_pctslope_21d_2d_v077_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_pctslope_63d_2d_v078_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_pctslope_252d_2d_v079_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_pctslope_21d_2d_v080_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_pctslope_63d_2d_v081_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_pctslope_252d_2d_v082_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_pctslope_21d_2d_v083_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_pctslope_63d_2d_v084_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_pctslope_252d_2d_v085_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_pctslope_21d_2d_v086_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_pctslope_63d_2d_v087_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_pctslope_252d_2d_v088_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_pctslope_21d_2d_v089_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_pctslope_63d_2d_v090_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_pctslope_252d_2d_v091_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sgnslope_21d_2d_v092_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sgnslope_63d_2d_v093_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_sgnslope_252d_2d_v094_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sgnslope_21d_2d_v095_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sgnslope_63d_2d_v096_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_sgnslope_252d_2d_v097_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sgnslope_21d_2d_v098_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sgnslope_63d_2d_v099_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_sgnslope_252d_2d_v100_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sgnslope_21d_2d_v101_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sgnslope_63d_2d_v102_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_sgnslope_252d_2d_v103_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sgnslope_21d_2d_v104_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sgnslope_63d_2d_v105_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_sgnslope_252d_2d_v106_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sgnslope_21d_2d_v107_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sgnslope_63d_2d_v108_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_sgnslope_252d_2d_v109_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sgnslope_21d_2d_v110_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sgnslope_63d_2d_v111_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_sgnslope_252d_2d_v112_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_logmagslope_21d_2d_v113_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_logmagslope_63d_2d_v114_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_logmagslope_252d_2d_v115_signal(deferredrev, closeadj):
    base = deferredrev
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_logmagslope_21d_2d_v116_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_logmagslope_63d_2d_v117_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_logmagslope_252d_2d_v118_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_logmagslope_21d_2d_v119_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_logmagslope_63d_2d_v120_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_logmagslope_252d_2d_v121_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_logmagslope_21d_2d_v122_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_logmagslope_63d_2d_v123_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_logmagslope_252d_2d_v124_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_logmagslope_21d_2d_v125_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_logmagslope_63d_2d_v126_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_logmagslope_252d_2d_v127_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_logmagslope_21d_2d_v128_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_logmagslope_63d_2d_v129_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_logmagslope_252d_2d_v130_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_logmagslope_21d_2d_v131_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_logmagslope_63d_2d_v132_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_logmagslope_252d_2d_v133_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drev_lvl|
def f029drb_f029_deferred_revenue_book_drev_lvl_logslope_63d_2d_v134_signal(deferredrev, closeadj):
    base = np.log((deferredrev).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drev_lvl|
def f029drb_f029_deferred_revenue_book_drev_lvl_logslope_252d_2d_v135_signal(deferredrev, closeadj):
    base = np.log((deferredrev).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drev_to_rev|
def f029drb_f029_deferred_revenue_book_drev_to_rev_logslope_63d_2d_v136_signal(deferredrev, revenue, closeadj):
    base = np.log((_f029_drev_to_rev(deferredrev, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drev_to_rev|
def f029drb_f029_deferred_revenue_book_drev_to_rev_logslope_252d_2d_v137_signal(deferredrev, revenue, closeadj):
    base = np.log((_f029_drev_to_rev(deferredrev, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drev_to_liab|
def f029drb_f029_deferred_revenue_book_drev_to_liab_logslope_63d_2d_v138_signal(deferredrev, liabilities, closeadj):
    base = np.log((deferredrev / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drev_to_liab|
def f029drb_f029_deferred_revenue_book_drev_to_liab_logslope_252d_2d_v139_signal(deferredrev, liabilities, closeadj):
    base = np.log((deferredrev / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drev_growth|
def f029drb_f029_deferred_revenue_book_drev_growth_logslope_63d_2d_v140_signal(deferredrev, closeadj):
    base = np.log((deferredrev.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drev_growth|
def f029drb_f029_deferred_revenue_book_drev_growth_logslope_252d_2d_v141_signal(deferredrev, closeadj):
    base = np.log((deferredrev.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|billings_proxy|
def f029drb_f029_deferred_revenue_book_billings_proxy_logslope_63d_2d_v142_signal(revenue, deferredrev, closeadj):
    base = np.log((revenue + deferredrev.diff(periods=63).fillna(0)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|billings_proxy|
def f029drb_f029_deferred_revenue_book_billings_proxy_logslope_252d_2d_v143_signal(revenue, deferredrev, closeadj):
    base = np.log((revenue + deferredrev.diff(periods=63).fillna(0)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|billings_growth|
def f029drb_f029_deferred_revenue_book_billings_growth_logslope_63d_2d_v144_signal(revenue, deferredrev, closeadj):
    base = np.log(((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|billings_growth|
def f029drb_f029_deferred_revenue_book_billings_growth_logslope_252d_2d_v145_signal(revenue, deferredrev, closeadj):
    base = np.log(((revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ndr_proxy|
def f029drb_f029_deferred_revenue_book_ndr_proxy_logslope_63d_2d_v146_signal(revenue, deferredrev, closeadj):
    base = np.log(((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ndr_proxy|
def f029drb_f029_deferred_revenue_book_ndr_proxy_logslope_252d_2d_v147_signal(revenue, deferredrev, closeadj):
    base = np.log(((revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

