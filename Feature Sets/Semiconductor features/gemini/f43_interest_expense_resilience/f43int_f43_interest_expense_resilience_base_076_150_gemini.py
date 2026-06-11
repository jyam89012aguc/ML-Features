import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f43int_f43_interest_expense_resilience_base_v076_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v076_signal'] = f43int_f43_interest_expense_resilience_base_v076_signal

def f43int_f43_interest_expense_resilience_base_v077_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v077_signal'] = f43int_f43_interest_expense_resilience_base_v077_signal

def f43int_f43_interest_expense_resilience_base_v078_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v078_signal'] = f43int_f43_interest_expense_resilience_base_v078_signal

def f43int_f43_interest_expense_resilience_base_v079_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v079_signal'] = f43int_f43_interest_expense_resilience_base_v079_signal

def f43int_f43_interest_expense_resilience_base_v080_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v080_signal'] = f43int_f43_interest_expense_resilience_base_v080_signal

def f43int_f43_interest_expense_resilience_base_v081_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v081_signal'] = f43int_f43_interest_expense_resilience_base_v081_signal

def f43int_f43_interest_expense_resilience_base_v082_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v082_signal'] = f43int_f43_interest_expense_resilience_base_v082_signal

def f43int_f43_interest_expense_resilience_base_v083_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v083_signal'] = f43int_f43_interest_expense_resilience_base_v083_signal

def f43int_f43_interest_expense_resilience_base_v084_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v084_signal'] = f43int_f43_interest_expense_resilience_base_v084_signal

def f43int_f43_interest_expense_resilience_base_v085_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v085_signal'] = f43int_f43_interest_expense_resilience_base_v085_signal

def f43int_f43_interest_expense_resilience_base_v086_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v086_signal'] = f43int_f43_interest_expense_resilience_base_v086_signal

def f43int_f43_interest_expense_resilience_base_v087_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v087_signal'] = f43int_f43_interest_expense_resilience_base_v087_signal

def f43int_f43_interest_expense_resilience_base_v088_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v088_signal'] = f43int_f43_interest_expense_resilience_base_v088_signal

def f43int_f43_interest_expense_resilience_base_v089_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v089_signal'] = f43int_f43_interest_expense_resilience_base_v089_signal

def f43int_f43_interest_expense_resilience_base_v090_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v090_signal'] = f43int_f43_interest_expense_resilience_base_v090_signal

def f43int_f43_interest_expense_resilience_base_v091_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v091_signal'] = f43int_f43_interest_expense_resilience_base_v091_signal

def f43int_f43_interest_expense_resilience_base_v092_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v092_signal'] = f43int_f43_interest_expense_resilience_base_v092_signal

def f43int_f43_interest_expense_resilience_base_v093_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v093_signal'] = f43int_f43_interest_expense_resilience_base_v093_signal

def f43int_f43_interest_expense_resilience_base_v094_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v094_signal'] = f43int_f43_interest_expense_resilience_base_v094_signal

def f43int_f43_interest_expense_resilience_base_v095_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v095_signal'] = f43int_f43_interest_expense_resilience_base_v095_signal

def f43int_f43_interest_expense_resilience_base_v096_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).mean())/(ebit / intexp.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v096_signal'] = f43int_f43_interest_expense_resilience_base_v096_signal

def f43int_f43_interest_expense_resilience_base_v097_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).mean())/(ebit / intexp.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v097_signal'] = f43int_f43_interest_expense_resilience_base_v097_signal

def f43int_f43_interest_expense_resilience_base_v098_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).mean())/(ebit / intexp.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v098_signal'] = f43int_f43_interest_expense_resilience_base_v098_signal

def f43int_f43_interest_expense_resilience_base_v099_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).mean())/(ebit / intexp.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v099_signal'] = f43int_f43_interest_expense_resilience_base_v099_signal

def f43int_f43_interest_expense_resilience_base_v100_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v100_signal'] = f43int_f43_interest_expense_resilience_base_v100_signal

def f43int_f43_interest_expense_resilience_base_v101_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v101_signal'] = f43int_f43_interest_expense_resilience_base_v101_signal

def f43int_f43_interest_expense_resilience_base_v102_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v102_signal'] = f43int_f43_interest_expense_resilience_base_v102_signal

def f43int_f43_interest_expense_resilience_base_v103_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v103_signal'] = f43int_f43_interest_expense_resilience_base_v103_signal

def f43int_f43_interest_expense_resilience_base_v104_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v104_signal'] = f43int_f43_interest_expense_resilience_base_v104_signal

def f43int_f43_interest_expense_resilience_base_v105_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v105_signal'] = f43int_f43_interest_expense_resilience_base_v105_signal

def f43int_f43_interest_expense_resilience_base_v106_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v106_signal'] = f43int_f43_interest_expense_resilience_base_v106_signal

def f43int_f43_interest_expense_resilience_base_v107_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v107_signal'] = f43int_f43_interest_expense_resilience_base_v107_signal

def f43int_f43_interest_expense_resilience_base_v108_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v108_signal'] = f43int_f43_interest_expense_resilience_base_v108_signal

def f43int_f43_interest_expense_resilience_base_v109_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v109_signal'] = f43int_f43_interest_expense_resilience_base_v109_signal

def f43int_f43_interest_expense_resilience_base_v110_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v110_signal'] = f43int_f43_interest_expense_resilience_base_v110_signal

def f43int_f43_interest_expense_resilience_base_v111_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v111_signal'] = f43int_f43_interest_expense_resilience_base_v111_signal

def f43int_f43_interest_expense_resilience_base_v112_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v112_signal'] = f43int_f43_interest_expense_resilience_base_v112_signal

def f43int_f43_interest_expense_resilience_base_v113_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v113_signal'] = f43int_f43_interest_expense_resilience_base_v113_signal

def f43int_f43_interest_expense_resilience_base_v114_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v114_signal'] = f43int_f43_interest_expense_resilience_base_v114_signal

def f43int_f43_interest_expense_resilience_base_v115_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v115_signal'] = f43int_f43_interest_expense_resilience_base_v115_signal

def f43int_f43_interest_expense_resilience_base_v116_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v116_signal'] = f43int_f43_interest_expense_resilience_base_v116_signal

def f43int_f43_interest_expense_resilience_base_v117_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v117_signal'] = f43int_f43_interest_expense_resilience_base_v117_signal

def f43int_f43_interest_expense_resilience_base_v118_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v118_signal'] = f43int_f43_interest_expense_resilience_base_v118_signal

def f43int_f43_interest_expense_resilience_base_v119_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v119_signal'] = f43int_f43_interest_expense_resilience_base_v119_signal

def f43int_f43_interest_expense_resilience_base_v120_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v120_signal'] = f43int_f43_interest_expense_resilience_base_v120_signal

def f43int_f43_interest_expense_resilience_base_v121_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v121_signal'] = f43int_f43_interest_expense_resilience_base_v121_signal

def f43int_f43_interest_expense_resilience_base_v122_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(63).max()-(ebit / intexp.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v122_signal'] = f43int_f43_interest_expense_resilience_base_v122_signal

def f43int_f43_interest_expense_resilience_base_v123_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(126).max()-(ebit / intexp.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v123_signal'] = f43int_f43_interest_expense_resilience_base_v123_signal

def f43int_f43_interest_expense_resilience_base_v124_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(252).max()-(ebit / intexp.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v124_signal'] = f43int_f43_interest_expense_resilience_base_v124_signal

def f43int_f43_interest_expense_resilience_base_v125_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v125_signal'] = f43int_f43_interest_expense_resilience_base_v125_signal

def f43int_f43_interest_expense_resilience_base_v126_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v126_signal'] = f43int_f43_interest_expense_resilience_base_v126_signal

def f43int_f43_interest_expense_resilience_base_v127_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).min())/((ebit / intexp.replace(0, np.nan)).rolling(63).max()-(ebit / intexp.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v127_signal'] = f43int_f43_interest_expense_resilience_base_v127_signal

def f43int_f43_interest_expense_resilience_base_v128_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).min())/((ebit / intexp.replace(0, np.nan)).rolling(126).max()-(ebit / intexp.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v128_signal'] = f43int_f43_interest_expense_resilience_base_v128_signal

def f43int_f43_interest_expense_resilience_base_v129_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).min())/((ebit / intexp.replace(0, np.nan)).rolling(252).max()-(ebit / intexp.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v129_signal'] = f43int_f43_interest_expense_resilience_base_v129_signal

def f43int_f43_interest_expense_resilience_base_v130_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).min())/((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v130_signal'] = f43int_f43_interest_expense_resilience_base_v130_signal

def f43int_f43_interest_expense_resilience_base_v131_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v131_signal'] = f43int_f43_interest_expense_resilience_base_v131_signal

def f43int_f43_interest_expense_resilience_base_v132_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v132_signal'] = f43int_f43_interest_expense_resilience_base_v132_signal

def f43int_f43_interest_expense_resilience_base_v133_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v133_signal'] = f43int_f43_interest_expense_resilience_base_v133_signal

def f43int_f43_interest_expense_resilience_base_v134_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v134_signal'] = f43int_f43_interest_expense_resilience_base_v134_signal

def f43int_f43_interest_expense_resilience_base_v135_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v135_signal'] = f43int_f43_interest_expense_resilience_base_v135_signal

def f43int_f43_interest_expense_resilience_base_v136_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v136_signal'] = f43int_f43_interest_expense_resilience_base_v136_signal

def f43int_f43_interest_expense_resilience_base_v137_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v137_signal'] = f43int_f43_interest_expense_resilience_base_v137_signal

def f43int_f43_interest_expense_resilience_base_v138_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v138_signal'] = f43int_f43_interest_expense_resilience_base_v138_signal

def f43int_f43_interest_expense_resilience_base_v139_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v139_signal'] = f43int_f43_interest_expense_resilience_base_v139_signal

def f43int_f43_interest_expense_resilience_base_v140_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v140_signal'] = f43int_f43_interest_expense_resilience_base_v140_signal

def f43int_f43_interest_expense_resilience_base_v141_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=21).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v141_signal'] = f43int_f43_interest_expense_resilience_base_v141_signal

def f43int_f43_interest_expense_resilience_base_v142_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=63).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v142_signal'] = f43int_f43_interest_expense_resilience_base_v142_signal

def f43int_f43_interest_expense_resilience_base_v143_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=126).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v143_signal'] = f43int_f43_interest_expense_resilience_base_v143_signal

def f43int_f43_interest_expense_resilience_base_v144_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v144_signal'] = f43int_f43_interest_expense_resilience_base_v144_signal

def f43int_f43_interest_expense_resilience_base_v145_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=504).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v145_signal'] = f43int_f43_interest_expense_resilience_base_v145_signal

def f43int_f43_interest_expense_resilience_base_v146_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v146_signal'] = f43int_f43_interest_expense_resilience_base_v146_signal

def f43int_f43_interest_expense_resilience_base_v147_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v147_signal'] = f43int_f43_interest_expense_resilience_base_v147_signal

def f43int_f43_interest_expense_resilience_base_v148_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v148_signal'] = f43int_f43_interest_expense_resilience_base_v148_signal

def f43int_f43_interest_expense_resilience_base_v149_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v149_signal'] = f43int_f43_interest_expense_resilience_base_v149_signal

def f43int_f43_interest_expense_resilience_base_v150_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v150_signal'] = f43int_f43_interest_expense_resilience_base_v150_signal

