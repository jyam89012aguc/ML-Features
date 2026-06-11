import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f43int_f43_interest_expense_resilience_base_v001_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v001_signal'] = f43int_f43_interest_expense_resilience_base_v001_signal

def f43int_f43_interest_expense_resilience_base_v002_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v002_signal'] = f43int_f43_interest_expense_resilience_base_v002_signal

def f43int_f43_interest_expense_resilience_base_v003_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v003_signal'] = f43int_f43_interest_expense_resilience_base_v003_signal

def f43int_f43_interest_expense_resilience_base_v004_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v004_signal'] = f43int_f43_interest_expense_resilience_base_v004_signal

def f43int_f43_interest_expense_resilience_base_v005_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v005_signal'] = f43int_f43_interest_expense_resilience_base_v005_signal

def f43int_f43_interest_expense_resilience_base_v006_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v006_signal'] = f43int_f43_interest_expense_resilience_base_v006_signal

def f43int_f43_interest_expense_resilience_base_v007_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v007_signal'] = f43int_f43_interest_expense_resilience_base_v007_signal

def f43int_f43_interest_expense_resilience_base_v008_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v008_signal'] = f43int_f43_interest_expense_resilience_base_v008_signal

def f43int_f43_interest_expense_resilience_base_v009_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v009_signal'] = f43int_f43_interest_expense_resilience_base_v009_signal

def f43int_f43_interest_expense_resilience_base_v010_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v010_signal'] = f43int_f43_interest_expense_resilience_base_v010_signal

def f43int_f43_interest_expense_resilience_base_v011_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v011_signal'] = f43int_f43_interest_expense_resilience_base_v011_signal

def f43int_f43_interest_expense_resilience_base_v012_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v012_signal'] = f43int_f43_interest_expense_resilience_base_v012_signal

def f43int_f43_interest_expense_resilience_base_v013_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v013_signal'] = f43int_f43_interest_expense_resilience_base_v013_signal

def f43int_f43_interest_expense_resilience_base_v014_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v014_signal'] = f43int_f43_interest_expense_resilience_base_v014_signal

def f43int_f43_interest_expense_resilience_base_v015_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v015_signal'] = f43int_f43_interest_expense_resilience_base_v015_signal

def f43int_f43_interest_expense_resilience_base_v016_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v016_signal'] = f43int_f43_interest_expense_resilience_base_v016_signal

def f43int_f43_interest_expense_resilience_base_v017_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v017_signal'] = f43int_f43_interest_expense_resilience_base_v017_signal

def f43int_f43_interest_expense_resilience_base_v018_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v018_signal'] = f43int_f43_interest_expense_resilience_base_v018_signal

def f43int_f43_interest_expense_resilience_base_v019_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v019_signal'] = f43int_f43_interest_expense_resilience_base_v019_signal

def f43int_f43_interest_expense_resilience_base_v020_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v020_signal'] = f43int_f43_interest_expense_resilience_base_v020_signal

def f43int_f43_interest_expense_resilience_base_v021_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).mean())/(ebit / intexp.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v021_signal'] = f43int_f43_interest_expense_resilience_base_v021_signal

def f43int_f43_interest_expense_resilience_base_v022_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).mean())/(ebit / intexp.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v022_signal'] = f43int_f43_interest_expense_resilience_base_v022_signal

def f43int_f43_interest_expense_resilience_base_v023_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).mean())/(ebit / intexp.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v023_signal'] = f43int_f43_interest_expense_resilience_base_v023_signal

def f43int_f43_interest_expense_resilience_base_v024_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).mean())/(ebit / intexp.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v024_signal'] = f43int_f43_interest_expense_resilience_base_v024_signal

def f43int_f43_interest_expense_resilience_base_v025_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v025_signal'] = f43int_f43_interest_expense_resilience_base_v025_signal

def f43int_f43_interest_expense_resilience_base_v026_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v026_signal'] = f43int_f43_interest_expense_resilience_base_v026_signal

def f43int_f43_interest_expense_resilience_base_v027_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v027_signal'] = f43int_f43_interest_expense_resilience_base_v027_signal

def f43int_f43_interest_expense_resilience_base_v028_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v028_signal'] = f43int_f43_interest_expense_resilience_base_v028_signal

def f43int_f43_interest_expense_resilience_base_v029_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v029_signal'] = f43int_f43_interest_expense_resilience_base_v029_signal

def f43int_f43_interest_expense_resilience_base_v030_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v030_signal'] = f43int_f43_interest_expense_resilience_base_v030_signal

def f43int_f43_interest_expense_resilience_base_v031_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v031_signal'] = f43int_f43_interest_expense_resilience_base_v031_signal

def f43int_f43_interest_expense_resilience_base_v032_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v032_signal'] = f43int_f43_interest_expense_resilience_base_v032_signal

def f43int_f43_interest_expense_resilience_base_v033_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v033_signal'] = f43int_f43_interest_expense_resilience_base_v033_signal

def f43int_f43_interest_expense_resilience_base_v034_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v034_signal'] = f43int_f43_interest_expense_resilience_base_v034_signal

def f43int_f43_interest_expense_resilience_base_v035_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v035_signal'] = f43int_f43_interest_expense_resilience_base_v035_signal

def f43int_f43_interest_expense_resilience_base_v036_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v036_signal'] = f43int_f43_interest_expense_resilience_base_v036_signal

def f43int_f43_interest_expense_resilience_base_v037_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v037_signal'] = f43int_f43_interest_expense_resilience_base_v037_signal

def f43int_f43_interest_expense_resilience_base_v038_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v038_signal'] = f43int_f43_interest_expense_resilience_base_v038_signal

def f43int_f43_interest_expense_resilience_base_v039_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v039_signal'] = f43int_f43_interest_expense_resilience_base_v039_signal

def f43int_f43_interest_expense_resilience_base_v040_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v040_signal'] = f43int_f43_interest_expense_resilience_base_v040_signal

def f43int_f43_interest_expense_resilience_base_v041_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v041_signal'] = f43int_f43_interest_expense_resilience_base_v041_signal

def f43int_f43_interest_expense_resilience_base_v042_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v042_signal'] = f43int_f43_interest_expense_resilience_base_v042_signal

def f43int_f43_interest_expense_resilience_base_v043_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v043_signal'] = f43int_f43_interest_expense_resilience_base_v043_signal

def f43int_f43_interest_expense_resilience_base_v044_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v044_signal'] = f43int_f43_interest_expense_resilience_base_v044_signal

def f43int_f43_interest_expense_resilience_base_v045_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v045_signal'] = f43int_f43_interest_expense_resilience_base_v045_signal

def f43int_f43_interest_expense_resilience_base_v046_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v046_signal'] = f43int_f43_interest_expense_resilience_base_v046_signal

def f43int_f43_interest_expense_resilience_base_v047_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(63).max()-(ebit / intexp.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v047_signal'] = f43int_f43_interest_expense_resilience_base_v047_signal

def f43int_f43_interest_expense_resilience_base_v048_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(126).max()-(ebit / intexp.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v048_signal'] = f43int_f43_interest_expense_resilience_base_v048_signal

def f43int_f43_interest_expense_resilience_base_v049_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(252).max()-(ebit / intexp.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v049_signal'] = f43int_f43_interest_expense_resilience_base_v049_signal

def f43int_f43_interest_expense_resilience_base_v050_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v050_signal'] = f43int_f43_interest_expense_resilience_base_v050_signal

def f43int_f43_interest_expense_resilience_base_v051_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v051_signal'] = f43int_f43_interest_expense_resilience_base_v051_signal

def f43int_f43_interest_expense_resilience_base_v052_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(63).min())/((ebit / intexp.replace(0, np.nan)).rolling(63).max()-(ebit / intexp.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v052_signal'] = f43int_f43_interest_expense_resilience_base_v052_signal

def f43int_f43_interest_expense_resilience_base_v053_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(126).min())/((ebit / intexp.replace(0, np.nan)).rolling(126).max()-(ebit / intexp.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v053_signal'] = f43int_f43_interest_expense_resilience_base_v053_signal

def f43int_f43_interest_expense_resilience_base_v054_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(252).min())/((ebit / intexp.replace(0, np.nan)).rolling(252).max()-(ebit / intexp.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v054_signal'] = f43int_f43_interest_expense_resilience_base_v054_signal

def f43int_f43_interest_expense_resilience_base_v055_signal(intexp, ebit):
    res = (((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).min())/((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v055_signal'] = f43int_f43_interest_expense_resilience_base_v055_signal

def f43int_f43_interest_expense_resilience_base_v056_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v056_signal'] = f43int_f43_interest_expense_resilience_base_v056_signal

def f43int_f43_interest_expense_resilience_base_v057_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v057_signal'] = f43int_f43_interest_expense_resilience_base_v057_signal

def f43int_f43_interest_expense_resilience_base_v058_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v058_signal'] = f43int_f43_interest_expense_resilience_base_v058_signal

def f43int_f43_interest_expense_resilience_base_v059_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v059_signal'] = f43int_f43_interest_expense_resilience_base_v059_signal

def f43int_f43_interest_expense_resilience_base_v060_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v060_signal'] = f43int_f43_interest_expense_resilience_base_v060_signal

def f43int_f43_interest_expense_resilience_base_v061_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v061_signal'] = f43int_f43_interest_expense_resilience_base_v061_signal

def f43int_f43_interest_expense_resilience_base_v062_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v062_signal'] = f43int_f43_interest_expense_resilience_base_v062_signal

def f43int_f43_interest_expense_resilience_base_v063_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v063_signal'] = f43int_f43_interest_expense_resilience_base_v063_signal

def f43int_f43_interest_expense_resilience_base_v064_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v064_signal'] = f43int_f43_interest_expense_resilience_base_v064_signal

def f43int_f43_interest_expense_resilience_base_v065_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v065_signal'] = f43int_f43_interest_expense_resilience_base_v065_signal

def f43int_f43_interest_expense_resilience_base_v066_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=21).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v066_signal'] = f43int_f43_interest_expense_resilience_base_v066_signal

def f43int_f43_interest_expense_resilience_base_v067_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=63).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v067_signal'] = f43int_f43_interest_expense_resilience_base_v067_signal

def f43int_f43_interest_expense_resilience_base_v068_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=126).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v068_signal'] = f43int_f43_interest_expense_resilience_base_v068_signal

def f43int_f43_interest_expense_resilience_base_v069_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v069_signal'] = f43int_f43_interest_expense_resilience_base_v069_signal

def f43int_f43_interest_expense_resilience_base_v070_signal(intexp, ebit):
    res = ((ebit / intexp.replace(0, np.nan)).ewm(span=504).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v070_signal'] = f43int_f43_interest_expense_resilience_base_v070_signal

def f43int_f43_interest_expense_resilience_base_v071_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v071_signal'] = f43int_f43_interest_expense_resilience_base_v071_signal

def f43int_f43_interest_expense_resilience_base_v072_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v072_signal'] = f43int_f43_interest_expense_resilience_base_v072_signal

def f43int_f43_interest_expense_resilience_base_v073_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v073_signal'] = f43int_f43_interest_expense_resilience_base_v073_signal

def f43int_f43_interest_expense_resilience_base_v074_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v074_signal'] = f43int_f43_interest_expense_resilience_base_v074_signal

def f43int_f43_interest_expense_resilience_base_v075_signal(intexp, ebit):
    res = (ebit / intexp.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_base_v075_signal'] = f43int_f43_interest_expense_resilience_base_v075_signal

