import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f58ds_f58_debt_servicing_capacity_calc001_63d_slope_v001_signal(ebitda, liabilities):
    res = ((ebitda / liabilities).rolling(63).kurt()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc001_63d_slope_v001_signal'] = f58ds_f58_debt_servicing_capacity_calc001_63d_slope_v001_signal

def f58ds_f58_debt_servicing_capacity_calc002_42d_slope_v002_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(42).quantile(0.5)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc002_42d_slope_v002_signal'] = f58ds_f58_debt_servicing_capacity_calc002_42d_slope_v002_signal

def f58ds_f58_debt_servicing_capacity_calc003_5d_slope_v003_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(5).quantile(0.5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc003_5d_slope_v003_signal'] = f58ds_f58_debt_servicing_capacity_calc003_5d_slope_v003_signal

def f58ds_f58_debt_servicing_capacity_calc004_63d_slope_v004_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc004_63d_slope_v004_signal'] = f58ds_f58_debt_servicing_capacity_calc004_63d_slope_v004_signal

def f58ds_f58_debt_servicing_capacity_calc005_10d_slope_v005_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(10).quantile(0.75)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc005_10d_slope_v005_signal'] = f58ds_f58_debt_servicing_capacity_calc005_10d_slope_v005_signal

def f58ds_f58_debt_servicing_capacity_calc006_21d_slope_v006_signal(ncfo, revenue):
    res = ((((ncfo / revenue)) / ((ncfo / revenue)).rolling(21).min())).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc006_21d_slope_v006_signal'] = f58ds_f58_debt_servicing_capacity_calc006_21d_slope_v006_signal

def f58ds_f58_debt_servicing_capacity_calc007_42d_slope_v007_signal(currentratio, debt):
    res = ((((currentratio / debt)) - ((currentratio / debt)).rolling(42).mean()) / ((currentratio / debt)).rolling(42).std()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc007_42d_slope_v007_signal'] = f58ds_f58_debt_servicing_capacity_calc007_42d_slope_v007_signal

def f58ds_f58_debt_servicing_capacity_calc008_5d_slope_v008_signal(fcf, intexp):
    res = ((((fcf / intexp)) - ((fcf / intexp)).rolling(5).mean()) / ((fcf / intexp)).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc008_5d_slope_v008_signal'] = f58ds_f58_debt_servicing_capacity_calc008_5d_slope_v008_signal

def f58ds_f58_debt_servicing_capacity_calc009_21d_slope_v009_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(21).max()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc009_21d_slope_v009_signal'] = f58ds_f58_debt_servicing_capacity_calc009_21d_slope_v009_signal

def f58ds_f58_debt_servicing_capacity_calc010_63d_slope_v010_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(63).skew()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc010_63d_slope_v010_signal'] = f58ds_f58_debt_servicing_capacity_calc010_63d_slope_v010_signal

def f58ds_f58_debt_servicing_capacity_calc011_5d_slope_v011_signal(currentratio, debt):
    res = ((currentratio / debt).diff(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc011_5d_slope_v011_signal'] = f58ds_f58_debt_servicing_capacity_calc011_5d_slope_v011_signal

def f58ds_f58_debt_servicing_capacity_calc012_5d_slope_v012_signal(debt, workingcapital):
    res = ((workingcapital / debt).pct_change(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc012_5d_slope_v012_signal'] = f58ds_f58_debt_servicing_capacity_calc012_5d_slope_v012_signal

def f58ds_f58_debt_servicing_capacity_calc013_21d_slope_v013_signal(debt, equity):
    res = ((((debt / equity)) / ((debt / equity)).rolling(21).min())).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc013_21d_slope_v013_signal'] = f58ds_f58_debt_servicing_capacity_calc013_21d_slope_v013_signal

def f58ds_f58_debt_servicing_capacity_calc014_42d_slope_v014_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(42).quantile(0.25)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc014_42d_slope_v014_signal'] = f58ds_f58_debt_servicing_capacity_calc014_42d_slope_v014_signal

def f58ds_f58_debt_servicing_capacity_calc015_10d_slope_v015_signal(debt, gp):
    res = ((gp / debt).rolling(10).rank(pct=True)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc015_10d_slope_v015_signal'] = f58ds_f58_debt_servicing_capacity_calc015_10d_slope_v015_signal

def f58ds_f58_debt_servicing_capacity_calc016_21d_slope_v016_signal(debt, fcf):
    res = ((fcf / debt).rolling(21).quantile(0.5)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc016_21d_slope_v016_signal'] = f58ds_f58_debt_servicing_capacity_calc016_21d_slope_v016_signal

def f58ds_f58_debt_servicing_capacity_calc017_5d_slope_v017_signal(liabilities, netinc):
    res = ((netinc / liabilities).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc017_5d_slope_v017_signal'] = f58ds_f58_debt_servicing_capacity_calc017_5d_slope_v017_signal

def f58ds_f58_debt_servicing_capacity_calc018_252d_slope_v018_signal(assets, fcf):
    res = (np.log(((fcf / assets)).abs().replace(0, np.nan)).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc018_252d_slope_v018_signal'] = f58ds_f58_debt_servicing_capacity_calc018_252d_slope_v018_signal

def f58ds_f58_debt_servicing_capacity_calc019_5d_slope_v019_signal(ncfo, revenue):
    res = ((((ncfo / revenue)) - ((ncfo / revenue)).rolling(5).mean()) / ((ncfo / revenue)).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc019_5d_slope_v019_signal'] = f58ds_f58_debt_servicing_capacity_calc019_5d_slope_v019_signal

def f58ds_f58_debt_servicing_capacity_calc020_252d_slope_v020_signal(fcf, intexp):
    res = ((fcf / intexp).rolling(252).quantile(0.25)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc020_252d_slope_v020_signal'] = f58ds_f58_debt_servicing_capacity_calc020_252d_slope_v020_signal

def f58ds_f58_debt_servicing_capacity_calc021_42d_slope_v021_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(42).min()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc021_42d_slope_v021_signal'] = f58ds_f58_debt_servicing_capacity_calc021_42d_slope_v021_signal

def f58ds_f58_debt_servicing_capacity_calc022_42d_slope_v022_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(42).var()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc022_42d_slope_v022_signal'] = f58ds_f58_debt_servicing_capacity_calc022_42d_slope_v022_signal

def f58ds_f58_debt_servicing_capacity_calc023_126d_slope_v023_signal(debt, workingcapital):
    res = ((((debt / workingcapital)) / ((debt / workingcapital)).rolling(126).max())).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc023_126d_slope_v023_signal'] = f58ds_f58_debt_servicing_capacity_calc023_126d_slope_v023_signal

def f58ds_f58_debt_servicing_capacity_calc024_252d_slope_v024_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc024_252d_slope_v024_signal'] = f58ds_f58_debt_servicing_capacity_calc024_252d_slope_v024_signal

def f58ds_f58_debt_servicing_capacity_calc025_10d_slope_v025_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc025_10d_slope_v025_signal'] = f58ds_f58_debt_servicing_capacity_calc025_10d_slope_v025_signal

def f58ds_f58_debt_servicing_capacity_calc026_5d_slope_v026_signal(debt, marketcap):
    res = ((debt / marketcap).pct_change(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc026_5d_slope_v026_signal'] = f58ds_f58_debt_servicing_capacity_calc026_5d_slope_v026_signal

def f58ds_f58_debt_servicing_capacity_calc027_63d_slope_v027_signal(fcf, intexp):
    res = ((fcf / intexp).rolling(63).rank(pct=True)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc027_63d_slope_v027_signal'] = f58ds_f58_debt_servicing_capacity_calc027_63d_slope_v027_signal

def f58ds_f58_debt_servicing_capacity_calc028_5d_slope_v028_signal(intexp, netinc):
    res = ((((netinc / intexp)) / ((netinc / intexp)).rolling(5).max())).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc028_5d_slope_v028_signal'] = f58ds_f58_debt_servicing_capacity_calc028_5d_slope_v028_signal

def f58ds_f58_debt_servicing_capacity_calc029_5d_slope_v029_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(5).quantile(0.5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc029_5d_slope_v029_signal'] = f58ds_f58_debt_servicing_capacity_calc029_5d_slope_v029_signal

def f58ds_f58_debt_servicing_capacity_calc030_126d_slope_v030_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc030_126d_slope_v030_signal'] = f58ds_f58_debt_servicing_capacity_calc030_126d_slope_v030_signal

def f58ds_f58_debt_servicing_capacity_calc031_252d_slope_v031_signal(ebitda, liabilities):
    res = ((ebitda / liabilities).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc031_252d_slope_v031_signal'] = f58ds_f58_debt_servicing_capacity_calc031_252d_slope_v031_signal

def f58ds_f58_debt_servicing_capacity_calc032_63d_slope_v032_signal(assets, fcf):
    res = ((fcf / assets).rolling(63).quantile(0.25)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc032_63d_slope_v032_signal'] = f58ds_f58_debt_servicing_capacity_calc032_63d_slope_v032_signal

def f58ds_f58_debt_servicing_capacity_calc033_10d_slope_v033_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(10).max()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc033_10d_slope_v033_signal'] = f58ds_f58_debt_servicing_capacity_calc033_10d_slope_v033_signal

def f58ds_f58_debt_servicing_capacity_calc034_126d_slope_v034_signal(debt, gp):
    res = ((gp / debt).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc034_126d_slope_v034_signal'] = f58ds_f58_debt_servicing_capacity_calc034_126d_slope_v034_signal

def f58ds_f58_debt_servicing_capacity_calc035_126d_slope_v035_signal(liabilities, revenue):
    res = ((liabilities / revenue).pct_change(126)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc035_126d_slope_v035_signal'] = f58ds_f58_debt_servicing_capacity_calc035_126d_slope_v035_signal

def f58ds_f58_debt_servicing_capacity_calc036_126d_slope_v036_signal(debt, gp):
    res = ((gp / debt).rolling(126).skew()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc036_126d_slope_v036_signal'] = f58ds_f58_debt_servicing_capacity_calc036_126d_slope_v036_signal

def f58ds_f58_debt_servicing_capacity_calc037_5d_slope_v037_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc037_5d_slope_v037_signal'] = f58ds_f58_debt_servicing_capacity_calc037_5d_slope_v037_signal

def f58ds_f58_debt_servicing_capacity_calc038_21d_slope_v038_signal(ebitda, liabilities):
    res = ((ebitda / liabilities).rolling(21).max()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc038_21d_slope_v038_signal'] = f58ds_f58_debt_servicing_capacity_calc038_21d_slope_v038_signal

def f58ds_f58_debt_servicing_capacity_calc039_63d_slope_v039_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(63).rank(pct=True)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc039_63d_slope_v039_signal'] = f58ds_f58_debt_servicing_capacity_calc039_63d_slope_v039_signal

def f58ds_f58_debt_servicing_capacity_calc040_252d_slope_v040_signal(ebitda, liabilities):
    res = ((liabilities / ebitda).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc040_252d_slope_v040_signal'] = f58ds_f58_debt_servicing_capacity_calc040_252d_slope_v040_signal

def f58ds_f58_debt_servicing_capacity_calc041_42d_slope_v041_signal(ebitda, ev):
    res = ((ev / ebitda).diff(42)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc041_42d_slope_v041_signal'] = f58ds_f58_debt_servicing_capacity_calc041_42d_slope_v041_signal

def f58ds_f58_debt_servicing_capacity_calc042_63d_slope_v042_signal(ebitda, intexp):
    res = ((((ebitda / intexp)) - ((ebitda / intexp)).rolling(63).mean()) / ((ebitda / intexp)).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc042_63d_slope_v042_signal'] = f58ds_f58_debt_servicing_capacity_calc042_63d_slope_v042_signal

def f58ds_f58_debt_servicing_capacity_calc043_252d_slope_v043_signal(debt, gp):
    res = ((debt / gp).rolling(252).quantile(0.25)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc043_252d_slope_v043_signal'] = f58ds_f58_debt_servicing_capacity_calc043_252d_slope_v043_signal

def f58ds_f58_debt_servicing_capacity_calc044_21d_slope_v044_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(21).quantile(0.25)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc044_21d_slope_v044_signal'] = f58ds_f58_debt_servicing_capacity_calc044_21d_slope_v044_signal

def f58ds_f58_debt_servicing_capacity_calc045_42d_slope_v045_signal(equity, liabilities):
    res = ((((liabilities / equity)) / ((liabilities / equity)).rolling(42).min())).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc045_42d_slope_v045_signal'] = f58ds_f58_debt_servicing_capacity_calc045_42d_slope_v045_signal

def f58ds_f58_debt_servicing_capacity_calc046_63d_slope_v046_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(63).var()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc046_63d_slope_v046_signal'] = f58ds_f58_debt_servicing_capacity_calc046_63d_slope_v046_signal

def f58ds_f58_debt_servicing_capacity_calc047_21d_slope_v047_signal(ebitda, intexp):
    res = ((ebitda / intexp).diff(21)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc047_21d_slope_v047_signal'] = f58ds_f58_debt_servicing_capacity_calc047_21d_slope_v047_signal

def f58ds_f58_debt_servicing_capacity_calc048_10d_slope_v048_signal(debt, fcf):
    res = ((fcf / debt).rolling(10).min()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc048_10d_slope_v048_signal'] = f58ds_f58_debt_servicing_capacity_calc048_10d_slope_v048_signal

def f58ds_f58_debt_servicing_capacity_calc049_42d_slope_v049_signal(ebitda, intexp):
    res = ((((ebitda / intexp)) / ((ebitda / intexp)).rolling(42).min())).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc049_42d_slope_v049_signal'] = f58ds_f58_debt_servicing_capacity_calc049_42d_slope_v049_signal

def f58ds_f58_debt_servicing_capacity_calc050_21d_slope_v050_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(21).var()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc050_21d_slope_v050_signal'] = f58ds_f58_debt_servicing_capacity_calc050_21d_slope_v050_signal

def f58ds_f58_debt_servicing_capacity_calc051_21d_slope_v051_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(21).min()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc051_21d_slope_v051_signal'] = f58ds_f58_debt_servicing_capacity_calc051_21d_slope_v051_signal

def f58ds_f58_debt_servicing_capacity_calc052_126d_slope_v052_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(126).quantile(0.75)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc052_126d_slope_v052_signal'] = f58ds_f58_debt_servicing_capacity_calc052_126d_slope_v052_signal

def f58ds_f58_debt_servicing_capacity_calc053_21d_slope_v053_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(21).quantile(0.5)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc053_21d_slope_v053_signal'] = f58ds_f58_debt_servicing_capacity_calc053_21d_slope_v053_signal

def f58ds_f58_debt_servicing_capacity_calc054_126d_slope_v054_signal(debt, equity):
    res = ((debt / equity).rolling(126).quantile(0.5)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc054_126d_slope_v054_signal'] = f58ds_f58_debt_servicing_capacity_calc054_126d_slope_v054_signal

def f58ds_f58_debt_servicing_capacity_calc055_42d_slope_v055_signal(debt, gp):
    res = ((debt / gp).rolling(42).skew()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc055_42d_slope_v055_signal'] = f58ds_f58_debt_servicing_capacity_calc055_42d_slope_v055_signal

def f58ds_f58_debt_servicing_capacity_calc056_21d_slope_v056_signal(intexp, revenue):
    res = (np.log(((intexp / revenue)).abs().replace(0, np.nan)).rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc056_21d_slope_v056_signal'] = f58ds_f58_debt_servicing_capacity_calc056_21d_slope_v056_signal

def f58ds_f58_debt_servicing_capacity_calc057_10d_slope_v057_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(10).var()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc057_10d_slope_v057_signal'] = f58ds_f58_debt_servicing_capacity_calc057_10d_slope_v057_signal

def f58ds_f58_debt_servicing_capacity_calc058_10d_slope_v058_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(10).quantile(0.5)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc058_10d_slope_v058_signal'] = f58ds_f58_debt_servicing_capacity_calc058_10d_slope_v058_signal

def f58ds_f58_debt_servicing_capacity_calc059_63d_slope_v059_signal(debt, gp):
    res = ((((gp / debt)) / ((gp / debt)).rolling(63).max())).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc059_63d_slope_v059_signal'] = f58ds_f58_debt_servicing_capacity_calc059_63d_slope_v059_signal

def f58ds_f58_debt_servicing_capacity_calc060_5d_slope_v060_signal(intexp, revenue):
    res = ((((intexp / revenue)) - ((intexp / revenue)).rolling(5).mean()) / ((intexp / revenue)).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc060_5d_slope_v060_signal'] = f58ds_f58_debt_servicing_capacity_calc060_5d_slope_v060_signal

def f58ds_f58_debt_servicing_capacity_calc061_42d_slope_v061_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(42).min()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc061_42d_slope_v061_signal'] = f58ds_f58_debt_servicing_capacity_calc061_42d_slope_v061_signal

def f58ds_f58_debt_servicing_capacity_calc062_5d_slope_v062_signal(debt, gp):
    res = ((gp / debt).rolling(5).skew()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc062_5d_slope_v062_signal'] = f58ds_f58_debt_servicing_capacity_calc062_5d_slope_v062_signal

def f58ds_f58_debt_servicing_capacity_calc063_42d_slope_v063_signal(debt, gp):
    res = ((((gp / debt)) / ((gp / debt)).rolling(42).min())).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc063_42d_slope_v063_signal'] = f58ds_f58_debt_servicing_capacity_calc063_42d_slope_v063_signal

def f58ds_f58_debt_servicing_capacity_calc064_63d_slope_v064_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(63).quantile(0.75)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc064_63d_slope_v064_signal'] = f58ds_f58_debt_servicing_capacity_calc064_63d_slope_v064_signal

def f58ds_f58_debt_servicing_capacity_calc065_10d_slope_v065_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(10).quantile(0.5)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc065_10d_slope_v065_signal'] = f58ds_f58_debt_servicing_capacity_calc065_10d_slope_v065_signal

def f58ds_f58_debt_servicing_capacity_calc066_126d_slope_v066_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(126).min()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc066_126d_slope_v066_signal'] = f58ds_f58_debt_servicing_capacity_calc066_126d_slope_v066_signal

def f58ds_f58_debt_servicing_capacity_calc067_5d_slope_v067_signal(liabilities, opinc):
    res = ((((opinc / liabilities)) - ((opinc / liabilities)).rolling(5).mean()) / ((opinc / liabilities)).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc067_5d_slope_v067_signal'] = f58ds_f58_debt_servicing_capacity_calc067_5d_slope_v067_signal

def f58ds_f58_debt_servicing_capacity_calc068_5d_slope_v068_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(5).rank(pct=True)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc068_5d_slope_v068_signal'] = f58ds_f58_debt_servicing_capacity_calc068_5d_slope_v068_signal

def f58ds_f58_debt_servicing_capacity_calc069_10d_slope_v069_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(10).max()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc069_10d_slope_v069_signal'] = f58ds_f58_debt_servicing_capacity_calc069_10d_slope_v069_signal

def f58ds_f58_debt_servicing_capacity_calc070_63d_slope_v070_signal(assets, debt):
    res = ((debt / assets).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc070_63d_slope_v070_signal'] = f58ds_f58_debt_servicing_capacity_calc070_63d_slope_v070_signal

def f58ds_f58_debt_servicing_capacity_calc071_5d_slope_v071_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(5).kurt()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc071_5d_slope_v071_signal'] = f58ds_f58_debt_servicing_capacity_calc071_5d_slope_v071_signal

def f58ds_f58_debt_servicing_capacity_calc072_126d_slope_v072_signal(debt, equity):
    res = ((debt / equity).pct_change(126)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc072_126d_slope_v072_signal'] = f58ds_f58_debt_servicing_capacity_calc072_126d_slope_v072_signal

def f58ds_f58_debt_servicing_capacity_calc073_10d_slope_v073_signal(intexp, netinc):
    res = ((netinc / intexp).diff(10)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc073_10d_slope_v073_signal'] = f58ds_f58_debt_servicing_capacity_calc073_10d_slope_v073_signal

def f58ds_f58_debt_servicing_capacity_calc074_252d_slope_v074_signal(debt, gp):
    res = ((gp / debt).rolling(252).max()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc074_252d_slope_v074_signal'] = f58ds_f58_debt_servicing_capacity_calc074_252d_slope_v074_signal

def f58ds_f58_debt_servicing_capacity_calc075_63d_slope_v075_signal(assets, fcf):
    res = ((fcf / assets).rolling(63).skew()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc075_63d_slope_v075_signal'] = f58ds_f58_debt_servicing_capacity_calc075_63d_slope_v075_signal

def f58ds_f58_debt_servicing_capacity_calc076_63d_slope_v076_signal(debt, workingcapital):
    res = ((((workingcapital / debt)) - ((workingcapital / debt)).rolling(63).mean()) / ((workingcapital / debt)).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc076_63d_slope_v076_signal'] = f58ds_f58_debt_servicing_capacity_calc076_63d_slope_v076_signal

def f58ds_f58_debt_servicing_capacity_calc077_63d_slope_v077_signal(assets, ebitda):
    res = ((ebitda / assets).pct_change(63)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc077_63d_slope_v077_signal'] = f58ds_f58_debt_servicing_capacity_calc077_63d_slope_v077_signal

def f58ds_f58_debt_servicing_capacity_calc078_5d_slope_v078_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(5).rank(pct=True)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc078_5d_slope_v078_signal'] = f58ds_f58_debt_servicing_capacity_calc078_5d_slope_v078_signal

def f58ds_f58_debt_servicing_capacity_calc079_10d_slope_v079_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc079_10d_slope_v079_signal'] = f58ds_f58_debt_servicing_capacity_calc079_10d_slope_v079_signal

def f58ds_f58_debt_servicing_capacity_calc080_5d_slope_v080_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(5).max()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc080_5d_slope_v080_signal'] = f58ds_f58_debt_servicing_capacity_calc080_5d_slope_v080_signal

def f58ds_f58_debt_servicing_capacity_calc081_5d_slope_v081_signal(debt, gp):
    res = ((debt / gp).rolling(5).max()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc081_5d_slope_v081_signal'] = f58ds_f58_debt_servicing_capacity_calc081_5d_slope_v081_signal

def f58ds_f58_debt_servicing_capacity_calc082_42d_slope_v082_signal(assets, netinc):
    res = ((netinc / assets).diff(42)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc082_42d_slope_v082_signal'] = f58ds_f58_debt_servicing_capacity_calc082_42d_slope_v082_signal

def f58ds_f58_debt_servicing_capacity_calc083_42d_slope_v083_signal(assets, netinc):
    res = ((((netinc / assets)) / ((netinc / assets)).rolling(42).max())).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc083_42d_slope_v083_signal'] = f58ds_f58_debt_servicing_capacity_calc083_42d_slope_v083_signal

def f58ds_f58_debt_servicing_capacity_calc084_63d_slope_v084_signal(debt, marketcap):
    res = ((debt / marketcap).diff(63)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc084_63d_slope_v084_signal'] = f58ds_f58_debt_servicing_capacity_calc084_63d_slope_v084_signal

def f58ds_f58_debt_servicing_capacity_calc085_21d_slope_v085_signal(debt, fcf):
    res = ((fcf / debt).diff(21)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc085_21d_slope_v085_signal'] = f58ds_f58_debt_servicing_capacity_calc085_21d_slope_v085_signal

def f58ds_f58_debt_servicing_capacity_calc086_42d_slope_v086_signal(liabilities, netinc):
    res = ((netinc / liabilities).rolling(42).max()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc086_42d_slope_v086_signal'] = f58ds_f58_debt_servicing_capacity_calc086_42d_slope_v086_signal

def f58ds_f58_debt_servicing_capacity_calc087_10d_slope_v087_signal(assets, fcf):
    res = ((fcf / assets).rolling(10).quantile(0.25)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc087_10d_slope_v087_signal'] = f58ds_f58_debt_servicing_capacity_calc087_10d_slope_v087_signal

def f58ds_f58_debt_servicing_capacity_calc088_21d_slope_v088_signal(debt, ncfo):
    res = ((ncfo / debt).rolling(21).var()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc088_21d_slope_v088_signal'] = f58ds_f58_debt_servicing_capacity_calc088_21d_slope_v088_signal

def f58ds_f58_debt_servicing_capacity_calc089_42d_slope_v089_signal(debt, gp):
    res = ((gp / debt).rolling(42).quantile(0.25)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc089_42d_slope_v089_signal'] = f58ds_f58_debt_servicing_capacity_calc089_42d_slope_v089_signal

def f58ds_f58_debt_servicing_capacity_calc090_252d_slope_v090_signal(equity, liabilities):
    res = ((liabilities / equity).pct_change(252)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc090_252d_slope_v090_signal'] = f58ds_f58_debt_servicing_capacity_calc090_252d_slope_v090_signal

def f58ds_f58_debt_servicing_capacity_calc091_63d_slope_v091_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(63).var()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc091_63d_slope_v091_signal'] = f58ds_f58_debt_servicing_capacity_calc091_63d_slope_v091_signal

def f58ds_f58_debt_servicing_capacity_calc092_42d_slope_v092_signal(debt, revenue):
    res = ((debt / revenue).rolling(42).quantile(0.25)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc092_42d_slope_v092_signal'] = f58ds_f58_debt_servicing_capacity_calc092_42d_slope_v092_signal

def f58ds_f58_debt_servicing_capacity_calc093_5d_slope_v093_signal(fcf, liabilities):
    res = ((fcf / liabilities).diff(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc093_5d_slope_v093_signal'] = f58ds_f58_debt_servicing_capacity_calc093_5d_slope_v093_signal

def f58ds_f58_debt_servicing_capacity_calc094_10d_slope_v094_signal(currentratio, debt):
    res = ((currentratio / debt).diff(10)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc094_10d_slope_v094_signal'] = f58ds_f58_debt_servicing_capacity_calc094_10d_slope_v094_signal

def f58ds_f58_debt_servicing_capacity_calc095_10d_slope_v095_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(10).quantile(0.25)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc095_10d_slope_v095_signal'] = f58ds_f58_debt_servicing_capacity_calc095_10d_slope_v095_signal

def f58ds_f58_debt_servicing_capacity_calc096_126d_slope_v096_signal(assets, netinc):
    res = ((netinc / assets).rolling(126).max()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc096_126d_slope_v096_signal'] = f58ds_f58_debt_servicing_capacity_calc096_126d_slope_v096_signal

def f58ds_f58_debt_servicing_capacity_calc097_5d_slope_v097_signal(fcf, intexp):
    res = ((((fcf / intexp)) / ((fcf / intexp)).rolling(5).max())).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc097_5d_slope_v097_signal'] = f58ds_f58_debt_servicing_capacity_calc097_5d_slope_v097_signal

def f58ds_f58_debt_servicing_capacity_calc098_42d_slope_v098_signal(debt, marketcap):
    res = (np.log(((debt / marketcap)).abs().replace(0, np.nan)).rolling(42).std()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc098_42d_slope_v098_signal'] = f58ds_f58_debt_servicing_capacity_calc098_42d_slope_v098_signal

def f58ds_f58_debt_servicing_capacity_calc099_5d_slope_v099_signal(equity, liabilities):
    res = ((liabilities / equity).diff(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc099_5d_slope_v099_signal'] = f58ds_f58_debt_servicing_capacity_calc099_5d_slope_v099_signal

def f58ds_f58_debt_servicing_capacity_calc100_126d_slope_v100_signal(debt, gp):
    res = (np.log(((debt / gp)).abs().replace(0, np.nan)).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc100_126d_slope_v100_signal'] = f58ds_f58_debt_servicing_capacity_calc100_126d_slope_v100_signal

def f58ds_f58_debt_servicing_capacity_calc101_5d_slope_v101_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(5).quantile(0.5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc101_5d_slope_v101_signal'] = f58ds_f58_debt_servicing_capacity_calc101_5d_slope_v101_signal

def f58ds_f58_debt_servicing_capacity_calc102_63d_slope_v102_signal(debt, workingcapital):
    res = ((debt / workingcapital).pct_change(63)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc102_63d_slope_v102_signal'] = f58ds_f58_debt_servicing_capacity_calc102_63d_slope_v102_signal

def f58ds_f58_debt_servicing_capacity_calc103_10d_slope_v103_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(10).rank(pct=True)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc103_10d_slope_v103_signal'] = f58ds_f58_debt_servicing_capacity_calc103_10d_slope_v103_signal

def f58ds_f58_debt_servicing_capacity_calc104_126d_slope_v104_signal(assets, fcf):
    res = ((((fcf / assets)) - ((fcf / assets)).rolling(126).mean()) / ((fcf / assets)).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc104_126d_slope_v104_signal'] = f58ds_f58_debt_servicing_capacity_calc104_126d_slope_v104_signal

def f58ds_f58_debt_servicing_capacity_calc105_42d_slope_v105_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc105_42d_slope_v105_signal'] = f58ds_f58_debt_servicing_capacity_calc105_42d_slope_v105_signal

def f58ds_f58_debt_servicing_capacity_calc106_63d_slope_v106_signal(currentratio, debt):
    res = ((currentratio / debt).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc106_63d_slope_v106_signal'] = f58ds_f58_debt_servicing_capacity_calc106_63d_slope_v106_signal

def f58ds_f58_debt_servicing_capacity_calc107_10d_slope_v107_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(10).quantile(0.5)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc107_10d_slope_v107_signal'] = f58ds_f58_debt_servicing_capacity_calc107_10d_slope_v107_signal

def f58ds_f58_debt_servicing_capacity_calc108_63d_slope_v108_signal(liabilities, netinc):
    res = ((((netinc / liabilities)) - ((netinc / liabilities)).rolling(63).mean()) / ((netinc / liabilities)).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc108_63d_slope_v108_signal'] = f58ds_f58_debt_servicing_capacity_calc108_63d_slope_v108_signal

def f58ds_f58_debt_servicing_capacity_calc109_126d_slope_v109_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc109_126d_slope_v109_signal'] = f58ds_f58_debt_servicing_capacity_calc109_126d_slope_v109_signal

def f58ds_f58_debt_servicing_capacity_calc110_10d_slope_v110_signal(fcf, intexp):
    res = ((fcf / intexp).rolling(10).std()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc110_10d_slope_v110_signal'] = f58ds_f58_debt_servicing_capacity_calc110_10d_slope_v110_signal

def f58ds_f58_debt_servicing_capacity_calc111_126d_slope_v111_signal(debt, workingcapital):
    res = ((debt / workingcapital).rolling(126).quantile(0.25)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc111_126d_slope_v111_signal'] = f58ds_f58_debt_servicing_capacity_calc111_126d_slope_v111_signal

def f58ds_f58_debt_servicing_capacity_calc112_126d_slope_v112_signal(debt, equity):
    res = ((debt / equity).rolling(126).skew()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc112_126d_slope_v112_signal'] = f58ds_f58_debt_servicing_capacity_calc112_126d_slope_v112_signal

def f58ds_f58_debt_servicing_capacity_calc113_42d_slope_v113_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(42).kurt()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc113_42d_slope_v113_signal'] = f58ds_f58_debt_servicing_capacity_calc113_42d_slope_v113_signal

def f58ds_f58_debt_servicing_capacity_calc114_42d_slope_v114_signal(debt, ncfo):
    res = ((ncfo / debt).diff(42)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc114_42d_slope_v114_signal'] = f58ds_f58_debt_servicing_capacity_calc114_42d_slope_v114_signal

def f58ds_f58_debt_servicing_capacity_calc115_10d_slope_v115_signal(debt, equity):
    res = ((debt / equity).rolling(10).quantile(0.75)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc115_10d_slope_v115_signal'] = f58ds_f58_debt_servicing_capacity_calc115_10d_slope_v115_signal

def f58ds_f58_debt_servicing_capacity_calc116_21d_slope_v116_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(21).skew()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc116_21d_slope_v116_signal'] = f58ds_f58_debt_servicing_capacity_calc116_21d_slope_v116_signal

def f58ds_f58_debt_servicing_capacity_calc117_5d_slope_v117_signal(debt, workingcapital):
    res = ((debt / workingcapital).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc117_5d_slope_v117_signal'] = f58ds_f58_debt_servicing_capacity_calc117_5d_slope_v117_signal

def f58ds_f58_debt_servicing_capacity_calc118_63d_slope_v118_signal(debt, ebitda):
    res = ((((debt / ebitda)) - ((debt / ebitda)).rolling(63).mean()) / ((debt / ebitda)).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc118_63d_slope_v118_signal'] = f58ds_f58_debt_servicing_capacity_calc118_63d_slope_v118_signal

def f58ds_f58_debt_servicing_capacity_calc119_126d_slope_v119_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(126).quantile(0.25)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc119_126d_slope_v119_signal'] = f58ds_f58_debt_servicing_capacity_calc119_126d_slope_v119_signal

def f58ds_f58_debt_servicing_capacity_calc120_63d_slope_v120_signal(intexp, opinc):
    res = ((((opinc / intexp)) - ((opinc / intexp)).rolling(63).mean()) / ((opinc / intexp)).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc120_63d_slope_v120_signal'] = f58ds_f58_debt_servicing_capacity_calc120_63d_slope_v120_signal

def f58ds_f58_debt_servicing_capacity_calc121_10d_slope_v121_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(10).quantile(0.25)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc121_10d_slope_v121_signal'] = f58ds_f58_debt_servicing_capacity_calc121_10d_slope_v121_signal

def f58ds_f58_debt_servicing_capacity_calc122_5d_slope_v122_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc122_5d_slope_v122_signal'] = f58ds_f58_debt_servicing_capacity_calc122_5d_slope_v122_signal

def f58ds_f58_debt_servicing_capacity_calc123_5d_slope_v123_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(5).skew()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc123_5d_slope_v123_signal'] = f58ds_f58_debt_servicing_capacity_calc123_5d_slope_v123_signal

def f58ds_f58_debt_servicing_capacity_calc124_252d_slope_v124_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(252).quantile(0.5)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc124_252d_slope_v124_signal'] = f58ds_f58_debt_servicing_capacity_calc124_252d_slope_v124_signal

def f58ds_f58_debt_servicing_capacity_calc125_63d_slope_v125_signal(assets, ebitda):
    res = (np.log(((ebitda / assets)).abs().replace(0, np.nan)).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc125_63d_slope_v125_signal'] = f58ds_f58_debt_servicing_capacity_calc125_63d_slope_v125_signal

def f58ds_f58_debt_servicing_capacity_calc126_126d_slope_v126_signal(debt, gp):
    res = ((debt / gp).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc126_126d_slope_v126_signal'] = f58ds_f58_debt_servicing_capacity_calc126_126d_slope_v126_signal

def f58ds_f58_debt_servicing_capacity_calc127_42d_slope_v127_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(42).quantile(0.75)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc127_42d_slope_v127_signal'] = f58ds_f58_debt_servicing_capacity_calc127_42d_slope_v127_signal

def f58ds_f58_debt_servicing_capacity_calc128_10d_slope_v128_signal(assets, fcf):
    res = ((fcf / assets).rolling(10).skew()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc128_10d_slope_v128_signal'] = f58ds_f58_debt_servicing_capacity_calc128_10d_slope_v128_signal

def f58ds_f58_debt_servicing_capacity_calc129_42d_slope_v129_signal(debt, gp):
    res = ((debt / gp).rolling(42).kurt()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc129_42d_slope_v129_signal'] = f58ds_f58_debt_servicing_capacity_calc129_42d_slope_v129_signal

def f58ds_f58_debt_servicing_capacity_calc130_63d_slope_v130_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(63).min()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc130_63d_slope_v130_signal'] = f58ds_f58_debt_servicing_capacity_calc130_63d_slope_v130_signal

def f58ds_f58_debt_servicing_capacity_calc131_5d_slope_v131_signal(assets, debt):
    res = ((debt / assets).diff(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc131_5d_slope_v131_signal'] = f58ds_f58_debt_servicing_capacity_calc131_5d_slope_v131_signal

def f58ds_f58_debt_servicing_capacity_calc132_21d_slope_v132_signal(assets, netinc):
    res = ((netinc / assets).diff(21)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc132_21d_slope_v132_signal'] = f58ds_f58_debt_servicing_capacity_calc132_21d_slope_v132_signal

def f58ds_f58_debt_servicing_capacity_calc133_252d_slope_v133_signal(debt, marketcap):
    res = ((((debt / marketcap)) - ((debt / marketcap)).rolling(252).mean()) / ((debt / marketcap)).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc133_252d_slope_v133_signal'] = f58ds_f58_debt_servicing_capacity_calc133_252d_slope_v133_signal

def f58ds_f58_debt_servicing_capacity_calc134_63d_slope_v134_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(63).quantile(0.75)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc134_63d_slope_v134_signal'] = f58ds_f58_debt_servicing_capacity_calc134_63d_slope_v134_signal

def f58ds_f58_debt_servicing_capacity_calc135_126d_slope_v135_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc135_126d_slope_v135_signal'] = f58ds_f58_debt_servicing_capacity_calc135_126d_slope_v135_signal

def f58ds_f58_debt_servicing_capacity_calc136_10d_slope_v136_signal(debt, workingcapital):
    res = (np.log(((workingcapital / debt)).abs().replace(0, np.nan)).rolling(10).std()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc136_10d_slope_v136_signal'] = f58ds_f58_debt_servicing_capacity_calc136_10d_slope_v136_signal

def f58ds_f58_debt_servicing_capacity_calc137_126d_slope_v137_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(126).var()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc137_126d_slope_v137_signal'] = f58ds_f58_debt_servicing_capacity_calc137_126d_slope_v137_signal

def f58ds_f58_debt_servicing_capacity_calc138_10d_slope_v138_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc138_10d_slope_v138_signal'] = f58ds_f58_debt_servicing_capacity_calc138_10d_slope_v138_signal

def f58ds_f58_debt_servicing_capacity_calc139_10d_slope_v139_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(10).rank(pct=True)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc139_10d_slope_v139_signal'] = f58ds_f58_debt_servicing_capacity_calc139_10d_slope_v139_signal

def f58ds_f58_debt_servicing_capacity_calc140_252d_slope_v140_signal(assets, debt):
    res = ((((debt / assets)) - ((debt / assets)).rolling(252).mean()) / ((debt / assets)).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc140_252d_slope_v140_signal'] = f58ds_f58_debt_servicing_capacity_calc140_252d_slope_v140_signal

def f58ds_f58_debt_servicing_capacity_calc141_21d_slope_v141_signal(ebitda, liabilities):
    res = (np.log(((ebitda / liabilities)).abs().replace(0, np.nan)).rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc141_21d_slope_v141_signal'] = f58ds_f58_debt_servicing_capacity_calc141_21d_slope_v141_signal

def f58ds_f58_debt_servicing_capacity_calc142_21d_slope_v142_signal(ebitda, liabilities):
    res = ((liabilities / ebitda).rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc142_21d_slope_v142_signal'] = f58ds_f58_debt_servicing_capacity_calc142_21d_slope_v142_signal

def f58ds_f58_debt_servicing_capacity_calc143_21d_slope_v143_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(21).var()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc143_21d_slope_v143_signal'] = f58ds_f58_debt_servicing_capacity_calc143_21d_slope_v143_signal

def f58ds_f58_debt_servicing_capacity_calc144_63d_slope_v144_signal(assets, ebitda):
    res = ((ebitda / assets).diff(63)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc144_63d_slope_v144_signal'] = f58ds_f58_debt_servicing_capacity_calc144_63d_slope_v144_signal

def f58ds_f58_debt_servicing_capacity_calc145_21d_slope_v145_signal(currentratio, debt):
    res = ((currentratio / debt).rolling(21).max()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc145_21d_slope_v145_signal'] = f58ds_f58_debt_servicing_capacity_calc145_21d_slope_v145_signal

def f58ds_f58_debt_servicing_capacity_calc146_5d_slope_v146_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(5).quantile(0.25)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc146_5d_slope_v146_signal'] = f58ds_f58_debt_servicing_capacity_calc146_5d_slope_v146_signal

def f58ds_f58_debt_servicing_capacity_calc147_42d_slope_v147_signal(liabilities, netinc):
    res = ((netinc / liabilities).rolling(42).kurt()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc147_42d_slope_v147_signal'] = f58ds_f58_debt_servicing_capacity_calc147_42d_slope_v147_signal

def f58ds_f58_debt_servicing_capacity_calc148_21d_slope_v148_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(21).quantile(0.5)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc148_21d_slope_v148_signal'] = f58ds_f58_debt_servicing_capacity_calc148_21d_slope_v148_signal

def f58ds_f58_debt_servicing_capacity_calc149_252d_slope_v149_signal(liabilities, opinc):
    res = ((opinc / liabilities).pct_change(252)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc149_252d_slope_v149_signal'] = f58ds_f58_debt_servicing_capacity_calc149_252d_slope_v149_signal

def f58ds_f58_debt_servicing_capacity_calc150_63d_slope_v150_signal(currentratio, debt):
    res = ((currentratio / debt).rolling(63).quantile(0.75)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc150_63d_slope_v150_signal'] = f58ds_f58_debt_servicing_capacity_calc150_63d_slope_v150_signal



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
