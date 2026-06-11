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
def _f50_quality_composite(roic, fcf, revenue, w):
    fcf_yield = fcf / revenue.replace(0, np.nan)
    return roic.rolling(w, min_periods=max(1, w // 2)).mean() + fcf_yield.rolling(w, min_periods=max(1, w // 2)).mean()


def _f50_low_vol_high_growth(closeadj, revenue, w):
    vol = closeadj.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    growth = revenue.pct_change(w)
    return growth / vol.replace(0, np.nan)


def _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, w):
    return (roic.rolling(w, min_periods=max(1, w // 2)).mean()
            + ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
            + (fcf / fcf.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)) - 1.0)



def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw5_jerk_v001_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean5_jerk_v002_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema5_jerk_v003_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled5_jerk_v004_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble5_jerk_v005_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw10_jerk_v006_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean10_jerk_v007_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema10_jerk_v008_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled10_jerk_v009_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble10_jerk_v010_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw21_jerk_v011_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean21_jerk_v012_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema21_jerk_v013_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled21_jerk_v014_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble21_jerk_v015_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw42_jerk_v016_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean42_jerk_v017_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema42_jerk_v018_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled42_jerk_v019_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble42_jerk_v020_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw63_jerk_v021_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean63_jerk_v022_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema63_jerk_v023_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled63_jerk_v024_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble63_jerk_v025_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw126_jerk_v026_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean126_jerk_v027_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema126_jerk_v028_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled126_jerk_v029_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble126_jerk_v030_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw5_jerk_v031_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean5_jerk_v032_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema5_jerk_v033_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled5_jerk_v034_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble5_jerk_v035_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw10_jerk_v036_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean10_jerk_v037_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema10_jerk_v038_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled10_jerk_v039_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble10_jerk_v040_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw21_jerk_v041_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean21_jerk_v042_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema21_jerk_v043_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled21_jerk_v044_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble21_jerk_v045_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw42_jerk_v046_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean42_jerk_v047_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema42_jerk_v048_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled42_jerk_v049_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble42_jerk_v050_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw63_jerk_v051_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean63_jerk_v052_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema63_jerk_v053_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled63_jerk_v054_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble63_jerk_v055_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw126_jerk_v056_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean126_jerk_v057_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema126_jerk_v058_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled126_jerk_v059_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble126_jerk_v060_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw5_jerk_v061_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean5_jerk_v062_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema5_jerk_v063_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled5_jerk_v064_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble5_jerk_v065_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw10_jerk_v066_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean10_jerk_v067_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema10_jerk_v068_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled10_jerk_v069_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble10_jerk_v070_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw21_jerk_v071_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean21_jerk_v072_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema21_jerk_v073_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled21_jerk_v074_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble21_jerk_v075_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw42_jerk_v076_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean42_jerk_v077_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema42_jerk_v078_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled42_jerk_v079_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble42_jerk_v080_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw63_jerk_v081_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean63_jerk_v082_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema63_jerk_v083_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled63_jerk_v084_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble63_jerk_v085_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw126_jerk_v086_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean126_jerk_v087_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema126_jerk_v088_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled126_jerk_v089_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble126_jerk_v090_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw5_jerk_v091_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean5_jerk_v092_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema5_jerk_v093_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled5_jerk_v094_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble5_jerk_v095_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw10_jerk_v096_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean10_jerk_v097_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema10_jerk_v098_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled10_jerk_v099_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble10_jerk_v100_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw21_jerk_v101_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean21_jerk_v102_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema21_jerk_v103_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled21_jerk_v104_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble21_jerk_v105_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw42_jerk_v106_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean42_jerk_v107_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema42_jerk_v108_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled42_jerk_v109_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble42_jerk_v110_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw63_jerk_v111_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean63_jerk_v112_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema63_jerk_v113_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled63_jerk_v114_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble63_jerk_v115_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw126_jerk_v116_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean126_jerk_v117_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema126_jerk_v118_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled126_jerk_v119_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble126_jerk_v120_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw5_jerk_v121_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean5_jerk_v122_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema5_jerk_v123_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled5_jerk_v124_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 5) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble5_jerk_v125_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 5).diff(5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw10_jerk_v126_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean10_jerk_v127_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema10_jerk_v128_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled10_jerk_v129_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 10) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble10_jerk_v130_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 10).diff(10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw21_jerk_v131_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean21_jerk_v132_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema21_jerk_v133_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled21_jerk_v134_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 21) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble21_jerk_v135_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 21).diff(21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw42_jerk_v136_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean42_jerk_v137_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema42_jerk_v138_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled42_jerk_v139_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 42) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble42_jerk_v140_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 42).diff(42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw63_jerk_v141_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean63_jerk_v142_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema63_jerk_v143_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled63_jerk_v144_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 63) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble63_jerk_v145_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 63).diff(63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw126_jerk_v146_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean126_jerk_v147_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema126_jerk_v148_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled126_jerk_v149_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 126) * 100.0
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble126_jerk_v150_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _jerk(base, 126).diff(126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw5_jerk_v001_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean5_jerk_v002_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema5_jerk_v003_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled5_jerk_v004_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble5_jerk_v005_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw10_jerk_v006_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean10_jerk_v007_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema10_jerk_v008_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled10_jerk_v009_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble10_jerk_v010_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw21_jerk_v011_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean21_jerk_v012_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema21_jerk_v013_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled21_jerk_v014_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble21_jerk_v015_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw42_jerk_v016_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean42_jerk_v017_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema42_jerk_v018_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled42_jerk_v019_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble42_jerk_v020_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw63_jerk_v021_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean63_jerk_v022_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema63_jerk_v023_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled63_jerk_v024_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble63_jerk_v025_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkraw126_jerk_v026_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkmean126_jerk_v027_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkema126_jerk_v028_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkscaled126_jerk_v029_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_jerkdouble126_jerk_v030_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw5_jerk_v031_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean5_jerk_v032_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema5_jerk_v033_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled5_jerk_v034_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble5_jerk_v035_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw10_jerk_v036_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean10_jerk_v037_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema10_jerk_v038_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled10_jerk_v039_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble10_jerk_v040_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw21_jerk_v041_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean21_jerk_v042_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema21_jerk_v043_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled21_jerk_v044_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble21_jerk_v045_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw42_jerk_v046_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean42_jerk_v047_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema42_jerk_v048_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled42_jerk_v049_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble42_jerk_v050_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw63_jerk_v051_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean63_jerk_v052_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema63_jerk_v053_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled63_jerk_v054_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble63_jerk_v055_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkraw126_jerk_v056_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkmean126_jerk_v057_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkema126_jerk_v058_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkscaled126_jerk_v059_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_jerkdouble126_jerk_v060_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw5_jerk_v061_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean5_jerk_v062_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema5_jerk_v063_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled5_jerk_v064_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble5_jerk_v065_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw10_jerk_v066_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean10_jerk_v067_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema10_jerk_v068_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled10_jerk_v069_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble10_jerk_v070_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw21_jerk_v071_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean21_jerk_v072_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema21_jerk_v073_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled21_jerk_v074_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble21_jerk_v075_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw42_jerk_v076_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean42_jerk_v077_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema42_jerk_v078_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled42_jerk_v079_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble42_jerk_v080_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw63_jerk_v081_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean63_jerk_v082_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema63_jerk_v083_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled63_jerk_v084_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble63_jerk_v085_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkraw126_jerk_v086_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkmean126_jerk_v087_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkema126_jerk_v088_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkscaled126_jerk_v089_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_jerkdouble126_jerk_v090_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw5_jerk_v091_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean5_jerk_v092_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema5_jerk_v093_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled5_jerk_v094_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble5_jerk_v095_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw10_jerk_v096_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean10_jerk_v097_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema10_jerk_v098_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled10_jerk_v099_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble10_jerk_v100_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw21_jerk_v101_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean21_jerk_v102_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema21_jerk_v103_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled21_jerk_v104_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble21_jerk_v105_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw42_jerk_v106_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean42_jerk_v107_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema42_jerk_v108_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled42_jerk_v109_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble42_jerk_v110_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw63_jerk_v111_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean63_jerk_v112_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema63_jerk_v113_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled63_jerk_v114_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble63_jerk_v115_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkraw126_jerk_v116_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkmean126_jerk_v117_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkema126_jerk_v118_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkscaled126_jerk_v119_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_jerkdouble126_jerk_v120_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw5_jerk_v121_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean5_jerk_v122_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema5_jerk_v123_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled5_jerk_v124_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble5_jerk_v125_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw10_jerk_v126_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean10_jerk_v127_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema10_jerk_v128_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled10_jerk_v129_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble10_jerk_v130_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw21_jerk_v131_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean21_jerk_v132_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema21_jerk_v133_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled21_jerk_v134_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble21_jerk_v135_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw42_jerk_v136_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean42_jerk_v137_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema42_jerk_v138_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled42_jerk_v139_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble42_jerk_v140_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw63_jerk_v141_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean63_jerk_v142_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema63_jerk_v143_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled63_jerk_v144_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble63_jerk_v145_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkraw126_jerk_v146_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkmean126_jerk_v147_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkema126_jerk_v148_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkscaled126_jerk_v149_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_jerkdouble126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_CD_IDIOSYNCRATIC_ALPHA_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")

    cols = {"closeadj": closeadj, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_low_vol_high_growth", "_f50_idiosyncratic_alpha_score")
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
    print(f"OK f50_cd_idiosyncratic_alpha_3rd_derivatives_001_150_claude: {n_features} features pass")
