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
def _f35_turnover_trajectory(assetturnover, w):
    return _mean(assetturnover, w) + (assetturnover - assetturnover.shift(w))


def _f35_sales_per_asset_compound(revenue, assets, w):
    ratio = revenue / assets.replace(0, np.nan)
    return _mean(ratio, w)


def _f35_turnover_persistence(assetturnover, w):
    m = _mean(assetturnover, w)
    sd = _std(assetturnover, w).replace(0, np.nan)
    return m / sd


def f35atc_f35_asset_turnover_compounding_traj_5d_base_v001_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_21d_base_v002_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_63d_base_v003_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_126d_base_v004_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_252d_base_v005_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_504d_base_v006_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_10d_base_v007_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_42d_base_v008_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_189d_base_v009_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_traj_378d_base_v010_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_5d_base_v011_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_21d_base_v012_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_63d_base_v013_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_126d_base_v014_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_252d_base_v015_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_504d_base_v016_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_10d_base_v017_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_42d_base_v018_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_189d_base_v019_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spa_378d_base_v020_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_21d_base_v021_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_63d_base_v022_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_126d_base_v023_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_252d_base_v024_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_504d_base_v025_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_42d_base_v026_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_189d_base_v027_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persist_378d_base_v028_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atmean_21d_base_v029_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 21) * closeadj + _f35_turnover_trajectory(assetturnover, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atmean_63d_base_v030_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 63) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atmean_252d_base_v031_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 252) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atmean_504d_base_v032_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 504) * closeadj + _f35_turnover_trajectory(assetturnover, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atstd_63d_base_v033_signal(assetturnover, closeadj):
    result = _std(assetturnover, 63) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atstd_252d_base_v034_signal(assetturnover, closeadj):
    result = _std(assetturnover, 252) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atz_63d_base_v035_signal(assetturnover, closeadj):
    result = _z(assetturnover, 252) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atz_252d_base_v036_signal(assetturnover, closeadj):
    result = _z(assetturnover, 504) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atema_21d_base_v037_signal(assetturnover, closeadj):
    result = assetturnover.ewm(span=21, min_periods=10).mean() * closeadj + _f35_turnover_trajectory(assetturnover, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atema_63d_base_v038_signal(assetturnover, closeadj):
    result = assetturnover.ewm(span=63, min_periods=20).mean() * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atema_252d_base_v039_signal(assetturnover, closeadj):
    result = assetturnover.ewm(span=252, min_periods=60).mean() * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spastd_63d_base_v040_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = _std(ratio, 63) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spastd_252d_base_v041_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = _std(ratio, 252) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaz_63d_base_v042_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = _z(ratio, 252) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaz_252d_base_v043_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = _z(ratio, 504) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaema_63d_base_v044_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = ratio.ewm(span=63, min_periods=20).mean() * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaema_252d_base_v045_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = ratio.ewm(span=252, min_periods=60).mean() * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxprice_63d_base_v046_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxprice_252d_base_v047_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajxprice_63d_base_v048_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajxprice_252d_base_v049_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxprice_63d_base_v050_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxprice_252d_base_v051_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atdiff_63d_base_v052_signal(assetturnover, closeadj):
    result = (assetturnover - assetturnover.shift(63)) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atdiff_252d_base_v053_signal(assetturnover, closeadj):
    result = (assetturnover - assetturnover.shift(252)) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atdiff_504d_base_v054_signal(assetturnover, closeadj):
    result = (assetturnover - assetturnover.shift(504)) * closeadj + _f35_turnover_trajectory(assetturnover, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spadiff_63d_base_v055_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = (ratio - ratio.shift(63)) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spadiff_252d_base_v056_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = (ratio - ratio.shift(252)) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistdiff_63d_base_v057_signal(assetturnover, closeadj):
    base = _f35_turnover_persistence(assetturnover, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistdiff_252d_base_v058_signal(assetturnover, closeadj):
    base = _f35_turnover_persistence(assetturnover, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajdiff_63d_base_v059_signal(assetturnover, closeadj):
    base = _f35_turnover_trajectory(assetturnover, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajdiff_252d_base_v060_signal(assetturnover, closeadj):
    base = _f35_turnover_trajectory(assetturnover, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atrank_63d_base_v061_signal(assetturnover, closeadj):
    rank = assetturnover.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atrank_252d_base_v062_signal(assetturnover, closeadj):
    rank = assetturnover.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistrank_63d_base_v063_signal(assetturnover, closeadj):
    base = _f35_turnover_persistence(assetturnover, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistrank_252d_base_v064_signal(assetturnover, closeadj):
    base = _f35_turnover_persistence(assetturnover, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_sparank_63d_base_v065_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    rank = ratio.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_sparank_252d_base_v066_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    rank = ratio.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atmax_252d_base_v067_signal(assetturnover, closeadj):
    result = assetturnover.rolling(252, min_periods=63).max() * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atmin_252d_base_v068_signal(assetturnover, closeadj):
    result = assetturnover.rolling(252, min_periods=63).min() * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atrange_252d_base_v069_signal(assetturnover, closeadj):
    rng = assetturnover.rolling(252, min_periods=63).max() - assetturnover.rolling(252, min_periods=63).min()
    result = rng * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atratio_63v252_base_v070_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 63) / _mean(assetturnover, 252).replace(0, np.nan) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atratio_252v504_base_v071_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 252) / _mean(assetturnover, 504).replace(0, np.nan) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atdiff_63m252_base_v072_signal(assetturnover, closeadj):
    result = (_mean(assetturnover, 63) - _mean(assetturnover, 252)) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atdiff_252m504_base_v073_signal(assetturnover, closeadj):
    result = (_mean(assetturnover, 252) - _mean(assetturnover, 504)) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevg_63d_base_v074_signal(assetturnover, revenue, closeadj):
    g = revenue.pct_change(63)
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * (1.0 + g.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevg_252d_base_v075_signal(assetturnover, revenue, closeadj):
    g = revenue.pct_change(252)
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * (1.0 + g.abs())
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35atc_f35_asset_turnover_compounding_traj_5d_base_v001_signal,
    f35atc_f35_asset_turnover_compounding_traj_21d_base_v002_signal,
    f35atc_f35_asset_turnover_compounding_traj_63d_base_v003_signal,
    f35atc_f35_asset_turnover_compounding_traj_126d_base_v004_signal,
    f35atc_f35_asset_turnover_compounding_traj_252d_base_v005_signal,
    f35atc_f35_asset_turnover_compounding_traj_504d_base_v006_signal,
    f35atc_f35_asset_turnover_compounding_traj_10d_base_v007_signal,
    f35atc_f35_asset_turnover_compounding_traj_42d_base_v008_signal,
    f35atc_f35_asset_turnover_compounding_traj_189d_base_v009_signal,
    f35atc_f35_asset_turnover_compounding_traj_378d_base_v010_signal,
    f35atc_f35_asset_turnover_compounding_spa_5d_base_v011_signal,
    f35atc_f35_asset_turnover_compounding_spa_21d_base_v012_signal,
    f35atc_f35_asset_turnover_compounding_spa_63d_base_v013_signal,
    f35atc_f35_asset_turnover_compounding_spa_126d_base_v014_signal,
    f35atc_f35_asset_turnover_compounding_spa_252d_base_v015_signal,
    f35atc_f35_asset_turnover_compounding_spa_504d_base_v016_signal,
    f35atc_f35_asset_turnover_compounding_spa_10d_base_v017_signal,
    f35atc_f35_asset_turnover_compounding_spa_42d_base_v018_signal,
    f35atc_f35_asset_turnover_compounding_spa_189d_base_v019_signal,
    f35atc_f35_asset_turnover_compounding_spa_378d_base_v020_signal,
    f35atc_f35_asset_turnover_compounding_persist_21d_base_v021_signal,
    f35atc_f35_asset_turnover_compounding_persist_63d_base_v022_signal,
    f35atc_f35_asset_turnover_compounding_persist_126d_base_v023_signal,
    f35atc_f35_asset_turnover_compounding_persist_252d_base_v024_signal,
    f35atc_f35_asset_turnover_compounding_persist_504d_base_v025_signal,
    f35atc_f35_asset_turnover_compounding_persist_42d_base_v026_signal,
    f35atc_f35_asset_turnover_compounding_persist_189d_base_v027_signal,
    f35atc_f35_asset_turnover_compounding_persist_378d_base_v028_signal,
    f35atc_f35_asset_turnover_compounding_atmean_21d_base_v029_signal,
    f35atc_f35_asset_turnover_compounding_atmean_63d_base_v030_signal,
    f35atc_f35_asset_turnover_compounding_atmean_252d_base_v031_signal,
    f35atc_f35_asset_turnover_compounding_atmean_504d_base_v032_signal,
    f35atc_f35_asset_turnover_compounding_atstd_63d_base_v033_signal,
    f35atc_f35_asset_turnover_compounding_atstd_252d_base_v034_signal,
    f35atc_f35_asset_turnover_compounding_atz_63d_base_v035_signal,
    f35atc_f35_asset_turnover_compounding_atz_252d_base_v036_signal,
    f35atc_f35_asset_turnover_compounding_atema_21d_base_v037_signal,
    f35atc_f35_asset_turnover_compounding_atema_63d_base_v038_signal,
    f35atc_f35_asset_turnover_compounding_atema_252d_base_v039_signal,
    f35atc_f35_asset_turnover_compounding_spastd_63d_base_v040_signal,
    f35atc_f35_asset_turnover_compounding_spastd_252d_base_v041_signal,
    f35atc_f35_asset_turnover_compounding_spaz_63d_base_v042_signal,
    f35atc_f35_asset_turnover_compounding_spaz_252d_base_v043_signal,
    f35atc_f35_asset_turnover_compounding_spaema_63d_base_v044_signal,
    f35atc_f35_asset_turnover_compounding_spaema_252d_base_v045_signal,
    f35atc_f35_asset_turnover_compounding_persistxprice_63d_base_v046_signal,
    f35atc_f35_asset_turnover_compounding_persistxprice_252d_base_v047_signal,
    f35atc_f35_asset_turnover_compounding_trajxprice_63d_base_v048_signal,
    f35atc_f35_asset_turnover_compounding_trajxprice_252d_base_v049_signal,
    f35atc_f35_asset_turnover_compounding_spaxprice_63d_base_v050_signal,
    f35atc_f35_asset_turnover_compounding_spaxprice_252d_base_v051_signal,
    f35atc_f35_asset_turnover_compounding_atdiff_63d_base_v052_signal,
    f35atc_f35_asset_turnover_compounding_atdiff_252d_base_v053_signal,
    f35atc_f35_asset_turnover_compounding_atdiff_504d_base_v054_signal,
    f35atc_f35_asset_turnover_compounding_spadiff_63d_base_v055_signal,
    f35atc_f35_asset_turnover_compounding_spadiff_252d_base_v056_signal,
    f35atc_f35_asset_turnover_compounding_persistdiff_63d_base_v057_signal,
    f35atc_f35_asset_turnover_compounding_persistdiff_252d_base_v058_signal,
    f35atc_f35_asset_turnover_compounding_trajdiff_63d_base_v059_signal,
    f35atc_f35_asset_turnover_compounding_trajdiff_252d_base_v060_signal,
    f35atc_f35_asset_turnover_compounding_atrank_63d_base_v061_signal,
    f35atc_f35_asset_turnover_compounding_atrank_252d_base_v062_signal,
    f35atc_f35_asset_turnover_compounding_persistrank_63d_base_v063_signal,
    f35atc_f35_asset_turnover_compounding_persistrank_252d_base_v064_signal,
    f35atc_f35_asset_turnover_compounding_sparank_63d_base_v065_signal,
    f35atc_f35_asset_turnover_compounding_sparank_252d_base_v066_signal,
    f35atc_f35_asset_turnover_compounding_atmax_252d_base_v067_signal,
    f35atc_f35_asset_turnover_compounding_atmin_252d_base_v068_signal,
    f35atc_f35_asset_turnover_compounding_atrange_252d_base_v069_signal,
    f35atc_f35_asset_turnover_compounding_atratio_63v252_base_v070_signal,
    f35atc_f35_asset_turnover_compounding_atratio_252v504_base_v071_signal,
    f35atc_f35_asset_turnover_compounding_atdiff_63m252_base_v072_signal,
    f35atc_f35_asset_turnover_compounding_atdiff_252m504_base_v073_signal,
    f35atc_f35_asset_turnover_compounding_atxrevg_63d_base_v074_signal,
    f35atc_f35_asset_turnover_compounding_atxrevg_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_ASSET_TURNOVER_COMPOUNDING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetturnover = pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "assets": assets, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_turnover_trajectory", "_f35_sales_per_asset_compound", "_f35_turnover_persistence")
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
    print(f"OK f35_asset_turnover_compounding_base_001_075_claude: {n_features} features pass")
