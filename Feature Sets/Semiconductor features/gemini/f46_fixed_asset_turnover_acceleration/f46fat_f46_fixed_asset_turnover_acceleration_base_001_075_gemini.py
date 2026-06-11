import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f46fat_f46_fixed_asset_turnover_acceleration_base_v001_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v001_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v001_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v002_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v002_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v002_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v003_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v003_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v003_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v004_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v004_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v004_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v005_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v005_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v005_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v006_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v006_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v006_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v007_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v007_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v007_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v008_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v008_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v008_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v009_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v009_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v009_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v010_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v010_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v010_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v011_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v011_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v011_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v012_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v012_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v012_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v013_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v013_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v013_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v014_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v014_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v014_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v015_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v015_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v015_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v016_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v016_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v016_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v017_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v017_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v017_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v018_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v018_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v018_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v019_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v019_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v019_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v020_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v020_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v020_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v021_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v021_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v021_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v022_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(63).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v022_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v022_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v023_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(126).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v023_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v023_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v024_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(252).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v024_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v024_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v025_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).mean())/(revenue / ppnenet.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v025_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v025_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v026_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v026_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v026_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v027_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(63).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v027_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v027_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v028_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(126).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v028_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v028_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v029_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(252).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v029_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v029_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v030_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).median())/(((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v030_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v030_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v031_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v031_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v031_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v032_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v032_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v032_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v033_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v033_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v033_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v034_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v034_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v034_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v035_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).gt((revenue / ppnenet.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v035_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v035_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v036_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v036_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v036_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v037_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v037_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v037_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v038_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v038_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v038_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v039_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v039_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v039_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v040_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v040_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v040_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v041_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v041_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v041_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v042_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v042_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v042_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v043_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v043_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v043_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v044_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v044_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v044_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v045_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v045_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v045_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v046_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v046_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v046_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v047_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).rolling(63).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v047_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v047_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v048_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v048_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v048_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v049_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).rolling(252).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v049_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v049_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v050_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v050_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v050_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v051_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(21).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v051_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v051_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v052_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(63).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(63).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v052_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v052_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v053_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(126).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(126).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v053_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v053_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v054_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(252).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(252).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v054_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v054_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v055_signal(revenue, ppnenet):
    res = (((revenue / ppnenet.replace(0, np.nan))-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min())/((revenue / ppnenet.replace(0, np.nan)).rolling(504).max()-(revenue / ppnenet.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v055_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v055_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v056_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v056_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v056_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v057_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v057_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v057_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v058_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v058_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v058_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v059_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v059_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v059_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v060_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v060_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v060_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v061_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v061_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v061_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v062_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v062_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v062_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v063_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v063_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v063_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v064_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v064_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v064_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v065_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan))/(revenue / ppnenet.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v065_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v065_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v066_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).ewm(span=21).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v066_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v066_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v067_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).ewm(span=63).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v067_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v067_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v068_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).ewm(span=126).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v068_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v068_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v069_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).ewm(span=252).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v069_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v069_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v070_signal(revenue, ppnenet):
    res = ((revenue / ppnenet.replace(0, np.nan)).ewm(span=504).mean() - (revenue / ppnenet.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v070_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v070_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v071_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v071_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v071_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v072_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v072_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v072_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v073_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v073_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v073_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v074_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v074_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v074_signal

def f46fat_f46_fixed_asset_turnover_acceleration_base_v075_signal(revenue, ppnenet):
    res = (revenue / ppnenet.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f46fat_f46_fixed_asset_turnover_acceleration_base_v075_signal'] = f46fat_f46_fixed_asset_turnover_acceleration_base_v075_signal

