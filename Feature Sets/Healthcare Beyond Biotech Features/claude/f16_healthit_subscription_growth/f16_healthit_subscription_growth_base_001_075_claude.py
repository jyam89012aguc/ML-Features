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
def _f16_deferred_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f16_subscription_proxy(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan).abs()


def _f16_subscription_acceleration(deferredrev, w):
    g = deferredrev.pct_change(periods=w)
    return g.diff(periods=w)


# ===== features =====
def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v001_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v002_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v003_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v004_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v005_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v006_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v007_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v008_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v009_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v010_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v011_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v012_signal(deferredrev, closeadj):
    result = (-_f16_deferred_growth(deferredrev, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v013_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21) * _f16_deferred_growth(deferredrev, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v014_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v015_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v016_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v017_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v018_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v019_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v020_signal(deferredrev, closeadj):
    result = np.log(_f16_deferred_growth(deferredrev, 21).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v021_signal(deferredrev, closeadj):
    result = np.sign(_f16_deferred_growth(deferredrev, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v022_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v023_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v024_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 21).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v025_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 21).rolling(21, min_periods=max(1, 21 // 2)).max() - _f16_deferred_growth(deferredrev, 21).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v026_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 21).rolling(63, min_periods=max(1, 63 // 2)).max() - _f16_deferred_growth(deferredrev, 21).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v027_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 21).rolling(252, min_periods=max(1, 252 // 2)).max() - _f16_deferred_growth(deferredrev, 21).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v028_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v029_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v030_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v031_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v032_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v033_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v034_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v035_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v036_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v037_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v038_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v039_signal(deferredrev, closeadj):
    result = (-_f16_deferred_growth(deferredrev, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v040_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63) * _f16_deferred_growth(deferredrev, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v041_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v042_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v043_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v044_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v045_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v046_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v047_signal(deferredrev, closeadj):
    result = np.log(_f16_deferred_growth(deferredrev, 63).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v048_signal(deferredrev, closeadj):
    result = np.sign(_f16_deferred_growth(deferredrev, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v049_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v050_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v051_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 63).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v052_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 63).rolling(21, min_periods=max(1, 21 // 2)).max() - _f16_deferred_growth(deferredrev, 63).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v053_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 63).rolling(63, min_periods=max(1, 63 // 2)).max() - _f16_deferred_growth(deferredrev, 63).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v054_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 63).rolling(252, min_periods=max(1, 252 // 2)).max() - _f16_deferred_growth(deferredrev, 63).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v055_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v056_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v057_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v058_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v059_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v060_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v061_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v062_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v063_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v064_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v065_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v066_signal(deferredrev, closeadj):
    result = (-_f16_deferred_growth(deferredrev, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v067_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126) * _f16_deferred_growth(deferredrev, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v068_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v069_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v070_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v071_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v072_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v073_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v074_signal(deferredrev, closeadj):
    result = np.log(_f16_deferred_growth(deferredrev, 126).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v075_signal(deferredrev, closeadj):
    result = np.sign(_f16_deferred_growth(deferredrev, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v001_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v002_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v003_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v004_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v005_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v006_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v007_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v008_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v009_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v010_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v011_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v012_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v013_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v014_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v015_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v016_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v017_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v018_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v019_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v020_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v021_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v022_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v023_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v024_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v025_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v026_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_21d_base_v027_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v028_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v029_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v030_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v031_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v032_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v033_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v034_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v035_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v036_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v037_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v038_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v039_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v040_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v041_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v042_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v043_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v044_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v045_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v046_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v047_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v048_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v049_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v050_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v051_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v052_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v053_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_63d_base_v054_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v055_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v056_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v057_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v058_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v059_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v060_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v061_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v062_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v063_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v064_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v065_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v066_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v067_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v068_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v069_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v070_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v071_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v072_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v073_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v074_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_HEALTHIT_SUBSCRIPTION_GROWTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f16_healthit_subscription_growth_base_001_075_claude: {n_features} features pass")
