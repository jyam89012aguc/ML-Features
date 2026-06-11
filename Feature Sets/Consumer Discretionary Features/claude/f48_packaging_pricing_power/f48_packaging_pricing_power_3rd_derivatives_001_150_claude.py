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
def _f48_gp_lift(gp, revenue, w):
    gpr = gp / revenue.replace(0, np.nan)
    return gpr - gpr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f48_pricing_pass_through(grossmargin, cor, revenue, w):
    cost_intensity = cor / revenue.replace(0, np.nan)
    cost_change = cost_intensity.diff(w)
    margin_change = grossmargin.diff(w)
    return margin_change - (-cost_change)


def _f48_packaging_durability(grossmargin, ebitdamargin, w):
    gm_floor = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    eb_floor = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    gm_mean = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    eb_mean = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (gm_floor / gm_mean.replace(0, np.nan).abs()) + (eb_floor / eb_mean.replace(0, np.nan).abs())



def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw5_jerk_v001_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean5_jerk_v002_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema5_jerk_v003_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled5_jerk_v004_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble5_jerk_v005_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw10_jerk_v006_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean10_jerk_v007_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema10_jerk_v008_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled10_jerk_v009_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble10_jerk_v010_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw21_jerk_v011_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean21_jerk_v012_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema21_jerk_v013_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled21_jerk_v014_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble21_jerk_v015_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw42_jerk_v016_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean42_jerk_v017_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema42_jerk_v018_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled42_jerk_v019_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble42_jerk_v020_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw63_jerk_v021_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean63_jerk_v022_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema63_jerk_v023_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled63_jerk_v024_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble63_jerk_v025_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw126_jerk_v026_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean126_jerk_v027_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema126_jerk_v028_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled126_jerk_v029_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble126_jerk_v030_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw5_jerk_v031_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean5_jerk_v032_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema5_jerk_v033_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled5_jerk_v034_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble5_jerk_v035_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw10_jerk_v036_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean10_jerk_v037_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema10_jerk_v038_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled10_jerk_v039_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble10_jerk_v040_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw21_jerk_v041_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean21_jerk_v042_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema21_jerk_v043_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled21_jerk_v044_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble21_jerk_v045_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw42_jerk_v046_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean42_jerk_v047_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema42_jerk_v048_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled42_jerk_v049_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble42_jerk_v050_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw63_jerk_v051_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean63_jerk_v052_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema63_jerk_v053_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled63_jerk_v054_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble63_jerk_v055_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw126_jerk_v056_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean126_jerk_v057_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema126_jerk_v058_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled126_jerk_v059_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble126_jerk_v060_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw5_jerk_v061_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean5_jerk_v062_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema5_jerk_v063_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled5_jerk_v064_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble5_jerk_v065_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw10_jerk_v066_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean10_jerk_v067_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema10_jerk_v068_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled10_jerk_v069_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble10_jerk_v070_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw21_jerk_v071_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean21_jerk_v072_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema21_jerk_v073_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled21_jerk_v074_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble21_jerk_v075_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw42_jerk_v076_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean42_jerk_v077_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema42_jerk_v078_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled42_jerk_v079_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble42_jerk_v080_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw63_jerk_v081_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean63_jerk_v082_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema63_jerk_v083_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled63_jerk_v084_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble63_jerk_v085_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw126_jerk_v086_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean126_jerk_v087_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema126_jerk_v088_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled126_jerk_v089_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble126_jerk_v090_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw5_jerk_v091_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean5_jerk_v092_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema5_jerk_v093_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled5_jerk_v094_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble5_jerk_v095_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw10_jerk_v096_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean10_jerk_v097_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema10_jerk_v098_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled10_jerk_v099_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble10_jerk_v100_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw21_jerk_v101_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean21_jerk_v102_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema21_jerk_v103_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled21_jerk_v104_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble21_jerk_v105_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw42_jerk_v106_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean42_jerk_v107_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema42_jerk_v108_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled42_jerk_v109_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble42_jerk_v110_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw63_jerk_v111_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean63_jerk_v112_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema63_jerk_v113_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled63_jerk_v114_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble63_jerk_v115_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw126_jerk_v116_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean126_jerk_v117_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema126_jerk_v118_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled126_jerk_v119_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble126_jerk_v120_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw5_jerk_v121_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean5_jerk_v122_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema5_jerk_v123_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled5_jerk_v124_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble5_jerk_v125_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw10_jerk_v126_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean10_jerk_v127_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema10_jerk_v128_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled10_jerk_v129_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble10_jerk_v130_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw21_jerk_v131_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean21_jerk_v132_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema21_jerk_v133_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled21_jerk_v134_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble21_jerk_v135_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw42_jerk_v136_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean42_jerk_v137_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema42_jerk_v138_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled42_jerk_v139_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble42_jerk_v140_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw63_jerk_v141_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean63_jerk_v142_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema63_jerk_v143_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled63_jerk_v144_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble63_jerk_v145_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw126_jerk_v146_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean126_jerk_v147_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema126_jerk_v148_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled126_jerk_v149_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble126_jerk_v150_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw5_jerk_v001_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean5_jerk_v002_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema5_jerk_v003_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled5_jerk_v004_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble5_jerk_v005_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw10_jerk_v006_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean10_jerk_v007_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema10_jerk_v008_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled10_jerk_v009_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble10_jerk_v010_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw21_jerk_v011_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean21_jerk_v012_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema21_jerk_v013_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled21_jerk_v014_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble21_jerk_v015_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw42_jerk_v016_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean42_jerk_v017_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema42_jerk_v018_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled42_jerk_v019_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble42_jerk_v020_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw63_jerk_v021_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean63_jerk_v022_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema63_jerk_v023_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled63_jerk_v024_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble63_jerk_v025_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkraw126_jerk_v026_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkmean126_jerk_v027_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkema126_jerk_v028_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkscaled126_jerk_v029_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_jerkdouble126_jerk_v030_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw5_jerk_v031_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean5_jerk_v032_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema5_jerk_v033_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled5_jerk_v034_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble5_jerk_v035_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw10_jerk_v036_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean10_jerk_v037_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema10_jerk_v038_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled10_jerk_v039_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble10_jerk_v040_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw21_jerk_v041_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean21_jerk_v042_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema21_jerk_v043_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled21_jerk_v044_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble21_jerk_v045_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw42_jerk_v046_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean42_jerk_v047_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema42_jerk_v048_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled42_jerk_v049_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble42_jerk_v050_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw63_jerk_v051_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean63_jerk_v052_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema63_jerk_v053_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled63_jerk_v054_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble63_jerk_v055_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkraw126_jerk_v056_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkmean126_jerk_v057_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkema126_jerk_v058_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkscaled126_jerk_v059_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_jerkdouble126_jerk_v060_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw5_jerk_v061_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean5_jerk_v062_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema5_jerk_v063_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled5_jerk_v064_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble5_jerk_v065_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw10_jerk_v066_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean10_jerk_v067_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema10_jerk_v068_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled10_jerk_v069_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble10_jerk_v070_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw21_jerk_v071_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean21_jerk_v072_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema21_jerk_v073_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled21_jerk_v074_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble21_jerk_v075_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw42_jerk_v076_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean42_jerk_v077_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema42_jerk_v078_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled42_jerk_v079_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble42_jerk_v080_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw63_jerk_v081_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean63_jerk_v082_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema63_jerk_v083_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled63_jerk_v084_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble63_jerk_v085_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkraw126_jerk_v086_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkmean126_jerk_v087_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkema126_jerk_v088_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkscaled126_jerk_v089_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_jerkdouble126_jerk_v090_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw5_jerk_v091_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean5_jerk_v092_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema5_jerk_v093_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled5_jerk_v094_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble5_jerk_v095_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw10_jerk_v096_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean10_jerk_v097_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema10_jerk_v098_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled10_jerk_v099_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble10_jerk_v100_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw21_jerk_v101_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean21_jerk_v102_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema21_jerk_v103_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled21_jerk_v104_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble21_jerk_v105_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw42_jerk_v106_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean42_jerk_v107_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema42_jerk_v108_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled42_jerk_v109_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble42_jerk_v110_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw63_jerk_v111_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean63_jerk_v112_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema63_jerk_v113_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled63_jerk_v114_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble63_jerk_v115_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkraw126_jerk_v116_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkmean126_jerk_v117_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkema126_jerk_v118_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkscaled126_jerk_v119_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_jerkdouble126_jerk_v120_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw5_jerk_v121_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean5_jerk_v122_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema5_jerk_v123_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled5_jerk_v124_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble5_jerk_v125_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw10_jerk_v126_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean10_jerk_v127_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema10_jerk_v128_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled10_jerk_v129_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble10_jerk_v130_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw21_jerk_v131_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean21_jerk_v132_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema21_jerk_v133_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled21_jerk_v134_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble21_jerk_v135_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw42_jerk_v136_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean42_jerk_v137_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema42_jerk_v138_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled42_jerk_v139_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble42_jerk_v140_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw63_jerk_v141_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean63_jerk_v142_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema63_jerk_v143_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled63_jerk_v144_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble63_jerk_v145_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkraw126_jerk_v146_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkmean126_jerk_v147_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkema126_jerk_v148_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkscaled126_jerk_v149_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_jerkdouble126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_PACKAGING_PRICING_POWER_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")

    cols = {"closeadj": closeadj, "gp": gp, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_gp_lift", "_f48_pricing_pass_through", "_f48_packaging_durability")
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
    print(f"OK f48_packaging_pricing_power_3rd_derivatives_001_150_claude: {n_features} features pass")
