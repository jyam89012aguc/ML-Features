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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f37_revenue_accel(revenue, w):
    # Second derivative of log revenue (acceleration)
    lr = np.log(revenue.replace(0, np.nan).abs())
    return lr.diff(w).diff(w)


def _f37_brand_cycle_signal(revenue, grossmargin, w):
    # Revenue growth + margin maintenance
    rev_g = revenue.pct_change(w)
    gm_stab = -_std(grossmargin, w)
    return rev_g + gm_stab


def _f37_product_cycle_score(revenue, ebitdamargin, w):
    # Revenue acceleration weighted by ebitda margin level
    lr = np.log(revenue.replace(0, np.nan).abs())
    accel = lr.diff(w).diff(w)
    return accel * _mean(ebitdamargin, w)


def f37fbc_f37_footwear_brand_cycle_revaccel_5d_base_v001_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_10d_base_v002_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_base_v003_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_42d_base_v004_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_base_v005_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_base_v006_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_189d_base_v007_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_base_v008_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_base_v009_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_504d_base_v010_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_5d_base_v011_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_10d_base_v012_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_base_v013_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_42d_base_v014_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_base_v015_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_base_v016_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_189d_base_v017_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_base_v018_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_base_v019_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_504d_base_v020_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_5d_base_v021_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_10d_base_v022_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_base_v023_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_42d_base_v024_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_base_v025_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_base_v026_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_189d_base_v027_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_base_v028_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_base_v029_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_504d_base_v030_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelz_21d_base_v031_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _z(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelz_63d_base_v032_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelz_126d_base_v033_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelz_252d_base_v034_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelz_378d_base_v035_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelz_504d_base_v036_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycema_10d_base_v037_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycema_21d_base_v038_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycema_42d_base_v039_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycema_63d_base_v040_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycema_126d_base_v041_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycema_252d_base_v042_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_base_v043_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_42d_base_v044_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 42)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_base_v045_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_base_v046_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 126)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_base_v047_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_504d_base_v048_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 504)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxgm_21d_base_v049_signal(revenue, ebitdamargin, grossmargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxgm_63d_base_v050_signal(revenue, ebitdamargin, grossmargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxgm_126d_base_v051_signal(revenue, ebitdamargin, grossmargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxgm_189d_base_v052_signal(revenue, ebitdamargin, grossmargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 189)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxgm_252d_base_v053_signal(revenue, ebitdamargin, grossmargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxgm_378d_base_v054_signal(revenue, ebitdamargin, grossmargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_base_v055_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_base_v056_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_base_v057_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_189d_base_v058_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 189)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_base_v059_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_base_v060_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelstd_42d_base_v061_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _std(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelstd_63d_base_v062_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelstd_126d_base_v063_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _std(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelstd_189d_base_v064_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _std(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelstd_252d_base_v065_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelstd_378d_base_v066_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _std(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycstd_63d_base_v067_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycstd_252d_base_v068_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycz_63d_base_v069_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycz_252d_base_v070_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelmean_63d_base_v071_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _mean(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelmean_252d_base_v072_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _mean(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycmean_189d_base_v073_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _mean(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycema_126d_base_v074_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycema_252d_base_v075_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37fbc_f37_footwear_brand_cycle_revaccel_5d_base_v001_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_10d_base_v002_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_base_v003_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_42d_base_v004_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_base_v005_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_base_v006_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_189d_base_v007_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_base_v008_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_base_v009_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_504d_base_v010_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_5d_base_v011_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_10d_base_v012_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_base_v013_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_42d_base_v014_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_base_v015_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_base_v016_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_189d_base_v017_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_base_v018_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_base_v019_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_504d_base_v020_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_5d_base_v021_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_10d_base_v022_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_base_v023_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_42d_base_v024_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_base_v025_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_base_v026_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_189d_base_v027_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_base_v028_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_base_v029_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_504d_base_v030_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelz_21d_base_v031_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelz_63d_base_v032_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelz_126d_base_v033_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelz_252d_base_v034_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelz_378d_base_v035_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelz_504d_base_v036_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycema_10d_base_v037_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycema_21d_base_v038_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycema_42d_base_v039_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycema_63d_base_v040_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycema_126d_base_v041_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycema_252d_base_v042_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_base_v043_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_42d_base_v044_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_base_v045_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_base_v046_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_base_v047_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_504d_base_v048_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxgm_21d_base_v049_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxgm_63d_base_v050_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxgm_126d_base_v051_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxgm_189d_base_v052_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxgm_252d_base_v053_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxgm_378d_base_v054_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_base_v055_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_base_v056_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_base_v057_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_189d_base_v058_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_base_v059_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_base_v060_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelstd_42d_base_v061_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelstd_63d_base_v062_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelstd_126d_base_v063_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelstd_189d_base_v064_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelstd_252d_base_v065_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelstd_378d_base_v066_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycstd_63d_base_v067_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycstd_252d_base_v068_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycz_63d_base_v069_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycz_252d_base_v070_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelmean_63d_base_v071_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelmean_252d_base_v072_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycmean_189d_base_v073_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycema_126d_base_v074_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycema_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_FOOTWEAR_BRAND_CYCLE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_revenue_accel", "_f37_brand_cycle_signal", "_f37_product_cycle_score",)
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
    print(f"OK f37_footwear_brand_cycle_001_075_claude: {n_features} features pass")
