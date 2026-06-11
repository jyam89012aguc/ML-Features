import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v001_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v001_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v001_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v002_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v002_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v002_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v003_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v003_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v003_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v004_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v004_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v004_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v005_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v005_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v005_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v006_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v006_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v006_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v007_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v007_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v007_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v008_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v008_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v008_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v009_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v009_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v009_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v010_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(63).std()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v010_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v010_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v011_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v011_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v011_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v012_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v012_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v012_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v013_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v013_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v013_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v014_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v014_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v014_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v015_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v015_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v015_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v016_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v016_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v016_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v017_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v017_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v017_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v018_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v018_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v018_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v019_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v019_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v019_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v020_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v020_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v020_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v021_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(5) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v021_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v021_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v022_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(21) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v022_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v022_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v023_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(63) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v023_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v023_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v024_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(126) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v024_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v024_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v025_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).diff(252) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(504).mean())/(capex / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v025_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v025_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v026_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(5) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v026_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v026_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v027_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(21) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v027_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v027_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v028_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(63) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v028_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v028_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v029_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(126) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v029_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v029_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v030_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).diff(252) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median())/(((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v030_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v030_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v031_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v031_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v031_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v032_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v032_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v032_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v033_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v033_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v033_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v034_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v034_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v034_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v035_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((capex / revenue.replace(0, np.nan)).gt((capex / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v035_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v035_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v036_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v036_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v036_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v037_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v037_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v037_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v038_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v038_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v038_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v039_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v039_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v039_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v040_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(126).max()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v040_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v040_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v041_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v041_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v041_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v042_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v042_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v042_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v043_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v043_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v043_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v044_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v044_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v044_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v045_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(252).min()).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v045_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v045_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v046_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v046_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v046_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v047_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v047_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v047_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v048_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v048_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v048_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v049_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v049_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v049_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v050_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(504).max()-(capex / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v050_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v050_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v051_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(5) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v051_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v051_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v052_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(21) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v052_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v052_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v053_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(63) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v053_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v053_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v054_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(126) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v054_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v054_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v055_signal(revenue, capex):
    res = ((((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).diff(252) / (((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((capex / revenue.replace(0, np.nan))-(capex / revenue.replace(0, np.nan)).rolling(21).min())/((capex / revenue.replace(0, np.nan)).rolling(21).max()-(capex / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v055_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v055_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v056_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v056_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v056_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v057_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v057_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v057_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v058_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v058_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v058_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v059_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v059_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v059_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v060_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v060_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v060_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v061_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v061_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v061_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v062_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v062_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v062_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v063_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v063_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v063_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v064_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v064_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v064_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v065_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((capex / revenue.replace(0, np.nan))/(capex / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v065_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v065_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v066_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v066_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v066_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v067_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v067_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v067_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v068_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v068_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v068_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v069_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v069_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v069_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v070_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean() - (capex / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v070_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v070_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v071_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(5) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(5) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v071_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v071_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v072_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(21) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(21) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v072_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v072_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v073_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(63) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(63) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v073_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v073_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v074_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(126) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(126) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v074_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v074_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v075_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(252) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).pct_change(504)).diff(252) / ((capex / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v075_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v075_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v076_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v076_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v076_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v077_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v077_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v077_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v078_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v078_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v078_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v079_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v079_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v079_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v080_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((capex / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v080_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v080_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v081_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v081_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v081_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v082_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v082_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v082_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v083_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v083_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v083_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v084_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v084_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v084_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v085_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(63).mean()/(capex / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v085_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v085_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v086_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v086_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v086_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v087_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v087_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v087_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v088_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v088_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v088_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v089_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v089_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v089_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v090_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(126).std()/(capex / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v090_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v090_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v091_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v091_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v091_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v092_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v092_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v092_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v093_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v093_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v093_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v094_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v094_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v094_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v095_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((capex / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v095_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v095_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v096_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v096_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v096_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v097_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v097_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v097_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v098_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v098_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v098_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v099_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v099_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v099_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v100_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(504).mean() - (capex / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v100_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v100_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v101_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v101_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v101_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v102_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v102_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v102_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v103_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v103_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v103_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v104_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v104_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v104_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v105_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v105_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v105_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v106_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v106_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v106_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v107_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v107_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v107_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v108_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v108_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v108_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v109_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v109_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v109_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v110_signal(revenue, capex, closeadj):
    res = ((((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((capex / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v110_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v110_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v111_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v111_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v111_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v112_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v112_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v112_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v113_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v113_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v113_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v114_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v114_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v114_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v115_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v115_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v115_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v116_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v116_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v116_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v117_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v117_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v117_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v118_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v118_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v118_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v119_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v119_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v119_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v120_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((capex / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v120_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v120_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v121_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v121_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v121_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v122_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v122_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v122_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v123_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v123_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v123_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v124_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v124_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v124_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v125_signal(revenue, capex, closeadj):
    res = (((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((capex / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v125_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v125_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v126_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v126_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v126_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v127_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v127_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v127_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v128_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v128_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v128_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v129_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v129_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v129_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v130_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((capex / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v130_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v130_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v131_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v131_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v131_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v132_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v132_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v132_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v133_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v133_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v133_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v134_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v134_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v134_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v135_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (capex / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v135_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v135_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v136_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(5) / ((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v136_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v136_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v137_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(21) / ((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v137_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v137_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v138_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(63) / ((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v138_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v138_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v139_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(126) / ((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v139_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v139_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v140_signal(revenue, capex):
    res = (((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).diff(252) / ((((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((capex / revenue.replace(0, np.nan)) - (capex / revenue.replace(0, np.nan)).shift(126))/(capex / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v140_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v140_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v141_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v141_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v141_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v142_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v142_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v142_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v143_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v143_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v143_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v144_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v144_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v144_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v145_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((capex / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v145_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v145_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v146_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(5) / (((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v146_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v146_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v147_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(21) / (((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v147_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v147_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v148_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(63) / (((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v148_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v148_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v149_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(126) / (((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v149_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v149_signal

def f41cyc_f41_cyclical_regime_proxies_3rdderiv_v150_signal(revenue, capex):
    res = ((((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).diff(252) / (((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((capex / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f41cyc_f41_cyclical_regime_proxies_3rdderiv_v150_signal'] = f41cyc_f41_cyclical_regime_proxies_3rdderiv_v150_signal

