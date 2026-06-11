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
def _f06_asset_turnover_proxy(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f06_sales_per_ppe(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan).abs()


def _f06_util_z(revenue, assets, w):
    turn = revenue / assets.replace(0, np.nan).abs()
    m = turn.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = turn.rolling(w, min_periods=max(1, w // 2)).std()
    return (turn - m) / sd.replace(0, np.nan)


# 21d turnover proxy * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_21d_base_v001_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover proxy * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_63d_base_v002_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d turnover proxy * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_126d_base_v003_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover proxy * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_252d_base_v004_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d turnover proxy * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_504d_base_v005_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sales per PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_21d_base_v006_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sales per PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_63d_base_v007_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sales per PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_126d_base_v008_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sales per PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_252d_base_v009_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sales per PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_504d_base_v010_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d util z
def f06cup_f06_capacity_utilization_proxy_utilz_63d_base_v011_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d util z
def f06cup_f06_capacity_utilization_proxy_utilz_126d_base_v012_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d util z
def f06cup_f06_capacity_utilization_proxy_utilz_252d_base_v013_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d util z
def f06cup_f06_capacity_utilization_proxy_utilz_504d_base_v014_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnstd_21d_base_v015_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnstd_63d_base_v016_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnstd_252d_base_v017_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnstd_504d_base_v018_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppestd_21d_base_v019_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppestd_63d_base_v020_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppestd_252d_base_v021_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppestd_504d_base_v022_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of turnover
def f06cup_f06_capacity_utilization_proxy_turnz_21d_base_v023_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of turnover
def f06cup_f06_capacity_utilization_proxy_turnz_63d_base_v024_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of turnover
def f06cup_f06_capacity_utilization_proxy_turnz_252d_base_v025_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of turnover
def f06cup_f06_capacity_utilization_proxy_turnz_504d_base_v026_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_sppez_21d_base_v027_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_sppez_63d_base_v028_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_sppez_252d_base_v029_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_sppez_504d_base_v030_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_5d_base_v031_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_10d_base_v032_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_42d_base_v033_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_189d_base_v034_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turn_378d_base_v035_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_5d_base_v036_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_10d_base_v037_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_42d_base_v038_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_189d_base_v039_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppe_378d_base_v040_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnema_21d_base_v041_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnema_63d_base_v042_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnema_252d_base_v043_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppeema_21d_base_v044_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppeema_63d_base_v045_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of sales-per-PPE * closeadj
def f06cup_f06_capacity_utilization_proxy_sppeema_252d_base_v046_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover gap to 252d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_turngap_21v252_base_v047_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover gap to 252d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_turngap_63v252_base_v048_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover gap to 504d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_turngap_63v504_base_v049_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 63) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d turnover gap to 504d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_turngap_126v504_base_v050_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 126) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sppe gap to 252d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_sppegap_21v252_base_v051_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe gap to 252d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_sppegap_63v252_base_v052_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe gap to 504d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_sppegap_63v504_base_v053_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 63) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sppe gap to 504d mean * closeadj
def f06cup_f06_capacity_utilization_proxy_sppegap_126v504_base_v054_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 126) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d util z * sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_21d_base_v055_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 21)
    sppe = _f06_sales_per_ppe(revenue, ppnenet)
    result = z * sppe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d util z * sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_63d_base_v056_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    sppe = _f06_sales_per_ppe(revenue, ppnenet)
    result = z * sppe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d util z * sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_252d_base_v057_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    sppe = _f06_sales_per_ppe(revenue, ppnenet)
    result = z * sppe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d util z * sales-per-PPE
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_504d_base_v058_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 504)
    sppe = _f06_sales_per_ppe(revenue, ppnenet)
    result = z * sppe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover / 252d turnover ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_turnratio_21v252_base_v059_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 21) / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover / 252d turnover ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_turnratio_63v252_base_v060_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 63) / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover / 504d turnover ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_turnratio_63v504_base_v061_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = (_mean(base, 63) / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sppe / 252d sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_sppertio_21v252_base_v062_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 21) / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe / 252d sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_sppertio_63v252_base_v063_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 63) / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe / 504d sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_sppertio_63v504_base_v064_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(base, 63) / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover - sppe difference * closeadj
def f06cup_f06_capacity_utilization_proxy_turnminussppe_21d_base_v065_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 21) - _mean(b, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover - sppe difference * closeadj
def f06cup_f06_capacity_utilization_proxy_turnminussppe_63d_base_v066_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 63) - _mean(b, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover - sppe difference * closeadj
def f06cup_f06_capacity_utilization_proxy_turnminussppe_252d_base_v067_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 252) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d turnover - sppe difference * closeadj
def f06cup_f06_capacity_utilization_proxy_turnminussppe_504d_base_v068_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 504) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover * sppe product * closeadj
def f06cup_f06_capacity_utilization_proxy_turnxsppe_21d_base_v069_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(a * b, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover * sppe product * closeadj
def f06cup_f06_capacity_utilization_proxy_turnxsppe_63d_base_v070_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(a * b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover * sppe product * closeadj
def f06cup_f06_capacity_utilization_proxy_turnxsppe_252d_base_v071_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(a * b, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover log * closeadj
def f06cup_f06_capacity_utilization_proxy_turnlog_63d_base_v072_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = np.log(_mean(base, 63).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sppe log * closeadj
def f06cup_f06_capacity_utilization_proxy_sppelog_252d_base_v073_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = np.log(_mean(base, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d util z * closeadj (squared)
def f06cup_f06_capacity_utilization_proxy_utilzsq_63d_base_v074_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    result = z * z.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d util z (squared) * closeadj
def f06cup_f06_capacity_utilization_proxy_utilzsq_252d_base_v075_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    result = z * z.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06cup_f06_capacity_utilization_proxy_turn_21d_base_v001_signal,
    f06cup_f06_capacity_utilization_proxy_turn_63d_base_v002_signal,
    f06cup_f06_capacity_utilization_proxy_turn_126d_base_v003_signal,
    f06cup_f06_capacity_utilization_proxy_turn_252d_base_v004_signal,
    f06cup_f06_capacity_utilization_proxy_turn_504d_base_v005_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_21d_base_v006_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_63d_base_v007_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_126d_base_v008_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_252d_base_v009_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_504d_base_v010_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_63d_base_v011_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_126d_base_v012_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_252d_base_v013_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_504d_base_v014_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_21d_base_v015_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_63d_base_v016_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_252d_base_v017_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_504d_base_v018_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_21d_base_v019_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_63d_base_v020_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_252d_base_v021_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_504d_base_v022_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_21d_base_v023_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_63d_base_v024_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_252d_base_v025_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_504d_base_v026_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_21d_base_v027_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_63d_base_v028_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_252d_base_v029_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_504d_base_v030_signal,
    f06cup_f06_capacity_utilization_proxy_turn_5d_base_v031_signal,
    f06cup_f06_capacity_utilization_proxy_turn_10d_base_v032_signal,
    f06cup_f06_capacity_utilization_proxy_turn_42d_base_v033_signal,
    f06cup_f06_capacity_utilization_proxy_turn_189d_base_v034_signal,
    f06cup_f06_capacity_utilization_proxy_turn_378d_base_v035_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_5d_base_v036_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_10d_base_v037_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_42d_base_v038_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_189d_base_v039_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_378d_base_v040_signal,
    f06cup_f06_capacity_utilization_proxy_turnema_21d_base_v041_signal,
    f06cup_f06_capacity_utilization_proxy_turnema_63d_base_v042_signal,
    f06cup_f06_capacity_utilization_proxy_turnema_252d_base_v043_signal,
    f06cup_f06_capacity_utilization_proxy_sppeema_21d_base_v044_signal,
    f06cup_f06_capacity_utilization_proxy_sppeema_63d_base_v045_signal,
    f06cup_f06_capacity_utilization_proxy_sppeema_252d_base_v046_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_21v252_base_v047_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_63v252_base_v048_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_63v504_base_v049_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_126v504_base_v050_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_21v252_base_v051_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_63v252_base_v052_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_63v504_base_v053_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_126v504_base_v054_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_21d_base_v055_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_63d_base_v056_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_252d_base_v057_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_504d_base_v058_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_21v252_base_v059_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_63v252_base_v060_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_63v504_base_v061_signal,
    f06cup_f06_capacity_utilization_proxy_sppertio_21v252_base_v062_signal,
    f06cup_f06_capacity_utilization_proxy_sppertio_63v252_base_v063_signal,
    f06cup_f06_capacity_utilization_proxy_sppertio_63v504_base_v064_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_21d_base_v065_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_63d_base_v066_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_252d_base_v067_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_504d_base_v068_signal,
    f06cup_f06_capacity_utilization_proxy_turnxsppe_21d_base_v069_signal,
    f06cup_f06_capacity_utilization_proxy_turnxsppe_63d_base_v070_signal,
    f06cup_f06_capacity_utilization_proxy_turnxsppe_252d_base_v071_signal,
    f06cup_f06_capacity_utilization_proxy_turnlog_63d_base_v072_signal,
    f06cup_f06_capacity_utilization_proxy_sppelog_252d_base_v073_signal,
    f06cup_f06_capacity_utilization_proxy_utilzsq_63d_base_v074_signal,
    f06cup_f06_capacity_utilization_proxy_utilzsq_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_CAPACITY_UTILIZATION_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {"closeadj": closeadj, "revenue": revenue, "assets": assets, "ppnenet": ppnenet}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_asset_turnover_proxy", "_f06_sales_per_ppe", "_f06_util_z")
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
    print(f"OK f06_capacity_utilization_proxy_base_001_075_claude: {n_features} features pass")
