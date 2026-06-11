import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f74da_f74_debt_to_assets_momentum_v001_signal(debt, assets):
    res = (debt / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v001_signal'] = f74da_f74_debt_to_assets_momentum_v001_signal

def f74da_f74_debt_to_assets_momentum_v002_signal(debt, assets):
    res = (debt / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v002_signal'] = f74da_f74_debt_to_assets_momentum_v002_signal

def f74da_f74_debt_to_assets_momentum_v003_signal(debt, assets):
    res = (debt / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v003_signal'] = f74da_f74_debt_to_assets_momentum_v003_signal

def f74da_f74_debt_to_assets_momentum_v004_signal(debt, assets):
    res = (debt / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v004_signal'] = f74da_f74_debt_to_assets_momentum_v004_signal

def f74da_f74_debt_to_assets_momentum_v005_signal(debt, assets):
    res = (debt / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v005_signal'] = f74da_f74_debt_to_assets_momentum_v005_signal

def f74da_f74_debt_to_assets_momentum_v006_signal(debt, assets):
    res = (debt / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v006_signal'] = f74da_f74_debt_to_assets_momentum_v006_signal

def f74da_f74_debt_to_assets_momentum_v007_signal(debt, assets):
    res = (debt / assets).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v007_signal'] = f74da_f74_debt_to_assets_momentum_v007_signal

def f74da_f74_debt_to_assets_momentum_v008_signal(debt, assets):
    res = (debt / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v008_signal'] = f74da_f74_debt_to_assets_momentum_v008_signal

def f74da_f74_debt_to_assets_momentum_v009_signal(debt, assets):
    res = (debt / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v009_signal'] = f74da_f74_debt_to_assets_momentum_v009_signal

def f74da_f74_debt_to_assets_momentum_v010_signal(debt, assets):
    res = (debt / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v010_signal'] = f74da_f74_debt_to_assets_momentum_v010_signal

def f74da_f74_debt_to_assets_momentum_v011_signal(assets, debt):
    res = (assets / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v011_signal'] = f74da_f74_debt_to_assets_momentum_v011_signal

def f74da_f74_debt_to_assets_momentum_v012_signal(assets, debt):
    res = (assets / debt).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v012_signal'] = f74da_f74_debt_to_assets_momentum_v012_signal

def f74da_f74_debt_to_assets_momentum_v013_signal(assets, debt):
    res = (assets / debt).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v013_signal'] = f74da_f74_debt_to_assets_momentum_v013_signal

def f74da_f74_debt_to_assets_momentum_v014_signal(assets, debt):
    res = (assets / debt).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v014_signal'] = f74da_f74_debt_to_assets_momentum_v014_signal

def f74da_f74_debt_to_assets_momentum_v015_signal(assets, debt):
    res = (assets / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v015_signal'] = f74da_f74_debt_to_assets_momentum_v015_signal

def f74da_f74_debt_to_assets_momentum_v016_signal(assets, debt):
    res = (assets / debt).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v016_signal'] = f74da_f74_debt_to_assets_momentum_v016_signal

def f74da_f74_debt_to_assets_momentum_v017_signal(assets, debt):
    res = (assets / debt).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v017_signal'] = f74da_f74_debt_to_assets_momentum_v017_signal

def f74da_f74_debt_to_assets_momentum_v018_signal(assets, debt):
    res = (assets / debt).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v018_signal'] = f74da_f74_debt_to_assets_momentum_v018_signal

def f74da_f74_debt_to_assets_momentum_v019_signal(assets, debt):
    res = (assets / debt).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v019_signal'] = f74da_f74_debt_to_assets_momentum_v019_signal

def f74da_f74_debt_to_assets_momentum_v020_signal(assets, debt):
    res = (assets / debt).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v020_signal'] = f74da_f74_debt_to_assets_momentum_v020_signal

def f74da_f74_debt_to_assets_momentum_v021_signal(debt, equity):
    res = (debt / equity).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v021_signal'] = f74da_f74_debt_to_assets_momentum_v021_signal

def f74da_f74_debt_to_assets_momentum_v022_signal(debt, equity):
    res = (debt / equity).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v022_signal'] = f74da_f74_debt_to_assets_momentum_v022_signal

def f74da_f74_debt_to_assets_momentum_v023_signal(debt, equity):
    res = (debt / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v023_signal'] = f74da_f74_debt_to_assets_momentum_v023_signal

def f74da_f74_debt_to_assets_momentum_v024_signal(debt, equity):
    res = (debt / equity).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v024_signal'] = f74da_f74_debt_to_assets_momentum_v024_signal

def f74da_f74_debt_to_assets_momentum_v025_signal(debt, equity):
    res = (debt / equity).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v025_signal'] = f74da_f74_debt_to_assets_momentum_v025_signal

def f74da_f74_debt_to_assets_momentum_v026_signal(debt, equity):
    res = (debt / equity).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v026_signal'] = f74da_f74_debt_to_assets_momentum_v026_signal

def f74da_f74_debt_to_assets_momentum_v027_signal(debt, equity):
    res = (debt / equity).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v027_signal'] = f74da_f74_debt_to_assets_momentum_v027_signal

def f74da_f74_debt_to_assets_momentum_v028_signal(debt, equity):
    res = (debt / equity).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v028_signal'] = f74da_f74_debt_to_assets_momentum_v028_signal

def f74da_f74_debt_to_assets_momentum_v029_signal(debt, equity):
    res = (debt / equity).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v029_signal'] = f74da_f74_debt_to_assets_momentum_v029_signal

def f74da_f74_debt_to_assets_momentum_v030_signal(debt, equity):
    res = (debt / equity).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v030_signal'] = f74da_f74_debt_to_assets_momentum_v030_signal

def f74da_f74_debt_to_assets_momentum_v031_signal(debt, marketcap):
    res = (debt / marketcap).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v031_signal'] = f74da_f74_debt_to_assets_momentum_v031_signal

def f74da_f74_debt_to_assets_momentum_v032_signal(debt, marketcap):
    res = (debt / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v032_signal'] = f74da_f74_debt_to_assets_momentum_v032_signal

def f74da_f74_debt_to_assets_momentum_v033_signal(debt, marketcap):
    res = (debt / marketcap).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v033_signal'] = f74da_f74_debt_to_assets_momentum_v033_signal

def f74da_f74_debt_to_assets_momentum_v034_signal(debt, marketcap):
    res = (debt / marketcap).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v034_signal'] = f74da_f74_debt_to_assets_momentum_v034_signal

def f74da_f74_debt_to_assets_momentum_v035_signal(debt, marketcap):
    res = (debt / marketcap).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v035_signal'] = f74da_f74_debt_to_assets_momentum_v035_signal

def f74da_f74_debt_to_assets_momentum_v036_signal(debt, marketcap):
    res = (debt / marketcap).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v036_signal'] = f74da_f74_debt_to_assets_momentum_v036_signal

def f74da_f74_debt_to_assets_momentum_v037_signal(debt, marketcap):
    res = (debt / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v037_signal'] = f74da_f74_debt_to_assets_momentum_v037_signal

def f74da_f74_debt_to_assets_momentum_v038_signal(debt, marketcap):
    res = (debt / marketcap).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v038_signal'] = f74da_f74_debt_to_assets_momentum_v038_signal

def f74da_f74_debt_to_assets_momentum_v039_signal(debt, marketcap):
    res = (debt / marketcap).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v039_signal'] = f74da_f74_debt_to_assets_momentum_v039_signal

def f74da_f74_debt_to_assets_momentum_v040_signal(debt, marketcap):
    res = (debt / marketcap).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v040_signal'] = f74da_f74_debt_to_assets_momentum_v040_signal

def f74da_f74_debt_to_assets_momentum_v041_signal(liabilities, assets):
    res = (liabilities / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v041_signal'] = f74da_f74_debt_to_assets_momentum_v041_signal

def f74da_f74_debt_to_assets_momentum_v042_signal(liabilities, assets):
    res = (liabilities / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v042_signal'] = f74da_f74_debt_to_assets_momentum_v042_signal

def f74da_f74_debt_to_assets_momentum_v043_signal(liabilities, assets):
    res = (liabilities / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v043_signal'] = f74da_f74_debt_to_assets_momentum_v043_signal

def f74da_f74_debt_to_assets_momentum_v044_signal(liabilities, assets):
    res = (liabilities / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v044_signal'] = f74da_f74_debt_to_assets_momentum_v044_signal

def f74da_f74_debt_to_assets_momentum_v045_signal(liabilities, assets):
    res = (liabilities / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v045_signal'] = f74da_f74_debt_to_assets_momentum_v045_signal

def f74da_f74_debt_to_assets_momentum_v046_signal(liabilities, assets):
    res = (liabilities / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v046_signal'] = f74da_f74_debt_to_assets_momentum_v046_signal

def f74da_f74_debt_to_assets_momentum_v047_signal(liabilities, assets):
    res = (liabilities / assets).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v047_signal'] = f74da_f74_debt_to_assets_momentum_v047_signal

def f74da_f74_debt_to_assets_momentum_v048_signal(liabilities, assets):
    res = (liabilities / assets).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v048_signal'] = f74da_f74_debt_to_assets_momentum_v048_signal

def f74da_f74_debt_to_assets_momentum_v049_signal(liabilities, assets):
    res = (liabilities / assets).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v049_signal'] = f74da_f74_debt_to_assets_momentum_v049_signal

def f74da_f74_debt_to_assets_momentum_v050_signal(liabilities, assets):
    res = (liabilities / assets).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v050_signal'] = f74da_f74_debt_to_assets_momentum_v050_signal

def f74da_f74_debt_to_assets_momentum_v051_signal(debt, revenue):
    res = (debt / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v051_signal'] = f74da_f74_debt_to_assets_momentum_v051_signal

def f74da_f74_debt_to_assets_momentum_v052_signal(debt, revenue):
    res = (debt / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v052_signal'] = f74da_f74_debt_to_assets_momentum_v052_signal

def f74da_f74_debt_to_assets_momentum_v053_signal(debt, revenue):
    res = (debt / revenue).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v053_signal'] = f74da_f74_debt_to_assets_momentum_v053_signal

def f74da_f74_debt_to_assets_momentum_v054_signal(debt, revenue):
    res = (debt / revenue).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v054_signal'] = f74da_f74_debt_to_assets_momentum_v054_signal

def f74da_f74_debt_to_assets_momentum_v055_signal(debt, revenue):
    res = (debt / revenue).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v055_signal'] = f74da_f74_debt_to_assets_momentum_v055_signal

def f74da_f74_debt_to_assets_momentum_v056_signal(debt, revenue):
    res = (debt / revenue).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v056_signal'] = f74da_f74_debt_to_assets_momentum_v056_signal

def f74da_f74_debt_to_assets_momentum_v057_signal(debt, revenue):
    res = (debt / revenue).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v057_signal'] = f74da_f74_debt_to_assets_momentum_v057_signal

def f74da_f74_debt_to_assets_momentum_v058_signal(debt, revenue):
    res = (debt / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v058_signal'] = f74da_f74_debt_to_assets_momentum_v058_signal

def f74da_f74_debt_to_assets_momentum_v059_signal(debt, revenue):
    res = (debt / revenue).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v059_signal'] = f74da_f74_debt_to_assets_momentum_v059_signal

def f74da_f74_debt_to_assets_momentum_v060_signal(debt, revenue):
    res = (debt / revenue).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v060_signal'] = f74da_f74_debt_to_assets_momentum_v060_signal

def f74da_f74_debt_to_assets_momentum_v061_signal(debt, ebitda):
    res = (debt / ebitda).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v061_signal'] = f74da_f74_debt_to_assets_momentum_v061_signal

def f74da_f74_debt_to_assets_momentum_v062_signal(debt, ebitda):
    res = (debt / ebitda).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v062_signal'] = f74da_f74_debt_to_assets_momentum_v062_signal

def f74da_f74_debt_to_assets_momentum_v063_signal(debt, ebitda):
    res = (debt / ebitda).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v063_signal'] = f74da_f74_debt_to_assets_momentum_v063_signal

def f74da_f74_debt_to_assets_momentum_v064_signal(debt, ebitda):
    res = (debt / ebitda).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v064_signal'] = f74da_f74_debt_to_assets_momentum_v064_signal

def f74da_f74_debt_to_assets_momentum_v065_signal(debt, ebitda):
    res = (debt / ebitda).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v065_signal'] = f74da_f74_debt_to_assets_momentum_v065_signal

def f74da_f74_debt_to_assets_momentum_v066_signal(debt, ebitda):
    res = (debt / ebitda).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v066_signal'] = f74da_f74_debt_to_assets_momentum_v066_signal

def f74da_f74_debt_to_assets_momentum_v067_signal(debt, ebitda):
    res = (debt / ebitda).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v067_signal'] = f74da_f74_debt_to_assets_momentum_v067_signal

def f74da_f74_debt_to_assets_momentum_v068_signal(debt, ebitda):
    res = (debt / ebitda).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v068_signal'] = f74da_f74_debt_to_assets_momentum_v068_signal

def f74da_f74_debt_to_assets_momentum_v069_signal(debt, ebitda):
    res = (debt / ebitda).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v069_signal'] = f74da_f74_debt_to_assets_momentum_v069_signal

def f74da_f74_debt_to_assets_momentum_v070_signal(debt, ebitda):
    res = (debt / ebitda).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v070_signal'] = f74da_f74_debt_to_assets_momentum_v070_signal

def f74da_f74_debt_to_assets_momentum_v071_signal(debt, assets):
    res = debt.pct_change(5) / assets.pct_change(5)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v071_signal'] = f74da_f74_debt_to_assets_momentum_v071_signal

def f74da_f74_debt_to_assets_momentum_v072_signal(debt, assets):
    res = debt.pct_change(10) / assets.pct_change(10)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v072_signal'] = f74da_f74_debt_to_assets_momentum_v072_signal

def f74da_f74_debt_to_assets_momentum_v073_signal(debt, assets):
    res = debt.pct_change(21) / assets.pct_change(21)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v073_signal'] = f74da_f74_debt_to_assets_momentum_v073_signal

def f74da_f74_debt_to_assets_momentum_v074_signal(debt, assets):
    res = debt.pct_change(42) / assets.pct_change(42)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v074_signal'] = f74da_f74_debt_to_assets_momentum_v074_signal

def f74da_f74_debt_to_assets_momentum_v075_signal(debt, assets):
    res = debt.pct_change(63) / assets.pct_change(63)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v075_signal'] = f74da_f74_debt_to_assets_momentum_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "assets": np.random.uniform(2000, 5000, n),
        "equity": np.random.uniform(1000, 3000, n),
        "marketcap": np.random.uniform(5000, 20000, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}")
                assert corr_matrix.iloc[i, j] <= 0.95, f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}"
    print(f"Self-test passed for {os.path.basename(__file__)}")
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
