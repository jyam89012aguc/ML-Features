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
def _f16_deferred_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f16_subscription_proxy(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan).abs()


def _f16_subscription_acceleration(deferredrev, w):
    g = deferredrev.pct_change(periods=w)
    return g.diff(periods=w)


# ===== features =====
def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v001_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v002_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v003_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v004_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v005_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v006_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v007_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v008_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v009_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v010_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v011_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v012_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v013_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v014_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v015_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v016_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v017_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v018_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v019_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v020_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v021_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v022_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v023_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v024_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * closeadj
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v025_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v026_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v027_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v028_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v029_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v030_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v031_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v032_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v033_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v034_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v035_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v036_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 21)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v037_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v038_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v039_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v040_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v041_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v042_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v043_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v044_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v045_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v046_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v047_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v048_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 63)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v049_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v050_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v051_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v052_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v053_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v054_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v055_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v056_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v057_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v058_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v059_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v060_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 21), 126)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v061_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v062_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v063_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v064_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v065_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v066_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v067_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v068_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v069_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v070_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v071_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v072_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v073_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v074_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v075_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v076_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v077_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v078_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v079_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v080_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v081_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v082_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v083_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v084_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v085_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v086_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v087_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v088_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v089_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v090_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v091_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v092_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v093_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v094_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v095_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v096_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v097_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v098_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v099_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v100_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v101_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v102_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v103_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v104_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v105_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v106_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v107_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v108_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v109_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v110_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v111_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v112_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v113_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v114_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v115_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v116_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v117_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v118_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v119_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v120_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v121_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v122_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v123_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v124_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v125_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v126_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v127_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v128_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v129_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v130_signal(deferredrev):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v131_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v132_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v133_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v134_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v135_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v136_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v137_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v138_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v139_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v140_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v141_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v142_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v143_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v144_signal(deferredrev, closeadj):
    base = _f16_deferred_growth(deferredrev, 63) * closeadj
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v145_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 63), 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v146_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 63), 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v147_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 63), 21)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v148_signal(deferredrev):
    base = _mean(_f16_deferred_growth(deferredrev, 63), 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v149_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 63), 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v150_signal(deferredrev, closeadj):
    base = _mean(_f16_deferred_growth(deferredrev, 63), 21)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v001_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v002_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v003_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v004_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v005_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v006_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v007_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v008_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v009_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v010_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v011_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v012_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v013_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v014_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v015_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v016_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v017_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v018_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v019_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v020_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v021_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v022_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v023_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v024_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v025_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v026_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v027_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v028_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v029_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v030_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v031_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v032_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v033_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v034_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v035_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v036_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v037_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v038_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v039_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v040_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v041_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v042_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v043_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v044_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v045_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v046_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v047_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v048_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v049_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v050_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v051_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v052_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v053_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v054_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v055_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v056_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v057_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v058_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v059_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v060_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v061_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v062_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v063_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v064_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v065_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v066_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v067_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v068_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v069_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v070_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v071_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v072_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v073_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v074_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v075_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v076_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v077_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v078_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v079_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v080_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v081_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v082_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v083_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v084_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v085_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v086_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v087_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v088_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v089_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v090_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v091_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v092_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v093_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v094_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v095_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v096_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v097_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v098_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v099_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v100_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v101_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v102_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v103_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v104_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v105_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v106_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v107_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v108_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v109_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v110_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v111_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v112_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v113_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v114_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v115_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v116_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v117_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v118_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v119_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_jerk_v120_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v121_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v122_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v123_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v124_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v125_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v126_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v127_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v128_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v129_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v130_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v131_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v132_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v133_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v134_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v135_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v136_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v137_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v138_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v139_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v140_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v141_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v142_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v143_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v144_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v145_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v146_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v147_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v148_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v149_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_HEALTHIT_SUBSCRIPTION_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "sgna": sgna,
        "opex": opex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f16_deferred_growth', '_f16_subscription_proxy', '_f16_subscription_acceleration')
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
    print(f"OK f16_healthit_subscription_growth_3rd_derivatives_001_150_claude: {n_features} features pass")
