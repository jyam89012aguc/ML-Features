import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f44cdr_f44_cash_to_debt_ratio_base_v001_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v001_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v001_signal

def f44cdr_f44_cash_to_debt_ratio_base_v002_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v002_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v002_signal

def f44cdr_f44_cash_to_debt_ratio_base_v003_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v003_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v003_signal

def f44cdr_f44_cash_to_debt_ratio_base_v004_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v004_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v004_signal

def f44cdr_f44_cash_to_debt_ratio_base_v005_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v005_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v005_signal

def f44cdr_f44_cash_to_debt_ratio_base_v006_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v006_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v006_signal

def f44cdr_f44_cash_to_debt_ratio_base_v007_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v007_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v007_signal

def f44cdr_f44_cash_to_debt_ratio_base_v008_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v008_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v008_signal

def f44cdr_f44_cash_to_debt_ratio_base_v009_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v009_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v009_signal

def f44cdr_f44_cash_to_debt_ratio_base_v010_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v010_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v010_signal

def f44cdr_f44_cash_to_debt_ratio_base_v011_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v011_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v011_signal

def f44cdr_f44_cash_to_debt_ratio_base_v012_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v012_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v012_signal

def f44cdr_f44_cash_to_debt_ratio_base_v013_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v013_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v013_signal

def f44cdr_f44_cash_to_debt_ratio_base_v014_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v014_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v014_signal

def f44cdr_f44_cash_to_debt_ratio_base_v015_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v015_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v015_signal

def f44cdr_f44_cash_to_debt_ratio_base_v016_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v016_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v016_signal

def f44cdr_f44_cash_to_debt_ratio_base_v017_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v017_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v017_signal

def f44cdr_f44_cash_to_debt_ratio_base_v018_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v018_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v018_signal

def f44cdr_f44_cash_to_debt_ratio_base_v019_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v019_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v019_signal

def f44cdr_f44_cash_to_debt_ratio_base_v020_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v020_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v020_signal

def f44cdr_f44_cash_to_debt_ratio_base_v021_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).mean())/(cashneq / debt.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v021_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v021_signal

def f44cdr_f44_cash_to_debt_ratio_base_v022_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(63).mean())/(cashneq / debt.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v022_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v022_signal

def f44cdr_f44_cash_to_debt_ratio_base_v023_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(126).mean())/(cashneq / debt.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v023_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v023_signal

def f44cdr_f44_cash_to_debt_ratio_base_v024_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(252).mean())/(cashneq / debt.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v024_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v024_signal

def f44cdr_f44_cash_to_debt_ratio_base_v025_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v025_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v025_signal

def f44cdr_f44_cash_to_debt_ratio_base_v026_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v026_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v026_signal

def f44cdr_f44_cash_to_debt_ratio_base_v027_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(63).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v027_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v027_signal

def f44cdr_f44_cash_to_debt_ratio_base_v028_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(126).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v028_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v028_signal

def f44cdr_f44_cash_to_debt_ratio_base_v029_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(252).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v029_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v029_signal

def f44cdr_f44_cash_to_debt_ratio_base_v030_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v030_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v030_signal

def f44cdr_f44_cash_to_debt_ratio_base_v031_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v031_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v031_signal

def f44cdr_f44_cash_to_debt_ratio_base_v032_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v032_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v032_signal

def f44cdr_f44_cash_to_debt_ratio_base_v033_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v033_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v033_signal

def f44cdr_f44_cash_to_debt_ratio_base_v034_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v034_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v034_signal

def f44cdr_f44_cash_to_debt_ratio_base_v035_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v035_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v035_signal

def f44cdr_f44_cash_to_debt_ratio_base_v036_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v036_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v036_signal

def f44cdr_f44_cash_to_debt_ratio_base_v037_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v037_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v037_signal

def f44cdr_f44_cash_to_debt_ratio_base_v038_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v038_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v038_signal

def f44cdr_f44_cash_to_debt_ratio_base_v039_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v039_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v039_signal

def f44cdr_f44_cash_to_debt_ratio_base_v040_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v040_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v040_signal

def f44cdr_f44_cash_to_debt_ratio_base_v041_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v041_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v041_signal

def f44cdr_f44_cash_to_debt_ratio_base_v042_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v042_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v042_signal

def f44cdr_f44_cash_to_debt_ratio_base_v043_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v043_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v043_signal

def f44cdr_f44_cash_to_debt_ratio_base_v044_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v044_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v044_signal

def f44cdr_f44_cash_to_debt_ratio_base_v045_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v045_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v045_signal

def f44cdr_f44_cash_to_debt_ratio_base_v046_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v046_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v046_signal

def f44cdr_f44_cash_to_debt_ratio_base_v047_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).rolling(63).max()-(cashneq / debt.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v047_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v047_signal

def f44cdr_f44_cash_to_debt_ratio_base_v048_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).rolling(126).max()-(cashneq / debt.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v048_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v048_signal

def f44cdr_f44_cash_to_debt_ratio_base_v049_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).rolling(252).max()-(cashneq / debt.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v049_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v049_signal

def f44cdr_f44_cash_to_debt_ratio_base_v050_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v050_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v050_signal

def f44cdr_f44_cash_to_debt_ratio_base_v051_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v051_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v051_signal

def f44cdr_f44_cash_to_debt_ratio_base_v052_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(63).min())/((cashneq / debt.replace(0, np.nan)).rolling(63).max()-(cashneq / debt.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v052_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v052_signal

def f44cdr_f44_cash_to_debt_ratio_base_v053_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(126).min())/((cashneq / debt.replace(0, np.nan)).rolling(126).max()-(cashneq / debt.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v053_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v053_signal

def f44cdr_f44_cash_to_debt_ratio_base_v054_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(252).min())/((cashneq / debt.replace(0, np.nan)).rolling(252).max()-(cashneq / debt.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v054_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v054_signal

def f44cdr_f44_cash_to_debt_ratio_base_v055_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).min())/((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v055_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v055_signal

def f44cdr_f44_cash_to_debt_ratio_base_v056_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v056_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v056_signal

def f44cdr_f44_cash_to_debt_ratio_base_v057_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v057_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v057_signal

def f44cdr_f44_cash_to_debt_ratio_base_v058_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v058_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v058_signal

def f44cdr_f44_cash_to_debt_ratio_base_v059_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v059_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v059_signal

def f44cdr_f44_cash_to_debt_ratio_base_v060_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v060_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v060_signal

def f44cdr_f44_cash_to_debt_ratio_base_v061_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v061_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v061_signal

def f44cdr_f44_cash_to_debt_ratio_base_v062_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v062_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v062_signal

def f44cdr_f44_cash_to_debt_ratio_base_v063_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v063_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v063_signal

def f44cdr_f44_cash_to_debt_ratio_base_v064_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v064_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v064_signal

def f44cdr_f44_cash_to_debt_ratio_base_v065_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v065_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v065_signal

def f44cdr_f44_cash_to_debt_ratio_base_v066_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).ewm(span=21).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v066_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v066_signal

def f44cdr_f44_cash_to_debt_ratio_base_v067_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).ewm(span=63).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v067_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v067_signal

def f44cdr_f44_cash_to_debt_ratio_base_v068_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).ewm(span=126).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v068_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v068_signal

def f44cdr_f44_cash_to_debt_ratio_base_v069_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v069_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v069_signal

def f44cdr_f44_cash_to_debt_ratio_base_v070_signal(cashneq, debt):
    res = ((cashneq / debt.replace(0, np.nan)).ewm(span=504).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v070_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v070_signal

def f44cdr_f44_cash_to_debt_ratio_base_v071_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v071_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v071_signal

def f44cdr_f44_cash_to_debt_ratio_base_v072_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v072_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v072_signal

def f44cdr_f44_cash_to_debt_ratio_base_v073_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v073_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v073_signal

def f44cdr_f44_cash_to_debt_ratio_base_v074_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v074_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v074_signal

def f44cdr_f44_cash_to_debt_ratio_base_v075_signal(cashneq, debt):
    res = (cashneq / debt.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_base_v075_signal'] = f44cdr_f44_cash_to_debt_ratio_base_v075_signal

