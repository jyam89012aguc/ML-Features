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


# 3d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_jerk_v001_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_jerk_v002_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_jerk_v003_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_jerk_v004_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_jerk_v005_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_jerk_v006_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_jerk_v007_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_jerk_v008_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_jerk_v009_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of revaccel base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_jerk_v010_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    base = a * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_jerk_v011_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_jerk_v012_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_jerk_v013_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_jerk_v014_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_jerk_v015_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_jerk_v016_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_jerk_v017_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_jerk_v018_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_jerk_v019_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of revaccel base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_jerk_v020_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    base = a * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_jerk_v021_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_jerk_v022_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_jerk_v023_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_jerk_v024_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_jerk_v025_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_jerk_v026_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_jerk_v027_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_jerk_v028_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_jerk_v029_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of revaccel base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_jerk_v030_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    base = a * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_3d_jerk_v031_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_jerk_v032_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_jerk_v033_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_jerk_v034_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_jerk_v035_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_jerk_v036_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_84d_jerk_v037_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_jerk_v038_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_168d_jerk_v039_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of btb base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_jerk_v040_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    base = btb * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_3d_jerk_v041_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_jerk_v042_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_jerk_v043_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_jerk_v044_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_jerk_v045_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_jerk_v046_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_84d_jerk_v047_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_jerk_v048_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_168d_jerk_v049_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of btb base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_jerk_v050_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    base = btb * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_3d_jerk_v051_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_jerk_v052_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_jerk_v053_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_jerk_v054_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_jerk_v055_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_jerk_v056_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_84d_jerk_v057_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_jerk_v058_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_168d_jerk_v059_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of btb base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_jerk_v060_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    base = btb * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_jerk_v061_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_jerk_v062_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_jerk_v063_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_jerk_v064_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_jerk_v065_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_jerk_v066_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_jerk_v067_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_jerk_v068_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_jerk_v069_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of billgrowth base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_jerk_v070_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    base = bg * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_jerk_v071_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_jerk_v072_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_jerk_v073_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_jerk_v074_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_jerk_v075_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_jerk_v076_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_jerk_v077_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_jerk_v078_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_jerk_v079_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of billgrowth base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_jerk_v080_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    base = bg * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_jerk_v081_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_jerk_v082_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_jerk_v083_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_jerk_v084_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_jerk_v085_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_jerk_v086_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_jerk_v087_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_jerk_v088_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_jerk_v089_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of billgrowth base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_jerk_v090_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    base = bg * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_jerk_v091_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_jerk_v092_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_jerk_v093_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_jerk_v094_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_jerk_v095_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_jerk_v096_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_jerk_v097_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_jerk_v098_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_jerk_v099_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of revaccelxrev base_w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_jerk_v100_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = a * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_jerk_v101_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_jerk_v102_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_jerk_v103_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_jerk_v104_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_jerk_v105_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_jerk_v106_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_jerk_v107_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_jerk_v108_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_jerk_v109_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of revaccelxrev base_w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_jerk_v110_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = a * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_jerk_v111_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_jerk_v112_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_jerk_v113_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_jerk_v114_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_jerk_v115_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_jerk_v116_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_jerk_v117_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_jerk_v118_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_jerk_v119_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of revaccelxrev base_w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_jerk_v120_signal(revenue):
    a = _f27_revenue_accel(revenue, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = a * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_jerk_v121_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_jerk_v122_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_jerk_v123_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_jerk_v124_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_jerk_v125_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_jerk_v126_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_jerk_v127_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_jerk_v128_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_jerk_v129_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of btbxrev base_w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_jerk_v130_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_jerk_v131_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_jerk_v132_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_jerk_v133_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_jerk_v134_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_jerk_v135_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_jerk_v136_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_jerk_v137_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_jerk_v138_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_jerk_v139_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of btbxrev base_w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_jerk_v140_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_jerk_v141_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_jerk_v142_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_jerk_v143_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_jerk_v144_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_jerk_v145_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_jerk_v146_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_jerk_v147_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_jerk_v148_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_jerk_v149_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of btbxrev base_w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_jerk_v150_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = btb * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_jerk_v001_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_jerk_v002_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_jerk_v003_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_jerk_v004_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_jerk_v005_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_jerk_v006_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_jerk_v007_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_jerk_v008_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_jerk_v009_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_jerk_v010_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_jerk_v011_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_jerk_v012_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_jerk_v013_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_jerk_v014_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_jerk_v015_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_jerk_v016_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_jerk_v017_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_jerk_v018_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_jerk_v019_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_jerk_v020_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_3d_jerk_v021_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_jerk_v022_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_jerk_v023_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_jerk_v024_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_jerk_v025_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_jerk_v026_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_84d_jerk_v027_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_jerk_v028_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_168d_jerk_v029_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_jerk_v030_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_3d_jerk_v031_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_jerk_v032_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_jerk_v033_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_jerk_v034_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_jerk_v035_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_jerk_v036_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_84d_jerk_v037_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_jerk_v038_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_168d_jerk_v039_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_jerk_v040_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_3d_jerk_v041_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_jerk_v042_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_jerk_v043_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_jerk_v044_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_jerk_v045_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_jerk_v046_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_84d_jerk_v047_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_jerk_v048_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_168d_jerk_v049_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_jerk_v050_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_3d_jerk_v051_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_jerk_v052_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_jerk_v053_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_jerk_v054_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_jerk_v055_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_jerk_v056_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_84d_jerk_v057_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_jerk_v058_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_168d_jerk_v059_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_jerk_v060_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_jerk_v061_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_jerk_v062_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_jerk_v063_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_jerk_v064_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_jerk_v065_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_jerk_v066_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_jerk_v067_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_jerk_v068_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_jerk_v069_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_jerk_v070_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_jerk_v071_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_jerk_v072_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_jerk_v073_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_jerk_v074_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_jerk_v075_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_jerk_v076_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_jerk_v077_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_jerk_v078_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_jerk_v079_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_jerk_v080_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_3d_jerk_v081_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_jerk_v082_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_jerk_v083_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_jerk_v084_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_jerk_v085_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_jerk_v086_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_84d_jerk_v087_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_jerk_v088_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_168d_jerk_v089_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_jerk_v090_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_jerk_v091_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_jerk_v092_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_jerk_v093_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_jerk_v094_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_jerk_v095_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_jerk_v096_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_jerk_v097_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_jerk_v098_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_jerk_v099_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_jerk_v100_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_jerk_v101_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_jerk_v102_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_jerk_v103_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_jerk_v104_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_jerk_v105_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_jerk_v106_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_jerk_v107_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_jerk_v108_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_jerk_v109_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_jerk_v110_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_3d_jerk_v111_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_jerk_v112_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_jerk_v113_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_jerk_v114_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_jerk_v115_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_jerk_v116_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_84d_jerk_v117_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_126d_jerk_v118_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_168d_jerk_v119_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_189d_jerk_v120_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_jerk_v121_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_jerk_v122_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_jerk_v123_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_jerk_v124_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_jerk_v125_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_jerk_v126_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_jerk_v127_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_jerk_v128_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_jerk_v129_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_jerk_v130_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_jerk_v131_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_jerk_v132_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_jerk_v133_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_jerk_v134_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_jerk_v135_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_jerk_v136_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_jerk_v137_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_jerk_v138_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_jerk_v139_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_jerk_v140_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_3d_jerk_v141_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_jerk_v142_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_jerk_v143_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_jerk_v144_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_jerk_v145_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_jerk_v146_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_84d_jerk_v147_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_126d_jerk_v148_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_168d_jerk_v149_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_189d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CRO_BOOK_TO_BILL_PROXY_REGISTRY_JERK_001_150 = REGISTRY


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
    print(f"OK f27_cro_book_to_bill_proxy_3rd_derivatives_001_150_claude: {n_features} features pass")
