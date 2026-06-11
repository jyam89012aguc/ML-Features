import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f47wcv_f47_working_capital_velocity_base_v076_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v076_signal'] = f47wcv_f47_working_capital_velocity_base_v076_signal

def f47wcv_f47_working_capital_velocity_base_v077_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v077_signal'] = f47wcv_f47_working_capital_velocity_base_v077_signal

def f47wcv_f47_working_capital_velocity_base_v078_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v078_signal'] = f47wcv_f47_working_capital_velocity_base_v078_signal

def f47wcv_f47_working_capital_velocity_base_v079_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v079_signal'] = f47wcv_f47_working_capital_velocity_base_v079_signal

def f47wcv_f47_working_capital_velocity_base_v080_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v080_signal'] = f47wcv_f47_working_capital_velocity_base_v080_signal

def f47wcv_f47_working_capital_velocity_base_v081_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v081_signal'] = f47wcv_f47_working_capital_velocity_base_v081_signal

def f47wcv_f47_working_capital_velocity_base_v082_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v082_signal'] = f47wcv_f47_working_capital_velocity_base_v082_signal

def f47wcv_f47_working_capital_velocity_base_v083_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v083_signal'] = f47wcv_f47_working_capital_velocity_base_v083_signal

def f47wcv_f47_working_capital_velocity_base_v084_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v084_signal'] = f47wcv_f47_working_capital_velocity_base_v084_signal

def f47wcv_f47_working_capital_velocity_base_v085_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v085_signal'] = f47wcv_f47_working_capital_velocity_base_v085_signal

def f47wcv_f47_working_capital_velocity_base_v086_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v086_signal'] = f47wcv_f47_working_capital_velocity_base_v086_signal

def f47wcv_f47_working_capital_velocity_base_v087_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v087_signal'] = f47wcv_f47_working_capital_velocity_base_v087_signal

def f47wcv_f47_working_capital_velocity_base_v088_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v088_signal'] = f47wcv_f47_working_capital_velocity_base_v088_signal

def f47wcv_f47_working_capital_velocity_base_v089_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v089_signal'] = f47wcv_f47_working_capital_velocity_base_v089_signal

def f47wcv_f47_working_capital_velocity_base_v090_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v090_signal'] = f47wcv_f47_working_capital_velocity_base_v090_signal

def f47wcv_f47_working_capital_velocity_base_v091_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v091_signal'] = f47wcv_f47_working_capital_velocity_base_v091_signal

def f47wcv_f47_working_capital_velocity_base_v092_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v092_signal'] = f47wcv_f47_working_capital_velocity_base_v092_signal

def f47wcv_f47_working_capital_velocity_base_v093_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v093_signal'] = f47wcv_f47_working_capital_velocity_base_v093_signal

def f47wcv_f47_working_capital_velocity_base_v094_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v094_signal'] = f47wcv_f47_working_capital_velocity_base_v094_signal

def f47wcv_f47_working_capital_velocity_base_v095_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v095_signal'] = f47wcv_f47_working_capital_velocity_base_v095_signal

def f47wcv_f47_working_capital_velocity_base_v096_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v096_signal'] = f47wcv_f47_working_capital_velocity_base_v096_signal

def f47wcv_f47_working_capital_velocity_base_v097_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v097_signal'] = f47wcv_f47_working_capital_velocity_base_v097_signal

def f47wcv_f47_working_capital_velocity_base_v098_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v098_signal'] = f47wcv_f47_working_capital_velocity_base_v098_signal

def f47wcv_f47_working_capital_velocity_base_v099_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v099_signal'] = f47wcv_f47_working_capital_velocity_base_v099_signal

def f47wcv_f47_working_capital_velocity_base_v100_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v100_signal'] = f47wcv_f47_working_capital_velocity_base_v100_signal

def f47wcv_f47_working_capital_velocity_base_v101_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v101_signal'] = f47wcv_f47_working_capital_velocity_base_v101_signal

def f47wcv_f47_working_capital_velocity_base_v102_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v102_signal'] = f47wcv_f47_working_capital_velocity_base_v102_signal

def f47wcv_f47_working_capital_velocity_base_v103_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v103_signal'] = f47wcv_f47_working_capital_velocity_base_v103_signal

def f47wcv_f47_working_capital_velocity_base_v104_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v104_signal'] = f47wcv_f47_working_capital_velocity_base_v104_signal

def f47wcv_f47_working_capital_velocity_base_v105_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v105_signal'] = f47wcv_f47_working_capital_velocity_base_v105_signal

def f47wcv_f47_working_capital_velocity_base_v106_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v106_signal'] = f47wcv_f47_working_capital_velocity_base_v106_signal

def f47wcv_f47_working_capital_velocity_base_v107_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v107_signal'] = f47wcv_f47_working_capital_velocity_base_v107_signal

def f47wcv_f47_working_capital_velocity_base_v108_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v108_signal'] = f47wcv_f47_working_capital_velocity_base_v108_signal

def f47wcv_f47_working_capital_velocity_base_v109_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v109_signal'] = f47wcv_f47_working_capital_velocity_base_v109_signal

def f47wcv_f47_working_capital_velocity_base_v110_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v110_signal'] = f47wcv_f47_working_capital_velocity_base_v110_signal

def f47wcv_f47_working_capital_velocity_base_v111_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v111_signal'] = f47wcv_f47_working_capital_velocity_base_v111_signal

def f47wcv_f47_working_capital_velocity_base_v112_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v112_signal'] = f47wcv_f47_working_capital_velocity_base_v112_signal

def f47wcv_f47_working_capital_velocity_base_v113_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v113_signal'] = f47wcv_f47_working_capital_velocity_base_v113_signal

def f47wcv_f47_working_capital_velocity_base_v114_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v114_signal'] = f47wcv_f47_working_capital_velocity_base_v114_signal

def f47wcv_f47_working_capital_velocity_base_v115_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v115_signal'] = f47wcv_f47_working_capital_velocity_base_v115_signal

def f47wcv_f47_working_capital_velocity_base_v116_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v116_signal'] = f47wcv_f47_working_capital_velocity_base_v116_signal

def f47wcv_f47_working_capital_velocity_base_v117_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v117_signal'] = f47wcv_f47_working_capital_velocity_base_v117_signal

def f47wcv_f47_working_capital_velocity_base_v118_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v118_signal'] = f47wcv_f47_working_capital_velocity_base_v118_signal

def f47wcv_f47_working_capital_velocity_base_v119_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v119_signal'] = f47wcv_f47_working_capital_velocity_base_v119_signal

def f47wcv_f47_working_capital_velocity_base_v120_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v120_signal'] = f47wcv_f47_working_capital_velocity_base_v120_signal

def f47wcv_f47_working_capital_velocity_base_v121_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v121_signal'] = f47wcv_f47_working_capital_velocity_base_v121_signal

def f47wcv_f47_working_capital_velocity_base_v122_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(63).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v122_signal'] = f47wcv_f47_working_capital_velocity_base_v122_signal

def f47wcv_f47_working_capital_velocity_base_v123_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v123_signal'] = f47wcv_f47_working_capital_velocity_base_v123_signal

def f47wcv_f47_working_capital_velocity_base_v124_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(252).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v124_signal'] = f47wcv_f47_working_capital_velocity_base_v124_signal

def f47wcv_f47_working_capital_velocity_base_v125_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v125_signal'] = f47wcv_f47_working_capital_velocity_base_v125_signal

def f47wcv_f47_working_capital_velocity_base_v126_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v126_signal'] = f47wcv_f47_working_capital_velocity_base_v126_signal

def f47wcv_f47_working_capital_velocity_base_v127_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(63).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v127_signal'] = f47wcv_f47_working_capital_velocity_base_v127_signal

def f47wcv_f47_working_capital_velocity_base_v128_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v128_signal'] = f47wcv_f47_working_capital_velocity_base_v128_signal

def f47wcv_f47_working_capital_velocity_base_v129_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(252).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v129_signal'] = f47wcv_f47_working_capital_velocity_base_v129_signal

def f47wcv_f47_working_capital_velocity_base_v130_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v130_signal'] = f47wcv_f47_working_capital_velocity_base_v130_signal

def f47wcv_f47_working_capital_velocity_base_v131_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v131_signal'] = f47wcv_f47_working_capital_velocity_base_v131_signal

def f47wcv_f47_working_capital_velocity_base_v132_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v132_signal'] = f47wcv_f47_working_capital_velocity_base_v132_signal

def f47wcv_f47_working_capital_velocity_base_v133_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v133_signal'] = f47wcv_f47_working_capital_velocity_base_v133_signal

def f47wcv_f47_working_capital_velocity_base_v134_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v134_signal'] = f47wcv_f47_working_capital_velocity_base_v134_signal

def f47wcv_f47_working_capital_velocity_base_v135_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v135_signal'] = f47wcv_f47_working_capital_velocity_base_v135_signal

def f47wcv_f47_working_capital_velocity_base_v136_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v136_signal'] = f47wcv_f47_working_capital_velocity_base_v136_signal

def f47wcv_f47_working_capital_velocity_base_v137_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v137_signal'] = f47wcv_f47_working_capital_velocity_base_v137_signal

def f47wcv_f47_working_capital_velocity_base_v138_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v138_signal'] = f47wcv_f47_working_capital_velocity_base_v138_signal

def f47wcv_f47_working_capital_velocity_base_v139_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v139_signal'] = f47wcv_f47_working_capital_velocity_base_v139_signal

def f47wcv_f47_working_capital_velocity_base_v140_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v140_signal'] = f47wcv_f47_working_capital_velocity_base_v140_signal

def f47wcv_f47_working_capital_velocity_base_v141_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=21).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v141_signal'] = f47wcv_f47_working_capital_velocity_base_v141_signal

def f47wcv_f47_working_capital_velocity_base_v142_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=63).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v142_signal'] = f47wcv_f47_working_capital_velocity_base_v142_signal

def f47wcv_f47_working_capital_velocity_base_v143_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=126).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v143_signal'] = f47wcv_f47_working_capital_velocity_base_v143_signal

def f47wcv_f47_working_capital_velocity_base_v144_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v144_signal'] = f47wcv_f47_working_capital_velocity_base_v144_signal

def f47wcv_f47_working_capital_velocity_base_v145_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v145_signal'] = f47wcv_f47_working_capital_velocity_base_v145_signal

def f47wcv_f47_working_capital_velocity_base_v146_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v146_signal'] = f47wcv_f47_working_capital_velocity_base_v146_signal

def f47wcv_f47_working_capital_velocity_base_v147_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v147_signal'] = f47wcv_f47_working_capital_velocity_base_v147_signal

def f47wcv_f47_working_capital_velocity_base_v148_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v148_signal'] = f47wcv_f47_working_capital_velocity_base_v148_signal

def f47wcv_f47_working_capital_velocity_base_v149_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v149_signal'] = f47wcv_f47_working_capital_velocity_base_v149_signal

def f47wcv_f47_working_capital_velocity_base_v150_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v150_signal'] = f47wcv_f47_working_capital_velocity_base_v150_signal

