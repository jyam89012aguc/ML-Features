import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f58ds_f58_debt_servicing_capacity_calc001_42d_accel_v001_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(42).quantile(0.25)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc001_42d_accel_v001_signal'] = f58ds_f58_debt_servicing_capacity_calc001_42d_accel_v001_signal

def f58ds_f58_debt_servicing_capacity_calc002_5d_accel_v002_signal(ebitda, ev):
    res = ((ev / ebitda).pct_change(5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc002_5d_accel_v002_signal'] = f58ds_f58_debt_servicing_capacity_calc002_5d_accel_v002_signal

def f58ds_f58_debt_servicing_capacity_calc003_5d_accel_v003_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc003_5d_accel_v003_signal'] = f58ds_f58_debt_servicing_capacity_calc003_5d_accel_v003_signal

def f58ds_f58_debt_servicing_capacity_calc004_5d_accel_v004_signal(debt, revenue):
    res = ((debt / revenue).rolling(5).kurt()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc004_5d_accel_v004_signal'] = f58ds_f58_debt_servicing_capacity_calc004_5d_accel_v004_signal

def f58ds_f58_debt_servicing_capacity_calc005_252d_accel_v005_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(252).kurt()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc005_252d_accel_v005_signal'] = f58ds_f58_debt_servicing_capacity_calc005_252d_accel_v005_signal

def f58ds_f58_debt_servicing_capacity_calc006_252d_accel_v006_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc006_252d_accel_v006_signal'] = f58ds_f58_debt_servicing_capacity_calc006_252d_accel_v006_signal

def f58ds_f58_debt_servicing_capacity_calc007_63d_accel_v007_signal(assets, netinc):
    res = ((netinc / assets).rolling(63).skew()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc007_63d_accel_v007_signal'] = f58ds_f58_debt_servicing_capacity_calc007_63d_accel_v007_signal

def f58ds_f58_debt_servicing_capacity_calc008_21d_accel_v008_signal(debt, fcf):
    res = ((fcf / debt).rolling(21).min()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc008_21d_accel_v008_signal'] = f58ds_f58_debt_servicing_capacity_calc008_21d_accel_v008_signal

def f58ds_f58_debt_servicing_capacity_calc009_252d_accel_v009_signal(assets, debt):
    res = (np.log(((debt / assets)).abs().replace(0, np.nan)).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc009_252d_accel_v009_signal'] = f58ds_f58_debt_servicing_capacity_calc009_252d_accel_v009_signal

def f58ds_f58_debt_servicing_capacity_calc010_63d_accel_v010_signal(ebitda, intexp):
    res = (np.log(((ebitda / intexp)).abs().replace(0, np.nan)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc010_63d_accel_v010_signal'] = f58ds_f58_debt_servicing_capacity_calc010_63d_accel_v010_signal

def f58ds_f58_debt_servicing_capacity_calc011_126d_accel_v011_signal(debt, fcf):
    res = ((fcf / debt).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc011_126d_accel_v011_signal'] = f58ds_f58_debt_servicing_capacity_calc011_126d_accel_v011_signal

def f58ds_f58_debt_servicing_capacity_calc012_5d_accel_v012_signal(debt, gp):
    res = ((gp / debt).rolling(5).max()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc012_5d_accel_v012_signal'] = f58ds_f58_debt_servicing_capacity_calc012_5d_accel_v012_signal

def f58ds_f58_debt_servicing_capacity_calc013_21d_accel_v013_signal(debt, workingcapital):
    res = ((((workingcapital / debt)) / ((workingcapital / debt)).rolling(21).max())).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc013_21d_accel_v013_signal'] = f58ds_f58_debt_servicing_capacity_calc013_21d_accel_v013_signal

def f58ds_f58_debt_servicing_capacity_calc014_126d_accel_v014_signal(liabilities, netinc):
    res = ((((netinc / liabilities)) - ((netinc / liabilities)).rolling(126).mean()) / ((netinc / liabilities)).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc014_126d_accel_v014_signal'] = f58ds_f58_debt_servicing_capacity_calc014_126d_accel_v014_signal

def f58ds_f58_debt_servicing_capacity_calc015_42d_accel_v015_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(42).skew()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc015_42d_accel_v015_signal'] = f58ds_f58_debt_servicing_capacity_calc015_42d_accel_v015_signal

def f58ds_f58_debt_servicing_capacity_calc016_252d_accel_v016_signal(debt, ebitda):
    res = ((((debt / ebitda)) - ((debt / ebitda)).rolling(252).mean()) / ((debt / ebitda)).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc016_252d_accel_v016_signal'] = f58ds_f58_debt_servicing_capacity_calc016_252d_accel_v016_signal

def f58ds_f58_debt_servicing_capacity_calc017_252d_accel_v017_signal(debt, workingcapital):
    res = ((((workingcapital / debt)) / ((workingcapital / debt)).rolling(252).min())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc017_252d_accel_v017_signal'] = f58ds_f58_debt_servicing_capacity_calc017_252d_accel_v017_signal

def f58ds_f58_debt_servicing_capacity_calc018_126d_accel_v018_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(126).quantile(0.75)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc018_126d_accel_v018_signal'] = f58ds_f58_debt_servicing_capacity_calc018_126d_accel_v018_signal

def f58ds_f58_debt_servicing_capacity_calc019_63d_accel_v019_signal(assets, fcf):
    res = ((fcf / assets).diff(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc019_63d_accel_v019_signal'] = f58ds_f58_debt_servicing_capacity_calc019_63d_accel_v019_signal

def f58ds_f58_debt_servicing_capacity_calc020_126d_accel_v020_signal(currentratio, debt):
    res = ((currentratio / debt).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc020_126d_accel_v020_signal'] = f58ds_f58_debt_servicing_capacity_calc020_126d_accel_v020_signal

def f58ds_f58_debt_servicing_capacity_calc021_21d_accel_v021_signal(debt, revenue):
    res = ((debt / revenue).rolling(21).rank(pct=True)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc021_21d_accel_v021_signal'] = f58ds_f58_debt_servicing_capacity_calc021_21d_accel_v021_signal

def f58ds_f58_debt_servicing_capacity_calc022_10d_accel_v022_signal(fcf, intexp):
    res = ((fcf / intexp).rolling(10).mean()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc022_10d_accel_v022_signal'] = f58ds_f58_debt_servicing_capacity_calc022_10d_accel_v022_signal

def f58ds_f58_debt_servicing_capacity_calc023_42d_accel_v023_signal(debt, marketcap):
    res = (np.log(((debt / marketcap)).abs().replace(0, np.nan)).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc023_42d_accel_v023_signal'] = f58ds_f58_debt_servicing_capacity_calc023_42d_accel_v023_signal

def f58ds_f58_debt_servicing_capacity_calc024_10d_accel_v024_signal(equity, liabilities):
    res = (np.log(((liabilities / equity)).abs().replace(0, np.nan)).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc024_10d_accel_v024_signal'] = f58ds_f58_debt_servicing_capacity_calc024_10d_accel_v024_signal

def f58ds_f58_debt_servicing_capacity_calc025_252d_accel_v025_signal(intexp, netinc):
    res = ((((netinc / intexp)) / ((netinc / intexp)).rolling(252).min())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc025_252d_accel_v025_signal'] = f58ds_f58_debt_servicing_capacity_calc025_252d_accel_v025_signal

def f58ds_f58_debt_servicing_capacity_calc026_63d_accel_v026_signal(debt, fcf):
    res = ((fcf / debt).rolling(63).var()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc026_63d_accel_v026_signal'] = f58ds_f58_debt_servicing_capacity_calc026_63d_accel_v026_signal

def f58ds_f58_debt_servicing_capacity_calc027_5d_accel_v027_signal(debt, gp):
    res = ((((debt / gp)) / ((debt / gp)).rolling(5).min())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc027_5d_accel_v027_signal'] = f58ds_f58_debt_servicing_capacity_calc027_5d_accel_v027_signal

def f58ds_f58_debt_servicing_capacity_calc028_63d_accel_v028_signal(debt, equity):
    res = ((debt / equity).rolling(63).mean()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc028_63d_accel_v028_signal'] = f58ds_f58_debt_servicing_capacity_calc028_63d_accel_v028_signal

def f58ds_f58_debt_servicing_capacity_calc029_252d_accel_v029_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(252).quantile(0.75)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc029_252d_accel_v029_signal'] = f58ds_f58_debt_servicing_capacity_calc029_252d_accel_v029_signal

def f58ds_f58_debt_servicing_capacity_calc030_21d_accel_v030_signal(liabilities, netinc):
    res = ((((netinc / liabilities)) - ((netinc / liabilities)).rolling(21).mean()) / ((netinc / liabilities)).rolling(21).std()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc030_21d_accel_v030_signal'] = f58ds_f58_debt_servicing_capacity_calc030_21d_accel_v030_signal

def f58ds_f58_debt_servicing_capacity_calc031_10d_accel_v031_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(10).max()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc031_10d_accel_v031_signal'] = f58ds_f58_debt_servicing_capacity_calc031_10d_accel_v031_signal

def f58ds_f58_debt_servicing_capacity_calc032_63d_accel_v032_signal(debt, ebitda):
    res = ((debt / ebitda).diff(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc032_63d_accel_v032_signal'] = f58ds_f58_debt_servicing_capacity_calc032_63d_accel_v032_signal

def f58ds_f58_debt_servicing_capacity_calc033_42d_accel_v033_signal(debt, equity):
    res = ((debt / equity).rolling(42).kurt()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc033_42d_accel_v033_signal'] = f58ds_f58_debt_servicing_capacity_calc033_42d_accel_v033_signal

def f58ds_f58_debt_servicing_capacity_calc034_63d_accel_v034_signal(debt, ebitda):
    res = ((((debt / ebitda)) / ((debt / ebitda)).rolling(63).max())).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc034_63d_accel_v034_signal'] = f58ds_f58_debt_servicing_capacity_calc034_63d_accel_v034_signal

def f58ds_f58_debt_servicing_capacity_calc035_21d_accel_v035_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(21).var()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc035_21d_accel_v035_signal'] = f58ds_f58_debt_servicing_capacity_calc035_21d_accel_v035_signal

def f58ds_f58_debt_servicing_capacity_calc036_10d_accel_v036_signal(fcf, liabilities):
    res = ((((fcf / liabilities)) - ((fcf / liabilities)).rolling(10).mean()) / ((fcf / liabilities)).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc036_10d_accel_v036_signal'] = f58ds_f58_debt_servicing_capacity_calc036_10d_accel_v036_signal

def f58ds_f58_debt_servicing_capacity_calc037_10d_accel_v037_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(10).quantile(0.75)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc037_10d_accel_v037_signal'] = f58ds_f58_debt_servicing_capacity_calc037_10d_accel_v037_signal

def f58ds_f58_debt_servicing_capacity_calc038_10d_accel_v038_signal(assets, fcf):
    res = ((fcf / assets).rolling(10).quantile(0.25)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc038_10d_accel_v038_signal'] = f58ds_f58_debt_servicing_capacity_calc038_10d_accel_v038_signal

def f58ds_f58_debt_servicing_capacity_calc039_10d_accel_v039_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(10).mean()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc039_10d_accel_v039_signal'] = f58ds_f58_debt_servicing_capacity_calc039_10d_accel_v039_signal

def f58ds_f58_debt_servicing_capacity_calc040_21d_accel_v040_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(21).quantile(0.25)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc040_21d_accel_v040_signal'] = f58ds_f58_debt_servicing_capacity_calc040_21d_accel_v040_signal

def f58ds_f58_debt_servicing_capacity_calc041_10d_accel_v041_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(10).rank(pct=True)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc041_10d_accel_v041_signal'] = f58ds_f58_debt_servicing_capacity_calc041_10d_accel_v041_signal

def f58ds_f58_debt_servicing_capacity_calc042_5d_accel_v042_signal(debt, workingcapital):
    res = ((debt / workingcapital).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc042_5d_accel_v042_signal'] = f58ds_f58_debt_servicing_capacity_calc042_5d_accel_v042_signal

def f58ds_f58_debt_servicing_capacity_calc043_126d_accel_v043_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc043_126d_accel_v043_signal'] = f58ds_f58_debt_servicing_capacity_calc043_126d_accel_v043_signal

def f58ds_f58_debt_servicing_capacity_calc044_252d_accel_v044_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(252).max()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc044_252d_accel_v044_signal'] = f58ds_f58_debt_servicing_capacity_calc044_252d_accel_v044_signal

def f58ds_f58_debt_servicing_capacity_calc045_126d_accel_v045_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(126).var()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc045_126d_accel_v045_signal'] = f58ds_f58_debt_servicing_capacity_calc045_126d_accel_v045_signal

def f58ds_f58_debt_servicing_capacity_calc046_252d_accel_v046_signal(ebitda, liabilities):
    res = ((((liabilities / ebitda)) / ((liabilities / ebitda)).rolling(252).min())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc046_252d_accel_v046_signal'] = f58ds_f58_debt_servicing_capacity_calc046_252d_accel_v046_signal

def f58ds_f58_debt_servicing_capacity_calc047_252d_accel_v047_signal(assets, ebitda):
    res = ((ebitda / assets).diff(252)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc047_252d_accel_v047_signal'] = f58ds_f58_debt_servicing_capacity_calc047_252d_accel_v047_signal

def f58ds_f58_debt_servicing_capacity_calc048_42d_accel_v048_signal(assets, netinc):
    res = ((netinc / assets).rolling(42).max()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc048_42d_accel_v048_signal'] = f58ds_f58_debt_servicing_capacity_calc048_42d_accel_v048_signal

def f58ds_f58_debt_servicing_capacity_calc049_63d_accel_v049_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(63).mean()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc049_63d_accel_v049_signal'] = f58ds_f58_debt_servicing_capacity_calc049_63d_accel_v049_signal

def f58ds_f58_debt_servicing_capacity_calc050_21d_accel_v050_signal(ebitda, intexp):
    res = (np.log(((ebitda / intexp)).abs().replace(0, np.nan)).rolling(21).std()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc050_21d_accel_v050_signal'] = f58ds_f58_debt_servicing_capacity_calc050_21d_accel_v050_signal

def f58ds_f58_debt_servicing_capacity_calc051_21d_accel_v051_signal(debt, marketcap):
    res = ((((debt / marketcap)) / ((debt / marketcap)).rolling(21).max())).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc051_21d_accel_v051_signal'] = f58ds_f58_debt_servicing_capacity_calc051_21d_accel_v051_signal

def f58ds_f58_debt_servicing_capacity_calc052_63d_accel_v052_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(63).rank(pct=True)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc052_63d_accel_v052_signal'] = f58ds_f58_debt_servicing_capacity_calc052_63d_accel_v052_signal

def f58ds_f58_debt_servicing_capacity_calc053_42d_accel_v053_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(42).quantile(0.75)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc053_42d_accel_v053_signal'] = f58ds_f58_debt_servicing_capacity_calc053_42d_accel_v053_signal

def f58ds_f58_debt_servicing_capacity_calc054_126d_accel_v054_signal(debt, gp):
    res = ((debt / gp).rolling(126).mean()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc054_126d_accel_v054_signal'] = f58ds_f58_debt_servicing_capacity_calc054_126d_accel_v054_signal

def f58ds_f58_debt_servicing_capacity_calc055_42d_accel_v055_signal(assets, fcf):
    res = ((fcf / assets).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc055_42d_accel_v055_signal'] = f58ds_f58_debt_servicing_capacity_calc055_42d_accel_v055_signal

def f58ds_f58_debt_servicing_capacity_calc056_252d_accel_v056_signal(ebitda, liabilities):
    res = ((liabilities / ebitda).rolling(252).var()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc056_252d_accel_v056_signal'] = f58ds_f58_debt_servicing_capacity_calc056_252d_accel_v056_signal

def f58ds_f58_debt_servicing_capacity_calc057_252d_accel_v057_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc057_252d_accel_v057_signal'] = f58ds_f58_debt_servicing_capacity_calc057_252d_accel_v057_signal

def f58ds_f58_debt_servicing_capacity_calc058_63d_accel_v058_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(63).quantile(0.5)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc058_63d_accel_v058_signal'] = f58ds_f58_debt_servicing_capacity_calc058_63d_accel_v058_signal

def f58ds_f58_debt_servicing_capacity_calc059_10d_accel_v059_signal(assets, netinc):
    res = ((netinc / assets).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc059_10d_accel_v059_signal'] = f58ds_f58_debt_servicing_capacity_calc059_10d_accel_v059_signal

def f58ds_f58_debt_servicing_capacity_calc060_5d_accel_v060_signal(debt, equity):
    res = ((((debt / equity)) / ((debt / equity)).rolling(5).max())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc060_5d_accel_v060_signal'] = f58ds_f58_debt_servicing_capacity_calc060_5d_accel_v060_signal

def f58ds_f58_debt_servicing_capacity_calc061_126d_accel_v061_signal(currentratio, debt):
    res = ((currentratio / debt).pct_change(126)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc061_126d_accel_v061_signal'] = f58ds_f58_debt_servicing_capacity_calc061_126d_accel_v061_signal

def f58ds_f58_debt_servicing_capacity_calc062_21d_accel_v062_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(21).var()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc062_21d_accel_v062_signal'] = f58ds_f58_debt_servicing_capacity_calc062_21d_accel_v062_signal

def f58ds_f58_debt_servicing_capacity_calc063_63d_accel_v063_signal(debt, workingcapital):
    res = ((((debt / workingcapital)) / ((debt / workingcapital)).rolling(63).min())).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc063_63d_accel_v063_signal'] = f58ds_f58_debt_servicing_capacity_calc063_63d_accel_v063_signal

def f58ds_f58_debt_servicing_capacity_calc064_5d_accel_v064_signal(currentratio, debt):
    res = ((((currentratio / debt)) / ((currentratio / debt)).rolling(5).min())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc064_5d_accel_v064_signal'] = f58ds_f58_debt_servicing_capacity_calc064_5d_accel_v064_signal

def f58ds_f58_debt_servicing_capacity_calc065_42d_accel_v065_signal(assets, fcf):
    res = ((((fcf / assets)) / ((fcf / assets)).rolling(42).min())).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc065_42d_accel_v065_signal'] = f58ds_f58_debt_servicing_capacity_calc065_42d_accel_v065_signal

def f58ds_f58_debt_servicing_capacity_calc066_252d_accel_v066_signal(debt, marketcap):
    res = ((((debt / marketcap)) / ((debt / marketcap)).rolling(252).min())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc066_252d_accel_v066_signal'] = f58ds_f58_debt_servicing_capacity_calc066_252d_accel_v066_signal

def f58ds_f58_debt_servicing_capacity_calc067_21d_accel_v067_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(21).skew()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc067_21d_accel_v067_signal'] = f58ds_f58_debt_servicing_capacity_calc067_21d_accel_v067_signal

def f58ds_f58_debt_servicing_capacity_calc068_63d_accel_v068_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(63).min()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc068_63d_accel_v068_signal'] = f58ds_f58_debt_servicing_capacity_calc068_63d_accel_v068_signal

def f58ds_f58_debt_servicing_capacity_calc069_21d_accel_v069_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(21).quantile(0.5)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc069_21d_accel_v069_signal'] = f58ds_f58_debt_servicing_capacity_calc069_21d_accel_v069_signal

def f58ds_f58_debt_servicing_capacity_calc070_42d_accel_v070_signal(debt, ebitda):
    res = ((((debt / ebitda)) - ((debt / ebitda)).rolling(42).mean()) / ((debt / ebitda)).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc070_42d_accel_v070_signal'] = f58ds_f58_debt_servicing_capacity_calc070_42d_accel_v070_signal

def f58ds_f58_debt_servicing_capacity_calc071_10d_accel_v071_signal(liabilities, opinc):
    res = ((opinc / liabilities).rolling(10).skew()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc071_10d_accel_v071_signal'] = f58ds_f58_debt_servicing_capacity_calc071_10d_accel_v071_signal

def f58ds_f58_debt_servicing_capacity_calc072_63d_accel_v072_signal(currentratio, debt):
    res = (np.log(((currentratio / debt)).abs().replace(0, np.nan)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc072_63d_accel_v072_signal'] = f58ds_f58_debt_servicing_capacity_calc072_63d_accel_v072_signal

def f58ds_f58_debt_servicing_capacity_calc073_63d_accel_v073_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(63).kurt()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc073_63d_accel_v073_signal'] = f58ds_f58_debt_servicing_capacity_calc073_63d_accel_v073_signal

def f58ds_f58_debt_servicing_capacity_calc074_126d_accel_v074_signal(ebitda, liabilities):
    res = ((liabilities / ebitda).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc074_126d_accel_v074_signal'] = f58ds_f58_debt_servicing_capacity_calc074_126d_accel_v074_signal

def f58ds_f58_debt_servicing_capacity_calc075_252d_accel_v075_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(252).quantile(0.5)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc075_252d_accel_v075_signal'] = f58ds_f58_debt_servicing_capacity_calc075_252d_accel_v075_signal

def f58ds_f58_debt_servicing_capacity_calc076_126d_accel_v076_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(126).mean()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc076_126d_accel_v076_signal'] = f58ds_f58_debt_servicing_capacity_calc076_126d_accel_v076_signal

def f58ds_f58_debt_servicing_capacity_calc077_126d_accel_v077_signal(debt, fcf):
    res = ((fcf / debt).pct_change(126)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc077_126d_accel_v077_signal'] = f58ds_f58_debt_servicing_capacity_calc077_126d_accel_v077_signal

def f58ds_f58_debt_servicing_capacity_calc078_126d_accel_v078_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc078_126d_accel_v078_signal'] = f58ds_f58_debt_servicing_capacity_calc078_126d_accel_v078_signal

def f58ds_f58_debt_servicing_capacity_calc079_63d_accel_v079_signal(liabilities, revenue):
    res = ((((liabilities / revenue)) - ((liabilities / revenue)).rolling(63).mean()) / ((liabilities / revenue)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc079_63d_accel_v079_signal'] = f58ds_f58_debt_servicing_capacity_calc079_63d_accel_v079_signal

def f58ds_f58_debt_servicing_capacity_calc080_63d_accel_v080_signal(intexp, netinc):
    res = ((netinc / intexp).diff(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc080_63d_accel_v080_signal'] = f58ds_f58_debt_servicing_capacity_calc080_63d_accel_v080_signal

def f58ds_f58_debt_servicing_capacity_calc081_10d_accel_v081_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(10).mean()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc081_10d_accel_v081_signal'] = f58ds_f58_debt_servicing_capacity_calc081_10d_accel_v081_signal

def f58ds_f58_debt_servicing_capacity_calc082_5d_accel_v082_signal(assets, debt):
    res = ((debt / assets).rolling(5).kurt()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc082_5d_accel_v082_signal'] = f58ds_f58_debt_servicing_capacity_calc082_5d_accel_v082_signal

def f58ds_f58_debt_servicing_capacity_calc083_5d_accel_v083_signal(debt, gp):
    res = ((debt / gp).rolling(5).quantile(0.25)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc083_5d_accel_v083_signal'] = f58ds_f58_debt_servicing_capacity_calc083_5d_accel_v083_signal

def f58ds_f58_debt_servicing_capacity_calc084_63d_accel_v084_signal(debt, equity):
    res = (np.log(((debt / equity)).abs().replace(0, np.nan)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc084_63d_accel_v084_signal'] = f58ds_f58_debt_servicing_capacity_calc084_63d_accel_v084_signal

def f58ds_f58_debt_servicing_capacity_calc085_21d_accel_v085_signal(debt, gp):
    res = ((((debt / gp)) - ((debt / gp)).rolling(21).mean()) / ((debt / gp)).rolling(21).std()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc085_21d_accel_v085_signal'] = f58ds_f58_debt_servicing_capacity_calc085_21d_accel_v085_signal

def f58ds_f58_debt_servicing_capacity_calc086_126d_accel_v086_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(126).quantile(0.75)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc086_126d_accel_v086_signal'] = f58ds_f58_debt_servicing_capacity_calc086_126d_accel_v086_signal

def f58ds_f58_debt_servicing_capacity_calc087_21d_accel_v087_signal(ebitda, ev):
    res = ((ev / ebitda).diff(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc087_21d_accel_v087_signal'] = f58ds_f58_debt_servicing_capacity_calc087_21d_accel_v087_signal

def f58ds_f58_debt_servicing_capacity_calc088_5d_accel_v088_signal(ebitda, liabilities):
    res = (np.log(((liabilities / ebitda)).abs().replace(0, np.nan)).rolling(5).std()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc088_5d_accel_v088_signal'] = f58ds_f58_debt_servicing_capacity_calc088_5d_accel_v088_signal

def f58ds_f58_debt_servicing_capacity_calc089_21d_accel_v089_signal(assets, netinc):
    res = ((netinc / assets).rolling(21).min()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc089_21d_accel_v089_signal'] = f58ds_f58_debt_servicing_capacity_calc089_21d_accel_v089_signal

def f58ds_f58_debt_servicing_capacity_calc090_63d_accel_v090_signal(debt, revenue):
    res = ((debt / revenue).pct_change(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc090_63d_accel_v090_signal'] = f58ds_f58_debt_servicing_capacity_calc090_63d_accel_v090_signal

def f58ds_f58_debt_servicing_capacity_calc091_126d_accel_v091_signal(debt, marketcap):
    res = ((debt / marketcap).rolling(126).kurt()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc091_126d_accel_v091_signal'] = f58ds_f58_debt_servicing_capacity_calc091_126d_accel_v091_signal

def f58ds_f58_debt_servicing_capacity_calc092_10d_accel_v092_signal(debt, workingcapital):
    res = ((debt / workingcapital).rolling(10).var()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc092_10d_accel_v092_signal'] = f58ds_f58_debt_servicing_capacity_calc092_10d_accel_v092_signal

def f58ds_f58_debt_servicing_capacity_calc093_252d_accel_v093_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(252).var()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc093_252d_accel_v093_signal'] = f58ds_f58_debt_servicing_capacity_calc093_252d_accel_v093_signal

def f58ds_f58_debt_servicing_capacity_calc094_5d_accel_v094_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(5).quantile(0.75)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc094_5d_accel_v094_signal'] = f58ds_f58_debt_servicing_capacity_calc094_5d_accel_v094_signal

def f58ds_f58_debt_servicing_capacity_calc095_42d_accel_v095_signal(assets, netinc):
    res = ((((netinc / assets)) / ((netinc / assets)).rolling(42).max())).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc095_42d_accel_v095_signal'] = f58ds_f58_debt_servicing_capacity_calc095_42d_accel_v095_signal

def f58ds_f58_debt_servicing_capacity_calc096_63d_accel_v096_signal(assets, debt):
    res = ((((debt / assets)) - ((debt / assets)).rolling(63).mean()) / ((debt / assets)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc096_63d_accel_v096_signal'] = f58ds_f58_debt_servicing_capacity_calc096_63d_accel_v096_signal

def f58ds_f58_debt_servicing_capacity_calc097_10d_accel_v097_signal(ebitda, liabilities):
    res = (np.log(((liabilities / ebitda)).abs().replace(0, np.nan)).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc097_10d_accel_v097_signal'] = f58ds_f58_debt_servicing_capacity_calc097_10d_accel_v097_signal

def f58ds_f58_debt_servicing_capacity_calc098_252d_accel_v098_signal(intexp, opinc):
    res = ((opinc / intexp).rolling(252).quantile(0.75)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc098_252d_accel_v098_signal'] = f58ds_f58_debt_servicing_capacity_calc098_252d_accel_v098_signal

def f58ds_f58_debt_servicing_capacity_calc099_126d_accel_v099_signal(debt, revenue):
    res = ((debt / revenue).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc099_126d_accel_v099_signal'] = f58ds_f58_debt_servicing_capacity_calc099_126d_accel_v099_signal

def f58ds_f58_debt_servicing_capacity_calc100_126d_accel_v100_signal(ncfo, revenue):
    res = (np.log(((ncfo / revenue)).abs().replace(0, np.nan)).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc100_126d_accel_v100_signal'] = f58ds_f58_debt_servicing_capacity_calc100_126d_accel_v100_signal

def f58ds_f58_debt_servicing_capacity_calc101_42d_accel_v101_signal(assets, debt):
    res = ((debt / assets).rolling(42).max()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc101_42d_accel_v101_signal'] = f58ds_f58_debt_servicing_capacity_calc101_42d_accel_v101_signal

def f58ds_f58_debt_servicing_capacity_calc102_21d_accel_v102_signal(ebitda, liabilities):
    res = ((liabilities / ebitda).rolling(21).mean()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc102_21d_accel_v102_signal'] = f58ds_f58_debt_servicing_capacity_calc102_21d_accel_v102_signal

def f58ds_f58_debt_servicing_capacity_calc103_5d_accel_v103_signal(fcf, intexp):
    res = ((fcf / intexp).rolling(5).kurt()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc103_5d_accel_v103_signal'] = f58ds_f58_debt_servicing_capacity_calc103_5d_accel_v103_signal

def f58ds_f58_debt_servicing_capacity_calc104_10d_accel_v104_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(10).quantile(0.25)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc104_10d_accel_v104_signal'] = f58ds_f58_debt_servicing_capacity_calc104_10d_accel_v104_signal

def f58ds_f58_debt_servicing_capacity_calc105_126d_accel_v105_signal(intexp, revenue):
    res = ((intexp / revenue).rolling(126).var()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc105_126d_accel_v105_signal'] = f58ds_f58_debt_servicing_capacity_calc105_126d_accel_v105_signal

def f58ds_f58_debt_servicing_capacity_calc106_10d_accel_v106_signal(fcf, intexp):
    res = ((((fcf / intexp)) / ((fcf / intexp)).rolling(10).max())).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc106_10d_accel_v106_signal'] = f58ds_f58_debt_servicing_capacity_calc106_10d_accel_v106_signal

def f58ds_f58_debt_servicing_capacity_calc107_21d_accel_v107_signal(debt, equity):
    res = ((debt / equity).pct_change(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc107_21d_accel_v107_signal'] = f58ds_f58_debt_servicing_capacity_calc107_21d_accel_v107_signal

def f58ds_f58_debt_servicing_capacity_calc108_10d_accel_v108_signal(currentratio, debt):
    res = ((currentratio / debt).rolling(10).max()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc108_10d_accel_v108_signal'] = f58ds_f58_debt_servicing_capacity_calc108_10d_accel_v108_signal

def f58ds_f58_debt_servicing_capacity_calc109_21d_accel_v109_signal(debt, gp):
    res = ((debt / gp).rolling(21).std()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc109_21d_accel_v109_signal'] = f58ds_f58_debt_servicing_capacity_calc109_21d_accel_v109_signal

def f58ds_f58_debt_servicing_capacity_calc110_42d_accel_v110_signal(equity, liabilities):
    res = ((liabilities / equity).rolling(42).quantile(0.75)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc110_42d_accel_v110_signal'] = f58ds_f58_debt_servicing_capacity_calc110_42d_accel_v110_signal

def f58ds_f58_debt_servicing_capacity_calc111_252d_accel_v111_signal(debt, gp):
    res = ((debt / gp).rolling(252).max()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc111_252d_accel_v111_signal'] = f58ds_f58_debt_servicing_capacity_calc111_252d_accel_v111_signal

def f58ds_f58_debt_servicing_capacity_calc112_63d_accel_v112_signal(debt, workingcapital):
    res = ((workingcapital / debt).pct_change(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc112_63d_accel_v112_signal'] = f58ds_f58_debt_servicing_capacity_calc112_63d_accel_v112_signal

def f58ds_f58_debt_servicing_capacity_calc113_5d_accel_v113_signal(ebitda, liabilities):
    res = ((ebitda / liabilities).rolling(5).max()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc113_5d_accel_v113_signal'] = f58ds_f58_debt_servicing_capacity_calc113_5d_accel_v113_signal

def f58ds_f58_debt_servicing_capacity_calc114_10d_accel_v114_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(10).kurt()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc114_10d_accel_v114_signal'] = f58ds_f58_debt_servicing_capacity_calc114_10d_accel_v114_signal

def f58ds_f58_debt_servicing_capacity_calc115_126d_accel_v115_signal(intexp, opinc):
    res = ((((intexp / opinc)) / ((intexp / opinc)).rolling(126).min())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc115_126d_accel_v115_signal'] = f58ds_f58_debt_servicing_capacity_calc115_126d_accel_v115_signal

def f58ds_f58_debt_servicing_capacity_calc116_126d_accel_v116_signal(intexp, netinc):
    res = ((netinc / intexp).diff(126)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc116_126d_accel_v116_signal'] = f58ds_f58_debt_servicing_capacity_calc116_126d_accel_v116_signal

def f58ds_f58_debt_servicing_capacity_calc117_252d_accel_v117_signal(debt, ncfo):
    res = (np.log(((ncfo / debt)).abs().replace(0, np.nan)).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc117_252d_accel_v117_signal'] = f58ds_f58_debt_servicing_capacity_calc117_252d_accel_v117_signal

def f58ds_f58_debt_servicing_capacity_calc118_252d_accel_v118_signal(fcf, intexp):
    res = ((fcf / intexp).rolling(252).min()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc118_252d_accel_v118_signal'] = f58ds_f58_debt_servicing_capacity_calc118_252d_accel_v118_signal

def f58ds_f58_debt_servicing_capacity_calc119_42d_accel_v119_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(42).var()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc119_42d_accel_v119_signal'] = f58ds_f58_debt_servicing_capacity_calc119_42d_accel_v119_signal

def f58ds_f58_debt_servicing_capacity_calc120_63d_accel_v120_signal(intexp, netinc):
    res = ((netinc / intexp).rolling(63).quantile(0.75)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc120_63d_accel_v120_signal'] = f58ds_f58_debt_servicing_capacity_calc120_63d_accel_v120_signal

def f58ds_f58_debt_servicing_capacity_calc121_42d_accel_v121_signal(debt, fcf):
    res = ((fcf / debt).rolling(42).kurt()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc121_42d_accel_v121_signal'] = f58ds_f58_debt_servicing_capacity_calc121_42d_accel_v121_signal

def f58ds_f58_debt_servicing_capacity_calc122_5d_accel_v122_signal(ebitda, ev):
    res = ((ev / ebitda).diff(5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc122_5d_accel_v122_signal'] = f58ds_f58_debt_servicing_capacity_calc122_5d_accel_v122_signal

def f58ds_f58_debt_servicing_capacity_calc123_21d_accel_v123_signal(ebitda, intexp):
    res = ((ebitda / intexp).diff(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc123_21d_accel_v123_signal'] = f58ds_f58_debt_servicing_capacity_calc123_21d_accel_v123_signal

def f58ds_f58_debt_servicing_capacity_calc124_252d_accel_v124_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(252).min()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc124_252d_accel_v124_signal'] = f58ds_f58_debt_servicing_capacity_calc124_252d_accel_v124_signal

def f58ds_f58_debt_servicing_capacity_calc125_5d_accel_v125_signal(assets, netinc):
    res = ((netinc / assets).rolling(5).max()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc125_5d_accel_v125_signal'] = f58ds_f58_debt_servicing_capacity_calc125_5d_accel_v125_signal

def f58ds_f58_debt_servicing_capacity_calc126_252d_accel_v126_signal(assets, ebitda):
    res = ((ebitda / assets).pct_change(252)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc126_252d_accel_v126_signal'] = f58ds_f58_debt_servicing_capacity_calc126_252d_accel_v126_signal

def f58ds_f58_debt_servicing_capacity_calc127_5d_accel_v127_signal(debt, ebitda):
    res = ((debt / ebitda).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc127_5d_accel_v127_signal'] = f58ds_f58_debt_servicing_capacity_calc127_5d_accel_v127_signal

def f58ds_f58_debt_servicing_capacity_calc128_126d_accel_v128_signal(ncfo, revenue):
    res = ((ncfo / revenue).rolling(126).mean()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc128_126d_accel_v128_signal'] = f58ds_f58_debt_servicing_capacity_calc128_126d_accel_v128_signal

def f58ds_f58_debt_servicing_capacity_calc129_10d_accel_v129_signal(ebitda, liabilities):
    res = ((ebitda / liabilities).rolling(10).var()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc129_10d_accel_v129_signal'] = f58ds_f58_debt_servicing_capacity_calc129_10d_accel_v129_signal

def f58ds_f58_debt_servicing_capacity_calc130_42d_accel_v130_signal(liabilities, revenue):
    res = ((liabilities / revenue).rolling(42).max()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc130_42d_accel_v130_signal'] = f58ds_f58_debt_servicing_capacity_calc130_42d_accel_v130_signal

def f58ds_f58_debt_servicing_capacity_calc131_63d_accel_v131_signal(debt, gp):
    res = ((gp / debt).rolling(63).quantile(0.75)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc131_63d_accel_v131_signal'] = f58ds_f58_debt_servicing_capacity_calc131_63d_accel_v131_signal

def f58ds_f58_debt_servicing_capacity_calc132_21d_accel_v132_signal(liabilities, revenue):
    res = ((((liabilities / revenue)) / ((liabilities / revenue)).rolling(21).max())).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc132_21d_accel_v132_signal'] = f58ds_f58_debt_servicing_capacity_calc132_21d_accel_v132_signal

def f58ds_f58_debt_servicing_capacity_calc133_126d_accel_v133_signal(debt, revenue):
    res = ((debt / revenue).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc133_126d_accel_v133_signal'] = f58ds_f58_debt_servicing_capacity_calc133_126d_accel_v133_signal

def f58ds_f58_debt_servicing_capacity_calc134_42d_accel_v134_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(42).kurt()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc134_42d_accel_v134_signal'] = f58ds_f58_debt_servicing_capacity_calc134_42d_accel_v134_signal

def f58ds_f58_debt_servicing_capacity_calc135_63d_accel_v135_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(63).max()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc135_63d_accel_v135_signal'] = f58ds_f58_debt_servicing_capacity_calc135_63d_accel_v135_signal

def f58ds_f58_debt_servicing_capacity_calc136_42d_accel_v136_signal(assets, netinc):
    res = ((((netinc / assets)) - ((netinc / assets)).rolling(42).mean()) / ((netinc / assets)).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc136_42d_accel_v136_signal'] = f58ds_f58_debt_servicing_capacity_calc136_42d_accel_v136_signal

def f58ds_f58_debt_servicing_capacity_calc137_126d_accel_v137_signal(fcf, intexp):
    res = ((((fcf / intexp)) / ((fcf / intexp)).rolling(126).max())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc137_126d_accel_v137_signal'] = f58ds_f58_debt_servicing_capacity_calc137_126d_accel_v137_signal

def f58ds_f58_debt_servicing_capacity_calc138_21d_accel_v138_signal(assets, debt):
    res = ((((debt / assets)) / ((debt / assets)).rolling(21).min())).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc138_21d_accel_v138_signal'] = f58ds_f58_debt_servicing_capacity_calc138_21d_accel_v138_signal

def f58ds_f58_debt_servicing_capacity_calc139_10d_accel_v139_signal(ncfo, revenue):
    res = ((ncfo / revenue).pct_change(10)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc139_10d_accel_v139_signal'] = f58ds_f58_debt_servicing_capacity_calc139_10d_accel_v139_signal

def f58ds_f58_debt_servicing_capacity_calc140_10d_accel_v140_signal(intexp, opinc):
    res = ((intexp / opinc).rolling(10).min()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc140_10d_accel_v140_signal'] = f58ds_f58_debt_servicing_capacity_calc140_10d_accel_v140_signal

def f58ds_f58_debt_servicing_capacity_calc141_126d_accel_v141_signal(assets, ebitda):
    res = ((ebitda / assets).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc141_126d_accel_v141_signal'] = f58ds_f58_debt_servicing_capacity_calc141_126d_accel_v141_signal

def f58ds_f58_debt_servicing_capacity_calc142_5d_accel_v142_signal(assets, netinc):
    res = ((netinc / assets).rolling(5).min()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc142_5d_accel_v142_signal'] = f58ds_f58_debt_servicing_capacity_calc142_5d_accel_v142_signal

def f58ds_f58_debt_servicing_capacity_calc143_252d_accel_v143_signal(fcf, liabilities):
    res = ((fcf / liabilities).diff(252)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc143_252d_accel_v143_signal'] = f58ds_f58_debt_servicing_capacity_calc143_252d_accel_v143_signal

def f58ds_f58_debt_servicing_capacity_calc144_126d_accel_v144_signal(debt, revenue):
    res = ((((debt / revenue)) / ((debt / revenue)).rolling(126).max())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc144_126d_accel_v144_signal'] = f58ds_f58_debt_servicing_capacity_calc144_126d_accel_v144_signal

def f58ds_f58_debt_servicing_capacity_calc145_21d_accel_v145_signal(ebitda, liabilities):
    res = ((liabilities / ebitda).rolling(21).kurt()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc145_21d_accel_v145_signal'] = f58ds_f58_debt_servicing_capacity_calc145_21d_accel_v145_signal

def f58ds_f58_debt_servicing_capacity_calc146_63d_accel_v146_signal(ebitda, intexp):
    res = ((ebitda / intexp).rolling(63).rank(pct=True)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc146_63d_accel_v146_signal'] = f58ds_f58_debt_servicing_capacity_calc146_63d_accel_v146_signal

def f58ds_f58_debt_servicing_capacity_calc147_252d_accel_v147_signal(debt, workingcapital):
    res = ((((debt / workingcapital)) / ((debt / workingcapital)).rolling(252).max())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc147_252d_accel_v147_signal'] = f58ds_f58_debt_servicing_capacity_calc147_252d_accel_v147_signal

def f58ds_f58_debt_servicing_capacity_calc148_126d_accel_v148_signal(debt, workingcapital):
    res = ((workingcapital / debt).rolling(126).var()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc148_126d_accel_v148_signal'] = f58ds_f58_debt_servicing_capacity_calc148_126d_accel_v148_signal

def f58ds_f58_debt_servicing_capacity_calc149_10d_accel_v149_signal(ebitda, ev):
    res = ((ev / ebitda).rolling(10).max()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc149_10d_accel_v149_signal'] = f58ds_f58_debt_servicing_capacity_calc149_10d_accel_v149_signal

def f58ds_f58_debt_servicing_capacity_calc150_63d_accel_v150_signal(ebitda, liabilities):
    res = ((ebitda / liabilities).rolling(63).quantile(0.5)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc150_63d_accel_v150_signal'] = f58ds_f58_debt_servicing_capacity_calc150_63d_accel_v150_signal



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
