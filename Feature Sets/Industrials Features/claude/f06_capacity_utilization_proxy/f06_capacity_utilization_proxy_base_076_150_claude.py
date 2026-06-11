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


# 21d turnover * volume-proxy (closeadj^2)
def f06cup_f06_capacity_utilization_proxy_turnxprice_21d_base_v076_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover * close^2
def f06cup_f06_capacity_utilization_proxy_turnxprice_63d_base_v077_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover * close^2
def f06cup_f06_capacity_utilization_proxy_turnxprice_252d_base_v078_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sppe * close^2
def f06cup_f06_capacity_utilization_proxy_sppexprice_21d_base_v079_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe * close^2
def f06cup_f06_capacity_utilization_proxy_sppexprice_63d_base_v080_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sppe * close^2
def f06cup_f06_capacity_utilization_proxy_sppexprice_252d_base_v081_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover * revenue
def f06cup_f06_capacity_utilization_proxy_turnxrev_21d_base_v082_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base * revenue, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover * revenue
def f06cup_f06_capacity_utilization_proxy_turnxrev_63d_base_v083_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base * revenue, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover * revenue
def f06cup_f06_capacity_utilization_proxy_turnxrev_252d_base_v084_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base * revenue, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sppe * revenue
def f06cup_f06_capacity_utilization_proxy_sppexrev_21d_base_v085_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base * revenue, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe * revenue
def f06cup_f06_capacity_utilization_proxy_sppexrev_63d_base_v086_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base * revenue, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sppe * revenue
def f06cup_f06_capacity_utilization_proxy_sppexrev_252d_base_v087_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base * revenue, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover / sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_tovsppe_21d_base_v088_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 21) / _mean(b, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover / sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_tovsppe_63d_base_v089_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 63) / _mean(b, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover / sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_tovsppe_252d_base_v090_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 252) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d turnover / sppe ratio * closeadj
def f06cup_f06_capacity_utilization_proxy_tovsppe_504d_base_v091_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 504) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d util z * revenue
def f06cup_f06_capacity_utilization_proxy_utilzxrev_21d_base_v092_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 21)
    result = z * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d util z * revenue
def f06cup_f06_capacity_utilization_proxy_utilzxrev_63d_base_v093_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    result = z * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d util z * revenue
def f06cup_f06_capacity_utilization_proxy_utilzxrev_252d_base_v094_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    result = z * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d util z * revenue
def f06cup_f06_capacity_utilization_proxy_utilzxrev_504d_base_v095_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 504)
    result = z * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d util z * ppnenet
def f06cup_f06_capacity_utilization_proxy_utilzxppe_63d_base_v096_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    result = z * ppnenet * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d util z * ppnenet
def f06cup_f06_capacity_utilization_proxy_utilzxppe_252d_base_v097_signal(revenue, assets, ppnenet, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    result = z * ppnenet * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover * ppnenet (capacity dollar use)
def f06cup_f06_capacity_utilization_proxy_turnxppe_21d_base_v098_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base * ppnenet, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover * ppnenet
def f06cup_f06_capacity_utilization_proxy_turnxppe_63d_base_v099_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base * ppnenet, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover * ppnenet
def f06cup_f06_capacity_utilization_proxy_turnxppe_252d_base_v100_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = _mean(base * ppnenet, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sppe * assets
def f06cup_f06_capacity_utilization_proxy_sppexassets_21d_base_v101_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base * assets, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe * assets
def f06cup_f06_capacity_utilization_proxy_sppexassets_63d_base_v102_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base * assets, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sppe * assets
def f06cup_f06_capacity_utilization_proxy_sppexassets_252d_base_v103_signal(revenue, assets, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = _mean(base * assets, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 5d util z
def f06cup_f06_capacity_utilization_proxy_utilz_5d_base_v104_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d util z
def f06cup_f06_capacity_utilization_proxy_utilz_10d_base_v105_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d util z
def f06cup_f06_capacity_utilization_proxy_utilz_21d_base_v106_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d util z
def f06cup_f06_capacity_utilization_proxy_utilz_42d_base_v107_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d util z
def f06cup_f06_capacity_utilization_proxy_utilz_189d_base_v108_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d util z
def f06cup_f06_capacity_utilization_proxy_utilz_378d_base_v109_signal(revenue, assets, closeadj):
    result = _f06_util_z(revenue, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmax_21d_base_v110_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmax_63d_base_v111_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmax_252d_base_v112_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmax_504d_base_v113_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmin_21d_base_v114_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(21, min_periods=5).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmin_63d_base_v115_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmin_252d_base_v116_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnmin_504d_base_v117_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    result = base.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppemax_21d_base_v118_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppemax_63d_base_v119_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppemax_252d_base_v120_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppemax_504d_base_v121_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range turnover (max - min) * closeadj
def f06cup_f06_capacity_utilization_proxy_turnrng_21d_base_v122_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    rng = base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range turnover
def f06cup_f06_capacity_utilization_proxy_turnrng_63d_base_v123_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    rng = base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range turnover
def f06cup_f06_capacity_utilization_proxy_turnrng_252d_base_v124_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range turnover
def f06cup_f06_capacity_utilization_proxy_turnrng_504d_base_v125_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    rng = base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover percentile (close-to-current-high band) * closeadj
def f06cup_f06_capacity_utilization_proxy_turnpct_63d_base_v126_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    mx = base.rolling(63, min_periods=21).max()
    mn = base.rolling(63, min_periods=21).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover percentile * closeadj
def f06cup_f06_capacity_utilization_proxy_turnpct_252d_base_v127_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    mx = base.rolling(252, min_periods=63).max()
    mn = base.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d turnover percentile * closeadj
def f06cup_f06_capacity_utilization_proxy_turnpct_504d_base_v128_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    mx = base.rolling(504, min_periods=126).max()
    mn = base.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sppe percentile * closeadj
def f06cup_f06_capacity_utilization_proxy_sppepct_252d_base_v129_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    mx = base.rolling(252, min_periods=63).max()
    mn = base.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sppe percentile * closeadj
def f06cup_f06_capacity_utilization_proxy_sppepct_504d_base_v130_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    mx = base.rolling(504, min_periods=126).max()
    mn = base.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite util pressure = util_z + turnpct, 63d
def f06cup_f06_capacity_utilization_proxy_utilpress_63d_base_v131_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    mx = base.rolling(63, min_periods=21).max()
    mn = base.rolling(63, min_periods=21).min()
    rng = (mx - mn).replace(0, np.nan)
    pct = (base - mn) / rng
    z = _f06_util_z(revenue, assets, 63)
    result = (z + pct) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite util pressure 252d
def f06cup_f06_capacity_utilization_proxy_utilpress_252d_base_v132_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    mx = base.rolling(252, min_periods=63).max()
    mn = base.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    pct = (base - mn) / rng
    z = _f06_util_z(revenue, assets, 252)
    result = (z + pct) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite util pressure 504d
def f06cup_f06_capacity_utilization_proxy_utilpress_504d_base_v133_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    mx = base.rolling(504, min_periods=126).max()
    mn = base.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    pct = (base - mn) / rng
    z = _f06_util_z(revenue, assets, 504)
    result = (z + pct) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnsqrt_21d_base_v134_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets).abs()
    result = np.sqrt(_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnsqrt_63d_base_v135_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets).abs()
    result = np.sqrt(_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt turnover * closeadj
def f06cup_f06_capacity_utilization_proxy_turnsqrt_252d_base_v136_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets).abs()
    result = np.sqrt(_mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppesqrt_21d_base_v137_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet).abs()
    result = np.sqrt(_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppesqrt_63d_base_v138_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet).abs()
    result = np.sqrt(_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt sppe * closeadj
def f06cup_f06_capacity_utilization_proxy_sppesqrt_252d_base_v139_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet).abs()
    result = np.sqrt(_mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover sign * closeadj * abs std proxy
def f06cup_f06_capacity_utilization_proxy_turnsign_21d_base_v140_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    deviation = base - _mean(base, 252)
    result = np.sign(deviation) * _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover sign * closeadj
def f06cup_f06_capacity_utilization_proxy_turnsign_63d_base_v141_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    deviation = base - _mean(base, 504)
    result = np.sign(deviation) * _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover std / mean (coefficient of variation) * closeadj
def f06cup_f06_capacity_utilization_proxy_turncv_21d_base_v142_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    cv = _std(base, 21) / _mean(base, 21).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover CV * closeadj
def f06cup_f06_capacity_utilization_proxy_turncv_63d_base_v143_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    cv = _std(base, 63) / _mean(base, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover CV * closeadj
def f06cup_f06_capacity_utilization_proxy_turncv_252d_base_v144_signal(revenue, assets, closeadj):
    base = _f06_asset_turnover_proxy(revenue, assets)
    cv = _std(base, 252) / _mean(base, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sppe CV * closeadj
def f06cup_f06_capacity_utilization_proxy_sppecv_63d_base_v145_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    cv = _std(base, 63) / _mean(base, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sppe CV * closeadj
def f06cup_f06_capacity_utilization_proxy_sppecv_252d_base_v146_signal(revenue, ppnenet, closeadj):
    base = _f06_sales_per_ppe(revenue, ppnenet)
    cv = _std(base, 252) / _mean(base, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d util_z * close diff
def f06cup_f06_capacity_utilization_proxy_utilzxcret_21d_base_v147_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 21)
    cret = closeadj.pct_change(21)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d util_z * close return
def f06cup_f06_capacity_utilization_proxy_utilzxcret_63d_base_v148_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 63)
    cret = closeadj.pct_change(63)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d util_z * close return
def f06cup_f06_capacity_utilization_proxy_utilzxcret_252d_base_v149_signal(revenue, assets, closeadj):
    z = _f06_util_z(revenue, assets, 252)
    cret = closeadj.pct_change(252)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite (turn + sppe) mean * closeadj
def f06cup_f06_capacity_utilization_proxy_composite_252d_base_v150_signal(revenue, assets, ppnenet, closeadj):
    a = _f06_asset_turnover_proxy(revenue, assets)
    b = _f06_sales_per_ppe(revenue, ppnenet)
    result = (_mean(a, 252) + _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06cup_f06_capacity_utilization_proxy_turnxprice_21d_base_v076_signal,
    f06cup_f06_capacity_utilization_proxy_turnxprice_63d_base_v077_signal,
    f06cup_f06_capacity_utilization_proxy_turnxprice_252d_base_v078_signal,
    f06cup_f06_capacity_utilization_proxy_sppexprice_21d_base_v079_signal,
    f06cup_f06_capacity_utilization_proxy_sppexprice_63d_base_v080_signal,
    f06cup_f06_capacity_utilization_proxy_sppexprice_252d_base_v081_signal,
    f06cup_f06_capacity_utilization_proxy_turnxrev_21d_base_v082_signal,
    f06cup_f06_capacity_utilization_proxy_turnxrev_63d_base_v083_signal,
    f06cup_f06_capacity_utilization_proxy_turnxrev_252d_base_v084_signal,
    f06cup_f06_capacity_utilization_proxy_sppexrev_21d_base_v085_signal,
    f06cup_f06_capacity_utilization_proxy_sppexrev_63d_base_v086_signal,
    f06cup_f06_capacity_utilization_proxy_sppexrev_252d_base_v087_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_21d_base_v088_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_63d_base_v089_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_252d_base_v090_signal,
    f06cup_f06_capacity_utilization_proxy_tovsppe_504d_base_v091_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxrev_21d_base_v092_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxrev_63d_base_v093_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxrev_252d_base_v094_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxrev_504d_base_v095_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxppe_63d_base_v096_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxppe_252d_base_v097_signal,
    f06cup_f06_capacity_utilization_proxy_turnxppe_21d_base_v098_signal,
    f06cup_f06_capacity_utilization_proxy_turnxppe_63d_base_v099_signal,
    f06cup_f06_capacity_utilization_proxy_turnxppe_252d_base_v100_signal,
    f06cup_f06_capacity_utilization_proxy_sppexassets_21d_base_v101_signal,
    f06cup_f06_capacity_utilization_proxy_sppexassets_63d_base_v102_signal,
    f06cup_f06_capacity_utilization_proxy_sppexassets_252d_base_v103_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_5d_base_v104_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_10d_base_v105_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_21d_base_v106_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_42d_base_v107_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_189d_base_v108_signal,
    f06cup_f06_capacity_utilization_proxy_utilz_378d_base_v109_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_21d_base_v110_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_63d_base_v111_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_252d_base_v112_signal,
    f06cup_f06_capacity_utilization_proxy_turnmax_504d_base_v113_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_21d_base_v114_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_63d_base_v115_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_252d_base_v116_signal,
    f06cup_f06_capacity_utilization_proxy_turnmin_504d_base_v117_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_21d_base_v118_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_63d_base_v119_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_252d_base_v120_signal,
    f06cup_f06_capacity_utilization_proxy_sppemax_504d_base_v121_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_21d_base_v122_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_63d_base_v123_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_252d_base_v124_signal,
    f06cup_f06_capacity_utilization_proxy_turnrng_504d_base_v125_signal,
    f06cup_f06_capacity_utilization_proxy_turnpct_63d_base_v126_signal,
    f06cup_f06_capacity_utilization_proxy_turnpct_252d_base_v127_signal,
    f06cup_f06_capacity_utilization_proxy_turnpct_504d_base_v128_signal,
    f06cup_f06_capacity_utilization_proxy_sppepct_252d_base_v129_signal,
    f06cup_f06_capacity_utilization_proxy_sppepct_504d_base_v130_signal,
    f06cup_f06_capacity_utilization_proxy_utilpress_63d_base_v131_signal,
    f06cup_f06_capacity_utilization_proxy_utilpress_252d_base_v132_signal,
    f06cup_f06_capacity_utilization_proxy_utilpress_504d_base_v133_signal,
    f06cup_f06_capacity_utilization_proxy_turnsqrt_21d_base_v134_signal,
    f06cup_f06_capacity_utilization_proxy_turnsqrt_63d_base_v135_signal,
    f06cup_f06_capacity_utilization_proxy_turnsqrt_252d_base_v136_signal,
    f06cup_f06_capacity_utilization_proxy_sppesqrt_21d_base_v137_signal,
    f06cup_f06_capacity_utilization_proxy_sppesqrt_63d_base_v138_signal,
    f06cup_f06_capacity_utilization_proxy_sppesqrt_252d_base_v139_signal,
    f06cup_f06_capacity_utilization_proxy_turnsign_21d_base_v140_signal,
    f06cup_f06_capacity_utilization_proxy_turnsign_63d_base_v141_signal,
    f06cup_f06_capacity_utilization_proxy_turncv_21d_base_v142_signal,
    f06cup_f06_capacity_utilization_proxy_turncv_63d_base_v143_signal,
    f06cup_f06_capacity_utilization_proxy_turncv_252d_base_v144_signal,
    f06cup_f06_capacity_utilization_proxy_sppecv_63d_base_v145_signal,
    f06cup_f06_capacity_utilization_proxy_sppecv_252d_base_v146_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxcret_21d_base_v147_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxcret_63d_base_v148_signal,
    f06cup_f06_capacity_utilization_proxy_utilzxcret_252d_base_v149_signal,
    f06cup_f06_capacity_utilization_proxy_composite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_CAPACITY_UTILIZATION_PROXY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f06_capacity_utilization_proxy_base_076_150_claude: {n_features} features pass")
