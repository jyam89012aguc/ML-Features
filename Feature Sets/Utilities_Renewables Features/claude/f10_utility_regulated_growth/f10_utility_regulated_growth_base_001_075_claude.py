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
def _f10_long_cycle_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f10_compounding_quality(revenue, w):
    g = revenue.pct_change(periods=w)
    g_mean = g.rolling(w, min_periods=max(1, w // 2)).mean()
    g_std = g.rolling(w, min_periods=max(1, w // 2)).std()
    return g_mean / g_std.replace(0, np.nan)


def _f10_revenue_compound(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return (rg + eg) * 0.5


def f10urg_f10_utility_regulated_growth_longg_mean_5d_base_v001_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_mean_21d_base_v002_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_mean_63d_base_v003_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_mean_126d_base_v004_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_mean_252d_base_v005_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_std_5d_base_v006_signal(revenue, closeadj):
    result = _std(_f10_long_cycle_growth(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_std_21d_base_v007_signal(revenue, closeadj):
    result = _std(_f10_long_cycle_growth(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_std_63d_base_v008_signal(revenue, closeadj):
    result = _std(_f10_long_cycle_growth(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_std_126d_base_v009_signal(revenue, closeadj):
    result = _std(_f10_long_cycle_growth(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_std_252d_base_v010_signal(revenue, closeadj):
    result = _std(_f10_long_cycle_growth(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_z_5d_base_v011_signal(revenue, closeadj):
    result = _z(_f10_long_cycle_growth(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_z_21d_base_v012_signal(revenue, closeadj):
    result = _z(_f10_long_cycle_growth(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_z_63d_base_v013_signal(revenue, closeadj):
    result = _z(_f10_long_cycle_growth(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_z_126d_base_v014_signal(revenue, closeadj):
    result = _z(_f10_long_cycle_growth(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_z_252d_base_v015_signal(revenue, closeadj):
    result = _z(_f10_long_cycle_growth(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_ema_5d_base_v016_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_ema_21d_base_v017_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_ema_63d_base_v018_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_ema_126d_base_v019_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_ema_252d_base_v020_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_range_5d_base_v021_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_range_21d_base_v022_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_range_63d_base_v023_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_range_126d_base_v024_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_range_252d_base_v025_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_mean_5d_base_v026_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_mean_21d_base_v027_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_mean_63d_base_v028_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_mean_126d_base_v029_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_mean_252d_base_v030_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_std_5d_base_v031_signal(revenue, closeadj):
    result = _std(_f10_compounding_quality(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_std_21d_base_v032_signal(revenue, closeadj):
    result = _std(_f10_compounding_quality(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_std_63d_base_v033_signal(revenue, closeadj):
    result = _std(_f10_compounding_quality(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_std_126d_base_v034_signal(revenue, closeadj):
    result = _std(_f10_compounding_quality(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_std_252d_base_v035_signal(revenue, closeadj):
    result = _std(_f10_compounding_quality(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_z_5d_base_v036_signal(revenue, closeadj):
    result = _z(_f10_compounding_quality(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_z_21d_base_v037_signal(revenue, closeadj):
    result = _z(_f10_compounding_quality(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_z_63d_base_v038_signal(revenue, closeadj):
    result = _z(_f10_compounding_quality(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_z_126d_base_v039_signal(revenue, closeadj):
    result = _z(_f10_compounding_quality(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_z_252d_base_v040_signal(revenue, closeadj):
    result = _z(_f10_compounding_quality(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_ema_5d_base_v041_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_ema_21d_base_v042_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_ema_63d_base_v043_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_ema_126d_base_v044_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_ema_252d_base_v045_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_range_5d_base_v046_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_range_21d_base_v047_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_range_63d_base_v048_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_range_126d_base_v049_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_range_252d_base_v050_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_mean_5d_base_v051_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_mean_21d_base_v052_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_mean_63d_base_v053_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_mean_126d_base_v054_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_mean_252d_base_v055_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_std_5d_base_v056_signal(revenue, ebitda, closeadj):
    result = _std(_f10_revenue_compound(revenue, ebitda, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_std_21d_base_v057_signal(revenue, ebitda, closeadj):
    result = _std(_f10_revenue_compound(revenue, ebitda, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_std_63d_base_v058_signal(revenue, ebitda, closeadj):
    result = _std(_f10_revenue_compound(revenue, ebitda, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_std_126d_base_v059_signal(revenue, ebitda, closeadj):
    result = _std(_f10_revenue_compound(revenue, ebitda, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_std_252d_base_v060_signal(revenue, ebitda, closeadj):
    result = _std(_f10_revenue_compound(revenue, ebitda, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_z_5d_base_v061_signal(revenue, ebitda, closeadj):
    result = _z(_f10_revenue_compound(revenue, ebitda, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_z_21d_base_v062_signal(revenue, ebitda, closeadj):
    result = _z(_f10_revenue_compound(revenue, ebitda, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_z_63d_base_v063_signal(revenue, ebitda, closeadj):
    result = _z(_f10_revenue_compound(revenue, ebitda, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_z_126d_base_v064_signal(revenue, ebitda, closeadj):
    result = _z(_f10_revenue_compound(revenue, ebitda, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_z_252d_base_v065_signal(revenue, ebitda, closeadj):
    result = _z(_f10_revenue_compound(revenue, ebitda, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_ema_5d_base_v066_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_ema_21d_base_v067_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_ema_63d_base_v068_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_ema_126d_base_v069_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_ema_252d_base_v070_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_range_5d_base_v071_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_range_21d_base_v072_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_range_63d_base_v073_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_range_126d_base_v074_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_range_252d_base_v075_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f10urg_f10_utility_regulated_growth_longg_mean_5d_base_v001_signal,
    f10urg_f10_utility_regulated_growth_longg_mean_21d_base_v002_signal,
    f10urg_f10_utility_regulated_growth_longg_mean_63d_base_v003_signal,
    f10urg_f10_utility_regulated_growth_longg_mean_126d_base_v004_signal,
    f10urg_f10_utility_regulated_growth_longg_mean_252d_base_v005_signal,
    f10urg_f10_utility_regulated_growth_longg_std_5d_base_v006_signal,
    f10urg_f10_utility_regulated_growth_longg_std_21d_base_v007_signal,
    f10urg_f10_utility_regulated_growth_longg_std_63d_base_v008_signal,
    f10urg_f10_utility_regulated_growth_longg_std_126d_base_v009_signal,
    f10urg_f10_utility_regulated_growth_longg_std_252d_base_v010_signal,
    f10urg_f10_utility_regulated_growth_longg_z_5d_base_v011_signal,
    f10urg_f10_utility_regulated_growth_longg_z_21d_base_v012_signal,
    f10urg_f10_utility_regulated_growth_longg_z_63d_base_v013_signal,
    f10urg_f10_utility_regulated_growth_longg_z_126d_base_v014_signal,
    f10urg_f10_utility_regulated_growth_longg_z_252d_base_v015_signal,
    f10urg_f10_utility_regulated_growth_longg_ema_5d_base_v016_signal,
    f10urg_f10_utility_regulated_growth_longg_ema_21d_base_v017_signal,
    f10urg_f10_utility_regulated_growth_longg_ema_63d_base_v018_signal,
    f10urg_f10_utility_regulated_growth_longg_ema_126d_base_v019_signal,
    f10urg_f10_utility_regulated_growth_longg_ema_252d_base_v020_signal,
    f10urg_f10_utility_regulated_growth_longg_range_5d_base_v021_signal,
    f10urg_f10_utility_regulated_growth_longg_range_21d_base_v022_signal,
    f10urg_f10_utility_regulated_growth_longg_range_63d_base_v023_signal,
    f10urg_f10_utility_regulated_growth_longg_range_126d_base_v024_signal,
    f10urg_f10_utility_regulated_growth_longg_range_252d_base_v025_signal,
    f10urg_f10_utility_regulated_growth_compq_mean_5d_base_v026_signal,
    f10urg_f10_utility_regulated_growth_compq_mean_21d_base_v027_signal,
    f10urg_f10_utility_regulated_growth_compq_mean_63d_base_v028_signal,
    f10urg_f10_utility_regulated_growth_compq_mean_126d_base_v029_signal,
    f10urg_f10_utility_regulated_growth_compq_mean_252d_base_v030_signal,
    f10urg_f10_utility_regulated_growth_compq_std_5d_base_v031_signal,
    f10urg_f10_utility_regulated_growth_compq_std_21d_base_v032_signal,
    f10urg_f10_utility_regulated_growth_compq_std_63d_base_v033_signal,
    f10urg_f10_utility_regulated_growth_compq_std_126d_base_v034_signal,
    f10urg_f10_utility_regulated_growth_compq_std_252d_base_v035_signal,
    f10urg_f10_utility_regulated_growth_compq_z_5d_base_v036_signal,
    f10urg_f10_utility_regulated_growth_compq_z_21d_base_v037_signal,
    f10urg_f10_utility_regulated_growth_compq_z_63d_base_v038_signal,
    f10urg_f10_utility_regulated_growth_compq_z_126d_base_v039_signal,
    f10urg_f10_utility_regulated_growth_compq_z_252d_base_v040_signal,
    f10urg_f10_utility_regulated_growth_compq_ema_5d_base_v041_signal,
    f10urg_f10_utility_regulated_growth_compq_ema_21d_base_v042_signal,
    f10urg_f10_utility_regulated_growth_compq_ema_63d_base_v043_signal,
    f10urg_f10_utility_regulated_growth_compq_ema_126d_base_v044_signal,
    f10urg_f10_utility_regulated_growth_compq_ema_252d_base_v045_signal,
    f10urg_f10_utility_regulated_growth_compq_range_5d_base_v046_signal,
    f10urg_f10_utility_regulated_growth_compq_range_21d_base_v047_signal,
    f10urg_f10_utility_regulated_growth_compq_range_63d_base_v048_signal,
    f10urg_f10_utility_regulated_growth_compq_range_126d_base_v049_signal,
    f10urg_f10_utility_regulated_growth_compq_range_252d_base_v050_signal,
    f10urg_f10_utility_regulated_growth_revcomp_mean_5d_base_v051_signal,
    f10urg_f10_utility_regulated_growth_revcomp_mean_21d_base_v052_signal,
    f10urg_f10_utility_regulated_growth_revcomp_mean_63d_base_v053_signal,
    f10urg_f10_utility_regulated_growth_revcomp_mean_126d_base_v054_signal,
    f10urg_f10_utility_regulated_growth_revcomp_mean_252d_base_v055_signal,
    f10urg_f10_utility_regulated_growth_revcomp_std_5d_base_v056_signal,
    f10urg_f10_utility_regulated_growth_revcomp_std_21d_base_v057_signal,
    f10urg_f10_utility_regulated_growth_revcomp_std_63d_base_v058_signal,
    f10urg_f10_utility_regulated_growth_revcomp_std_126d_base_v059_signal,
    f10urg_f10_utility_regulated_growth_revcomp_std_252d_base_v060_signal,
    f10urg_f10_utility_regulated_growth_revcomp_z_5d_base_v061_signal,
    f10urg_f10_utility_regulated_growth_revcomp_z_21d_base_v062_signal,
    f10urg_f10_utility_regulated_growth_revcomp_z_63d_base_v063_signal,
    f10urg_f10_utility_regulated_growth_revcomp_z_126d_base_v064_signal,
    f10urg_f10_utility_regulated_growth_revcomp_z_252d_base_v065_signal,
    f10urg_f10_utility_regulated_growth_revcomp_ema_5d_base_v066_signal,
    f10urg_f10_utility_regulated_growth_revcomp_ema_21d_base_v067_signal,
    f10urg_f10_utility_regulated_growth_revcomp_ema_63d_base_v068_signal,
    f10urg_f10_utility_regulated_growth_revcomp_ema_126d_base_v069_signal,
    f10urg_f10_utility_regulated_growth_revcomp_ema_252d_base_v070_signal,
    f10urg_f10_utility_regulated_growth_revcomp_range_5d_base_v071_signal,
    f10urg_f10_utility_regulated_growth_revcomp_range_21d_base_v072_signal,
    f10urg_f10_utility_regulated_growth_revcomp_range_63d_base_v073_signal,
    f10urg_f10_utility_regulated_growth_revcomp_range_126d_base_v074_signal,
    f10urg_f10_utility_regulated_growth_revcomp_range_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_UTILITY_REGULATED_GROWTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_long_cycle_growth", "_f10_compounding_quality", "_f10_revenue_compound",)
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
    print(f"OK f10_utility_regulated_growth_base_001_075_claude: {n_features} features pass")
