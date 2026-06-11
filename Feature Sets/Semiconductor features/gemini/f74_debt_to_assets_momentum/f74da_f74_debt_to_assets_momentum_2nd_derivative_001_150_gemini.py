import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f74da_f74_debt_to_assets_momentum_2ndderiv_v001_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v001_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v001_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v002_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v002_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v002_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v003_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v003_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v003_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v004_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v004_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v004_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v005_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v005_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v005_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v006_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).std()).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v006_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v006_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v007_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).std()).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v007_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v007_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v008_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).std()).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v008_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v008_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v009_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).std()).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v009_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v009_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v010_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).std()).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v010_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v010_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v011_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v011_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v011_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v012_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v012_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v012_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v013_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v013_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v013_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v014_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v014_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v014_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v015_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v015_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v015_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v016_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v016_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v016_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v017_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v017_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v017_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v018_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v018_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v018_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v019_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v019_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v019_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v020_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v020_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v020_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v021_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v021_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v021_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v022_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v022_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v022_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v023_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v023_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v023_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v024_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v024_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v024_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v025_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(504).mean())/(debt / assets.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v025_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v025_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v026_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v026_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v026_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v027_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v027_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v027_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v028_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v028_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v028_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v029_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v029_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v029_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v030_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median())/(((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v030_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v030_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v031_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v031_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v031_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v032_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v032_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v032_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v033_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v033_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v033_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v034_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v034_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v034_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v035_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((debt / assets.replace(0, np.nan)).gt((debt / assets.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v035_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v035_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v036_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).max()).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v036_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v036_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v037_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).max()).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v037_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v037_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v038_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).max()).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v038_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v038_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v039_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).max()).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v039_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v039_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v040_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).max()).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v040_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v040_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v041_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).min()).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v041_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v041_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v042_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).min()).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v042_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v042_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v043_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).min()).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v043_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v043_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v044_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).min()).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v044_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v044_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v045_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(252).min()).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v045_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v045_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v046_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).diff(5) / (((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v046_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v046_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v047_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).diff(21) / (((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v047_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v047_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v048_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).diff(63) / (((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v048_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v048_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v049_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).diff(126) / (((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v049_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v049_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v050_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).diff(252) / (((debt / assets.replace(0, np.nan)).rolling(504).max()-(debt / assets.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v050_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v050_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v051_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v051_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v051_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v052_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v052_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v052_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v053_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v053_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v053_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v054_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v054_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v054_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v055_signal(debt, assets):
    res = (((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((debt / assets.replace(0, np.nan))-(debt / assets.replace(0, np.nan)).rolling(21).min())/((debt / assets.replace(0, np.nan)).rolling(21).max()-(debt / assets.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v055_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v055_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v056_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v056_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v056_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v057_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v057_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v057_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v058_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v058_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v058_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v059_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v059_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v059_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v060_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v060_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v060_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v061_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v061_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v061_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v062_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v062_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v062_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v063_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v063_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v063_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v064_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v064_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v064_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v065_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((debt / assets.replace(0, np.nan))/(debt / assets.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v065_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v065_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v066_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v066_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v066_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v067_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v067_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v067_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v068_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v068_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v068_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v069_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v069_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v069_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v070_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((debt / assets.replace(0, np.nan)).ewm(span=252).mean() - (debt / assets.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v070_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v070_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v071_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).pct_change(504)).diff(5) / ((debt / assets.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v071_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v071_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v072_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).pct_change(504)).diff(21) / ((debt / assets.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v072_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v072_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v073_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).pct_change(504)).diff(63) / ((debt / assets.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v073_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v073_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v074_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).pct_change(504)).diff(126) / ((debt / assets.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v074_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v074_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v075_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).pct_change(504)).diff(252) / ((debt / assets.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v075_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v075_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v076_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v076_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v076_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v077_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v077_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v077_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v078_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v078_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v078_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v079_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v079_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v079_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v080_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((debt / assets.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v080_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v080_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v081_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v081_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v081_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v082_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v082_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v082_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v083_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v083_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v083_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v084_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v084_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v084_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v085_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(63).mean()/(debt / assets.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v085_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v085_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v086_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v086_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v086_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v087_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v087_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v087_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v088_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v088_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v088_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v089_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v089_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v089_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v090_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(126).std()/(debt / assets.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v090_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v090_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v091_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v091_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v091_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v092_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v092_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v092_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v093_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v093_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v093_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v094_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v094_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v094_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v095_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((debt / assets.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v095_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v095_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v096_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).diff(5) / (((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v096_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v096_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v097_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).diff(21) / (((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v097_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v097_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v098_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).diff(63) / (((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v098_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v098_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v099_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).diff(126) / (((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v099_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v099_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v100_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).diff(252) / (((debt / assets.replace(0, np.nan)).rolling(504).mean() - (debt / assets.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v100_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v100_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v101_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v101_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v101_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v102_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v102_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v102_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v103_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v103_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v103_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v104_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v104_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v104_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v105_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v105_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v105_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v106_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v106_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v106_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v107_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v107_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v107_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v108_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v108_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v108_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v109_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v109_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v109_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v110_signal(debt, assets, closeadj):
    res = (((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((debt / assets.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v110_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v110_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v111_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v111_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v111_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v112_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v112_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v112_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v113_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v113_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v113_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v114_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v114_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v114_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v115_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v115_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v115_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v116_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v116_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v116_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v117_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v117_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v117_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v118_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v118_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v118_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v119_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v119_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v119_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v120_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((debt / assets.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v120_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v120_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v121_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v121_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v121_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v122_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v122_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v122_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v123_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v123_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v123_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v124_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v124_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v124_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v125_signal(debt, assets, closeadj):
    res = ((((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((debt / assets.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v125_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v125_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v126_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v126_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v126_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v127_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v127_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v127_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v128_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v128_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v128_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v129_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v129_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v129_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v130_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((debt / assets.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v130_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v130_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v131_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v131_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v131_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v132_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v132_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v132_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v133_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v133_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v133_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v134_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v134_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v134_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v135_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((debt / assets.replace(0, np.nan)).rolling(63).quantile(0.75) - (debt / assets.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v135_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v135_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v136_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v136_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v136_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v137_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v137_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v137_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v138_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v138_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v138_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v139_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v139_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v139_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v140_signal(debt, assets):
    res = ((((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((debt / assets.replace(0, np.nan)) - (debt / assets.replace(0, np.nan)).shift(126))/(debt / assets.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v140_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v140_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v141_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v141_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v141_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v142_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v142_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v142_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v143_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v143_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v143_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v144_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v144_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v144_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v145_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((debt / assets.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v145_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v145_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v146_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((debt / assets.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v146_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v146_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v147_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((debt / assets.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v147_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v147_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v148_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((debt / assets.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v148_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v148_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v149_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((debt / assets.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v149_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v149_signal

def f74da_f74_debt_to_assets_momentum_2ndderiv_v150_signal(debt, assets):
    res = (((debt / assets.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((debt / assets.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_2ndderiv_v150_signal'] = f74da_f74_debt_to_assets_momentum_2ndderiv_v150_signal

