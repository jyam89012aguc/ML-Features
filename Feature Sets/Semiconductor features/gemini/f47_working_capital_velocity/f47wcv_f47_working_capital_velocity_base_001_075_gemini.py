import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f47wcv_f47_working_capital_velocity_base_v001_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v001_signal'] = f47wcv_f47_working_capital_velocity_base_v001_signal

def f47wcv_f47_working_capital_velocity_base_v002_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v002_signal'] = f47wcv_f47_working_capital_velocity_base_v002_signal

def f47wcv_f47_working_capital_velocity_base_v003_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v003_signal'] = f47wcv_f47_working_capital_velocity_base_v003_signal

def f47wcv_f47_working_capital_velocity_base_v004_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v004_signal'] = f47wcv_f47_working_capital_velocity_base_v004_signal

def f47wcv_f47_working_capital_velocity_base_v005_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v005_signal'] = f47wcv_f47_working_capital_velocity_base_v005_signal

def f47wcv_f47_working_capital_velocity_base_v006_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v006_signal'] = f47wcv_f47_working_capital_velocity_base_v006_signal

def f47wcv_f47_working_capital_velocity_base_v007_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v007_signal'] = f47wcv_f47_working_capital_velocity_base_v007_signal

def f47wcv_f47_working_capital_velocity_base_v008_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v008_signal'] = f47wcv_f47_working_capital_velocity_base_v008_signal

def f47wcv_f47_working_capital_velocity_base_v009_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v009_signal'] = f47wcv_f47_working_capital_velocity_base_v009_signal

def f47wcv_f47_working_capital_velocity_base_v010_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v010_signal'] = f47wcv_f47_working_capital_velocity_base_v010_signal

def f47wcv_f47_working_capital_velocity_base_v011_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v011_signal'] = f47wcv_f47_working_capital_velocity_base_v011_signal

def f47wcv_f47_working_capital_velocity_base_v012_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v012_signal'] = f47wcv_f47_working_capital_velocity_base_v012_signal

def f47wcv_f47_working_capital_velocity_base_v013_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v013_signal'] = f47wcv_f47_working_capital_velocity_base_v013_signal

def f47wcv_f47_working_capital_velocity_base_v014_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v014_signal'] = f47wcv_f47_working_capital_velocity_base_v014_signal

def f47wcv_f47_working_capital_velocity_base_v015_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v015_signal'] = f47wcv_f47_working_capital_velocity_base_v015_signal

def f47wcv_f47_working_capital_velocity_base_v016_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v016_signal'] = f47wcv_f47_working_capital_velocity_base_v016_signal

def f47wcv_f47_working_capital_velocity_base_v017_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v017_signal'] = f47wcv_f47_working_capital_velocity_base_v017_signal

def f47wcv_f47_working_capital_velocity_base_v018_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v018_signal'] = f47wcv_f47_working_capital_velocity_base_v018_signal

def f47wcv_f47_working_capital_velocity_base_v019_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v019_signal'] = f47wcv_f47_working_capital_velocity_base_v019_signal

def f47wcv_f47_working_capital_velocity_base_v020_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v020_signal'] = f47wcv_f47_working_capital_velocity_base_v020_signal

def f47wcv_f47_working_capital_velocity_base_v021_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v021_signal'] = f47wcv_f47_working_capital_velocity_base_v021_signal

def f47wcv_f47_working_capital_velocity_base_v022_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v022_signal'] = f47wcv_f47_working_capital_velocity_base_v022_signal

def f47wcv_f47_working_capital_velocity_base_v023_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v023_signal'] = f47wcv_f47_working_capital_velocity_base_v023_signal

def f47wcv_f47_working_capital_velocity_base_v024_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v024_signal'] = f47wcv_f47_working_capital_velocity_base_v024_signal

def f47wcv_f47_working_capital_velocity_base_v025_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).mean())/(workingcapital / revenue.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v025_signal'] = f47wcv_f47_working_capital_velocity_base_v025_signal

def f47wcv_f47_working_capital_velocity_base_v026_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v026_signal'] = f47wcv_f47_working_capital_velocity_base_v026_signal

def f47wcv_f47_working_capital_velocity_base_v027_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v027_signal'] = f47wcv_f47_working_capital_velocity_base_v027_signal

def f47wcv_f47_working_capital_velocity_base_v028_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v028_signal'] = f47wcv_f47_working_capital_velocity_base_v028_signal

def f47wcv_f47_working_capital_velocity_base_v029_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v029_signal'] = f47wcv_f47_working_capital_velocity_base_v029_signal

def f47wcv_f47_working_capital_velocity_base_v030_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).median())/(((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v030_signal'] = f47wcv_f47_working_capital_velocity_base_v030_signal

def f47wcv_f47_working_capital_velocity_base_v031_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v031_signal'] = f47wcv_f47_working_capital_velocity_base_v031_signal

def f47wcv_f47_working_capital_velocity_base_v032_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v032_signal'] = f47wcv_f47_working_capital_velocity_base_v032_signal

def f47wcv_f47_working_capital_velocity_base_v033_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v033_signal'] = f47wcv_f47_working_capital_velocity_base_v033_signal

def f47wcv_f47_working_capital_velocity_base_v034_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v034_signal'] = f47wcv_f47_working_capital_velocity_base_v034_signal

def f47wcv_f47_working_capital_velocity_base_v035_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).gt((workingcapital / revenue.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v035_signal'] = f47wcv_f47_working_capital_velocity_base_v035_signal

def f47wcv_f47_working_capital_velocity_base_v036_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v036_signal'] = f47wcv_f47_working_capital_velocity_base_v036_signal

def f47wcv_f47_working_capital_velocity_base_v037_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v037_signal'] = f47wcv_f47_working_capital_velocity_base_v037_signal

def f47wcv_f47_working_capital_velocity_base_v038_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v038_signal'] = f47wcv_f47_working_capital_velocity_base_v038_signal

def f47wcv_f47_working_capital_velocity_base_v039_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v039_signal'] = f47wcv_f47_working_capital_velocity_base_v039_signal

def f47wcv_f47_working_capital_velocity_base_v040_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v040_signal'] = f47wcv_f47_working_capital_velocity_base_v040_signal

def f47wcv_f47_working_capital_velocity_base_v041_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v041_signal'] = f47wcv_f47_working_capital_velocity_base_v041_signal

def f47wcv_f47_working_capital_velocity_base_v042_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v042_signal'] = f47wcv_f47_working_capital_velocity_base_v042_signal

def f47wcv_f47_working_capital_velocity_base_v043_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v043_signal'] = f47wcv_f47_working_capital_velocity_base_v043_signal

def f47wcv_f47_working_capital_velocity_base_v044_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v044_signal'] = f47wcv_f47_working_capital_velocity_base_v044_signal

def f47wcv_f47_working_capital_velocity_base_v045_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v045_signal'] = f47wcv_f47_working_capital_velocity_base_v045_signal

def f47wcv_f47_working_capital_velocity_base_v046_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v046_signal'] = f47wcv_f47_working_capital_velocity_base_v046_signal

def f47wcv_f47_working_capital_velocity_base_v047_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(63).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v047_signal'] = f47wcv_f47_working_capital_velocity_base_v047_signal

def f47wcv_f47_working_capital_velocity_base_v048_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v048_signal'] = f47wcv_f47_working_capital_velocity_base_v048_signal

def f47wcv_f47_working_capital_velocity_base_v049_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(252).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v049_signal'] = f47wcv_f47_working_capital_velocity_base_v049_signal

def f47wcv_f47_working_capital_velocity_base_v050_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v050_signal'] = f47wcv_f47_working_capital_velocity_base_v050_signal

def f47wcv_f47_working_capital_velocity_base_v051_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(21).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v051_signal'] = f47wcv_f47_working_capital_velocity_base_v051_signal

def f47wcv_f47_working_capital_velocity_base_v052_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(63).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(63).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v052_signal'] = f47wcv_f47_working_capital_velocity_base_v052_signal

def f47wcv_f47_working_capital_velocity_base_v053_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(126).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(126).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v053_signal'] = f47wcv_f47_working_capital_velocity_base_v053_signal

def f47wcv_f47_working_capital_velocity_base_v054_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(252).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(252).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v054_signal'] = f47wcv_f47_working_capital_velocity_base_v054_signal

def f47wcv_f47_working_capital_velocity_base_v055_signal(workingcapital, revenue):
    res = (((workingcapital / revenue.replace(0, np.nan))-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min())/((workingcapital / revenue.replace(0, np.nan)).rolling(504).max()-(workingcapital / revenue.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v055_signal'] = f47wcv_f47_working_capital_velocity_base_v055_signal

def f47wcv_f47_working_capital_velocity_base_v056_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v056_signal'] = f47wcv_f47_working_capital_velocity_base_v056_signal

def f47wcv_f47_working_capital_velocity_base_v057_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v057_signal'] = f47wcv_f47_working_capital_velocity_base_v057_signal

def f47wcv_f47_working_capital_velocity_base_v058_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v058_signal'] = f47wcv_f47_working_capital_velocity_base_v058_signal

def f47wcv_f47_working_capital_velocity_base_v059_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v059_signal'] = f47wcv_f47_working_capital_velocity_base_v059_signal

def f47wcv_f47_working_capital_velocity_base_v060_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v060_signal'] = f47wcv_f47_working_capital_velocity_base_v060_signal

def f47wcv_f47_working_capital_velocity_base_v061_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v061_signal'] = f47wcv_f47_working_capital_velocity_base_v061_signal

def f47wcv_f47_working_capital_velocity_base_v062_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v062_signal'] = f47wcv_f47_working_capital_velocity_base_v062_signal

def f47wcv_f47_working_capital_velocity_base_v063_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v063_signal'] = f47wcv_f47_working_capital_velocity_base_v063_signal

def f47wcv_f47_working_capital_velocity_base_v064_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v064_signal'] = f47wcv_f47_working_capital_velocity_base_v064_signal

def f47wcv_f47_working_capital_velocity_base_v065_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan))/(workingcapital / revenue.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v065_signal'] = f47wcv_f47_working_capital_velocity_base_v065_signal

def f47wcv_f47_working_capital_velocity_base_v066_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=21).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v066_signal'] = f47wcv_f47_working_capital_velocity_base_v066_signal

def f47wcv_f47_working_capital_velocity_base_v067_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=63).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v067_signal'] = f47wcv_f47_working_capital_velocity_base_v067_signal

def f47wcv_f47_working_capital_velocity_base_v068_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=126).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v068_signal'] = f47wcv_f47_working_capital_velocity_base_v068_signal

def f47wcv_f47_working_capital_velocity_base_v069_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=252).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v069_signal'] = f47wcv_f47_working_capital_velocity_base_v069_signal

def f47wcv_f47_working_capital_velocity_base_v070_signal(workingcapital, revenue):
    res = ((workingcapital / revenue.replace(0, np.nan)).ewm(span=504).mean() - (workingcapital / revenue.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v070_signal'] = f47wcv_f47_working_capital_velocity_base_v070_signal

def f47wcv_f47_working_capital_velocity_base_v071_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v071_signal'] = f47wcv_f47_working_capital_velocity_base_v071_signal

def f47wcv_f47_working_capital_velocity_base_v072_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v072_signal'] = f47wcv_f47_working_capital_velocity_base_v072_signal

def f47wcv_f47_working_capital_velocity_base_v073_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v073_signal'] = f47wcv_f47_working_capital_velocity_base_v073_signal

def f47wcv_f47_working_capital_velocity_base_v074_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v074_signal'] = f47wcv_f47_working_capital_velocity_base_v074_signal

def f47wcv_f47_working_capital_velocity_base_v075_signal(workingcapital, revenue):
    res = (workingcapital / revenue.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f47wcv_f47_working_capital_velocity_base_v075_signal'] = f47wcv_f47_working_capital_velocity_base_v075_signal

