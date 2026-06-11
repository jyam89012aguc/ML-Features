import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f47wcv_f47_working_capital_velocity_2ndderiv_v001_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v001_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v001_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v002_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v002_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v002_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v003_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v003_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v003_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v004_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v004_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v004_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v005_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v005_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v005_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v006_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v006_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v006_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v007_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v007_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v007_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v008_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v008_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v008_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v009_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v009_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v009_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v010_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v010_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v010_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v011_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v011_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v011_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v012_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v012_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v012_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v013_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v013_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v013_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v014_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v014_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v014_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v015_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v015_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v015_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v016_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v016_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v016_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v017_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v017_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v017_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v018_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v018_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v018_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v019_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v019_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v019_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v020_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v020_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v020_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v021_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v021_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v021_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v022_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v022_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v022_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v023_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v023_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v023_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v024_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v024_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v024_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v025_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v025_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v025_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v026_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v026_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v026_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v027_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v027_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v027_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v028_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v028_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v028_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v029_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v029_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v029_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v030_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v030_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v030_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v031_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v031_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v031_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v032_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v032_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v032_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v033_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v033_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v033_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v034_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v034_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v034_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v035_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v035_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v035_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v036_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v036_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v036_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v037_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v037_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v037_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v038_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v038_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v038_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v039_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v039_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v039_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v040_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v040_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v040_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v041_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v041_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v041_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v042_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v042_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v042_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v043_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v043_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v043_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v044_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v044_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v044_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v045_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v045_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v045_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v046_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).diff(5) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v046_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v046_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v047_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).diff(21) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v047_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v047_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v048_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).diff(63) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v048_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v048_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v049_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).diff(126) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v049_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v049_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v050_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).diff(252) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v050_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v050_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v051_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v051_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v051_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v052_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v052_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v052_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v053_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v053_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v053_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v054_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v054_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v054_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v055_signal(workingcapital, revenue):
    res = (((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v055_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v055_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v056_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v056_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v056_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v057_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v057_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v057_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v058_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v058_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v058_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v059_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v059_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v059_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v060_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v060_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v060_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v061_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v061_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v061_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v062_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v062_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v062_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v063_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v063_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v063_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v064_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v064_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v064_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v065_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v065_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v065_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v066_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v066_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v066_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v067_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v067_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v067_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v068_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v068_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v068_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v069_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v069_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v069_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v070_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v070_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v070_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v071_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v071_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v071_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v072_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v072_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v072_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v073_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v073_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v073_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v074_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v074_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v074_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v075_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v075_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v075_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v076_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v076_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v076_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v077_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v077_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v077_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v078_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v078_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v078_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v079_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v079_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v079_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v080_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v080_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v080_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v081_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v081_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v081_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v082_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v082_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v082_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v083_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v083_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v083_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v084_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v084_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v084_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v085_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()/(workingcapital / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v085_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v085_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v086_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v086_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v086_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v087_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v087_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v087_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v088_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v088_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v088_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v089_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v089_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v089_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v090_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(126).std()/(workingcapital / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v090_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v090_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v091_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v091_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v091_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v092_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v092_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v092_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v093_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v093_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v093_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v094_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v094_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v094_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v095_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v095_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v095_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v096_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).diff(5) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v096_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v096_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v097_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).diff(21) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v097_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v097_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v098_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).diff(63) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v098_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v098_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v099_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).diff(126) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v099_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v099_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v100_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).diff(252) / (((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean() - (workingcapital / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v100_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v100_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v101_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v101_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v101_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v102_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v102_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v102_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v103_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v103_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v103_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v104_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v104_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v104_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v105_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v105_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v105_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v106_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v106_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v106_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v107_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v107_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v107_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v108_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v108_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v108_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v109_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v109_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v109_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v110_signal(workingcapital, revenue, closeadj):
    res = (((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v110_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v110_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v111_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v111_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v111_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v112_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v112_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v112_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v113_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v113_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v113_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v114_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v114_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v114_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v115_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v115_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v115_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v116_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v116_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v116_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v117_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v117_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v117_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v118_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v118_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v118_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v119_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v119_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v119_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v120_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((workingcapital / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v120_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v120_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v121_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v121_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v121_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v122_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v122_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v122_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v123_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v123_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v123_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v124_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v124_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v124_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v125_signal(workingcapital, revenue, closeadj):
    res = ((((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((workingcapital / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v125_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v125_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v126_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v126_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v126_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v127_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v127_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v127_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v128_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v128_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v128_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v129_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v129_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v129_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v130_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((workingcapital / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v130_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v130_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v131_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v131_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v131_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v132_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v132_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v132_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v133_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v133_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v133_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v134_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v134_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v134_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v135_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (workingcapital / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v135_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v135_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v136_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v136_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v136_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v137_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v137_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v137_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v138_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v138_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v138_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v139_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v139_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v139_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v140_signal(workingcapital, revenue):
    res = ((((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((workingcapital / revenue.replace(0, np.nan)) - (workingcapital / revenue.replace(0, np.nan)).shift(126))/(workingcapital / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v140_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v140_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v141_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v141_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v141_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v142_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v142_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v142_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v143_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v143_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v143_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v144_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v144_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v144_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v145_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v145_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v145_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v146_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v146_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v146_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v147_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v147_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v147_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v148_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v148_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v148_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v149_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v149_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v149_signal

def f47wcv_f47_working_capital_velocity_2ndderiv_v150_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_2ndderiv_v150_signal'] = f47wcv_f47_working_capital_velocity_2ndderiv_v150_signal

