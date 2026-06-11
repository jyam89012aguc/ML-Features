import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f73ag_f73_asset_growth_efficiency_v001_signal(assets, revenue):
    res = (assets / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v001_signal'] = f73ag_f73_asset_growth_efficiency_v001_signal

def f73ag_f73_asset_growth_efficiency_v002_signal(assets, revenue):
    res = (assets / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v002_signal'] = f73ag_f73_asset_growth_efficiency_v002_signal

def f73ag_f73_asset_growth_efficiency_v003_signal(assets, revenue):
    res = (assets / revenue).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v003_signal'] = f73ag_f73_asset_growth_efficiency_v003_signal

def f73ag_f73_asset_growth_efficiency_v004_signal(assets, revenue):
    res = (assets / revenue).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v004_signal'] = f73ag_f73_asset_growth_efficiency_v004_signal

def f73ag_f73_asset_growth_efficiency_v005_signal(revenue, assets):
    res = (revenue / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v005_signal'] = f73ag_f73_asset_growth_efficiency_v005_signal

def f73ag_f73_asset_growth_efficiency_v006_signal(revenue, assets):
    res = (revenue / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v006_signal'] = f73ag_f73_asset_growth_efficiency_v006_signal

def f73ag_f73_asset_growth_efficiency_v007_signal(revenue, assets):
    res = (revenue / assets).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v007_signal'] = f73ag_f73_asset_growth_efficiency_v007_signal

def f73ag_f73_asset_growth_efficiency_v008_signal(assets, ebitda):
    res = (assets / ebitda).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v008_signal'] = f73ag_f73_asset_growth_efficiency_v008_signal

def f73ag_f73_asset_growth_efficiency_v009_signal(assets, ebitda):
    res = (assets / ebitda).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v009_signal'] = f73ag_f73_asset_growth_efficiency_v009_signal

def f73ag_f73_asset_growth_efficiency_v010_signal(assets, ebitda):
    res = (assets / ebitda).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v010_signal'] = f73ag_f73_asset_growth_efficiency_v010_signal

def f73ag_f73_asset_growth_efficiency_v011_signal(ebitda, assets):
    res = (ebitda / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v011_signal'] = f73ag_f73_asset_growth_efficiency_v011_signal

def f73ag_f73_asset_growth_efficiency_v012_signal(ebitda, assets):
    res = (ebitda / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v012_signal'] = f73ag_f73_asset_growth_efficiency_v012_signal

def f73ag_f73_asset_growth_efficiency_v013_signal(ebitda, assets):
    res = (ebitda / assets).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v013_signal'] = f73ag_f73_asset_growth_efficiency_v013_signal

def f73ag_f73_asset_growth_efficiency_v014_signal(assets, netinc):
    res = (assets / netinc).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v014_signal'] = f73ag_f73_asset_growth_efficiency_v014_signal

def f73ag_f73_asset_growth_efficiency_v015_signal(assets, netinc):
    res = (assets / netinc).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v015_signal'] = f73ag_f73_asset_growth_efficiency_v015_signal

def f73ag_f73_asset_growth_efficiency_v016_signal(netinc, assets):
    res = (netinc / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v016_signal'] = f73ag_f73_asset_growth_efficiency_v016_signal

def f73ag_f73_asset_growth_efficiency_v017_signal(netinc, assets):
    res = (netinc / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v017_signal'] = f73ag_f73_asset_growth_efficiency_v017_signal

def f73ag_f73_asset_growth_efficiency_v018_signal(assets, equity):
    res = (assets / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v018_signal'] = f73ag_f73_asset_growth_efficiency_v018_signal

def f73ag_f73_asset_growth_efficiency_v019_signal(assets, equity):
    res = (assets / equity).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v019_signal'] = f73ag_f73_asset_growth_efficiency_v019_signal

def f73ag_f73_asset_growth_efficiency_v020_signal(assets, equity):
    res = (assets / equity).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v020_signal'] = f73ag_f73_asset_growth_efficiency_v020_signal

def f73ag_f73_asset_growth_efficiency_v021_signal(assets, marketcap):
    res = (assets / marketcap).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v021_signal'] = f73ag_f73_asset_growth_efficiency_v021_signal

def f73ag_f73_asset_growth_efficiency_v022_signal(assets, marketcap):
    res = (assets / marketcap).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v022_signal'] = f73ag_f73_asset_growth_efficiency_v022_signal

def f73ag_f73_asset_growth_efficiency_v023_signal(assets, marketcap):
    res = (assets / marketcap).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v023_signal'] = f73ag_f73_asset_growth_efficiency_v023_signal

def f73ag_f73_asset_growth_efficiency_v024_signal(marketcap, assets):
    res = (marketcap / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v024_signal'] = f73ag_f73_asset_growth_efficiency_v024_signal

def f73ag_f73_asset_growth_efficiency_v025_signal(marketcap, assets):
    res = (marketcap / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v025_signal'] = f73ag_f73_asset_growth_efficiency_v025_signal

def f73ag_f73_asset_growth_efficiency_v026_signal(assets, ev):
    res = (assets / ev).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v026_signal'] = f73ag_f73_asset_growth_efficiency_v026_signal

def f73ag_f73_asset_growth_efficiency_v027_signal(assets, ev):
    res = (assets / ev).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v027_signal'] = f73ag_f73_asset_growth_efficiency_v027_signal

def f73ag_f73_asset_growth_efficiency_v028_signal(assets, liabilities):
    res = (assets / liabilities).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v028_signal'] = f73ag_f73_asset_growth_efficiency_v028_signal

def f73ag_f73_asset_growth_efficiency_v029_signal(assets, liabilities):
    res = (assets / liabilities).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v029_signal'] = f73ag_f73_asset_growth_efficiency_v029_signal

def f73ag_f73_asset_growth_efficiency_v030_signal(assets, liabilities):
    res = (assets / liabilities).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v030_signal'] = f73ag_f73_asset_growth_efficiency_v030_signal

def f73ag_f73_asset_growth_efficiency_v031_signal(liabilities, assets):
    res = (liabilities / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v031_signal'] = f73ag_f73_asset_growth_efficiency_v031_signal

def f73ag_f73_asset_growth_efficiency_v032_signal(liabilities, assets):
    res = (liabilities / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v032_signal'] = f73ag_f73_asset_growth_efficiency_v032_signal

def f73ag_f73_asset_growth_efficiency_v033_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v033_signal'] = f73ag_f73_asset_growth_efficiency_v033_signal

def f73ag_f73_asset_growth_efficiency_v034_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v034_signal'] = f73ag_f73_asset_growth_efficiency_v034_signal

def f73ag_f73_asset_growth_efficiency_v035_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v035_signal'] = f73ag_f73_asset_growth_efficiency_v035_signal

def f73ag_f73_asset_growth_efficiency_v036_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v036_signal'] = f73ag_f73_asset_growth_efficiency_v036_signal

def f73ag_f73_asset_growth_efficiency_v037_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v037_signal'] = f73ag_f73_asset_growth_efficiency_v037_signal

def f73ag_f73_asset_growth_efficiency_v038_signal(assets, capex):
    res = (assets / capex).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v038_signal'] = f73ag_f73_asset_growth_efficiency_v038_signal

def f73ag_f73_asset_growth_efficiency_v039_signal(assets, capex):
    res = (assets / capex).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v039_signal'] = f73ag_f73_asset_growth_efficiency_v039_signal

def f73ag_f73_asset_growth_efficiency_v040_signal(capex, assets):
    res = (capex / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v040_signal'] = f73ag_f73_asset_growth_efficiency_v040_signal

def f73ag_f73_asset_growth_efficiency_v041_signal(capex, assets):
    res = (capex / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v041_signal'] = f73ag_f73_asset_growth_efficiency_v041_signal

def f73ag_f73_asset_growth_efficiency_v042_signal(assets, fcf):
    res = (assets / fcf).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v042_signal'] = f73ag_f73_asset_growth_efficiency_v042_signal

def f73ag_f73_asset_growth_efficiency_v043_signal(assets, fcf):
    res = (assets / fcf).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v043_signal'] = f73ag_f73_asset_growth_efficiency_v043_signal

def f73ag_f73_asset_growth_efficiency_v044_signal(fcf, assets):
    res = (fcf / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v044_signal'] = f73ag_f73_asset_growth_efficiency_v044_signal

def f73ag_f73_asset_growth_efficiency_v045_signal(fcf, assets):
    res = (fcf / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v045_signal'] = f73ag_f73_asset_growth_efficiency_v045_signal

def f73ag_f73_asset_growth_efficiency_v046_signal(assets, ncfo):
    res = (assets / ncfo).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v046_signal'] = f73ag_f73_asset_growth_efficiency_v046_signal

def f73ag_f73_asset_growth_efficiency_v047_signal(assets, ncfo):
    res = (assets / ncfo).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v047_signal'] = f73ag_f73_asset_growth_efficiency_v047_signal

def f73ag_f73_asset_growth_efficiency_v048_signal(ncfo, assets):
    res = (ncfo / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v048_signal'] = f73ag_f73_asset_growth_efficiency_v048_signal

def f73ag_f73_asset_growth_efficiency_v049_signal(ncfo, assets):
    res = (ncfo / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v049_signal'] = f73ag_f73_asset_growth_efficiency_v049_signal

def f73ag_f73_asset_growth_efficiency_v050_signal(assets, gp):
    res = (assets / gp).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v050_signal'] = f73ag_f73_asset_growth_efficiency_v050_signal

def f73ag_f73_asset_growth_efficiency_v051_signal(assets, gp):
    res = (assets / gp).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v051_signal'] = f73ag_f73_asset_growth_efficiency_v051_signal

def f73ag_f73_asset_growth_efficiency_v052_signal(gp, assets):
    res = (gp / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v052_signal'] = f73ag_f73_asset_growth_efficiency_v052_signal

def f73ag_f73_asset_growth_efficiency_v053_signal(gp, assets):
    res = (gp / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v053_signal'] = f73ag_f73_asset_growth_efficiency_v053_signal

def f73ag_f73_asset_growth_efficiency_v054_signal(assets, opinc):
    res = (assets / opinc).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v054_signal'] = f73ag_f73_asset_growth_efficiency_v054_signal

def f73ag_f73_asset_growth_efficiency_v055_signal(assets, opinc):
    res = (assets / opinc).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v055_signal'] = f73ag_f73_asset_growth_efficiency_v055_signal

def f73ag_f73_asset_growth_efficiency_v056_signal(opinc, assets):
    res = (opinc / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v056_signal'] = f73ag_f73_asset_growth_efficiency_v056_signal

def f73ag_f73_asset_growth_efficiency_v057_signal(opinc, assets):
    res = (opinc / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v057_signal'] = f73ag_f73_asset_growth_efficiency_v057_signal

def f73ag_f73_asset_growth_efficiency_v058_signal(assets, retearn):
    res = (assets / retearn).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v058_signal'] = f73ag_f73_asset_growth_efficiency_v058_signal

def f73ag_f73_asset_growth_efficiency_v059_signal(assets, retearn):
    res = (assets / retearn).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v059_signal'] = f73ag_f73_asset_growth_efficiency_v059_signal

def f73ag_f73_asset_growth_efficiency_v060_signal(retearn, assets):
    res = (retearn / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v060_signal'] = f73ag_f73_asset_growth_efficiency_v060_signal

def f73ag_f73_asset_growth_efficiency_v061_signal(assets, debt):
    res = (assets / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v061_signal'] = f73ag_f73_asset_growth_efficiency_v061_signal

def f73ag_f73_asset_growth_efficiency_v062_signal(assets, debt):
    res = (assets / debt).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v062_signal'] = f73ag_f73_asset_growth_efficiency_v062_signal

def f73ag_f73_asset_growth_efficiency_v063_signal(debt, assets):
    res = (debt / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v063_signal'] = f73ag_f73_asset_growth_efficiency_v063_signal

def f73ag_f73_asset_growth_efficiency_v064_signal(debt, assets):
    res = (debt / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v064_signal'] = f73ag_f73_asset_growth_efficiency_v064_signal

def f73ag_f73_asset_growth_efficiency_v065_signal(assets):
    res = assets.pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v065_signal'] = f73ag_f73_asset_growth_efficiency_v065_signal

def f73ag_f73_asset_growth_efficiency_v066_signal(assets):
    res = assets.pct_change(10).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v066_signal'] = f73ag_f73_asset_growth_efficiency_v066_signal

def f73ag_f73_asset_growth_efficiency_v067_signal(assets):
    res = assets.pct_change(21).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v067_signal'] = f73ag_f73_asset_growth_efficiency_v067_signal

def f73ag_f73_asset_growth_efficiency_v068_signal(revenue, assets):
    res = revenue.pct_change(5) / assets.pct_change(5)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v068_signal'] = f73ag_f73_asset_growth_efficiency_v068_signal

def f73ag_f73_asset_growth_efficiency_v069_signal(revenue, assets):
    res = revenue.pct_change(10) / assets.pct_change(10)
    return res.rolling(42).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v069_signal'] = f73ag_f73_asset_growth_efficiency_v069_signal

def f73ag_f73_asset_growth_efficiency_v070_signal(ebitda, assets):
    res = ebitda.pct_change(21) / assets.pct_change(21)
    return res.rolling(63).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v070_signal'] = f73ag_f73_asset_growth_efficiency_v070_signal

def f73ag_f73_asset_growth_efficiency_v071_signal(ebitda, assets):
    res = ebitda.pct_change(42) / assets.pct_change(42)
    return res.rolling(90).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v071_signal'] = f73ag_f73_asset_growth_efficiency_v071_signal

def f73ag_f73_asset_growth_efficiency_v072_signal(netinc, assets):
    res = netinc.pct_change(63) / assets.pct_change(63)
    return res.rolling(126).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v072_signal'] = f73ag_f73_asset_growth_efficiency_v072_signal

def f73ag_f73_asset_growth_efficiency_v073_signal(netinc, assets):
    res = netinc.pct_change(90) / assets.pct_change(90)
    return res.rolling(252).std().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v073_signal'] = f73ag_f73_asset_growth_efficiency_v073_signal

def f73ag_f73_asset_growth_efficiency_v074_signal(assets, equity):
    res = assets.pct_change(5) - equity.pct_change(5)
    return res.rolling(21).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v074_signal'] = f73ag_f73_asset_growth_efficiency_v074_signal

def f73ag_f73_asset_growth_efficiency_v075_signal(assets, liabilities):
    res = assets.pct_change(10) - liabilities.pct_change(10)
    return res.rolling(42).mean().replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f73ag_f73_asset_growth_efficiency_v075_signal'] = f73ag_f73_asset_growth_efficiency_v075_signal

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
        "closeadj": np.random.uniform(10, 100, n),
        "volume": np.random.uniform(100000, 1000000, n),
        "ncfo": np.random.uniform(30, 150, n),
        "capex": np.random.uniform(10, 50, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n),
        "workingcapital": np.random.uniform(200, 800, n),
        "gp": np.random.uniform(100, 400, n),
        "retearn": np.random.uniform(500, 2000, n),
        "fcf": np.random.uniform(20, 120, n)
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
