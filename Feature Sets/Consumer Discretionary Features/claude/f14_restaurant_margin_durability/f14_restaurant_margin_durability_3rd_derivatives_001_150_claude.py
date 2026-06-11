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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


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

def _f14_margin_durability(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f14_margin_growth_stability(ebitdamargin, revenue, w):
    rg = revenue.pct_change(periods=w)
    msd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return rg / msd.replace(0, np.nan)


def _f14_durability_score(ebitdamargin, grossmargin, w):
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    esd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    gsd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (em + gm) / (esd + gsd).replace(0, np.nan)


# ===== features =====

def f14rmd_f14_restaurant_margin_durability_md_w5_5d_jerk_v001_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w5_10d_jerk_v002_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w5_21d_jerk_v003_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w5_42d_jerk_v004_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w5_63d_jerk_v005_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w10_5d_jerk_v006_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w10_10d_jerk_v007_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w10_21d_jerk_v008_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w10_42d_jerk_v009_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w10_63d_jerk_v010_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w21_5d_jerk_v011_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w21_10d_jerk_v012_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w21_21d_jerk_v013_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w21_42d_jerk_v014_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w21_63d_jerk_v015_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w42_5d_jerk_v016_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w42_10d_jerk_v017_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w42_21d_jerk_v018_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w42_42d_jerk_v019_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w42_63d_jerk_v020_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w63_5d_jerk_v021_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w63_10d_jerk_v022_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w63_21d_jerk_v023_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w63_42d_jerk_v024_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w63_63d_jerk_v025_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w126_5d_jerk_v026_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w126_10d_jerk_v027_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w126_21d_jerk_v028_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w126_42d_jerk_v029_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w126_63d_jerk_v030_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w189_5d_jerk_v031_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w189_10d_jerk_v032_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w189_21d_jerk_v033_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w189_42d_jerk_v034_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w189_63d_jerk_v035_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w252_5d_jerk_v036_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w252_10d_jerk_v037_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w252_21d_jerk_v038_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w252_42d_jerk_v039_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w252_63d_jerk_v040_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w378_5d_jerk_v041_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w378_10d_jerk_v042_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w378_21d_jerk_v043_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w378_42d_jerk_v044_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w378_63d_jerk_v045_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w504_5d_jerk_v046_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w504_10d_jerk_v047_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w504_21d_jerk_v048_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w504_42d_jerk_v049_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_w504_63d_jerk_v050_signal(ebitdamargin, closeadj):
    result = _jerk(_f14_margin_durability(ebitdamargin, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w5_5d_jerk_v051_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w5_10d_jerk_v052_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w5_21d_jerk_v053_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w5_42d_jerk_v054_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w5_63d_jerk_v055_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w10_5d_jerk_v056_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w10_10d_jerk_v057_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w10_21d_jerk_v058_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w10_42d_jerk_v059_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w10_63d_jerk_v060_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w21_5d_jerk_v061_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w21_10d_jerk_v062_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w21_21d_jerk_v063_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w21_42d_jerk_v064_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w21_63d_jerk_v065_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w42_5d_jerk_v066_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w42_10d_jerk_v067_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w42_21d_jerk_v068_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w42_42d_jerk_v069_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w42_63d_jerk_v070_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w63_5d_jerk_v071_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w63_10d_jerk_v072_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w63_21d_jerk_v073_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w63_42d_jerk_v074_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w63_63d_jerk_v075_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w126_5d_jerk_v076_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w126_10d_jerk_v077_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w126_21d_jerk_v078_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w126_42d_jerk_v079_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w126_63d_jerk_v080_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w189_5d_jerk_v081_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w189_10d_jerk_v082_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w189_21d_jerk_v083_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w189_42d_jerk_v084_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w189_63d_jerk_v085_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w252_5d_jerk_v086_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w252_10d_jerk_v087_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w252_21d_jerk_v088_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w252_42d_jerk_v089_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w252_63d_jerk_v090_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w378_5d_jerk_v091_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w378_10d_jerk_v092_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w378_21d_jerk_v093_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w378_42d_jerk_v094_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w378_63d_jerk_v095_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w504_5d_jerk_v096_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w504_10d_jerk_v097_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w504_21d_jerk_v098_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w504_42d_jerk_v099_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_w504_63d_jerk_v100_signal(ebitdamargin, revenue, closeadj):
    result = _jerk(_f14_margin_growth_stability(ebitdamargin, revenue, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w5_5d_jerk_v101_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w5_10d_jerk_v102_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w5_21d_jerk_v103_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w5_42d_jerk_v104_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w5_63d_jerk_v105_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w10_5d_jerk_v106_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w10_10d_jerk_v107_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w10_21d_jerk_v108_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w10_42d_jerk_v109_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w10_63d_jerk_v110_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w21_5d_jerk_v111_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w21_10d_jerk_v112_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w21_21d_jerk_v113_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w21_42d_jerk_v114_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w21_63d_jerk_v115_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w42_5d_jerk_v116_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w42_10d_jerk_v117_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w42_21d_jerk_v118_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w42_42d_jerk_v119_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w42_63d_jerk_v120_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w63_5d_jerk_v121_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w63_10d_jerk_v122_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w63_21d_jerk_v123_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w63_42d_jerk_v124_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w63_63d_jerk_v125_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w126_5d_jerk_v126_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w126_10d_jerk_v127_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w126_21d_jerk_v128_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w126_42d_jerk_v129_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w126_63d_jerk_v130_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w189_5d_jerk_v131_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w189_10d_jerk_v132_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w189_21d_jerk_v133_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w189_42d_jerk_v134_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w189_63d_jerk_v135_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w252_5d_jerk_v136_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w252_10d_jerk_v137_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w252_21d_jerk_v138_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w252_42d_jerk_v139_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w252_63d_jerk_v140_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w378_5d_jerk_v141_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w378_10d_jerk_v142_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w378_21d_jerk_v143_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w378_42d_jerk_v144_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w378_63d_jerk_v145_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w504_5d_jerk_v146_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w504_10d_jerk_v147_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w504_21d_jerk_v148_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w504_42d_jerk_v149_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_w504_63d_jerk_v150_signal(ebitdamargin, grossmargin, closeadj):
    result = _jerk(_f14_durability_score(ebitdamargin, grossmargin, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f14rmd_f14_restaurant_margin_durability_md_w5_5d_jerk_v001_signal,
    f14rmd_f14_restaurant_margin_durability_md_w5_10d_jerk_v002_signal,
    f14rmd_f14_restaurant_margin_durability_md_w5_21d_jerk_v003_signal,
    f14rmd_f14_restaurant_margin_durability_md_w5_42d_jerk_v004_signal,
    f14rmd_f14_restaurant_margin_durability_md_w5_63d_jerk_v005_signal,
    f14rmd_f14_restaurant_margin_durability_md_w10_5d_jerk_v006_signal,
    f14rmd_f14_restaurant_margin_durability_md_w10_10d_jerk_v007_signal,
    f14rmd_f14_restaurant_margin_durability_md_w10_21d_jerk_v008_signal,
    f14rmd_f14_restaurant_margin_durability_md_w10_42d_jerk_v009_signal,
    f14rmd_f14_restaurant_margin_durability_md_w10_63d_jerk_v010_signal,
    f14rmd_f14_restaurant_margin_durability_md_w21_5d_jerk_v011_signal,
    f14rmd_f14_restaurant_margin_durability_md_w21_10d_jerk_v012_signal,
    f14rmd_f14_restaurant_margin_durability_md_w21_21d_jerk_v013_signal,
    f14rmd_f14_restaurant_margin_durability_md_w21_42d_jerk_v014_signal,
    f14rmd_f14_restaurant_margin_durability_md_w21_63d_jerk_v015_signal,
    f14rmd_f14_restaurant_margin_durability_md_w42_5d_jerk_v016_signal,
    f14rmd_f14_restaurant_margin_durability_md_w42_10d_jerk_v017_signal,
    f14rmd_f14_restaurant_margin_durability_md_w42_21d_jerk_v018_signal,
    f14rmd_f14_restaurant_margin_durability_md_w42_42d_jerk_v019_signal,
    f14rmd_f14_restaurant_margin_durability_md_w42_63d_jerk_v020_signal,
    f14rmd_f14_restaurant_margin_durability_md_w63_5d_jerk_v021_signal,
    f14rmd_f14_restaurant_margin_durability_md_w63_10d_jerk_v022_signal,
    f14rmd_f14_restaurant_margin_durability_md_w63_21d_jerk_v023_signal,
    f14rmd_f14_restaurant_margin_durability_md_w63_42d_jerk_v024_signal,
    f14rmd_f14_restaurant_margin_durability_md_w63_63d_jerk_v025_signal,
    f14rmd_f14_restaurant_margin_durability_md_w126_5d_jerk_v026_signal,
    f14rmd_f14_restaurant_margin_durability_md_w126_10d_jerk_v027_signal,
    f14rmd_f14_restaurant_margin_durability_md_w126_21d_jerk_v028_signal,
    f14rmd_f14_restaurant_margin_durability_md_w126_42d_jerk_v029_signal,
    f14rmd_f14_restaurant_margin_durability_md_w126_63d_jerk_v030_signal,
    f14rmd_f14_restaurant_margin_durability_md_w189_5d_jerk_v031_signal,
    f14rmd_f14_restaurant_margin_durability_md_w189_10d_jerk_v032_signal,
    f14rmd_f14_restaurant_margin_durability_md_w189_21d_jerk_v033_signal,
    f14rmd_f14_restaurant_margin_durability_md_w189_42d_jerk_v034_signal,
    f14rmd_f14_restaurant_margin_durability_md_w189_63d_jerk_v035_signal,
    f14rmd_f14_restaurant_margin_durability_md_w252_5d_jerk_v036_signal,
    f14rmd_f14_restaurant_margin_durability_md_w252_10d_jerk_v037_signal,
    f14rmd_f14_restaurant_margin_durability_md_w252_21d_jerk_v038_signal,
    f14rmd_f14_restaurant_margin_durability_md_w252_42d_jerk_v039_signal,
    f14rmd_f14_restaurant_margin_durability_md_w252_63d_jerk_v040_signal,
    f14rmd_f14_restaurant_margin_durability_md_w378_5d_jerk_v041_signal,
    f14rmd_f14_restaurant_margin_durability_md_w378_10d_jerk_v042_signal,
    f14rmd_f14_restaurant_margin_durability_md_w378_21d_jerk_v043_signal,
    f14rmd_f14_restaurant_margin_durability_md_w378_42d_jerk_v044_signal,
    f14rmd_f14_restaurant_margin_durability_md_w378_63d_jerk_v045_signal,
    f14rmd_f14_restaurant_margin_durability_md_w504_5d_jerk_v046_signal,
    f14rmd_f14_restaurant_margin_durability_md_w504_10d_jerk_v047_signal,
    f14rmd_f14_restaurant_margin_durability_md_w504_21d_jerk_v048_signal,
    f14rmd_f14_restaurant_margin_durability_md_w504_42d_jerk_v049_signal,
    f14rmd_f14_restaurant_margin_durability_md_w504_63d_jerk_v050_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w5_5d_jerk_v051_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w5_10d_jerk_v052_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w5_21d_jerk_v053_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w5_42d_jerk_v054_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w5_63d_jerk_v055_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w10_5d_jerk_v056_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w10_10d_jerk_v057_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w10_21d_jerk_v058_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w10_42d_jerk_v059_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w10_63d_jerk_v060_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w21_5d_jerk_v061_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w21_10d_jerk_v062_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w21_21d_jerk_v063_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w21_42d_jerk_v064_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w21_63d_jerk_v065_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w42_5d_jerk_v066_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w42_10d_jerk_v067_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w42_21d_jerk_v068_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w42_42d_jerk_v069_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w42_63d_jerk_v070_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w63_5d_jerk_v071_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w63_10d_jerk_v072_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w63_21d_jerk_v073_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w63_42d_jerk_v074_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w63_63d_jerk_v075_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w126_5d_jerk_v076_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w126_10d_jerk_v077_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w126_21d_jerk_v078_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w126_42d_jerk_v079_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w126_63d_jerk_v080_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w189_5d_jerk_v081_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w189_10d_jerk_v082_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w189_21d_jerk_v083_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w189_42d_jerk_v084_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w189_63d_jerk_v085_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w252_5d_jerk_v086_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w252_10d_jerk_v087_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w252_21d_jerk_v088_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w252_42d_jerk_v089_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w252_63d_jerk_v090_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w378_5d_jerk_v091_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w378_10d_jerk_v092_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w378_21d_jerk_v093_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w378_42d_jerk_v094_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w378_63d_jerk_v095_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w504_5d_jerk_v096_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w504_10d_jerk_v097_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w504_21d_jerk_v098_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w504_42d_jerk_v099_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_w504_63d_jerk_v100_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w5_5d_jerk_v101_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w5_10d_jerk_v102_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w5_21d_jerk_v103_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w5_42d_jerk_v104_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w5_63d_jerk_v105_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w10_5d_jerk_v106_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w10_10d_jerk_v107_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w10_21d_jerk_v108_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w10_42d_jerk_v109_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w10_63d_jerk_v110_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w21_5d_jerk_v111_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w21_10d_jerk_v112_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w21_21d_jerk_v113_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w21_42d_jerk_v114_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w21_63d_jerk_v115_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w42_5d_jerk_v116_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w42_10d_jerk_v117_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w42_21d_jerk_v118_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w42_42d_jerk_v119_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w42_63d_jerk_v120_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w63_5d_jerk_v121_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w63_10d_jerk_v122_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w63_21d_jerk_v123_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w63_42d_jerk_v124_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w63_63d_jerk_v125_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w126_5d_jerk_v126_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w126_10d_jerk_v127_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w126_21d_jerk_v128_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w126_42d_jerk_v129_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w126_63d_jerk_v130_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w189_5d_jerk_v131_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w189_10d_jerk_v132_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w189_21d_jerk_v133_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w189_42d_jerk_v134_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w189_63d_jerk_v135_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w252_5d_jerk_v136_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w252_10d_jerk_v137_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w252_21d_jerk_v138_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w252_42d_jerk_v139_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w252_63d_jerk_v140_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w378_5d_jerk_v141_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w378_10d_jerk_v142_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w378_21d_jerk_v143_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w378_42d_jerk_v144_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w378_63d_jerk_v145_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w504_5d_jerk_v146_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w504_10d_jerk_v147_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w504_21d_jerk_v148_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w504_42d_jerk_v149_signal,
    f14rmd_f14_restaurant_margin_durability_ds_w504_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_RESTAURANT_MARGIN_DURABILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex,
        "assets": assets, "ppnenet": ppnenet,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f14_margin_durability", "_f14_margin_growth_stability", "_f14_durability_score")
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
    print(f"OK f14_restaurant_margin_durability_3rd_derivatives_001_150_claude: {n_features} features pass")
