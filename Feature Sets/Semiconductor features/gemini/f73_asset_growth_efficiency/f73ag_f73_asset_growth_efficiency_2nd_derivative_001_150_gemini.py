import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f73ag_f73_asset_growth_efficiency_v001_2nd_signal(assets, revenue):
    res = (assets / revenue).rolling(5).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v001_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v001_2nd_signal

def f73ag_f73_asset_growth_efficiency_v002_2nd_signal(assets, revenue):
    res = (assets / revenue).rolling(10).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v002_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v002_2nd_signal

def f73ag_f73_asset_growth_efficiency_v003_2nd_signal(assets, revenue):
    res = (assets / revenue).rolling(21).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v003_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v003_2nd_signal

def f73ag_f73_asset_growth_efficiency_v004_2nd_signal(assets, revenue):
    res = (assets / revenue).rolling(63).kurt().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v004_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v004_2nd_signal

def f73ag_f73_asset_growth_efficiency_v005_2nd_signal(revenue, assets):
    res = (revenue / assets).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v005_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v005_2nd_signal

def f73ag_f73_asset_growth_efficiency_v006_2nd_signal(revenue, assets):
    res = (revenue / assets).rolling(21).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v006_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v006_2nd_signal

def f73ag_f73_asset_growth_efficiency_v007_2nd_signal(revenue, assets):
    res = (revenue / assets).rolling(63).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v007_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v007_2nd_signal

def f73ag_f73_asset_growth_efficiency_v008_2nd_signal(assets, ebitda):
    res = (assets / ebitda).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v008_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v008_2nd_signal

def f73ag_f73_asset_growth_efficiency_v009_2nd_signal(assets, ebitda):
    res = (assets / ebitda).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v009_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v009_2nd_signal

def f73ag_f73_asset_growth_efficiency_v010_2nd_signal(assets, ebitda):
    res = (assets / ebitda).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v010_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v010_2nd_signal

def f73ag_f73_asset_growth_efficiency_v011_2nd_signal(ebitda, assets):
    res = (ebitda / assets).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v011_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v011_2nd_signal

def f73ag_f73_asset_growth_efficiency_v012_2nd_signal(ebitda, assets):
    res = (ebitda / assets).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v012_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v012_2nd_signal

def f73ag_f73_asset_growth_efficiency_v013_2nd_signal(ebitda, assets):
    res = (ebitda / assets).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v013_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v013_2nd_signal

def f73ag_f73_asset_growth_efficiency_v014_2nd_signal(assets, netinc):
    res = (assets / netinc).rolling(42).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v014_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v014_2nd_signal

def f73ag_f73_asset_growth_efficiency_v015_2nd_signal(assets, netinc):
    res = (assets / netinc).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v015_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v015_2nd_signal

def f73ag_f73_asset_growth_efficiency_v016_2nd_signal(netinc, assets):
    res = (netinc / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v016_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v016_2nd_signal

def f73ag_f73_asset_growth_efficiency_v017_2nd_signal(netinc, assets):
    res = (netinc / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v017_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v017_2nd_signal

def f73ag_f73_asset_growth_efficiency_v018_2nd_signal(assets, equity):
    res = (assets / equity).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v018_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v018_2nd_signal

def f73ag_f73_asset_growth_efficiency_v019_2nd_signal(assets, equity):
    res = (assets / equity).rolling(90).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v019_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v019_2nd_signal

def f73ag_f73_asset_growth_efficiency_v020_2nd_signal(assets, equity):
    res = (assets / equity).rolling(252).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v020_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v020_2nd_signal

def f73ag_f73_asset_growth_efficiency_v021_2nd_signal(assets, marketcap):
    res = (assets / marketcap).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v021_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v021_2nd_signal

def f73ag_f73_asset_growth_efficiency_v022_2nd_signal(assets, marketcap):
    res = (assets / marketcap).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v022_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v022_2nd_signal

def f73ag_f73_asset_growth_efficiency_v023_2nd_signal(assets, marketcap):
    res = (assets / marketcap).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v023_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v023_2nd_signal

def f73ag_f73_asset_growth_efficiency_v024_2nd_signal(marketcap, assets):
    res = (marketcap / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v024_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v024_2nd_signal

def f73ag_f73_asset_growth_efficiency_v025_2nd_signal(marketcap, assets):
    res = (marketcap / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v025_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v025_2nd_signal

def f73ag_f73_asset_growth_efficiency_v026_2nd_signal(assets, ev):
    res = (assets / ev).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v026_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v026_2nd_signal

def f73ag_f73_asset_growth_efficiency_v027_2nd_signal(assets, ev):
    res = (assets / ev).rolling(90).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v027_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v027_2nd_signal

def f73ag_f73_asset_growth_efficiency_v028_2nd_signal(assets, liabilities):
    res = (assets / liabilities).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v028_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v028_2nd_signal

def f73ag_f73_asset_growth_efficiency_v029_2nd_signal(assets, liabilities):
    res = (assets / liabilities).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v029_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v029_2nd_signal

def f73ag_f73_asset_growth_efficiency_v030_2nd_signal(assets, liabilities):
    res = (assets / liabilities).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v030_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v030_2nd_signal

def f73ag_f73_asset_growth_efficiency_v031_2nd_signal(liabilities, assets):
    res = (liabilities / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v031_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v031_2nd_signal

def f73ag_f73_asset_growth_efficiency_v032_2nd_signal(liabilities, assets):
    res = (liabilities / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v032_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v032_2nd_signal

def f73ag_f73_asset_growth_efficiency_v033_2nd_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v033_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v033_2nd_signal

def f73ag_f73_asset_growth_efficiency_v034_2nd_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v034_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v034_2nd_signal

def f73ag_f73_asset_growth_efficiency_v035_2nd_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v035_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v035_2nd_signal

def f73ag_f73_asset_growth_efficiency_v036_2nd_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v036_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v036_2nd_signal

def f73ag_f73_asset_growth_efficiency_v037_2nd_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v037_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v037_2nd_signal

def f73ag_f73_asset_growth_efficiency_v038_2nd_signal(assets, capex):
    res = (assets / capex).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v038_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v038_2nd_signal

def f73ag_f73_asset_growth_efficiency_v039_2nd_signal(assets, capex):
    res = (assets / capex).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v039_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v039_2nd_signal

def f73ag_f73_asset_growth_efficiency_v040_2nd_signal(capex, assets):
    res = (capex / assets).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v040_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v040_2nd_signal

def f73ag_f73_asset_growth_efficiency_v041_2nd_signal(capex, assets):
    res = (capex / assets).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v041_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v041_2nd_signal

def f73ag_f73_asset_growth_efficiency_v042_2nd_signal(assets, fcf):
    res = (assets / fcf).rolling(42).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v042_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v042_2nd_signal

def f73ag_f73_asset_growth_efficiency_v043_2nd_signal(assets, fcf):
    res = (assets / fcf).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v043_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v043_2nd_signal

def f73ag_f73_asset_growth_efficiency_v044_2nd_signal(fcf, assets):
    res = (fcf / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v044_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v044_2nd_signal

def f73ag_f73_asset_growth_efficiency_v045_2nd_signal(fcf, assets):
    res = (fcf / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v045_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v045_2nd_signal

def f73ag_f73_asset_growth_efficiency_v046_2nd_signal(assets, ncfo):
    res = (assets / ncfo).rolling(42).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v046_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v046_2nd_signal

def f73ag_f73_asset_growth_efficiency_v047_2nd_signal(assets, ncfo):
    res = (assets / ncfo).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v047_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v047_2nd_signal

def f73ag_f73_asset_growth_efficiency_v048_2nd_signal(ncfo, assets):
    res = (ncfo / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v048_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v048_2nd_signal

def f73ag_f73_asset_growth_efficiency_v049_2nd_signal(ncfo, assets):
    res = (ncfo / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v049_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v049_2nd_signal

def f73ag_f73_asset_growth_efficiency_v050_2nd_signal(assets, gp):
    res = (assets / gp).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v050_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v050_2nd_signal

def f73ag_f73_asset_growth_efficiency_v051_2nd_signal(assets, gp):
    res = (assets / gp).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v051_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v051_2nd_signal

def f73ag_f73_asset_growth_efficiency_v052_2nd_signal(gp, assets):
    res = (gp / assets).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v052_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v052_2nd_signal

def f73ag_f73_asset_growth_efficiency_v053_2nd_signal(gp, assets):
    res = (gp / assets).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v053_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v053_2nd_signal

def f73ag_f73_asset_growth_efficiency_v054_2nd_signal(assets, opinc):
    res = (assets / opinc).rolling(42).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v054_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v054_2nd_signal

def f73ag_f73_asset_growth_efficiency_v055_2nd_signal(assets, opinc):
    res = (assets / opinc).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v055_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v055_2nd_signal

def f73ag_f73_asset_growth_efficiency_v056_2nd_signal(opinc, assets):
    res = (opinc / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v056_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v056_2nd_signal

def f73ag_f73_asset_growth_efficiency_v057_2nd_signal(opinc, assets):
    res = (opinc / assets).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v057_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v057_2nd_signal

def f73ag_f73_asset_growth_efficiency_v058_2nd_signal(assets, retearn):
    res = (assets / retearn).rolling(42).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v058_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v058_2nd_signal

def f73ag_f73_asset_growth_efficiency_v059_2nd_signal(assets, retearn):
    res = (assets / retearn).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v059_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v059_2nd_signal

def f73ag_f73_asset_growth_efficiency_v060_2nd_signal(retearn, assets):
    res = (retearn / assets).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v060_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v060_2nd_signal

def f73ag_f73_asset_growth_efficiency_v061_2nd_signal(assets, debt):
    res = (assets / debt).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v061_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v061_2nd_signal

def f73ag_f73_asset_growth_efficiency_v062_2nd_signal(assets, debt):
    res = (assets / debt).rolling(90).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v062_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v062_2nd_signal

def f73ag_f73_asset_growth_efficiency_v063_2nd_signal(debt, assets):
    res = (debt / assets).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v063_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v063_2nd_signal

def f73ag_f73_asset_growth_efficiency_v064_2nd_signal(debt, assets):
    res = (debt / assets).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v064_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v064_2nd_signal

def f73ag_f73_asset_growth_efficiency_v065_2nd_signal(assets):
    res = assets.pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v065_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v065_2nd_signal

def f73ag_f73_asset_growth_efficiency_v066_2nd_signal(assets):
    res = assets.pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v066_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v066_2nd_signal

def f73ag_f73_asset_growth_efficiency_v067_2nd_signal(assets):
    res = assets.pct_change(21).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v067_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v067_2nd_signal

def f73ag_f73_asset_growth_efficiency_v068_2nd_signal(revenue, assets):
    res = (revenue.pct_change(5) / assets.pct_change(5)).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v068_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v068_2nd_signal

def f73ag_f73_asset_growth_efficiency_v069_2nd_signal(revenue, assets):
    res = (revenue.pct_change(10) / assets.pct_change(10)).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v069_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v069_2nd_signal

def f73ag_f73_asset_growth_efficiency_v070_2nd_signal(ebitda, assets):
    res = (ebitda.pct_change(21) / assets.pct_change(21)).rolling(63).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v070_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v070_2nd_signal

def f73ag_f73_asset_growth_efficiency_v071_2nd_signal(ebitda, assets):
    res = (ebitda.pct_change(42) / assets.pct_change(42)).rolling(90).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v071_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v071_2nd_signal

def f73ag_f73_asset_growth_efficiency_v072_2nd_signal(netinc, assets):
    res = (netinc.pct_change(63) / assets.pct_change(63)).rolling(126).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v072_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v072_2nd_signal

def f73ag_f73_asset_growth_efficiency_v073_2nd_signal(netinc, assets):
    res = (netinc.pct_change(90) / assets.pct_change(90)).rolling(252).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v073_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v073_2nd_signal

def f73ag_f73_asset_growth_efficiency_v074_2nd_signal(assets, equity):
    res = (assets.pct_change(5) - equity.pct_change(5)).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v074_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v074_2nd_signal

def f73ag_f73_asset_growth_efficiency_v075_2nd_signal(assets, liabilities):
    res = (assets.pct_change(10) - liabilities.pct_change(10)).rolling(42).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v075_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v075_2nd_signal

def f73ag_f73_asset_growth_efficiency_v076_2nd_signal(assets, equity):
    res = (assets.pct_change(21) - equity.pct_change(21)).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v076_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v076_2nd_signal

def f73ag_f73_asset_growth_efficiency_v077_2nd_signal(assets, liabilities):
    res = (assets.pct_change(21) - liabilities.pct_change(21)).rolling(126).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v077_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v077_2nd_signal

def f73ag_f73_asset_growth_efficiency_v078_2nd_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(10).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v078_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v078_2nd_signal

def f73ag_f73_asset_growth_efficiency_v079_2nd_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v079_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v079_2nd_signal

def f73ag_f73_asset_growth_efficiency_v080_2nd_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v080_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v080_2nd_signal

def f73ag_f73_asset_growth_efficiency_v081_2nd_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v081_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v081_2nd_signal

def f73ag_f73_asset_growth_efficiency_v082_2nd_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v082_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v082_2nd_signal

def f73ag_f73_asset_growth_efficiency_v083_2nd_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v083_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v083_2nd_signal

def f73ag_f73_asset_growth_efficiency_v084_2nd_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v084_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v084_2nd_signal

def f73ag_f73_asset_growth_efficiency_v085_2nd_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v085_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v085_2nd_signal

def f73ag_f73_asset_growth_efficiency_v086_2nd_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v086_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v086_2nd_signal

def f73ag_f73_asset_growth_efficiency_v087_2nd_signal(netinc, sharesbas):
    res = (netinc / sharesbas).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v087_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v087_2nd_signal

def f73ag_f73_asset_growth_efficiency_v088_2nd_signal(netinc, sharesbas):
    res = (netinc / sharesbas).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v088_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v088_2nd_signal

def f73ag_f73_asset_growth_efficiency_v089_2nd_signal(ebitda, sharesbas):
    res = (ebitda / sharesbas).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v089_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v089_2nd_signal

def f73ag_f73_asset_growth_efficiency_v090_2nd_signal(ebitda, sharesbas):
    res = (ebitda / sharesbas).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v090_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v090_2nd_signal

def f73ag_f73_asset_growth_efficiency_v091_2nd_signal(assets, currentratio):
    res = (assets / currentratio).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v091_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v091_2nd_signal

def f73ag_f73_asset_growth_efficiency_v092_2nd_signal(assets, currentratio):
    res = (assets / currentratio).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v092_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v092_2nd_signal

def f73ag_f73_asset_growth_efficiency_v093_2nd_signal(revenue, currentratio):
    res = (revenue / currentratio).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v093_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v093_2nd_signal

def f73ag_f73_asset_growth_efficiency_v094_2nd_signal(revenue, currentratio):
    res = (revenue / currentratio).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v094_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v094_2nd_signal

def f73ag_f73_asset_growth_efficiency_v095_2nd_signal(assets, gp):
    res = (assets / gp).rolling(126).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v095_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v095_2nd_signal

def f73ag_f73_asset_growth_efficiency_v096_2nd_signal(assets, opinc):
    res = (assets / opinc).rolling(252).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v096_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v096_2nd_signal

def f73ag_f73_asset_growth_efficiency_v097_2nd_signal(assets, fcf):
    res = (assets / fcf).rolling(252).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v097_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v097_2nd_signal

def f73ag_f73_asset_growth_efficiency_v098_2nd_signal(assets, ncfo):
    res = (assets / ncfo).rolling(252).skew().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v098_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v098_2nd_signal

def f73ag_f73_asset_growth_efficiency_v099_2nd_signal(revenue, equity):
    res = (revenue / equity).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v099_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v099_2nd_signal

def f73ag_f73_asset_growth_efficiency_v100_2nd_signal(revenue, equity):
    res = (revenue / equity).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v100_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v100_2nd_signal

def f73ag_f73_asset_growth_efficiency_v101_2nd_signal(ebitda, equity):
    res = (ebitda / equity).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v101_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v101_2nd_signal

def f73ag_f73_asset_growth_efficiency_v102_2nd_signal(ebitda, equity):
    res = (ebitda / equity).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v102_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v102_2nd_signal

def f73ag_f73_asset_growth_efficiency_v103_2nd_signal(netinc, equity):
    res = (netinc / equity).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v103_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v103_2nd_signal

def f73ag_f73_asset_growth_efficiency_v104_2nd_signal(netinc, equity):
    res = (netinc / equity).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v104_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v104_2nd_signal

def f73ag_f73_asset_growth_efficiency_v105_2nd_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v105_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v105_2nd_signal

def f73ag_f73_asset_growth_efficiency_v106_2nd_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v106_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v106_2nd_signal

def f73ag_f73_asset_growth_efficiency_v107_2nd_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v107_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v107_2nd_signal

def f73ag_f73_asset_growth_efficiency_v108_2nd_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v108_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v108_2nd_signal

def f73ag_f73_asset_growth_efficiency_v109_2nd_signal(netinc, liabilities):
    res = (netinc / liabilities).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v109_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v109_2nd_signal

def f73ag_f73_asset_growth_efficiency_v110_2nd_signal(netinc, liabilities):
    res = (netinc / liabilities).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v110_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v110_2nd_signal

def f73ag_f73_asset_growth_efficiency_v111_2nd_signal(assets, revenue, equity):
    res = (assets / (revenue + equity)).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v111_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v111_2nd_signal

def f73ag_f73_asset_growth_efficiency_v112_2nd_signal(assets, revenue, equity):
    res = (assets / (revenue + equity)).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v112_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v112_2nd_signal

def f73ag_f73_asset_growth_efficiency_v113_2nd_signal(assets, ebitda, netinc):
    res = (assets / (ebitda + netinc)).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v113_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v113_2nd_signal

def f73ag_f73_asset_growth_efficiency_v114_2nd_signal(assets, ebitda, netinc):
    res = (assets / (ebitda + netinc)).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v114_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v114_2nd_signal

def f73ag_f73_asset_growth_efficiency_v115_2nd_signal(revenue, assets):
    res = (revenue.diff(5) / assets.diff(5)).rolling(252).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v115_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v115_2nd_signal

def f73ag_f73_asset_growth_efficiency_v116_2nd_signal(revenue, assets):
    res = (revenue.diff(10) / assets.diff(10)).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v116_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v116_2nd_signal

def f73ag_f73_asset_growth_efficiency_v117_2nd_signal(ebitda, assets):
    res = (ebitda.diff(5) / assets.diff(5)).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v117_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v117_2nd_signal

def f73ag_f73_asset_growth_efficiency_v118_2nd_signal(ebitda, assets):
    res = (ebitda.diff(10) / assets.diff(10)).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v118_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v118_2nd_signal

def f73ag_f73_asset_growth_efficiency_v119_2nd_signal(netinc, assets):
    res = (netinc.diff(5) / assets.diff(5)).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v119_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v119_2nd_signal

def f73ag_f73_asset_growth_efficiency_v120_2nd_signal(netinc, assets):
    res = (netinc.diff(10) / assets.diff(10)).rolling(42).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v120_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v120_2nd_signal

def f73ag_f73_asset_growth_efficiency_v121_2nd_signal(assets, revenue):
    res = (assets / revenue).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v121_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v121_2nd_signal

def f73ag_f73_asset_growth_efficiency_v122_2nd_signal(assets, revenue):
    res = (assets / revenue).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v122_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v122_2nd_signal

def f73ag_f73_asset_growth_efficiency_v123_2nd_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v123_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v123_2nd_signal

def f73ag_f73_asset_growth_efficiency_v124_2nd_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v124_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v124_2nd_signal

def f73ag_f73_asset_growth_efficiency_v125_2nd_signal(assets, netinc):
    res = (assets / netinc).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v125_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v125_2nd_signal

def f73ag_f73_asset_growth_efficiency_v126_2nd_signal(assets, netinc):
    res = (assets / netinc).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v126_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v126_2nd_signal

def f73ag_f73_asset_growth_efficiency_v127_2nd_signal(assets, equity):
    res = (assets / equity).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v127_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v127_2nd_signal

def f73ag_f73_asset_growth_efficiency_v128_2nd_signal(assets, equity):
    res = (assets / equity).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v128_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v128_2nd_signal

def f73ag_f73_asset_growth_efficiency_v129_2nd_signal(assets, liabilities):
    res = (assets / liabilities).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v129_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v129_2nd_signal

def f73ag_f73_asset_growth_efficiency_v130_2nd_signal(assets, liabilities):
    res = (assets / liabilities).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v130_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v130_2nd_signal

def f73ag_f73_asset_growth_efficiency_v131_2nd_signal(assets, workingcapital):
    res = (assets / workingcapital).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v131_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v131_2nd_signal

def f73ag_f73_asset_growth_efficiency_v132_2nd_signal(assets, workingcapital):
    res = (assets / workingcapital).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v132_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v132_2nd_signal

def f73ag_f73_asset_growth_efficiency_v133_2nd_signal(assets, marketcap):
    res = (assets / marketcap).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v133_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v133_2nd_signal

def f73ag_f73_asset_growth_efficiency_v134_2nd_signal(assets, marketcap):
    res = (assets / marketcap).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v134_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v134_2nd_signal

def f73ag_f73_asset_growth_efficiency_v135_2nd_signal(assets, ev):
    res = (assets / ev).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v135_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v135_2nd_signal

def f73ag_f73_asset_growth_efficiency_v136_2nd_signal(assets, ev):
    res = (assets / ev).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v136_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v136_2nd_signal

def f73ag_f73_asset_growth_efficiency_v137_2nd_signal(assets, capex):
    res = (assets / capex).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v137_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v137_2nd_signal

def f73ag_f73_asset_growth_efficiency_v138_2nd_signal(assets, capex):
    res = (assets / capex).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v138_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v138_2nd_signal

def f73ag_f73_asset_growth_efficiency_v139_2nd_signal(assets, fcf):
    res = (assets / fcf).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v139_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v139_2nd_signal

def f73ag_f73_asset_growth_efficiency_v140_2nd_signal(assets, fcf):
    res = (assets / fcf).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v140_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v140_2nd_signal

def f73ag_f73_asset_growth_efficiency_v141_2nd_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v141_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v141_2nd_signal

def f73ag_f73_asset_growth_efficiency_v142_2nd_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v142_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v142_2nd_signal

def f73ag_f73_asset_growth_efficiency_v143_2nd_signal(assets, gp):
    res = (assets / gp).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v143_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v143_2nd_signal

def f73ag_f73_asset_growth_efficiency_v144_2nd_signal(assets, gp):
    res = (assets / gp).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v144_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v144_2nd_signal

def f73ag_f73_asset_growth_efficiency_v145_2nd_signal(assets, opinc):
    res = (assets / opinc).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v145_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v145_2nd_signal

def f73ag_f73_asset_growth_efficiency_v146_2nd_signal(assets, opinc):
    res = (assets / opinc).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v146_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v146_2nd_signal

def f73ag_f73_asset_growth_efficiency_v147_2nd_signal(assets, retearn):
    res = (assets / retearn).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v147_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v147_2nd_signal

def f73ag_f73_asset_growth_efficiency_v148_2nd_signal(assets, retearn):
    res = (assets / retearn).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v148_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v148_2nd_signal

def f73ag_f73_asset_growth_efficiency_v149_2nd_signal(assets, debt):
    res = (assets / debt).pct_change(5).rolling(21).mean().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v149_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v149_2nd_signal

def f73ag_f73_asset_growth_efficiency_v150_2nd_signal(assets, debt):
    res = (assets / debt).pct_change(10).rolling(63).std().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v150_2nd_signal'] = f73ag_f73_asset_growth_efficiency_v150_2nd_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "opinc": np.random.uniform(40, 180, n),
        "netinc": np.random.uniform(20, 100, n),
        "assets": np.random.uniform(2000, 5000, n),
        "equity": np.random.uniform(1000, 3000, n),
        "marketcap": np.random.uniform(5000, 20000, n),
        "ev": np.random.uniform(6000, 25000, n),
        "volume": np.random.uniform(100000, 1000000, n),
        "ncfo": np.random.uniform(30, 150, n),
        "capex": np.random.uniform(10, 50, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n),
        "workingcapital": np.random.uniform(200, 800, n),
        "gp": np.random.uniform(100, 400, n),
        "retearn": np.random.uniform(500, 2000, n),
        "fcf": np.random.uniform(20, 120, n),
        "sharesbas": np.random.uniform(10, 100, n),
        "currentratio": np.random.uniform(0.5, 3.0, n)
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
