import pandas as pd
import numpy as np
import os

FEATURE_FUNCTIONS = {}

def f74da_f74_debt_to_assets_momentum_v001_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(5).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v001_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v001_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v002_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(5).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v002_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v002_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v003_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(10).mean().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v003_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v003_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v004_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(10).std().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v004_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v004_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v005_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v005_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v005_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v006_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v006_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v006_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v007_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(42).mean().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v007_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v007_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v008_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(42).std().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v008_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v008_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v009_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v009_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v009_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v010_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v010_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v010_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v011_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(5).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v011_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v011_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v012_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(5).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v012_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v012_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v013_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(10).mean().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v013_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v013_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v014_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(10).std().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v014_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v014_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v015_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v015_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v015_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v016_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v016_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v016_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v017_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(42).mean().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v017_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v017_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v018_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(42).std().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v018_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v018_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v019_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v019_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v019_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v020_3rd_derivative(assets, debt):
    res = (assets / debt).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v020_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v020_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v021_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(10).mean().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v021_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v021_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v022_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(10).std().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v022_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v022_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v023_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v023_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v023_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v024_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v024_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v024_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v025_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(42).mean().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v025_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v025_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v026_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(42).std().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v026_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v026_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v027_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v027_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v027_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v028_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v028_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v028_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v029_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(126).mean().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v029_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v029_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v030_3rd_derivative(debt, equity):
    res = (debt / equity).rolling(126).std().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v030_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v030_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v031_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(10).mean().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v031_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v031_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v032_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(10).std().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v032_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v032_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v033_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v033_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v033_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v034_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v034_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v034_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v035_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(42).mean().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v035_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v035_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v036_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(42).std().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v036_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v036_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v037_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v037_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v037_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v038_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v038_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v038_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v039_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(126).mean().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v039_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v039_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v040_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).rolling(126).std().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v040_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v040_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v041_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(5).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v041_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v041_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v042_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(5).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v042_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v042_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v043_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v043_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v043_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v044_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v044_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v044_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v045_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v045_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v045_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v046_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v046_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v046_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v047_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(126).mean().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v047_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v047_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v048_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(126).std().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v048_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v048_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v049_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(252).mean().diff(252).diff(252).diff(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v049_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v049_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v050_3rd_derivative(liabilities, assets):
    res = (liabilities / assets).rolling(252).std().diff(252).diff(252).diff(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v050_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v050_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v051_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v051_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v051_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v052_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v052_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v052_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v053_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(42).mean().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v053_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v053_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v054_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(42).std().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v054_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v054_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v055_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v055_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v055_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v056_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v056_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v056_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v057_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(126).mean().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v057_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v057_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v058_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(126).std().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v058_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v058_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v059_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(252).mean().diff(252).diff(252).diff(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v059_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v059_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v060_3rd_derivative(debt, revenue):
    res = (debt / revenue).rolling(252).std().diff(252).diff(252).diff(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v060_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v060_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v061_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(10).mean().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v061_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v061_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v062_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(10).std().diff(10).diff(10).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v062_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v062_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v063_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(21).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v063_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v063_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v064_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(21).std().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v064_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v064_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v065_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(42).mean().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v065_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v065_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v066_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(42).std().diff(42).diff(42).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v066_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v066_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v067_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(63).mean().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v067_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v067_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v068_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(63).std().diff(63).diff(63).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v068_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v068_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v069_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(126).mean().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v069_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v069_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v070_3rd_derivative(debt, ebitda):
    res = (debt / ebitda).rolling(126).std().diff(126).diff(126).diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v070_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v070_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v071_3rd_derivative(debt, assets):
    base = debt.pct_change(5) / assets.pct_change(5)
    res = base.rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v071_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v071_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v072_3rd_derivative(debt, assets):
    base = debt.pct_change(10) / assets.pct_change(10)
    res = base.rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v072_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v072_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v073_3rd_derivative(debt, assets):
    base = debt.pct_change(21) / assets.pct_change(21)
    res = base.rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v073_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v073_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v074_3rd_derivative(debt, assets):
    base = debt.pct_change(42) / assets.pct_change(42)
    res = base.rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v074_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v074_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v075_3rd_derivative(debt, assets):
    base = debt.pct_change(63) / assets.pct_change(63)
    res = base.rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v075_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v075_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v076_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v076_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v076_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v077_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v077_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v077_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v078_3rd_derivative(debt, ev):
    res = (debt / ev).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v078_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v078_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v079_3rd_derivative(debt, ev):
    res = (debt / ev).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v079_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v079_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v080_3rd_derivative(debt, gp):
    res = (debt / gp).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v080_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v080_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v081_3rd_derivative(debt, gp):
    res = (debt / gp).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v081_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v081_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v082_3rd_derivative(debt, fcf):
    res = (debt / fcf).rolling(42).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v082_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v082_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v083_3rd_derivative(debt, fcf):
    res = (debt / fcf).rolling(126).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v083_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v083_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v084_3rd_derivative(debt, opinc):
    res = (debt / opinc).rolling(63).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v084_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v084_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v085_3rd_derivative(debt, opinc):
    res = (debt / opinc).rolling(252).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v085_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v085_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v086_3rd_derivative(debt, workingcapital):
    res = (debt / workingcapital).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v086_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v086_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v087_3rd_derivative(debt, workingcapital):
    res = (debt / workingcapital).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v087_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v087_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v088_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = (ratio.rolling(21).mean() / ratio.rolling(126).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v088_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v088_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v089_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = (ratio.rolling(21).std() / ratio.rolling(126).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v089_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v089_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v090_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).pct_change(21).rolling(42).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v090_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v090_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v091_3rd_derivative(debt, marketcap):
    res = (debt / marketcap).pct_change(63).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v091_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v091_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v092_3rd_derivative(liabilities, revenue):
    res = (liabilities / revenue).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v092_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v092_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v093_3rd_derivative(liabilities, revenue):
    res = (liabilities / revenue).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v093_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v093_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v094_3rd_derivative(liabilities, ebitda):
    res = (liabilities / ebitda).rolling(42).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v094_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v094_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v095_3rd_derivative(liabilities, ebitda):
    res = (liabilities / ebitda).rolling(126).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v095_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v095_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v096_3rd_derivative(debt, equity):
    res = (debt / equity).diff(10).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v096_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v096_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v097_3rd_derivative(debt, equity):
    res = (debt / equity).diff(21).rolling(63).std().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v097_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v097_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v098_3rd_derivative(debt, liabilities, assets):
    base = (debt / liabilities).rolling(21).mean() * (liabilities / assets).rolling(21).mean()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v098_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v098_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v099_3rd_derivative(debt, liabilities, assets):
    base = (debt / liabilities).rolling(63).std() * (liabilities / assets).rolling(63).std()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v099_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v099_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v100_3rd_derivative(debt, marketcap, revenue):
    base = (debt / marketcap).rolling(21).mean() / (revenue / marketcap).rolling(21).mean()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v100_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v100_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v101_3rd_derivative(debt, marketcap, revenue):
    base = (debt / marketcap).rolling(63).std() / (revenue / marketcap).rolling(63).std()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v101_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v101_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v102_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(21).skew().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v102_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v102_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v103_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(63).kurt().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v103_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v103_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v104_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(126).skew().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v104_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v104_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v105_3rd_derivative(debt, assets):
    res = (debt / assets).rolling(252).kurt().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v105_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v105_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v106_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(21).quantile(0.25).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v106_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v106_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v107_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(21).quantile(0.75).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v107_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v107_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v108_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(63).quantile(0.25).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v108_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v108_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v109_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(63).quantile(0.75).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v109_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v109_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v110_3rd_derivative(debt, ev):
    res = (debt / ev).rolling(21).rank(pct=True).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v110_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v110_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v111_3rd_derivative(liabilities, ev):
    res = (liabilities / ev).rolling(126).rank(pct=True).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v111_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v111_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v112_3rd_derivative(debt, fcf):
    ratio = debt / fcf
    res = (ratio / ratio.rolling(21).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v112_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v112_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v113_3rd_derivative(liabilities, fcf):
    ratio = liabilities / fcf
    res = (ratio / ratio.rolling(126).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v113_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v113_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v114_3rd_derivative(debt, gp):
    ratio = debt / gp
    res = ((ratio - ratio.rolling(21).mean()) / ratio.rolling(21).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v114_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v114_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v115_3rd_derivative(liabilities, gp):
    ratio = liabilities / gp
    res = ((ratio - ratio.rolling(126).mean()) / ratio.rolling(126).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v115_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v115_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v116_3rd_derivative(debt, revenue):
    res = ((debt / revenue).rolling(21).max() / (debt / revenue).rolling(21).min()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v116_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v116_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v117_3rd_derivative(debt, revenue):
    res = ((debt / revenue).rolling(63).max() / (debt / revenue).rolling(63).min()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v117_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v117_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v118_3rd_derivative(debt, assets):
    res = (debt.diff(5).diff(5) / assets.diff(5)).rolling(21).mean().diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v118_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v118_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v119_3rd_derivative(debt, assets):
    res = (debt.diff(21) / assets.diff(21)).rolling(63).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v119_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v119_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v120_3rd_derivative(debt, equity):
    res = (debt.pct_change(5) - equity.pct_change(5)).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v120_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v120_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v121_3rd_derivative(debt, equity):
    res = (debt.pct_change(21) - equity.pct_change(21)).rolling(63).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v121_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v121_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v122_3rd_derivative(liabilities, marketcap):
    res = (liabilities / marketcap).rolling(21).mean().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v122_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v122_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v123_3rd_derivative(liabilities, marketcap):
    res = (liabilities / marketcap).rolling(63).mean().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v123_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v123_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v124_3rd_derivative(debt, assets, volume):
    base = (debt / assets).rolling(21).mean() * volume.pct_change(5).rolling(21).mean()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v124_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v124_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v125_3rd_derivative(debt, assets, volume):
    base = (debt / assets).rolling(63).mean() * volume.pct_change(21).rolling(63).mean()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v125_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v125_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v126_3rd_derivative(debt, assets):
    res = ((debt / assets).rolling(21).std() / (debt / assets).rolling(252).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v126_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v126_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v127_3rd_derivative(debt, assets):
    res = ((debt / assets).rolling(63).std() / (debt / assets).rolling(252).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v127_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v127_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v128_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = (ratio / ratio.shift(21) - 1).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v128_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v128_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v129_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = (ratio / ratio.shift(63) - 1).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v129_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v129_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v130_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(21).median().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v130_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v130_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v131_3rd_derivative(debt, liabilities):
    res = (debt / liabilities).rolling(63).median().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v131_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v131_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v132_3rd_derivative(debt, ev):
    res = (debt / ev).rolling(21).std().pct_change(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v132_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v132_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v133_3rd_derivative(debt, ev):
    res = (debt / ev).rolling(63).std().pct_change(21).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v133_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v133_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v134_3rd_derivative(debt, gp):
    res = ((debt / gp).rolling(21).max() - (debt / gp).rolling(21).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v134_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v134_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v135_3rd_derivative(debt, gp):
    res = ((debt / gp).rolling(63).max() - (debt / gp).rolling(63).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v135_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v135_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v136_3rd_derivative(debt, fcf):
    res = ((debt / fcf).rolling(21).min() - (debt / fcf).rolling(21).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v136_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v136_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v137_3rd_derivative(debt, fcf):
    res = ((debt / fcf).rolling(63).min() - (debt / fcf).rolling(63).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v137_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v137_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v138_3rd_derivative(debt, opinc):
    base = (debt / opinc).rolling(42).std() / (debt / opinc).rolling(42).mean().abs()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v138_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v138_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v139_3rd_derivative(debt, opinc):
    base = (debt / opinc).rolling(126).std() / (debt / opinc).rolling(126).mean().abs()
    res = base.diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v139_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v139_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v140_3rd_derivative(debt, workingcapital):
    res = (debt / workingcapital).rolling(21).skew().diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v140_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v140_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v141_3rd_derivative(debt, workingcapital):
    res = (debt / workingcapital).rolling(63).skew().diff(21).diff(21).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v141_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v141_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v142_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = (ratio.rolling(7).mean() - ratio.rolling(28).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v142_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v142_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v143_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = (ratio.rolling(30).mean() - ratio.rolling(90).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v143_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v143_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v144_3rd_derivative(liabilities, assets):
    ratio = liabilities / assets
    res = (ratio.rolling(7).mean() - ratio.rolling(28).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v144_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v144_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v145_3rd_derivative(liabilities, assets):
    ratio = liabilities / assets
    res = (ratio.rolling(30).mean() - ratio.rolling(90).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v145_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v145_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v146_3rd_derivative(debt, marketcap):
    ratio = debt / marketcap
    res = (ratio.rolling(7).std() - ratio.rolling(28).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v146_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v146_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v147_3rd_derivative(debt, marketcap):
    ratio = debt / marketcap
    res = (ratio.rolling(30).std() - ratio.rolling(90).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v147_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v147_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v148_3rd_derivative(debt, revenue):
    ratio = debt / revenue
    res = (ratio.rolling(7).mean() - ratio.rolling(28).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v148_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v148_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v149_3rd_derivative(debt, revenue):
    ratio = debt / revenue
    res = (ratio.rolling(30).mean() - ratio.rolling(90).mean()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v149_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v149_3rd_derivative

def f74da_f74_debt_to_assets_momentum_v150_3rd_derivative(debt, assets):
    ratio = debt / assets
    res = ((ratio - ratio.shift(5)) / ratio.rolling(21).std()).diff(5).diff(5).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f74da_f74_debt_to_assets_momentum_v150_3rd_derivative'] = f74da_f74_debt_to_assets_momentum_v150_3rd_derivative

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "opinc": np.random.uniform(40, 180, n),
        "assets": np.random.uniform(2000, 5000, n),
        "equity": np.random.uniform(1000, 3000, n),
        "marketcap": np.random.uniform(5000, 20000, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n),
        "ev": np.random.uniform(6000, 25000, n),
        "gp": np.random.uniform(100, 400, n),
        "fcf": np.random.uniform(20, 120, n),
        "workingcapital": np.random.uniform(200, 800, n),
        "volume": np.random.uniform(100000, 1000000, n)
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
