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
def _f17_arr_proxy(revenue, deferredrev, w):
    smooth_rev = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (smooth_rev + deferredrev) / revenue.replace(0, np.nan).abs()


def _f17_revenue_recurring_share(deferredrev, revenue, w):
    rev_w = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return deferredrev / rev_w.replace(0, np.nan).abs()


def _f17_arr_quality(revenue, deferredrev, w):
    rev_std = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    rev_mean = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    cv = rev_std / rev_mean.replace(0, np.nan).abs()
    return deferredrev / revenue.replace(0, np.nan).abs() / cv.replace(0, np.nan)


# ===== features =====
def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v001_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v002_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v003_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v004_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v005_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v006_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v007_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v008_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v009_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v010_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v011_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v012_signal(revenue, deferredrev, closeadj):
    result = (-_f17_arr_proxy(revenue, deferredrev, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v013_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21) * _f17_arr_proxy(revenue, deferredrev, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v014_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v015_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v016_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v017_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v018_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v019_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v020_signal(revenue, deferredrev, closeadj):
    result = np.log(_f17_arr_proxy(revenue, deferredrev, 21).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v021_signal(revenue, deferredrev, closeadj):
    result = np.sign(_f17_arr_proxy(revenue, deferredrev, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v022_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v023_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v024_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 21).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v025_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 21).rolling(21, min_periods=max(1, 21 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 21).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v026_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 21).rolling(63, min_periods=max(1, 63 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 21).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_21d_base_v027_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 21).rolling(252, min_periods=max(1, 252 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 21).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v028_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v029_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v030_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v031_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v032_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v033_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v034_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v035_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v036_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v037_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v038_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v039_signal(revenue, deferredrev, closeadj):
    result = (-_f17_arr_proxy(revenue, deferredrev, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v040_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63) * _f17_arr_proxy(revenue, deferredrev, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v041_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v042_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v043_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v044_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v045_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v046_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v047_signal(revenue, deferredrev, closeadj):
    result = np.log(_f17_arr_proxy(revenue, deferredrev, 63).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v048_signal(revenue, deferredrev, closeadj):
    result = np.sign(_f17_arr_proxy(revenue, deferredrev, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v049_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v050_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v051_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 63).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v052_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 63).rolling(21, min_periods=max(1, 21 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 63).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v053_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 63).rolling(63, min_periods=max(1, 63 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 63).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_63d_base_v054_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 63).rolling(252, min_periods=max(1, 252 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 63).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v055_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v056_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v057_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v058_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v059_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v060_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v061_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v062_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v063_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v064_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v065_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v066_signal(revenue, deferredrev, closeadj):
    result = (-_f17_arr_proxy(revenue, deferredrev, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v067_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126) * _f17_arr_proxy(revenue, deferredrev, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v068_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v069_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v070_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v071_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v072_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v073_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v074_signal(revenue, deferredrev, closeadj):
    result = np.log(_f17_arr_proxy(revenue, deferredrev, 126).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v075_signal(revenue, deferredrev, closeadj):
    result = np.sign(_f17_arr_proxy(revenue, deferredrev, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v001_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v002_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v003_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v004_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v005_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v006_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v007_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v008_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v009_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v010_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v011_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v012_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v013_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v014_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v015_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v016_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v017_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v018_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v019_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v020_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v021_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v022_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v023_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v024_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v025_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v026_signal,
    f17has_f17_healthit_arr_signature_arrproxy_21d_base_v027_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v028_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v029_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v030_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v031_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v032_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v033_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v034_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v035_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v036_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v037_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v038_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v039_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v040_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v041_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v042_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v043_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v044_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v045_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v046_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v047_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v048_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v049_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v050_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v051_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v052_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v053_signal,
    f17has_f17_healthit_arr_signature_arrproxy_63d_base_v054_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v055_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v056_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v057_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v058_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v059_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v060_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v061_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v062_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v063_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v064_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v065_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v066_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v067_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v068_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v069_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v070_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v071_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v072_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v073_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v074_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_HEALTHIT_ARR_SIGNATURE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f17_arr_proxy', '_f17_revenue_recurring_share', '_f17_arr_quality')
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
    print(f"OK f17_healthit_arr_signature_base_001_075_claude: {n_features} features pass")
