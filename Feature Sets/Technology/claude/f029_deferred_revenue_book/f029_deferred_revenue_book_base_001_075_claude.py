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
def _f029_drev_to_rev(deferredrev, revenue):
    return deferredrev / revenue.abs().replace(0, np.nan)


# 21d mean of drev_lvl scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_lvl_mean_21d_base_v001_signal(deferredrev, closeadj):
    base = deferredrev
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drev_lvl scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_lvl_mean_63d_base_v002_signal(deferredrev, closeadj):
    base = deferredrev
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drev_lvl scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_lvl_mean_126d_base_v003_signal(deferredrev, closeadj):
    base = deferredrev
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drev_lvl scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_lvl_mean_252d_base_v004_signal(deferredrev, closeadj):
    base = deferredrev
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drev_lvl scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_lvl_mean_504d_base_v005_signal(deferredrev, closeadj):
    base = deferredrev
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drev_to_rev scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_rev_mean_21d_base_v006_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drev_to_rev scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_rev_mean_63d_base_v007_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drev_to_rev scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_rev_mean_126d_base_v008_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drev_to_rev scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_rev_mean_252d_base_v009_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drev_to_rev scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_rev_mean_504d_base_v010_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drev_to_liab scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_liab_mean_21d_base_v011_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drev_to_liab scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_liab_mean_63d_base_v012_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drev_to_liab scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_liab_mean_126d_base_v013_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drev_to_liab scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_liab_mean_252d_base_v014_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drev_to_liab scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_to_liab_mean_504d_base_v015_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drev_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_growth_mean_21d_base_v016_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drev_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_growth_mean_63d_base_v017_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drev_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_growth_mean_126d_base_v018_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drev_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_growth_mean_252d_base_v019_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drev_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_drev_growth_mean_504d_base_v020_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of billings_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_proxy_mean_21d_base_v021_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of billings_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_proxy_mean_63d_base_v022_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of billings_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_proxy_mean_126d_base_v023_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of billings_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_proxy_mean_252d_base_v024_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of billings_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_proxy_mean_504d_base_v025_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of billings_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_growth_mean_21d_base_v026_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of billings_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_growth_mean_63d_base_v027_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of billings_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_growth_mean_126d_base_v028_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of billings_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_growth_mean_252d_base_v029_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of billings_growth scaled by closeadj
def f029drb_f029_deferred_revenue_book_billings_growth_mean_504d_base_v030_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ndr_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_ndr_proxy_mean_21d_base_v031_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ndr_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_ndr_proxy_mean_63d_base_v032_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ndr_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_ndr_proxy_mean_126d_base_v033_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ndr_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_ndr_proxy_mean_252d_base_v034_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ndr_proxy scaled by closeadj
def f029drb_f029_deferred_revenue_book_ndr_proxy_mean_504d_base_v035_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_median_63d_base_v036_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_median_252d_base_v037_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_median_504d_base_v038_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_median_63d_base_v039_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_median_252d_base_v040_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_median_504d_base_v041_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_median_63d_base_v042_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_median_252d_base_v043_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_median_504d_base_v044_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_median_63d_base_v045_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_median_252d_base_v046_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_median_504d_base_v047_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_median_63d_base_v048_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_median_252d_base_v049_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_median_504d_base_v050_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_median_63d_base_v051_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_median_252d_base_v052_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_median_504d_base_v053_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_median_63d_base_v054_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_median_252d_base_v055_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_median_504d_base_v056_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_rmax_252d_base_v057_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_rmax_504d_base_v058_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_rmax_252d_base_v059_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_rmax_504d_base_v060_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_rmax_252d_base_v061_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_rmax_504d_base_v062_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_rmax_252d_base_v063_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_rmax_504d_base_v064_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_rmax_252d_base_v065_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_rmax_504d_base_v066_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_rmax_252d_base_v067_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_rmax_504d_base_v068_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_rmax_252d_base_v069_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_rmax_504d_base_v070_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_rmin_252d_base_v071_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_rmin_504d_base_v072_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_rmin_252d_base_v073_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_rmin_504d_base_v074_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_rmin_252d_base_v075_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

