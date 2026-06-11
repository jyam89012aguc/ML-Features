import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v001_signal(revenue):
    res = (((revenue).rolling(21).mean()).diff(5) / ((revenue).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v001_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v001_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v002_signal(revenue):
    res = (((revenue).rolling(21).mean()).diff(21) / ((revenue).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v002_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v002_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v003_signal(revenue):
    res = (((revenue).rolling(21).mean()).diff(63) / ((revenue).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v003_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v003_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v004_signal(revenue):
    res = (((revenue).rolling(21).mean()).diff(126) / ((revenue).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v004_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v004_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v005_signal(revenue):
    res = (((revenue).rolling(21).mean()).diff(252) / ((revenue).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v005_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v005_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v006_signal(revenue):
    res = (((revenue).rolling(63).std()).diff(5) / ((revenue).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v006_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v006_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v007_signal(revenue):
    res = (((revenue).rolling(63).std()).diff(21) / ((revenue).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v007_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v007_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v008_signal(revenue):
    res = (((revenue).rolling(63).std()).diff(63) / ((revenue).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v008_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v008_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v009_signal(revenue):
    res = (((revenue).rolling(63).std()).diff(126) / ((revenue).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v009_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v009_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v010_signal(revenue):
    res = (((revenue).rolling(63).std()).diff(252) / ((revenue).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v010_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v010_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v011_signal(revenue):
    res = (((revenue).rolling(126).skew()).diff(5) / ((revenue).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v011_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v011_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v012_signal(revenue):
    res = (((revenue).rolling(126).skew()).diff(21) / ((revenue).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v012_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v012_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v013_signal(revenue):
    res = (((revenue).rolling(126).skew()).diff(63) / ((revenue).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v013_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v013_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v014_signal(revenue):
    res = (((revenue).rolling(126).skew()).diff(126) / ((revenue).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v014_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v014_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v015_signal(revenue):
    res = (((revenue).rolling(126).skew()).diff(252) / ((revenue).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v015_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v015_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v016_signal(revenue):
    res = (((revenue).rolling(252).kurt()).diff(5) / ((revenue).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v016_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v016_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v017_signal(revenue):
    res = (((revenue).rolling(252).kurt()).diff(21) / ((revenue).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v017_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v017_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v018_signal(revenue):
    res = (((revenue).rolling(252).kurt()).diff(63) / ((revenue).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v018_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v018_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v019_signal(revenue):
    res = (((revenue).rolling(252).kurt()).diff(126) / ((revenue).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v019_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v019_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v020_signal(revenue):
    res = (((revenue).rolling(252).kurt()).diff(252) / ((revenue).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v020_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v020_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v021_signal(revenue):
    res = (((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).diff(5) / ((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v021_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v021_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v022_signal(revenue):
    res = (((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).diff(21) / ((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v022_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v022_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v023_signal(revenue):
    res = (((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).diff(63) / ((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v023_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v023_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v024_signal(revenue):
    res = (((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).diff(126) / ((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v024_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v024_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v025_signal(revenue):
    res = (((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).diff(252) / ((((revenue)-(revenue).rolling(504).mean())/(revenue).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v025_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v025_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v026_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v026_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v026_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v027_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v027_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v027_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v028_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v028_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v028_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v029_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v029_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v029_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v030_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((revenue)-(revenue).rolling(21).median())/(((revenue)-(revenue).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v030_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v030_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v031_signal(revenue):
    res = ((((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).diff(5) / (((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v031_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v031_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v032_signal(revenue):
    res = ((((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).diff(21) / (((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v032_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v032_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v033_signal(revenue):
    res = ((((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).diff(63) / (((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v033_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v033_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v034_signal(revenue):
    res = ((((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).diff(126) / (((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v034_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v034_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v035_signal(revenue):
    res = ((((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).diff(252) / (((revenue).gt((revenue).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v035_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v035_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v036_signal(revenue):
    res = (((revenue).rolling(126).max()).diff(5) / ((revenue).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v036_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v036_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v037_signal(revenue):
    res = (((revenue).rolling(126).max()).diff(21) / ((revenue).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v037_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v037_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v038_signal(revenue):
    res = (((revenue).rolling(126).max()).diff(63) / ((revenue).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v038_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v038_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v039_signal(revenue):
    res = (((revenue).rolling(126).max()).diff(126) / ((revenue).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v039_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v039_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v040_signal(revenue):
    res = (((revenue).rolling(126).max()).diff(252) / ((revenue).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v040_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v040_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v041_signal(revenue):
    res = (((revenue).rolling(252).min()).diff(5) / ((revenue).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v041_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v041_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v042_signal(revenue):
    res = (((revenue).rolling(252).min()).diff(21) / ((revenue).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v042_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v042_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v043_signal(revenue):
    res = (((revenue).rolling(252).min()).diff(63) / ((revenue).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v043_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v043_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v044_signal(revenue):
    res = (((revenue).rolling(252).min()).diff(126) / ((revenue).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v044_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v044_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v045_signal(revenue):
    res = (((revenue).rolling(252).min()).diff(252) / ((revenue).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v045_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v045_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v046_signal(revenue):
    res = ((((revenue).rolling(504).max()-(revenue).rolling(504).min())).diff(5) / (((revenue).rolling(504).max()-(revenue).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v046_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v046_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v047_signal(revenue):
    res = ((((revenue).rolling(504).max()-(revenue).rolling(504).min())).diff(21) / (((revenue).rolling(504).max()-(revenue).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v047_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v047_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v048_signal(revenue):
    res = ((((revenue).rolling(504).max()-(revenue).rolling(504).min())).diff(63) / (((revenue).rolling(504).max()-(revenue).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v048_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v048_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v049_signal(revenue):
    res = ((((revenue).rolling(504).max()-(revenue).rolling(504).min())).diff(126) / (((revenue).rolling(504).max()-(revenue).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v049_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v049_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v050_signal(revenue):
    res = ((((revenue).rolling(504).max()-(revenue).rolling(504).min())).diff(252) / (((revenue).rolling(504).max()-(revenue).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v050_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v050_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v051_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).diff(5) / ((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v051_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v051_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v052_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).diff(21) / ((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v052_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v052_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v053_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).diff(63) / ((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v053_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v053_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v054_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).diff(126) / ((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v054_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v054_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v055_signal(revenue):
    res = (((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).diff(252) / ((((revenue)-(revenue).rolling(21).min())/((revenue).rolling(21).max()-(revenue).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v055_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v055_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v056_signal(revenue):
    res = ((((revenue)/(revenue).rolling(63).max() - 1)).diff(5) / (((revenue)/(revenue).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v056_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v056_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v057_signal(revenue):
    res = ((((revenue)/(revenue).rolling(63).max() - 1)).diff(21) / (((revenue)/(revenue).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v057_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v057_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v058_signal(revenue):
    res = ((((revenue)/(revenue).rolling(63).max() - 1)).diff(63) / (((revenue)/(revenue).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v058_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v058_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v059_signal(revenue):
    res = ((((revenue)/(revenue).rolling(63).max() - 1)).diff(126) / (((revenue)/(revenue).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v059_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v059_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v060_signal(revenue):
    res = ((((revenue)/(revenue).rolling(63).max() - 1)).diff(252) / (((revenue)/(revenue).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v060_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v060_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v061_signal(revenue):
    res = ((((revenue)/(revenue).rolling(126).min() - 1)).diff(5) / (((revenue)/(revenue).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v061_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v061_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v062_signal(revenue):
    res = ((((revenue)/(revenue).rolling(126).min() - 1)).diff(21) / (((revenue)/(revenue).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v062_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v062_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v063_signal(revenue):
    res = ((((revenue)/(revenue).rolling(126).min() - 1)).diff(63) / (((revenue)/(revenue).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v063_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v063_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v064_signal(revenue):
    res = ((((revenue)/(revenue).rolling(126).min() - 1)).diff(126) / (((revenue)/(revenue).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v064_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v064_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v065_signal(revenue):
    res = ((((revenue)/(revenue).rolling(126).min() - 1)).diff(252) / (((revenue)/(revenue).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v065_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v065_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v066_signal(revenue):
    res = ((((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).diff(5) / (((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v066_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v066_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v067_signal(revenue):
    res = ((((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).diff(21) / (((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v067_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v067_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v068_signal(revenue):
    res = ((((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).diff(63) / (((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v068_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v068_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v069_signal(revenue):
    res = ((((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).diff(126) / (((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v069_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v069_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v070_signal(revenue):
    res = ((((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).diff(252) / (((revenue).ewm(span=252).mean() - (revenue).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v070_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v070_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v071_signal(revenue):
    res = (((revenue).pct_change(504)).diff(5) / ((revenue).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v071_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v071_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v072_signal(revenue):
    res = (((revenue).pct_change(504)).diff(21) / ((revenue).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v072_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v072_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v073_signal(revenue):
    res = (((revenue).pct_change(504)).diff(63) / ((revenue).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v073_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v073_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v074_signal(revenue):
    res = (((revenue).pct_change(504)).diff(126) / ((revenue).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v074_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v074_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v075_signal(revenue):
    res = (((revenue).pct_change(504)).diff(252) / ((revenue).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v075_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v075_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v076_signal(revenue):
    res = (((revenue).diff(21).rolling(21).sum()).diff(5) / ((revenue).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v076_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v076_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v077_signal(revenue):
    res = (((revenue).diff(21).rolling(21).sum()).diff(21) / ((revenue).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v077_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v077_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v078_signal(revenue):
    res = (((revenue).diff(21).rolling(21).sum()).diff(63) / ((revenue).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v078_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v078_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v079_signal(revenue):
    res = (((revenue).diff(21).rolling(21).sum()).diff(126) / ((revenue).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v079_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v079_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v080_signal(revenue):
    res = (((revenue).diff(21).rolling(21).sum()).diff(252) / ((revenue).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v080_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v080_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v081_signal(revenue):
    res = (((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).diff(5) / ((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v081_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v081_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v082_signal(revenue):
    res = (((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).diff(21) / ((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v082_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v082_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v083_signal(revenue):
    res = (((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).diff(63) / ((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v083_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v083_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v084_signal(revenue):
    res = (((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).diff(126) / ((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v084_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v084_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v085_signal(revenue):
    res = (((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).diff(252) / ((revenue).rolling(63).mean()/(revenue).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v085_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v085_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v086_signal(revenue):
    res = (((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).diff(5) / ((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v086_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v086_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v087_signal(revenue):
    res = (((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).diff(21) / ((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v087_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v087_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v088_signal(revenue):
    res = (((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).diff(63) / ((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v088_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v088_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v089_signal(revenue):
    res = (((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).diff(126) / ((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v089_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v089_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v090_signal(revenue):
    res = (((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).diff(252) / ((revenue).rolling(126).std()/(revenue).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v090_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v090_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v091_signal(revenue):
    res = (((revenue).diff().rolling(252).sum()).diff(5) / ((revenue).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v091_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v091_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v092_signal(revenue):
    res = (((revenue).diff().rolling(252).sum()).diff(21) / ((revenue).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v092_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v092_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v093_signal(revenue):
    res = (((revenue).diff().rolling(252).sum()).diff(63) / ((revenue).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v093_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v093_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v094_signal(revenue):
    res = (((revenue).diff().rolling(252).sum()).diff(126) / ((revenue).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v094_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v094_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v095_signal(revenue):
    res = (((revenue).diff().rolling(252).sum()).diff(252) / ((revenue).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v095_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v095_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v096_signal(revenue):
    res = ((((revenue).rolling(504).mean() - (revenue).shift(504))).diff(5) / (((revenue).rolling(504).mean() - (revenue).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v096_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v096_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v097_signal(revenue):
    res = ((((revenue).rolling(504).mean() - (revenue).shift(504))).diff(21) / (((revenue).rolling(504).mean() - (revenue).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v097_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v097_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v098_signal(revenue):
    res = ((((revenue).rolling(504).mean() - (revenue).shift(504))).diff(63) / (((revenue).rolling(504).mean() - (revenue).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v098_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v098_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v099_signal(revenue):
    res = ((((revenue).rolling(504).mean() - (revenue).shift(504))).diff(126) / (((revenue).rolling(504).mean() - (revenue).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v099_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v099_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v100_signal(revenue):
    res = ((((revenue).rolling(504).mean() - (revenue).shift(504))).diff(252) / (((revenue).rolling(504).mean() - (revenue).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v100_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v100_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v101_signal(revenue, closeadj):
    res = (((revenue).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((revenue).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v101_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v101_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v102_signal(revenue, closeadj):
    res = (((revenue).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((revenue).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v102_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v102_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v103_signal(revenue, closeadj):
    res = (((revenue).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((revenue).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v103_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v103_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v104_signal(revenue, closeadj):
    res = (((revenue).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((revenue).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v104_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v104_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v105_signal(revenue, closeadj):
    res = (((revenue).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((revenue).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v105_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v105_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v106_signal(revenue, closeadj):
    res = (((revenue).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((revenue).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v106_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v106_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v107_signal(revenue, closeadj):
    res = (((revenue).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((revenue).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v107_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v107_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v108_signal(revenue, closeadj):
    res = (((revenue).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((revenue).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v108_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v108_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v109_signal(revenue, closeadj):
    res = (((revenue).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((revenue).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v109_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v109_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v110_signal(revenue, closeadj):
    res = (((revenue).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((revenue).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v110_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v110_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v111_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(126).mean()).diff(5) / (((revenue)/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v111_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v111_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v112_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(126).mean()).diff(21) / (((revenue)/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v112_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v112_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v113_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(126).mean()).diff(63) / (((revenue)/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v113_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v113_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v114_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(126).mean()).diff(126) / (((revenue)/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v114_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v114_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v115_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(126).mean()).diff(252) / (((revenue)/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v115_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v115_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v116_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(252).std()).diff(5) / (((revenue)/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v116_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v116_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v117_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(252).std()).diff(21) / (((revenue)/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v117_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v117_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v118_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(252).std()).diff(63) / (((revenue)/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v118_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v118_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v119_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(252).std()).diff(126) / (((revenue)/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v119_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v119_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v120_signal(revenue, closeadj):
    res = ((((revenue)/closeadj).rolling(252).std()).diff(252) / (((revenue)/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v120_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v120_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v121_signal(revenue, closeadj):
    res = ((((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v121_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v121_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v122_signal(revenue, closeadj):
    res = ((((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v122_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v122_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v123_signal(revenue, closeadj):
    res = ((((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v123_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v123_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v124_signal(revenue, closeadj):
    res = ((((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v124_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v124_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v125_signal(revenue, closeadj):
    res = ((((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((revenue).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v125_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v125_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v126_signal(revenue):
    res = ((((revenue).diff().gt(0)).rolling(21).mean()).diff(5) / (((revenue).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v126_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v126_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v127_signal(revenue):
    res = ((((revenue).diff().gt(0)).rolling(21).mean()).diff(21) / (((revenue).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v127_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v127_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v128_signal(revenue):
    res = ((((revenue).diff().gt(0)).rolling(21).mean()).diff(63) / (((revenue).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v128_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v128_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v129_signal(revenue):
    res = ((((revenue).diff().gt(0)).rolling(21).mean()).diff(126) / (((revenue).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v129_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v129_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v130_signal(revenue):
    res = ((((revenue).diff().gt(0)).rolling(21).mean()).diff(252) / (((revenue).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v130_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v130_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v131_signal(revenue):
    res = (((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).diff(5) / ((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v131_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v131_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v132_signal(revenue):
    res = (((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).diff(21) / ((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v132_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v132_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v133_signal(revenue):
    res = (((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).diff(63) / ((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v133_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v133_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v134_signal(revenue):
    res = (((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).diff(126) / ((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v134_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v134_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v135_signal(revenue):
    res = (((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).diff(252) / ((revenue).rolling(63).quantile(0.75) - (revenue).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v135_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v135_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v136_signal(revenue):
    res = ((((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).diff(5) / (((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v136_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v136_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v137_signal(revenue):
    res = ((((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).diff(21) / (((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v137_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v137_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v138_signal(revenue):
    res = ((((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).diff(63) / (((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v138_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v138_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v139_signal(revenue):
    res = ((((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).diff(126) / (((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v139_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v139_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v140_signal(revenue):
    res = ((((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).diff(252) / (((revenue) - (revenue).shift(126))/(revenue).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v140_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v140_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v141_signal(revenue):
    res = (((revenue).ewm(span=252).mean()).diff(5) / ((revenue).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v141_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v141_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v142_signal(revenue):
    res = (((revenue).ewm(span=252).mean()).diff(21) / ((revenue).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v142_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v142_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v143_signal(revenue):
    res = (((revenue).ewm(span=252).mean()).diff(63) / ((revenue).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v143_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v143_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v144_signal(revenue):
    res = (((revenue).ewm(span=252).mean()).diff(126) / ((revenue).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v144_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v144_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v145_signal(revenue):
    res = (((revenue).ewm(span=252).mean()).diff(252) / ((revenue).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v145_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v145_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v146_signal(revenue):
    res = (((revenue).ewm(span=504).std()).diff(5) / ((revenue).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v146_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v146_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v147_signal(revenue):
    res = (((revenue).ewm(span=504).std()).diff(21) / ((revenue).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v147_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v147_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v148_signal(revenue):
    res = (((revenue).ewm(span=504).std()).diff(63) / ((revenue).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v148_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v148_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v149_signal(revenue):
    res = (((revenue).ewm(span=504).std()).diff(126) / ((revenue).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v149_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v149_signal

def f50rdr_f50_revenue_dispersion_regime_2ndderiv_v150_signal(revenue):
    res = (((revenue).ewm(span=504).std()).diff(252) / ((revenue).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f50rdr_f50_revenue_dispersion_regime_2ndderiv_v150_signal'] = f50rdr_f50_revenue_dispersion_regime_2ndderiv_v150_signal

