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


# 5d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_5d_base_v001_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 5)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_10d_base_v002_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 10)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_21d_base_v003_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_42d_base_v004_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 42)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_63d_base_v005_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_126d_base_v006_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 126)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_189d_base_v007_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 189)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_252d_base_v008_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_378d_base_v009_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 378)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue cv x close
def f29ccc_f29_cro_client_concentration_revcv_504d_base_v010_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 504)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_5d_base_v011_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_10d_base_v012_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_21d_base_v013_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_42d_base_v014_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_63d_base_v015_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_126d_base_v016_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_189d_base_v017_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_252d_base_v018_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_378d_base_v019_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue diversification x close
def f29ccc_f29_cro_client_concentration_revdiv_504d_base_v020_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_5d_base_v021_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 5)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_10d_base_v022_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 10)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_21d_base_v023_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_42d_base_v024_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 42)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_63d_base_v025_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_126d_base_v026_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 126)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_189d_base_v027_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 189)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_252d_base_v028_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_378d_base_v029_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 378)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d concentration proxy x close
def f29ccc_f29_cro_client_concentration_conprx_504d_base_v030_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 504)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_5d_base_v031_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 5)
    result = _z(cv, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_10d_base_v032_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 10)
    result = _z(cv, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_21d_base_v033_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    result = _z(cv, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_42d_base_v034_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 42)
    result = _z(cv, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_63d_base_v035_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    result = _z(cv, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_126d_base_v036_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 126)
    result = _z(cv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_189d_base_v037_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 189)
    result = _z(cv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_252d_base_v038_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    result = _z(cv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_378d_base_v039_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 378)
    result = _z(cv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue cv zscore x close
def f29ccc_f29_cro_client_concentration_revcvz_504d_base_v040_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 504)
    result = _z(cv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_5d_base_v041_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 5)
    result = _z(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_10d_base_v042_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 10)
    result = _z(d, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_21d_base_v043_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    result = _z(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_42d_base_v044_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 42)
    result = _z(d, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_63d_base_v045_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_126d_base_v046_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 126)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_189d_base_v047_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 189)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_252d_base_v048_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_378d_base_v049_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 378)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue diversification zscore x close
def f29ccc_f29_cro_client_concentration_revdivz_504d_base_v050_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 504)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_5d_base_v051_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 5)
    result = _z(cp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_10d_base_v052_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 10)
    result = _z(cp, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_21d_base_v053_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    result = _z(cp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_42d_base_v054_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 42)
    result = _z(cp, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_63d_base_v055_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    result = _z(cp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_126d_base_v056_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 126)
    result = _z(cp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_189d_base_v057_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 189)
    result = _z(cp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_252d_base_v058_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    result = _z(cp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_378d_base_v059_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 378)
    result = _z(cp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d concentration proxy zscore x close
def f29ccc_f29_cro_client_concentration_conprxz_504d_base_v060_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 504)
    result = _z(cp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d revenue cv x deferred rev mean
def f29ccc_f29_cro_client_concentration_revcvxdr_5d_base_v061_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 5)
    dr = deferredrev.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = cv * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue cv x deferred rev mean
def f29ccc_f29_cro_client_concentration_revcvxdr_10d_base_v062_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 10)
    dr = deferredrev.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = cv * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue cv x deferred rev mean
def f29ccc_f29_cro_client_concentration_revcvxdr_21d_base_v063_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = cv * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue cv x deferred rev mean
def f29ccc_f29_cro_client_concentration_revcvxdr_42d_base_v064_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = cv * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue cv x deferred rev mean
def f29ccc_f29_cro_client_concentration_revcvxdr_63d_base_v065_signal(revenue, deferredrev):
    cv = _f29_revenue_cv(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = cv * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d revenue divers x deferred rev mean
def f29ccc_f29_cro_client_concentration_revdivxdr_5d_base_v066_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 5)
    dr = deferredrev.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = d * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue divers x deferred rev mean
def f29ccc_f29_cro_client_concentration_revdivxdr_10d_base_v067_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 10)
    dr = deferredrev.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = d * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue divers x deferred rev mean
def f29ccc_f29_cro_client_concentration_revdivxdr_21d_base_v068_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = d * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue divers x deferred rev mean
def f29ccc_f29_cro_client_concentration_revdivxdr_42d_base_v069_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = d * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue divers x deferred rev mean
def f29ccc_f29_cro_client_concentration_revdivxdr_63d_base_v070_signal(revenue, deferredrev):
    d = _f29_revenue_diversification(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = d * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d concentration proxy x deferred rev mean
def f29ccc_f29_cro_client_concentration_conprxxdr_5d_base_v071_signal(revenue, deferredrev):
    cp = _f29_concentration_proxy(revenue, 5)
    dr = deferredrev.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = cp * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d concentration proxy x deferred rev mean
def f29ccc_f29_cro_client_concentration_conprxxdr_10d_base_v072_signal(revenue, deferredrev):
    cp = _f29_concentration_proxy(revenue, 10)
    dr = deferredrev.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = cp * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d concentration proxy x deferred rev mean
def f29ccc_f29_cro_client_concentration_conprxxdr_21d_base_v073_signal(revenue, deferredrev):
    cp = _f29_concentration_proxy(revenue, 21)
    dr = deferredrev.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = cp * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d concentration proxy x deferred rev mean
def f29ccc_f29_cro_client_concentration_conprxxdr_42d_base_v074_signal(revenue, deferredrev):
    cp = _f29_concentration_proxy(revenue, 42)
    dr = deferredrev.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = cp * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d concentration proxy x deferred rev mean
def f29ccc_f29_cro_client_concentration_conprxxdr_63d_base_v075_signal(revenue, deferredrev):
    cp = _f29_concentration_proxy(revenue, 63)
    dr = deferredrev.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = cp * dr / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f29ccc_f29_cro_client_concentration_revcv_5d_base_v001_signal,
    f29ccc_f29_cro_client_concentration_revcv_10d_base_v002_signal,
    f29ccc_f29_cro_client_concentration_revcv_21d_base_v003_signal,
    f29ccc_f29_cro_client_concentration_revcv_42d_base_v004_signal,
    f29ccc_f29_cro_client_concentration_revcv_63d_base_v005_signal,
    f29ccc_f29_cro_client_concentration_revcv_126d_base_v006_signal,
    f29ccc_f29_cro_client_concentration_revcv_189d_base_v007_signal,
    f29ccc_f29_cro_client_concentration_revcv_252d_base_v008_signal,
    f29ccc_f29_cro_client_concentration_revcv_378d_base_v009_signal,
    f29ccc_f29_cro_client_concentration_revcv_504d_base_v010_signal,
    f29ccc_f29_cro_client_concentration_revdiv_5d_base_v011_signal,
    f29ccc_f29_cro_client_concentration_revdiv_10d_base_v012_signal,
    f29ccc_f29_cro_client_concentration_revdiv_21d_base_v013_signal,
    f29ccc_f29_cro_client_concentration_revdiv_42d_base_v014_signal,
    f29ccc_f29_cro_client_concentration_revdiv_63d_base_v015_signal,
    f29ccc_f29_cro_client_concentration_revdiv_126d_base_v016_signal,
    f29ccc_f29_cro_client_concentration_revdiv_189d_base_v017_signal,
    f29ccc_f29_cro_client_concentration_revdiv_252d_base_v018_signal,
    f29ccc_f29_cro_client_concentration_revdiv_378d_base_v019_signal,
    f29ccc_f29_cro_client_concentration_revdiv_504d_base_v020_signal,
    f29ccc_f29_cro_client_concentration_conprx_5d_base_v021_signal,
    f29ccc_f29_cro_client_concentration_conprx_10d_base_v022_signal,
    f29ccc_f29_cro_client_concentration_conprx_21d_base_v023_signal,
    f29ccc_f29_cro_client_concentration_conprx_42d_base_v024_signal,
    f29ccc_f29_cro_client_concentration_conprx_63d_base_v025_signal,
    f29ccc_f29_cro_client_concentration_conprx_126d_base_v026_signal,
    f29ccc_f29_cro_client_concentration_conprx_189d_base_v027_signal,
    f29ccc_f29_cro_client_concentration_conprx_252d_base_v028_signal,
    f29ccc_f29_cro_client_concentration_conprx_378d_base_v029_signal,
    f29ccc_f29_cro_client_concentration_conprx_504d_base_v030_signal,
    f29ccc_f29_cro_client_concentration_revcvz_5d_base_v031_signal,
    f29ccc_f29_cro_client_concentration_revcvz_10d_base_v032_signal,
    f29ccc_f29_cro_client_concentration_revcvz_21d_base_v033_signal,
    f29ccc_f29_cro_client_concentration_revcvz_42d_base_v034_signal,
    f29ccc_f29_cro_client_concentration_revcvz_63d_base_v035_signal,
    f29ccc_f29_cro_client_concentration_revcvz_126d_base_v036_signal,
    f29ccc_f29_cro_client_concentration_revcvz_189d_base_v037_signal,
    f29ccc_f29_cro_client_concentration_revcvz_252d_base_v038_signal,
    f29ccc_f29_cro_client_concentration_revcvz_378d_base_v039_signal,
    f29ccc_f29_cro_client_concentration_revcvz_504d_base_v040_signal,
    f29ccc_f29_cro_client_concentration_revdivz_5d_base_v041_signal,
    f29ccc_f29_cro_client_concentration_revdivz_10d_base_v042_signal,
    f29ccc_f29_cro_client_concentration_revdivz_21d_base_v043_signal,
    f29ccc_f29_cro_client_concentration_revdivz_42d_base_v044_signal,
    f29ccc_f29_cro_client_concentration_revdivz_63d_base_v045_signal,
    f29ccc_f29_cro_client_concentration_revdivz_126d_base_v046_signal,
    f29ccc_f29_cro_client_concentration_revdivz_189d_base_v047_signal,
    f29ccc_f29_cro_client_concentration_revdivz_252d_base_v048_signal,
    f29ccc_f29_cro_client_concentration_revdivz_378d_base_v049_signal,
    f29ccc_f29_cro_client_concentration_revdivz_504d_base_v050_signal,
    f29ccc_f29_cro_client_concentration_conprxz_5d_base_v051_signal,
    f29ccc_f29_cro_client_concentration_conprxz_10d_base_v052_signal,
    f29ccc_f29_cro_client_concentration_conprxz_21d_base_v053_signal,
    f29ccc_f29_cro_client_concentration_conprxz_42d_base_v054_signal,
    f29ccc_f29_cro_client_concentration_conprxz_63d_base_v055_signal,
    f29ccc_f29_cro_client_concentration_conprxz_126d_base_v056_signal,
    f29ccc_f29_cro_client_concentration_conprxz_189d_base_v057_signal,
    f29ccc_f29_cro_client_concentration_conprxz_252d_base_v058_signal,
    f29ccc_f29_cro_client_concentration_conprxz_378d_base_v059_signal,
    f29ccc_f29_cro_client_concentration_conprxz_504d_base_v060_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_5d_base_v061_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_10d_base_v062_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_21d_base_v063_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_42d_base_v064_signal,
    f29ccc_f29_cro_client_concentration_revcvxdr_63d_base_v065_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_5d_base_v066_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_10d_base_v067_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_21d_base_v068_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_42d_base_v069_signal,
    f29ccc_f29_cro_client_concentration_revdivxdr_63d_base_v070_signal,
    f29ccc_f29_cro_client_concentration_conprxxdr_5d_base_v071_signal,
    f29ccc_f29_cro_client_concentration_conprxxdr_10d_base_v072_signal,
    f29ccc_f29_cro_client_concentration_conprxxdr_21d_base_v073_signal,
    f29ccc_f29_cro_client_concentration_conprxxdr_42d_base_v074_signal,
    f29ccc_f29_cro_client_concentration_conprxxdr_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_CRO_CLIENT_CONCENTRATION_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f29_cro_client_concentration_base_001_075_claude: {n_features} features pass")
