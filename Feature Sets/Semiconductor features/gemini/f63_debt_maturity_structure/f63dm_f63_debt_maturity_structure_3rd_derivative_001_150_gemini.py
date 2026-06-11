import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f63dm_f63_debt_maturity_structure_calc001_5d_3rd_v001_signal(assets, debt):
    res = ((debt / assets).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc001_5d_3rd_v001_signal"] = f63dm_f63_debt_maturity_structure_calc001_5d_3rd_v001_signal

def f63dm_f63_debt_maturity_structure_calc002_5d_3rd_v002_signal(debt, equity):
    res = ((debt / equity).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc002_5d_3rd_v002_signal"] = f63dm_f63_debt_maturity_structure_calc002_5d_3rd_v002_signal

def f63dm_f63_debt_maturity_structure_calc003_5d_3rd_v003_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc003_5d_3rd_v003_signal"] = f63dm_f63_debt_maturity_structure_calc003_5d_3rd_v003_signal

def f63dm_f63_debt_maturity_structure_calc004_5d_3rd_v004_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc004_5d_3rd_v004_signal"] = f63dm_f63_debt_maturity_structure_calc004_5d_3rd_v004_signal

def f63dm_f63_debt_maturity_structure_calc005_5d_3rd_v005_signal(assets, liabilities):
    res = ((liabilities / assets).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc005_5d_3rd_v005_signal"] = f63dm_f63_debt_maturity_structure_calc005_5d_3rd_v005_signal

def f63dm_f63_debt_maturity_structure_calc006_5d_3rd_v006_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc006_5d_3rd_v006_signal"] = f63dm_f63_debt_maturity_structure_calc006_5d_3rd_v006_signal

def f63dm_f63_debt_maturity_structure_calc007_5d_3rd_v007_signal(currentratio):
    res = (currentratio.rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc007_5d_3rd_v007_signal"] = f63dm_f63_debt_maturity_structure_calc007_5d_3rd_v007_signal

def f63dm_f63_debt_maturity_structure_calc008_5d_3rd_v008_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc008_5d_3rd_v008_signal"] = f63dm_f63_debt_maturity_structure_calc008_5d_3rd_v008_signal

def f63dm_f63_debt_maturity_structure_calc009_5d_3rd_v009_signal(debt, intexp):
    res = ((intexp / debt).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc009_5d_3rd_v009_signal"] = f63dm_f63_debt_maturity_structure_calc009_5d_3rd_v009_signal

def f63dm_f63_debt_maturity_structure_calc010_5d_3rd_v010_signal(debt, fcf):
    res = ((fcf / debt).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc010_5d_3rd_v010_signal"] = f63dm_f63_debt_maturity_structure_calc010_5d_3rd_v010_signal

def f63dm_f63_debt_maturity_structure_calc011_5d_3rd_v011_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc011_5d_3rd_v011_signal"] = f63dm_f63_debt_maturity_structure_calc011_5d_3rd_v011_signal

def f63dm_f63_debt_maturity_structure_calc012_5d_3rd_v012_signal(debt, revenue):
    res = ((debt / revenue).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc012_5d_3rd_v012_signal"] = f63dm_f63_debt_maturity_structure_calc012_5d_3rd_v012_signal

def f63dm_f63_debt_maturity_structure_calc013_5d_3rd_v013_signal(debt, opinc):
    res = ((debt / opinc).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc013_5d_3rd_v013_signal"] = f63dm_f63_debt_maturity_structure_calc013_5d_3rd_v013_signal

def f63dm_f63_debt_maturity_structure_calc014_5d_3rd_v014_signal(debt, ev):
    res = ((debt / ev).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc014_5d_3rd_v014_signal"] = f63dm_f63_debt_maturity_structure_calc014_5d_3rd_v014_signal

def f63dm_f63_debt_maturity_structure_calc015_5d_3rd_v015_signal(assets, equity):
    res = ((equity / assets).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc015_5d_3rd_v015_signal"] = f63dm_f63_debt_maturity_structure_calc015_5d_3rd_v015_signal

def f63dm_f63_debt_maturity_structure_calc016_10d_3rd_v016_signal(assets, debt):
    res = ((debt / assets).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc016_10d_3rd_v016_signal"] = f63dm_f63_debt_maturity_structure_calc016_10d_3rd_v016_signal

def f63dm_f63_debt_maturity_structure_calc017_10d_3rd_v017_signal(debt, equity):
    res = ((debt / equity).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc017_10d_3rd_v017_signal"] = f63dm_f63_debt_maturity_structure_calc017_10d_3rd_v017_signal

def f63dm_f63_debt_maturity_structure_calc018_10d_3rd_v018_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc018_10d_3rd_v018_signal"] = f63dm_f63_debt_maturity_structure_calc018_10d_3rd_v018_signal

def f63dm_f63_debt_maturity_structure_calc019_10d_3rd_v019_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc019_10d_3rd_v019_signal"] = f63dm_f63_debt_maturity_structure_calc019_10d_3rd_v019_signal

def f63dm_f63_debt_maturity_structure_calc020_10d_3rd_v020_signal(assets, liabilities):
    res = ((liabilities / assets).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc020_10d_3rd_v020_signal"] = f63dm_f63_debt_maturity_structure_calc020_10d_3rd_v020_signal

def f63dm_f63_debt_maturity_structure_calc021_10d_3rd_v021_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc021_10d_3rd_v021_signal"] = f63dm_f63_debt_maturity_structure_calc021_10d_3rd_v021_signal

def f63dm_f63_debt_maturity_structure_calc022_10d_3rd_v022_signal(currentratio):
    res = (currentratio.rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc022_10d_3rd_v022_signal"] = f63dm_f63_debt_maturity_structure_calc022_10d_3rd_v022_signal

def f63dm_f63_debt_maturity_structure_calc023_10d_3rd_v023_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc023_10d_3rd_v023_signal"] = f63dm_f63_debt_maturity_structure_calc023_10d_3rd_v023_signal

def f63dm_f63_debt_maturity_structure_calc024_10d_3rd_v024_signal(debt, intexp):
    res = ((intexp / debt).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc024_10d_3rd_v024_signal"] = f63dm_f63_debt_maturity_structure_calc024_10d_3rd_v024_signal

def f63dm_f63_debt_maturity_structure_calc025_10d_3rd_v025_signal(debt, fcf):
    res = ((fcf / debt).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc025_10d_3rd_v025_signal"] = f63dm_f63_debt_maturity_structure_calc025_10d_3rd_v025_signal

def f63dm_f63_debt_maturity_structure_calc026_10d_3rd_v026_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc026_10d_3rd_v026_signal"] = f63dm_f63_debt_maturity_structure_calc026_10d_3rd_v026_signal

def f63dm_f63_debt_maturity_structure_calc027_10d_3rd_v027_signal(debt, revenue):
    res = ((debt / revenue).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc027_10d_3rd_v027_signal"] = f63dm_f63_debt_maturity_structure_calc027_10d_3rd_v027_signal

def f63dm_f63_debt_maturity_structure_calc028_10d_3rd_v028_signal(debt, opinc):
    res = ((debt / opinc).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc028_10d_3rd_v028_signal"] = f63dm_f63_debt_maturity_structure_calc028_10d_3rd_v028_signal

def f63dm_f63_debt_maturity_structure_calc029_10d_3rd_v029_signal(debt, ev):
    res = ((debt / ev).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc029_10d_3rd_v029_signal"] = f63dm_f63_debt_maturity_structure_calc029_10d_3rd_v029_signal

def f63dm_f63_debt_maturity_structure_calc030_10d_3rd_v030_signal(assets, equity):
    res = ((equity / assets).rolling(10).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc030_10d_3rd_v030_signal"] = f63dm_f63_debt_maturity_structure_calc030_10d_3rd_v030_signal

def f63dm_f63_debt_maturity_structure_calc031_21d_3rd_v031_signal(assets, debt):
    res = ((debt / assets).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc031_21d_3rd_v031_signal"] = f63dm_f63_debt_maturity_structure_calc031_21d_3rd_v031_signal

def f63dm_f63_debt_maturity_structure_calc032_21d_3rd_v032_signal(debt, equity):
    res = ((debt / equity).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc032_21d_3rd_v032_signal"] = f63dm_f63_debt_maturity_structure_calc032_21d_3rd_v032_signal

def f63dm_f63_debt_maturity_structure_calc033_21d_3rd_v033_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc033_21d_3rd_v033_signal"] = f63dm_f63_debt_maturity_structure_calc033_21d_3rd_v033_signal

def f63dm_f63_debt_maturity_structure_calc034_21d_3rd_v034_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc034_21d_3rd_v034_signal"] = f63dm_f63_debt_maturity_structure_calc034_21d_3rd_v034_signal

def f63dm_f63_debt_maturity_structure_calc035_21d_3rd_v035_signal(assets, liabilities):
    res = ((liabilities / assets).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc035_21d_3rd_v035_signal"] = f63dm_f63_debt_maturity_structure_calc035_21d_3rd_v035_signal

def f63dm_f63_debt_maturity_structure_calc036_21d_3rd_v036_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc036_21d_3rd_v036_signal"] = f63dm_f63_debt_maturity_structure_calc036_21d_3rd_v036_signal

def f63dm_f63_debt_maturity_structure_calc037_21d_3rd_v037_signal(currentratio):
    res = (currentratio.rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc037_21d_3rd_v037_signal"] = f63dm_f63_debt_maturity_structure_calc037_21d_3rd_v037_signal

def f63dm_f63_debt_maturity_structure_calc038_21d_3rd_v038_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc038_21d_3rd_v038_signal"] = f63dm_f63_debt_maturity_structure_calc038_21d_3rd_v038_signal

def f63dm_f63_debt_maturity_structure_calc039_21d_3rd_v039_signal(debt, intexp):
    res = ((intexp / debt).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc039_21d_3rd_v039_signal"] = f63dm_f63_debt_maturity_structure_calc039_21d_3rd_v039_signal

def f63dm_f63_debt_maturity_structure_calc040_21d_3rd_v040_signal(debt, fcf):
    res = ((fcf / debt).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc040_21d_3rd_v040_signal"] = f63dm_f63_debt_maturity_structure_calc040_21d_3rd_v040_signal

def f63dm_f63_debt_maturity_structure_calc041_21d_3rd_v041_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc041_21d_3rd_v041_signal"] = f63dm_f63_debt_maturity_structure_calc041_21d_3rd_v041_signal

def f63dm_f63_debt_maturity_structure_calc042_21d_3rd_v042_signal(debt, revenue):
    res = ((debt / revenue).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc042_21d_3rd_v042_signal"] = f63dm_f63_debt_maturity_structure_calc042_21d_3rd_v042_signal

def f63dm_f63_debt_maturity_structure_calc043_21d_3rd_v043_signal(debt, opinc):
    res = ((debt / opinc).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc043_21d_3rd_v043_signal"] = f63dm_f63_debt_maturity_structure_calc043_21d_3rd_v043_signal

def f63dm_f63_debt_maturity_structure_calc044_21d_3rd_v044_signal(debt, ev):
    res = ((debt / ev).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc044_21d_3rd_v044_signal"] = f63dm_f63_debt_maturity_structure_calc044_21d_3rd_v044_signal

def f63dm_f63_debt_maturity_structure_calc045_21d_3rd_v045_signal(assets, equity):
    res = ((equity / assets).rolling(21).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc045_21d_3rd_v045_signal"] = f63dm_f63_debt_maturity_structure_calc045_21d_3rd_v045_signal

def f63dm_f63_debt_maturity_structure_calc046_42d_3rd_v046_signal(assets, debt):
    res = ((debt / assets).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc046_42d_3rd_v046_signal"] = f63dm_f63_debt_maturity_structure_calc046_42d_3rd_v046_signal

def f63dm_f63_debt_maturity_structure_calc047_42d_3rd_v047_signal(debt, equity):
    res = ((debt / equity).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc047_42d_3rd_v047_signal"] = f63dm_f63_debt_maturity_structure_calc047_42d_3rd_v047_signal

def f63dm_f63_debt_maturity_structure_calc048_42d_3rd_v048_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc048_42d_3rd_v048_signal"] = f63dm_f63_debt_maturity_structure_calc048_42d_3rd_v048_signal

def f63dm_f63_debt_maturity_structure_calc049_42d_3rd_v049_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc049_42d_3rd_v049_signal"] = f63dm_f63_debt_maturity_structure_calc049_42d_3rd_v049_signal

def f63dm_f63_debt_maturity_structure_calc050_42d_3rd_v050_signal(assets, liabilities):
    res = ((liabilities / assets).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc050_42d_3rd_v050_signal"] = f63dm_f63_debt_maturity_structure_calc050_42d_3rd_v050_signal

def f63dm_f63_debt_maturity_structure_calc051_42d_3rd_v051_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc051_42d_3rd_v051_signal"] = f63dm_f63_debt_maturity_structure_calc051_42d_3rd_v051_signal

def f63dm_f63_debt_maturity_structure_calc052_42d_3rd_v052_signal(currentratio):
    res = (currentratio.rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc052_42d_3rd_v052_signal"] = f63dm_f63_debt_maturity_structure_calc052_42d_3rd_v052_signal

def f63dm_f63_debt_maturity_structure_calc053_42d_3rd_v053_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc053_42d_3rd_v053_signal"] = f63dm_f63_debt_maturity_structure_calc053_42d_3rd_v053_signal

def f63dm_f63_debt_maturity_structure_calc054_42d_3rd_v054_signal(debt, intexp):
    res = ((intexp / debt).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc054_42d_3rd_v054_signal"] = f63dm_f63_debt_maturity_structure_calc054_42d_3rd_v054_signal

def f63dm_f63_debt_maturity_structure_calc055_42d_3rd_v055_signal(debt, fcf):
    res = ((fcf / debt).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc055_42d_3rd_v055_signal"] = f63dm_f63_debt_maturity_structure_calc055_42d_3rd_v055_signal

def f63dm_f63_debt_maturity_structure_calc056_42d_3rd_v056_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc056_42d_3rd_v056_signal"] = f63dm_f63_debt_maturity_structure_calc056_42d_3rd_v056_signal

def f63dm_f63_debt_maturity_structure_calc057_42d_3rd_v057_signal(debt, revenue):
    res = ((debt / revenue).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc057_42d_3rd_v057_signal"] = f63dm_f63_debt_maturity_structure_calc057_42d_3rd_v057_signal

def f63dm_f63_debt_maturity_structure_calc058_42d_3rd_v058_signal(debt, opinc):
    res = ((debt / opinc).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc058_42d_3rd_v058_signal"] = f63dm_f63_debt_maturity_structure_calc058_42d_3rd_v058_signal

def f63dm_f63_debt_maturity_structure_calc059_42d_3rd_v059_signal(debt, ev):
    res = ((debt / ev).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc059_42d_3rd_v059_signal"] = f63dm_f63_debt_maturity_structure_calc059_42d_3rd_v059_signal

def f63dm_f63_debt_maturity_structure_calc060_42d_3rd_v060_signal(assets, equity):
    res = ((equity / assets).rolling(42).mean()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc060_42d_3rd_v060_signal"] = f63dm_f63_debt_maturity_structure_calc060_42d_3rd_v060_signal

def f63dm_f63_debt_maturity_structure_calc061_63d_3rd_v061_signal(assets, debt):
    res = ((debt / assets).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc061_63d_3rd_v061_signal"] = f63dm_f63_debt_maturity_structure_calc061_63d_3rd_v061_signal

def f63dm_f63_debt_maturity_structure_calc062_63d_3rd_v062_signal(debt, equity):
    res = ((debt / equity).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc062_63d_3rd_v062_signal"] = f63dm_f63_debt_maturity_structure_calc062_63d_3rd_v062_signal

def f63dm_f63_debt_maturity_structure_calc063_63d_3rd_v063_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc063_63d_3rd_v063_signal"] = f63dm_f63_debt_maturity_structure_calc063_63d_3rd_v063_signal

def f63dm_f63_debt_maturity_structure_calc064_63d_3rd_v064_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc064_63d_3rd_v064_signal"] = f63dm_f63_debt_maturity_structure_calc064_63d_3rd_v064_signal

def f63dm_f63_debt_maturity_structure_calc065_63d_3rd_v065_signal(assets, liabilities):
    res = ((liabilities / assets).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc065_63d_3rd_v065_signal"] = f63dm_f63_debt_maturity_structure_calc065_63d_3rd_v065_signal

def f63dm_f63_debt_maturity_structure_calc066_63d_3rd_v066_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc066_63d_3rd_v066_signal"] = f63dm_f63_debt_maturity_structure_calc066_63d_3rd_v066_signal

def f63dm_f63_debt_maturity_structure_calc067_63d_3rd_v067_signal(currentratio):
    res = (currentratio.rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc067_63d_3rd_v067_signal"] = f63dm_f63_debt_maturity_structure_calc067_63d_3rd_v067_signal

def f63dm_f63_debt_maturity_structure_calc068_63d_3rd_v068_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc068_63d_3rd_v068_signal"] = f63dm_f63_debt_maturity_structure_calc068_63d_3rd_v068_signal

def f63dm_f63_debt_maturity_structure_calc069_63d_3rd_v069_signal(debt, intexp):
    res = ((intexp / debt).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc069_63d_3rd_v069_signal"] = f63dm_f63_debt_maturity_structure_calc069_63d_3rd_v069_signal

def f63dm_f63_debt_maturity_structure_calc070_63d_3rd_v070_signal(debt, fcf):
    res = ((fcf / debt).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc070_63d_3rd_v070_signal"] = f63dm_f63_debt_maturity_structure_calc070_63d_3rd_v070_signal

def f63dm_f63_debt_maturity_structure_calc071_63d_3rd_v071_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc071_63d_3rd_v071_signal"] = f63dm_f63_debt_maturity_structure_calc071_63d_3rd_v071_signal

def f63dm_f63_debt_maturity_structure_calc072_63d_3rd_v072_signal(debt, revenue):
    res = ((debt / revenue).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc072_63d_3rd_v072_signal"] = f63dm_f63_debt_maturity_structure_calc072_63d_3rd_v072_signal

def f63dm_f63_debt_maturity_structure_calc073_63d_3rd_v073_signal(debt, opinc):
    res = ((debt / opinc).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc073_63d_3rd_v073_signal"] = f63dm_f63_debt_maturity_structure_calc073_63d_3rd_v073_signal

def f63dm_f63_debt_maturity_structure_calc074_63d_3rd_v074_signal(debt, ev):
    res = ((debt / ev).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc074_63d_3rd_v074_signal"] = f63dm_f63_debt_maturity_structure_calc074_63d_3rd_v074_signal

def f63dm_f63_debt_maturity_structure_calc075_63d_3rd_v075_signal(assets, equity):
    res = ((equity / assets).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc075_63d_3rd_v075_signal"] = f63dm_f63_debt_maturity_structure_calc075_63d_3rd_v075_signal

def f63dm_f63_debt_maturity_structure_calc076_60d_3rd_v076_signal(assets, debt):
    res = ((debt / assets).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc076_60d_3rd_v076_signal"] = f63dm_f63_debt_maturity_structure_calc076_60d_3rd_v076_signal

def f63dm_f63_debt_maturity_structure_calc077_60d_3rd_v077_signal(debt, equity):
    res = ((debt / equity).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc077_60d_3rd_v077_signal"] = f63dm_f63_debt_maturity_structure_calc077_60d_3rd_v077_signal

def f63dm_f63_debt_maturity_structure_calc078_60d_3rd_v078_signal(debt, ebitda):
    res = ((debt / ebitda).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc078_60d_3rd_v078_signal"] = f63dm_f63_debt_maturity_structure_calc078_60d_3rd_v078_signal

def f63dm_f63_debt_maturity_structure_calc079_60d_3rd_v079_signal(debt, marketcap):
    res = ((debt / marketcap).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc079_60d_3rd_v079_signal"] = f63dm_f63_debt_maturity_structure_calc079_60d_3rd_v079_signal

def f63dm_f63_debt_maturity_structure_calc080_60d_3rd_v080_signal(assets, liabilities):
    res = ((liabilities / assets).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc080_60d_3rd_v080_signal"] = f63dm_f63_debt_maturity_structure_calc080_60d_3rd_v080_signal

def f63dm_f63_debt_maturity_structure_calc081_60d_3rd_v081_signal(debt, workingcapital):
    res = ((workingcapital / debt).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc081_60d_3rd_v081_signal"] = f63dm_f63_debt_maturity_structure_calc081_60d_3rd_v081_signal

def f63dm_f63_debt_maturity_structure_calc082_60d_3rd_v082_signal(currentratio):
    res = (currentratio.diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc082_60d_3rd_v082_signal"] = f63dm_f63_debt_maturity_structure_calc082_60d_3rd_v082_signal

def f63dm_f63_debt_maturity_structure_calc083_60d_3rd_v083_signal(intexp, revenue):
    res = ((intexp / revenue).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc083_60d_3rd_v083_signal"] = f63dm_f63_debt_maturity_structure_calc083_60d_3rd_v083_signal

def f63dm_f63_debt_maturity_structure_calc084_60d_3rd_v084_signal(debt, intexp):
    res = ((intexp / debt).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc084_60d_3rd_v084_signal"] = f63dm_f63_debt_maturity_structure_calc084_60d_3rd_v084_signal

def f63dm_f63_debt_maturity_structure_calc085_60d_3rd_v085_signal(debt, fcf):
    res = ((fcf / debt).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc085_60d_3rd_v085_signal"] = f63dm_f63_debt_maturity_structure_calc085_60d_3rd_v085_signal

def f63dm_f63_debt_maturity_structure_calc086_60d_3rd_v086_signal(debt, ncfo):
    res = ((ncfo / debt).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc086_60d_3rd_v086_signal"] = f63dm_f63_debt_maturity_structure_calc086_60d_3rd_v086_signal

def f63dm_f63_debt_maturity_structure_calc087_60d_3rd_v087_signal(debt, revenue):
    res = ((debt / revenue).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc087_60d_3rd_v087_signal"] = f63dm_f63_debt_maturity_structure_calc087_60d_3rd_v087_signal

def f63dm_f63_debt_maturity_structure_calc088_60d_3rd_v088_signal(debt, opinc):
    res = ((debt / opinc).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc088_60d_3rd_v088_signal"] = f63dm_f63_debt_maturity_structure_calc088_60d_3rd_v088_signal

def f63dm_f63_debt_maturity_structure_calc089_60d_3rd_v089_signal(debt, ev):
    res = ((debt / ev).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc089_60d_3rd_v089_signal"] = f63dm_f63_debt_maturity_structure_calc089_60d_3rd_v089_signal

def f63dm_f63_debt_maturity_structure_calc090_60d_3rd_v090_signal(assets, equity):
    res = ((equity / assets).diff(60)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc090_60d_3rd_v090_signal"] = f63dm_f63_debt_maturity_structure_calc090_60d_3rd_v090_signal

def f63dm_f63_debt_maturity_structure_calc091_120d_3rd_v091_signal(assets, debt):
    res = ((debt / assets).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc091_120d_3rd_v091_signal"] = f63dm_f63_debt_maturity_structure_calc091_120d_3rd_v091_signal

def f63dm_f63_debt_maturity_structure_calc092_120d_3rd_v092_signal(debt, equity):
    res = ((debt / equity).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc092_120d_3rd_v092_signal"] = f63dm_f63_debt_maturity_structure_calc092_120d_3rd_v092_signal

def f63dm_f63_debt_maturity_structure_calc093_120d_3rd_v093_signal(debt, ebitda):
    res = ((debt / ebitda).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc093_120d_3rd_v093_signal"] = f63dm_f63_debt_maturity_structure_calc093_120d_3rd_v093_signal

def f63dm_f63_debt_maturity_structure_calc094_120d_3rd_v094_signal(debt, marketcap):
    res = ((debt / marketcap).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc094_120d_3rd_v094_signal"] = f63dm_f63_debt_maturity_structure_calc094_120d_3rd_v094_signal

def f63dm_f63_debt_maturity_structure_calc095_120d_3rd_v095_signal(assets, liabilities):
    res = ((liabilities / assets).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc095_120d_3rd_v095_signal"] = f63dm_f63_debt_maturity_structure_calc095_120d_3rd_v095_signal

def f63dm_f63_debt_maturity_structure_calc096_120d_3rd_v096_signal(debt, workingcapital):
    res = ((workingcapital / debt).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc096_120d_3rd_v096_signal"] = f63dm_f63_debt_maturity_structure_calc096_120d_3rd_v096_signal

def f63dm_f63_debt_maturity_structure_calc097_120d_3rd_v097_signal(currentratio):
    res = (currentratio.diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc097_120d_3rd_v097_signal"] = f63dm_f63_debt_maturity_structure_calc097_120d_3rd_v097_signal

def f63dm_f63_debt_maturity_structure_calc098_120d_3rd_v098_signal(intexp, revenue):
    res = ((intexp / revenue).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc098_120d_3rd_v098_signal"] = f63dm_f63_debt_maturity_structure_calc098_120d_3rd_v098_signal

def f63dm_f63_debt_maturity_structure_calc099_120d_3rd_v099_signal(debt, intexp):
    res = ((intexp / debt).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc099_120d_3rd_v099_signal"] = f63dm_f63_debt_maturity_structure_calc099_120d_3rd_v099_signal

def f63dm_f63_debt_maturity_structure_calc100_120d_3rd_v100_signal(debt, fcf):
    res = ((fcf / debt).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc100_120d_3rd_v100_signal"] = f63dm_f63_debt_maturity_structure_calc100_120d_3rd_v100_signal

def f63dm_f63_debt_maturity_structure_calc101_120d_3rd_v101_signal(debt, ncfo):
    res = ((ncfo / debt).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc101_120d_3rd_v101_signal"] = f63dm_f63_debt_maturity_structure_calc101_120d_3rd_v101_signal

def f63dm_f63_debt_maturity_structure_calc102_120d_3rd_v102_signal(debt, revenue):
    res = ((debt / revenue).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc102_120d_3rd_v102_signal"] = f63dm_f63_debt_maturity_structure_calc102_120d_3rd_v102_signal

def f63dm_f63_debt_maturity_structure_calc103_120d_3rd_v103_signal(debt, opinc):
    res = ((debt / opinc).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc103_120d_3rd_v103_signal"] = f63dm_f63_debt_maturity_structure_calc103_120d_3rd_v103_signal

def f63dm_f63_debt_maturity_structure_calc104_120d_3rd_v104_signal(debt, ev):
    res = ((debt / ev).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc104_120d_3rd_v104_signal"] = f63dm_f63_debt_maturity_structure_calc104_120d_3rd_v104_signal

def f63dm_f63_debt_maturity_structure_calc105_120d_3rd_v105_signal(assets, equity):
    res = ((equity / assets).diff(120)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc105_120d_3rd_v105_signal"] = f63dm_f63_debt_maturity_structure_calc105_120d_3rd_v105_signal

def f63dm_f63_debt_maturity_structure_calc106_30d_3rd_v106_signal(assets, debt):
    res = ((debt / assets).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc106_30d_3rd_v106_signal"] = f63dm_f63_debt_maturity_structure_calc106_30d_3rd_v106_signal

def f63dm_f63_debt_maturity_structure_calc107_30d_3rd_v107_signal(debt, equity):
    res = ((debt / equity).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc107_30d_3rd_v107_signal"] = f63dm_f63_debt_maturity_structure_calc107_30d_3rd_v107_signal

def f63dm_f63_debt_maturity_structure_calc108_30d_3rd_v108_signal(debt, ebitda):
    res = ((debt / ebitda).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc108_30d_3rd_v108_signal"] = f63dm_f63_debt_maturity_structure_calc108_30d_3rd_v108_signal

def f63dm_f63_debt_maturity_structure_calc109_30d_3rd_v109_signal(debt, marketcap):
    res = ((debt / marketcap).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc109_30d_3rd_v109_signal"] = f63dm_f63_debt_maturity_structure_calc109_30d_3rd_v109_signal

def f63dm_f63_debt_maturity_structure_calc110_30d_3rd_v110_signal(assets, liabilities):
    res = ((liabilities / assets).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc110_30d_3rd_v110_signal"] = f63dm_f63_debt_maturity_structure_calc110_30d_3rd_v110_signal

def f63dm_f63_debt_maturity_structure_calc111_30d_3rd_v111_signal(debt, workingcapital):
    res = ((workingcapital / debt).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc111_30d_3rd_v111_signal"] = f63dm_f63_debt_maturity_structure_calc111_30d_3rd_v111_signal

def f63dm_f63_debt_maturity_structure_calc112_30d_3rd_v112_signal(currentratio):
    res = (currentratio.diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc112_30d_3rd_v112_signal"] = f63dm_f63_debt_maturity_structure_calc112_30d_3rd_v112_signal

def f63dm_f63_debt_maturity_structure_calc113_30d_3rd_v113_signal(intexp, revenue):
    res = ((intexp / revenue).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc113_30d_3rd_v113_signal"] = f63dm_f63_debt_maturity_structure_calc113_30d_3rd_v113_signal

def f63dm_f63_debt_maturity_structure_calc114_30d_3rd_v114_signal(debt, intexp):
    res = ((intexp / debt).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc114_30d_3rd_v114_signal"] = f63dm_f63_debt_maturity_structure_calc114_30d_3rd_v114_signal

def f63dm_f63_debt_maturity_structure_calc115_30d_3rd_v115_signal(debt, fcf):
    res = ((fcf / debt).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc115_30d_3rd_v115_signal"] = f63dm_f63_debt_maturity_structure_calc115_30d_3rd_v115_signal

def f63dm_f63_debt_maturity_structure_calc116_30d_3rd_v116_signal(debt, ncfo):
    res = ((ncfo / debt).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc116_30d_3rd_v116_signal"] = f63dm_f63_debt_maturity_structure_calc116_30d_3rd_v116_signal

def f63dm_f63_debt_maturity_structure_calc117_30d_3rd_v117_signal(debt, revenue):
    res = ((debt / revenue).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc117_30d_3rd_v117_signal"] = f63dm_f63_debt_maturity_structure_calc117_30d_3rd_v117_signal

def f63dm_f63_debt_maturity_structure_calc118_30d_3rd_v118_signal(debt, opinc):
    res = ((debt / opinc).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc118_30d_3rd_v118_signal"] = f63dm_f63_debt_maturity_structure_calc118_30d_3rd_v118_signal

def f63dm_f63_debt_maturity_structure_calc119_30d_3rd_v119_signal(debt, ev):
    res = ((debt / ev).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc119_30d_3rd_v119_signal"] = f63dm_f63_debt_maturity_structure_calc119_30d_3rd_v119_signal

def f63dm_f63_debt_maturity_structure_calc120_30d_3rd_v120_signal(assets, equity):
    res = ((equity / assets).diff(30)).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc120_30d_3rd_v120_signal"] = f63dm_f63_debt_maturity_structure_calc120_30d_3rd_v120_signal

def f63dm_f63_debt_maturity_structure_calc121_90d_3rd_v121_signal(assets, debt):
    res = ((debt / assets).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc121_90d_3rd_v121_signal"] = f63dm_f63_debt_maturity_structure_calc121_90d_3rd_v121_signal

def f63dm_f63_debt_maturity_structure_calc122_90d_3rd_v122_signal(debt, equity):
    res = ((debt / equity).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc122_90d_3rd_v122_signal"] = f63dm_f63_debt_maturity_structure_calc122_90d_3rd_v122_signal

def f63dm_f63_debt_maturity_structure_calc123_90d_3rd_v123_signal(debt, ebitda):
    res = ((debt / ebitda).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc123_90d_3rd_v123_signal"] = f63dm_f63_debt_maturity_structure_calc123_90d_3rd_v123_signal

def f63dm_f63_debt_maturity_structure_calc124_90d_3rd_v124_signal(debt, marketcap):
    res = ((debt / marketcap).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc124_90d_3rd_v124_signal"] = f63dm_f63_debt_maturity_structure_calc124_90d_3rd_v124_signal

def f63dm_f63_debt_maturity_structure_calc125_90d_3rd_v125_signal(assets, liabilities):
    res = ((liabilities / assets).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc125_90d_3rd_v125_signal"] = f63dm_f63_debt_maturity_structure_calc125_90d_3rd_v125_signal

def f63dm_f63_debt_maturity_structure_calc126_90d_3rd_v126_signal(debt, workingcapital):
    res = ((workingcapital / debt).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc126_90d_3rd_v126_signal"] = f63dm_f63_debt_maturity_structure_calc126_90d_3rd_v126_signal

def f63dm_f63_debt_maturity_structure_calc127_90d_3rd_v127_signal(currentratio):
    res = (currentratio.diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc127_90d_3rd_v127_signal"] = f63dm_f63_debt_maturity_structure_calc127_90d_3rd_v127_signal

def f63dm_f63_debt_maturity_structure_calc128_90d_3rd_v128_signal(intexp, revenue):
    res = ((intexp / revenue).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc128_90d_3rd_v128_signal"] = f63dm_f63_debt_maturity_structure_calc128_90d_3rd_v128_signal

def f63dm_f63_debt_maturity_structure_calc129_90d_3rd_v129_signal(debt, intexp):
    res = ((intexp / debt).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc129_90d_3rd_v129_signal"] = f63dm_f63_debt_maturity_structure_calc129_90d_3rd_v129_signal

def f63dm_f63_debt_maturity_structure_calc130_90d_3rd_v130_signal(debt, fcf):
    res = ((fcf / debt).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc130_90d_3rd_v130_signal"] = f63dm_f63_debt_maturity_structure_calc130_90d_3rd_v130_signal

def f63dm_f63_debt_maturity_structure_calc131_90d_3rd_v131_signal(debt, ncfo):
    res = ((ncfo / debt).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc131_90d_3rd_v131_signal"] = f63dm_f63_debt_maturity_structure_calc131_90d_3rd_v131_signal

def f63dm_f63_debt_maturity_structure_calc132_90d_3rd_v132_signal(debt, revenue):
    res = ((debt / revenue).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc132_90d_3rd_v132_signal"] = f63dm_f63_debt_maturity_structure_calc132_90d_3rd_v132_signal

def f63dm_f63_debt_maturity_structure_calc133_90d_3rd_v133_signal(debt, opinc):
    res = ((debt / opinc).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc133_90d_3rd_v133_signal"] = f63dm_f63_debt_maturity_structure_calc133_90d_3rd_v133_signal

def f63dm_f63_debt_maturity_structure_calc134_90d_3rd_v134_signal(debt, ev):
    res = ((debt / ev).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc134_90d_3rd_v134_signal"] = f63dm_f63_debt_maturity_structure_calc134_90d_3rd_v134_signal

def f63dm_f63_debt_maturity_structure_calc135_90d_3rd_v135_signal(assets, equity):
    res = ((equity / assets).diff(90)).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc135_90d_3rd_v135_signal"] = f63dm_f63_debt_maturity_structure_calc135_90d_3rd_v135_signal

def f63dm_f63_debt_maturity_structure_calc136_150d_3rd_v136_signal(assets, debt):
    res = ((debt / assets).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc136_150d_3rd_v136_signal"] = f63dm_f63_debt_maturity_structure_calc136_150d_3rd_v136_signal

def f63dm_f63_debt_maturity_structure_calc137_150d_3rd_v137_signal(debt, equity):
    res = ((debt / equity).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc137_150d_3rd_v137_signal"] = f63dm_f63_debt_maturity_structure_calc137_150d_3rd_v137_signal

def f63dm_f63_debt_maturity_structure_calc138_150d_3rd_v138_signal(debt, ebitda):
    res = ((debt / ebitda).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc138_150d_3rd_v138_signal"] = f63dm_f63_debt_maturity_structure_calc138_150d_3rd_v138_signal

def f63dm_f63_debt_maturity_structure_calc139_150d_3rd_v139_signal(debt, marketcap):
    res = ((debt / marketcap).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc139_150d_3rd_v139_signal"] = f63dm_f63_debt_maturity_structure_calc139_150d_3rd_v139_signal

def f63dm_f63_debt_maturity_structure_calc140_150d_3rd_v140_signal(assets, liabilities):
    res = ((liabilities / assets).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc140_150d_3rd_v140_signal"] = f63dm_f63_debt_maturity_structure_calc140_150d_3rd_v140_signal

def f63dm_f63_debt_maturity_structure_calc141_150d_3rd_v141_signal(debt, workingcapital):
    res = ((workingcapital / debt).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc141_150d_3rd_v141_signal"] = f63dm_f63_debt_maturity_structure_calc141_150d_3rd_v141_signal

def f63dm_f63_debt_maturity_structure_calc142_150d_3rd_v142_signal(currentratio):
    res = (currentratio.diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc142_150d_3rd_v142_signal"] = f63dm_f63_debt_maturity_structure_calc142_150d_3rd_v142_signal

def f63dm_f63_debt_maturity_structure_calc143_150d_3rd_v143_signal(intexp, revenue):
    res = ((intexp / revenue).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc143_150d_3rd_v143_signal"] = f63dm_f63_debt_maturity_structure_calc143_150d_3rd_v143_signal

def f63dm_f63_debt_maturity_structure_calc144_150d_3rd_v144_signal(debt, intexp):
    res = ((intexp / debt).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc144_150d_3rd_v144_signal"] = f63dm_f63_debt_maturity_structure_calc144_150d_3rd_v144_signal

def f63dm_f63_debt_maturity_structure_calc145_150d_3rd_v145_signal(debt, fcf):
    res = ((fcf / debt).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc145_150d_3rd_v145_signal"] = f63dm_f63_debt_maturity_structure_calc145_150d_3rd_v145_signal

def f63dm_f63_debt_maturity_structure_calc146_150d_3rd_v146_signal(debt, ncfo):
    res = ((ncfo / debt).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc146_150d_3rd_v146_signal"] = f63dm_f63_debt_maturity_structure_calc146_150d_3rd_v146_signal

def f63dm_f63_debt_maturity_structure_calc147_150d_3rd_v147_signal(debt, revenue):
    res = ((debt / revenue).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc147_150d_3rd_v147_signal"] = f63dm_f63_debt_maturity_structure_calc147_150d_3rd_v147_signal

def f63dm_f63_debt_maturity_structure_calc148_150d_3rd_v148_signal(debt, opinc):
    res = ((debt / opinc).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc148_150d_3rd_v148_signal"] = f63dm_f63_debt_maturity_structure_calc148_150d_3rd_v148_signal

def f63dm_f63_debt_maturity_structure_calc149_150d_3rd_v149_signal(debt, ev):
    res = ((debt / ev).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc149_150d_3rd_v149_signal"] = f63dm_f63_debt_maturity_structure_calc149_150d_3rd_v149_signal

def f63dm_f63_debt_maturity_structure_calc150_150d_3rd_v150_signal(assets, equity):
    res = ((equity / assets).diff(150)).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS["f63dm_f63_debt_maturity_structure_calc150_150d_3rd_v150_signal"] = f63dm_f63_debt_maturity_structure_calc150_150d_3rd_v150_signal

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
