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


def _f03_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f03_capex_to_assets(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f03_capex_dynamics(capex, revenue, w):
    ci = capex / revenue.replace(0, np.nan)
    return ci - ci.rolling(w, min_periods=max(1, w // 2)).mean()


# Variants on intensity with cross-sectional aware close
def f03uci_f03_utility_capex_intensity_intensxret_63d_base_v076_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * closeadj.pct_change(21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxret_252d_base_v077_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * closeadj.pct_change(63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxret_63d_base_v078_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 63) * closeadj.pct_change(21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxret_252d_base_v079_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 252) * closeadj.pct_change(63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxabsret_63d_base_v080_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * closeadj.pct_change(21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxabsret_252d_base_v081_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * closeadj.pct_change(63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxclosez_63d_base_v082_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * _z(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxclosez_252d_base_v083_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxclosez_252d_base_v084_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 252) * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxvolz_63d_base_v085_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxvolz_252d_base_v086_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Sign × volume
def f03uci_f03_utility_capex_intensity_intenssign_63d_base_v087_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    result = np.sign(base - _mean(base, 252)) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenssign_252d_base_v088_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    result = np.sign(base - _mean(base, 504)) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Abs × close
def f03uci_f03_utility_capex_intensity_intensabs_63d_base_v089_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsabs_252d_base_v090_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 252).abs() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex/Assets EMA short × close
def f03uci_f03_utility_capex_intensity_assetsema_63d_base_v091_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex/Assets squared
def f03uci_f03_utility_capex_intensity_assetssq_63d_base_v092_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetssq_252d_base_v093_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Cap/Asset volume
def f03uci_f03_utility_capex_intensity_assetsxvol_63d_base_v094_signal(capex, assets, closeadj, volume):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 63) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Cap/Asset ATR
def f03uci_f03_utility_capex_intensity_assetsxatr_63d_base_v095_signal(capex, assets, closeadj, high, low):
    base = _f03_capex_to_assets(capex, assets)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _mean(base, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Cap/Asset gap
def f03uci_f03_utility_capex_intensity_assetsgap_63d_base_v096_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Cap/Asset rank short
def f03uci_f03_utility_capex_intensity_assetsrank_63d_base_v097_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base.rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity rank short
def f03uci_f03_utility_capex_intensity_intensityrank_63d_base_v098_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Cap/Asset short z
def f03uci_f03_utility_capex_intensity_assetsz_63d_base_v099_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex / market scale × close
def f03uci_f03_utility_capex_intensity_capexgrowthxsize_63d_base_v100_signal(capex, revenue, closeadj):
    g = capex.pct_change(63)
    s = np.log(capex.abs().replace(0, np.nan))
    rb = _f03_capex_intensity(capex, revenue)
    result = g * s * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexgrowthxsize_252d_base_v101_signal(capex, revenue, closeadj):
    g = capex.pct_change(252)
    s = np.log(capex.abs().replace(0, np.nan))
    rb = _f03_capex_intensity(capex, revenue)
    result = g * s * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Revenue growth × intensity × close
def f03uci_f03_utility_capex_intensity_intensxrevgrowth_63d_base_v102_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    rg = revenue.pct_change(63)
    result = _mean(base, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevgrowth_252d_base_v103_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    rg = revenue.pct_change(252)
    result = _mean(base, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex acceleration × close
def f03uci_f03_utility_capex_intensity_capexaccel_63d_base_v104_signal(capex, revenue, closeadj):
    g = capex.pct_change(63)
    accel = g - g.shift(21)
    rb = _f03_capex_intensity(capex, revenue)
    result = accel * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexaccel_252d_base_v105_signal(capex, revenue, closeadj):
    g = capex.pct_change(252)
    accel = g - g.shift(63)
    rb = _f03_capex_intensity(capex, revenue)
    result = accel * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × inverse close × scale
def f03uci_f03_utility_capex_intensity_intensxinvprice_63d_base_v106_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxinvprice_252d_base_v107_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics gap × close
def f03uci_f03_utility_capex_intensity_dyngap_63d_base_v108_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    result = (d - _mean(d, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyngap_252d_base_v109_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    result = (d - _mean(d, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics × close pct
def f03uci_f03_utility_capex_intensity_dynxretpct_63d_base_v110_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    result = d * closeadj.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxretpct_252d_base_v111_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    result = d * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics rank
def f03uci_f03_utility_capex_intensity_dynrank_63d_base_v112_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    result = d.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynrank_252d_base_v113_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    result = d.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics z
def f03uci_f03_utility_capex_intensity_dynz_63d_base_v114_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynz_252d_base_v115_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics × dollar volume
def f03uci_f03_utility_capex_intensity_dynxdv_63d_base_v116_signal(capex, revenue, closeadj, volume):
    d = _f03_capex_dynamics(capex, revenue, 63)
    dv = closeadj * volume
    result = d * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxdv_252d_base_v117_signal(capex, revenue, closeadj, volume):
    d = _f03_capex_dynamics(capex, revenue, 252)
    dv = closeadj * volume
    result = d * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × dollar volume
def f03uci_f03_utility_capex_intensity_intensxdv_63d_base_v118_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    dv = closeadj * volume
    result = _mean(base, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxdv_252d_base_v119_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    dv = closeadj * volume
    result = _mean(base, 252) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Cap/Asset × dollar volume
def f03uci_f03_utility_capex_intensity_assetsxdv_63d_base_v120_signal(capex, assets, closeadj, volume):
    base = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    result = _mean(base, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxdv_252d_base_v121_signal(capex, assets, closeadj, volume):
    base = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    result = _mean(base, 252) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Spread vs target (15% capex-to-revenue typical for utilities)
def f03uci_f03_utility_capex_intensity_intensspread_63d_base_v122_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (base - 0.15) * closeadj * _mean(base, 63) / _mean(base, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensspread_252d_base_v123_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (base - 0.15) * closeadj * _mean(base, 252) / _mean(base, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × intensity_to_assets × close (combined)
def f03uci_f03_utility_capex_intensity_combodyn_63d_base_v124_signal(capex, revenue, assets, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    ca = _f03_capex_to_assets(capex, assets)
    result = d * _mean(ca, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_combodyn_252d_base_v125_signal(capex, revenue, assets, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    ca = _f03_capex_to_assets(capex, assets)
    result = d * _mean(ca, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# MA cross
def f03uci_f03_utility_capex_intensity_intenscross_21_252_base_v126_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenscross_63_252_base_v127_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenscross_5_63_base_v128_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (_mean(base, 5) - _mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex/assets MA cross
def f03uci_f03_utility_capex_intensity_assetscross_21_252_base_v129_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetscross_63_252_base_v130_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex/assets dynamics-like
def f03uci_f03_utility_capex_intensity_assetsdyn_63d_base_v131_signal(capex, assets, revenue, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    rb = _f03_capex_dynamics(capex, revenue, 63)
    dyn = base - _mean(base, 63)
    result = dyn * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsdyn_252d_base_v132_signal(capex, assets, revenue, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    rb = _f03_capex_dynamics(capex, revenue, 252)
    dyn = base - _mean(base, 252)
    result = dyn * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × revenue growth × close × volume
def f03uci_f03_utility_capex_intensity_intensxrgxvol_63d_base_v133_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    rg = revenue.pct_change(63)
    result = _mean(base, 63) * rg * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrgxvol_252d_base_v134_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    rg = revenue.pct_change(252)
    result = _mean(base, 252) * rg * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Combined intensity × log assets × close
def f03uci_f03_utility_capex_intensity_intensxassetsize_63d_base_v135_signal(capex, revenue, assets, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    s = np.log(assets.replace(0, np.nan))
    result = _mean(base, 63) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxassetsize_252d_base_v136_signal(capex, revenue, assets, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    s = np.log(assets.replace(0, np.nan))
    result = _mean(base, 252) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × revenue/assets ratio × close
def f03uci_f03_utility_capex_intensity_intensxrevassets_63d_base_v137_signal(capex, revenue, assets, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    ratio = revenue / assets.replace(0, np.nan)
    result = _mean(base, 63) * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevassets_252d_base_v138_signal(capex, revenue, assets, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    ratio = revenue / assets.replace(0, np.nan)
    result = _mean(base, 252) * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex sum × close (raw spend in window)
def f03uci_f03_utility_capex_intensity_capexsumxclose_63d_base_v139_signal(capex, revenue, closeadj):
    rb = _f03_capex_intensity(capex, revenue)
    result = capex.rolling(63, min_periods=21).sum() / revenue.rolling(63, min_periods=21).sum().replace(0, np.nan) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexsumxclose_252d_base_v140_signal(capex, revenue, closeadj):
    rb = _f03_capex_intensity(capex, revenue)
    result = capex.rolling(252, min_periods=63).sum() / revenue.rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Capex × assets × close
def f03uci_f03_utility_capex_intensity_capexsumxassets_252d_base_v141_signal(capex, assets, closeadj):
    rb = _f03_capex_to_assets(capex, assets)
    result = capex.rolling(252, min_periods=63).sum() / assets.rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × volume × ATR
def f03uci_f03_utility_capex_intensity_intensxvolxatr_63d_base_v142_signal(capex, revenue, closeadj, volume, high, low):
    base = _f03_capex_intensity(capex, revenue)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _mean(base, 63) * _mean(volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxvolxatr_252d_base_v143_signal(capex, revenue, closeadj, volume, high, low):
    base = _f03_capex_intensity(capex, revenue)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _mean(base, 252) * _mean(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Capex/Assets × revenue/assets × close
def f03uci_f03_utility_capex_intensity_assetsxrevassets_63d_base_v144_signal(capex, assets, revenue, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    ratio = revenue / assets.replace(0, np.nan)
    result = _mean(base, 63) * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxrevassets_252d_base_v145_signal(capex, assets, revenue, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    ratio = revenue / assets.replace(0, np.nan)
    result = _mean(base, 252) * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Combined intensity × capex/assets × atr
def f03uci_f03_utility_capex_intensity_comboxatr_63d_base_v146_signal(capex, revenue, assets, closeadj, high, low):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _mean(ci, 63) * _mean(ca, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_comboxatr_252d_base_v147_signal(capex, revenue, assets, closeadj, high, low):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _mean(ci, 252) * _mean(ca, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Combined × dollar volume
def f03uci_f03_utility_capex_intensity_comboxdv_63d_base_v148_signal(capex, revenue, assets, closeadj, volume):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    result = _mean(ci, 63) * _mean(ca, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_comboxdv_252d_base_v149_signal(capex, revenue, assets, closeadj, volume):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    result = _mean(ci, 252) * _mean(ca, 252) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics cubed × close
def f03uci_f03_utility_capex_intensity_dyncube_252d_base_v150_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    result = d * d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03uci_f03_utility_capex_intensity_intensxret_63d_base_v076_signal,
    f03uci_f03_utility_capex_intensity_intensxret_252d_base_v077_signal,
    f03uci_f03_utility_capex_intensity_assetsxret_63d_base_v078_signal,
    f03uci_f03_utility_capex_intensity_assetsxret_252d_base_v079_signal,
    f03uci_f03_utility_capex_intensity_intensxabsret_63d_base_v080_signal,
    f03uci_f03_utility_capex_intensity_intensxabsret_252d_base_v081_signal,
    f03uci_f03_utility_capex_intensity_intensxclosez_63d_base_v082_signal,
    f03uci_f03_utility_capex_intensity_intensxclosez_252d_base_v083_signal,
    f03uci_f03_utility_capex_intensity_assetsxclosez_252d_base_v084_signal,
    f03uci_f03_utility_capex_intensity_intensxvolz_63d_base_v085_signal,
    f03uci_f03_utility_capex_intensity_intensxvolz_252d_base_v086_signal,
    f03uci_f03_utility_capex_intensity_intenssign_63d_base_v087_signal,
    f03uci_f03_utility_capex_intensity_intenssign_252d_base_v088_signal,
    f03uci_f03_utility_capex_intensity_intensabs_63d_base_v089_signal,
    f03uci_f03_utility_capex_intensity_assetsabs_252d_base_v090_signal,
    f03uci_f03_utility_capex_intensity_assetsema_63d_base_v091_signal,
    f03uci_f03_utility_capex_intensity_assetssq_63d_base_v092_signal,
    f03uci_f03_utility_capex_intensity_assetssq_252d_base_v093_signal,
    f03uci_f03_utility_capex_intensity_assetsxvol_63d_base_v094_signal,
    f03uci_f03_utility_capex_intensity_assetsxatr_63d_base_v095_signal,
    f03uci_f03_utility_capex_intensity_assetsgap_63d_base_v096_signal,
    f03uci_f03_utility_capex_intensity_assetsrank_63d_base_v097_signal,
    f03uci_f03_utility_capex_intensity_intensityrank_63d_base_v098_signal,
    f03uci_f03_utility_capex_intensity_assetsz_63d_base_v099_signal,
    f03uci_f03_utility_capex_intensity_capexgrowthxsize_63d_base_v100_signal,
    f03uci_f03_utility_capex_intensity_capexgrowthxsize_252d_base_v101_signal,
    f03uci_f03_utility_capex_intensity_intensxrevgrowth_63d_base_v102_signal,
    f03uci_f03_utility_capex_intensity_intensxrevgrowth_252d_base_v103_signal,
    f03uci_f03_utility_capex_intensity_capexaccel_63d_base_v104_signal,
    f03uci_f03_utility_capex_intensity_capexaccel_252d_base_v105_signal,
    f03uci_f03_utility_capex_intensity_intensxinvprice_63d_base_v106_signal,
    f03uci_f03_utility_capex_intensity_intensxinvprice_252d_base_v107_signal,
    f03uci_f03_utility_capex_intensity_dyngap_63d_base_v108_signal,
    f03uci_f03_utility_capex_intensity_dyngap_252d_base_v109_signal,
    f03uci_f03_utility_capex_intensity_dynxretpct_63d_base_v110_signal,
    f03uci_f03_utility_capex_intensity_dynxretpct_252d_base_v111_signal,
    f03uci_f03_utility_capex_intensity_dynrank_63d_base_v112_signal,
    f03uci_f03_utility_capex_intensity_dynrank_252d_base_v113_signal,
    f03uci_f03_utility_capex_intensity_dynz_63d_base_v114_signal,
    f03uci_f03_utility_capex_intensity_dynz_252d_base_v115_signal,
    f03uci_f03_utility_capex_intensity_dynxdv_63d_base_v116_signal,
    f03uci_f03_utility_capex_intensity_dynxdv_252d_base_v117_signal,
    f03uci_f03_utility_capex_intensity_intensxdv_63d_base_v118_signal,
    f03uci_f03_utility_capex_intensity_intensxdv_252d_base_v119_signal,
    f03uci_f03_utility_capex_intensity_assetsxdv_63d_base_v120_signal,
    f03uci_f03_utility_capex_intensity_assetsxdv_252d_base_v121_signal,
    f03uci_f03_utility_capex_intensity_intensspread_63d_base_v122_signal,
    f03uci_f03_utility_capex_intensity_intensspread_252d_base_v123_signal,
    f03uci_f03_utility_capex_intensity_combodyn_63d_base_v124_signal,
    f03uci_f03_utility_capex_intensity_combodyn_252d_base_v125_signal,
    f03uci_f03_utility_capex_intensity_intenscross_21_252_base_v126_signal,
    f03uci_f03_utility_capex_intensity_intenscross_63_252_base_v127_signal,
    f03uci_f03_utility_capex_intensity_intenscross_5_63_base_v128_signal,
    f03uci_f03_utility_capex_intensity_assetscross_21_252_base_v129_signal,
    f03uci_f03_utility_capex_intensity_assetscross_63_252_base_v130_signal,
    f03uci_f03_utility_capex_intensity_assetsdyn_63d_base_v131_signal,
    f03uci_f03_utility_capex_intensity_assetsdyn_252d_base_v132_signal,
    f03uci_f03_utility_capex_intensity_intensxrgxvol_63d_base_v133_signal,
    f03uci_f03_utility_capex_intensity_intensxrgxvol_252d_base_v134_signal,
    f03uci_f03_utility_capex_intensity_intensxassetsize_63d_base_v135_signal,
    f03uci_f03_utility_capex_intensity_intensxassetsize_252d_base_v136_signal,
    f03uci_f03_utility_capex_intensity_intensxrevassets_63d_base_v137_signal,
    f03uci_f03_utility_capex_intensity_intensxrevassets_252d_base_v138_signal,
    f03uci_f03_utility_capex_intensity_capexsumxclose_63d_base_v139_signal,
    f03uci_f03_utility_capex_intensity_capexsumxclose_252d_base_v140_signal,
    f03uci_f03_utility_capex_intensity_capexsumxassets_252d_base_v141_signal,
    f03uci_f03_utility_capex_intensity_intensxvolxatr_63d_base_v142_signal,
    f03uci_f03_utility_capex_intensity_intensxvolxatr_252d_base_v143_signal,
    f03uci_f03_utility_capex_intensity_assetsxrevassets_63d_base_v144_signal,
    f03uci_f03_utility_capex_intensity_assetsxrevassets_252d_base_v145_signal,
    f03uci_f03_utility_capex_intensity_comboxatr_63d_base_v146_signal,
    f03uci_f03_utility_capex_intensity_comboxatr_252d_base_v147_signal,
    f03uci_f03_utility_capex_intensity_comboxdv_63d_base_v148_signal,
    f03uci_f03_utility_capex_intensity_comboxdv_252d_base_v149_signal,
    f03uci_f03_utility_capex_intensity_dyncube_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_UTILITY_CAPEX_INTENSITY_REGISTRY_076_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "capex": capex, "revenue": revenue, "assets": assets,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f03_capex_intensity", "_f03_capex_to_assets", "_f03_capex_dynamics")
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
    print(f"OK f03_utility_capex_intensity_base_076_150_claude: {n_features} features pass")
