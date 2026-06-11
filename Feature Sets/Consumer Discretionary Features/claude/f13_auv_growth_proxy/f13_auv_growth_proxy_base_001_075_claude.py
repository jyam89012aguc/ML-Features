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

def _f13_revenue_per_ppe(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f13_auv_growth(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    return rpp.pct_change(periods=w)


def _f13_unit_volume_trajectory(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    g1 = rpp.pct_change(periods=w)
    g2 = rpp.pct_change(periods=2 * w)
    return g1 + 0.5 * g2


# ===== features =====

def f13auv_f13_auv_growth_proxy_rpp_xclose_5d_base_v001_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_5d_base_v002_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_5d_base_v003_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_5d_base_v004_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_10d_base_v005_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_10d_base_v006_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_10d_base_v007_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_10d_base_v008_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_21d_base_v009_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_21d_base_v010_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_21d_base_v011_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_21d_base_v012_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_42d_base_v013_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_42d_base_v014_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_42d_base_v015_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_42d_base_v016_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_63d_base_v017_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_63d_base_v018_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_63d_base_v019_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_63d_base_v020_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_126d_base_v021_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_126d_base_v022_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_126d_base_v023_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_126d_base_v024_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_189d_base_v025_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_189d_base_v026_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_189d_base_v027_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_189d_base_v028_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_252d_base_v029_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_252d_base_v030_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_252d_base_v031_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_252d_base_v032_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_378d_base_v033_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_378d_base_v034_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_378d_base_v035_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_378d_base_v036_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_xclose_504d_base_v037_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_zclose_504d_base_v038_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_mclose_504d_base_v039_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rpp_sclose_504d_base_v040_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_revenue_per_ppe(revenue, ppnenet), 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_5d_base_v041_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_5d_base_v042_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_5d_base_v043_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_5d_base_v044_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_10d_base_v045_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_10d_base_v046_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_10d_base_v047_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_10d_base_v048_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_21d_base_v049_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_21d_base_v050_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_21d_base_v051_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_21d_base_v052_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_42d_base_v053_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_42d_base_v054_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_42d_base_v055_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_42d_base_v056_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_63d_base_v057_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_63d_base_v058_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_63d_base_v059_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_63d_base_v060_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_126d_base_v061_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_126d_base_v062_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_126d_base_v063_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_126d_base_v064_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_189d_base_v065_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_189d_base_v066_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_189d_base_v067_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_189d_base_v068_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_252d_base_v069_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_252d_base_v070_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_252d_base_v071_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_252d_base_v072_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_378d_base_v073_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_378d_base_v074_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_378d_base_v075_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f13auv_f13_auv_growth_proxy_rpp_xclose_5d_base_v001_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_5d_base_v002_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_5d_base_v003_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_5d_base_v004_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_10d_base_v005_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_10d_base_v006_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_10d_base_v007_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_10d_base_v008_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_21d_base_v009_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_21d_base_v010_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_21d_base_v011_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_21d_base_v012_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_42d_base_v013_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_42d_base_v014_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_42d_base_v015_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_42d_base_v016_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_63d_base_v017_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_63d_base_v018_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_63d_base_v019_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_63d_base_v020_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_126d_base_v021_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_126d_base_v022_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_126d_base_v023_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_126d_base_v024_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_189d_base_v025_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_189d_base_v026_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_189d_base_v027_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_189d_base_v028_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_252d_base_v029_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_252d_base_v030_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_252d_base_v031_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_252d_base_v032_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_378d_base_v033_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_378d_base_v034_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_378d_base_v035_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_378d_base_v036_signal,
    f13auv_f13_auv_growth_proxy_rpp_xclose_504d_base_v037_signal,
    f13auv_f13_auv_growth_proxy_rpp_zclose_504d_base_v038_signal,
    f13auv_f13_auv_growth_proxy_rpp_mclose_504d_base_v039_signal,
    f13auv_f13_auv_growth_proxy_rpp_sclose_504d_base_v040_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_5d_base_v041_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_5d_base_v042_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_5d_base_v043_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_5d_base_v044_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_10d_base_v045_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_10d_base_v046_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_10d_base_v047_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_10d_base_v048_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_21d_base_v049_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_21d_base_v050_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_21d_base_v051_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_21d_base_v052_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_42d_base_v053_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_42d_base_v054_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_42d_base_v055_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_42d_base_v056_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_63d_base_v057_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_63d_base_v058_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_63d_base_v059_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_63d_base_v060_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_126d_base_v061_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_126d_base_v062_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_126d_base_v063_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_126d_base_v064_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_189d_base_v065_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_189d_base_v066_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_189d_base_v067_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_189d_base_v068_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_252d_base_v069_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_252d_base_v070_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_252d_base_v071_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_252d_base_v072_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_378d_base_v073_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_378d_base_v074_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_378d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_AUV_GROWTH_PROXY_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f13_revenue_per_ppe", "_f13_auv_growth", "_f13_unit_volume_trajectory")
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
    print(f"OK f13_auv_growth_proxy_base_001_075_claude: {n_features} features pass")
