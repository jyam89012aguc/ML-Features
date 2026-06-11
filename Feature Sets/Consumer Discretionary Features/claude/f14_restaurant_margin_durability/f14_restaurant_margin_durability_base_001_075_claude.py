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

def f14rmd_f14_restaurant_margin_durability_md_xclose_5d_base_v001_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_5d_base_v002_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_5d_base_v003_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_5d_base_v004_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_10d_base_v005_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_10d_base_v006_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_10d_base_v007_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_10d_base_v008_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_21d_base_v009_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_21d_base_v010_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_21d_base_v011_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_21d_base_v012_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_42d_base_v013_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_42d_base_v014_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_42d_base_v015_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_42d_base_v016_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_63d_base_v017_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_63d_base_v018_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_63d_base_v019_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_63d_base_v020_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_126d_base_v021_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_126d_base_v022_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_126d_base_v023_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_126d_base_v024_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_189d_base_v025_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_189d_base_v026_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_189d_base_v027_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_189d_base_v028_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_252d_base_v029_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_252d_base_v030_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_252d_base_v031_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_252d_base_v032_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_378d_base_v033_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_378d_base_v034_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_378d_base_v035_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_378d_base_v036_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_xclose_504d_base_v037_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_zclose_504d_base_v038_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_mclose_504d_base_v039_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_md_sclose_504d_base_v040_signal(ebitdamargin, closeadj):
    result = _f14_margin_durability(ebitdamargin, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_5d_base_v041_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_5d_base_v042_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_5d_base_v043_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_5d_base_v044_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_10d_base_v045_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_10d_base_v046_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_10d_base_v047_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_10d_base_v048_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_21d_base_v049_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_21d_base_v050_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_21d_base_v051_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_21d_base_v052_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_42d_base_v053_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_42d_base_v054_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_42d_base_v055_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_42d_base_v056_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_63d_base_v057_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_63d_base_v058_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_63d_base_v059_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_63d_base_v060_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_126d_base_v061_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_126d_base_v062_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_126d_base_v063_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_126d_base_v064_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_189d_base_v065_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_189d_base_v066_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_189d_base_v067_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_189d_base_v068_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_252d_base_v069_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_252d_base_v070_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_252d_base_v071_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_252d_base_v072_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_378d_base_v073_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_378d_base_v074_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_378d_base_v075_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f14rmd_f14_restaurant_margin_durability_md_xclose_5d_base_v001_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_5d_base_v002_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_5d_base_v003_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_5d_base_v004_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_10d_base_v005_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_10d_base_v006_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_10d_base_v007_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_10d_base_v008_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_21d_base_v009_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_21d_base_v010_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_21d_base_v011_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_21d_base_v012_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_42d_base_v013_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_42d_base_v014_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_42d_base_v015_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_42d_base_v016_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_63d_base_v017_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_63d_base_v018_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_63d_base_v019_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_63d_base_v020_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_126d_base_v021_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_126d_base_v022_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_126d_base_v023_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_126d_base_v024_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_189d_base_v025_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_189d_base_v026_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_189d_base_v027_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_189d_base_v028_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_252d_base_v029_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_252d_base_v030_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_252d_base_v031_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_252d_base_v032_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_378d_base_v033_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_378d_base_v034_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_378d_base_v035_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_378d_base_v036_signal,
    f14rmd_f14_restaurant_margin_durability_md_xclose_504d_base_v037_signal,
    f14rmd_f14_restaurant_margin_durability_md_zclose_504d_base_v038_signal,
    f14rmd_f14_restaurant_margin_durability_md_mclose_504d_base_v039_signal,
    f14rmd_f14_restaurant_margin_durability_md_sclose_504d_base_v040_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_5d_base_v041_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_5d_base_v042_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_5d_base_v043_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_5d_base_v044_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_10d_base_v045_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_10d_base_v046_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_10d_base_v047_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_10d_base_v048_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_21d_base_v049_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_21d_base_v050_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_21d_base_v051_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_21d_base_v052_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_42d_base_v053_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_42d_base_v054_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_42d_base_v055_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_42d_base_v056_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_63d_base_v057_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_63d_base_v058_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_63d_base_v059_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_63d_base_v060_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_126d_base_v061_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_126d_base_v062_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_126d_base_v063_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_126d_base_v064_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_189d_base_v065_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_189d_base_v066_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_189d_base_v067_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_189d_base_v068_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_252d_base_v069_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_252d_base_v070_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_252d_base_v071_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_252d_base_v072_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_378d_base_v073_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_378d_base_v074_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_378d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_RESTAURANT_MARGIN_DURABILITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f14_restaurant_margin_durability_base_001_075_claude: {n_features} features pass")
