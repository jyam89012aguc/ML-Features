import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f73ag_f73_asset_growth_efficiency_v076_signal(assets, equity):
    res = assets.pct_change(21) - equity.pct_change(21)
    return res.rolling(126).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v076_signal'] = f73ag_f73_asset_growth_efficiency_v076_signal

def f73ag_f73_asset_growth_efficiency_v077_signal(assets, liabilities):
    res = assets.pct_change(21) - liabilities.pct_change(21)
    return res.rolling(126).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v077_signal'] = f73ag_f73_asset_growth_efficiency_v077_signal

def f73ag_f73_asset_growth_efficiency_v078_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v078_signal'] = f73ag_f73_asset_growth_efficiency_v078_signal

def f73ag_f73_asset_growth_efficiency_v079_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v079_signal'] = f73ag_f73_asset_growth_efficiency_v079_signal

def f73ag_f73_asset_growth_efficiency_v080_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v080_signal'] = f73ag_f73_asset_growth_efficiency_v080_signal

def f73ag_f73_asset_growth_efficiency_v081_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v081_signal'] = f73ag_f73_asset_growth_efficiency_v081_signal

def f73ag_f73_asset_growth_efficiency_v082_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v082_signal'] = f73ag_f73_asset_growth_efficiency_v082_signal

def f73ag_f73_asset_growth_efficiency_v083_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v083_signal'] = f73ag_f73_asset_growth_efficiency_v083_signal

def f73ag_f73_asset_growth_efficiency_v084_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v084_signal'] = f73ag_f73_asset_growth_efficiency_v084_signal

def f73ag_f73_asset_growth_efficiency_v085_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v085_signal'] = f73ag_f73_asset_growth_efficiency_v085_signal

def f73ag_f73_asset_growth_efficiency_v086_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v086_signal'] = f73ag_f73_asset_growth_efficiency_v086_signal

def f73ag_f73_asset_growth_efficiency_v087_signal(netinc, sharesbas):
    res = (netinc / sharesbas).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v087_signal'] = f73ag_f73_asset_growth_efficiency_v087_signal

def f73ag_f73_asset_growth_efficiency_v088_signal(netinc, sharesbas):
    res = (netinc / sharesbas).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v088_signal'] = f73ag_f73_asset_growth_efficiency_v088_signal

def f73ag_f73_asset_growth_efficiency_v089_signal(ebitda, sharesbas):
    res = (ebitda / sharesbas).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v089_signal'] = f73ag_f73_asset_growth_efficiency_v089_signal

def f73ag_f73_asset_growth_efficiency_v090_signal(ebitda, sharesbas):
    res = (ebitda / sharesbas).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v090_signal'] = f73ag_f73_asset_growth_efficiency_v090_signal

def f73ag_f73_asset_growth_efficiency_v091_signal(assets, currentratio):
    res = (assets / currentratio).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v091_signal'] = f73ag_f73_asset_growth_efficiency_v091_signal

def f73ag_f73_asset_growth_efficiency_v092_signal(assets, currentratio):
    res = (assets / currentratio).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v092_signal'] = f73ag_f73_asset_growth_efficiency_v092_signal

def f73ag_f73_asset_growth_efficiency_v093_signal(revenue, currentratio):
    res = (revenue / currentratio).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v093_signal'] = f73ag_f73_asset_growth_efficiency_v093_signal

def f73ag_f73_asset_growth_efficiency_v094_signal(revenue, currentratio):
    res = (revenue / currentratio).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v094_signal'] = f73ag_f73_asset_growth_efficiency_v094_signal

def f73ag_f73_asset_growth_efficiency_v095_signal(assets, gp):
    res = (assets / gp).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v095_signal'] = f73ag_f73_asset_growth_efficiency_v095_signal

def f73ag_f73_asset_growth_efficiency_v096_signal(assets, opinc):
    res = (assets / opinc).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v096_signal'] = f73ag_f73_asset_growth_efficiency_v096_signal

def f73ag_f73_asset_growth_efficiency_v097_signal(assets, fcf):
    res = (assets / fcf).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v097_signal'] = f73ag_f73_asset_growth_efficiency_v097_signal

def f73ag_f73_asset_growth_efficiency_v098_signal(assets, ncfo):
    res = (assets / ncfo).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v098_signal'] = f73ag_f73_asset_growth_efficiency_v098_signal

def f73ag_f73_asset_growth_efficiency_v099_signal(revenue, equity):
    res = (revenue / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v099_signal'] = f73ag_f73_asset_growth_efficiency_v099_signal

def f73ag_f73_asset_growth_efficiency_v100_signal(revenue, equity):
    res = (revenue / equity).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v100_signal'] = f73ag_f73_asset_growth_efficiency_v100_signal

def f73ag_f73_asset_growth_efficiency_v101_signal(ebitda, equity):
    res = (ebitda / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v101_signal'] = f73ag_f73_asset_growth_efficiency_v101_signal

def f73ag_f73_asset_growth_efficiency_v102_signal(ebitda, equity):
    res = (ebitda / equity).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v102_signal'] = f73ag_f73_asset_growth_efficiency_v102_signal

def f73ag_f73_asset_growth_efficiency_v103_signal(netinc, equity):
    res = (netinc / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v103_signal'] = f73ag_f73_asset_growth_efficiency_v103_signal

def f73ag_f73_asset_growth_efficiency_v104_signal(netinc, equity):
    res = (netinc / equity).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v104_signal'] = f73ag_f73_asset_growth_efficiency_v104_signal

def f73ag_f73_asset_growth_efficiency_v105_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v105_signal'] = f73ag_f73_asset_growth_efficiency_v105_signal

def f73ag_f73_asset_growth_efficiency_v106_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v106_signal'] = f73ag_f73_asset_growth_efficiency_v106_signal

def f73ag_f73_asset_growth_efficiency_v107_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v107_signal'] = f73ag_f73_asset_growth_efficiency_v107_signal

def f73ag_f73_asset_growth_efficiency_v108_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v108_signal'] = f73ag_f73_asset_growth_efficiency_v108_signal

def f73ag_f73_asset_growth_efficiency_v109_signal(netinc, liabilities):
    res = (netinc / liabilities).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v109_signal'] = f73ag_f73_asset_growth_efficiency_v109_signal

def f73ag_f73_asset_growth_efficiency_v110_signal(netinc, liabilities):
    res = (netinc / liabilities).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v110_signal'] = f73ag_f73_asset_growth_efficiency_v110_signal

def f73ag_f73_asset_growth_efficiency_v111_signal(assets, revenue, equity):
    res = (assets / (revenue + equity)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v111_signal'] = f73ag_f73_asset_growth_efficiency_v111_signal

def f73ag_f73_asset_growth_efficiency_v112_signal(assets, revenue, equity):
    res = (assets / (revenue + equity)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v112_signal'] = f73ag_f73_asset_growth_efficiency_v112_signal

def f73ag_f73_asset_growth_efficiency_v113_signal(assets, ebitda, netinc):
    res = (assets / (ebitda + netinc)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v113_signal'] = f73ag_f73_asset_growth_efficiency_v113_signal

def f73ag_f73_asset_growth_efficiency_v114_signal(assets, ebitda, netinc):
    res = (assets / (ebitda + netinc)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v114_signal'] = f73ag_f73_asset_growth_efficiency_v114_signal

def f73ag_f73_asset_growth_efficiency_v115_signal(revenue, assets):
    res = revenue.diff(10) / assets.diff(10)
    return res.rolling(252).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v115_signal'] = f73ag_f73_asset_growth_efficiency_v115_signal

def f73ag_f73_asset_growth_efficiency_v116_signal(revenue, assets):
    res = revenue.diff(21) / assets.diff(21)
    return res.rolling(5).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v116_signal'] = f73ag_f73_asset_growth_efficiency_v116_signal

def f73ag_f73_asset_growth_efficiency_v117_signal(ebitda, assets):
    res = ebitda.diff(10) / assets.diff(10)
    return res.rolling(42).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v117_signal'] = f73ag_f73_asset_growth_efficiency_v117_signal

def f73ag_f73_asset_growth_efficiency_v118_signal(ebitda, assets):
    res = ebitda.diff(21) / assets.diff(21)
    return res.rolling(42).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v118_signal'] = f73ag_f73_asset_growth_efficiency_v118_signal

def f73ag_f73_asset_growth_efficiency_v119_signal(netinc, assets):
    res = netinc.diff(10) / assets.diff(10)
    return res.rolling(42).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v119_signal'] = f73ag_f73_asset_growth_efficiency_v119_signal

def f73ag_f73_asset_growth_efficiency_v120_signal(netinc, assets):
    res = netinc.diff(21) / assets.diff(21)
    return res.rolling(126).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v120_signal'] = f73ag_f73_asset_growth_efficiency_v120_signal

def f73ag_f73_asset_growth_efficiency_v121_signal(assets, revenue):
    res = (assets / revenue).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v121_signal'] = f73ag_f73_asset_growth_efficiency_v121_signal

def f73ag_f73_asset_growth_efficiency_v122_signal(assets, revenue):
    res = (assets / revenue).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v122_signal'] = f73ag_f73_asset_growth_efficiency_v122_signal

def f73ag_f73_asset_growth_efficiency_v123_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v123_signal'] = f73ag_f73_asset_growth_efficiency_v123_signal

def f73ag_f73_asset_growth_efficiency_v124_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v124_signal'] = f73ag_f73_asset_growth_efficiency_v124_signal

def f73ag_f73_asset_growth_efficiency_v125_signal(assets, netinc):
    res = (assets / netinc).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v125_signal'] = f73ag_f73_asset_growth_efficiency_v125_signal

def f73ag_f73_asset_growth_efficiency_v126_signal(assets, netinc):
    res = (assets / netinc).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v126_signal'] = f73ag_f73_asset_growth_efficiency_v126_signal

def f73ag_f73_asset_growth_efficiency_v127_signal(assets, equity):
    res = (assets / equity).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v127_signal'] = f73ag_f73_asset_growth_efficiency_v127_signal

def f73ag_f73_asset_growth_efficiency_v128_signal(assets, equity):
    res = (assets / equity).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v128_signal'] = f73ag_f73_asset_growth_efficiency_v128_signal

def f73ag_f73_asset_growth_efficiency_v129_signal(assets, liabilities):
    res = (assets / liabilities).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v129_signal'] = f73ag_f73_asset_growth_efficiency_v129_signal

def f73ag_f73_asset_growth_efficiency_v130_signal(assets, liabilities):
    res = (assets / liabilities).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v130_signal'] = f73ag_f73_asset_growth_efficiency_v130_signal

def f73ag_f73_asset_growth_efficiency_v131_signal(assets, workingcapital):
    res = (assets / workingcapital).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v131_signal'] = f73ag_f73_asset_growth_efficiency_v131_signal

def f73ag_f73_asset_growth_efficiency_v132_signal(assets, workingcapital):
    res = (assets / workingcapital).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v132_signal'] = f73ag_f73_asset_growth_efficiency_v132_signal

def f73ag_f73_asset_growth_efficiency_v133_signal(assets, marketcap):
    res = (assets / marketcap).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v133_signal'] = f73ag_f73_asset_growth_efficiency_v133_signal

def f73ag_f73_asset_growth_efficiency_v134_signal(assets, marketcap):
    res = (assets / marketcap).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v134_signal'] = f73ag_f73_asset_growth_efficiency_v134_signal

def f73ag_f73_asset_growth_efficiency_v135_signal(assets, ev):
    res = (assets / ev).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v135_signal'] = f73ag_f73_asset_growth_efficiency_v135_signal

def f73ag_f73_asset_growth_efficiency_v136_signal(assets, ev):
    res = (assets / ev).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v136_signal'] = f73ag_f73_asset_growth_efficiency_v136_signal

def f73ag_f73_asset_growth_efficiency_v137_signal(assets, capex):
    res = (assets / capex).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v137_signal'] = f73ag_f73_asset_growth_efficiency_v137_signal

def f73ag_f73_asset_growth_efficiency_v138_signal(assets, capex):
    res = (assets / capex).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v138_signal'] = f73ag_f73_asset_growth_efficiency_v138_signal

def f73ag_f73_asset_growth_efficiency_v139_signal(assets, fcf):
    res = (assets / fcf).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v139_signal'] = f73ag_f73_asset_growth_efficiency_v139_signal

def f73ag_f73_asset_growth_efficiency_v140_signal(assets, fcf):
    res = (assets / fcf).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v140_signal'] = f73ag_f73_asset_growth_efficiency_v140_signal

def f73ag_f73_asset_growth_efficiency_v141_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v141_signal'] = f73ag_f73_asset_growth_efficiency_v141_signal

def f73ag_f73_asset_growth_efficiency_v142_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v142_signal'] = f73ag_f73_asset_growth_efficiency_v142_signal

def f73ag_f73_asset_growth_efficiency_v143_signal(assets, gp):
    res = (assets / gp).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v143_signal'] = f73ag_f73_asset_growth_efficiency_v143_signal

def f73ag_f73_asset_growth_efficiency_v144_signal(assets, gp):
    res = (assets / gp).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v144_signal'] = f73ag_f73_asset_growth_efficiency_v144_signal

def f73ag_f73_asset_growth_efficiency_v145_signal(assets, opinc):
    res = (assets / opinc).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v145_signal'] = f73ag_f73_asset_growth_efficiency_v145_signal

def f73ag_f73_asset_growth_efficiency_v146_signal(assets, opinc):
    res = (assets / opinc).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v146_signal'] = f73ag_f73_asset_growth_efficiency_v146_signal

def f73ag_f73_asset_growth_efficiency_v147_signal(assets, retearn):
    res = (assets / retearn).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v147_signal'] = f73ag_f73_asset_growth_efficiency_v147_signal

def f73ag_f73_asset_growth_efficiency_v148_signal(assets, retearn):
    res = (assets / retearn).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v148_signal'] = f73ag_f73_asset_growth_efficiency_v148_signal

def f73ag_f73_asset_growth_efficiency_v149_signal(assets, debt):
    res = (assets / debt).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v149_signal'] = f73ag_f73_asset_growth_efficiency_v149_signal

def f73ag_f73_asset_growth_efficiency_v150_signal(assets, debt):
    res = (assets / debt).pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v150_signal'] = f73ag_f73_asset_growth_efficiency_v150_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "opinc": np.random.uniform(40, 180, n),
        "netinc": np.random.uniform(20, 100, n),
        "assets": np.random.uniform(2000, 5000, n),
        "equity": np.random.uniform(1000, 3000, n),
        "marketcap": np.random.uniform(5000, 20000, n),
        "ev": np.random.uniform(6000, 25000, n),
        "closeadj": np.random.uniform(10, 100, n),
        "volume": np.random.uniform(100000, 1000000, n),
        "ncfo": np.random.uniform(30, 150, n),
        "capex": np.random.uniform(10, 50, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n),
        "workingcapital": np.random.uniform(200, 800, n),
        "gp": np.random.uniform(100, 400, n),
        "retearn": np.random.uniform(500, 2000, n),
        "fcf": np.random.uniform(20, 120, n),
        "sharesbas": np.random.uniform(10, 100, n),
        "currentratio": np.random.uniform(0.5, 3.0, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}")
                assert corr_matrix.iloc[i, j] <= 0.95, f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}"
    print(f"Self-test passed for {os.path.basename(__file__)}")

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
