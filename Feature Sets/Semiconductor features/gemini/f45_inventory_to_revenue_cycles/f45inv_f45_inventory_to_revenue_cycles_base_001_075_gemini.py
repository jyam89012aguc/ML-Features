import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f45inv_f45_inventory_to_revenue_cycles_base_v001_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v001_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v001_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v002_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v002_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v002_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v003_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v003_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v003_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v004_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v004_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v004_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v005_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v005_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v005_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v006_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v006_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v006_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v007_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v007_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v007_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v008_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v008_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v008_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v009_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v009_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v009_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v010_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v010_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v010_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v011_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v011_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v011_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v012_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v012_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v012_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v013_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v013_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v013_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v014_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v014_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v014_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v015_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v015_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v015_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v016_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v016_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v016_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v017_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v017_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v017_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v018_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v018_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v018_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v019_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v019_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v019_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v020_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v020_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v020_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v021_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).mean())/(inventory / revenue.replace(0, np.nan)).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v021_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v021_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v022_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(63).mean())/(inventory / revenue.replace(0, np.nan)).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v022_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v022_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v023_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(126).mean())/(inventory / revenue.replace(0, np.nan)).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v023_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v023_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v024_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(252).mean())/(inventory / revenue.replace(0, np.nan)).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v024_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v024_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v025_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).mean())/(inventory / revenue.replace(0, np.nan)).rolling(504).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v025_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v025_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v026_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).median()).abs().rolling(21).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v026_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v026_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v027_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(63).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(63).median()).abs().rolling(63).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v027_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v027_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v028_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(126).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(126).median()).abs().rolling(126).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v028_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v028_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v029_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(252).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(252).median()).abs().rolling(252).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v029_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v029_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v030_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).median())/(((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).median()).abs().rolling(504).median()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v030_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v030_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v031_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(21).mean()).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v031_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v031_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v032_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(63).mean()).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v032_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v032_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v033_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(126).mean()).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v033_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v033_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v034_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(252).mean()).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v034_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v034_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v035_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).gt((inventory / revenue.replace(0, np.nan)).rolling(504).mean()).rolling(504).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v035_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v035_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v036_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v036_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v036_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v037_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v037_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v037_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v038_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v038_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v038_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v039_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v039_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v039_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v040_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v040_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v040_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v041_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v041_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v041_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v042_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v042_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v042_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v043_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v043_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v043_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v044_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v044_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v044_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v045_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v045_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v045_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v046_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v046_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v046_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v047_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).rolling(63).max()-(inventory / revenue.replace(0, np.nan)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v047_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v047_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v048_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).rolling(126).max()-(inventory / revenue.replace(0, np.nan)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v048_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v048_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v049_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).rolling(252).max()-(inventory / revenue.replace(0, np.nan)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v049_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v049_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v050_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v050_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v050_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v051_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(21).min())/((inventory / revenue.replace(0, np.nan)).rolling(21).max()-(inventory / revenue.replace(0, np.nan)).rolling(21).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v051_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v051_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v052_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(63).min())/((inventory / revenue.replace(0, np.nan)).rolling(63).max()-(inventory / revenue.replace(0, np.nan)).rolling(63).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v052_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v052_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v053_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(126).min())/((inventory / revenue.replace(0, np.nan)).rolling(126).max()-(inventory / revenue.replace(0, np.nan)).rolling(126).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v053_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v053_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v054_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(252).min())/((inventory / revenue.replace(0, np.nan)).rolling(252).max()-(inventory / revenue.replace(0, np.nan)).rolling(252).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v054_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v054_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v055_signal(inventory, revenue):
    res = (((inventory / revenue.replace(0, np.nan))-(inventory / revenue.replace(0, np.nan)).rolling(504).min())/((inventory / revenue.replace(0, np.nan)).rolling(504).max()-(inventory / revenue.replace(0, np.nan)).rolling(504).min()))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v055_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v055_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v056_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(21).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v056_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v056_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v057_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v057_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v057_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v058_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v058_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v058_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v059_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(252).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v059_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v059_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v060_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(504).max() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v060_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v060_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v061_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(21).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v061_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v061_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v062_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(63).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v062_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v062_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v063_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(126).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v063_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v063_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v064_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(252).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v064_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v064_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v065_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan))/(inventory / revenue.replace(0, np.nan)).rolling(504).min() - 1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v065_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v065_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v066_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).ewm(span=21).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=21*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v066_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v066_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v067_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).ewm(span=63).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=63*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v067_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v067_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v068_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).ewm(span=126).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=126*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v068_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v068_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v069_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).ewm(span=252).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=252*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v069_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v069_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v070_signal(inventory, revenue):
    res = ((inventory / revenue.replace(0, np.nan)).ewm(span=504).mean() - (inventory / revenue.replace(0, np.nan)).ewm(span=504*3).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v070_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v070_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v071_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v071_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v071_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v072_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v072_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v072_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v073_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v073_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v073_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v074_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v074_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v074_signal

def f45inv_f45_inventory_to_revenue_cycles_base_v075_signal(inventory, revenue):
    res = (inventory / revenue.replace(0, np.nan)).pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f45inv_f45_inventory_to_revenue_cycles_base_v075_signal'] = f45inv_f45_inventory_to_revenue_cycles_base_v075_signal

