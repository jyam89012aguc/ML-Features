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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)



# ===== folder domain primitives =====
def _f47_revenue_floor(revenue, w):
    return revenue.rolling(w, min_periods=max(1, w // 2)).min() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f47_non_cyclical_share(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    mx = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return mn / mx.replace(0, np.nan)


def _f47_durability_score(revenue, ebitdamargin, w):
    floor = revenue.rolling(w, min_periods=max(1, w // 2)).min() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    mstable = 1.0 - ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().fillna(0) / ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()
    return floor * mstable



def f47hid_f47_home_improvement_durability_floor_21d_jerkraw5_jerk_v001_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkmean5_jerk_v002_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkema5_jerk_v003_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkscaled5_jerk_v004_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkdouble5_jerk_v005_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkraw10_jerk_v006_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkmean10_jerk_v007_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkema10_jerk_v008_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkscaled10_jerk_v009_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkdouble10_jerk_v010_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkraw21_jerk_v011_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkmean21_jerk_v012_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkema21_jerk_v013_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkscaled21_jerk_v014_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkdouble21_jerk_v015_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkraw42_jerk_v016_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkmean42_jerk_v017_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkema42_jerk_v018_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkscaled42_jerk_v019_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkdouble42_jerk_v020_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkraw63_jerk_v021_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkmean63_jerk_v022_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkema63_jerk_v023_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkscaled63_jerk_v024_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkdouble63_jerk_v025_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkraw126_jerk_v026_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkmean126_jerk_v027_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkema126_jerk_v028_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkscaled126_jerk_v029_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_jerkdouble126_jerk_v030_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkraw5_jerk_v031_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkmean5_jerk_v032_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkema5_jerk_v033_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkscaled5_jerk_v034_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkdouble5_jerk_v035_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkraw10_jerk_v036_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkmean10_jerk_v037_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkema10_jerk_v038_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkscaled10_jerk_v039_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkdouble10_jerk_v040_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkraw21_jerk_v041_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkmean21_jerk_v042_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkema21_jerk_v043_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkscaled21_jerk_v044_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkdouble21_jerk_v045_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkraw42_jerk_v046_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkmean42_jerk_v047_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkema42_jerk_v048_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkscaled42_jerk_v049_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkdouble42_jerk_v050_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkraw63_jerk_v051_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkmean63_jerk_v052_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkema63_jerk_v053_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkscaled63_jerk_v054_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkdouble63_jerk_v055_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkraw126_jerk_v056_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkmean126_jerk_v057_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkema126_jerk_v058_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkscaled126_jerk_v059_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_jerkdouble126_jerk_v060_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkraw5_jerk_v061_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkmean5_jerk_v062_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkema5_jerk_v063_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkscaled5_jerk_v064_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkdouble5_jerk_v065_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkraw10_jerk_v066_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkmean10_jerk_v067_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkema10_jerk_v068_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkscaled10_jerk_v069_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkdouble10_jerk_v070_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkraw21_jerk_v071_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkmean21_jerk_v072_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkema21_jerk_v073_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkscaled21_jerk_v074_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkdouble21_jerk_v075_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkraw42_jerk_v076_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkmean42_jerk_v077_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkema42_jerk_v078_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkscaled42_jerk_v079_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkdouble42_jerk_v080_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkraw63_jerk_v081_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkmean63_jerk_v082_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkema63_jerk_v083_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkscaled63_jerk_v084_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkdouble63_jerk_v085_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkraw126_jerk_v086_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkmean126_jerk_v087_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkema126_jerk_v088_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkscaled126_jerk_v089_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_jerkdouble126_jerk_v090_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkraw5_jerk_v091_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkmean5_jerk_v092_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkema5_jerk_v093_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkscaled5_jerk_v094_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkdouble5_jerk_v095_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkraw10_jerk_v096_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkmean10_jerk_v097_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkema10_jerk_v098_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkscaled10_jerk_v099_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkdouble10_jerk_v100_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkraw21_jerk_v101_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkmean21_jerk_v102_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkema21_jerk_v103_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkscaled21_jerk_v104_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkdouble21_jerk_v105_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkraw42_jerk_v106_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkmean42_jerk_v107_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkema42_jerk_v108_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkscaled42_jerk_v109_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkdouble42_jerk_v110_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkraw63_jerk_v111_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkmean63_jerk_v112_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkema63_jerk_v113_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkscaled63_jerk_v114_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkdouble63_jerk_v115_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkraw126_jerk_v116_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkmean126_jerk_v117_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkema126_jerk_v118_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkscaled126_jerk_v119_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_jerkdouble126_jerk_v120_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkraw5_jerk_v121_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkmean5_jerk_v122_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkema5_jerk_v123_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkscaled5_jerk_v124_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkdouble5_jerk_v125_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkraw10_jerk_v126_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkmean10_jerk_v127_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkema10_jerk_v128_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkscaled10_jerk_v129_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkdouble10_jerk_v130_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkraw21_jerk_v131_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkmean21_jerk_v132_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkema21_jerk_v133_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkscaled21_jerk_v134_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkdouble21_jerk_v135_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkraw42_jerk_v136_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkmean42_jerk_v137_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkema42_jerk_v138_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkscaled42_jerk_v139_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkdouble42_jerk_v140_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkraw63_jerk_v141_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkmean63_jerk_v142_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkema63_jerk_v143_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkscaled63_jerk_v144_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkdouble63_jerk_v145_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkraw126_jerk_v146_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkmean126_jerk_v147_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkema126_jerk_v148_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkscaled126_jerk_v149_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_jerkdouble126_jerk_v150_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hid_f47_home_improvement_durability_floor_21d_jerkraw5_jerk_v001_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkmean5_jerk_v002_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkema5_jerk_v003_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkscaled5_jerk_v004_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkdouble5_jerk_v005_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkraw10_jerk_v006_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkmean10_jerk_v007_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkema10_jerk_v008_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkscaled10_jerk_v009_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkdouble10_jerk_v010_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkraw21_jerk_v011_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkmean21_jerk_v012_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkema21_jerk_v013_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkscaled21_jerk_v014_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkdouble21_jerk_v015_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkraw42_jerk_v016_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkmean42_jerk_v017_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkema42_jerk_v018_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkscaled42_jerk_v019_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkdouble42_jerk_v020_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkraw63_jerk_v021_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkmean63_jerk_v022_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkema63_jerk_v023_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkscaled63_jerk_v024_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkdouble63_jerk_v025_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkraw126_jerk_v026_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkmean126_jerk_v027_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkema126_jerk_v028_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkscaled126_jerk_v029_signal,
    f47hid_f47_home_improvement_durability_floor_21d_jerkdouble126_jerk_v030_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkraw5_jerk_v031_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkmean5_jerk_v032_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkema5_jerk_v033_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkscaled5_jerk_v034_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkdouble5_jerk_v035_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkraw10_jerk_v036_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkmean10_jerk_v037_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkema10_jerk_v038_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkscaled10_jerk_v039_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkdouble10_jerk_v040_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkraw21_jerk_v041_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkmean21_jerk_v042_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkema21_jerk_v043_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkscaled21_jerk_v044_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkdouble21_jerk_v045_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkraw42_jerk_v046_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkmean42_jerk_v047_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkema42_jerk_v048_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkscaled42_jerk_v049_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkdouble42_jerk_v050_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkraw63_jerk_v051_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkmean63_jerk_v052_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkema63_jerk_v053_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkscaled63_jerk_v054_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkdouble63_jerk_v055_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkraw126_jerk_v056_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkmean126_jerk_v057_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkema126_jerk_v058_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkscaled126_jerk_v059_signal,
    f47hid_f47_home_improvement_durability_floor_63d_jerkdouble126_jerk_v060_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkraw5_jerk_v061_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkmean5_jerk_v062_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkema5_jerk_v063_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkscaled5_jerk_v064_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkdouble5_jerk_v065_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkraw10_jerk_v066_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkmean10_jerk_v067_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkema10_jerk_v068_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkscaled10_jerk_v069_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkdouble10_jerk_v070_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkraw21_jerk_v071_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkmean21_jerk_v072_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkema21_jerk_v073_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkscaled21_jerk_v074_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkdouble21_jerk_v075_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkraw42_jerk_v076_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkmean42_jerk_v077_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkema42_jerk_v078_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkscaled42_jerk_v079_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkdouble42_jerk_v080_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkraw63_jerk_v081_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkmean63_jerk_v082_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkema63_jerk_v083_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkscaled63_jerk_v084_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkdouble63_jerk_v085_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkraw126_jerk_v086_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkmean126_jerk_v087_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkema126_jerk_v088_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkscaled126_jerk_v089_signal,
    f47hid_f47_home_improvement_durability_floor_126d_jerkdouble126_jerk_v090_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkraw5_jerk_v091_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkmean5_jerk_v092_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkema5_jerk_v093_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkscaled5_jerk_v094_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkdouble5_jerk_v095_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkraw10_jerk_v096_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkmean10_jerk_v097_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkema10_jerk_v098_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkscaled10_jerk_v099_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkdouble10_jerk_v100_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkraw21_jerk_v101_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkmean21_jerk_v102_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkema21_jerk_v103_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkscaled21_jerk_v104_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkdouble21_jerk_v105_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkraw42_jerk_v106_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkmean42_jerk_v107_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkema42_jerk_v108_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkscaled42_jerk_v109_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkdouble42_jerk_v110_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkraw63_jerk_v111_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkmean63_jerk_v112_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkema63_jerk_v113_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkscaled63_jerk_v114_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkdouble63_jerk_v115_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkraw126_jerk_v116_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkmean126_jerk_v117_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkema126_jerk_v118_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkscaled126_jerk_v119_signal,
    f47hid_f47_home_improvement_durability_floor_252d_jerkdouble126_jerk_v120_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkraw5_jerk_v121_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkmean5_jerk_v122_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkema5_jerk_v123_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkscaled5_jerk_v124_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkdouble5_jerk_v125_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkraw10_jerk_v126_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkmean10_jerk_v127_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkema10_jerk_v128_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkscaled10_jerk_v129_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkdouble10_jerk_v130_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkraw21_jerk_v131_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkmean21_jerk_v132_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkema21_jerk_v133_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkscaled21_jerk_v134_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkdouble21_jerk_v135_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkraw42_jerk_v136_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkmean42_jerk_v137_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkema42_jerk_v138_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkscaled42_jerk_v139_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkdouble42_jerk_v140_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkraw63_jerk_v141_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkmean63_jerk_v142_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkema63_jerk_v143_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkscaled63_jerk_v144_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkdouble63_jerk_v145_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkraw126_jerk_v146_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkmean126_jerk_v147_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkema126_jerk_v148_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkscaled126_jerk_v149_signal,
    f47hid_f47_home_improvement_durability_floor_504d_jerkdouble126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HOME_IMPROVEMENT_DURABILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_revenue_floor", "_f47_non_cyclical_share", "_f47_durability_score")
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
    print(f"OK f47_home_improvement_durability_3rd_derivatives_001_150_claude: {n_features} features pass")
