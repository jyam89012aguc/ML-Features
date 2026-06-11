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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f27_revenue_accel(revenue, w):
    g1 = revenue.pct_change(periods=w)
    g2 = revenue.pct_change(periods=w).shift(w)
    return g1 - g2


def _f27_book_to_bill(revenue, deferredrev, w):
    backlog_chg = deferredrev.diff(periods=w)
    rev_chg = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (backlog_chg + rev_chg) / rev_chg.replace(0, np.nan)


def _f27_bill_growth_signature(revenue, w):
    g = revenue.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


# 3d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_slope_v001_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_slope_v002_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_slope_v003_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_slope_v004_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_slope_v005_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_slope_v006_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_slope_v007_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_slope_v008_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_slope_v009_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_slope_v010_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_slope_v011_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_slope_v012_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_slope_v013_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_slope_v014_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_slope_v015_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_slope_v016_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_slope_v017_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_slope_v018_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_slope_v019_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_slope_v020_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_slope_v021_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_slope_v022_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_slope_v023_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_slope_v024_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_slope_v025_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_slope_v026_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_slope_v027_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_slope_v028_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_slope_v029_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_slope_v030_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_3d_slope_v031_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_slope_v032_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_slope_v033_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_slope_v034_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_slope_v035_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_slope_v036_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_84d_slope_v037_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_slope_v038_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_168d_slope_v039_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_slope_v040_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_3d_slope_v041_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_slope_v042_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_slope_v043_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_slope_v044_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_slope_v045_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_slope_v046_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_84d_slope_v047_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_slope_v048_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_168d_slope_v049_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_slope_v050_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_3d_slope_v051_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_slope_v052_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_slope_v053_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_slope_v054_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_slope_v055_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_slope_v056_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_84d_slope_v057_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_slope_v058_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_168d_slope_v059_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_slope_v060_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_slope_v061_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_slope_v062_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_slope_v063_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_slope_v064_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_slope_v065_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_slope_v066_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_slope_v067_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_slope_v068_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_slope_v069_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_slope_v070_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_slope_v071_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_slope_v072_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_slope_v073_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_slope_v074_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_slope_v075_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_slope_v076_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_slope_v077_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_slope_v078_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_slope_v079_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_slope_v080_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_slope_v081_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_slope_v082_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_slope_v083_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_slope_v084_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_slope_v085_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_slope_v086_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_slope_v087_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_slope_v088_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_slope_v089_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_slope_v090_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_slope_v091_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_slope_v092_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_slope_v093_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_slope_v094_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_slope_v095_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_slope_v096_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_slope_v097_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_slope_v098_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_slope_v099_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_slope_v100_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_slope_v101_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_slope_v102_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_slope_v103_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_slope_v104_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_slope_v105_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_slope_v106_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_slope_v107_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_slope_v108_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_slope_v109_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_slope_v110_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_slope_v111_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_slope_v112_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_slope_v113_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_slope_v114_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_slope_v115_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_slope_v116_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_slope_v117_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_slope_v118_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_slope_v119_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_slope_v120_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_slope_v121_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_slope_v122_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_slope_v123_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_slope_v124_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_slope_v125_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_slope_v126_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_slope_v127_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_slope_v128_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_slope_v129_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_slope_v130_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_slope_v131_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_slope_v132_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_slope_v133_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_slope_v134_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_slope_v135_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_slope_v136_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_slope_v137_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_slope_v138_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_slope_v139_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_slope_v140_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_slope_v141_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_slope_v142_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_slope_v143_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_slope_v144_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_slope_v145_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_slope_v146_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_slope_v147_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_slope_v148_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_slope_v149_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_slope_v150_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_slope_v001_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_slope_v002_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_slope_v003_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_slope_v004_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_slope_v005_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_slope_v006_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_slope_v007_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_slope_v008_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_slope_v009_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_slope_v010_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_slope_v011_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_slope_v012_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_slope_v013_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_slope_v014_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_slope_v015_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_slope_v016_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_slope_v017_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_slope_v018_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_slope_v019_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_slope_v020_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_slope_v021_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_slope_v022_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_slope_v023_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_slope_v024_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_slope_v025_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_slope_v026_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_slope_v027_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_slope_v028_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_slope_v029_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_slope_v030_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_3d_slope_v031_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_slope_v032_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_slope_v033_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_slope_v034_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_slope_v035_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_slope_v036_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_84d_slope_v037_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_slope_v038_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_168d_slope_v039_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_slope_v040_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_3d_slope_v041_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_slope_v042_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_slope_v043_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_slope_v044_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_slope_v045_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_slope_v046_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_84d_slope_v047_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_slope_v048_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_168d_slope_v049_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_slope_v050_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_3d_slope_v051_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_slope_v052_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_slope_v053_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_slope_v054_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_slope_v055_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_slope_v056_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_84d_slope_v057_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_slope_v058_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_168d_slope_v059_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_slope_v060_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_slope_v061_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_slope_v062_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_slope_v063_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_slope_v064_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_slope_v065_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_slope_v066_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_slope_v067_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_slope_v068_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_slope_v069_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_slope_v070_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_slope_v071_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_slope_v072_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_slope_v073_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_slope_v074_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_slope_v075_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_slope_v076_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_slope_v077_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_slope_v078_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_slope_v079_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_slope_v080_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_slope_v081_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_slope_v082_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_slope_v083_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_slope_v084_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_slope_v085_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_slope_v086_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_slope_v087_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_slope_v088_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_slope_v089_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_slope_v090_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_slope_v091_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_slope_v092_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_slope_v093_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_slope_v094_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_slope_v095_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_slope_v096_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_slope_v097_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_slope_v098_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_slope_v099_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_slope_v100_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_slope_v101_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_slope_v102_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_slope_v103_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_slope_v104_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_slope_v105_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_slope_v106_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_slope_v107_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_slope_v108_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_slope_v109_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_slope_v110_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_slope_v111_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_slope_v112_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_slope_v113_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_slope_v114_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_slope_v115_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_slope_v116_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_slope_v117_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_slope_v118_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_slope_v119_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_slope_v120_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_slope_v121_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_slope_v122_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_slope_v123_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_slope_v124_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_slope_v125_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_slope_v126_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_slope_v127_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_slope_v128_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_slope_v129_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_slope_v130_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_slope_v131_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_slope_v132_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_slope_v133_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_slope_v134_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_slope_v135_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_slope_v136_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_slope_v137_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_slope_v138_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_slope_v139_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_slope_v140_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_slope_v141_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_slope_v142_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_slope_v143_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_slope_v144_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_slope_v145_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_slope_v146_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_slope_v147_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_slope_v148_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_slope_v149_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CRO_BOOK_TO_BILL_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_revenue_accel", "_f27_book_to_bill", "_f27_bill_growth_signature",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f27_cro_book_to_bill_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
