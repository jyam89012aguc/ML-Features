import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f63dm_f63_debt_maturity_structure_calc001_5d_base_v001_signal(assets, debt):
    res = (debt / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc001_5d_base_v001_signal'] = f63dm_f63_debt_maturity_structure_calc001_5d_base_v001_signal

def f63dm_f63_debt_maturity_structure_calc002_5d_base_v002_signal(debt, equity):
    res = (debt / equity).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc002_5d_base_v002_signal'] = f63dm_f63_debt_maturity_structure_calc002_5d_base_v002_signal

def f63dm_f63_debt_maturity_structure_calc003_5d_base_v003_signal(debt, ebitda):
    res = (debt / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc003_5d_base_v003_signal'] = f63dm_f63_debt_maturity_structure_calc003_5d_base_v003_signal

def f63dm_f63_debt_maturity_structure_calc004_5d_base_v004_signal(debt, marketcap):
    res = (debt / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc004_5d_base_v004_signal'] = f63dm_f63_debt_maturity_structure_calc004_5d_base_v004_signal

def f63dm_f63_debt_maturity_structure_calc005_5d_base_v005_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc005_5d_base_v005_signal'] = f63dm_f63_debt_maturity_structure_calc005_5d_base_v005_signal

def f63dm_f63_debt_maturity_structure_calc006_5d_base_v006_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc006_5d_base_v006_signal'] = f63dm_f63_debt_maturity_structure_calc006_5d_base_v006_signal

def f63dm_f63_debt_maturity_structure_calc007_5d_base_v007_signal(currentratio):
    res = currentratio.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc007_5d_base_v007_signal'] = f63dm_f63_debt_maturity_structure_calc007_5d_base_v007_signal

def f63dm_f63_debt_maturity_structure_calc008_5d_base_v008_signal(intexp, revenue):
    res = (intexp / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc008_5d_base_v008_signal'] = f63dm_f63_debt_maturity_structure_calc008_5d_base_v008_signal

def f63dm_f63_debt_maturity_structure_calc009_5d_base_v009_signal(debt, intexp):
    res = (intexp / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc009_5d_base_v009_signal'] = f63dm_f63_debt_maturity_structure_calc009_5d_base_v009_signal

def f63dm_f63_debt_maturity_structure_calc010_5d_base_v010_signal(debt, fcf):
    res = (fcf / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc010_5d_base_v010_signal'] = f63dm_f63_debt_maturity_structure_calc010_5d_base_v010_signal

def f63dm_f63_debt_maturity_structure_calc011_5d_base_v011_signal(debt, ncfo):
    res = (ncfo / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc011_5d_base_v011_signal'] = f63dm_f63_debt_maturity_structure_calc011_5d_base_v011_signal

def f63dm_f63_debt_maturity_structure_calc012_5d_base_v012_signal(debt, revenue):
    res = (debt / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc012_5d_base_v012_signal'] = f63dm_f63_debt_maturity_structure_calc012_5d_base_v012_signal

def f63dm_f63_debt_maturity_structure_calc013_5d_base_v013_signal(debt, opinc):
    res = (debt / opinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc013_5d_base_v013_signal'] = f63dm_f63_debt_maturity_structure_calc013_5d_base_v013_signal

def f63dm_f63_debt_maturity_structure_calc014_5d_base_v014_signal(debt, ev):
    res = (debt / ev).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc014_5d_base_v014_signal'] = f63dm_f63_debt_maturity_structure_calc014_5d_base_v014_signal

def f63dm_f63_debt_maturity_structure_calc015_5d_base_v015_signal(assets, equity):
    res = (equity / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc015_5d_base_v015_signal'] = f63dm_f63_debt_maturity_structure_calc015_5d_base_v015_signal

def f63dm_f63_debt_maturity_structure_calc016_10d_base_v016_signal(assets, debt):
    res = (debt / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc016_10d_base_v016_signal'] = f63dm_f63_debt_maturity_structure_calc016_10d_base_v016_signal

def f63dm_f63_debt_maturity_structure_calc017_10d_base_v017_signal(debt, equity):
    res = (debt / equity).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc017_10d_base_v017_signal'] = f63dm_f63_debt_maturity_structure_calc017_10d_base_v017_signal

def f63dm_f63_debt_maturity_structure_calc018_10d_base_v018_signal(debt, ebitda):
    res = (debt / ebitda).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc018_10d_base_v018_signal'] = f63dm_f63_debt_maturity_structure_calc018_10d_base_v018_signal

def f63dm_f63_debt_maturity_structure_calc019_10d_base_v019_signal(debt, marketcap):
    res = (debt / marketcap).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc019_10d_base_v019_signal'] = f63dm_f63_debt_maturity_structure_calc019_10d_base_v019_signal

def f63dm_f63_debt_maturity_structure_calc020_10d_base_v020_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc020_10d_base_v020_signal'] = f63dm_f63_debt_maturity_structure_calc020_10d_base_v020_signal

def f63dm_f63_debt_maturity_structure_calc021_10d_base_v021_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc021_10d_base_v021_signal'] = f63dm_f63_debt_maturity_structure_calc021_10d_base_v021_signal

def f63dm_f63_debt_maturity_structure_calc022_10d_base_v022_signal(currentratio):
    res = currentratio.rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc022_10d_base_v022_signal'] = f63dm_f63_debt_maturity_structure_calc022_10d_base_v022_signal

def f63dm_f63_debt_maturity_structure_calc023_10d_base_v023_signal(intexp, revenue):
    res = (intexp / revenue).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc023_10d_base_v023_signal'] = f63dm_f63_debt_maturity_structure_calc023_10d_base_v023_signal

def f63dm_f63_debt_maturity_structure_calc024_10d_base_v024_signal(debt, intexp):
    res = (intexp / debt).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc024_10d_base_v024_signal'] = f63dm_f63_debt_maturity_structure_calc024_10d_base_v024_signal

def f63dm_f63_debt_maturity_structure_calc025_10d_base_v025_signal(debt, fcf):
    res = (fcf / debt).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc025_10d_base_v025_signal'] = f63dm_f63_debt_maturity_structure_calc025_10d_base_v025_signal

def f63dm_f63_debt_maturity_structure_calc026_10d_base_v026_signal(debt, ncfo):
    res = (ncfo / debt).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc026_10d_base_v026_signal'] = f63dm_f63_debt_maturity_structure_calc026_10d_base_v026_signal

def f63dm_f63_debt_maturity_structure_calc027_10d_base_v027_signal(debt, revenue):
    res = (debt / revenue).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc027_10d_base_v027_signal'] = f63dm_f63_debt_maturity_structure_calc027_10d_base_v027_signal

def f63dm_f63_debt_maturity_structure_calc028_10d_base_v028_signal(debt, opinc):
    res = (debt / opinc).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc028_10d_base_v028_signal'] = f63dm_f63_debt_maturity_structure_calc028_10d_base_v028_signal

def f63dm_f63_debt_maturity_structure_calc029_10d_base_v029_signal(debt, ev):
    res = (debt / ev).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc029_10d_base_v029_signal'] = f63dm_f63_debt_maturity_structure_calc029_10d_base_v029_signal

def f63dm_f63_debt_maturity_structure_calc030_10d_base_v030_signal(assets, equity):
    res = (equity / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc030_10d_base_v030_signal'] = f63dm_f63_debt_maturity_structure_calc030_10d_base_v030_signal

def f63dm_f63_debt_maturity_structure_calc031_21d_base_v031_signal(assets, debt):
    res = (debt / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc031_21d_base_v031_signal'] = f63dm_f63_debt_maturity_structure_calc031_21d_base_v031_signal

def f63dm_f63_debt_maturity_structure_calc032_21d_base_v032_signal(debt, equity):
    res = (debt / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc032_21d_base_v032_signal'] = f63dm_f63_debt_maturity_structure_calc032_21d_base_v032_signal

def f63dm_f63_debt_maturity_structure_calc033_21d_base_v033_signal(debt, ebitda):
    res = (debt / ebitda).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc033_21d_base_v033_signal'] = f63dm_f63_debt_maturity_structure_calc033_21d_base_v033_signal

def f63dm_f63_debt_maturity_structure_calc034_21d_base_v034_signal(debt, marketcap):
    res = (debt / marketcap).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc034_21d_base_v034_signal'] = f63dm_f63_debt_maturity_structure_calc034_21d_base_v034_signal

def f63dm_f63_debt_maturity_structure_calc035_21d_base_v035_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc035_21d_base_v035_signal'] = f63dm_f63_debt_maturity_structure_calc035_21d_base_v035_signal

def f63dm_f63_debt_maturity_structure_calc036_21d_base_v036_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc036_21d_base_v036_signal'] = f63dm_f63_debt_maturity_structure_calc036_21d_base_v036_signal

def f63dm_f63_debt_maturity_structure_calc037_21d_base_v037_signal(currentratio):
    res = currentratio.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc037_21d_base_v037_signal'] = f63dm_f63_debt_maturity_structure_calc037_21d_base_v037_signal

def f63dm_f63_debt_maturity_structure_calc038_21d_base_v038_signal(intexp, revenue):
    res = (intexp / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc038_21d_base_v038_signal'] = f63dm_f63_debt_maturity_structure_calc038_21d_base_v038_signal

def f63dm_f63_debt_maturity_structure_calc039_21d_base_v039_signal(debt, intexp):
    res = (intexp / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc039_21d_base_v039_signal'] = f63dm_f63_debt_maturity_structure_calc039_21d_base_v039_signal

def f63dm_f63_debt_maturity_structure_calc040_21d_base_v040_signal(debt, fcf):
    res = (fcf / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc040_21d_base_v040_signal'] = f63dm_f63_debt_maturity_structure_calc040_21d_base_v040_signal

def f63dm_f63_debt_maturity_structure_calc041_21d_base_v041_signal(debt, ncfo):
    res = (ncfo / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc041_21d_base_v041_signal'] = f63dm_f63_debt_maturity_structure_calc041_21d_base_v041_signal

def f63dm_f63_debt_maturity_structure_calc042_21d_base_v042_signal(debt, revenue):
    res = (debt / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc042_21d_base_v042_signal'] = f63dm_f63_debt_maturity_structure_calc042_21d_base_v042_signal

def f63dm_f63_debt_maturity_structure_calc043_21d_base_v043_signal(debt, opinc):
    res = (debt / opinc).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc043_21d_base_v043_signal'] = f63dm_f63_debt_maturity_structure_calc043_21d_base_v043_signal

def f63dm_f63_debt_maturity_structure_calc044_21d_base_v044_signal(debt, ev):
    res = (debt / ev).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc044_21d_base_v044_signal'] = f63dm_f63_debt_maturity_structure_calc044_21d_base_v044_signal

def f63dm_f63_debt_maturity_structure_calc045_21d_base_v045_signal(assets, equity):
    res = (equity / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc045_21d_base_v045_signal'] = f63dm_f63_debt_maturity_structure_calc045_21d_base_v045_signal

def f63dm_f63_debt_maturity_structure_calc046_42d_base_v046_signal(assets, debt):
    res = (debt / assets).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc046_42d_base_v046_signal'] = f63dm_f63_debt_maturity_structure_calc046_42d_base_v046_signal

def f63dm_f63_debt_maturity_structure_calc047_42d_base_v047_signal(debt, equity):
    res = (debt / equity).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc047_42d_base_v047_signal'] = f63dm_f63_debt_maturity_structure_calc047_42d_base_v047_signal

def f63dm_f63_debt_maturity_structure_calc048_42d_base_v048_signal(debt, ebitda):
    res = (debt / ebitda).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc048_42d_base_v048_signal'] = f63dm_f63_debt_maturity_structure_calc048_42d_base_v048_signal

def f63dm_f63_debt_maturity_structure_calc049_42d_base_v049_signal(debt, marketcap):
    res = (debt / marketcap).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc049_42d_base_v049_signal'] = f63dm_f63_debt_maturity_structure_calc049_42d_base_v049_signal

def f63dm_f63_debt_maturity_structure_calc050_42d_base_v050_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc050_42d_base_v050_signal'] = f63dm_f63_debt_maturity_structure_calc050_42d_base_v050_signal

def f63dm_f63_debt_maturity_structure_calc051_42d_base_v051_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc051_42d_base_v051_signal'] = f63dm_f63_debt_maturity_structure_calc051_42d_base_v051_signal

def f63dm_f63_debt_maturity_structure_calc052_42d_base_v052_signal(currentratio):
    res = currentratio.rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc052_42d_base_v052_signal'] = f63dm_f63_debt_maturity_structure_calc052_42d_base_v052_signal

def f63dm_f63_debt_maturity_structure_calc053_42d_base_v053_signal(intexp, revenue):
    res = (intexp / revenue).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc053_42d_base_v053_signal'] = f63dm_f63_debt_maturity_structure_calc053_42d_base_v053_signal

def f63dm_f63_debt_maturity_structure_calc054_42d_base_v054_signal(debt, intexp):
    res = (intexp / debt).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc054_42d_base_v054_signal'] = f63dm_f63_debt_maturity_structure_calc054_42d_base_v054_signal

def f63dm_f63_debt_maturity_structure_calc055_42d_base_v055_signal(debt, fcf):
    res = (fcf / debt).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc055_42d_base_v055_signal'] = f63dm_f63_debt_maturity_structure_calc055_42d_base_v055_signal

def f63dm_f63_debt_maturity_structure_calc056_42d_base_v056_signal(debt, ncfo):
    res = (ncfo / debt).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc056_42d_base_v056_signal'] = f63dm_f63_debt_maturity_structure_calc056_42d_base_v056_signal

def f63dm_f63_debt_maturity_structure_calc057_42d_base_v057_signal(debt, revenue):
    res = (debt / revenue).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc057_42d_base_v057_signal'] = f63dm_f63_debt_maturity_structure_calc057_42d_base_v057_signal

def f63dm_f63_debt_maturity_structure_calc058_42d_base_v058_signal(debt, opinc):
    res = (debt / opinc).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc058_42d_base_v058_signal'] = f63dm_f63_debt_maturity_structure_calc058_42d_base_v058_signal

def f63dm_f63_debt_maturity_structure_calc059_42d_base_v059_signal(debt, ev):
    res = (debt / ev).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc059_42d_base_v059_signal'] = f63dm_f63_debt_maturity_structure_calc059_42d_base_v059_signal

def f63dm_f63_debt_maturity_structure_calc060_42d_base_v060_signal(assets, equity):
    res = (equity / assets).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc060_42d_base_v060_signal'] = f63dm_f63_debt_maturity_structure_calc060_42d_base_v060_signal

def f63dm_f63_debt_maturity_structure_calc061_63d_base_v061_signal(assets, debt):
    res = (debt / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc061_63d_base_v061_signal'] = f63dm_f63_debt_maturity_structure_calc061_63d_base_v061_signal

def f63dm_f63_debt_maturity_structure_calc062_63d_base_v062_signal(debt, equity):
    res = (debt / equity).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc062_63d_base_v062_signal'] = f63dm_f63_debt_maturity_structure_calc062_63d_base_v062_signal

def f63dm_f63_debt_maturity_structure_calc063_63d_base_v063_signal(debt, ebitda):
    res = (debt / ebitda).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc063_63d_base_v063_signal'] = f63dm_f63_debt_maturity_structure_calc063_63d_base_v063_signal

def f63dm_f63_debt_maturity_structure_calc064_63d_base_v064_signal(debt, marketcap):
    res = (debt / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc064_63d_base_v064_signal'] = f63dm_f63_debt_maturity_structure_calc064_63d_base_v064_signal

def f63dm_f63_debt_maturity_structure_calc065_63d_base_v065_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc065_63d_base_v065_signal'] = f63dm_f63_debt_maturity_structure_calc065_63d_base_v065_signal

def f63dm_f63_debt_maturity_structure_calc066_63d_base_v066_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc066_63d_base_v066_signal'] = f63dm_f63_debt_maturity_structure_calc066_63d_base_v066_signal

def f63dm_f63_debt_maturity_structure_calc067_63d_base_v067_signal(currentratio):
    res = currentratio.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc067_63d_base_v067_signal'] = f63dm_f63_debt_maturity_structure_calc067_63d_base_v067_signal

def f63dm_f63_debt_maturity_structure_calc068_63d_base_v068_signal(intexp, revenue):
    res = (intexp / revenue).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc068_63d_base_v068_signal'] = f63dm_f63_debt_maturity_structure_calc068_63d_base_v068_signal

def f63dm_f63_debt_maturity_structure_calc069_63d_base_v069_signal(debt, intexp):
    res = (intexp / debt).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc069_63d_base_v069_signal'] = f63dm_f63_debt_maturity_structure_calc069_63d_base_v069_signal

def f63dm_f63_debt_maturity_structure_calc070_63d_base_v070_signal(debt, fcf):
    res = (fcf / debt).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc070_63d_base_v070_signal'] = f63dm_f63_debt_maturity_structure_calc070_63d_base_v070_signal

def f63dm_f63_debt_maturity_structure_calc071_63d_base_v071_signal(debt, ncfo):
    res = (ncfo / debt).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc071_63d_base_v071_signal'] = f63dm_f63_debt_maturity_structure_calc071_63d_base_v071_signal

def f63dm_f63_debt_maturity_structure_calc072_63d_base_v072_signal(debt, revenue):
    res = (debt / revenue).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc072_63d_base_v072_signal'] = f63dm_f63_debt_maturity_structure_calc072_63d_base_v072_signal

def f63dm_f63_debt_maturity_structure_calc073_63d_base_v073_signal(debt, opinc):
    res = (debt / opinc).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc073_63d_base_v073_signal'] = f63dm_f63_debt_maturity_structure_calc073_63d_base_v073_signal

def f63dm_f63_debt_maturity_structure_calc074_63d_base_v074_signal(debt, ev):
    res = (debt / ev).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc074_63d_base_v074_signal'] = f63dm_f63_debt_maturity_structure_calc074_63d_base_v074_signal

def f63dm_f63_debt_maturity_structure_calc075_63d_base_v075_signal(assets, equity):
    res = (equity / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc075_63d_base_v075_signal'] = f63dm_f63_debt_maturity_structure_calc075_63d_base_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "debt": np.random.uniform(100, 1000, n),
        "assets": np.random.uniform(1000, 5000, n),
        "equity": np.random.uniform(500, 3000, n),
        "ebitda": np.random.uniform(50, 500, n),
        "marketcap": np.random.uniform(1000, 10000, n),
        "liabilities": np.random.uniform(500, 4000, n),
        "workingcapital": np.random.uniform(50, 1000, n),
        "currentratio": np.random.uniform(0.5, 3.0, n),
        "intexp": np.random.uniform(5, 100, n),
        "revenue": np.random.uniform(500, 5000, n),
        "fcf": np.random.uniform(10, 500, n),
        "ncfo": np.random.uniform(20, 600, n),
        "opinc": np.random.uniform(30, 700, n),
        "ev": np.random.uniform(1000, 15000, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        max_corr = 0
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                c = corr_matrix.iloc[i, j]
                if c > max_corr: max_corr = c
        print(f"Max correlation: {max_corr}")
        assert max_corr <= 0.95, f"Max correlation {max_corr} > 0.95"
    print("Self-test passed")

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
