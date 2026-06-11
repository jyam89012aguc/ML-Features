import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f43int_f43_interest_expense_resilience_3rdderiv_v001_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v001_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v001_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v002_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v002_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v002_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v003_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v003_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v003_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v004_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v004_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v004_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v005_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v005_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v005_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v006_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v006_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v006_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v007_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v007_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v007_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v008_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v008_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v008_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v009_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v009_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v009_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v010_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(63).std()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v010_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v010_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v011_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v011_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v011_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v012_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v012_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v012_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v013_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v013_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v013_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v014_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v014_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v014_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v015_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v015_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v015_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v016_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v016_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v016_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v017_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v017_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v017_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v018_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v018_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v018_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v019_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v019_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v019_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v020_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v020_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v020_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v021_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(5) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v021_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v021_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v022_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(21) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v022_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v022_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v023_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(63) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v023_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v023_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v024_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(126) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v024_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v024_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v025_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(252) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(504).mean())/(ebit / intexp.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v025_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v025_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v026_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(5) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v026_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v026_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v027_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(21) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v027_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v027_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v028_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(63) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v028_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v028_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v029_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(126) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v029_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v029_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v030_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(252) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median())/(((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v030_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v030_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v031_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v031_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v031_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v032_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v032_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v032_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v033_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v033_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v033_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v034_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v034_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v034_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v035_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((ebit / intexp.replace(0, np.nan)).gt((ebit / intexp.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v035_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v035_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v036_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v036_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v036_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v037_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v037_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v037_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v038_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v038_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v038_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v039_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v039_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v039_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v040_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(126).max()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v040_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v040_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v041_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v041_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v041_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v042_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v042_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v042_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v043_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v043_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v043_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v044_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v044_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v044_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v045_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(252).min()).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v045_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v045_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v046_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v046_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v046_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v047_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v047_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v047_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v048_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v048_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v048_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v049_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v049_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v049_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v050_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(504).max()-(ebit / intexp.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v050_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v050_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v051_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(5) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v051_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v051_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v052_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(21) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v052_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v052_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v053_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(63) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v053_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v053_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v054_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(126) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v054_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v054_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v055_signal(intexp, ebit):
    res = ((((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(252) / (((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((ebit / intexp.replace(0, np.nan))-(ebit / intexp.replace(0, np.nan)).rolling(21).min())/((ebit / intexp.replace(0, np.nan)).rolling(21).max()-(ebit / intexp.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v055_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v055_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v056_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v056_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v056_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v057_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v057_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v057_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v058_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v058_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v058_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v059_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v059_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v059_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v060_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v060_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v060_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v061_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v061_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v061_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v062_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v062_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v062_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v063_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v063_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v063_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v064_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v064_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v064_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v065_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((ebit / intexp.replace(0, np.nan))/(ebit / intexp.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v065_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v065_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v066_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v066_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v066_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v067_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v067_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v067_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v068_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v068_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v068_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v069_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v069_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v069_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v070_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean() - (ebit / intexp.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v070_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v070_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v071_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(5) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(5) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v071_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v071_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v072_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(21) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(21) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v072_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v072_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v073_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(63) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(63) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v073_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v073_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v074_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(126) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(126) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v074_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v074_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v075_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(252) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).pct_change(504)).diff(252) / ((ebit / intexp.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v075_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v075_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v076_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v076_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v076_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v077_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v077_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v077_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v078_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v078_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v078_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v079_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v079_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v079_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v080_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((ebit / intexp.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v080_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v080_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v081_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v081_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v081_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v082_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v082_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v082_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v083_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v083_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v083_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v084_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v084_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v084_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v085_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(63).mean()/(ebit / intexp.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v085_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v085_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v086_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v086_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v086_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v087_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v087_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v087_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v088_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v088_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v088_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v089_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v089_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v089_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v090_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(126).std()/(ebit / intexp.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v090_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v090_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v091_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v091_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v091_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v092_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v092_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v092_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v093_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v093_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v093_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v094_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v094_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v094_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v095_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((ebit / intexp.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v095_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v095_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v096_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v096_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v096_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v097_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v097_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v097_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v098_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v098_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v098_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v099_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v099_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v099_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v100_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(504).mean() - (ebit / intexp.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v100_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v100_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v101_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v101_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v101_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v102_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v102_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v102_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v103_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v103_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v103_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v104_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v104_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v104_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v105_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v105_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v105_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v106_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v106_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v106_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v107_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v107_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v107_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v108_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v108_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v108_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v109_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v109_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v109_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v110_signal(intexp, ebit, closeadj):
    res = ((((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((ebit / intexp.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v110_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v110_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v111_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v111_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v111_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v112_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v112_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v112_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v113_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v113_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v113_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v114_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v114_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v114_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v115_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v115_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v115_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v116_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v116_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v116_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v117_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v117_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v117_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v118_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v118_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v118_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v119_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v119_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v119_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v120_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((ebit / intexp.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v120_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v120_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v121_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v121_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v121_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v122_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v122_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v122_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v123_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v123_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v123_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v124_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v124_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v124_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v125_signal(intexp, ebit, closeadj):
    res = (((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((ebit / intexp.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v125_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v125_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v126_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v126_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v126_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v127_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v127_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v127_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v128_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v128_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v128_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v129_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v129_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v129_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v130_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((ebit / intexp.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v130_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v130_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v131_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v131_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v131_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v132_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v132_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v132_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v133_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v133_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v133_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v134_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v134_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v134_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v135_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.75) - (ebit / intexp.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v135_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v135_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v136_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(5) / ((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v136_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v136_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v137_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(21) / ((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v137_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v137_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v138_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(63) / ((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v138_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v138_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v139_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(126) / ((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v139_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v139_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v140_signal(intexp, ebit):
    res = (((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(252) / ((((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((ebit / intexp.replace(0, np.nan)) - (ebit / intexp.replace(0, np.nan)).shift(126))/(ebit / intexp.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v140_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v140_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v141_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v141_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v141_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v142_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v142_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v142_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v143_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v143_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v143_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v144_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v144_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v144_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v145_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((ebit / intexp.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v145_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v145_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v146_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(5) / (((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v146_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v146_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v147_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(21) / (((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v147_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v147_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v148_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(63) / (((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v148_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v148_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v149_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(126) / (((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v149_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v149_signal

def f43int_f43_interest_expense_resilience_3rdderiv_v150_signal(intexp, ebit):
    res = ((((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(252) / (((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((ebit / intexp.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f43int_f43_interest_expense_resilience_3rdderiv_v150_signal'] = f43int_f43_interest_expense_resilience_3rdderiv_v150_signal

