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
def _f07_opex_intensity(opex, revenue):
    return opex / revenue.replace(0, np.nan)


def _f07_efficiency_trend(opex, revenue, w):
    oi = opex / revenue.replace(0, np.nan)
    return -oi.rolling(w, min_periods=max(1, w // 2)).mean()


def _f07_efficiency_score(opex, sgna, revenue, w):
    oi = opex / revenue.replace(0, np.nan)
    si = sgna / revenue.replace(0, np.nan)
    combined = (oi + si) * 0.5
    return -combined.rolling(w, min_periods=max(1, w // 2)).mean()


def f07uef_f07_utility_efficiency_opexint_mean_5d_base_v001_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_mean_21d_base_v002_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_mean_63d_base_v003_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_mean_126d_base_v004_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_mean_252d_base_v005_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_std_5d_base_v006_signal(opex, revenue, closeadj):
    result = _std(_f07_opex_intensity(opex, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_std_21d_base_v007_signal(opex, revenue, closeadj):
    result = _std(_f07_opex_intensity(opex, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_std_63d_base_v008_signal(opex, revenue, closeadj):
    result = _std(_f07_opex_intensity(opex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_std_126d_base_v009_signal(opex, revenue, closeadj):
    result = _std(_f07_opex_intensity(opex, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_std_252d_base_v010_signal(opex, revenue, closeadj):
    result = _std(_f07_opex_intensity(opex, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_z_5d_base_v011_signal(opex, revenue, closeadj):
    result = _z(_f07_opex_intensity(opex, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_z_21d_base_v012_signal(opex, revenue, closeadj):
    result = _z(_f07_opex_intensity(opex, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_z_63d_base_v013_signal(opex, revenue, closeadj):
    result = _z(_f07_opex_intensity(opex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_z_126d_base_v014_signal(opex, revenue, closeadj):
    result = _z(_f07_opex_intensity(opex, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_z_252d_base_v015_signal(opex, revenue, closeadj):
    result = _z(_f07_opex_intensity(opex, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_ema_5d_base_v016_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_ema_21d_base_v017_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_ema_63d_base_v018_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_ema_126d_base_v019_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_ema_252d_base_v020_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_range_5d_base_v021_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_range_21d_base_v022_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_range_63d_base_v023_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_range_126d_base_v024_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_range_252d_base_v025_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_mean_5d_base_v026_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_mean_21d_base_v027_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_mean_63d_base_v028_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_mean_126d_base_v029_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_mean_252d_base_v030_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_std_5d_base_v031_signal(opex, revenue, closeadj):
    result = _std(_f07_efficiency_trend(opex, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_std_21d_base_v032_signal(opex, revenue, closeadj):
    result = _std(_f07_efficiency_trend(opex, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_std_63d_base_v033_signal(opex, revenue, closeadj):
    result = _std(_f07_efficiency_trend(opex, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_std_126d_base_v034_signal(opex, revenue, closeadj):
    result = _std(_f07_efficiency_trend(opex, revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_std_252d_base_v035_signal(opex, revenue, closeadj):
    result = _std(_f07_efficiency_trend(opex, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_z_5d_base_v036_signal(opex, revenue, closeadj):
    result = _z(_f07_efficiency_trend(opex, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_z_21d_base_v037_signal(opex, revenue, closeadj):
    result = _z(_f07_efficiency_trend(opex, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_z_63d_base_v038_signal(opex, revenue, closeadj):
    result = _z(_f07_efficiency_trend(opex, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_z_126d_base_v039_signal(opex, revenue, closeadj):
    result = _z(_f07_efficiency_trend(opex, revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_z_252d_base_v040_signal(opex, revenue, closeadj):
    result = _z(_f07_efficiency_trend(opex, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_ema_5d_base_v041_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_ema_21d_base_v042_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_ema_63d_base_v043_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_ema_126d_base_v044_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_ema_252d_base_v045_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_range_5d_base_v046_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_range_21d_base_v047_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_range_63d_base_v048_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_range_126d_base_v049_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_range_252d_base_v050_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_mean_5d_base_v051_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_mean_21d_base_v052_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_mean_63d_base_v053_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_mean_126d_base_v054_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_mean_252d_base_v055_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_std_5d_base_v056_signal(opex, sgna, revenue, closeadj):
    result = _std(_f07_efficiency_score(opex, sgna, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_std_21d_base_v057_signal(opex, sgna, revenue, closeadj):
    result = _std(_f07_efficiency_score(opex, sgna, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_std_63d_base_v058_signal(opex, sgna, revenue, closeadj):
    result = _std(_f07_efficiency_score(opex, sgna, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_std_126d_base_v059_signal(opex, sgna, revenue, closeadj):
    result = _std(_f07_efficiency_score(opex, sgna, revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_std_252d_base_v060_signal(opex, sgna, revenue, closeadj):
    result = _std(_f07_efficiency_score(opex, sgna, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_z_5d_base_v061_signal(opex, sgna, revenue, closeadj):
    result = _z(_f07_efficiency_score(opex, sgna, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_z_21d_base_v062_signal(opex, sgna, revenue, closeadj):
    result = _z(_f07_efficiency_score(opex, sgna, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_z_63d_base_v063_signal(opex, sgna, revenue, closeadj):
    result = _z(_f07_efficiency_score(opex, sgna, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_z_126d_base_v064_signal(opex, sgna, revenue, closeadj):
    result = _z(_f07_efficiency_score(opex, sgna, revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_z_252d_base_v065_signal(opex, sgna, revenue, closeadj):
    result = _z(_f07_efficiency_score(opex, sgna, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_ema_5d_base_v066_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_ema_21d_base_v067_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_ema_63d_base_v068_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_ema_126d_base_v069_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_ema_252d_base_v070_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_range_5d_base_v071_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_range_21d_base_v072_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_range_63d_base_v073_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_range_126d_base_v074_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_range_252d_base_v075_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f07uef_f07_utility_efficiency_opexint_mean_5d_base_v001_signal,
    f07uef_f07_utility_efficiency_opexint_mean_21d_base_v002_signal,
    f07uef_f07_utility_efficiency_opexint_mean_63d_base_v003_signal,
    f07uef_f07_utility_efficiency_opexint_mean_126d_base_v004_signal,
    f07uef_f07_utility_efficiency_opexint_mean_252d_base_v005_signal,
    f07uef_f07_utility_efficiency_opexint_std_5d_base_v006_signal,
    f07uef_f07_utility_efficiency_opexint_std_21d_base_v007_signal,
    f07uef_f07_utility_efficiency_opexint_std_63d_base_v008_signal,
    f07uef_f07_utility_efficiency_opexint_std_126d_base_v009_signal,
    f07uef_f07_utility_efficiency_opexint_std_252d_base_v010_signal,
    f07uef_f07_utility_efficiency_opexint_z_5d_base_v011_signal,
    f07uef_f07_utility_efficiency_opexint_z_21d_base_v012_signal,
    f07uef_f07_utility_efficiency_opexint_z_63d_base_v013_signal,
    f07uef_f07_utility_efficiency_opexint_z_126d_base_v014_signal,
    f07uef_f07_utility_efficiency_opexint_z_252d_base_v015_signal,
    f07uef_f07_utility_efficiency_opexint_ema_5d_base_v016_signal,
    f07uef_f07_utility_efficiency_opexint_ema_21d_base_v017_signal,
    f07uef_f07_utility_efficiency_opexint_ema_63d_base_v018_signal,
    f07uef_f07_utility_efficiency_opexint_ema_126d_base_v019_signal,
    f07uef_f07_utility_efficiency_opexint_ema_252d_base_v020_signal,
    f07uef_f07_utility_efficiency_opexint_range_5d_base_v021_signal,
    f07uef_f07_utility_efficiency_opexint_range_21d_base_v022_signal,
    f07uef_f07_utility_efficiency_opexint_range_63d_base_v023_signal,
    f07uef_f07_utility_efficiency_opexint_range_126d_base_v024_signal,
    f07uef_f07_utility_efficiency_opexint_range_252d_base_v025_signal,
    f07uef_f07_utility_efficiency_efftrend_mean_5d_base_v026_signal,
    f07uef_f07_utility_efficiency_efftrend_mean_21d_base_v027_signal,
    f07uef_f07_utility_efficiency_efftrend_mean_63d_base_v028_signal,
    f07uef_f07_utility_efficiency_efftrend_mean_126d_base_v029_signal,
    f07uef_f07_utility_efficiency_efftrend_mean_252d_base_v030_signal,
    f07uef_f07_utility_efficiency_efftrend_std_5d_base_v031_signal,
    f07uef_f07_utility_efficiency_efftrend_std_21d_base_v032_signal,
    f07uef_f07_utility_efficiency_efftrend_std_63d_base_v033_signal,
    f07uef_f07_utility_efficiency_efftrend_std_126d_base_v034_signal,
    f07uef_f07_utility_efficiency_efftrend_std_252d_base_v035_signal,
    f07uef_f07_utility_efficiency_efftrend_z_5d_base_v036_signal,
    f07uef_f07_utility_efficiency_efftrend_z_21d_base_v037_signal,
    f07uef_f07_utility_efficiency_efftrend_z_63d_base_v038_signal,
    f07uef_f07_utility_efficiency_efftrend_z_126d_base_v039_signal,
    f07uef_f07_utility_efficiency_efftrend_z_252d_base_v040_signal,
    f07uef_f07_utility_efficiency_efftrend_ema_5d_base_v041_signal,
    f07uef_f07_utility_efficiency_efftrend_ema_21d_base_v042_signal,
    f07uef_f07_utility_efficiency_efftrend_ema_63d_base_v043_signal,
    f07uef_f07_utility_efficiency_efftrend_ema_126d_base_v044_signal,
    f07uef_f07_utility_efficiency_efftrend_ema_252d_base_v045_signal,
    f07uef_f07_utility_efficiency_efftrend_range_5d_base_v046_signal,
    f07uef_f07_utility_efficiency_efftrend_range_21d_base_v047_signal,
    f07uef_f07_utility_efficiency_efftrend_range_63d_base_v048_signal,
    f07uef_f07_utility_efficiency_efftrend_range_126d_base_v049_signal,
    f07uef_f07_utility_efficiency_efftrend_range_252d_base_v050_signal,
    f07uef_f07_utility_efficiency_effsc_mean_5d_base_v051_signal,
    f07uef_f07_utility_efficiency_effsc_mean_21d_base_v052_signal,
    f07uef_f07_utility_efficiency_effsc_mean_63d_base_v053_signal,
    f07uef_f07_utility_efficiency_effsc_mean_126d_base_v054_signal,
    f07uef_f07_utility_efficiency_effsc_mean_252d_base_v055_signal,
    f07uef_f07_utility_efficiency_effsc_std_5d_base_v056_signal,
    f07uef_f07_utility_efficiency_effsc_std_21d_base_v057_signal,
    f07uef_f07_utility_efficiency_effsc_std_63d_base_v058_signal,
    f07uef_f07_utility_efficiency_effsc_std_126d_base_v059_signal,
    f07uef_f07_utility_efficiency_effsc_std_252d_base_v060_signal,
    f07uef_f07_utility_efficiency_effsc_z_5d_base_v061_signal,
    f07uef_f07_utility_efficiency_effsc_z_21d_base_v062_signal,
    f07uef_f07_utility_efficiency_effsc_z_63d_base_v063_signal,
    f07uef_f07_utility_efficiency_effsc_z_126d_base_v064_signal,
    f07uef_f07_utility_efficiency_effsc_z_252d_base_v065_signal,
    f07uef_f07_utility_efficiency_effsc_ema_5d_base_v066_signal,
    f07uef_f07_utility_efficiency_effsc_ema_21d_base_v067_signal,
    f07uef_f07_utility_efficiency_effsc_ema_63d_base_v068_signal,
    f07uef_f07_utility_efficiency_effsc_ema_126d_base_v069_signal,
    f07uef_f07_utility_efficiency_effsc_ema_252d_base_v070_signal,
    f07uef_f07_utility_efficiency_effsc_range_5d_base_v071_signal,
    f07uef_f07_utility_efficiency_effsc_range_21d_base_v072_signal,
    f07uef_f07_utility_efficiency_effsc_range_63d_base_v073_signal,
    f07uef_f07_utility_efficiency_effsc_range_126d_base_v074_signal,
    f07uef_f07_utility_efficiency_effsc_range_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_UTILITY_EFFICIENCY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "sgna": sgna, "opex": opex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f07_opex_intensity", "_f07_efficiency_trend", "_f07_efficiency_score",)
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
    print(f"OK f07_utility_efficiency_base_001_075_claude: {n_features} features pass")
