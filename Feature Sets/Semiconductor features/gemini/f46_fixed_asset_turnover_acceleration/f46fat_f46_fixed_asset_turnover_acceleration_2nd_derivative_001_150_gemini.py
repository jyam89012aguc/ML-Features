import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v001_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v001_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v001_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v002_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v002_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v002_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v003_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v003_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v003_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v004_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v004_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v004_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v005_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v005_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v005_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v006_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v006_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v006_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v007_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v007_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v007_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v008_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v008_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v008_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v009_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v009_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v009_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v010_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v010_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v010_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v011_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v011_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v011_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v012_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v012_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v012_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v013_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v013_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v013_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v014_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v014_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v014_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v015_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v015_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v015_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v016_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v016_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v016_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v017_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v017_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v017_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v018_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v018_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v018_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v019_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v019_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v019_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v020_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v020_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v020_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v021_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v021_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v021_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v022_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v022_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v022_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v023_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v023_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v023_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v024_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v024_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v024_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v025_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v025_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v025_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v026_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v026_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v026_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v027_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v027_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v027_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v028_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v028_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v028_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v029_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v029_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v029_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v030_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v030_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v030_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v031_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v031_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v031_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v032_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v032_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v032_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v033_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v033_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v033_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v034_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v034_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v034_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v035_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v035_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v035_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v036_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v036_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v036_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v037_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v037_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v037_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v038_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v038_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v038_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v039_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v039_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v039_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v040_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v040_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v040_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v041_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v041_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v041_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v042_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v042_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v042_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v043_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v043_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v043_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v044_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v044_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v044_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v045_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v045_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v045_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v046_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).diff(5) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v046_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v046_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v047_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).diff(21) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v047_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v047_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v048_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).diff(63) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v048_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v048_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v049_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).diff(126) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v049_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v049_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v050_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).diff(252) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v050_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v050_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v051_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v051_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v051_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v052_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v052_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v052_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v053_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v053_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v053_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v054_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v054_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v054_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v055_signal(revenue, ppnenet):
    res = (((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v055_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v055_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v056_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v056_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v056_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v057_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v057_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v057_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v058_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v058_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v058_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v059_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v059_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v059_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v060_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v060_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v060_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v061_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v061_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v061_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v062_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v062_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v062_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v063_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v063_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v063_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v064_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v064_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v064_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v065_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v065_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v065_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v066_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v066_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v066_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v067_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v067_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v067_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v068_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v068_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v068_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v069_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v069_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v069_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v070_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v070_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v070_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v071_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v071_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v071_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v072_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v072_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v072_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v073_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v073_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v073_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v074_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v074_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v074_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v075_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v075_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v075_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v076_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v076_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v076_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v077_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v077_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v077_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v078_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v078_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v078_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v079_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v079_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v079_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v080_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v080_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v080_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v081_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v081_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v081_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v082_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v082_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v082_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v083_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v083_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v083_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v084_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v084_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v084_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v085_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()/(revenue / ppnenet.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v085_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v085_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v086_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v086_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v086_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v087_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v087_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v087_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v088_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v088_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v088_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v089_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v089_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v089_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v090_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(126).std()/(revenue / ppnenet.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v090_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v090_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v091_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v091_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v091_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v092_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v092_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v092_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v093_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v093_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v093_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v094_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v094_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v094_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v095_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v095_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v095_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v096_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).diff(5) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v096_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v096_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v097_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).diff(21) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v097_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v097_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v098_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).diff(63) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v098_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v098_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v099_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).diff(126) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v099_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v099_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v100_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).diff(252) / (((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean() - (revenue / ppnenet.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v100_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v100_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v101_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v101_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v101_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v102_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v102_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v102_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v103_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v103_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v103_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v104_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v104_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v104_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v105_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v105_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v105_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v106_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v106_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v106_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v107_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v107_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v107_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v108_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v108_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v108_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v109_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v109_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v109_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v110_signal(revenue, ppnenet, closeadj):
    res = (((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v110_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v110_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v111_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v111_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v111_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v112_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v112_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v112_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v113_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v113_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v113_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v114_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v114_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v114_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v115_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v115_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v115_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v116_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v116_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v116_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v117_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v117_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v117_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v118_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v118_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v118_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v119_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v119_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v119_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v120_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((revenue / ppnenet.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v120_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v120_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v121_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v121_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v121_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v122_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v122_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v122_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v123_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v123_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v123_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v124_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v124_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v124_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v125_signal(revenue, ppnenet, closeadj):
    res = ((((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((revenue / ppnenet.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v125_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v125_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v126_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v126_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v126_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v127_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v127_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v127_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v128_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v128_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v128_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v129_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v129_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v129_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v130_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((revenue / ppnenet.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v130_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v130_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v131_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v131_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v131_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v132_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v132_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v132_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v133_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v133_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v133_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v134_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v134_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v134_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v135_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.75) - (revenue / ppnenet.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v135_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v135_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v136_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v136_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v136_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v137_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v137_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v137_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v138_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v138_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v138_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v139_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v139_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v139_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v140_signal(revenue, ppnenet):
    res = ((((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((revenue / ppnenet.replace(0, np.nan)) - (revenue / ppnenet.replace(0, np.nan)).shift(126))/(revenue / ppnenet.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v140_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v140_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v141_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v141_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v141_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v142_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v142_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v142_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v143_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v143_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v143_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v144_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v144_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v144_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v145_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v145_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v145_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v146_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v146_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v146_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v147_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v147_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v147_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v148_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v148_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v148_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v149_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v149_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v149_signal

def f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v150_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v150_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_2ndderiv_v150_signal

