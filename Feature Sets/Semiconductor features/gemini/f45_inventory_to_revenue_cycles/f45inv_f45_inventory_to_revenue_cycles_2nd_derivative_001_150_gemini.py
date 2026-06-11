import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v001_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v001_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v001_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v002_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v002_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v002_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v003_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v003_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v003_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v004_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v004_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v004_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v005_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v005_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v005_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v006_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).std()).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v006_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v006_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v007_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).std()).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v007_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v007_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v008_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).std()).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v008_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v008_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v009_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).std()).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v009_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v009_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v010_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).std()).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(63).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v010_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v010_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v011_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v011_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v011_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v012_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v012_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v012_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v013_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v013_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v013_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v014_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v014_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v014_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v015_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(126).skew()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v015_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v015_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v016_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v016_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v016_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v017_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v017_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v017_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v018_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v018_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v018_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v019_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v019_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v019_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v020_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(252).kurt()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v020_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v020_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v021_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).diff(5) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v021_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v021_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v022_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).diff(21) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v022_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v022_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v023_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).diff(63) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v023_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v023_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v024_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).diff(126) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v024_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v024_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v025_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).diff(252) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v025_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v025_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v026_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(5) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v026_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v026_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v027_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(21) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v027_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v027_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v028_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(63) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v028_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v028_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v029_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(126) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v029_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v029_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v030_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).diff(252) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v030_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v030_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v031_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(5) / (((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v031_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v031_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v032_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(21) / (((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v032_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v032_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v033_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(63) / (((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v033_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v033_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v034_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(126) / (((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v034_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v034_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v035_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).diff(252) / (((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v035_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v035_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v036_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).max()).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v036_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v036_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v037_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).max()).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v037_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v037_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v038_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).max()).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v038_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v038_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v039_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).max()).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v039_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v039_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v040_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).max()).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(126).max()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v040_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v040_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v041_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).min()).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v041_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v041_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v042_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).min()).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v042_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v042_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v043_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).min()).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v043_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v043_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v044_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).min()).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v044_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v044_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v045_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(252).min()).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(252).min()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v045_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v045_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v046_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).diff(5) / (((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v046_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v046_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v047_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).diff(21) / (((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v047_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v047_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v048_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).diff(63) / (((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v048_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v048_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v049_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).diff(126) / (((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v049_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v049_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v050_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).diff(252) / (((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v050_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v050_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v051_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).diff(5) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v051_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v051_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v052_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).diff(21) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v052_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v052_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v053_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).diff(63) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v053_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v053_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v054_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).diff(126) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v054_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v054_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v055_signal(inventory, revenue):
    res = (((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).diff(252) / ((((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v055_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v055_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v056_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(5) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v056_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v056_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v057_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(21) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v057_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v057_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v058_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(63) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v058_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v058_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v059_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(126) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v059_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v059_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v060_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).diff(252) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v060_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v060_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v061_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(5) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v061_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v061_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v062_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(21) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v062_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v062_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v063_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(63) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v063_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v063_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v064_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(126) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v064_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v064_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v065_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).diff(252) / (((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v065_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v065_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v066_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(5) / (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v066_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v066_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v067_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(21) / (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v067_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v067_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v068_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(63) / (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v068_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v068_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v069_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(126) / (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v069_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v069_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v070_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).diff(252) / (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v070_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v070_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v071_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(504)).diff(5) / ((inventory / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v071_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v071_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v072_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(504)).diff(21) / ((inventory / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v072_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v072_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v073_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(504)).diff(63) / ((inventory / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v073_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v073_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v074_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(504)).diff(126) / ((inventory / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v074_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v074_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v075_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(504)).diff(252) / ((inventory / revenue.replace(0, np.nan)).pct_change(504)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v075_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v075_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v076_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(5) / ((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v076_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v076_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v077_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(21) / ((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v077_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v077_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v078_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(63) / ((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v078_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v078_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v079_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(126) / ((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v079_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v079_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v080_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).diff(252) / ((inventory / revenue.replace(0, np.nan)).diff(21).rolling(21).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v080_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v080_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v081_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v081_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v081_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v082_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v082_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v082_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v083_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v083_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v083_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v084_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v084_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v084_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v085_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(63).mean()/(inventory / revenue.replace(0, np.nan)).rolling(63*2).mean() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v085_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v085_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v086_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v086_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v086_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v087_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v087_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v087_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v088_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v088_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v088_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v089_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v089_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v089_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v090_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(126).std()/(inventory / revenue.replace(0, np.nan)).rolling(126*2).std() - 1).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v090_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v090_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v091_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(5) / ((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v091_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v091_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v092_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(21) / ((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v092_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v092_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v093_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(63) / ((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v093_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v093_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v094_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(126) / ((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v094_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v094_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v095_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).diff(252) / ((inventory / revenue.replace(0, np.nan)).diff().rolling(252).sum()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v095_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v095_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v096_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).diff(5) / (((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v096_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v096_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v097_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).diff(21) / (((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v097_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v097_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v098_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).diff(63) / (((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v098_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v098_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v099_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).diff(126) / (((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v099_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v099_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v100_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).diff(252) / (((inventory / revenue.replace(0, np.nan)).rolling(504).mean() - (inventory / revenue.replace(0, np.nan)).shift(504))).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v100_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v100_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v101_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v101_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v101_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v102_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v102_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v102_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v103_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v103_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v103_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v104_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v104_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v104_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v105_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(21).mean() * closeadj.pct_change(21)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v105_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v105_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v106_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(5) / ((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v106_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v106_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v107_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(21) / ((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v107_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v107_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v108_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(63) / ((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v108_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v108_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v109_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(126) / ((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v109_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v109_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v110_signal(inventory, revenue, closeadj):
    res = (((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).diff(252) / ((inventory / revenue.replace(0, np.nan)).pct_change(63) * closeadj.pct_change(63)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v110_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v110_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v111_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(5) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v111_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v111_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v112_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(21) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v112_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v112_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v113_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(63) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v113_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v113_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v114_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(126) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v114_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v114_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v115_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).diff(252) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(126).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v115_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v115_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v116_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(5) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v116_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v116_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v117_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(21) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v117_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v117_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v118_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(63) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v118_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v118_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v119_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(126) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v119_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v119_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v120_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).diff(252) / (((inventory / revenue.replace(0, np.nan))/closeadj).rolling(252).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v120_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v120_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v121_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(5) / (((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v121_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v121_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v122_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(21) / (((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v122_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v122_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v123_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(63) / (((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v123_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v123_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v124_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(126) / (((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v124_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v124_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v125_signal(inventory, revenue, closeadj):
    res = ((((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).diff(252) / (((inventory / revenue.replace(0, np.nan)).rank(pct=True) - closeadj.rank(pct=True)).rolling(504).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v125_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v125_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v126_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(5) / (((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v126_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v126_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v127_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(21) / (((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v127_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v127_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v128_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(63) / (((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v128_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v128_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v129_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(126) / (((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v129_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v129_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v130_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).diff(252) / (((inventory / revenue.replace(0, np.nan)).diff().gt(0)).rolling(21).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v130_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v130_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v131_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(5) / ((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v131_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v131_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v132_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(21) / ((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v132_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v132_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v133_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(63) / ((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v133_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v133_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v134_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(126) / ((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v134_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v134_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v135_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).diff(252) / ((inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.75) - (inventory / revenue.replace(0, np.nan)).rolling(63).quantile(0.25)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v135_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v135_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v136_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(5) / (((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v136_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v136_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v137_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(21) / (((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v137_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v137_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v138_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(63) / (((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v138_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v138_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v139_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(126) / (((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v139_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v139_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v140_signal(inventory, revenue):
    res = ((((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).diff(252) / (((inventory / revenue.replace(0, np.nan)) - (inventory / revenue.replace(0, np.nan)).shift(126))/(inventory / revenue.replace(0, np.nan)).abs().replace(0, np.nan).shift(126)).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v140_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v140_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v141_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(5) / ((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v141_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v141_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v142_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(21) / ((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v142_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v142_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v143_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(63) / ((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v143_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v143_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v144_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(126) / ((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v144_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v144_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v145_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).diff(252) / ((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v145_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v145_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v146_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(5) / ((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v146_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v146_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v147_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(21) / ((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v147_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v147_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v148_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(63) / ((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v148_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v148_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v149_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(126) / ((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v149_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v149_signal

def f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v150_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).diff(252) / ((inventory / revenue.replace(0, np.nan)).ewm(span=504).std()).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v150_signal'] = f45inv_f45_inventory_to_revenue_cycles_2ndderiv_v150_signal

