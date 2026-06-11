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
def _f21_revenue_sensitivity(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f21_commodity_leverage(revenue, ebitdamargin, w):
    rev_chg = revenue.pct_change(periods=w)
    mar_chg = ebitdamargin.diff(periods=w)
    return rev_chg * (1.0 + mar_chg)


def _f21_price_leverage_score(revenue, w):
    z = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).mean()) /         revenue.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return z * revenue.pct_change(periods=max(1, w // 4))


def f21upl_f21_uranium_price_leverage_revsens_5d_base_v001_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v002_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v003_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v004_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v005_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v006_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v007_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_5d_base_v008_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 5) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v009_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v010_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v011_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v012_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v013_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v014_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v015_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_10d_base_v016_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 10) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v017_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v018_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v019_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v020_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v021_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v022_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v023_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_21d_base_v024_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v025_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v026_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v027_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v028_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v029_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v030_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v031_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_42d_base_v032_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 42) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v033_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v034_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v035_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v036_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v037_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v038_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v039_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_63d_base_v040_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 63) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v041_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v042_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v043_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v044_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v045_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v046_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v047_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_126d_base_v048_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 126) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v049_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v050_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v051_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v052_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v053_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v054_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v055_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_189d_base_v056_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 189) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v057_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v058_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v059_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v060_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v061_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v062_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v063_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_252d_base_v064_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 252) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v065_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v066_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v067_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v068_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v069_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v070_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v071_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_378d_base_v072_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 378) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v073_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v074_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v075_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v001_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v002_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v003_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v004_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v005_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v006_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v007_signal,
    f21upl_f21_uranium_price_leverage_revsens_5d_base_v008_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v009_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v010_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v011_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v012_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v013_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v014_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v015_signal,
    f21upl_f21_uranium_price_leverage_revsens_10d_base_v016_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v017_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v018_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v019_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v020_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v021_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v022_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v023_signal,
    f21upl_f21_uranium_price_leverage_revsens_21d_base_v024_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v025_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v026_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v027_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v028_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v029_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v030_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v031_signal,
    f21upl_f21_uranium_price_leverage_revsens_42d_base_v032_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v033_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v034_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v035_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v036_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v037_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v038_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v039_signal,
    f21upl_f21_uranium_price_leverage_revsens_63d_base_v040_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v041_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v042_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v043_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v044_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v045_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v046_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v047_signal,
    f21upl_f21_uranium_price_leverage_revsens_126d_base_v048_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v049_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v050_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v051_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v052_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v053_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v054_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v055_signal,
    f21upl_f21_uranium_price_leverage_revsens_189d_base_v056_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v057_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v058_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v059_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v060_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v061_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v062_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v063_signal,
    f21upl_f21_uranium_price_leverage_revsens_252d_base_v064_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v065_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v066_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v067_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v068_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v069_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v070_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v071_signal,
    f21upl_f21_uranium_price_leverage_revsens_378d_base_v072_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v073_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v074_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_URANIUM_PRICE_LEVERAGE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    inventory = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "capex": capex,
        "depamor": depamor,
        "cor": cor,
        "assets": assets,
        "inventory": inventory,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f21_revenue_sensitivity', '_f21_commodity_leverage', '_f21_price_leverage_score')
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
    print(f"OK f21_uranium_price_leverage_base_001_075_claude: {n_features} features pass")
