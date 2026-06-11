import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f42tax_f42_tax_efficiency_momentum_base_v076_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v076_signal'] = f42tax_f42_tax_efficiency_momentum_base_v076_signal

def f42tax_f42_tax_efficiency_momentum_base_v077_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v077_signal'] = f42tax_f42_tax_efficiency_momentum_base_v077_signal

def f42tax_f42_tax_efficiency_momentum_base_v078_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v078_signal'] = f42tax_f42_tax_efficiency_momentum_base_v078_signal

def f42tax_f42_tax_efficiency_momentum_base_v079_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v079_signal'] = f42tax_f42_tax_efficiency_momentum_base_v079_signal

def f42tax_f42_tax_efficiency_momentum_base_v080_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v080_signal'] = f42tax_f42_tax_efficiency_momentum_base_v080_signal

def f42tax_f42_tax_efficiency_momentum_base_v081_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v081_signal'] = f42tax_f42_tax_efficiency_momentum_base_v081_signal

def f42tax_f42_tax_efficiency_momentum_base_v082_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v082_signal'] = f42tax_f42_tax_efficiency_momentum_base_v082_signal

def f42tax_f42_tax_efficiency_momentum_base_v083_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v083_signal'] = f42tax_f42_tax_efficiency_momentum_base_v083_signal

def f42tax_f42_tax_efficiency_momentum_base_v084_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v084_signal'] = f42tax_f42_tax_efficiency_momentum_base_v084_signal

def f42tax_f42_tax_efficiency_momentum_base_v085_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v085_signal'] = f42tax_f42_tax_efficiency_momentum_base_v085_signal

def f42tax_f42_tax_efficiency_momentum_base_v086_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v086_signal'] = f42tax_f42_tax_efficiency_momentum_base_v086_signal

def f42tax_f42_tax_efficiency_momentum_base_v087_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v087_signal'] = f42tax_f42_tax_efficiency_momentum_base_v087_signal

def f42tax_f42_tax_efficiency_momentum_base_v088_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v088_signal'] = f42tax_f42_tax_efficiency_momentum_base_v088_signal

def f42tax_f42_tax_efficiency_momentum_base_v089_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v089_signal'] = f42tax_f42_tax_efficiency_momentum_base_v089_signal

def f42tax_f42_tax_efficiency_momentum_base_v090_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v090_signal'] = f42tax_f42_tax_efficiency_momentum_base_v090_signal

def f42tax_f42_tax_efficiency_momentum_base_v091_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v091_signal'] = f42tax_f42_tax_efficiency_momentum_base_v091_signal

def f42tax_f42_tax_efficiency_momentum_base_v092_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v092_signal'] = f42tax_f42_tax_efficiency_momentum_base_v092_signal

def f42tax_f42_tax_efficiency_momentum_base_v093_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v093_signal'] = f42tax_f42_tax_efficiency_momentum_base_v093_signal

def f42tax_f42_tax_efficiency_momentum_base_v094_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v094_signal'] = f42tax_f42_tax_efficiency_momentum_base_v094_signal

def f42tax_f42_tax_efficiency_momentum_base_v095_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v095_signal'] = f42tax_f42_tax_efficiency_momentum_base_v095_signal

def f42tax_f42_tax_efficiency_momentum_base_v096_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).mean())/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v096_signal'] = f42tax_f42_tax_efficiency_momentum_base_v096_signal

def f42tax_f42_tax_efficiency_momentum_base_v097_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).mean())/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v097_signal'] = f42tax_f42_tax_efficiency_momentum_base_v097_signal

def f42tax_f42_tax_efficiency_momentum_base_v098_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).mean())/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v098_signal'] = f42tax_f42_tax_efficiency_momentum_base_v098_signal

def f42tax_f42_tax_efficiency_momentum_base_v099_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).mean())/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v099_signal'] = f42tax_f42_tax_efficiency_momentum_base_v099_signal

def f42tax_f42_tax_efficiency_momentum_base_v100_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).mean())/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v100_signal'] = f42tax_f42_tax_efficiency_momentum_base_v100_signal

def f42tax_f42_tax_efficiency_momentum_base_v101_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).median())/(((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v101_signal'] = f42tax_f42_tax_efficiency_momentum_base_v101_signal

def f42tax_f42_tax_efficiency_momentum_base_v102_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).median())/(((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v102_signal'] = f42tax_f42_tax_efficiency_momentum_base_v102_signal

def f42tax_f42_tax_efficiency_momentum_base_v103_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).median())/(((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v103_signal'] = f42tax_f42_tax_efficiency_momentum_base_v103_signal

def f42tax_f42_tax_efficiency_momentum_base_v104_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).median())/(((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v104_signal'] = f42tax_f42_tax_efficiency_momentum_base_v104_signal

def f42tax_f42_tax_efficiency_momentum_base_v105_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).median())/(((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v105_signal'] = f42tax_f42_tax_efficiency_momentum_base_v105_signal

def f42tax_f42_tax_efficiency_momentum_base_v106_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).gt((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v106_signal'] = f42tax_f42_tax_efficiency_momentum_base_v106_signal

def f42tax_f42_tax_efficiency_momentum_base_v107_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).gt((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v107_signal'] = f42tax_f42_tax_efficiency_momentum_base_v107_signal

def f42tax_f42_tax_efficiency_momentum_base_v108_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).gt((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v108_signal'] = f42tax_f42_tax_efficiency_momentum_base_v108_signal

def f42tax_f42_tax_efficiency_momentum_base_v109_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).gt((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v109_signal'] = f42tax_f42_tax_efficiency_momentum_base_v109_signal

def f42tax_f42_tax_efficiency_momentum_base_v110_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).gt((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v110_signal'] = f42tax_f42_tax_efficiency_momentum_base_v110_signal

def f42tax_f42_tax_efficiency_momentum_base_v111_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v111_signal'] = f42tax_f42_tax_efficiency_momentum_base_v111_signal

def f42tax_f42_tax_efficiency_momentum_base_v112_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v112_signal'] = f42tax_f42_tax_efficiency_momentum_base_v112_signal

def f42tax_f42_tax_efficiency_momentum_base_v113_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v113_signal'] = f42tax_f42_tax_efficiency_momentum_base_v113_signal

def f42tax_f42_tax_efficiency_momentum_base_v114_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v114_signal'] = f42tax_f42_tax_efficiency_momentum_base_v114_signal

def f42tax_f42_tax_efficiency_momentum_base_v115_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v115_signal'] = f42tax_f42_tax_efficiency_momentum_base_v115_signal

def f42tax_f42_tax_efficiency_momentum_base_v116_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v116_signal'] = f42tax_f42_tax_efficiency_momentum_base_v116_signal

def f42tax_f42_tax_efficiency_momentum_base_v117_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v117_signal'] = f42tax_f42_tax_efficiency_momentum_base_v117_signal

def f42tax_f42_tax_efficiency_momentum_base_v118_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v118_signal'] = f42tax_f42_tax_efficiency_momentum_base_v118_signal

def f42tax_f42_tax_efficiency_momentum_base_v119_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v119_signal'] = f42tax_f42_tax_efficiency_momentum_base_v119_signal

def f42tax_f42_tax_efficiency_momentum_base_v120_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v120_signal'] = f42tax_f42_tax_efficiency_momentum_base_v120_signal

def f42tax_f42_tax_efficiency_momentum_base_v121_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v121_signal'] = f42tax_f42_tax_efficiency_momentum_base_v121_signal

def f42tax_f42_tax_efficiency_momentum_base_v122_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v122_signal'] = f42tax_f42_tax_efficiency_momentum_base_v122_signal

def f42tax_f42_tax_efficiency_momentum_base_v123_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v123_signal'] = f42tax_f42_tax_efficiency_momentum_base_v123_signal

def f42tax_f42_tax_efficiency_momentum_base_v124_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v124_signal'] = f42tax_f42_tax_efficiency_momentum_base_v124_signal

def f42tax_f42_tax_efficiency_momentum_base_v125_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v125_signal'] = f42tax_f42_tax_efficiency_momentum_base_v125_signal

def f42tax_f42_tax_efficiency_momentum_base_v126_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).min())/((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v126_signal'] = f42tax_f42_tax_efficiency_momentum_base_v126_signal

def f42tax_f42_tax_efficiency_momentum_base_v127_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).min())/((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v127_signal'] = f42tax_f42_tax_efficiency_momentum_base_v127_signal

def f42tax_f42_tax_efficiency_momentum_base_v128_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).min())/((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v128_signal'] = f42tax_f42_tax_efficiency_momentum_base_v128_signal

def f42tax_f42_tax_efficiency_momentum_base_v129_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).min())/((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v129_signal'] = f42tax_f42_tax_efficiency_momentum_base_v129_signal

def f42tax_f42_tax_efficiency_momentum_base_v130_signal(taxexp, netinc):
    res = (((taxexp / (taxexp + netinc).replace(0, np.nan))-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).min())/((taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).max()-(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v130_signal'] = f42tax_f42_tax_efficiency_momentum_base_v130_signal

def f42tax_f42_tax_efficiency_momentum_base_v131_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v131_signal'] = f42tax_f42_tax_efficiency_momentum_base_v131_signal

def f42tax_f42_tax_efficiency_momentum_base_v132_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v132_signal'] = f42tax_f42_tax_efficiency_momentum_base_v132_signal

def f42tax_f42_tax_efficiency_momentum_base_v133_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v133_signal'] = f42tax_f42_tax_efficiency_momentum_base_v133_signal

def f42tax_f42_tax_efficiency_momentum_base_v134_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v134_signal'] = f42tax_f42_tax_efficiency_momentum_base_v134_signal

def f42tax_f42_tax_efficiency_momentum_base_v135_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v135_signal'] = f42tax_f42_tax_efficiency_momentum_base_v135_signal

def f42tax_f42_tax_efficiency_momentum_base_v136_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v136_signal'] = f42tax_f42_tax_efficiency_momentum_base_v136_signal

def f42tax_f42_tax_efficiency_momentum_base_v137_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v137_signal'] = f42tax_f42_tax_efficiency_momentum_base_v137_signal

def f42tax_f42_tax_efficiency_momentum_base_v138_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v138_signal'] = f42tax_f42_tax_efficiency_momentum_base_v138_signal

def f42tax_f42_tax_efficiency_momentum_base_v139_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v139_signal'] = f42tax_f42_tax_efficiency_momentum_base_v139_signal

def f42tax_f42_tax_efficiency_momentum_base_v140_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan))/(taxexp / (taxexp + netinc).replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v140_signal'] = f42tax_f42_tax_efficiency_momentum_base_v140_signal

def f42tax_f42_tax_efficiency_momentum_base_v141_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=21).mean() - (taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v141_signal'] = f42tax_f42_tax_efficiency_momentum_base_v141_signal

def f42tax_f42_tax_efficiency_momentum_base_v142_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=63).mean() - (taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v142_signal'] = f42tax_f42_tax_efficiency_momentum_base_v142_signal

def f42tax_f42_tax_efficiency_momentum_base_v143_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=126).mean() - (taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v143_signal'] = f42tax_f42_tax_efficiency_momentum_base_v143_signal

def f42tax_f42_tax_efficiency_momentum_base_v144_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=252).mean() - (taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v144_signal'] = f42tax_f42_tax_efficiency_momentum_base_v144_signal

def f42tax_f42_tax_efficiency_momentum_base_v145_signal(taxexp, netinc):
    res = ((taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=504).mean() - (taxexp / (taxexp + netinc).replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v145_signal'] = f42tax_f42_tax_efficiency_momentum_base_v145_signal

def f42tax_f42_tax_efficiency_momentum_base_v146_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v146_signal'] = f42tax_f42_tax_efficiency_momentum_base_v146_signal

def f42tax_f42_tax_efficiency_momentum_base_v147_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v147_signal'] = f42tax_f42_tax_efficiency_momentum_base_v147_signal

def f42tax_f42_tax_efficiency_momentum_base_v148_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v148_signal'] = f42tax_f42_tax_efficiency_momentum_base_v148_signal

def f42tax_f42_tax_efficiency_momentum_base_v149_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v149_signal'] = f42tax_f42_tax_efficiency_momentum_base_v149_signal

def f42tax_f42_tax_efficiency_momentum_base_v150_signal(taxexp, netinc):
    res = (taxexp / (taxexp + netinc).replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f42tax_f42_tax_efficiency_momentum_base_v150_signal'] = f42tax_f42_tax_efficiency_momentum_base_v150_signal

