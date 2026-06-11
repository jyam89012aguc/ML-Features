import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f73ag_f73_asset_growth_efficiency_v001_3rd_signal(assets, revenue):
    res = (assets / revenue).rolling(5).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v001_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v001_3rd_signal

def f73ag_f73_asset_growth_efficiency_v002_3rd_signal(assets, revenue):
    res = (assets / revenue).rolling(10).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v002_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v002_3rd_signal

def f73ag_f73_asset_growth_efficiency_v003_3rd_signal(assets, revenue):
    res = (assets / revenue).rolling(21).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v003_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v003_3rd_signal

def f73ag_f73_asset_growth_efficiency_v004_3rd_signal(assets, revenue):
    res = (assets / revenue).rolling(63).kurt().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v004_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v004_3rd_signal

def f73ag_f73_asset_growth_efficiency_v005_3rd_signal(revenue, assets):
    res = (revenue / assets).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v005_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v005_3rd_signal

def f73ag_f73_asset_growth_efficiency_v006_3rd_signal(revenue, assets):
    res = (revenue / assets).rolling(21).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v006_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v006_3rd_signal

def f73ag_f73_asset_growth_efficiency_v007_3rd_signal(revenue, assets):
    res = (revenue / assets).rolling(63).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v007_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v007_3rd_signal

def f73ag_f73_asset_growth_efficiency_v008_3rd_signal(assets, ebitda):
    res = (assets / ebitda).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v008_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v008_3rd_signal

def f73ag_f73_asset_growth_efficiency_v009_3rd_signal(assets, ebitda):
    res = (assets / ebitda).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v009_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v009_3rd_signal

def f73ag_f73_asset_growth_efficiency_v010_3rd_signal(assets, ebitda):
    res = (assets / ebitda).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v010_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v010_3rd_signal

def f73ag_f73_asset_growth_efficiency_v011_3rd_signal(ebitda, assets):
    res = (ebitda / assets).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v011_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v011_3rd_signal

def f73ag_f73_asset_growth_efficiency_v012_3rd_signal(ebitda, assets):
    res = (ebitda / assets).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v012_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v012_3rd_signal

def f73ag_f73_asset_growth_efficiency_v013_3rd_signal(ebitda, assets):
    res = (ebitda / assets).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v013_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v013_3rd_signal

def f73ag_f73_asset_growth_efficiency_v014_3rd_signal(assets, netinc):
    res = (assets / netinc).rolling(42).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v014_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v014_3rd_signal

def f73ag_f73_asset_growth_efficiency_v015_3rd_signal(assets, netinc):
    res = (assets / netinc).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v015_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v015_3rd_signal

def f73ag_f73_asset_growth_efficiency_v016_3rd_signal(netinc, assets):
    res = (netinc / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v016_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v016_3rd_signal

def f73ag_f73_asset_growth_efficiency_v017_3rd_signal(netinc, assets):
    res = (netinc / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v017_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v017_3rd_signal

def f73ag_f73_asset_growth_efficiency_v018_3rd_signal(assets, equity):
    res = (assets / equity).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v018_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v018_3rd_signal

def f73ag_f73_asset_growth_efficiency_v019_3rd_signal(assets, equity):
    res = (assets / equity).rolling(90).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v019_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v019_3rd_signal

def f73ag_f73_asset_growth_efficiency_v020_3rd_signal(assets, equity):
    res = (assets / equity).rolling(252).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v020_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v020_3rd_signal

def f73ag_f73_asset_growth_efficiency_v021_3rd_signal(assets, marketcap):
    res = (assets / marketcap).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v021_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v021_3rd_signal

def f73ag_f73_asset_growth_efficiency_v022_3rd_signal(assets, marketcap):
    res = (assets / marketcap).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v022_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v022_3rd_signal

def f73ag_f73_asset_growth_efficiency_v023_3rd_signal(assets, marketcap):
    res = (assets / marketcap).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v023_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v023_3rd_signal

def f73ag_f73_asset_growth_efficiency_v024_3rd_signal(marketcap, assets):
    res = (marketcap / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v024_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v024_3rd_signal

def f73ag_f73_asset_growth_efficiency_v025_3rd_signal(marketcap, assets):
    res = (marketcap / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v025_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v025_3rd_signal

def f73ag_f73_asset_growth_efficiency_v026_3rd_signal(assets, ev):
    res = (assets / ev).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v026_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v026_3rd_signal

def f73ag_f73_asset_growth_efficiency_v027_3rd_signal(assets, ev):
    res = (assets / ev).rolling(90).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v027_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v027_3rd_signal

def f73ag_f73_asset_growth_efficiency_v028_3rd_signal(assets, liabilities):
    res = (assets / liabilities).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v028_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v028_3rd_signal

def f73ag_f73_asset_growth_efficiency_v029_3rd_signal(assets, liabilities):
    res = (assets / liabilities).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v029_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v029_3rd_signal

def f73ag_f73_asset_growth_efficiency_v030_3rd_signal(assets, liabilities):
    res = (assets / liabilities).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v030_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v030_3rd_signal

def f73ag_f73_asset_growth_efficiency_v031_3rd_signal(liabilities, assets):
    res = (liabilities / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v031_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v031_3rd_signal

def f73ag_f73_asset_growth_efficiency_v032_3rd_signal(liabilities, assets):
    res = (liabilities / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v032_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v032_3rd_signal

def f73ag_f73_asset_growth_efficiency_v033_3rd_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v033_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v033_3rd_signal

def f73ag_f73_asset_growth_efficiency_v034_3rd_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v034_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v034_3rd_signal

def f73ag_f73_asset_growth_efficiency_v035_3rd_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v035_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v035_3rd_signal

def f73ag_f73_asset_growth_efficiency_v036_3rd_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v036_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v036_3rd_signal

def f73ag_f73_asset_growth_efficiency_v037_3rd_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v037_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v037_3rd_signal

def f73ag_f73_asset_growth_efficiency_v038_3rd_signal(assets, capex):
    res = (assets / capex).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v038_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v038_3rd_signal

def f73ag_f73_asset_growth_efficiency_v039_3rd_signal(assets, capex):
    res = (assets / capex).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v039_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v039_3rd_signal

def f73ag_f73_asset_growth_efficiency_v040_3rd_signal(capex, assets):
    res = (capex / assets).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v040_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v040_3rd_signal

def f73ag_f73_asset_growth_efficiency_v041_3rd_signal(capex, assets):
    res = (capex / assets).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v041_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v041_3rd_signal

def f73ag_f73_asset_growth_efficiency_v042_3rd_signal(assets, fcf):
    res = (assets / fcf).rolling(42).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v042_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v042_3rd_signal

def f73ag_f73_asset_growth_efficiency_v043_3rd_signal(assets, fcf):
    res = (assets / fcf).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v043_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v043_3rd_signal

def f73ag_f73_asset_growth_efficiency_v044_3rd_signal(fcf, assets):
    res = (fcf / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v044_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v044_3rd_signal

def f73ag_f73_asset_growth_efficiency_v045_3rd_signal(fcf, assets):
    res = (fcf / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v045_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v045_3rd_signal

def f73ag_f73_asset_growth_efficiency_v046_3rd_signal(assets, ncfo):
    res = (assets / ncfo).rolling(42).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v046_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v046_3rd_signal

def f73ag_f73_asset_growth_efficiency_v047_3rd_signal(assets, ncfo):
    res = (assets / ncfo).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v047_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v047_3rd_signal

def f73ag_f73_asset_growth_efficiency_v048_3rd_signal(ncfo, assets):
    res = (ncfo / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v048_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v048_3rd_signal

def f73ag_f73_asset_growth_efficiency_v049_3rd_signal(ncfo, assets):
    res = (ncfo / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v049_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v049_3rd_signal

def f73ag_f73_asset_growth_efficiency_v050_3rd_signal(assets, gp):
    res = (assets / gp).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v050_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v050_3rd_signal

def f73ag_f73_asset_growth_efficiency_v051_3rd_signal(assets, gp):
    res = (assets / gp).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v051_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v051_3rd_signal

def f73ag_f73_asset_growth_efficiency_v052_3rd_signal(gp, assets):
    res = (gp / assets).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v052_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v052_3rd_signal

def f73ag_f73_asset_growth_efficiency_v053_3rd_signal(gp, assets):
    res = (gp / assets).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v053_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v053_3rd_signal

def f73ag_f73_asset_growth_efficiency_v054_3rd_signal(assets, opinc):
    res = (assets / opinc).rolling(42).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v054_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v054_3rd_signal

def f73ag_f73_asset_growth_efficiency_v055_3rd_signal(assets, opinc):
    res = (assets / opinc).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v055_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v055_3rd_signal

def f73ag_f73_asset_growth_efficiency_v056_3rd_signal(opinc, assets):
    res = (opinc / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v056_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v056_3rd_signal

def f73ag_f73_asset_growth_efficiency_v057_3rd_signal(opinc, assets):
    res = (opinc / assets).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v057_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v057_3rd_signal

def f73ag_f73_asset_growth_efficiency_v058_3rd_signal(assets, retearn):
    res = (assets / retearn).rolling(42).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v058_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v058_3rd_signal

def f73ag_f73_asset_growth_efficiency_v059_3rd_signal(assets, retearn):
    res = (assets / retearn).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v059_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v059_3rd_signal

def f73ag_f73_asset_growth_efficiency_v060_3rd_signal(retearn, assets):
    res = (retearn / assets).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v060_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v060_3rd_signal

def f73ag_f73_asset_growth_efficiency_v061_3rd_signal(assets, debt):
    res = (assets / debt).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v061_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v061_3rd_signal

def f73ag_f73_asset_growth_efficiency_v062_3rd_signal(assets, debt):
    res = (assets / debt).rolling(90).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v062_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v062_3rd_signal

def f73ag_f73_asset_growth_efficiency_v063_3rd_signal(debt, assets):
    res = (debt / assets).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v063_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v063_3rd_signal

def f73ag_f73_asset_growth_efficiency_v064_3rd_signal(debt, assets):
    res = (debt / assets).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v064_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v064_3rd_signal

def f73ag_f73_asset_growth_efficiency_v065_3rd_signal(assets):
    res = assets.pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v065_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v065_3rd_signal

def f73ag_f73_asset_growth_efficiency_v066_3rd_signal(assets):
    res = assets.pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v066_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v066_3rd_signal

def f73ag_f73_asset_growth_efficiency_v067_3rd_signal(assets):
    res = assets.pct_change(21).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v067_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v067_3rd_signal

def f73ag_f73_asset_growth_efficiency_v068_3rd_signal(revenue, assets):
    res = (revenue.pct_change(5) / assets.pct_change(5)).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v068_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v068_3rd_signal

def f73ag_f73_asset_growth_efficiency_v069_3rd_signal(revenue, assets):
    res = (revenue.pct_change(10) / assets.pct_change(10)).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v069_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v069_3rd_signal

def f73ag_f73_asset_growth_efficiency_v070_3rd_signal(ebitda, assets):
    res = (ebitda.pct_change(21) / assets.pct_change(21)).rolling(63).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v070_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v070_3rd_signal

def f73ag_f73_asset_growth_efficiency_v071_3rd_signal(ebitda, assets):
    res = (ebitda.pct_change(42) / assets.pct_change(42)).rolling(90).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v071_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v071_3rd_signal

def f73ag_f73_asset_growth_efficiency_v072_3rd_signal(netinc, assets):
    res = (netinc.pct_change(63) / assets.pct_change(63)).rolling(126).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v072_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v072_3rd_signal

def f73ag_f73_asset_growth_efficiency_v073_3rd_signal(netinc, assets):
    res = (netinc.pct_change(90) / assets.pct_change(90)).rolling(252).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v073_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v073_3rd_signal

def f73ag_f73_asset_growth_efficiency_v074_3rd_signal(assets, equity):
    res = (assets.pct_change(5) - equity.pct_change(5)).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v074_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v074_3rd_signal

def f73ag_f73_asset_growth_efficiency_v075_3rd_signal(assets, liabilities):
    res = (assets.pct_change(10) - liabilities.pct_change(10)).rolling(42).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v075_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v075_3rd_signal

def f73ag_f73_asset_growth_efficiency_v076_3rd_signal(assets, equity):
    res = (assets.pct_change(21) - equity.pct_change(21)).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v076_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v076_3rd_signal

def f73ag_f73_asset_growth_efficiency_v077_3rd_signal(assets, liabilities):
    res = (assets.pct_change(21) - liabilities.pct_change(21)).rolling(126).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v077_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v077_3rd_signal

def f73ag_f73_asset_growth_efficiency_v078_3rd_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(10).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v078_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v078_3rd_signal

def f73ag_f73_asset_growth_efficiency_v079_3rd_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v079_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v079_3rd_signal

def f73ag_f73_asset_growth_efficiency_v080_3rd_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v080_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v080_3rd_signal

def f73ag_f73_asset_growth_efficiency_v081_3rd_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v081_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v081_3rd_signal

def f73ag_f73_asset_growth_efficiency_v082_3rd_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v082_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v082_3rd_signal

def f73ag_f73_asset_growth_efficiency_v083_3rd_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v083_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v083_3rd_signal

def f73ag_f73_asset_growth_efficiency_v084_3rd_signal(assets, sharesbas):
    res = (assets / sharesbas).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v084_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v084_3rd_signal

def f73ag_f73_asset_growth_efficiency_v085_3rd_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v085_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v085_3rd_signal

def f73ag_f73_asset_growth_efficiency_v086_3rd_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v086_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v086_3rd_signal

def f73ag_f73_asset_growth_efficiency_v087_3rd_signal(netinc, sharesbas):
    res = (netinc / sharesbas).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v087_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v087_3rd_signal

def f73ag_f73_asset_growth_efficiency_v088_3rd_signal(netinc, sharesbas):
    res = (netinc / sharesbas).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v088_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v088_3rd_signal

def f73ag_f73_asset_growth_efficiency_v089_3rd_signal(ebitda, sharesbas):
    res = (ebitda / sharesbas).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v089_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v089_3rd_signal

def f73ag_f73_asset_growth_efficiency_v090_3rd_signal(ebitda, sharesbas):
    res = (ebitda / sharesbas).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v090_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v090_3rd_signal

def f73ag_f73_asset_growth_efficiency_v091_3rd_signal(assets, currentratio):
    res = (assets / currentratio).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v091_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v091_3rd_signal

def f73ag_f73_asset_growth_efficiency_v092_3rd_signal(assets, currentratio):
    res = (assets / currentratio).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v092_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v092_3rd_signal

def f73ag_f73_asset_growth_efficiency_v093_3rd_signal(revenue, currentratio):
    res = (revenue / currentratio).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v093_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v093_3rd_signal

def f73ag_f73_asset_growth_efficiency_v094_3rd_signal(revenue, currentratio):
    res = (revenue / currentratio).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v094_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v094_3rd_signal

def f73ag_f73_asset_growth_efficiency_v095_3rd_signal(assets, gp):
    res = (assets / gp).rolling(126).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v095_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v095_3rd_signal

def f73ag_f73_asset_growth_efficiency_v096_3rd_signal(assets, opinc):
    res = (assets / opinc).rolling(252).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v096_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v096_3rd_signal

def f73ag_f73_asset_growth_efficiency_v097_3rd_signal(assets, fcf):
    res = (assets / fcf).rolling(252).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v097_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v097_3rd_signal

def f73ag_f73_asset_growth_efficiency_v098_3rd_signal(assets, ncfo):
    res = (assets / ncfo).rolling(252).skew().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v098_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v098_3rd_signal

def f73ag_f73_asset_growth_efficiency_v099_3rd_signal(revenue, equity):
    res = (revenue / equity).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v099_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v099_3rd_signal

def f73ag_f73_asset_growth_efficiency_v100_3rd_signal(revenue, equity):
    res = (revenue / equity).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v100_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v100_3rd_signal

def f73ag_f73_asset_growth_efficiency_v101_3rd_signal(ebitda, equity):
    res = (ebitda / equity).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v101_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v101_3rd_signal

def f73ag_f73_asset_growth_efficiency_v102_3rd_signal(ebitda, equity):
    res = (ebitda / equity).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v102_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v102_3rd_signal

def f73ag_f73_asset_growth_efficiency_v103_3rd_signal(netinc, equity):
    res = (netinc / equity).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v103_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v103_3rd_signal

def f73ag_f73_asset_growth_efficiency_v104_3rd_signal(netinc, equity):
    res = (netinc / equity).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v104_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v104_3rd_signal

def f73ag_f73_asset_growth_efficiency_v105_3rd_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v105_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v105_3rd_signal

def f73ag_f73_asset_growth_efficiency_v106_3rd_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v106_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v106_3rd_signal

def f73ag_f73_asset_growth_efficiency_v107_3rd_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v107_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v107_3rd_signal

def f73ag_f73_asset_growth_efficiency_v108_3rd_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v108_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v108_3rd_signal

def f73ag_f73_asset_growth_efficiency_v109_3rd_signal(netinc, liabilities):
    res = (netinc / liabilities).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v109_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v109_3rd_signal

def f73ag_f73_asset_growth_efficiency_v110_3rd_signal(netinc, liabilities):
    res = (netinc / liabilities).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v110_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v110_3rd_signal

def f73ag_f73_asset_growth_efficiency_v111_3rd_signal(assets, revenue, equity):
    res = (assets / (revenue + equity)).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v111_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v111_3rd_signal

def f73ag_f73_asset_growth_efficiency_v112_3rd_signal(assets, revenue, equity):
    res = (assets / (revenue + equity)).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v112_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v112_3rd_signal

def f73ag_f73_asset_growth_efficiency_v113_3rd_signal(assets, ebitda, netinc):
    res = (assets / (ebitda + netinc)).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v113_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v113_3rd_signal

def f73ag_f73_asset_growth_efficiency_v114_3rd_signal(assets, ebitda, netinc):
    res = (assets / (ebitda + netinc)).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v114_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v114_3rd_signal

def f73ag_f73_asset_growth_efficiency_v115_3rd_signal(revenue, assets):
    res = (revenue.diff(5) / assets.diff(5)).rolling(252).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v115_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v115_3rd_signal

def f73ag_f73_asset_growth_efficiency_v116_3rd_signal(revenue, assets):
    res = (revenue.diff(10) / assets.diff(10)).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v116_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v116_3rd_signal

def f73ag_f73_asset_growth_efficiency_v117_3rd_signal(ebitda, assets):
    res = (ebitda.diff(5) / assets.diff(5)).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v117_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v117_3rd_signal

def f73ag_f73_asset_growth_efficiency_v118_3rd_signal(ebitda, assets):
    res = (ebitda.diff(10) / assets.diff(10)).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v118_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v118_3rd_signal

def f73ag_f73_asset_growth_efficiency_v119_3rd_signal(netinc, assets):
    res = (netinc.diff(5) / assets.diff(5)).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v119_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v119_3rd_signal

def f73ag_f73_asset_growth_efficiency_v120_3rd_signal(netinc, assets):
    res = (netinc.diff(10) / assets.diff(10)).rolling(42).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v120_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v120_3rd_signal

def f73ag_f73_asset_growth_efficiency_v121_3rd_signal(assets, revenue):
    res = (assets / revenue).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v121_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v121_3rd_signal

def f73ag_f73_asset_growth_efficiency_v122_3rd_signal(assets, revenue):
    res = (assets / revenue).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v122_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v122_3rd_signal

def f73ag_f73_asset_growth_efficiency_v123_3rd_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v123_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v123_3rd_signal

def f73ag_f73_asset_growth_efficiency_v124_3rd_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v124_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v124_3rd_signal

def f73ag_f73_asset_growth_efficiency_v125_3rd_signal(assets, netinc):
    res = (assets / netinc).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v125_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v125_3rd_signal

def f73ag_f73_asset_growth_efficiency_v126_3rd_signal(assets, netinc):
    res = (assets / netinc).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v126_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v126_3rd_signal

def f73ag_f73_asset_growth_efficiency_v127_3rd_signal(assets, equity):
    res = (assets / equity).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v127_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v127_3rd_signal

def f73ag_f73_asset_growth_efficiency_v128_3rd_signal(assets, equity):
    res = (assets / equity).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v128_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v128_3rd_signal

def f73ag_f73_asset_growth_efficiency_v129_3rd_signal(assets, liabilities):
    res = (assets / liabilities).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v129_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v129_3rd_signal

def f73ag_f73_asset_growth_efficiency_v130_3rd_signal(assets, liabilities):
    res = (assets / liabilities).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v130_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v130_3rd_signal

def f73ag_f73_asset_growth_efficiency_v131_3rd_signal(assets, workingcapital):
    res = (assets / workingcapital).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v131_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v131_3rd_signal

def f73ag_f73_asset_growth_efficiency_v132_3rd_signal(assets, workingcapital):
    res = (assets / workingcapital).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v132_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v132_3rd_signal

def f73ag_f73_asset_growth_efficiency_v133_3rd_signal(assets, marketcap):
    res = (assets / marketcap).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v133_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v133_3rd_signal

def f73ag_f73_asset_growth_efficiency_v134_3rd_signal(assets, marketcap):
    res = (assets / marketcap).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v134_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v134_3rd_signal

def f73ag_f73_asset_growth_efficiency_v135_3rd_signal(assets, ev):
    res = (assets / ev).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v135_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v135_3rd_signal

def f73ag_f73_asset_growth_efficiency_v136_3rd_signal(assets, ev):
    res = (assets / ev).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v136_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v136_3rd_signal

def f73ag_f73_asset_growth_efficiency_v137_3rd_signal(assets, capex):
    res = (assets / capex).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v137_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v137_3rd_signal

def f73ag_f73_asset_growth_efficiency_v138_3rd_signal(assets, capex):
    res = (assets / capex).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v138_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v138_3rd_signal

def f73ag_f73_asset_growth_efficiency_v139_3rd_signal(assets, fcf):
    res = (assets / fcf).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v139_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v139_3rd_signal

def f73ag_f73_asset_growth_efficiency_v140_3rd_signal(assets, fcf):
    res = (assets / fcf).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v140_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v140_3rd_signal

def f73ag_f73_asset_growth_efficiency_v141_3rd_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v141_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v141_3rd_signal

def f73ag_f73_asset_growth_efficiency_v142_3rd_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v142_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v142_3rd_signal

def f73ag_f73_asset_growth_efficiency_v143_3rd_signal(assets, gp):
    res = (assets / gp).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v143_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v143_3rd_signal

def f73ag_f73_asset_growth_efficiency_v144_3rd_signal(assets, gp):
    res = (assets / gp).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v144_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v144_3rd_signal

def f73ag_f73_asset_growth_efficiency_v145_3rd_signal(assets, opinc):
    res = (assets / opinc).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v145_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v145_3rd_signal

def f73ag_f73_asset_growth_efficiency_v146_3rd_signal(assets, opinc):
    res = (assets / opinc).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v146_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v146_3rd_signal

def f73ag_f73_asset_growth_efficiency_v147_3rd_signal(assets, retearn):
    res = (assets / retearn).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v147_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v147_3rd_signal

def f73ag_f73_asset_growth_efficiency_v148_3rd_signal(assets, retearn):
    res = (assets / retearn).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v148_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v148_3rd_signal

def f73ag_f73_asset_growth_efficiency_v149_3rd_signal(assets, debt):
    res = (assets / debt).pct_change(5).rolling(21).mean().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v149_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v149_3rd_signal

def f73ag_f73_asset_growth_efficiency_v150_3rd_signal(assets, debt):
    res = (assets / debt).pct_change(10).rolling(63).std().diff().diff().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v150_3rd_signal'] = f73ag_f73_asset_growth_efficiency_v150_3rd_signal

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
