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
def _f29_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f29_revenue_diversification(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return m / (sd.replace(0, np.nan) + 1e-6)


def _f29_concentration_proxy(revenue, w):
    g = revenue.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).std()


# 3d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_3d_slope_v001_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_5d_slope_v002_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_10d_slope_v003_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_21d_slope_v004_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_42d_slope_v005_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_63d_slope_v006_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_84d_slope_v007_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_126d_slope_v008_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_168d_slope_v009_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revcv base_w=21
def f29ccc_f29_cro_client_concentration_revcv_189d_slope_v010_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    base = cv * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_3d_slope_v011_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_5d_slope_v012_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_10d_slope_v013_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_21d_slope_v014_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_42d_slope_v015_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_63d_slope_v016_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_84d_slope_v017_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_126d_slope_v018_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_168d_slope_v019_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revcv base_w=63
def f29ccc_f29_cro_client_concentration_revcv_189d_slope_v020_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    base = cv * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_3d_slope_v021_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_5d_slope_v022_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_10d_slope_v023_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_21d_slope_v024_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_42d_slope_v025_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_63d_slope_v026_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_84d_slope_v027_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_126d_slope_v028_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_168d_slope_v029_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revcv base_w=252
def f29ccc_f29_cro_client_concentration_revcv_189d_slope_v030_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    base = cv * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_3d_slope_v031_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_5d_slope_v032_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_10d_slope_v033_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_21d_slope_v034_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_42d_slope_v035_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_63d_slope_v036_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_84d_slope_v037_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_126d_slope_v038_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_168d_slope_v039_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revdiv base_w=21
def f29ccc_f29_cro_client_concentration_revdiv_189d_slope_v040_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    base = d * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_3d_slope_v041_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_5d_slope_v042_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_10d_slope_v043_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_21d_slope_v044_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_42d_slope_v045_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_63d_slope_v046_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_84d_slope_v047_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_126d_slope_v048_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_168d_slope_v049_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revdiv base_w=63
def f29ccc_f29_cro_client_concentration_revdiv_189d_slope_v050_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    base = d * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_3d_slope_v051_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_5d_slope_v052_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_10d_slope_v053_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_21d_slope_v054_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_42d_slope_v055_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_63d_slope_v056_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_84d_slope_v057_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_126d_slope_v058_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_168d_slope_v059_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revdiv base_w=252
def f29ccc_f29_cro_client_concentration_revdiv_189d_slope_v060_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    base = d * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_3d_slope_v061_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_5d_slope_v062_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_10d_slope_v063_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_21d_slope_v064_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_42d_slope_v065_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_63d_slope_v066_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_84d_slope_v067_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_126d_slope_v068_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_168d_slope_v069_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of conprx base_w=21
def f29ccc_f29_cro_client_concentration_conprx_189d_slope_v070_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    base = cp * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_3d_slope_v071_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_5d_slope_v072_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_10d_slope_v073_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_21d_slope_v074_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_42d_slope_v075_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_63d_slope_v076_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_84d_slope_v077_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_126d_slope_v078_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_168d_slope_v079_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of conprx base_w=63
def f29ccc_f29_cro_client_concentration_conprx_189d_slope_v080_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    base = cp * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_3d_slope_v081_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_5d_slope_v082_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_10d_slope_v083_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_21d_slope_v084_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_42d_slope_v085_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_63d_slope_v086_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_84d_slope_v087_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_126d_slope_v088_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_168d_slope_v089_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of conprx base_w=252
def f29ccc_f29_cro_client_concentration_conprx_189d_slope_v090_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    base = cp * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_3d_slope_v091_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_5d_slope_v092_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_10d_slope_v093_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_21d_slope_v094_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_42d_slope_v095_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_63d_slope_v096_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_84d_slope_v097_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_126d_slope_v098_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_168d_slope_v099_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revcvxdr base_w=21
def f29ccc_f29_cro_client_concentration_revcvxdr_189d_slope_v100_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=11).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_3d_slope_v101_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_5d_slope_v102_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_10d_slope_v103_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_21d_slope_v104_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_42d_slope_v105_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_63d_slope_v106_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_84d_slope_v107_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_126d_slope_v108_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_168d_slope_v109_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revcvxdr base_w=63
def f29ccc_f29_cro_client_concentration_revcvxdr_189d_slope_v110_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=32).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_3d_slope_v111_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_5d_slope_v112_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_10d_slope_v113_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_21d_slope_v114_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_42d_slope_v115_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_63d_slope_v116_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_84d_slope_v117_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_126d_slope_v118_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_168d_slope_v119_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revcvxdr base_w=252
def f29ccc_f29_cro_client_concentration_revcvxdr_189d_slope_v120_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 252)
    dr = deferredrev.rolling(252, min_periods=126).mean()
    base = cv * dr / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_3d_slope_v121_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_5d_slope_v122_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_10d_slope_v123_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_21d_slope_v124_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_42d_slope_v125_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_63d_slope_v126_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_84d_slope_v127_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_126d_slope_v128_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_168d_slope_v129_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revdivxdr base_w=42
def f29ccc_f29_cro_client_concentration_revdivxdr_189d_slope_v130_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=21).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_3d_slope_v131_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_5d_slope_v132_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_10d_slope_v133_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_21d_slope_v134_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_42d_slope_v135_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_63d_slope_v136_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_84d_slope_v137_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_126d_slope_v138_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_168d_slope_v139_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revdivxdr base_w=126
def f29ccc_f29_cro_client_concentration_revdivxdr_189d_slope_v140_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 126)
    dr = deferredrev.rolling(126, min_periods=63).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_3d_slope_v141_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_5d_slope_v142_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_10d_slope_v143_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_21d_slope_v144_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_42d_slope_v145_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_63d_slope_v146_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_84d_slope_v147_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_126d_slope_v148_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_168d_slope_v149_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of revdivxdr base_w=504
def f29ccc_f29_cro_client_concentration_revdivxdr_189d_slope_v150_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 504)
    dr = deferredrev.rolling(504, min_periods=252).mean()
    base = d * dr / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f29ccc_f29_cro_client_concentration_revcv_3d_slope_v001_signal,
    f29ccc_f29_cro_client_concentration_revcv_5d_slope_v002_signal,
    f29ccc_f29_cro_client_concentration_revcv_10d_slope_v003_signal,
    f29ccc_f29_cro_client_concentration_revcv_21d_slope_v004_signal,
    f29ccc_f29_cro_client_concentration_revcv_42d_slope_v005_signal,
    f29ccc_f29_cro_client_concentration_revcv_63d_slope_v006_signal,
    f29ccc_f29_cro_client_concentration_revcv_84d_slope_v007_signal,
    f29ccc_f29_cro_client_concentration_revcv_126d_slope_v008_signal,
    f29ccc_f29_cro_client_concentration_revcv_168d_slope_v009_signal,
    f29ccc_f29_cro_client_concentration_revcv_189d_slope_v010_signal,
    f29ccc_f29_cro_client_concentration_revcv_3d_slope_v011_signal,
    f29ccc_f29_cro_client_concentration_revcv_5d_slope_v012_signal,
    f29ccc_f29_cro_client_concentration_revcv_10d_slope_v013_signal,
    f29ccc_f29_cro_client_concentration_revcv_21d_slope_v014_signal,
    f29ccc_f29_cro_client_concentration_revcv_42d_slope_v015_signal,
    f29ccc_f29_cro_client_concentration_revcv_63d_slope_v016_signal,
    f29ccc_f29_cro_client_concentration_revcv_84d_slope_v017_signal,
    f29ccc_f29_cro_client_concentration_revcv_126d_slope_v018_signal,
    f29ccc_f29_cro_client_concentration_revcv_168d_slope_v019_signal,
    f29ccc_f29_cro_client_concentration_revcv_189d_slope_v020_signal,
    f29ccc_f29_cro_client_concentration_revcv_3d_slope_v021_signal,
    f29ccc_f29_cro_client_concentration_revcv_5d_slope_v022_signal,
    f29ccc_f29_cro_client_concentration_revcv_10d_slope_v023_signal,
    f29ccc_f29_cro_client_concentration_revcv_21d_slope_v024_signal,
    f29ccc_f29_cro_client_concentration_revcv_42d_slope_v025_signal,
    f29ccc_f29_cro_client_concentration_revcv_63d_slope_v026_signal,
    f29ccc_f29_cro_client_concentration_revcv_84d_slope_v027_signal,
    f29ccc_f29_cro_client_concentration_revcv_126d_slope_v028_signal,
    f29ccc_f29_cro_client_concentration_revcv_168d_slope_v029_signal,
    f29ccc_f29_cro_client_concentration_revcv_189d_slope_v030_signal,
    f29ccc_f29_cro_client_concentration_revdiv_3d_slope_v031_signal,
    f29ccc_f29_cro_client_concentration_revdiv_5d_slope_v032_signal,
    f29ccc_f29_cro_client_concentration_revdiv_10d_slope_v033_signal,
    f29ccc_f29_cro_client_concentration_revdiv_21d_slope_v034_signal,
    f29ccc_f29_cro_client_concentration_revdiv_42d_slope_v035_signal,
    f29ccc_f29_cro_client_concentration_revdiv_63d_slope_v036_signal,
    f29ccc_f29_cro_client_concentration_revdiv_84d_slope_v037_signal,
    f29ccc_f29_cro_client_concentration_revdiv_126d_slope_v038_signal,
    f29ccc_f29_cro_client_concentration_revdiv_168d_slope_v039_signal,
    f29ccc_f29_cro_client_concentration_revdiv_189d_slope_v040_signal,
    f29ccc_f29_cro_client_concentration_revdiv_3d_slope_v041_signal,
    f29ccc_f29_cro_client_concentration_revdiv_5d_slope_v042_signal,
    f29ccc_f29_cro_client_concentration_revdiv_10d_slope_v043_signal,
    f29ccc_f29_cro_client_concentration_revdiv_21d_slope_v044_signal,
    f29ccc_f29_cro_client_concentration_revdiv_42d_slope_v045_signal,
    f29ccc_f29_cro_client_concentration_revdiv_63d_slope_v046_signal,
    f29ccc_f29_cro_client_concentration_revdiv_84d_slope_v047_signal,
    f29ccc_f29_cro_client_concentration_revdiv_126d_slope_v048_signal,
    f29ccc_f29_cro_client_concentration_revdiv_168d_slope_v049_signal,
    f29ccc_f29_cro_client_concentration_revdiv_189d_slope_v050_signal,
    f29ccc_f29_cro_client_concentration_revdiv_3d_slope_v051_signal,
    f29ccc_f29_cro_client_concentration_revdiv_5d_slope_v052_signal,
    f29ccc_f29_cro_client_concentration_revdiv_10d_slope_v053_signal,
    f29ccc_f29_cro_client_concentration_revdiv_21d_slope_v054_signal,
    f29ccc_f29_cro_client_concentration_revdiv_42d_slope_v055_signal,
    f29ccc_f29_cro_client_concentration_revdiv_63d_slope_v056_signal,
    f29ccc_f29_cro_client_concentration_revdiv_84d_slope_v057_signal,
    f29ccc_f29_cro_client_concentration_revdiv_126d_slope_v058_signal,
    f29ccc_f29_cro_client_concentration_revdiv_168d_slope_v059_signal,
    f29ccc_f29_cro_client_concentration_revdiv_189d_slope_v060_signal,
    f29ccc_f29_cro_client_concentration_conprx_3d_slope_v061_signal,
    f29ccc_f29_cro_client_concentration_conprx_5d_slope_v062_signal,
    f29ccc_f29_cro_client_concentration_conprx_10d_slope_v063_signal,
    f29ccc_f29_cro_client_concentration_conprx_21d_slope_v064_signal,
    f29ccc_f29_cro_client_concentration_conprx_42d_slope_v065_signal,
    f29ccc_f29_cro_client_concentration_conprx_63d_slope_v066_signal,
    f29ccc_f29_cro_client_concentration_conprx_84d_slope_v067_signal,
    f29ccc_f29_cro_client_concentration_conprx_126d_slope_v068_signal,
    f29ccc_f29_cro_client_concentration_conprx_168d_slope_v069_signal,
    f29ccc_f29_cro_client_concentration_conprx_189d_slope_v070_signal,
    f29ccc_f29_cro_client_concentration_conprx_3d_slope_v071_signal,
    f29ccc_f29_cro_client_concentration_conprx_5d_slope_v072_signal,
    f29ccc_f29_cro_client_concentration_conprx_10d_slope_v073_signal,
    f29ccc_f29_cro_client_concentration_conprx_21d_slope_v074_signal,
    f29ccc_f29_cro_client_concentration_conprx_42d_slope_v075_signal,
    f29ccc_f29_cro_client_concentration_conprx_63d_slope_v076_signal,
    f29ccc_f29_cro_client_concentration_conprx_84d_slope_v077_signal,
    f29ccc_f29_cro_client_concentration_conprx_126d_slope_v078_signal,
    f29ccc_f29_cro_client_concentration_conprx_168d_slope_v079_signal,
    f29ccc_f29_cro_client_concentration_conprx_189d_slope_v080_signal,
    f29ccc_f29_cro_client_concentration_conprx_3d_slope_v081_signal,
    f29ccc_f29_cro_client_concentration_conprx_5d_slope_v082_signal,
    f29ccc_f29_cro_client_concentration_conprx_10d_slope_v083_signal,
    f29ccc_f29_cro_client_concentration_conprx_21d_slope_v084_signal,
    f29ccc_f29_cro_client_concentration_conprx_42d_slope_v085_signal,
    f29ccc_f29_cro_client_concentration_conprx_63d_slope_v086_signal,
    f29ccc_f29_cro_client_concentration_conprx_84d_slope_v087_signal,
    f29ccc_f29_cro_client_concentration_conprx_126d_slope_v088_signal,
    f29ccc_f29_cro_client_concentration_conprx_168d_slope_v089_signal,
    f29ccc_f29_cro_client_concentration_conprx_189d_slope_v090_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_3d_slope_v091_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_5d_slope_v092_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_10d_slope_v093_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_21d_slope_v094_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_42d_slope_v095_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_63d_slope_v096_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_84d_slope_v097_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_126d_slope_v098_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_168d_slope_v099_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_189d_slope_v100_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_3d_slope_v101_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_5d_slope_v102_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_10d_slope_v103_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_21d_slope_v104_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_42d_slope_v105_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_63d_slope_v106_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_84d_slope_v107_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_126d_slope_v108_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_168d_slope_v109_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_189d_slope_v110_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_3d_slope_v111_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_5d_slope_v112_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_10d_slope_v113_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_21d_slope_v114_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_42d_slope_v115_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_63d_slope_v116_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_84d_slope_v117_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_126d_slope_v118_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_168d_slope_v119_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_189d_slope_v120_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_3d_slope_v121_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_5d_slope_v122_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_10d_slope_v123_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_21d_slope_v124_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_42d_slope_v125_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_63d_slope_v126_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_84d_slope_v127_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_126d_slope_v128_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_168d_slope_v129_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_189d_slope_v130_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_3d_slope_v131_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_5d_slope_v132_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_10d_slope_v133_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_21d_slope_v134_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_42d_slope_v135_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_63d_slope_v136_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_84d_slope_v137_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_126d_slope_v138_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_168d_slope_v139_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_189d_slope_v140_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_3d_slope_v141_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_5d_slope_v142_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_10d_slope_v143_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_21d_slope_v144_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_42d_slope_v145_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_63d_slope_v146_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_84d_slope_v147_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_126d_slope_v148_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_168d_slope_v149_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_CRO_CLIENT_CONCENTRATION_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f29_revenue_cv", "_f29_revenue_diversification", "_f29_concentration_proxy",)
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
    print(f"OK f29_cro_client_concentration_2nd_derivatives_001_150_claude: {n_features} features pass")
