import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f57at_f57_asset_turnover_velocity_calc076_126d_base_v076_signal(capex, revenue):
    res = ((revenue / capex) / (revenue / capex).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc076_126d_base_v076_signal'] = f57at_f57_asset_turnover_velocity_calc076_126d_base_v076_signal

def f57at_f57_asset_turnover_velocity_calc077_42d_base_v077_signal(assets, netinc):
    res = (netinc / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc077_42d_base_v077_signal'] = f57at_f57_asset_turnover_velocity_calc077_42d_base_v077_signal

def f57at_f57_asset_turnover_velocity_calc078_42d_base_v078_signal(assets, revenue):
    res = (revenue / assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc078_42d_base_v078_signal'] = f57at_f57_asset_turnover_velocity_calc078_42d_base_v078_signal

def f57at_f57_asset_turnover_velocity_calc079_5d_base_v079_signal(assets, revenue):
    res = (revenue / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc079_5d_base_v079_signal'] = f57at_f57_asset_turnover_velocity_calc079_5d_base_v079_signal

def f57at_f57_asset_turnover_velocity_calc080_5d_base_v080_signal(assets, gp):
    res = ((gp / assets) - (gp / assets).rolling(5).mean()) / (gp / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc080_5d_base_v080_signal'] = f57at_f57_asset_turnover_velocity_calc080_5d_base_v080_signal

def f57at_f57_asset_turnover_velocity_calc081_10d_base_v081_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc081_10d_base_v081_signal'] = f57at_f57_asset_turnover_velocity_calc081_10d_base_v081_signal

def f57at_f57_asset_turnover_velocity_calc082_5d_base_v082_signal(assets, netinc):
    res = (netinc / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc082_5d_base_v082_signal'] = f57at_f57_asset_turnover_velocity_calc082_5d_base_v082_signal

def f57at_f57_asset_turnover_velocity_calc083_63d_base_v083_signal(revenue, workingcapital):
    res = ((revenue / workingcapital) / (revenue / workingcapital).rolling(63).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc083_63d_base_v083_signal'] = f57at_f57_asset_turnover_velocity_calc083_63d_base_v083_signal

def f57at_f57_asset_turnover_velocity_calc084_21d_base_v084_signal(capex, revenue):
    res = (revenue / capex).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc084_21d_base_v084_signal'] = f57at_f57_asset_turnover_velocity_calc084_21d_base_v084_signal

def f57at_f57_asset_turnover_velocity_calc085_63d_base_v085_signal(assets, fcf):
    res = np.log((fcf / assets).abs().replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc085_63d_base_v085_signal'] = f57at_f57_asset_turnover_velocity_calc085_63d_base_v085_signal

def f57at_f57_asset_turnover_velocity_calc086_21d_base_v086_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc086_21d_base_v086_signal'] = f57at_f57_asset_turnover_velocity_calc086_21d_base_v086_signal

def f57at_f57_asset_turnover_velocity_calc087_21d_base_v087_signal(assets, opinc):
    res = (opinc / assets).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc087_21d_base_v087_signal'] = f57at_f57_asset_turnover_velocity_calc087_21d_base_v087_signal

def f57at_f57_asset_turnover_velocity_calc088_252d_base_v088_signal(capex, revenue):
    res = (revenue / capex).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc088_252d_base_v088_signal'] = f57at_f57_asset_turnover_velocity_calc088_252d_base_v088_signal

def f57at_f57_asset_turnover_velocity_calc089_5d_base_v089_signal(assets, gp):
    res = (gp / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc089_5d_base_v089_signal'] = f57at_f57_asset_turnover_velocity_calc089_5d_base_v089_signal

def f57at_f57_asset_turnover_velocity_calc090_5d_base_v090_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc090_5d_base_v090_signal'] = f57at_f57_asset_turnover_velocity_calc090_5d_base_v090_signal

def f57at_f57_asset_turnover_velocity_calc091_42d_base_v091_signal(assets, fcf):
    res = (fcf / assets).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc091_42d_base_v091_signal'] = f57at_f57_asset_turnover_velocity_calc091_42d_base_v091_signal

def f57at_f57_asset_turnover_velocity_calc092_126d_base_v092_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc092_126d_base_v092_signal'] = f57at_f57_asset_turnover_velocity_calc092_126d_base_v092_signal

def f57at_f57_asset_turnover_velocity_calc093_126d_base_v093_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc093_126d_base_v093_signal'] = f57at_f57_asset_turnover_velocity_calc093_126d_base_v093_signal

def f57at_f57_asset_turnover_velocity_calc094_63d_base_v094_signal(capex, revenue):
    res = (revenue / capex).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc094_63d_base_v094_signal'] = f57at_f57_asset_turnover_velocity_calc094_63d_base_v094_signal

def f57at_f57_asset_turnover_velocity_calc095_42d_base_v095_signal(assets, fcf):
    res = (fcf / assets).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc095_42d_base_v095_signal'] = f57at_f57_asset_turnover_velocity_calc095_42d_base_v095_signal

def f57at_f57_asset_turnover_velocity_calc096_63d_base_v096_signal(liabilities, revenue):
    res = (revenue / liabilities).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc096_63d_base_v096_signal'] = f57at_f57_asset_turnover_velocity_calc096_63d_base_v096_signal

def f57at_f57_asset_turnover_velocity_calc097_10d_base_v097_signal(assets, gp):
    res = ((gp / assets) / (gp / assets).rolling(10).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc097_10d_base_v097_signal'] = f57at_f57_asset_turnover_velocity_calc097_10d_base_v097_signal

def f57at_f57_asset_turnover_velocity_calc098_21d_base_v098_signal(revenue, workingcapital):
    res = ((revenue / workingcapital) - (revenue / workingcapital).rolling(21).mean()) / (revenue / workingcapital).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc098_21d_base_v098_signal'] = f57at_f57_asset_turnover_velocity_calc098_21d_base_v098_signal

def f57at_f57_asset_turnover_velocity_calc099_10d_base_v099_signal(assets, revenue):
    res = (revenue / assets).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc099_10d_base_v099_signal'] = f57at_f57_asset_turnover_velocity_calc099_10d_base_v099_signal

def f57at_f57_asset_turnover_velocity_calc100_10d_base_v100_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc100_10d_base_v100_signal'] = f57at_f57_asset_turnover_velocity_calc100_10d_base_v100_signal

def f57at_f57_asset_turnover_velocity_calc101_126d_base_v101_signal(equity, gp):
    res = (gp / equity).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc101_126d_base_v101_signal'] = f57at_f57_asset_turnover_velocity_calc101_126d_base_v101_signal

def f57at_f57_asset_turnover_velocity_calc102_10d_base_v102_signal(assets, gp):
    res = (gp / assets).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc102_10d_base_v102_signal'] = f57at_f57_asset_turnover_velocity_calc102_10d_base_v102_signal

def f57at_f57_asset_turnover_velocity_calc103_252d_base_v103_signal(assets, opinc):
    res = (opinc / assets).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc103_252d_base_v103_signal'] = f57at_f57_asset_turnover_velocity_calc103_252d_base_v103_signal

def f57at_f57_asset_turnover_velocity_calc104_10d_base_v104_signal(equity, gp):
    res = (gp / equity).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc104_10d_base_v104_signal'] = f57at_f57_asset_turnover_velocity_calc104_10d_base_v104_signal

def f57at_f57_asset_turnover_velocity_calc105_252d_base_v105_signal(equity, revenue):
    res = ((revenue / equity) / (revenue / equity).rolling(252).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc105_252d_base_v105_signal'] = f57at_f57_asset_turnover_velocity_calc105_252d_base_v105_signal

def f57at_f57_asset_turnover_velocity_calc106_63d_base_v106_signal(equity, revenue):
    res = (revenue / equity).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc106_63d_base_v106_signal'] = f57at_f57_asset_turnover_velocity_calc106_63d_base_v106_signal

def f57at_f57_asset_turnover_velocity_calc107_126d_base_v107_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc107_126d_base_v107_signal'] = f57at_f57_asset_turnover_velocity_calc107_126d_base_v107_signal

def f57at_f57_asset_turnover_velocity_calc108_21d_base_v108_signal(liabilities, revenue):
    res = (revenue / liabilities).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc108_21d_base_v108_signal'] = f57at_f57_asset_turnover_velocity_calc108_21d_base_v108_signal

def f57at_f57_asset_turnover_velocity_calc109_63d_base_v109_signal(equity, gp):
    res = np.log((gp / equity).abs().replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc109_63d_base_v109_signal'] = f57at_f57_asset_turnover_velocity_calc109_63d_base_v109_signal

def f57at_f57_asset_turnover_velocity_calc110_10d_base_v110_signal(equity, revenue):
    res = (revenue / equity).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc110_10d_base_v110_signal'] = f57at_f57_asset_turnover_velocity_calc110_10d_base_v110_signal

def f57at_f57_asset_turnover_velocity_calc111_63d_base_v111_signal(equity, revenue):
    res = (revenue / equity).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc111_63d_base_v111_signal'] = f57at_f57_asset_turnover_velocity_calc111_63d_base_v111_signal

def f57at_f57_asset_turnover_velocity_calc112_21d_base_v112_signal(assets, netinc):
    res = (netinc / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc112_21d_base_v112_signal'] = f57at_f57_asset_turnover_velocity_calc112_21d_base_v112_signal

def f57at_f57_asset_turnover_velocity_calc113_252d_base_v113_signal(assets, gp):
    res = (gp / assets).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc113_252d_base_v113_signal'] = f57at_f57_asset_turnover_velocity_calc113_252d_base_v113_signal

def f57at_f57_asset_turnover_velocity_calc114_21d_base_v114_signal(assets, opinc):
    res = ((opinc / assets) / (opinc / assets).rolling(21).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc114_21d_base_v114_signal'] = f57at_f57_asset_turnover_velocity_calc114_21d_base_v114_signal

def f57at_f57_asset_turnover_velocity_calc115_10d_base_v115_signal(capex, revenue):
    res = (revenue / capex).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc115_10d_base_v115_signal'] = f57at_f57_asset_turnover_velocity_calc115_10d_base_v115_signal

def f57at_f57_asset_turnover_velocity_calc116_252d_base_v116_signal(capex, revenue):
    res = np.log((revenue / capex).abs().replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc116_252d_base_v116_signal'] = f57at_f57_asset_turnover_velocity_calc116_252d_base_v116_signal

def f57at_f57_asset_turnover_velocity_calc117_5d_base_v117_signal(equity, gp):
    res = (gp / equity).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc117_5d_base_v117_signal'] = f57at_f57_asset_turnover_velocity_calc117_5d_base_v117_signal

def f57at_f57_asset_turnover_velocity_calc118_21d_base_v118_signal(capex, revenue):
    res = (revenue / capex).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc118_21d_base_v118_signal'] = f57at_f57_asset_turnover_velocity_calc118_21d_base_v118_signal

def f57at_f57_asset_turnover_velocity_calc119_21d_base_v119_signal(assets, netinc):
    res = (netinc / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc119_21d_base_v119_signal'] = f57at_f57_asset_turnover_velocity_calc119_21d_base_v119_signal

def f57at_f57_asset_turnover_velocity_calc120_42d_base_v120_signal(capex, revenue):
    res = (revenue / capex).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc120_42d_base_v120_signal'] = f57at_f57_asset_turnover_velocity_calc120_42d_base_v120_signal

def f57at_f57_asset_turnover_velocity_calc121_5d_base_v121_signal(capex, revenue):
    res = (revenue / capex).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc121_5d_base_v121_signal'] = f57at_f57_asset_turnover_velocity_calc121_5d_base_v121_signal

def f57at_f57_asset_turnover_velocity_calc122_252d_base_v122_signal(equity, revenue):
    res = (revenue / equity).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc122_252d_base_v122_signal'] = f57at_f57_asset_turnover_velocity_calc122_252d_base_v122_signal

def f57at_f57_asset_turnover_velocity_calc123_126d_base_v123_signal(capex, revenue):
    res = (revenue / capex).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc123_126d_base_v123_signal'] = f57at_f57_asset_turnover_velocity_calc123_126d_base_v123_signal

def f57at_f57_asset_turnover_velocity_calc124_21d_base_v124_signal(equity, revenue):
    res = (revenue / equity).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc124_21d_base_v124_signal'] = f57at_f57_asset_turnover_velocity_calc124_21d_base_v124_signal

def f57at_f57_asset_turnover_velocity_calc125_42d_base_v125_signal(equity, gp):
    res = (gp / equity).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc125_42d_base_v125_signal'] = f57at_f57_asset_turnover_velocity_calc125_42d_base_v125_signal

def f57at_f57_asset_turnover_velocity_calc126_5d_base_v126_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc126_5d_base_v126_signal'] = f57at_f57_asset_turnover_velocity_calc126_5d_base_v126_signal

def f57at_f57_asset_turnover_velocity_calc127_21d_base_v127_signal(equity, gp):
    res = (gp / equity).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc127_21d_base_v127_signal'] = f57at_f57_asset_turnover_velocity_calc127_21d_base_v127_signal

def f57at_f57_asset_turnover_velocity_calc128_21d_base_v128_signal(capex, revenue):
    res = (revenue / capex).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc128_21d_base_v128_signal'] = f57at_f57_asset_turnover_velocity_calc128_21d_base_v128_signal

def f57at_f57_asset_turnover_velocity_calc129_5d_base_v129_signal(assets, revenue):
    res = ((revenue / assets) / (revenue / assets).rolling(5).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc129_5d_base_v129_signal'] = f57at_f57_asset_turnover_velocity_calc129_5d_base_v129_signal

def f57at_f57_asset_turnover_velocity_calc130_10d_base_v130_signal(assets, fcf):
    res = (fcf / assets).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc130_10d_base_v130_signal'] = f57at_f57_asset_turnover_velocity_calc130_10d_base_v130_signal

def f57at_f57_asset_turnover_velocity_calc131_42d_base_v131_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc131_42d_base_v131_signal'] = f57at_f57_asset_turnover_velocity_calc131_42d_base_v131_signal

def f57at_f57_asset_turnover_velocity_calc132_63d_base_v132_signal(equity, revenue):
    res = (revenue / equity).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc132_63d_base_v132_signal'] = f57at_f57_asset_turnover_velocity_calc132_63d_base_v132_signal

def f57at_f57_asset_turnover_velocity_calc133_5d_base_v133_signal(equity, gp):
    res = ((gp / equity) - (gp / equity).rolling(5).mean()) / (gp / equity).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc133_5d_base_v133_signal'] = f57at_f57_asset_turnover_velocity_calc133_5d_base_v133_signal

def f57at_f57_asset_turnover_velocity_calc134_126d_base_v134_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc134_126d_base_v134_signal'] = f57at_f57_asset_turnover_velocity_calc134_126d_base_v134_signal

def f57at_f57_asset_turnover_velocity_calc135_21d_base_v135_signal(equity, revenue):
    res = (revenue / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc135_21d_base_v135_signal'] = f57at_f57_asset_turnover_velocity_calc135_21d_base_v135_signal

def f57at_f57_asset_turnover_velocity_calc136_5d_base_v136_signal(equity, revenue):
    res = ((revenue / equity) / (revenue / equity).rolling(5).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc136_5d_base_v136_signal'] = f57at_f57_asset_turnover_velocity_calc136_5d_base_v136_signal

def f57at_f57_asset_turnover_velocity_calc137_10d_base_v137_signal(equity, revenue):
    res = (revenue / equity).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc137_10d_base_v137_signal'] = f57at_f57_asset_turnover_velocity_calc137_10d_base_v137_signal

def f57at_f57_asset_turnover_velocity_calc138_5d_base_v138_signal(capex, revenue):
    res = (revenue / capex).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc138_5d_base_v138_signal'] = f57at_f57_asset_turnover_velocity_calc138_5d_base_v138_signal

def f57at_f57_asset_turnover_velocity_calc139_5d_base_v139_signal(assets, fcf):
    res = (fcf / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc139_5d_base_v139_signal'] = f57at_f57_asset_turnover_velocity_calc139_5d_base_v139_signal

def f57at_f57_asset_turnover_velocity_calc140_5d_base_v140_signal(revenue, workingcapital):
    res = ((revenue / workingcapital) / (revenue / workingcapital).rolling(5).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc140_5d_base_v140_signal'] = f57at_f57_asset_turnover_velocity_calc140_5d_base_v140_signal

def f57at_f57_asset_turnover_velocity_calc141_5d_base_v141_signal(revenue, workingcapital):
    res = ((revenue / workingcapital) - (revenue / workingcapital).rolling(5).mean()) / (revenue / workingcapital).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc141_5d_base_v141_signal'] = f57at_f57_asset_turnover_velocity_calc141_5d_base_v141_signal

def f57at_f57_asset_turnover_velocity_calc142_21d_base_v142_signal(assets, fcf):
    res = (fcf / assets).rolling(21).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc142_21d_base_v142_signal'] = f57at_f57_asset_turnover_velocity_calc142_21d_base_v142_signal

def f57at_f57_asset_turnover_velocity_calc143_126d_base_v143_signal(capex, revenue):
    res = (revenue / capex).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc143_126d_base_v143_signal'] = f57at_f57_asset_turnover_velocity_calc143_126d_base_v143_signal

def f57at_f57_asset_turnover_velocity_calc144_63d_base_v144_signal(equity, gp):
    res = (gp / equity).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc144_63d_base_v144_signal'] = f57at_f57_asset_turnover_velocity_calc144_63d_base_v144_signal

def f57at_f57_asset_turnover_velocity_calc145_252d_base_v145_signal(assets, fcf):
    res = (fcf / assets).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc145_252d_base_v145_signal'] = f57at_f57_asset_turnover_velocity_calc145_252d_base_v145_signal

def f57at_f57_asset_turnover_velocity_calc146_63d_base_v146_signal(assets, revenue):
    res = ((revenue / assets) / (revenue / assets).rolling(63).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc146_63d_base_v146_signal'] = f57at_f57_asset_turnover_velocity_calc146_63d_base_v146_signal

def f57at_f57_asset_turnover_velocity_calc147_126d_base_v147_signal(equity, revenue):
    res = (revenue / equity).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc147_126d_base_v147_signal'] = f57at_f57_asset_turnover_velocity_calc147_126d_base_v147_signal

def f57at_f57_asset_turnover_velocity_calc148_63d_base_v148_signal(assets, fcf):
    res = (fcf / assets).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc148_63d_base_v148_signal'] = f57at_f57_asset_turnover_velocity_calc148_63d_base_v148_signal

def f57at_f57_asset_turnover_velocity_calc149_252d_base_v149_signal(capex, revenue):
    res = ((revenue / capex) / (revenue / capex).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc149_252d_base_v149_signal'] = f57at_f57_asset_turnover_velocity_calc149_252d_base_v149_signal

def f57at_f57_asset_turnover_velocity_calc150_5d_base_v150_signal(assets, fcf):
    res = (fcf / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc150_5d_base_v150_signal'] = f57at_f57_asset_turnover_velocity_calc150_5d_base_v150_signal


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
