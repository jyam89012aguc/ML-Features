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
def _f06_asset_turnover_proxy(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f06_sales_per_ppe(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan).abs()


def _f06_util_z(revenue, assets, w):
    turn = revenue / assets.replace(0, np.nan).abs()
    m = turn.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = turn.rolling(w, min_periods=max(1, w // 2)).std()
    return (turn - m) / sd.replace(0, np.nan)


# ============== SLOPE FEATURES (150) ==============

# slope of 21d mean turnover * closeadj, 5d
def f06cup_f06_capacity_utilization_proxy_turn_21d_jerk_v001_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d mean turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turn_21d_jerk_v002_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d mean turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turn_63d_jerk_v003_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d mean turnover * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turn_63d_jerk_v004_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d mean turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turn_126d_jerk_v005_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d mean turnover * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turn_126d_jerk_v006_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d mean turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turn_252d_jerk_v007_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d mean turnover * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turn_252d_jerk_v008_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d mean turnover * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turn_504d_jerk_v009_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d mean turnover * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_turn_504d_jerk_v010_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d mean sppe * closeadj, 5d
def f06cup_f06_capacity_utilization_proxy_sppe_21d_jerk_v011_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d mean sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppe_21d_jerk_v012_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d mean sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppe_63d_jerk_v013_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d mean sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppe_63d_jerk_v014_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d mean sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppe_126d_jerk_v015_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d mean sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppe_126d_jerk_v016_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d mean sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppe_252d_jerk_v017_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d mean sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppe_252d_jerk_v018_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d mean sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppe_504d_jerk_v019_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d mean sppe * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_sppe_504d_jerk_v020_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d util_z * closeadj, 5d
def f06cup_f06_capacity_utilization_proxy_utilz_63d_jerk_v021_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d util_z * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_utilz_63d_jerk_v022_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d util_z * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_utilz_126d_jerk_v023_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d util_z * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_utilz_252d_jerk_v024_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d util_z * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_utilz_252d_jerk_v025_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d util_z * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_utilz_504d_jerk_v026_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d util_z * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_utilz_504d_jerk_v027_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d std turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnstd_21d_jerk_v028_signal(revenue, assets, closeadj):
    base = _std(_f06_asset_turnover_proxy(revenue, assets), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d std turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnstd_63d_jerk_v029_signal(revenue, assets, closeadj):
    base = _std(_f06_asset_turnover_proxy(revenue, assets), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d std turnover * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turnstd_252d_jerk_v030_signal(revenue, assets, closeadj):
    base = _std(_f06_asset_turnover_proxy(revenue, assets), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d std turnover * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_turnstd_504d_jerk_v031_signal(revenue, assets, closeadj):
    base = _std(_f06_asset_turnover_proxy(revenue, assets), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d std sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppestd_21d_jerk_v032_signal(revenue, ppnenet, closeadj):
    base = _std(_f06_sales_per_ppe(revenue, ppnenet), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d std sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppestd_63d_jerk_v033_signal(revenue, ppnenet, closeadj):
    base = _std(_f06_sales_per_ppe(revenue, ppnenet), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d std sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppestd_252d_jerk_v034_signal(revenue, ppnenet, closeadj):
    base = _std(_f06_sales_per_ppe(revenue, ppnenet), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d std sppe * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_sppestd_504d_jerk_v035_signal(revenue, ppnenet, closeadj):
    base = _std(_f06_sales_per_ppe(revenue, ppnenet), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d z turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnz_21d_jerk_v036_signal(revenue, assets, closeadj):
    base = _z(_f06_asset_turnover_proxy(revenue, assets), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d z turnover * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnz_63d_jerk_v037_signal(revenue, assets, closeadj):
    base = _z(_f06_asset_turnover_proxy(revenue, assets), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d z turnover * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turnz_252d_jerk_v038_signal(revenue, assets, closeadj):
    base = _z(_f06_asset_turnover_proxy(revenue, assets), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d z turnover * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_turnz_504d_jerk_v039_signal(revenue, assets, closeadj):
    base = _z(_f06_asset_turnover_proxy(revenue, assets), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d z sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppez_21d_jerk_v040_signal(revenue, ppnenet, closeadj):
    base = _z(_f06_sales_per_ppe(revenue, ppnenet), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d z sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppez_63d_jerk_v041_signal(revenue, ppnenet, closeadj):
    base = _z(_f06_sales_per_ppe(revenue, ppnenet), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d z sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppez_252d_jerk_v042_signal(revenue, ppnenet, closeadj):
    base = _z(_f06_sales_per_ppe(revenue, ppnenet), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d z sppe * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_sppez_504d_jerk_v043_signal(revenue, ppnenet, closeadj):
    base = _z(_f06_sales_per_ppe(revenue, ppnenet), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d turn * closeadj, 5d
def f06cup_f06_capacity_utilization_proxy_turn_5d_jerk_v044_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 10d turn * closeadj, 10d
def f06cup_f06_capacity_utilization_proxy_turn_10d_jerk_v045_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 42d turn * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turn_42d_jerk_v046_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 189d turn * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turn_189d_jerk_v047_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 378d turn * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_turn_378d_jerk_v048_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets), 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d sppe * closeadj, 5d
def f06cup_f06_capacity_utilization_proxy_sppe_5d_jerk_v049_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 10d sppe * closeadj, 10d
def f06cup_f06_capacity_utilization_proxy_sppe_10d_jerk_v050_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 42d sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppe_42d_jerk_v051_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 189d sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppe_189d_jerk_v052_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 378d sppe * closeadj, 126d
def f06cup_f06_capacity_utilization_proxy_sppe_378d_jerk_v053_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet), 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d EMA turn * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnema_21d_jerk_v054_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d EMA turn * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnema_63d_jerk_v055_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d EMA turn * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turnema_252d_jerk_v056_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d EMA sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppeema_21d_jerk_v057_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d EMA sppe * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppeema_63d_jerk_v058_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d EMA sppe * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppeema_252d_jerk_v059_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21v252 turn gap * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turngap_21v252_jerk_v060_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63v252 turn gap * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turngap_63v252_jerk_v061_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63v504 turn gap * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turngap_63v504_jerk_v062_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126v504 turn gap * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turngap_126v504_jerk_v063_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 126) - _mean(b, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21v252 sppe gap * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppegap_21v252_jerk_v064_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63v252 sppe gap * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_sppegap_63v252_jerk_v065_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63v504 sppe gap * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppegap_63v504_jerk_v066_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126v504 sppe gap * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_sppegap_126v504_jerk_v067_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(b, 126) - _mean(b, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz_x_sppe 21d, 21d
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_21d_jerk_v068_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_util_z(revenue, assets, 21) * _f06_sales_per_ppe(revenue, ppnenet) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz_x_sppe 63d, 21d
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_63d_jerk_v069_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_util_z(revenue, assets, 63) * _f06_sales_per_ppe(revenue, ppnenet) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz_x_sppe 252d, 63d
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_252d_jerk_v070_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_util_z(revenue, assets, 252) * _f06_sales_per_ppe(revenue, ppnenet) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz_x_sppe 504d, 126d
def f06cup_f06_capacity_utilization_proxy_utilzxsppe_504d_jerk_v071_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_util_z(revenue, assets, 504) * _f06_sales_per_ppe(revenue, ppnenet) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnratio 21v252 * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnratio_21v252_jerk_v072_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnratio 63v252 * closeadj, 21d
def f06cup_f06_capacity_utilization_proxy_turnratio_63v252_jerk_v073_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnratio 63v504 * closeadj, 63d
def f06cup_f06_capacity_utilization_proxy_turnratio_63v504_jerk_v074_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnminussppe 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnminussppe_21d_jerk_v075_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 21) - _mean(b, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnminussppe 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnminussppe_63d_jerk_v076_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 63) - _mean(b, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnminussppe 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnminussppe_252d_jerk_v077_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 252) - _mean(b, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnxsppe 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnxsppe_21d_jerk_v078_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = _mean(a * b, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnxsppe 63d, 63d
def f06cup_f06_capacity_utilization_proxy_turnxsppe_63d_jerk_v079_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = _mean(a * b, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnxsppe 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnxsppe_252d_jerk_v080_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = _mean(a * b, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn x revenue 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnxrev_21d_jerk_v081_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets) * revenue, 21) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn x revenue 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnxrev_63d_jerk_v082_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets) * revenue, 63) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn x revenue 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnxrev_252d_jerk_v083_signal(revenue, assets, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets) * revenue, 252) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe x revenue 21d, 21d
def f06cup_f06_capacity_utilization_proxy_sppexrev_21d_jerk_v084_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet) * revenue, 21) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe x revenue 63d, 21d
def f06cup_f06_capacity_utilization_proxy_sppexrev_63d_jerk_v085_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet) * revenue, 63) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe x revenue 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppexrev_252d_jerk_v086_signal(revenue, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet) * revenue, 252) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tovsppe ratio 21d, 21d
def f06cup_f06_capacity_utilization_proxy_tovsppe_21d_jerk_v087_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 21) / _mean(b, 21).replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tovsppe ratio 63d, 21d
def f06cup_f06_capacity_utilization_proxy_tovsppe_63d_jerk_v088_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 63) / _mean(b, 63).replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tovsppe ratio 252d, 63d
def f06cup_f06_capacity_utilization_proxy_tovsppe_252d_jerk_v089_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 252) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z x revenue 63d, 21d
def f06cup_f06_capacity_utilization_proxy_utilzxrev_63d_jerk_v090_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 63) * revenue * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z x revenue 252d, 63d
def f06cup_f06_capacity_utilization_proxy_utilzxrev_252d_jerk_v091_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 252) * revenue * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z x ppnenet 63d, 21d
def f06cup_f06_capacity_utilization_proxy_utilzxppe_63d_jerk_v092_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_util_z(revenue, assets, 63) * ppnenet * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z x ppnenet 252d, 63d
def f06cup_f06_capacity_utilization_proxy_utilzxppe_252d_jerk_v093_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_util_z(revenue, assets, 252) * ppnenet * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn x ppnenet 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnxppe_63d_jerk_v094_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets) * ppnenet, 63) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn x ppnenet 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnxppe_252d_jerk_v095_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets) * ppnenet, 252) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe x assets 63d, 21d
def f06cup_f06_capacity_utilization_proxy_sppexassets_63d_jerk_v096_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet) * assets, 63) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe x assets 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppexassets_252d_jerk_v097_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet) * assets, 252) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 5d, 5d
def f06cup_f06_capacity_utilization_proxy_utilz_5d_jerk_v098_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 10d, 10d
def f06cup_f06_capacity_utilization_proxy_utilz_10d_jerk_v099_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 21d, 21d
def f06cup_f06_capacity_utilization_proxy_utilz_21d_jerk_v100_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 42d, 21d
def f06cup_f06_capacity_utilization_proxy_utilz_42d_jerk_v101_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 189d, 63d
def f06cup_f06_capacity_utilization_proxy_utilz_189d_jerk_v102_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 378d, 126d
def f06cup_f06_capacity_utilization_proxy_utilz_378d_jerk_v103_signal(revenue, assets, closeadj):
    base = _f06_util_z(revenue, assets, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn max 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnmax_21d_jerk_v104_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(21, min_periods=5).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn max 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnmax_63d_jerk_v105_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn max 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnmax_252d_jerk_v106_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn max 504d, 126d
def f06cup_f06_capacity_utilization_proxy_turnmax_504d_jerk_v107_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(504, min_periods=126).max() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn min 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnmin_21d_jerk_v108_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(21, min_periods=5).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn min 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnmin_63d_jerk_v109_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn min 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnmin_252d_jerk_v110_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = b.rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe max 63d, 21d
def f06cup_f06_capacity_utilization_proxy_sppemax_63d_jerk_v111_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = b.rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe max 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppemax_252d_jerk_v112_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = b.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe max 504d, 126d
def f06cup_f06_capacity_utilization_proxy_sppemax_504d_jerk_v113_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = b.rolling(504, min_periods=126).max() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn range 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnrng_21d_jerk_v114_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    rng = b.rolling(21, min_periods=5).max() - b.rolling(21, min_periods=5).min()
    base = rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn range 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnrng_63d_jerk_v115_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    rng = b.rolling(63, min_periods=21).max() - b.rolling(63, min_periods=21).min()
    base = rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn range 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnrng_252d_jerk_v116_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnpct 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnpct_63d_jerk_v117_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    mx = b.rolling(63, min_periods=21).max()
    mn = b.rolling(63, min_periods=21).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnpct 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnpct_252d_jerk_v118_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turnpct 504d, 126d
def f06cup_f06_capacity_utilization_proxy_turnpct_504d_jerk_v119_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppepct 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppepct_252d_jerk_v120_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilpress 63d, 21d
def f06cup_f06_capacity_utilization_proxy_utilpress_63d_jerk_v121_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    mx = b.rolling(63, min_periods=21).max()
    mn = b.rolling(63, min_periods=21).min()
    rng = (mx - mn).replace(0, np.nan)
    pct = (b - mn) / rng
    z = _f06_util_z(revenue, assets, 63)
    base = (z + pct) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilpress 252d, 63d
def f06cup_f06_capacity_utilization_proxy_utilpress_252d_jerk_v122_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    pct = (b - mn) / rng
    z = _f06_util_z(revenue, assets, 252)
    base = (z + pct) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilpress 504d, 126d
def f06cup_f06_capacity_utilization_proxy_utilpress_504d_jerk_v123_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    pct = (b - mn) / rng
    z = _f06_util_z(revenue, assets, 504)
    base = (z + pct) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt turn 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnsqrt_63d_jerk_v124_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets).abs()
    base = np.sqrt(_mean(b, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt turn 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnsqrt_252d_jerk_v125_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt sppe 63d, 21d
def f06cup_f06_capacity_utilization_proxy_sppesqrt_63d_jerk_v126_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet).abs()
    base = np.sqrt(_mean(b, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt sppe 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppesqrt_252d_jerk_v127_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn CV 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turncv_21d_jerk_v128_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    cv = _std(b, 21) / _mean(b, 21).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn CV 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turncv_63d_jerk_v129_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn CV 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turncv_252d_jerk_v130_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe CV 63d, 21d
def f06cup_f06_capacity_utilization_proxy_sppecv_63d_jerk_v131_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe CV 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppecv_252d_jerk_v132_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz x cret 63d, 21d
def f06cup_f06_capacity_utilization_proxy_utilzxcret_63d_jerk_v133_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    cret = closeadj.pct_change(63)
    base = z * cret * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz x cret 252d, 63d
def f06cup_f06_capacity_utilization_proxy_utilzxcret_252d_jerk_v134_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    cret = closeadj.pct_change(252)
    base = z * cret * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite (turn+sppe) 252d, 63d
def f06cup_f06_capacity_utilization_proxy_composite_252d_jerk_v135_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(a, 252) + _mean(b, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn x ppnenet 21d, 21d
def f06cup_f06_capacity_utilization_proxy_turnxppe_21d_jerk_v136_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f06_asset_turnover_proxy(revenue, assets) * ppnenet, 21) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe x assets 21d, 21d
def f06cup_f06_capacity_utilization_proxy_sppexassets_21d_jerk_v137_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f06_sales_per_ppe(revenue, ppnenet) * assets, 21) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn log 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnlog_63d_jerk_v138_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = np.log(_mean(b, 63).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sppe log 252d, 63d
def f06cup_f06_capacity_utilization_proxy_sppelog_252d_jerk_v139_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz sq 63d, 21d
def f06cup_f06_capacity_utilization_proxy_utilzsq_63d_jerk_v140_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    base = z * z.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of utilz sq 252d, 63d
def f06cup_f06_capacity_utilization_proxy_utilzsq_252d_jerk_v141_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    base = z * z.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z * sppe gap (21v252)
def f06cup_f06_capacity_utilization_proxy_utilzxsppegap_63d_jerk_v142_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    gap = _mean(b, 21) - _mean(b, 252)
    base = z * gap * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z * sppe gap (63v252) 252d
def f06cup_f06_capacity_utilization_proxy_utilzxsppegap_252d_jerk_v143_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    gap = _mean(b, 63) - _mean(b, 252)
    base = z * gap * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn moving + sppe weight 63d, 21d
def f06cup_f06_capacity_utilization_proxy_turnsppwt_63d_jerk_v144_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (0.5 * _mean(a, 63) + 0.5 * _mean(b, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of turn-sppe weight 252d, 63d
def f06cup_f06_capacity_utilization_proxy_turnsppwt_252d_jerk_v145_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (0.5 * _mean(a, 252) + 0.5 * _mean(b, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 63d vs util_z 252d diff
def f06cup_f06_capacity_utilization_proxy_utilzdiff_63m252_jerk_v146_signal(revenue, assets, closeadj):
    base = (_f06_util_z(revenue, assets, 63) - _f06_util_z(revenue, assets, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of util_z 252d vs util_z 504d diff
def f06cup_f06_capacity_utilization_proxy_utilzdiff_252m504_jerk_v147_signal(revenue, assets, closeadj):
    base = (_f06_util_z(revenue, assets, 252) - _f06_util_z(revenue, assets, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of long-term sppe ratio 252v504
def f06cup_f06_capacity_utilization_proxy_sppertio_252v504_jerk_v148_signal(revenue, ppnenet, closeadj):
    b = _f06_sales_per_ppe(revenue, ppnenet)
    base = (_mean(b, 252) / _mean(b, 504).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of long-term turn ratio 252v504
def f06cup_f06_capacity_utilization_proxy_turnratio_252v504_jerk_v149_signal(revenue, assets, closeadj):
    b = _f06_asset_turnover_proxy(revenue, assets)
    base = (_mean(b, 252) / _mean(b, 504).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of total utilization composite 504d, 126d
def f06cup_f06_capacity_utilization_proxy_compositeall_504d_jerk_v150_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    z = _f06_util_z(revenue, assets, 252)
    base = (_mean(a, 504) + _mean(b, 504) + z) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06cup_f06_capacity_utilization_proxy_turn_21d_jerk_v001_signal,
    f06cup_f06_capacity_utilization_proxy_turn_21d_jerk_v002_signal,
    f06cup_f06_capacity_utilization_proxy_turn_63d_jerk_v003_signal,
    f06cup_f06_capacity_utilization_proxy_turn_63d_jerk_v004_signal,
    f06cup_f06_capacity_utilization_proxy_turn_126d_jerk_v005_signal,
    f06cup_f06_capacity_utilization_proxy_turn_126d_jerk_v006_signal,
    f06cup_f06_capacity_utilization_proxy_turn_252d_jerk_v007_signal,
    f06cup_f06_capacity_utilization_proxy_turn_252d_jerk_v008_signal,
    f06cup_f06_capacity_utilization_proxy_turn_504d_jerk_v009_signal,
    f06cup_f06_capacity_utilization_proxy_turn_504d_jerk_v010_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_21d_jerk_v011_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_21d_jerk_v012_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_63d_jerk_v013_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_63d_jerk_v014_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_126d_jerk_v015_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_126d_jerk_v016_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_252d_jerk_v017_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_252d_jerk_v018_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_504d_jerk_v019_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_504d_jerk_v020_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_63d_jerk_v021_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_63d_jerk_v022_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_126d_jerk_v023_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_252d_jerk_v024_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_252d_jerk_v025_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_504d_jerk_v026_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_504d_jerk_v027_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_21d_jerk_v028_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_63d_jerk_v029_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_252d_jerk_v030_signal,
    f06cup_f06_capacity_utilization_proxy_turnstd_504d_jerk_v031_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_21d_jerk_v032_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_63d_jerk_v033_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_252d_jerk_v034_signal,
    f06cup_f06_capacity_utilization_proxy_sppestd_504d_jerk_v035_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_21d_jerk_v036_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_63d_jerk_v037_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_252d_jerk_v038_signal,
    f06cup_f06_capacity_utilization_proxy_turnz_504d_jerk_v039_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_21d_jerk_v040_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_63d_jerk_v041_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_252d_jerk_v042_signal,
    f06cup_f06_capacity_utilization_proxy_sppez_504d_jerk_v043_signal,
    f06cup_f06_capacity_utilization_proxy_turn_5d_jerk_v044_signal,
    f06cup_f06_capacity_utilization_proxy_turn_10d_jerk_v045_signal,
    f06cup_f06_capacity_utilization_proxy_turn_42d_jerk_v046_signal,
    f06cup_f06_capacity_utilization_proxy_turn_189d_jerk_v047_signal,
    f06cup_f06_capacity_utilization_proxy_turn_378d_jerk_v048_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_5d_jerk_v049_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_10d_jerk_v050_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_42d_jerk_v051_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_189d_jerk_v052_signal,
    f06cup_f06_capacity_utilization_proxy_sppe_378d_jerk_v053_signal,
    f06cup_f06_capacity_utilization_proxy_turnema_21d_jerk_v054_signal,
    f06cup_f06_capacity_utilization_proxy_turnema_63d_jerk_v055_signal,
    f06cup_f06_capacity_utilization_proxy_turnema_252d_jerk_v056_signal,
    f06cup_f06_capacity_utilization_proxy_sppeema_21d_jerk_v057_signal,
    f06cup_f06_capacity_utilization_proxy_sppeema_63d_jerk_v058_signal,
    f06cup_f06_capacity_utilization_proxy_sppeema_252d_jerk_v059_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_21v252_jerk_v060_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_63v252_jerk_v061_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_63v504_jerk_v062_signal,
    f06cup_f06_capacity_utilization_proxy_turngap_126v504_jerk_v063_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_21v252_jerk_v064_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_63v252_jerk_v065_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_63v504_jerk_v066_signal,
    f06cup_f06_capacity_utilization_proxy_sppegap_126v504_jerk_v067_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_21d_jerk_v068_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_63d_jerk_v069_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_252d_jerk_v070_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppe_504d_jerk_v071_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_21v252_jerk_v072_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_63v252_jerk_v073_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_63v504_jerk_v074_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_21d_jerk_v075_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_63d_jerk_v076_signal,
    f06cup_f06_capacity_utilization_proxy_turnminussppe_252d_jerk_v077_signal,
    f06cup_f06_capacity_utilization_proxy_turnxsppe_21d_jerk_v078_signal,
    f06cup_f06_capacity_utilization_proxy_turnxsppe_63d_jerk_v079_signal,
    f06cup_f06_capacity_utilization_proxy_turnxsppe_252d_jerk_v080_signal,
    f06cup_f06_capacity_utilization_proxy_turnxrev_21d_jerk_v081_signal,
    f06cup_f06_capacity_utilization_proxy_turnxrev_63d_jerk_v082_signal,
    f06cup_f06_capacity_utilization_proxy_turnxrev_252d_jerk_v083_signal,
    f06cup_f06_capacity_utilization_proxy_sppexrev_21d_jerk_v084_signal,
    f06cup_f06_capacity_utilization_proxy_sppexrev_63d_jerk_v085_signal,
    f06cup_f06_capacity_utilization_proxy_sppexrev_252d_jerk_v086_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_21d_jerk_v087_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_63d_jerk_v088_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_252d_jerk_v089_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxrev_63d_jerk_v090_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxrev_252d_jerk_v091_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxppe_63d_jerk_v092_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxppe_252d_jerk_v093_signal,
    f06cup_f06_capacity_utilization_proxy_turnxppe_63d_jerk_v094_signal,
    f06cup_f06_capacity_utilization_proxy_turnxppe_252d_jerk_v095_signal,
    f06cup_f06_capacity_utilization_proxy_sppexassets_63d_jerk_v096_signal,
    f06cup_f06_capacity_utilization_proxy_sppexassets_252d_jerk_v097_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_5d_jerk_v098_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_10d_jerk_v099_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_21d_jerk_v100_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_42d_jerk_v101_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_189d_jerk_v102_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_378d_jerk_v103_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_21d_jerk_v104_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_63d_jerk_v105_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_252d_jerk_v106_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_504d_jerk_v107_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_21d_jerk_v108_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_63d_jerk_v109_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_252d_jerk_v110_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_63d_jerk_v111_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_252d_jerk_v112_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_504d_jerk_v113_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_21d_jerk_v114_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_63d_jerk_v115_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_252d_jerk_v116_signal,
    f06cup_f06_capacity_utilization_proxy_turnpct_63d_jerk_v117_signal,
    f06cup_f06_capacity_utilization_proxy_turnpct_252d_jerk_v118_signal,
    f06cup_f06_capacity_utilization_proxy_turnpct_504d_jerk_v119_signal,
    f06cup_f06_capacity_utilization_proxy_sppepct_252d_jerk_v120_signal,
    f06cup_f06_capacity_utilization_proxy_utilpress_63d_jerk_v121_signal,
    f06cup_f06_capacity_utilization_proxy_utilpress_252d_jerk_v122_signal,
    f06cup_f06_capacity_utilization_proxy_utilpress_504d_jerk_v123_signal,
    f06cup_f06_capacity_utilization_proxy_turnsqrt_63d_jerk_v124_signal,
    f06cup_f06_capacity_utilization_proxy_turnsqrt_252d_jerk_v125_signal,
    f06cup_f06_capacity_utilization_proxy_sppesqrt_63d_jerk_v126_signal,
    f06cup_f06_capacity_utilization_proxy_sppesqrt_252d_jerk_v127_signal,
    f06cup_f06_capacity_utilization_proxy_turncv_21d_jerk_v128_signal,
    f06cup_f06_capacity_utilization_proxy_turncv_63d_jerk_v129_signal,
    f06cup_f06_capacity_utilization_proxy_turncv_252d_jerk_v130_signal,
    f06cup_f06_capacity_utilization_proxy_sppecv_63d_jerk_v131_signal,
    f06cup_f06_capacity_utilization_proxy_sppecv_252d_jerk_v132_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxcret_63d_jerk_v133_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxcret_252d_jerk_v134_signal,
    f06cup_f06_capacity_utilization_proxy_composite_252d_jerk_v135_signal,
    f06cup_f06_capacity_utilization_proxy_turnxppe_21d_jerk_v136_signal,
    f06cup_f06_capacity_utilization_proxy_sppexassets_21d_jerk_v137_signal,
    f06cup_f06_capacity_utilization_proxy_turnlog_63d_jerk_v138_signal,
    f06cup_f06_capacity_utilization_proxy_sppelog_252d_jerk_v139_signal,
    f06cup_f06_capacity_utilization_proxy_utilzsq_63d_jerk_v140_signal,
    f06cup_f06_capacity_utilization_proxy_utilzsq_252d_jerk_v141_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppegap_63d_jerk_v142_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxsppegap_252d_jerk_v143_signal,
    f06cup_f06_capacity_utilization_proxy_turnsppwt_63d_jerk_v144_signal,
    f06cup_f06_capacity_utilization_proxy_turnsppwt_252d_jerk_v145_signal,
    f06cup_f06_capacity_utilization_proxy_utilzdiff_63m252_jerk_v146_signal,
    f06cup_f06_capacity_utilization_proxy_utilzdiff_252m504_jerk_v147_signal,
    f06cup_f06_capacity_utilization_proxy_sppertio_252v504_jerk_v148_signal,
    f06cup_f06_capacity_utilization_proxy_turnratio_252v504_jerk_v149_signal,
    f06cup_f06_capacity_utilization_proxy_compositeall_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_CAPACITY_UTILIZATION_PROXY_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f06_capacity_utilization_proxy_3rd_derivatives_001_150_claude: {n_features} features pass")
