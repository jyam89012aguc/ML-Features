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


# 63d z-score of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_z_63d_base_v076_signal(deferredrev, closeadj):
    base = deferredrev
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_z_126d_base_v077_signal(deferredrev, closeadj):
    base = deferredrev
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_z_252d_base_v078_signal(deferredrev, closeadj):
    base = deferredrev
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_z_504d_base_v079_signal(deferredrev, closeadj):
    base = deferredrev
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_z_63d_base_v080_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_z_126d_base_v081_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_z_252d_base_v082_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_z_504d_base_v083_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_z_63d_base_v084_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_z_126d_base_v085_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_z_252d_base_v086_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_z_504d_base_v087_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_z_63d_base_v088_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_z_126d_base_v089_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_z_252d_base_v090_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_z_504d_base_v091_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_z_63d_base_v092_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_z_126d_base_v093_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_z_252d_base_v094_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_z_504d_base_v095_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_z_63d_base_v096_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_z_126d_base_v097_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_z_252d_base_v098_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_z_504d_base_v099_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_z_63d_base_v100_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_z_126d_base_v101_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_z_252d_base_v102_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_z_504d_base_v103_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_distmax_252d_base_v104_signal(deferredrev, closeadj):
    base = deferredrev
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_distmax_504d_base_v105_signal(deferredrev, closeadj):
    base = deferredrev
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_distmax_252d_base_v106_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_distmax_504d_base_v107_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_distmax_252d_base_v108_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_distmax_504d_base_v109_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_distmax_252d_base_v110_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_distmax_504d_base_v111_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_distmax_252d_base_v112_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_distmax_504d_base_v113_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_distmax_252d_base_v114_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_distmax_504d_base_v115_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_distmax_252d_base_v116_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_distmax_504d_base_v117_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_distmed_126d_base_v118_signal(deferredrev, closeadj):
    base = deferredrev
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_distmed_252d_base_v119_signal(deferredrev, closeadj):
    base = deferredrev
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_distmed_504d_base_v120_signal(deferredrev, closeadj):
    base = deferredrev
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_distmed_126d_base_v121_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_distmed_252d_base_v122_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_distmed_504d_base_v123_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_distmed_126d_base_v124_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_distmed_252d_base_v125_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_distmed_504d_base_v126_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_distmed_126d_base_v127_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_distmed_252d_base_v128_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_distmed_504d_base_v129_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_distmed_126d_base_v130_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_distmed_252d_base_v131_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_distmed_504d_base_v132_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_distmed_126d_base_v133_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_distmed_252d_base_v134_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_distmed_504d_base_v135_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_distmed_126d_base_v136_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_distmed_252d_base_v137_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ndr_proxy
def f029drb_f029_deferred_revenue_book_ndr_proxy_distmed_504d_base_v138_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=252).fillna(0)) / revenue.shift(252).abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_chg_63d_base_v139_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drev_lvl
def f029drb_f029_deferred_revenue_book_drev_lvl_chg_252d_base_v140_signal(deferredrev, closeadj):
    base = deferredrev
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_chg_63d_base_v141_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drev_to_rev
def f029drb_f029_deferred_revenue_book_drev_to_rev_chg_252d_base_v142_signal(deferredrev, revenue, closeadj):
    base = _f029_drev_to_rev(deferredrev, revenue)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_chg_63d_base_v143_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drev_to_liab
def f029drb_f029_deferred_revenue_book_drev_to_liab_chg_252d_base_v144_signal(deferredrev, liabilities, closeadj):
    base = deferredrev / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_chg_63d_base_v145_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drev_growth
def f029drb_f029_deferred_revenue_book_drev_growth_chg_252d_base_v146_signal(deferredrev, closeadj):
    base = deferredrev.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_chg_63d_base_v147_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in billings_proxy
def f029drb_f029_deferred_revenue_book_billings_proxy_chg_252d_base_v148_signal(revenue, deferredrev, closeadj):
    base = revenue + deferredrev.diff(periods=63).fillna(0)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_chg_63d_base_v149_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in billings_growth
def f029drb_f029_deferred_revenue_book_billings_growth_chg_252d_base_v150_signal(revenue, deferredrev, closeadj):
    base = (revenue + deferredrev.diff(periods=63).fillna(0)).pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

