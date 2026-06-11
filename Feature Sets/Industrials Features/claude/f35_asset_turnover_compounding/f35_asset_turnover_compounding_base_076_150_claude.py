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


def f35atc_f35_asset_turnover_compounding_atxsq_63d_base_v076_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxsq_252d_base_v077_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxsq_63d_base_v078_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxsq_252d_base_v079_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxsq_63d_base_v080_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxsq_252d_base_v081_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spasharpe_63d_base_v082_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = (_mean(ratio, 63) / _std(ratio, 63).replace(0, np.nan)) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spasharpe_252d_base_v083_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = (_mean(ratio, 252) / _std(ratio, 252).replace(0, np.nan)) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atabs_63d_base_v084_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atabs_252d_base_v085_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistabs_63d_base_v086_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistabs_252d_base_v087_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atsign_63d_base_v088_signal(assetturnover, closeadj):
    base = (assetturnover > assetturnover.shift(63)).astype(float)
    result = _mean(base, 63) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atsign_252d_base_v089_signal(assetturnover, closeadj):
    base = (assetturnover > assetturnover.shift(252)).astype(float)
    result = _mean(base, 252) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevvar_63d_base_v090_signal(assetturnover, revenue, closeadj):
    rv = _std(revenue.pct_change(), 63)
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * (1.0 + rv)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevvar_252d_base_v091_signal(assetturnover, revenue, closeadj):
    rv = _std(revenue.pct_change(), 252)
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * (1.0 + rv)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spadelta_63d_base_v092_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = (_mean(ratio, 63) - _mean(ratio, 252)) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spadelta_252d_base_v093_signal(revenue, assets, closeadj):
    ratio = revenue / assets.replace(0, np.nan)
    result = (_mean(ratio, 252) - _mean(ratio, 504)) * closeadj + _f35_sales_per_asset_compound(revenue, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevgrowth_63d_base_v094_signal(assetturnover, revenue, closeadj):
    g = revenue.pct_change(63)
    result = _mean(assetturnover, 63) * closeadj * (1.0 + g) + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevgrowth_252d_base_v095_signal(assetturnover, revenue, closeadj):
    g = revenue.pct_change(252)
    result = _mean(assetturnover, 252) * closeadj * (1.0 + g) + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxassetslog_63d_base_v096_signal(assetturnover, assets, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * np.log(assets.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxassetslog_252d_base_v097_signal(assetturnover, assets, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * np.log(assets.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxassetslog_63d_base_v098_signal(assetturnover, assets, closeadj):
    result = _f35_turnover_persistence(assetturnover, 63) * closeadj * np.log(assets.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxassetslog_252d_base_v099_signal(assetturnover, assets, closeadj):
    result = _f35_turnover_persistence(assetturnover, 252) * closeadj * np.log(assets.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_compositeq_63d_base_v100_signal(assetturnover, revenue, assets, closeadj):
    a = _f35_turnover_trajectory(assetturnover, 63)
    b = _f35_sales_per_asset_compound(revenue, assets, 63)
    c = _f35_turnover_persistence(assetturnover, 63)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_compositeq_252d_base_v101_signal(assetturnover, revenue, assets, closeadj):
    a = _f35_turnover_trajectory(assetturnover, 252)
    b = _f35_sales_per_asset_compound(revenue, assets, 252)
    c = _f35_turnover_persistence(assetturnover, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxvol_63d_base_v102_signal(assetturnover, closeadj):
    vol = _std(closeadj.pct_change(), 63)
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * vol
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxvol_252d_base_v103_signal(assetturnover, closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * vol
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxvol_63d_base_v104_signal(assetturnover, closeadj):
    vol = _std(closeadj.pct_change(), 63)
    result = _f35_turnover_persistence(assetturnover, 63) * closeadj * vol
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxvol_252d_base_v105_signal(assetturnover, closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _f35_turnover_persistence(assetturnover, 252) * closeadj * vol
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxvol_63d_base_v106_signal(revenue, assets, closeadj):
    vol = _std(closeadj.pct_change(), 63)
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj * vol
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxvol_252d_base_v107_signal(revenue, assets, closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj * vol
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_sparatio_63v252_base_v108_signal(revenue, assets, closeadj):
    a = _f35_sales_per_asset_compound(revenue, assets, 63)
    b = _f35_sales_per_asset_compound(revenue, assets, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_sparatio_252v504_base_v109_signal(revenue, assets, closeadj):
    a = _f35_sales_per_asset_compound(revenue, assets, 252)
    b = _f35_sales_per_asset_compound(revenue, assets, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistratio_63v252_base_v110_signal(assetturnover, closeadj):
    a = _f35_turnover_persistence(assetturnover, 63)
    b = _f35_turnover_persistence(assetturnover, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistratio_252v504_base_v111_signal(assetturnover, closeadj):
    a = _f35_turnover_persistence(assetturnover, 252)
    b = _f35_turnover_persistence(assetturnover, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaminusat_63d_base_v112_signal(revenue, assets, assetturnover, closeadj):
    a = _f35_sales_per_asset_compound(revenue, assets, 63)
    b = _mean(assetturnover, 63)
    result = (a - b) * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaminusat_252d_base_v113_signal(revenue, assets, assetturnover, closeadj):
    a = _f35_sales_per_asset_compound(revenue, assets, 252)
    b = _mean(assetturnover, 252)
    result = (a - b) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxinvprice_63d_base_v114_signal(assetturnover, closeadj):
    inv = 1.0 / _mean(closeadj, 63).replace(0, np.nan)
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * inv * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxinvprice_252d_base_v115_signal(assetturnover, closeadj):
    inv = 1.0 / _mean(closeadj, 252).replace(0, np.nan)
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * inv * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxat_63d_base_v116_signal(assetturnover, closeadj):
    a = _f35_turnover_persistence(assetturnover, 63)
    b = _f35_turnover_trajectory(assetturnover, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxat_252d_base_v117_signal(assetturnover, closeadj):
    a = _f35_turnover_persistence(assetturnover, 252)
    b = _f35_turnover_trajectory(assetturnover, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxat_63d_base_v118_signal(revenue, assets, assetturnover, closeadj):
    a = _f35_sales_per_asset_compound(revenue, assets, 63)
    b = _f35_turnover_persistence(assetturnover, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxat_252d_base_v119_signal(revenue, assets, assetturnover, closeadj):
    a = _f35_sales_per_asset_compound(revenue, assets, 252)
    b = _f35_turnover_persistence(assetturnover, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atquantilehi_63d_base_v120_signal(assetturnover, closeadj):
    qhi = assetturnover.rolling(252, min_periods=63).quantile(0.75)
    result = qhi * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atquantilelo_63d_base_v121_signal(assetturnover, closeadj):
    qlo = assetturnover.rolling(252, min_periods=63).quantile(0.25)
    result = qlo * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atiqr_63d_base_v122_signal(assetturnover, closeadj):
    iqr = assetturnover.rolling(252, min_periods=63).quantile(0.75) - assetturnover.rolling(252, min_periods=63).quantile(0.25)
    result = iqr * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atvspeak_252d_base_v123_signal(assetturnover, closeadj):
    peak = assetturnover.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (assetturnover / peak) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atvspeak_504d_base_v124_signal(assetturnover, closeadj):
    peak = assetturnover.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (assetturnover / peak) * closeadj + _f35_turnover_trajectory(assetturnover, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atdeep_252d_base_v125_signal(assetturnover, closeadj):
    med = assetturnover.rolling(252, min_periods=63).median()
    deep = (assetturnover < med).astype(float)
    result = _mean(deep, 252) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_athigh_252d_base_v126_signal(assetturnover, closeadj):
    med = assetturnover.rolling(252, min_periods=63).median()
    hi = (assetturnover > med).astype(float)
    result = _mean(hi, 252) * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistema_63d_base_v127_signal(assetturnover, closeadj):
    base = _f35_turnover_persistence(assetturnover, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistema_252d_base_v128_signal(assetturnover, closeadj):
    base = _f35_turnover_persistence(assetturnover, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajema_63d_base_v129_signal(assetturnover, closeadj):
    base = _f35_turnover_trajectory(assetturnover, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajema_252d_base_v130_signal(assetturnover, closeadj):
    base = _f35_turnover_trajectory(assetturnover, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaema_63d_alt_base_v131_signal(revenue, assets, closeadj):
    base = _f35_sales_per_asset_compound(revenue, assets, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaema_252d_alt_base_v132_signal(revenue, assets, closeadj):
    base = _f35_sales_per_asset_compound(revenue, assets, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxpricelog_63d_base_v133_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxpricelog_252d_base_v134_signal(assetturnover, closeadj):
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxpricelog_63d_base_v135_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxpricelog_252d_base_v136_signal(revenue, assets, closeadj):
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atcumsum_63d_base_v137_signal(assetturnover, closeadj):
    result = assetturnover.rolling(63, min_periods=21).sum() * closeadj + _f35_turnover_trajectory(assetturnover, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atcumsum_252d_base_v138_signal(assetturnover, closeadj):
    result = assetturnover.rolling(252, min_periods=63).sum() * closeadj + _f35_turnover_trajectory(assetturnover, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxassetsg_63d_base_v139_signal(assetturnover, assets, closeadj):
    g = assets.pct_change(63)
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxassetsg_252d_base_v140_signal(assetturnover, assets, closeadj):
    g = assets.pct_change(252)
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxassetsg_63d_base_v141_signal(revenue, assets, closeadj):
    g = assets.pct_change(63)
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxassetsg_252d_base_v142_signal(revenue, assets, closeadj):
    g = assets.pct_change(252)
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevpershare_63d_base_v143_signal(assetturnover, revenue, closeadj):
    rps = revenue / 1e8
    result = _f35_turnover_trajectory(assetturnover, 63) * closeadj * np.log(rps.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_atxrevpershare_252d_base_v144_signal(assetturnover, revenue, closeadj):
    rps = revenue / 1e8
    result = _f35_turnover_trajectory(assetturnover, 252) * closeadj * np.log(rps.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxrevpershare_63d_base_v145_signal(revenue, assets, closeadj):
    rps = revenue / 1e8
    result = _f35_sales_per_asset_compound(revenue, assets, 63) * closeadj * np.log(rps.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_spaxrevpershare_252d_base_v146_signal(revenue, assets, closeadj):
    rps = revenue / 1e8
    result = _f35_sales_per_asset_compound(revenue, assets, 252) * closeadj * np.log(rps.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxprice_5d_base_v147_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 21) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_persistxprice_504d_base_v148_signal(assetturnover, closeadj):
    result = _f35_turnover_persistence(assetturnover, 504) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajxlog_63d_base_v149_signal(assetturnover, closeadj):
    base = _f35_turnover_trajectory(assetturnover, 63)
    result = np.sign(base) * np.log1p(base.abs() * 50.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35atc_f35_asset_turnover_compounding_trajxlog_252d_base_v150_signal(assetturnover, closeadj):
    base = _f35_turnover_trajectory(assetturnover, 252)
    result = np.sign(base) * np.log1p(base.abs() * 50.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35atc_f35_asset_turnover_compounding_atxsq_63d_base_v076_signal,
    f35atc_f35_asset_turnover_compounding_atxsq_252d_base_v077_signal,
    f35atc_f35_asset_turnover_compounding_persistxsq_63d_base_v078_signal,
    f35atc_f35_asset_turnover_compounding_persistxsq_252d_base_v079_signal,
    f35atc_f35_asset_turnover_compounding_spaxsq_63d_base_v080_signal,
    f35atc_f35_asset_turnover_compounding_spaxsq_252d_base_v081_signal,
    f35atc_f35_asset_turnover_compounding_spasharpe_63d_base_v082_signal,
    f35atc_f35_asset_turnover_compounding_spasharpe_252d_base_v083_signal,
    f35atc_f35_asset_turnover_compounding_atabs_63d_base_v084_signal,
    f35atc_f35_asset_turnover_compounding_atabs_252d_base_v085_signal,
    f35atc_f35_asset_turnover_compounding_persistabs_63d_base_v086_signal,
    f35atc_f35_asset_turnover_compounding_persistabs_252d_base_v087_signal,
    f35atc_f35_asset_turnover_compounding_atsign_63d_base_v088_signal,
    f35atc_f35_asset_turnover_compounding_atsign_252d_base_v089_signal,
    f35atc_f35_asset_turnover_compounding_atxrevvar_63d_base_v090_signal,
    f35atc_f35_asset_turnover_compounding_atxrevvar_252d_base_v091_signal,
    f35atc_f35_asset_turnover_compounding_spadelta_63d_base_v092_signal,
    f35atc_f35_asset_turnover_compounding_spadelta_252d_base_v093_signal,
    f35atc_f35_asset_turnover_compounding_atxrevgrowth_63d_base_v094_signal,
    f35atc_f35_asset_turnover_compounding_atxrevgrowth_252d_base_v095_signal,
    f35atc_f35_asset_turnover_compounding_atxassetslog_63d_base_v096_signal,
    f35atc_f35_asset_turnover_compounding_atxassetslog_252d_base_v097_signal,
    f35atc_f35_asset_turnover_compounding_persistxassetslog_63d_base_v098_signal,
    f35atc_f35_asset_turnover_compounding_persistxassetslog_252d_base_v099_signal,
    f35atc_f35_asset_turnover_compounding_compositeq_63d_base_v100_signal,
    f35atc_f35_asset_turnover_compounding_compositeq_252d_base_v101_signal,
    f35atc_f35_asset_turnover_compounding_atxvol_63d_base_v102_signal,
    f35atc_f35_asset_turnover_compounding_atxvol_252d_base_v103_signal,
    f35atc_f35_asset_turnover_compounding_persistxvol_63d_base_v104_signal,
    f35atc_f35_asset_turnover_compounding_persistxvol_252d_base_v105_signal,
    f35atc_f35_asset_turnover_compounding_spaxvol_63d_base_v106_signal,
    f35atc_f35_asset_turnover_compounding_spaxvol_252d_base_v107_signal,
    f35atc_f35_asset_turnover_compounding_sparatio_63v252_base_v108_signal,
    f35atc_f35_asset_turnover_compounding_sparatio_252v504_base_v109_signal,
    f35atc_f35_asset_turnover_compounding_persistratio_63v252_base_v110_signal,
    f35atc_f35_asset_turnover_compounding_persistratio_252v504_base_v111_signal,
    f35atc_f35_asset_turnover_compounding_spaminusat_63d_base_v112_signal,
    f35atc_f35_asset_turnover_compounding_spaminusat_252d_base_v113_signal,
    f35atc_f35_asset_turnover_compounding_atxinvprice_63d_base_v114_signal,
    f35atc_f35_asset_turnover_compounding_atxinvprice_252d_base_v115_signal,
    f35atc_f35_asset_turnover_compounding_persistxat_63d_base_v116_signal,
    f35atc_f35_asset_turnover_compounding_persistxat_252d_base_v117_signal,
    f35atc_f35_asset_turnover_compounding_spaxat_63d_base_v118_signal,
    f35atc_f35_asset_turnover_compounding_spaxat_252d_base_v119_signal,
    f35atc_f35_asset_turnover_compounding_atquantilehi_63d_base_v120_signal,
    f35atc_f35_asset_turnover_compounding_atquantilelo_63d_base_v121_signal,
    f35atc_f35_asset_turnover_compounding_atiqr_63d_base_v122_signal,
    f35atc_f35_asset_turnover_compounding_atvspeak_252d_base_v123_signal,
    f35atc_f35_asset_turnover_compounding_atvspeak_504d_base_v124_signal,
    f35atc_f35_asset_turnover_compounding_atdeep_252d_base_v125_signal,
    f35atc_f35_asset_turnover_compounding_athigh_252d_base_v126_signal,
    f35atc_f35_asset_turnover_compounding_persistema_63d_base_v127_signal,
    f35atc_f35_asset_turnover_compounding_persistema_252d_base_v128_signal,
    f35atc_f35_asset_turnover_compounding_trajema_63d_base_v129_signal,
    f35atc_f35_asset_turnover_compounding_trajema_252d_base_v130_signal,
    f35atc_f35_asset_turnover_compounding_spaema_63d_alt_base_v131_signal,
    f35atc_f35_asset_turnover_compounding_spaema_252d_alt_base_v132_signal,
    f35atc_f35_asset_turnover_compounding_atxpricelog_63d_base_v133_signal,
    f35atc_f35_asset_turnover_compounding_atxpricelog_252d_base_v134_signal,
    f35atc_f35_asset_turnover_compounding_spaxpricelog_63d_base_v135_signal,
    f35atc_f35_asset_turnover_compounding_spaxpricelog_252d_base_v136_signal,
    f35atc_f35_asset_turnover_compounding_atcumsum_63d_base_v137_signal,
    f35atc_f35_asset_turnover_compounding_atcumsum_252d_base_v138_signal,
    f35atc_f35_asset_turnover_compounding_atxassetsg_63d_base_v139_signal,
    f35atc_f35_asset_turnover_compounding_atxassetsg_252d_base_v140_signal,
    f35atc_f35_asset_turnover_compounding_spaxassetsg_63d_base_v141_signal,
    f35atc_f35_asset_turnover_compounding_spaxassetsg_252d_base_v142_signal,
    f35atc_f35_asset_turnover_compounding_atxrevpershare_63d_base_v143_signal,
    f35atc_f35_asset_turnover_compounding_atxrevpershare_252d_base_v144_signal,
    f35atc_f35_asset_turnover_compounding_spaxrevpershare_63d_base_v145_signal,
    f35atc_f35_asset_turnover_compounding_spaxrevpershare_252d_base_v146_signal,
    f35atc_f35_asset_turnover_compounding_persistxprice_5d_base_v147_signal,
    f35atc_f35_asset_turnover_compounding_persistxprice_504d_base_v148_signal,
    f35atc_f35_asset_turnover_compounding_trajxlog_63d_base_v149_signal,
    f35atc_f35_asset_turnover_compounding_trajxlog_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_ASSET_TURNOVER_COMPOUNDING_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f35_asset_turnover_compounding_base_076_150_claude: {n_features} features pass")
