import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f58ds_f58_debt_servicing_capacity_calc001_5d_base_v001_signal(assets, ebitda):
    res = (ebitda / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc001_5d_base_v001_signal'] = f58ds_f58_debt_servicing_capacity_calc001_5d_base_v001_signal

def f58ds_f58_debt_servicing_capacity_calc002_21d_base_v002_signal(liabilities, opinc):
    res = (opinc / liabilities).rolling(21).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc002_21d_base_v002_signal'] = f58ds_f58_debt_servicing_capacity_calc002_21d_base_v002_signal

def f58ds_f58_debt_servicing_capacity_calc003_10d_base_v003_signal(debt, marketcap):
    res = (debt / marketcap).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc003_10d_base_v003_signal'] = f58ds_f58_debt_servicing_capacity_calc003_10d_base_v003_signal

def f58ds_f58_debt_servicing_capacity_calc004_126d_base_v004_signal(assets, fcf):
    res = (fcf / assets).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc004_126d_base_v004_signal'] = f58ds_f58_debt_servicing_capacity_calc004_126d_base_v004_signal

def f58ds_f58_debt_servicing_capacity_calc005_42d_base_v005_signal(currentratio, debt):
    res = (currentratio / debt).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc005_42d_base_v005_signal'] = f58ds_f58_debt_servicing_capacity_calc005_42d_base_v005_signal

def f58ds_f58_debt_servicing_capacity_calc006_5d_base_v006_signal(debt, ebitda):
    res = (debt / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc006_5d_base_v006_signal'] = f58ds_f58_debt_servicing_capacity_calc006_5d_base_v006_signal

def f58ds_f58_debt_servicing_capacity_calc007_63d_base_v007_signal(debt, marketcap):
    res = (debt / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc007_63d_base_v007_signal'] = f58ds_f58_debt_servicing_capacity_calc007_63d_base_v007_signal

def f58ds_f58_debt_servicing_capacity_calc008_10d_base_v008_signal(debt, gp):
    res = np.log(((debt / gp)).abs().replace(0, np.nan)).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc008_10d_base_v008_signal'] = f58ds_f58_debt_servicing_capacity_calc008_10d_base_v008_signal

def f58ds_f58_debt_servicing_capacity_calc009_42d_base_v009_signal(debt, marketcap):
    res = (debt / marketcap).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc009_42d_base_v009_signal'] = f58ds_f58_debt_servicing_capacity_calc009_42d_base_v009_signal

def f58ds_f58_debt_servicing_capacity_calc010_252d_base_v010_signal(debt, workingcapital):
    res = (debt / workingcapital).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc010_252d_base_v010_signal'] = f58ds_f58_debt_servicing_capacity_calc010_252d_base_v010_signal

def f58ds_f58_debt_servicing_capacity_calc011_252d_base_v011_signal(liabilities, netinc):
    res = (netinc / liabilities).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc011_252d_base_v011_signal'] = f58ds_f58_debt_servicing_capacity_calc011_252d_base_v011_signal

def f58ds_f58_debt_servicing_capacity_calc012_42d_base_v012_signal(ncfo, revenue):
    res = (((ncfo / revenue)) - ((ncfo / revenue)).rolling(42).mean()) / ((ncfo / revenue)).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc012_42d_base_v012_signal'] = f58ds_f58_debt_servicing_capacity_calc012_42d_base_v012_signal

def f58ds_f58_debt_servicing_capacity_calc013_10d_base_v013_signal(ebitda, ev):
    res = (ev / ebitda).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc013_10d_base_v013_signal'] = f58ds_f58_debt_servicing_capacity_calc013_10d_base_v013_signal

def f58ds_f58_debt_servicing_capacity_calc014_21d_base_v014_signal(liabilities, netinc):
    res = (netinc / liabilities).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc014_21d_base_v014_signal'] = f58ds_f58_debt_servicing_capacity_calc014_21d_base_v014_signal

def f58ds_f58_debt_servicing_capacity_calc015_42d_base_v015_signal(ebitda, intexp):
    res = (ebitda / intexp).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc015_42d_base_v015_signal'] = f58ds_f58_debt_servicing_capacity_calc015_42d_base_v015_signal

def f58ds_f58_debt_servicing_capacity_calc016_252d_base_v016_signal(fcf, intexp):
    res = (((fcf / intexp)) / ((fcf / intexp)).rolling(252).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc016_252d_base_v016_signal'] = f58ds_f58_debt_servicing_capacity_calc016_252d_base_v016_signal

def f58ds_f58_debt_servicing_capacity_calc017_21d_base_v017_signal(liabilities, revenue):
    res = (liabilities / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc017_21d_base_v017_signal'] = f58ds_f58_debt_servicing_capacity_calc017_21d_base_v017_signal

def f58ds_f58_debt_servicing_capacity_calc018_42d_base_v018_signal(liabilities, opinc):
    res = (opinc / liabilities).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc018_42d_base_v018_signal'] = f58ds_f58_debt_servicing_capacity_calc018_42d_base_v018_signal

def f58ds_f58_debt_servicing_capacity_calc019_42d_base_v019_signal(debt, gp):
    res = (gp / debt).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc019_42d_base_v019_signal'] = f58ds_f58_debt_servicing_capacity_calc019_42d_base_v019_signal

def f58ds_f58_debt_servicing_capacity_calc020_21d_base_v020_signal(debt, gp):
    res = (((debt / gp)) / ((debt / gp)).rolling(21).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc020_21d_base_v020_signal'] = f58ds_f58_debt_servicing_capacity_calc020_21d_base_v020_signal

def f58ds_f58_debt_servicing_capacity_calc021_10d_base_v021_signal(currentratio, debt):
    res = (currentratio / debt).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc021_10d_base_v021_signal'] = f58ds_f58_debt_servicing_capacity_calc021_10d_base_v021_signal

def f58ds_f58_debt_servicing_capacity_calc022_126d_base_v022_signal(debt, equity):
    res = (debt / equity).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc022_126d_base_v022_signal'] = f58ds_f58_debt_servicing_capacity_calc022_126d_base_v022_signal

def f58ds_f58_debt_servicing_capacity_calc023_21d_base_v023_signal(liabilities, netinc):
    res = (netinc / liabilities).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc023_21d_base_v023_signal'] = f58ds_f58_debt_servicing_capacity_calc023_21d_base_v023_signal

def f58ds_f58_debt_servicing_capacity_calc024_10d_base_v024_signal(ebitda, liabilities):
    res = (liabilities / ebitda).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc024_10d_base_v024_signal'] = f58ds_f58_debt_servicing_capacity_calc024_10d_base_v024_signal

def f58ds_f58_debt_servicing_capacity_calc025_21d_base_v025_signal(intexp, netinc):
    res = (netinc / intexp).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc025_21d_base_v025_signal'] = f58ds_f58_debt_servicing_capacity_calc025_21d_base_v025_signal

def f58ds_f58_debt_servicing_capacity_calc026_252d_base_v026_signal(assets, ebitda):
    res = (((ebitda / assets)) / ((ebitda / assets)).rolling(252).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc026_252d_base_v026_signal'] = f58ds_f58_debt_servicing_capacity_calc026_252d_base_v026_signal

def f58ds_f58_debt_servicing_capacity_calc027_21d_base_v027_signal(debt, ncfo):
    res = (((ncfo / debt)) / ((ncfo / debt)).rolling(21).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc027_21d_base_v027_signal'] = f58ds_f58_debt_servicing_capacity_calc027_21d_base_v027_signal

def f58ds_f58_debt_servicing_capacity_calc028_126d_base_v028_signal(assets, debt):
    res = (debt / assets).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc028_126d_base_v028_signal'] = f58ds_f58_debt_servicing_capacity_calc028_126d_base_v028_signal

def f58ds_f58_debt_servicing_capacity_calc029_126d_base_v029_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc029_126d_base_v029_signal'] = f58ds_f58_debt_servicing_capacity_calc029_126d_base_v029_signal

def f58ds_f58_debt_servicing_capacity_calc030_126d_base_v030_signal(liabilities, revenue):
    res = (liabilities / revenue).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc030_126d_base_v030_signal'] = f58ds_f58_debt_servicing_capacity_calc030_126d_base_v030_signal

def f58ds_f58_debt_servicing_capacity_calc031_126d_base_v031_signal(debt, gp):
    res = (debt / gp).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc031_126d_base_v031_signal'] = f58ds_f58_debt_servicing_capacity_calc031_126d_base_v031_signal

def f58ds_f58_debt_servicing_capacity_calc032_42d_base_v032_signal(debt, ncfo):
    res = (((ncfo / debt)) / ((ncfo / debt)).rolling(42).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc032_42d_base_v032_signal'] = f58ds_f58_debt_servicing_capacity_calc032_42d_base_v032_signal

def f58ds_f58_debt_servicing_capacity_calc033_126d_base_v033_signal(ebitda, ev):
    res = (ev / ebitda).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc033_126d_base_v033_signal'] = f58ds_f58_debt_servicing_capacity_calc033_126d_base_v033_signal

def f58ds_f58_debt_servicing_capacity_calc034_21d_base_v034_signal(assets, fcf):
    res = (fcf / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc034_21d_base_v034_signal'] = f58ds_f58_debt_servicing_capacity_calc034_21d_base_v034_signal

def f58ds_f58_debt_servicing_capacity_calc035_252d_base_v035_signal(debt, marketcap):
    res = (debt / marketcap).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc035_252d_base_v035_signal'] = f58ds_f58_debt_servicing_capacity_calc035_252d_base_v035_signal

def f58ds_f58_debt_servicing_capacity_calc036_21d_base_v036_signal(debt, workingcapital):
    res = (((debt / workingcapital)) / ((debt / workingcapital)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc036_21d_base_v036_signal'] = f58ds_f58_debt_servicing_capacity_calc036_21d_base_v036_signal

def f58ds_f58_debt_servicing_capacity_calc037_5d_base_v037_signal(ebitda, ev):
    res = (ev / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc037_5d_base_v037_signal'] = f58ds_f58_debt_servicing_capacity_calc037_5d_base_v037_signal

def f58ds_f58_debt_servicing_capacity_calc038_63d_base_v038_signal(debt, gp):
    res = (((gp / debt)) - ((gp / debt)).rolling(63).mean()) / ((gp / debt)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc038_63d_base_v038_signal'] = f58ds_f58_debt_servicing_capacity_calc038_63d_base_v038_signal

def f58ds_f58_debt_servicing_capacity_calc039_126d_base_v039_signal(assets, debt):
    res = (debt / assets).rolling(126).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc039_126d_base_v039_signal'] = f58ds_f58_debt_servicing_capacity_calc039_126d_base_v039_signal

def f58ds_f58_debt_servicing_capacity_calc040_126d_base_v040_signal(intexp, netinc):
    res = (netinc / intexp).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc040_126d_base_v040_signal'] = f58ds_f58_debt_servicing_capacity_calc040_126d_base_v040_signal

def f58ds_f58_debt_servicing_capacity_calc041_21d_base_v041_signal(debt, fcf):
    res = (fcf / debt).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc041_21d_base_v041_signal'] = f58ds_f58_debt_servicing_capacity_calc041_21d_base_v041_signal

def f58ds_f58_debt_servicing_capacity_calc042_126d_base_v042_signal(debt, marketcap):
    res = (debt / marketcap).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc042_126d_base_v042_signal'] = f58ds_f58_debt_servicing_capacity_calc042_126d_base_v042_signal

def f58ds_f58_debt_servicing_capacity_calc043_63d_base_v043_signal(liabilities, opinc):
    res = np.log(((opinc / liabilities)).abs().replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc043_63d_base_v043_signal'] = f58ds_f58_debt_servicing_capacity_calc043_63d_base_v043_signal

def f58ds_f58_debt_servicing_capacity_calc044_63d_base_v044_signal(assets, netinc):
    res = (((netinc / assets)) / ((netinc / assets)).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc044_63d_base_v044_signal'] = f58ds_f58_debt_servicing_capacity_calc044_63d_base_v044_signal

def f58ds_f58_debt_servicing_capacity_calc045_10d_base_v045_signal(fcf, intexp):
    res = (fcf / intexp).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc045_10d_base_v045_signal'] = f58ds_f58_debt_servicing_capacity_calc045_10d_base_v045_signal

def f58ds_f58_debt_servicing_capacity_calc046_42d_base_v046_signal(intexp, revenue):
    res = (intexp / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc046_42d_base_v046_signal'] = f58ds_f58_debt_servicing_capacity_calc046_42d_base_v046_signal

def f58ds_f58_debt_servicing_capacity_calc047_5d_base_v047_signal(liabilities, netinc):
    res = (netinc / liabilities).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc047_5d_base_v047_signal'] = f58ds_f58_debt_servicing_capacity_calc047_5d_base_v047_signal

def f58ds_f58_debt_servicing_capacity_calc048_126d_base_v048_signal(debt, fcf):
    res = (fcf / debt).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc048_126d_base_v048_signal'] = f58ds_f58_debt_servicing_capacity_calc048_126d_base_v048_signal

def f58ds_f58_debt_servicing_capacity_calc049_126d_base_v049_signal(debt, workingcapital):
    res = np.log(((debt / workingcapital)).abs().replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc049_126d_base_v049_signal'] = f58ds_f58_debt_servicing_capacity_calc049_126d_base_v049_signal

def f58ds_f58_debt_servicing_capacity_calc050_5d_base_v050_signal(liabilities, revenue):
    res = (((liabilities / revenue)) / ((liabilities / revenue)).rolling(5).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc050_5d_base_v050_signal'] = f58ds_f58_debt_servicing_capacity_calc050_5d_base_v050_signal

def f58ds_f58_debt_servicing_capacity_calc051_63d_base_v051_signal(intexp, netinc):
    res = (netinc / intexp).rolling(63).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc051_63d_base_v051_signal'] = f58ds_f58_debt_servicing_capacity_calc051_63d_base_v051_signal

def f58ds_f58_debt_servicing_capacity_calc052_21d_base_v052_signal(intexp, revenue):
    res = (intexp / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc052_21d_base_v052_signal'] = f58ds_f58_debt_servicing_capacity_calc052_21d_base_v052_signal

def f58ds_f58_debt_servicing_capacity_calc053_126d_base_v053_signal(assets, fcf):
    res = (fcf / assets).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc053_126d_base_v053_signal'] = f58ds_f58_debt_servicing_capacity_calc053_126d_base_v053_signal

def f58ds_f58_debt_servicing_capacity_calc054_63d_base_v054_signal(assets, fcf):
    res = (fcf / assets).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc054_63d_base_v054_signal'] = f58ds_f58_debt_servicing_capacity_calc054_63d_base_v054_signal

def f58ds_f58_debt_servicing_capacity_calc055_126d_base_v055_signal(liabilities, netinc):
    res = (((netinc / liabilities)) - ((netinc / liabilities)).rolling(126).mean()) / ((netinc / liabilities)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc055_126d_base_v055_signal'] = f58ds_f58_debt_servicing_capacity_calc055_126d_base_v055_signal

def f58ds_f58_debt_servicing_capacity_calc056_21d_base_v056_signal(intexp, opinc):
    res = np.log(((opinc / intexp)).abs().replace(0, np.nan)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc056_21d_base_v056_signal'] = f58ds_f58_debt_servicing_capacity_calc056_21d_base_v056_signal

def f58ds_f58_debt_servicing_capacity_calc057_42d_base_v057_signal(debt, ncfo):
    res = (ncfo / debt).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc057_42d_base_v057_signal'] = f58ds_f58_debt_servicing_capacity_calc057_42d_base_v057_signal

def f58ds_f58_debt_servicing_capacity_calc058_126d_base_v058_signal(liabilities, opinc):
    res = (opinc / liabilities).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc058_126d_base_v058_signal'] = f58ds_f58_debt_servicing_capacity_calc058_126d_base_v058_signal

def f58ds_f58_debt_servicing_capacity_calc059_252d_base_v059_signal(intexp, revenue):
    res = (intexp / revenue).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc059_252d_base_v059_signal'] = f58ds_f58_debt_servicing_capacity_calc059_252d_base_v059_signal

def f58ds_f58_debt_servicing_capacity_calc060_5d_base_v060_signal(intexp, revenue):
    res = (intexp / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc060_5d_base_v060_signal'] = f58ds_f58_debt_servicing_capacity_calc060_5d_base_v060_signal

def f58ds_f58_debt_servicing_capacity_calc061_126d_base_v061_signal(intexp, opinc):
    res = (intexp / opinc).rolling(126).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc061_126d_base_v061_signal'] = f58ds_f58_debt_servicing_capacity_calc061_126d_base_v061_signal

def f58ds_f58_debt_servicing_capacity_calc062_10d_base_v062_signal(liabilities, revenue):
    res = (liabilities / revenue).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc062_10d_base_v062_signal'] = f58ds_f58_debt_servicing_capacity_calc062_10d_base_v062_signal

def f58ds_f58_debt_servicing_capacity_calc063_252d_base_v063_signal(fcf, intexp):
    res = (fcf / intexp).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc063_252d_base_v063_signal'] = f58ds_f58_debt_servicing_capacity_calc063_252d_base_v063_signal

def f58ds_f58_debt_servicing_capacity_calc064_252d_base_v064_signal(debt, gp):
    res = (debt / gp).rolling(252).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc064_252d_base_v064_signal'] = f58ds_f58_debt_servicing_capacity_calc064_252d_base_v064_signal

def f58ds_f58_debt_servicing_capacity_calc065_5d_base_v065_signal(debt, gp):
    res = (((gp / debt)) - ((gp / debt)).rolling(5).mean()) / ((gp / debt)).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc065_5d_base_v065_signal'] = f58ds_f58_debt_servicing_capacity_calc065_5d_base_v065_signal

def f58ds_f58_debt_servicing_capacity_calc066_5d_base_v066_signal(debt, revenue):
    res = (debt / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc066_5d_base_v066_signal'] = f58ds_f58_debt_servicing_capacity_calc066_5d_base_v066_signal

def f58ds_f58_debt_servicing_capacity_calc067_21d_base_v067_signal(debt, gp):
    res = (gp / debt).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc067_21d_base_v067_signal'] = f58ds_f58_debt_servicing_capacity_calc067_21d_base_v067_signal

def f58ds_f58_debt_servicing_capacity_calc068_5d_base_v068_signal(debt, marketcap):
    res = (debt / marketcap).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc068_5d_base_v068_signal'] = f58ds_f58_debt_servicing_capacity_calc068_5d_base_v068_signal

def f58ds_f58_debt_servicing_capacity_calc069_63d_base_v069_signal(assets, netinc):
    res = (netinc / assets).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc069_63d_base_v069_signal'] = f58ds_f58_debt_servicing_capacity_calc069_63d_base_v069_signal

def f58ds_f58_debt_servicing_capacity_calc070_126d_base_v070_signal(ebitda, intexp):
    res = (ebitda / intexp).rolling(126).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc070_126d_base_v070_signal'] = f58ds_f58_debt_servicing_capacity_calc070_126d_base_v070_signal

def f58ds_f58_debt_servicing_capacity_calc071_5d_base_v071_signal(intexp, opinc):
    res = (intexp / opinc).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc071_5d_base_v071_signal'] = f58ds_f58_debt_servicing_capacity_calc071_5d_base_v071_signal

def f58ds_f58_debt_servicing_capacity_calc072_126d_base_v072_signal(debt, fcf):
    res = (fcf / debt).rolling(126).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc072_126d_base_v072_signal'] = f58ds_f58_debt_servicing_capacity_calc072_126d_base_v072_signal

def f58ds_f58_debt_servicing_capacity_calc073_10d_base_v073_signal(debt, gp):
    res = (debt / gp).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc073_10d_base_v073_signal'] = f58ds_f58_debt_servicing_capacity_calc073_10d_base_v073_signal

def f58ds_f58_debt_servicing_capacity_calc074_252d_base_v074_signal(intexp, revenue):
    res = np.log(((intexp / revenue)).abs().replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc074_252d_base_v074_signal'] = f58ds_f58_debt_servicing_capacity_calc074_252d_base_v074_signal

def f58ds_f58_debt_servicing_capacity_calc075_63d_base_v075_signal(assets, debt):
    res = (debt / assets).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc075_63d_base_v075_signal'] = f58ds_f58_debt_servicing_capacity_calc075_63d_base_v075_signal



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
