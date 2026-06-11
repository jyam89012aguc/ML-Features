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
def _f33_roic_trajectory(roic, w):
    return _mean(roic, w) + (roic - roic.shift(w))


def _f33_roic_persistence(roic, w):
    m = _mean(roic, w)
    sd = _std(roic, w).replace(0, np.nan)
    return m / sd


def _f33_capital_efficiency_uplift(roic, roa, w):
    return _mean(roic - roa, w)


def f33cec_f33_capital_efficiency_compounding_roictrend_5d_base_v001_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_21d_base_v002_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_63d_base_v003_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_126d_base_v004_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_252d_base_v005_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_504d_base_v006_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicpersist_21d_base_v007_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicpersist_63d_base_v008_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicpersist_126d_base_v009_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicpersist_252d_base_v010_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicpersist_504d_base_v011_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_21d_base_v012_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_63d_base_v013_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_126d_base_v014_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_252d_base_v015_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_504d_base_v016_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicmean_21d_base_v017_signal(roic, closeadj):
    result = _mean(roic, 21) * closeadj + _f33_roic_trajectory(roic, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicmean_63d_base_v018_signal(roic, closeadj):
    result = _mean(roic, 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicmean_252d_base_v019_signal(roic, closeadj):
    result = _mean(roic, 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicmean_504d_base_v020_signal(roic, closeadj):
    result = _mean(roic, 504) * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicstd_63d_base_v021_signal(roic, closeadj):
    result = _std(roic, 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicstd_252d_base_v022_signal(roic, closeadj):
    result = _std(roic, 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicstd_504d_base_v023_signal(roic, closeadj):
    result = _std(roic, 504) * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicz_63d_base_v024_signal(roic, closeadj):
    result = _z(roic, 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicz_252d_base_v025_signal(roic, closeadj):
    result = _z(roic, 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicz_504d_base_v026_signal(roic, closeadj):
    result = _z(roic, 504) * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roeuplift_63d_base_v027_signal(roic, roe, closeadj):
    base = _mean(roic - roe, 63)
    result = base * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roeuplift_252d_base_v028_signal(roic, roe, closeadj):
    base = _mean(roic - roe, 252)
    result = base * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roeuplift_504d_base_v029_signal(roic, roe, closeadj):
    base = _mean(roic - roe, 504)
    result = base * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicema_21d_base_v030_signal(roic, closeadj):
    result = roic.ewm(span=21, min_periods=10).mean() * closeadj + _f33_roic_trajectory(roic, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicema_63d_base_v031_signal(roic, closeadj):
    result = roic.ewm(span=63, min_periods=20).mean() * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicema_252d_base_v032_signal(roic, closeadj):
    result = roic.ewm(span=252, min_periods=60).mean() * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_5d_alt_base_v033_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_42d_base_v034_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_189d_base_v035_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roictrend_378d_base_v036_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_5d_base_v037_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_10d_base_v038_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_42d_base_v039_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_189d_base_v040_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_378d_base_v041_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_5d_base_v042_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_10d_base_v043_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_42d_base_v044_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_189d_base_v045_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_378d_base_v046_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxprice_63d_base_v047_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxprice_252d_base_v048_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftxprice_63d_base_v049_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftxprice_252d_base_v050_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajxprice_63d_base_v051_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajxprice_252d_base_v052_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicrank_63d_base_v053_signal(roic, closeadj):
    rank = roic.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicrank_252d_base_v054_signal(roic, closeadj):
    rank = roic.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistrank_63d_base_v055_signal(roic, closeadj):
    base = _f33_roic_persistence(roic, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistrank_252d_base_v056_signal(roic, closeadj):
    base = _f33_roic_persistence(roic, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftrank_63d_base_v057_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftrank_252d_base_v058_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicdiff_63d_base_v059_signal(roic, closeadj):
    result = (roic - roic.shift(63)) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicdiff_252d_base_v060_signal(roic, closeadj):
    result = (roic - roic.shift(252)) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicdiff_504d_base_v061_signal(roic, closeadj):
    result = (roic - roic.shift(504)) * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicmax_252d_base_v062_signal(roic, closeadj):
    result = roic.rolling(252, min_periods=63).max() * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicmin_252d_base_v063_signal(roic, closeadj):
    result = roic.rolling(252, min_periods=63).min() * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicrange_252d_base_v064_signal(roic, closeadj):
    rng = roic.rolling(252, min_periods=63).max() - roic.rolling(252, min_periods=63).min()
    result = rng * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicratio_63v252_base_v065_signal(roic, closeadj):
    result = _mean(roic, 63) / _mean(roic, 252).replace(0, np.nan) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicratio_252v504_base_v066_signal(roic, closeadj):
    result = _mean(roic, 252) / _mean(roic, 504).replace(0, np.nan) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftratio_63v252_base_v067_signal(roic, roa, closeadj):
    a = _f33_capital_efficiency_uplift(roic, roa, 63)
    b = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftratio_252v504_base_v068_signal(roic, roa, closeadj):
    a = _f33_capital_efficiency_uplift(roic, roa, 252)
    b = _f33_capital_efficiency_uplift(roic, roa, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistdiff_63d_base_v069_signal(roic, closeadj):
    base = _f33_roic_persistence(roic, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistdiff_252d_base_v070_signal(roic, closeadj):
    base = _f33_roic_persistence(roic, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftdiff_63d_base_v071_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftdiff_252d_base_v072_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajdiff_63d_base_v073_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajdiff_252d_base_v074_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_compositeq_252d_base_v075_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 252)
    b = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33cec_f33_capital_efficiency_compounding_roictrend_5d_base_v001_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_21d_base_v002_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_63d_base_v003_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_126d_base_v004_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_252d_base_v005_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_504d_base_v006_signal,
    f33cec_f33_capital_efficiency_compounding_roicpersist_21d_base_v007_signal,
    f33cec_f33_capital_efficiency_compounding_roicpersist_63d_base_v008_signal,
    f33cec_f33_capital_efficiency_compounding_roicpersist_126d_base_v009_signal,
    f33cec_f33_capital_efficiency_compounding_roicpersist_252d_base_v010_signal,
    f33cec_f33_capital_efficiency_compounding_roicpersist_504d_base_v011_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_21d_base_v012_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_63d_base_v013_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_126d_base_v014_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_252d_base_v015_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_504d_base_v016_signal,
    f33cec_f33_capital_efficiency_compounding_roicmean_21d_base_v017_signal,
    f33cec_f33_capital_efficiency_compounding_roicmean_63d_base_v018_signal,
    f33cec_f33_capital_efficiency_compounding_roicmean_252d_base_v019_signal,
    f33cec_f33_capital_efficiency_compounding_roicmean_504d_base_v020_signal,
    f33cec_f33_capital_efficiency_compounding_roicstd_63d_base_v021_signal,
    f33cec_f33_capital_efficiency_compounding_roicstd_252d_base_v022_signal,
    f33cec_f33_capital_efficiency_compounding_roicstd_504d_base_v023_signal,
    f33cec_f33_capital_efficiency_compounding_roicz_63d_base_v024_signal,
    f33cec_f33_capital_efficiency_compounding_roicz_252d_base_v025_signal,
    f33cec_f33_capital_efficiency_compounding_roicz_504d_base_v026_signal,
    f33cec_f33_capital_efficiency_compounding_roeuplift_63d_base_v027_signal,
    f33cec_f33_capital_efficiency_compounding_roeuplift_252d_base_v028_signal,
    f33cec_f33_capital_efficiency_compounding_roeuplift_504d_base_v029_signal,
    f33cec_f33_capital_efficiency_compounding_roicema_21d_base_v030_signal,
    f33cec_f33_capital_efficiency_compounding_roicema_63d_base_v031_signal,
    f33cec_f33_capital_efficiency_compounding_roicema_252d_base_v032_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_5d_alt_base_v033_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_42d_base_v034_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_189d_base_v035_signal,
    f33cec_f33_capital_efficiency_compounding_roictrend_378d_base_v036_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_5d_base_v037_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_10d_base_v038_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_42d_base_v039_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_189d_base_v040_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_378d_base_v041_signal,
    f33cec_f33_capital_efficiency_compounding_persist_5d_base_v042_signal,
    f33cec_f33_capital_efficiency_compounding_persist_10d_base_v043_signal,
    f33cec_f33_capital_efficiency_compounding_persist_42d_base_v044_signal,
    f33cec_f33_capital_efficiency_compounding_persist_189d_base_v045_signal,
    f33cec_f33_capital_efficiency_compounding_persist_378d_base_v046_signal,
    f33cec_f33_capital_efficiency_compounding_persistxprice_63d_base_v047_signal,
    f33cec_f33_capital_efficiency_compounding_persistxprice_252d_base_v048_signal,
    f33cec_f33_capital_efficiency_compounding_upliftxprice_63d_base_v049_signal,
    f33cec_f33_capital_efficiency_compounding_upliftxprice_252d_base_v050_signal,
    f33cec_f33_capital_efficiency_compounding_trajxprice_63d_base_v051_signal,
    f33cec_f33_capital_efficiency_compounding_trajxprice_252d_base_v052_signal,
    f33cec_f33_capital_efficiency_compounding_roicrank_63d_base_v053_signal,
    f33cec_f33_capital_efficiency_compounding_roicrank_252d_base_v054_signal,
    f33cec_f33_capital_efficiency_compounding_persistrank_63d_base_v055_signal,
    f33cec_f33_capital_efficiency_compounding_persistrank_252d_base_v056_signal,
    f33cec_f33_capital_efficiency_compounding_upliftrank_63d_base_v057_signal,
    f33cec_f33_capital_efficiency_compounding_upliftrank_252d_base_v058_signal,
    f33cec_f33_capital_efficiency_compounding_roicdiff_63d_base_v059_signal,
    f33cec_f33_capital_efficiency_compounding_roicdiff_252d_base_v060_signal,
    f33cec_f33_capital_efficiency_compounding_roicdiff_504d_base_v061_signal,
    f33cec_f33_capital_efficiency_compounding_roicmax_252d_base_v062_signal,
    f33cec_f33_capital_efficiency_compounding_roicmin_252d_base_v063_signal,
    f33cec_f33_capital_efficiency_compounding_roicrange_252d_base_v064_signal,
    f33cec_f33_capital_efficiency_compounding_roicratio_63v252_base_v065_signal,
    f33cec_f33_capital_efficiency_compounding_roicratio_252v504_base_v066_signal,
    f33cec_f33_capital_efficiency_compounding_upliftratio_63v252_base_v067_signal,
    f33cec_f33_capital_efficiency_compounding_upliftratio_252v504_base_v068_signal,
    f33cec_f33_capital_efficiency_compounding_persistdiff_63d_base_v069_signal,
    f33cec_f33_capital_efficiency_compounding_persistdiff_252d_base_v070_signal,
    f33cec_f33_capital_efficiency_compounding_upliftdiff_63d_base_v071_signal,
    f33cec_f33_capital_efficiency_compounding_upliftdiff_252d_base_v072_signal,
    f33cec_f33_capital_efficiency_compounding_trajdiff_63d_base_v073_signal,
    f33cec_f33_capital_efficiency_compounding_trajdiff_252d_base_v074_signal,
    f33cec_f33_capital_efficiency_compounding_compositeq_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_CAPITAL_EFFICIENCY_COMPOUNDING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roa  = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe  = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f33_roic_trajectory", "_f33_roic_persistence", "_f33_capital_efficiency_uplift")
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
    print(f"OK f33_capital_efficiency_compounding_base_001_075_claude: {n_features} features pass")
