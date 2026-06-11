import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v001_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v001_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v001_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v002_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v002_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v002_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v003_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v003_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v003_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v004_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v004_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v004_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v005_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v005_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v005_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v006_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).std()).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v006_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v006_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v007_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).std()).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v007_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v007_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v008_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).std()).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v008_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v008_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v009_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).std()).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v009_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v009_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v010_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).std()).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v010_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v010_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v011_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v011_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v011_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v012_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v012_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v012_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v013_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v013_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v013_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v014_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v014_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v014_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v015_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v015_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v015_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v016_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v016_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v016_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v017_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v017_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v017_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v018_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v018_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v018_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v019_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v019_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v019_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v020_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v020_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v020_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v021_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v021_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v021_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v022_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v022_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v022_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v023_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v023_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v023_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v024_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v024_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v024_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v025_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(504).mean())/(cashneq / debt.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v025_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v025_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v026_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v026_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v026_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v027_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v027_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v027_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v028_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v028_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v028_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v029_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v029_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v029_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v030_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median())/(((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v030_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v030_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v031_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v031_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v031_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v032_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v032_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v032_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v033_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v033_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v033_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v034_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v034_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v034_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v035_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((cashneq / debt.replace(0, np.nan)).gt((cashneq / debt.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v035_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v035_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v036_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).max()).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v036_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v036_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v037_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).max()).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v037_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v037_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v038_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).max()).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v038_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v038_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v039_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).max()).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v039_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v039_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v040_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).max()).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v040_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v040_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v041_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).min()).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v041_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v041_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v042_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).min()).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v042_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v042_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v043_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).min()).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v043_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v043_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v044_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).min()).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v044_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v044_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v045_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(252).min()).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v045_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v045_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v046_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).diff(5) / (((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v046_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v046_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v047_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).diff(21) / (((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v047_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v047_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v048_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).diff(63) / (((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v048_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v048_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v049_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).diff(126) / (((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v049_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v049_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v050_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).diff(252) / (((cashneq / debt.replace(0, np.nan)).rolling(504).max()-(cashneq / debt.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v050_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v050_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v051_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v051_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v051_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v052_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v052_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v052_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v053_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v053_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v053_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v054_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v054_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v054_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v055_signal(cashneq, debt):
    res = (((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((cashneq / debt.replace(0, np.nan))-(cashneq / debt.replace(0, np.nan)).rolling(21).min())/((cashneq / debt.replace(0, np.nan)).rolling(21).max()-(cashneq / debt.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v055_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v055_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v056_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v056_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v056_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v057_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v057_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v057_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v058_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v058_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v058_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v059_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v059_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v059_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v060_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v060_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v060_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v061_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v061_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v061_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v062_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v062_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v062_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v063_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v063_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v063_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v064_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v064_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v064_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v065_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((cashneq / debt.replace(0, np.nan))/(cashneq / debt.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v065_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v065_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v066_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v066_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v066_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v067_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v067_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v067_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v068_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v068_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v068_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v069_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v069_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v069_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v070_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean() - (cashneq / debt.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v070_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v070_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v071_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(504)).diff(5) / ((cashneq / debt.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v071_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v071_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v072_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(504)).diff(21) / ((cashneq / debt.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v072_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v072_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v073_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(504)).diff(63) / ((cashneq / debt.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v073_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v073_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v074_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(504)).diff(126) / ((cashneq / debt.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v074_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v074_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v075_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(504)).diff(252) / ((cashneq / debt.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v075_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v075_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v076_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v076_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v076_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v077_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v077_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v077_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v078_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v078_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v078_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v079_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v079_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v079_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v080_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((cashneq / debt.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v080_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v080_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v081_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v081_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v081_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v082_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v082_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v082_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v083_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v083_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v083_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v084_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v084_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v084_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v085_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(63).mean()/(cashneq / debt.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v085_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v085_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v086_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v086_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v086_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v087_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v087_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v087_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v088_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v088_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v088_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v089_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v089_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v089_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v090_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(126).std()/(cashneq / debt.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v090_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v090_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v091_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v091_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v091_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v092_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v092_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v092_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v093_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v093_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v093_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v094_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v094_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v094_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v095_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((cashneq / debt.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v095_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v095_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v096_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).diff(5) / (((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v096_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v096_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v097_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).diff(21) / (((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v097_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v097_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v098_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).diff(63) / (((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v098_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v098_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v099_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).diff(126) / (((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v099_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v099_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v100_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).diff(252) / (((cashneq / debt.replace(0, np.nan)).rolling(504).mean() - (cashneq / debt.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v100_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v100_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v101_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v101_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v101_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v102_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v102_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v102_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v103_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v103_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v103_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v104_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v104_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v104_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v105_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v105_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v105_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v106_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v106_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v106_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v107_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v107_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v107_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v108_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v108_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v108_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v109_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v109_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v109_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v110_signal(cashneq, debt, closeadj):
    res = (((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((cashneq / debt.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v110_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v110_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v111_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v111_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v111_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v112_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v112_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v112_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v113_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v113_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v113_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v114_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v114_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v114_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v115_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v115_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v115_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v116_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v116_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v116_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v117_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v117_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v117_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v118_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v118_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v118_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v119_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v119_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v119_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v120_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((cashneq / debt.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v120_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v120_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v121_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v121_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v121_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v122_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v122_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v122_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v123_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v123_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v123_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v124_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v124_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v124_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v125_signal(cashneq, debt, closeadj):
    res = ((((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((cashneq / debt.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v125_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v125_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v126_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v126_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v126_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v127_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v127_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v127_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v128_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v128_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v128_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v129_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v129_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v129_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v130_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((cashneq / debt.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v130_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v130_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v131_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v131_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v131_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v132_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v132_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v132_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v133_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v133_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v133_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v134_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v134_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v134_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v135_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.75) - (cashneq / debt.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v135_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v135_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v136_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v136_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v136_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v137_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v137_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v137_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v138_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v138_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v138_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v139_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v139_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v139_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v140_signal(cashneq, debt):
    res = ((((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((cashneq / debt.replace(0, np.nan)) - (cashneq / debt.replace(0, np.nan)).shift(126))/(cashneq / debt.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v140_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v140_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v141_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v141_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v141_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v142_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v142_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v142_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v143_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v143_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v143_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v144_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v144_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v144_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v145_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((cashneq / debt.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v145_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v145_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v146_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v146_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v146_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v147_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v147_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v147_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v148_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v148_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v148_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v149_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v149_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v149_signal

def f44cdr_f44_cash_to_debt_ratio_2ndderiv_v150_signal(cashneq, debt):
    res = (((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((cashneq / debt.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f44cdr_f44_cash_to_debt_ratio_2ndderiv_v150_signal'] = f44cdr_f44_cash_to_debt_ratio_2ndderiv_v150_signal

