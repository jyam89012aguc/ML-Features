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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v001_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v002_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v003_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v004_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v005_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v006_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v007_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v008_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v009_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v010_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v011_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v012_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v013_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v014_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v015_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v016_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v017_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v018_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v019_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v020_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v021_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v022_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v023_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v024_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v025_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v026_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v027_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v028_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v029_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v030_signal(revenue, closeadj):
    base = _f37_revenue_accel(revenue, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v031_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v032_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v033_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v034_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v035_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v036_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v037_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v038_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v039_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v040_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v041_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v042_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v043_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v044_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v045_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v046_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v047_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v048_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v049_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v050_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v051_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v052_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v053_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v054_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v055_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v056_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v057_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v058_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v059_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v060_signal(revenue, grossmargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v061_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v062_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v063_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v064_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v065_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v068_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v069_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v070_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v071_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v072_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v073_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v076_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v077_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v078_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v079_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v080_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v081_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v082_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v083_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v084_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v085_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v086_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v087_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v088_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v089_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v090_signal(revenue, ebitdamargin, closeadj):
    base = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v091_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v092_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v093_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v094_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v095_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v096_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v097_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v098_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v099_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v100_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v101_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v102_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v103_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v104_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v105_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v106_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v107_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v108_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v109_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v110_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v111_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v112_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v113_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v114_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v115_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v116_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v117_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v118_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v119_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v120_signal(revenue, grossmargin, closeadj):
    base = _f37_revenue_accel(revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v121_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21) * ebitdamargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v122_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21) * ebitdamargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v123_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21) * ebitdamargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v124_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21) * ebitdamargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v125_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21) * ebitdamargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v126_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 21) * ebitdamargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v127_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63) * ebitdamargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v128_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63) * ebitdamargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v129_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63) * ebitdamargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v130_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63) * ebitdamargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v131_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63) * ebitdamargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v132_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 63) * ebitdamargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v133_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126) * ebitdamargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v134_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126) * ebitdamargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v135_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126) * ebitdamargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v136_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126) * ebitdamargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v137_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126) * ebitdamargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v138_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 126) * ebitdamargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v139_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252) * ebitdamargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v140_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252) * ebitdamargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v141_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252) * ebitdamargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v142_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252) * ebitdamargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v143_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252) * ebitdamargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v144_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 252) * ebitdamargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v145_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378) * ebitdamargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v146_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378) * ebitdamargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v147_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378) * ebitdamargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v148_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378) * ebitdamargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v149_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378) * ebitdamargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v150_signal(revenue, grossmargin, ebitdamargin, closeadj):
    base = _f37_brand_cycle_signal(revenue, grossmargin, 378) * ebitdamargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v001_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v002_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v003_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v004_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v005_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_21d_slope_v006_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v007_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v008_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v009_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v010_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v011_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_63d_slope_v012_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v013_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v014_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v015_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v016_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v017_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_126d_slope_v018_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v019_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v020_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v021_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v022_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v023_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_252d_slope_v024_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v025_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v026_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v027_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v028_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v029_signal,
    f37fbc_f37_footwear_brand_cycle_revaccel_378d_slope_v030_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v031_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v032_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v033_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v034_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v035_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_21d_slope_v036_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v037_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v038_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v039_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v040_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v041_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_63d_slope_v042_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v043_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v044_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v045_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v046_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v047_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_126d_slope_v048_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v049_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v050_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v051_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v052_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v053_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_252d_slope_v054_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v055_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v056_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v057_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v058_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v059_signal,
    f37fbc_f37_footwear_brand_cycle_brandcyc_378d_slope_v060_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v061_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v062_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v063_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v064_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v065_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_21d_slope_v066_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v067_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v068_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v069_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v070_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v071_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_63d_slope_v072_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v073_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v074_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v075_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v076_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v077_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_126d_slope_v078_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v079_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v080_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v081_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v082_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v083_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_252d_slope_v084_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v085_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v086_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v087_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v088_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v089_signal,
    f37fbc_f37_footwear_brand_cycle_prodcyc_378d_slope_v090_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v091_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v092_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v093_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v094_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v095_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_21d_slope_v096_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v097_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v098_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v099_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v100_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v101_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_63d_slope_v102_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v103_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v104_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v105_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v106_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v107_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_126d_slope_v108_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v109_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v110_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v111_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v112_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v113_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_252d_slope_v114_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v115_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v116_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v117_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v118_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v119_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxgm_378d_slope_v120_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v121_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v122_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v123_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v124_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v125_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_21d_slope_v126_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v127_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v128_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v129_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v130_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v131_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_63d_slope_v132_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v133_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v134_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v135_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v136_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v137_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_126d_slope_v138_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v139_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v140_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v141_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v142_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v143_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_252d_slope_v144_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v145_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v146_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v147_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v148_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v149_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxem_378d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_FOOTWEAR_BRAND_CYCLE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f37_footwear_brand_cycle_slope_001_150_claude: {n_features} features pass")
