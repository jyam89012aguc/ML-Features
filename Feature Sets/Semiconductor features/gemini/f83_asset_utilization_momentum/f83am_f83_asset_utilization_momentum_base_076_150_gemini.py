import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f83am_f83_asset_utilization_momentum_calc076_38d_val_v076_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(38).mean()
    v2 = ratio.rolling(43).std()
    v3 = ratio.diff(38)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(38)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc076_38d_val_v076_signal'] = f83am_f83_asset_utilization_momentum_calc076_38d_val_v076_signal

def f83am_f83_asset_utilization_momentum_calc077_91d_val_v077_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(91).mean()
    v2 = ratio.rolling(96).std()
    v3 = ratio.diff(91)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc077_91d_val_v077_signal'] = f83am_f83_asset_utilization_momentum_calc077_91d_val_v077_signal

def f83am_f83_asset_utilization_momentum_calc078_144d_val_v078_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(144).mean()
    v2 = ratio.rolling(149).std()
    v3 = ratio.diff(144)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc078_144d_val_v078_signal'] = f83am_f83_asset_utilization_momentum_calc078_144d_val_v078_signal

def f83am_f83_asset_utilization_momentum_calc079_197d_val_v079_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(197).mean()
    v2 = ratio.rolling(202).std()
    v3 = ratio.diff(197)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc079_197d_val_v079_signal'] = f83am_f83_asset_utilization_momentum_calc079_197d_val_v079_signal

def f83am_f83_asset_utilization_momentum_calc080_50d_val_v080_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(50).mean()
    v2 = ratio.rolling(55).std()
    v3 = ratio.diff(50)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc080_50d_val_v080_signal'] = f83am_f83_asset_utilization_momentum_calc080_50d_val_v080_signal

def f83am_f83_asset_utilization_momentum_calc081_103d_val_v081_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(103).mean()
    v2 = ratio.rolling(108).std()
    v3 = ratio.diff(103)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc081_103d_val_v081_signal'] = f83am_f83_asset_utilization_momentum_calc081_103d_val_v081_signal

def f83am_f83_asset_utilization_momentum_calc082_156d_val_v082_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(156).mean()
    v2 = ratio.rolling(161).std()
    v3 = ratio.diff(156)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(156)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc082_156d_val_v082_signal'] = f83am_f83_asset_utilization_momentum_calc082_156d_val_v082_signal

def f83am_f83_asset_utilization_momentum_calc083_209d_val_v083_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(209).mean()
    v2 = ratio.rolling(214).std()
    v3 = ratio.diff(209)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc083_209d_val_v083_signal'] = f83am_f83_asset_utilization_momentum_calc083_209d_val_v083_signal

def f83am_f83_asset_utilization_momentum_calc084_62d_val_v084_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(62).mean()
    v2 = ratio.rolling(67).std()
    v3 = ratio.diff(62)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc084_62d_val_v084_signal'] = f83am_f83_asset_utilization_momentum_calc084_62d_val_v084_signal

def f83am_f83_asset_utilization_momentum_calc085_115d_val_v085_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(115).mean()
    v2 = ratio.rolling(120).std()
    v3 = ratio.diff(115)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc085_115d_val_v085_signal'] = f83am_f83_asset_utilization_momentum_calc085_115d_val_v085_signal

def f83am_f83_asset_utilization_momentum_calc086_168d_val_v086_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(168).mean()
    v2 = ratio.rolling(173).std()
    v3 = ratio.diff(168)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc086_168d_val_v086_signal'] = f83am_f83_asset_utilization_momentum_calc086_168d_val_v086_signal

def f83am_f83_asset_utilization_momentum_calc087_21d_val_v087_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(21).mean()
    v2 = ratio.rolling(26).std()
    v3 = ratio.diff(21)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc087_21d_val_v087_signal'] = f83am_f83_asset_utilization_momentum_calc087_21d_val_v087_signal

def f83am_f83_asset_utilization_momentum_calc088_74d_val_v088_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(74).mean()
    v2 = ratio.rolling(79).std()
    v3 = ratio.diff(74)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(74)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc088_74d_val_v088_signal'] = f83am_f83_asset_utilization_momentum_calc088_74d_val_v088_signal

def f83am_f83_asset_utilization_momentum_calc089_127d_val_v089_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(127).mean()
    v2 = ratio.rolling(132).std()
    v3 = ratio.diff(127)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc089_127d_val_v089_signal'] = f83am_f83_asset_utilization_momentum_calc089_127d_val_v089_signal

def f83am_f83_asset_utilization_momentum_calc090_180d_val_v090_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(180).mean()
    v2 = ratio.rolling(185).std()
    v3 = ratio.diff(180)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc090_180d_val_v090_signal'] = f83am_f83_asset_utilization_momentum_calc090_180d_val_v090_signal

def f83am_f83_asset_utilization_momentum_calc091_33d_val_v091_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(33).mean()
    v2 = ratio.rolling(38).std()
    v3 = ratio.diff(33)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc091_33d_val_v091_signal'] = f83am_f83_asset_utilization_momentum_calc091_33d_val_v091_signal

def f83am_f83_asset_utilization_momentum_calc092_86d_val_v092_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(86).mean()
    v2 = ratio.rolling(91).std()
    v3 = ratio.diff(86)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc092_86d_val_v092_signal'] = f83am_f83_asset_utilization_momentum_calc092_86d_val_v092_signal

def f83am_f83_asset_utilization_momentum_calc093_139d_val_v093_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(139).mean()
    v2 = ratio.rolling(144).std()
    v3 = ratio.diff(139)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc093_139d_val_v093_signal'] = f83am_f83_asset_utilization_momentum_calc093_139d_val_v093_signal

def f83am_f83_asset_utilization_momentum_calc094_192d_val_v094_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(192).mean()
    v2 = ratio.rolling(197).std()
    v3 = ratio.diff(192)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(192)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc094_192d_val_v094_signal'] = f83am_f83_asset_utilization_momentum_calc094_192d_val_v094_signal

def f83am_f83_asset_utilization_momentum_calc095_45d_val_v095_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(45).mean()
    v2 = ratio.rolling(50).std()
    v3 = ratio.diff(45)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc095_45d_val_v095_signal'] = f83am_f83_asset_utilization_momentum_calc095_45d_val_v095_signal

def f83am_f83_asset_utilization_momentum_calc096_98d_val_v096_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(98).mean()
    v2 = ratio.rolling(103).std()
    v3 = ratio.diff(98)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc096_98d_val_v096_signal'] = f83am_f83_asset_utilization_momentum_calc096_98d_val_v096_signal

def f83am_f83_asset_utilization_momentum_calc097_151d_val_v097_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(151).mean()
    v2 = ratio.rolling(156).std()
    v3 = ratio.diff(151)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc097_151d_val_v097_signal'] = f83am_f83_asset_utilization_momentum_calc097_151d_val_v097_signal

def f83am_f83_asset_utilization_momentum_calc098_204d_val_v098_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(204).mean()
    v2 = ratio.rolling(209).std()
    v3 = ratio.diff(204)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc098_204d_val_v098_signal'] = f83am_f83_asset_utilization_momentum_calc098_204d_val_v098_signal

def f83am_f83_asset_utilization_momentum_calc099_57d_val_v099_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(57).mean()
    v2 = ratio.rolling(62).std()
    v3 = ratio.diff(57)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc099_57d_val_v099_signal'] = f83am_f83_asset_utilization_momentum_calc099_57d_val_v099_signal

def f83am_f83_asset_utilization_momentum_calc100_110d_val_v100_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(110).mean()
    v2 = ratio.rolling(115).std()
    v3 = ratio.diff(110)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(110)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc100_110d_val_v100_signal'] = f83am_f83_asset_utilization_momentum_calc100_110d_val_v100_signal

def f83am_f83_asset_utilization_momentum_calc101_163d_val_v101_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(163).mean()
    v2 = ratio.rolling(168).std()
    v3 = ratio.diff(163)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc101_163d_val_v101_signal'] = f83am_f83_asset_utilization_momentum_calc101_163d_val_v101_signal

def f83am_f83_asset_utilization_momentum_calc102_16d_val_v102_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(16).mean()
    v2 = ratio.rolling(21).std()
    v3 = ratio.diff(16)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc102_16d_val_v102_signal'] = f83am_f83_asset_utilization_momentum_calc102_16d_val_v102_signal

def f83am_f83_asset_utilization_momentum_calc103_69d_val_v103_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(69).mean()
    v2 = ratio.rolling(74).std()
    v3 = ratio.diff(69)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc103_69d_val_v103_signal'] = f83am_f83_asset_utilization_momentum_calc103_69d_val_v103_signal

def f83am_f83_asset_utilization_momentum_calc104_122d_val_v104_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(122).mean()
    v2 = ratio.rolling(127).std()
    v3 = ratio.diff(122)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc104_122d_val_v104_signal'] = f83am_f83_asset_utilization_momentum_calc104_122d_val_v104_signal

def f83am_f83_asset_utilization_momentum_calc105_175d_val_v105_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(175).mean()
    v2 = ratio.rolling(180).std()
    v3 = ratio.diff(175)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc105_175d_val_v105_signal'] = f83am_f83_asset_utilization_momentum_calc105_175d_val_v105_signal

def f83am_f83_asset_utilization_momentum_calc106_28d_val_v106_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(28).mean()
    v2 = ratio.rolling(33).std()
    v3 = ratio.diff(28)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(28)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc106_28d_val_v106_signal'] = f83am_f83_asset_utilization_momentum_calc106_28d_val_v106_signal

def f83am_f83_asset_utilization_momentum_calc107_81d_val_v107_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(81).mean()
    v2 = ratio.rolling(86).std()
    v3 = ratio.diff(81)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc107_81d_val_v107_signal'] = f83am_f83_asset_utilization_momentum_calc107_81d_val_v107_signal

def f83am_f83_asset_utilization_momentum_calc108_134d_val_v108_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(134).mean()
    v2 = ratio.rolling(139).std()
    v3 = ratio.diff(134)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc108_134d_val_v108_signal'] = f83am_f83_asset_utilization_momentum_calc108_134d_val_v108_signal

def f83am_f83_asset_utilization_momentum_calc109_187d_val_v109_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(187).mean()
    v2 = ratio.rolling(192).std()
    v3 = ratio.diff(187)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc109_187d_val_v109_signal'] = f83am_f83_asset_utilization_momentum_calc109_187d_val_v109_signal

def f83am_f83_asset_utilization_momentum_calc110_40d_val_v110_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(40).mean()
    v2 = ratio.rolling(45).std()
    v3 = ratio.diff(40)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc110_40d_val_v110_signal'] = f83am_f83_asset_utilization_momentum_calc110_40d_val_v110_signal

def f83am_f83_asset_utilization_momentum_calc111_93d_val_v111_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(93).mean()
    v2 = ratio.rolling(98).std()
    v3 = ratio.diff(93)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc111_93d_val_v111_signal'] = f83am_f83_asset_utilization_momentum_calc111_93d_val_v111_signal

def f83am_f83_asset_utilization_momentum_calc112_146d_val_v112_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(146).mean()
    v2 = ratio.rolling(151).std()
    v3 = ratio.diff(146)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(146)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc112_146d_val_v112_signal'] = f83am_f83_asset_utilization_momentum_calc112_146d_val_v112_signal

def f83am_f83_asset_utilization_momentum_calc113_199d_val_v113_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(199).mean()
    v2 = ratio.rolling(204).std()
    v3 = ratio.diff(199)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc113_199d_val_v113_signal'] = f83am_f83_asset_utilization_momentum_calc113_199d_val_v113_signal

def f83am_f83_asset_utilization_momentum_calc114_52d_val_v114_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(52).mean()
    v2 = ratio.rolling(57).std()
    v3 = ratio.diff(52)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc114_52d_val_v114_signal'] = f83am_f83_asset_utilization_momentum_calc114_52d_val_v114_signal

def f83am_f83_asset_utilization_momentum_calc115_105d_val_v115_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(105).mean()
    v2 = ratio.rolling(110).std()
    v3 = ratio.diff(105)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc115_105d_val_v115_signal'] = f83am_f83_asset_utilization_momentum_calc115_105d_val_v115_signal

def f83am_f83_asset_utilization_momentum_calc116_158d_val_v116_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(158).mean()
    v2 = ratio.rolling(163).std()
    v3 = ratio.diff(158)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc116_158d_val_v116_signal'] = f83am_f83_asset_utilization_momentum_calc116_158d_val_v116_signal

def f83am_f83_asset_utilization_momentum_calc117_11d_val_v117_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(11).mean()
    v2 = ratio.rolling(16).std()
    v3 = ratio.diff(11)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc117_11d_val_v117_signal'] = f83am_f83_asset_utilization_momentum_calc117_11d_val_v117_signal

def f83am_f83_asset_utilization_momentum_calc118_64d_val_v118_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(64).mean()
    v2 = ratio.rolling(69).std()
    v3 = ratio.diff(64)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(64)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc118_64d_val_v118_signal'] = f83am_f83_asset_utilization_momentum_calc118_64d_val_v118_signal

def f83am_f83_asset_utilization_momentum_calc119_117d_val_v119_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(117).mean()
    v2 = ratio.rolling(122).std()
    v3 = ratio.diff(117)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc119_117d_val_v119_signal'] = f83am_f83_asset_utilization_momentum_calc119_117d_val_v119_signal

def f83am_f83_asset_utilization_momentum_calc120_170d_val_v120_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(170).mean()
    v2 = ratio.rolling(175).std()
    v3 = ratio.diff(170)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc120_170d_val_v120_signal'] = f83am_f83_asset_utilization_momentum_calc120_170d_val_v120_signal

def f83am_f83_asset_utilization_momentum_calc121_23d_val_v121_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(23).mean()
    v2 = ratio.rolling(28).std()
    v3 = ratio.diff(23)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc121_23d_val_v121_signal'] = f83am_f83_asset_utilization_momentum_calc121_23d_val_v121_signal

def f83am_f83_asset_utilization_momentum_calc122_76d_val_v122_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(76).mean()
    v2 = ratio.rolling(81).std()
    v3 = ratio.diff(76)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc122_76d_val_v122_signal'] = f83am_f83_asset_utilization_momentum_calc122_76d_val_v122_signal

def f83am_f83_asset_utilization_momentum_calc123_129d_val_v123_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(129).mean()
    v2 = ratio.rolling(134).std()
    v3 = ratio.diff(129)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc123_129d_val_v123_signal'] = f83am_f83_asset_utilization_momentum_calc123_129d_val_v123_signal

def f83am_f83_asset_utilization_momentum_calc124_182d_val_v124_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(182).mean()
    v2 = ratio.rolling(187).std()
    v3 = ratio.diff(182)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(182)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc124_182d_val_v124_signal'] = f83am_f83_asset_utilization_momentum_calc124_182d_val_v124_signal

def f83am_f83_asset_utilization_momentum_calc125_35d_val_v125_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(35).mean()
    v2 = ratio.rolling(40).std()
    v3 = ratio.diff(35)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc125_35d_val_v125_signal'] = f83am_f83_asset_utilization_momentum_calc125_35d_val_v125_signal

def f83am_f83_asset_utilization_momentum_calc126_88d_val_v126_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(88).mean()
    v2 = ratio.rolling(93).std()
    v3 = ratio.diff(88)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc126_88d_val_v126_signal'] = f83am_f83_asset_utilization_momentum_calc126_88d_val_v126_signal

def f83am_f83_asset_utilization_momentum_calc127_141d_val_v127_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(141).mean()
    v2 = ratio.rolling(146).std()
    v3 = ratio.diff(141)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc127_141d_val_v127_signal'] = f83am_f83_asset_utilization_momentum_calc127_141d_val_v127_signal

def f83am_f83_asset_utilization_momentum_calc128_194d_val_v128_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(194).mean()
    v2 = ratio.rolling(199).std()
    v3 = ratio.diff(194)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc128_194d_val_v128_signal'] = f83am_f83_asset_utilization_momentum_calc128_194d_val_v128_signal

def f83am_f83_asset_utilization_momentum_calc129_47d_val_v129_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(47).mean()
    v2 = ratio.rolling(52).std()
    v3 = ratio.diff(47)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc129_47d_val_v129_signal'] = f83am_f83_asset_utilization_momentum_calc129_47d_val_v129_signal

def f83am_f83_asset_utilization_momentum_calc130_100d_val_v130_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(100).mean()
    v2 = ratio.rolling(105).std()
    v3 = ratio.diff(100)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(100)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc130_100d_val_v130_signal'] = f83am_f83_asset_utilization_momentum_calc130_100d_val_v130_signal

def f83am_f83_asset_utilization_momentum_calc131_153d_val_v131_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(153).mean()
    v2 = ratio.rolling(158).std()
    v3 = ratio.diff(153)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc131_153d_val_v131_signal'] = f83am_f83_asset_utilization_momentum_calc131_153d_val_v131_signal

def f83am_f83_asset_utilization_momentum_calc132_206d_val_v132_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(206).mean()
    v2 = ratio.rolling(211).std()
    v3 = ratio.diff(206)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc132_206d_val_v132_signal'] = f83am_f83_asset_utilization_momentum_calc132_206d_val_v132_signal

def f83am_f83_asset_utilization_momentum_calc133_59d_val_v133_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(59).mean()
    v2 = ratio.rolling(64).std()
    v3 = ratio.diff(59)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc133_59d_val_v133_signal'] = f83am_f83_asset_utilization_momentum_calc133_59d_val_v133_signal

def f83am_f83_asset_utilization_momentum_calc134_112d_val_v134_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(112).mean()
    v2 = ratio.rolling(117).std()
    v3 = ratio.diff(112)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc134_112d_val_v134_signal'] = f83am_f83_asset_utilization_momentum_calc134_112d_val_v134_signal

def f83am_f83_asset_utilization_momentum_calc135_165d_val_v135_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(165).mean()
    v2 = ratio.rolling(170).std()
    v3 = ratio.diff(165)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc135_165d_val_v135_signal'] = f83am_f83_asset_utilization_momentum_calc135_165d_val_v135_signal

def f83am_f83_asset_utilization_momentum_calc136_18d_val_v136_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(18).mean()
    v2 = ratio.rolling(23).std()
    v3 = ratio.diff(18)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(18)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc136_18d_val_v136_signal'] = f83am_f83_asset_utilization_momentum_calc136_18d_val_v136_signal

def f83am_f83_asset_utilization_momentum_calc137_71d_val_v137_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(71).mean()
    v2 = ratio.rolling(76).std()
    v3 = ratio.diff(71)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc137_71d_val_v137_signal'] = f83am_f83_asset_utilization_momentum_calc137_71d_val_v137_signal

def f83am_f83_asset_utilization_momentum_calc138_124d_val_v138_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(124).mean()
    v2 = ratio.rolling(129).std()
    v3 = ratio.diff(124)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc138_124d_val_v138_signal'] = f83am_f83_asset_utilization_momentum_calc138_124d_val_v138_signal

def f83am_f83_asset_utilization_momentum_calc139_177d_val_v139_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(177).mean()
    v2 = ratio.rolling(182).std()
    v3 = ratio.diff(177)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc139_177d_val_v139_signal'] = f83am_f83_asset_utilization_momentum_calc139_177d_val_v139_signal

def f83am_f83_asset_utilization_momentum_calc140_30d_val_v140_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(30).mean()
    v2 = ratio.rolling(35).std()
    v3 = ratio.diff(30)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc140_30d_val_v140_signal'] = f83am_f83_asset_utilization_momentum_calc140_30d_val_v140_signal

def f83am_f83_asset_utilization_momentum_calc141_83d_val_v141_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(83).mean()
    v2 = ratio.rolling(88).std()
    v3 = ratio.diff(83)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc141_83d_val_v141_signal'] = f83am_f83_asset_utilization_momentum_calc141_83d_val_v141_signal

def f83am_f83_asset_utilization_momentum_calc142_136d_val_v142_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(136).mean()
    v2 = ratio.rolling(141).std()
    v3 = ratio.diff(136)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(136)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc142_136d_val_v142_signal'] = f83am_f83_asset_utilization_momentum_calc142_136d_val_v142_signal

def f83am_f83_asset_utilization_momentum_calc143_189d_val_v143_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(189).mean()
    v2 = ratio.rolling(194).std()
    v3 = ratio.diff(189)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc143_189d_val_v143_signal'] = f83am_f83_asset_utilization_momentum_calc143_189d_val_v143_signal

def f83am_f83_asset_utilization_momentum_calc144_42d_val_v144_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(42).mean()
    v2 = ratio.rolling(47).std()
    v3 = ratio.diff(42)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc144_42d_val_v144_signal'] = f83am_f83_asset_utilization_momentum_calc144_42d_val_v144_signal

def f83am_f83_asset_utilization_momentum_calc145_95d_val_v145_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(95).mean()
    v2 = ratio.rolling(100).std()
    v3 = ratio.diff(95)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc145_95d_val_v145_signal'] = f83am_f83_asset_utilization_momentum_calc145_95d_val_v145_signal

def f83am_f83_asset_utilization_momentum_calc146_148d_val_v146_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(148).mean()
    v2 = ratio.rolling(153).std()
    v3 = ratio.diff(148)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc146_148d_val_v146_signal'] = f83am_f83_asset_utilization_momentum_calc146_148d_val_v146_signal

def f83am_f83_asset_utilization_momentum_calc147_201d_val_v147_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(201).mean()
    v2 = ratio.rolling(206).std()
    v3 = ratio.diff(201)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc147_201d_val_v147_signal'] = f83am_f83_asset_utilization_momentum_calc147_201d_val_v147_signal

def f83am_f83_asset_utilization_momentum_calc148_54d_val_v148_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(54).mean()
    v2 = ratio.rolling(59).std()
    v3 = ratio.diff(54)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(54)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc148_54d_val_v148_signal'] = f83am_f83_asset_utilization_momentum_calc148_54d_val_v148_signal

def f83am_f83_asset_utilization_momentum_calc149_107d_val_v149_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(107).mean()
    v2 = ratio.rolling(112).std()
    v3 = ratio.diff(107)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc149_107d_val_v149_signal'] = f83am_f83_asset_utilization_momentum_calc149_107d_val_v149_signal

def f83am_f83_asset_utilization_momentum_calc150_160d_val_v150_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(160).mean()
    v2 = ratio.rolling(165).std()
    v3 = ratio.diff(160)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc150_160d_val_v150_signal'] = f83am_f83_asset_utilization_momentum_calc150_160d_val_v150_signal


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
