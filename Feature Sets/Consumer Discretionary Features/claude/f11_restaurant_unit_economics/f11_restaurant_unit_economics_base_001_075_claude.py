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

def _f11_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f11_ebitda_per_asset(ebitda, assets):
    return ebitda / assets.replace(0, np.nan)


def _f11_unit_econ_score(revenue, ebitda, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    epa = ebitda / assets.replace(0, np.nan)
    rpa_m = rpa.rolling(w, min_periods=max(1, w // 2)).mean()
    epa_m = epa.rolling(w, min_periods=max(1, w // 2)).mean()
    return rpa_m * 0.5 + epa_m * 0.5


# ===== features =====

def f11rue_f11_restaurant_unit_economics_rpa_xclose_5d_base_v001_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_5d_base_v002_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_5d_base_v003_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_5d_base_v004_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_10d_base_v005_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_10d_base_v006_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_10d_base_v007_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_10d_base_v008_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_21d_base_v009_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_21d_base_v010_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_21d_base_v011_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_21d_base_v012_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_42d_base_v013_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_42d_base_v014_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_42d_base_v015_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_42d_base_v016_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_63d_base_v017_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_63d_base_v018_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_63d_base_v019_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_63d_base_v020_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_126d_base_v021_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_126d_base_v022_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_126d_base_v023_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_126d_base_v024_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_189d_base_v025_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_189d_base_v026_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_189d_base_v027_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_189d_base_v028_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_252d_base_v029_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_252d_base_v030_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_252d_base_v031_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_252d_base_v032_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_378d_base_v033_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_378d_base_v034_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_378d_base_v035_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_378d_base_v036_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_xclose_504d_base_v037_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_zclose_504d_base_v038_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_mclose_504d_base_v039_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_sclose_504d_base_v040_signal(revenue, assets, closeadj):
    result = _mean(_f11_revenue_per_asset(revenue, assets), 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_5d_base_v041_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_5d_base_v042_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_5d_base_v043_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_5d_base_v044_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_10d_base_v045_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_10d_base_v046_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_10d_base_v047_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_10d_base_v048_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_21d_base_v049_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_21d_base_v050_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_21d_base_v051_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_21d_base_v052_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_42d_base_v053_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_42d_base_v054_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_42d_base_v055_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_42d_base_v056_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_63d_base_v057_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_63d_base_v058_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_63d_base_v059_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_63d_base_v060_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_126d_base_v061_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_126d_base_v062_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_126d_base_v063_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_126d_base_v064_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_189d_base_v065_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_189d_base_v066_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_189d_base_v067_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_189d_base_v068_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_252d_base_v069_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_252d_base_v070_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_252d_base_v071_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_252d_base_v072_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_378d_base_v073_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_378d_base_v074_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_378d_base_v075_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f11rue_f11_restaurant_unit_economics_rpa_xclose_5d_base_v001_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_5d_base_v002_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_5d_base_v003_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_5d_base_v004_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_10d_base_v005_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_10d_base_v006_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_10d_base_v007_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_10d_base_v008_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_21d_base_v009_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_21d_base_v010_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_21d_base_v011_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_21d_base_v012_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_42d_base_v013_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_42d_base_v014_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_42d_base_v015_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_42d_base_v016_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_63d_base_v017_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_63d_base_v018_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_63d_base_v019_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_63d_base_v020_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_126d_base_v021_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_126d_base_v022_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_126d_base_v023_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_126d_base_v024_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_189d_base_v025_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_189d_base_v026_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_189d_base_v027_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_189d_base_v028_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_252d_base_v029_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_252d_base_v030_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_252d_base_v031_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_252d_base_v032_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_378d_base_v033_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_378d_base_v034_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_378d_base_v035_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_378d_base_v036_signal,
    f11rue_f11_restaurant_unit_economics_rpa_xclose_504d_base_v037_signal,
    f11rue_f11_restaurant_unit_economics_rpa_zclose_504d_base_v038_signal,
    f11rue_f11_restaurant_unit_economics_rpa_mclose_504d_base_v039_signal,
    f11rue_f11_restaurant_unit_economics_rpa_sclose_504d_base_v040_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_5d_base_v041_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_5d_base_v042_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_5d_base_v043_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_5d_base_v044_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_10d_base_v045_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_10d_base_v046_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_10d_base_v047_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_10d_base_v048_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_21d_base_v049_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_21d_base_v050_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_21d_base_v051_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_21d_base_v052_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_42d_base_v053_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_42d_base_v054_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_42d_base_v055_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_42d_base_v056_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_63d_base_v057_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_63d_base_v058_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_63d_base_v059_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_63d_base_v060_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_126d_base_v061_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_126d_base_v062_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_126d_base_v063_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_126d_base_v064_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_189d_base_v065_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_189d_base_v066_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_189d_base_v067_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_189d_base_v068_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_252d_base_v069_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_252d_base_v070_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_252d_base_v071_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_252d_base_v072_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_378d_base_v073_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_378d_base_v074_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_378d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RESTAURANT_UNIT_ECONOMICS_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f11_revenue_per_asset", "_f11_ebitda_per_asset", "_f11_unit_econ_score")
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
    print(f"OK f11_restaurant_unit_economics_base_001_075_claude: {n_features} features pass")
