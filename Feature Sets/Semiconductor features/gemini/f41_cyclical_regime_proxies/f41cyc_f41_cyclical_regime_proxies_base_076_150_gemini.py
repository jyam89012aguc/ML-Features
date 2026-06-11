import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f41cyc_f41_cyclical_regime_proxies_base_v076_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v076_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v076_signal

def f41cyc_f41_cyclical_regime_proxies_base_v077_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v077_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v077_signal

def f41cyc_f41_cyclical_regime_proxies_base_v078_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v078_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v078_signal

def f41cyc_f41_cyclical_regime_proxies_base_v079_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v079_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v079_signal

def f41cyc_f41_cyclical_regime_proxies_base_v080_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v080_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v080_signal

def f41cyc_f41_cyclical_regime_proxies_base_v081_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v081_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v081_signal

def f41cyc_f41_cyclical_regime_proxies_base_v082_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v082_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v082_signal

def f41cyc_f41_cyclical_regime_proxies_base_v083_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v083_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v083_signal

def f41cyc_f41_cyclical_regime_proxies_base_v084_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v084_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v084_signal

def f41cyc_f41_cyclical_regime_proxies_base_v085_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v085_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v085_signal

def f41cyc_f41_cyclical_regime_proxies_base_v086_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v086_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v086_signal

def f41cyc_f41_cyclical_regime_proxies_base_v087_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v087_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v087_signal

def f41cyc_f41_cyclical_regime_proxies_base_v088_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v088_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v088_signal

def f41cyc_f41_cyclical_regime_proxies_base_v089_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v089_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v089_signal

def f41cyc_f41_cyclical_regime_proxies_base_v090_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v090_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v090_signal

def f41cyc_f41_cyclical_regime_proxies_base_v091_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v091_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v091_signal

def f41cyc_f41_cyclical_regime_proxies_base_v092_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v092_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v092_signal

def f41cyc_f41_cyclical_regime_proxies_base_v093_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v093_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v093_signal

def f41cyc_f41_cyclical_regime_proxies_base_v094_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v094_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v094_signal

def f41cyc_f41_cyclical_regime_proxies_base_v095_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v095_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v095_signal

def f41cyc_f41_cyclical_regime_proxies_base_v096_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).mean())/(capex / revenue.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v096_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v096_signal

def f41cyc_f41_cyclical_regime_proxies_base_v097_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(63).mean())/(capex / revenue.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v097_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v097_signal

def f41cyc_f41_cyclical_regime_proxies_base_v098_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(126).mean())/(capex / revenue.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v098_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v098_signal

def f41cyc_f41_cyclical_regime_proxies_base_v099_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(252).mean())/(capex / revenue.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v099_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v099_signal

def f41cyc_f41_cyclical_regime_proxies_base_v100_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v100_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v100_signal

def f41cyc_f41_cyclical_regime_proxies_base_v101_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v101_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v101_signal

def f41cyc_f41_cyclical_regime_proxies_base_v102_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(63).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v102_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v102_signal

def f41cyc_f41_cyclical_regime_proxies_base_v103_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(126).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v103_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v103_signal

def f41cyc_f41_cyclical_regime_proxies_base_v104_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(252).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v104_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v104_signal

def f41cyc_f41_cyclical_regime_proxies_base_v105_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v105_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v105_signal

def f41cyc_f41_cyclical_regime_proxies_base_v106_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v106_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v106_signal

def f41cyc_f41_cyclical_regime_proxies_base_v107_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v107_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v107_signal

def f41cyc_f41_cyclical_regime_proxies_base_v108_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v108_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v108_signal

def f41cyc_f41_cyclical_regime_proxies_base_v109_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v109_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v109_signal

def f41cyc_f41_cyclical_regime_proxies_base_v110_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v110_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v110_signal

def f41cyc_f41_cyclical_regime_proxies_base_v111_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v111_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v111_signal

def f41cyc_f41_cyclical_regime_proxies_base_v112_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v112_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v112_signal

def f41cyc_f41_cyclical_regime_proxies_base_v113_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v113_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v113_signal

def f41cyc_f41_cyclical_regime_proxies_base_v114_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v114_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v114_signal

def f41cyc_f41_cyclical_regime_proxies_base_v115_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v115_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v115_signal

def f41cyc_f41_cyclical_regime_proxies_base_v116_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v116_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v116_signal

def f41cyc_f41_cyclical_regime_proxies_base_v117_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v117_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v117_signal

def f41cyc_f41_cyclical_regime_proxies_base_v118_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v118_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v118_signal

def f41cyc_f41_cyclical_regime_proxies_base_v119_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v119_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v119_signal

def f41cyc_f41_cyclical_regime_proxies_base_v120_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v120_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v120_signal

def f41cyc_f41_cyclical_regime_proxies_base_v121_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v121_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v121_signal

def f41cyc_f41_cyclical_regime_proxies_base_v122_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).rolling(63).max()-(capex / revenue.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v122_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v122_signal

def f41cyc_f41_cyclical_regime_proxies_base_v123_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).rolling(126).max()-(capex / revenue.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v123_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v123_signal

def f41cyc_f41_cyclical_regime_proxies_base_v124_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).rolling(252).max()-(capex / revenue.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v124_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v124_signal

def f41cyc_f41_cyclical_regime_proxies_base_v125_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v125_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v125_signal

def f41cyc_f41_cyclical_regime_proxies_base_v126_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v126_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v126_signal

def f41cyc_f41_cyclical_regime_proxies_base_v127_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(63).min())/((capex / revenue.replace(0, np.nan)).rolling(63).max()-(capex / revenue.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v127_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v127_signal

def f41cyc_f41_cyclical_regime_proxies_base_v128_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(126).min())/((capex / revenue.replace(0, np.nan)).rolling(126).max()-(capex / revenue.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v128_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v128_signal

def f41cyc_f41_cyclical_regime_proxies_base_v129_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(252).min())/((capex / revenue.replace(0, np.nan)).rolling(252).max()-(capex / revenue.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v129_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v129_signal

def f41cyc_f41_cyclical_regime_proxies_base_v130_signal(revenue, capex):
    res = (((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).min())/((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v130_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v130_signal

def f41cyc_f41_cyclical_regime_proxies_base_v131_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v131_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v131_signal

def f41cyc_f41_cyclical_regime_proxies_base_v132_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v132_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v132_signal

def f41cyc_f41_cyclical_regime_proxies_base_v133_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v133_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v133_signal

def f41cyc_f41_cyclical_regime_proxies_base_v134_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v134_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v134_signal

def f41cyc_f41_cyclical_regime_proxies_base_v135_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v135_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v135_signal

def f41cyc_f41_cyclical_regime_proxies_base_v136_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v136_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v136_signal

def f41cyc_f41_cyclical_regime_proxies_base_v137_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v137_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v137_signal

def f41cyc_f41_cyclical_regime_proxies_base_v138_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v138_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v138_signal

def f41cyc_f41_cyclical_regime_proxies_base_v139_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v139_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v139_signal

def f41cyc_f41_cyclical_regime_proxies_base_v140_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v140_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v140_signal

def f41cyc_f41_cyclical_regime_proxies_base_v141_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).ewm(span=21).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v141_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v141_signal

def f41cyc_f41_cyclical_regime_proxies_base_v142_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).ewm(span=63).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v142_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v142_signal

def f41cyc_f41_cyclical_regime_proxies_base_v143_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).ewm(span=126).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v143_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v143_signal

def f41cyc_f41_cyclical_regime_proxies_base_v144_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v144_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v144_signal

def f41cyc_f41_cyclical_regime_proxies_base_v145_signal(revenue, capex):
    res = ((capex / revenue.replace(0, np.nan)).ewm(span=504).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v145_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v145_signal

def f41cyc_f41_cyclical_regime_proxies_base_v146_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v146_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v146_signal

def f41cyc_f41_cyclical_regime_proxies_base_v147_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v147_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v147_signal

def f41cyc_f41_cyclical_regime_proxies_base_v148_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v148_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v148_signal

def f41cyc_f41_cyclical_regime_proxies_base_v149_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v149_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v149_signal

def f41cyc_f41_cyclical_regime_proxies_base_v150_signal(revenue, capex):
    res = (capex / revenue.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_base_v150_signal'] = f41cyc_f41_cyclical_regime_proxies_base_v150_signal

