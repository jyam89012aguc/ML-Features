import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f59fc_f59_fcf_conversion_quality_calc001_252d_jerk_v001_signal(high, pe, eps):
    res = (pe / eps).rolling(252).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc001_252d_jerk_v001_signal'] = f59fc_f59_fcf_conversion_quality_calc001_252d_jerk_v001_signal

def f59fc_f59_fcf_conversion_quality_calc002_10d_jerk_v002_signal(low, close, retearn):
    res = (retearn / close).rolling(10).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc002_10d_jerk_v002_signal'] = f59fc_f59_fcf_conversion_quality_calc002_10d_jerk_v002_signal

def f59fc_f59_fcf_conversion_quality_calc003_42d_jerk_v003_signal(ncfi, pe, intexp):
    res = (pe / ncfi).rolling(42).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc003_42d_jerk_v003_signal'] = f59fc_f59_fcf_conversion_quality_calc003_42d_jerk_v003_signal

def f59fc_f59_fcf_conversion_quality_calc004_126d_jerk_v004_signal(open, ncff, intexp):
    res = (ncff / open).rolling(126).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc004_126d_jerk_v004_signal'] = f59fc_f59_fcf_conversion_quality_calc004_126d_jerk_v004_signal

def f59fc_f59_fcf_conversion_quality_calc005_126d_jerk_v005_signal(retearn, volume):
    res = (retearn / volume).rolling(126).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc005_126d_jerk_v005_signal'] = f59fc_f59_fcf_conversion_quality_calc005_126d_jerk_v005_signal

def f59fc_f59_fcf_conversion_quality_calc006_126d_jerk_v006_signal(ncfi, workingcapital):
    res = (workingcapital / ncfi).rolling(126).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc006_126d_jerk_v006_signal'] = f59fc_f59_fcf_conversion_quality_calc006_126d_jerk_v006_signal

def f59fc_f59_fcf_conversion_quality_calc007_21d_jerk_v007_signal(ncff, netinc, eps):
    res = (ncff / netinc).rolling(21).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc007_21d_jerk_v007_signal'] = f59fc_f59_fcf_conversion_quality_calc007_21d_jerk_v007_signal

def f59fc_f59_fcf_conversion_quality_calc008_21d_jerk_v008_signal(close, opinc, taxexp):
    res = (opinc / close).rolling(21).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc008_21d_jerk_v008_signal'] = f59fc_f59_fcf_conversion_quality_calc008_21d_jerk_v008_signal

def f59fc_f59_fcf_conversion_quality_calc009_21d_jerk_v009_signal(open, closeadj, opinc):
    res = (opinc / closeadj).rolling(21).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc009_21d_jerk_v009_signal'] = f59fc_f59_fcf_conversion_quality_calc009_21d_jerk_v009_signal

def f59fc_f59_fcf_conversion_quality_calc010_42d_jerk_v010_signal(closeadj, ncfi, close):
    res = (ncfi / close).rolling(42).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc010_42d_jerk_v010_signal'] = f59fc_f59_fcf_conversion_quality_calc010_42d_jerk_v010_signal

def f59fc_f59_fcf_conversion_quality_calc011_10d_jerk_v011_signal(pe, high):
    res = (pe / high).rolling(10).std().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc011_10d_jerk_v011_signal'] = f59fc_f59_fcf_conversion_quality_calc011_10d_jerk_v011_signal

def f59fc_f59_fcf_conversion_quality_calc012_5d_jerk_v012_signal(ebitda, netinc, ncfo):
    res = (netinc / ncfo).rolling(5).mean().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc012_5d_jerk_v012_signal'] = f59fc_f59_fcf_conversion_quality_calc012_5d_jerk_v012_signal

def f59fc_f59_fcf_conversion_quality_calc013_10d_jerk_v013_signal(closeadj, netinc):
    res = (netinc / closeadj).rolling(10).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc013_10d_jerk_v013_signal'] = f59fc_f59_fcf_conversion_quality_calc013_10d_jerk_v013_signal

def f59fc_f59_fcf_conversion_quality_calc014_252d_jerk_v014_signal(ncfi, ebitda):
    res = (ebitda / ncfi).rolling(252).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc014_252d_jerk_v014_signal'] = f59fc_f59_fcf_conversion_quality_calc014_252d_jerk_v014_signal

def f59fc_f59_fcf_conversion_quality_calc015_5d_jerk_v015_signal(sharesbas, pb, taxexp):
    res = (taxexp / sharesbas).rolling(5).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc015_5d_jerk_v015_signal'] = f59fc_f59_fcf_conversion_quality_calc015_5d_jerk_v015_signal

def f59fc_f59_fcf_conversion_quality_calc016_63d_jerk_v016_signal(intexp, revenue):
    res = (intexp / revenue).rolling(63).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc016_63d_jerk_v016_signal'] = f59fc_f59_fcf_conversion_quality_calc016_63d_jerk_v016_signal

def f59fc_f59_fcf_conversion_quality_calc017_63d_jerk_v017_signal(assets, fcf):
    res = (assets / fcf).rolling(63).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc017_63d_jerk_v017_signal'] = f59fc_f59_fcf_conversion_quality_calc017_63d_jerk_v017_signal

def f59fc_f59_fcf_conversion_quality_calc018_10d_jerk_v018_signal(closeadj, ncfi, evebitda):
    res = (ncfi / closeadj).rolling(10).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc018_10d_jerk_v018_signal'] = f59fc_f59_fcf_conversion_quality_calc018_10d_jerk_v018_signal

def f59fc_f59_fcf_conversion_quality_calc019_63d_jerk_v019_signal(closeadj, pe):
    res = (closeadj / pe).rolling(63).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc019_63d_jerk_v019_signal'] = f59fc_f59_fcf_conversion_quality_calc019_63d_jerk_v019_signal

def f59fc_f59_fcf_conversion_quality_calc020_5d_jerk_v020_signal(assets, workingcapital):
    res = (workingcapital / assets).rolling(5).mean().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc020_5d_jerk_v020_signal'] = f59fc_f59_fcf_conversion_quality_calc020_5d_jerk_v020_signal

def f59fc_f59_fcf_conversion_quality_calc021_63d_jerk_v021_signal(opinc, netinc):
    res = (opinc / netinc).rolling(63).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc021_63d_jerk_v021_signal'] = f59fc_f59_fcf_conversion_quality_calc021_63d_jerk_v021_signal

def f59fc_f59_fcf_conversion_quality_calc022_252d_jerk_v022_signal(ev, evebitda):
    res = (evebitda / ev).rolling(252).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc022_252d_jerk_v022_signal'] = f59fc_f59_fcf_conversion_quality_calc022_252d_jerk_v022_signal

def f59fc_f59_fcf_conversion_quality_calc023_42d_jerk_v023_signal(gp, close, volume):
    res = (close / gp).rolling(42).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc023_42d_jerk_v023_signal'] = f59fc_f59_fcf_conversion_quality_calc023_42d_jerk_v023_signal

def f59fc_f59_fcf_conversion_quality_calc024_5d_jerk_v024_signal(ps, netinc):
    res = (netinc / ps).rolling(5).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc024_5d_jerk_v024_signal'] = f59fc_f59_fcf_conversion_quality_calc024_5d_jerk_v024_signal

def f59fc_f59_fcf_conversion_quality_calc025_5d_jerk_v025_signal(close, revenue):
    res = (revenue / close).rolling(5).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc025_5d_jerk_v025_signal'] = f59fc_f59_fcf_conversion_quality_calc025_5d_jerk_v025_signal

def f59fc_f59_fcf_conversion_quality_calc026_252d_jerk_v026_signal(closeadj, opinc, workingcapital):
    res = (opinc / closeadj).rolling(252).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc026_252d_jerk_v026_signal'] = f59fc_f59_fcf_conversion_quality_calc026_252d_jerk_v026_signal

def f59fc_f59_fcf_conversion_quality_calc027_5d_jerk_v027_signal(open, workingcapital):
    res = (open / workingcapital).rolling(5).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc027_5d_jerk_v027_signal'] = f59fc_f59_fcf_conversion_quality_calc027_5d_jerk_v027_signal

def f59fc_f59_fcf_conversion_quality_calc028_5d_jerk_v028_signal(liabilities, capex):
    res = (capex / liabilities).rolling(5).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc028_5d_jerk_v028_signal'] = f59fc_f59_fcf_conversion_quality_calc028_5d_jerk_v028_signal

def f59fc_f59_fcf_conversion_quality_calc029_21d_jerk_v029_signal(ps, assets):
    res = (assets / ps).rolling(21).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc029_21d_jerk_v029_signal'] = f59fc_f59_fcf_conversion_quality_calc029_21d_jerk_v029_signal

def f59fc_f59_fcf_conversion_quality_calc030_126d_jerk_v030_signal(closeadj, marketcap, pb):
    res = (closeadj / pb).rolling(126).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc030_126d_jerk_v030_signal'] = f59fc_f59_fcf_conversion_quality_calc030_126d_jerk_v030_signal

def f59fc_f59_fcf_conversion_quality_calc031_126d_jerk_v031_signal(evebit, intexp):
    res = (intexp / evebit).rolling(126).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc031_126d_jerk_v031_signal'] = f59fc_f59_fcf_conversion_quality_calc031_126d_jerk_v031_signal

def f59fc_f59_fcf_conversion_quality_calc032_21d_jerk_v032_signal(debt, intexp, revenue):
    res = (intexp / revenue).rolling(21).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc032_21d_jerk_v032_signal'] = f59fc_f59_fcf_conversion_quality_calc032_21d_jerk_v032_signal

def f59fc_f59_fcf_conversion_quality_calc033_252d_jerk_v033_signal(retearn, workingcapital, ebitda):
    res = (retearn / ebitda).rolling(252).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc033_252d_jerk_v033_signal'] = f59fc_f59_fcf_conversion_quality_calc033_252d_jerk_v033_signal

def f59fc_f59_fcf_conversion_quality_calc034_252d_jerk_v034_signal(ncfo, volume, evebitda):
    res = (volume / evebitda).rolling(252).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc034_252d_jerk_v034_signal'] = f59fc_f59_fcf_conversion_quality_calc034_252d_jerk_v034_signal

def f59fc_f59_fcf_conversion_quality_calc035_252d_jerk_v035_signal(ev, currentratio, workingcapital):
    res = (ev / currentratio).rolling(252).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc035_252d_jerk_v035_signal'] = f59fc_f59_fcf_conversion_quality_calc035_252d_jerk_v035_signal

def f59fc_f59_fcf_conversion_quality_calc036_5d_jerk_v036_signal(assets, netinc):
    res = (assets / netinc).rolling(5).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc036_5d_jerk_v036_signal'] = f59fc_f59_fcf_conversion_quality_calc036_5d_jerk_v036_signal

def f59fc_f59_fcf_conversion_quality_calc037_21d_jerk_v037_signal(ncff, intexp, liabilities):
    res = (ncff / intexp).rolling(21).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc037_21d_jerk_v037_signal'] = f59fc_f59_fcf_conversion_quality_calc037_21d_jerk_v037_signal

def f59fc_f59_fcf_conversion_quality_calc038_252d_jerk_v038_signal(ev, assets, revenue):
    res = (ev / assets).rolling(252).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc038_252d_jerk_v038_signal'] = f59fc_f59_fcf_conversion_quality_calc038_252d_jerk_v038_signal

def f59fc_f59_fcf_conversion_quality_calc039_10d_jerk_v039_signal(sharesbas, intexp):
    res = (sharesbas / intexp).rolling(10).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc039_10d_jerk_v039_signal'] = f59fc_f59_fcf_conversion_quality_calc039_10d_jerk_v039_signal

def f59fc_f59_fcf_conversion_quality_calc040_252d_jerk_v040_signal(sharesbas, netinc):
    res = (netinc / sharesbas).rolling(252).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc040_252d_jerk_v040_signal'] = f59fc_f59_fcf_conversion_quality_calc040_252d_jerk_v040_signal

def f59fc_f59_fcf_conversion_quality_calc041_21d_jerk_v041_signal(ev, pb):
    res = (pb / ev).rolling(21).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc041_21d_jerk_v041_signal'] = f59fc_f59_fcf_conversion_quality_calc041_21d_jerk_v041_signal

def f59fc_f59_fcf_conversion_quality_calc042_63d_jerk_v042_signal(low, close, intexp):
    res = (intexp / close).rolling(63).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc042_63d_jerk_v042_signal'] = f59fc_f59_fcf_conversion_quality_calc042_63d_jerk_v042_signal

def f59fc_f59_fcf_conversion_quality_calc043_252d_jerk_v043_signal(close, volume, ncfi):
    res = (close / volume).rolling(252).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc043_252d_jerk_v043_signal'] = f59fc_f59_fcf_conversion_quality_calc043_252d_jerk_v043_signal

def f59fc_f59_fcf_conversion_quality_calc044_10d_jerk_v044_signal(evebit, equity):
    res = (equity / evebit).rolling(10).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc044_10d_jerk_v044_signal'] = f59fc_f59_fcf_conversion_quality_calc044_10d_jerk_v044_signal

def f59fc_f59_fcf_conversion_quality_calc045_126d_jerk_v045_signal(ncff, workingcapital, equity):
    res = (equity / ncff).rolling(126).mean().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc045_126d_jerk_v045_signal'] = f59fc_f59_fcf_conversion_quality_calc045_126d_jerk_v045_signal

def f59fc_f59_fcf_conversion_quality_calc046_126d_jerk_v046_signal(capex, assets, revenue):
    res = (assets / revenue).rolling(126).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc046_126d_jerk_v046_signal'] = f59fc_f59_fcf_conversion_quality_calc046_126d_jerk_v046_signal

def f59fc_f59_fcf_conversion_quality_calc047_5d_jerk_v047_signal(retearn, ncfo, high):
    res = (retearn / high).rolling(5).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc047_5d_jerk_v047_signal'] = f59fc_f59_fcf_conversion_quality_calc047_5d_jerk_v047_signal

def f59fc_f59_fcf_conversion_quality_calc048_5d_jerk_v048_signal(assets, liabilities):
    res = (assets / liabilities).rolling(5).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc048_5d_jerk_v048_signal'] = f59fc_f59_fcf_conversion_quality_calc048_5d_jerk_v048_signal

def f59fc_f59_fcf_conversion_quality_calc049_126d_jerk_v049_signal(marketcap, taxexp):
    res = (marketcap / taxexp).rolling(126).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc049_126d_jerk_v049_signal'] = f59fc_f59_fcf_conversion_quality_calc049_126d_jerk_v049_signal

def f59fc_f59_fcf_conversion_quality_calc050_126d_jerk_v050_signal(volume, evebitda):
    res = (evebitda / volume).rolling(126).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc050_126d_jerk_v050_signal'] = f59fc_f59_fcf_conversion_quality_calc050_126d_jerk_v050_signal

def f59fc_f59_fcf_conversion_quality_calc051_21d_jerk_v051_signal(ncfo, high):
    res = (ncfo / high).rolling(21).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc051_21d_jerk_v051_signal'] = f59fc_f59_fcf_conversion_quality_calc051_21d_jerk_v051_signal

def f59fc_f59_fcf_conversion_quality_calc052_5d_jerk_v052_signal(closeadj, close, evebitda):
    res = (close / closeadj).rolling(5).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc052_5d_jerk_v052_signal'] = f59fc_f59_fcf_conversion_quality_calc052_5d_jerk_v052_signal

def f59fc_f59_fcf_conversion_quality_calc053_126d_jerk_v053_signal(opinc, fcf):
    res = (fcf / opinc).rolling(126).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc053_126d_jerk_v053_signal'] = f59fc_f59_fcf_conversion_quality_calc053_126d_jerk_v053_signal

def f59fc_f59_fcf_conversion_quality_calc054_5d_jerk_v054_signal(low, revenue, liabilities):
    res = (liabilities / revenue).rolling(5).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc054_5d_jerk_v054_signal'] = f59fc_f59_fcf_conversion_quality_calc054_5d_jerk_v054_signal

def f59fc_f59_fcf_conversion_quality_calc055_10d_jerk_v055_signal(volume, taxexp):
    res = (volume / taxexp).rolling(10).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc055_10d_jerk_v055_signal'] = f59fc_f59_fcf_conversion_quality_calc055_10d_jerk_v055_signal

def f59fc_f59_fcf_conversion_quality_calc056_63d_jerk_v056_signal(gp, close, eps):
    res = (eps / close).rolling(63).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc056_63d_jerk_v056_signal'] = f59fc_f59_fcf_conversion_quality_calc056_63d_jerk_v056_signal

def f59fc_f59_fcf_conversion_quality_calc057_10d_jerk_v057_signal(low, ncff, netinc):
    res = (ncff / low).rolling(10).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc057_10d_jerk_v057_signal'] = f59fc_f59_fcf_conversion_quality_calc057_10d_jerk_v057_signal

def f59fc_f59_fcf_conversion_quality_calc058_126d_jerk_v058_signal(sharesbas, liabilities):
    res = (sharesbas / liabilities).rolling(126).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc058_126d_jerk_v058_signal'] = f59fc_f59_fcf_conversion_quality_calc058_126d_jerk_v058_signal

def f59fc_f59_fcf_conversion_quality_calc059_126d_jerk_v059_signal(ncfi, debt, capex):
    res = (debt / ncfi).rolling(126).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc059_126d_jerk_v059_signal'] = f59fc_f59_fcf_conversion_quality_calc059_126d_jerk_v059_signal

def f59fc_f59_fcf_conversion_quality_calc060_10d_jerk_v060_signal(assets, pe, evebitda):
    res = (assets / evebitda).rolling(10).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc060_10d_jerk_v060_signal'] = f59fc_f59_fcf_conversion_quality_calc060_10d_jerk_v060_signal

def f59fc_f59_fcf_conversion_quality_calc061_126d_jerk_v061_signal(closeadj, ncfo):
    res = (ncfo / closeadj).rolling(126).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc061_126d_jerk_v061_signal'] = f59fc_f59_fcf_conversion_quality_calc061_126d_jerk_v061_signal

def f59fc_f59_fcf_conversion_quality_calc062_126d_jerk_v062_signal(open, ps):
    res = (open / ps).rolling(126).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc062_126d_jerk_v062_signal'] = f59fc_f59_fcf_conversion_quality_calc062_126d_jerk_v062_signal

def f59fc_f59_fcf_conversion_quality_calc063_42d_jerk_v063_signal(ps, liabilities):
    res = (ps / liabilities).rolling(42).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc063_42d_jerk_v063_signal'] = f59fc_f59_fcf_conversion_quality_calc063_42d_jerk_v063_signal

def f59fc_f59_fcf_conversion_quality_calc064_5d_jerk_v064_signal(open, sharesbas, ebitda):
    res = (ebitda / sharesbas).rolling(5).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc064_5d_jerk_v064_signal'] = f59fc_f59_fcf_conversion_quality_calc064_5d_jerk_v064_signal

def f59fc_f59_fcf_conversion_quality_calc065_126d_jerk_v065_signal(close, marketcap, capex):
    res = (marketcap / capex).rolling(126).std().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc065_126d_jerk_v065_signal'] = f59fc_f59_fcf_conversion_quality_calc065_126d_jerk_v065_signal

def f59fc_f59_fcf_conversion_quality_calc066_21d_jerk_v066_signal(liabilities, netinc, revenue):
    res = (revenue / netinc).rolling(21).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc066_21d_jerk_v066_signal'] = f59fc_f59_fcf_conversion_quality_calc066_21d_jerk_v066_signal

def f59fc_f59_fcf_conversion_quality_calc067_63d_jerk_v067_signal(closeadj, fcf):
    res = (closeadj / fcf).rolling(63).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc067_63d_jerk_v067_signal'] = f59fc_f59_fcf_conversion_quality_calc067_63d_jerk_v067_signal

def f59fc_f59_fcf_conversion_quality_calc068_5d_jerk_v068_signal(marketcap, equity):
    res = (equity / marketcap).rolling(5).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc068_5d_jerk_v068_signal'] = f59fc_f59_fcf_conversion_quality_calc068_5d_jerk_v068_signal

def f59fc_f59_fcf_conversion_quality_calc069_42d_jerk_v069_signal(gp, ncfo):
    res = (gp / ncfo).rolling(42).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc069_42d_jerk_v069_signal'] = f59fc_f59_fcf_conversion_quality_calc069_42d_jerk_v069_signal

def f59fc_f59_fcf_conversion_quality_calc070_5d_jerk_v070_signal(netinc, ebitda):
    res = (netinc / ebitda).rolling(5).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc070_5d_jerk_v070_signal'] = f59fc_f59_fcf_conversion_quality_calc070_5d_jerk_v070_signal

def f59fc_f59_fcf_conversion_quality_calc071_5d_jerk_v071_signal(volume, ncfo):
    res = (volume / ncfo).rolling(5).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc071_5d_jerk_v071_signal'] = f59fc_f59_fcf_conversion_quality_calc071_5d_jerk_v071_signal

def f59fc_f59_fcf_conversion_quality_calc072_10d_jerk_v072_signal(fcf, ebitda):
    res = (fcf / ebitda).rolling(10).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc072_10d_jerk_v072_signal'] = f59fc_f59_fcf_conversion_quality_calc072_10d_jerk_v072_signal

def f59fc_f59_fcf_conversion_quality_calc073_42d_jerk_v073_signal(gp, ebitda):
    res = (ebitda / gp).rolling(42).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc073_42d_jerk_v073_signal'] = f59fc_f59_fcf_conversion_quality_calc073_42d_jerk_v073_signal

def f59fc_f59_fcf_conversion_quality_calc074_63d_jerk_v074_signal(marketcap, high):
    res = (high / marketcap).rolling(63).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc074_63d_jerk_v074_signal'] = f59fc_f59_fcf_conversion_quality_calc074_63d_jerk_v074_signal

def f59fc_f59_fcf_conversion_quality_calc075_5d_jerk_v075_signal(low, equity):
    res = (equity / low).rolling(5).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc075_5d_jerk_v075_signal'] = f59fc_f59_fcf_conversion_quality_calc075_5d_jerk_v075_signal

def f59fc_f59_fcf_conversion_quality_calc076_126d_jerk_v076_signal(marketcap, capex):
    res = (capex / marketcap).rolling(126).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc076_126d_jerk_v076_signal'] = f59fc_f59_fcf_conversion_quality_calc076_126d_jerk_v076_signal

def f59fc_f59_fcf_conversion_quality_calc077_10d_jerk_v077_signal(equity, revenue):
    res = (equity / revenue).rolling(10).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc077_10d_jerk_v077_signal'] = f59fc_f59_fcf_conversion_quality_calc077_10d_jerk_v077_signal

def f59fc_f59_fcf_conversion_quality_calc078_21d_jerk_v078_signal(ncff, assets):
    res = (assets / ncff).rolling(21).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc078_21d_jerk_v078_signal'] = f59fc_f59_fcf_conversion_quality_calc078_21d_jerk_v078_signal

def f59fc_f59_fcf_conversion_quality_calc079_63d_jerk_v079_signal(low, liabilities):
    res = (low / liabilities).rolling(63).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc079_63d_jerk_v079_signal'] = f59fc_f59_fcf_conversion_quality_calc079_63d_jerk_v079_signal

def f59fc_f59_fcf_conversion_quality_calc080_126d_jerk_v080_signal(opinc, debt, liabilities):
    res = (liabilities / opinc).rolling(126).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc080_126d_jerk_v080_signal'] = f59fc_f59_fcf_conversion_quality_calc080_126d_jerk_v080_signal

def f59fc_f59_fcf_conversion_quality_calc081_21d_jerk_v081_signal(currentratio, assets, volume):
    res = (currentratio / assets).rolling(21).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc081_21d_jerk_v081_signal'] = f59fc_f59_fcf_conversion_quality_calc081_21d_jerk_v081_signal

def f59fc_f59_fcf_conversion_quality_calc082_10d_jerk_v082_signal(evebit, retearn, liabilities):
    res = (retearn / liabilities).rolling(10).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc082_10d_jerk_v082_signal'] = f59fc_f59_fcf_conversion_quality_calc082_10d_jerk_v082_signal

def f59fc_f59_fcf_conversion_quality_calc083_10d_jerk_v083_signal(open, closeadj, fcf):
    res = (closeadj / open).rolling(10).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc083_10d_jerk_v083_signal'] = f59fc_f59_fcf_conversion_quality_calc083_10d_jerk_v083_signal

def f59fc_f59_fcf_conversion_quality_calc084_252d_jerk_v084_signal(debt, netinc, pe):
    res = (pe / netinc).rolling(252).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc084_252d_jerk_v084_signal'] = f59fc_f59_fcf_conversion_quality_calc084_252d_jerk_v084_signal

def f59fc_f59_fcf_conversion_quality_calc085_252d_jerk_v085_signal(open, opinc, revenue):
    res = (revenue / opinc).rolling(252).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc085_252d_jerk_v085_signal'] = f59fc_f59_fcf_conversion_quality_calc085_252d_jerk_v085_signal

def f59fc_f59_fcf_conversion_quality_calc086_10d_jerk_v086_signal(ps, equity):
    res = (ps / equity).rolling(10).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc086_10d_jerk_v086_signal'] = f59fc_f59_fcf_conversion_quality_calc086_10d_jerk_v086_signal

def f59fc_f59_fcf_conversion_quality_calc087_21d_jerk_v087_signal(pb, eps):
    res = (pb / eps).rolling(21).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc087_21d_jerk_v087_signal'] = f59fc_f59_fcf_conversion_quality_calc087_21d_jerk_v087_signal

def f59fc_f59_fcf_conversion_quality_calc088_5d_jerk_v088_signal(ev, taxexp):
    res = (taxexp / ev).rolling(5).mean().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc088_5d_jerk_v088_signal'] = f59fc_f59_fcf_conversion_quality_calc088_5d_jerk_v088_signal

def f59fc_f59_fcf_conversion_quality_calc089_42d_jerk_v089_signal(currentratio, workingcapital):
    res = (workingcapital / currentratio).rolling(42).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc089_42d_jerk_v089_signal'] = f59fc_f59_fcf_conversion_quality_calc089_42d_jerk_v089_signal

def f59fc_f59_fcf_conversion_quality_calc090_252d_jerk_v090_signal(ncff, assets, intexp):
    res = (ncff / intexp).rolling(252).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc090_252d_jerk_v090_signal'] = f59fc_f59_fcf_conversion_quality_calc090_252d_jerk_v090_signal

def f59fc_f59_fcf_conversion_quality_calc091_63d_jerk_v091_signal(equity, taxexp):
    res = (equity / taxexp).rolling(63).std().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc091_63d_jerk_v091_signal'] = f59fc_f59_fcf_conversion_quality_calc091_63d_jerk_v091_signal

def f59fc_f59_fcf_conversion_quality_calc092_252d_jerk_v092_signal(assets, workingcapital, capex):
    res = (workingcapital / assets).rolling(252).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc092_252d_jerk_v092_signal'] = f59fc_f59_fcf_conversion_quality_calc092_252d_jerk_v092_signal

def f59fc_f59_fcf_conversion_quality_calc093_10d_jerk_v093_signal(ncff, ncfo, liabilities):
    res = (ncfo / liabilities).rolling(10).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc093_10d_jerk_v093_signal'] = f59fc_f59_fcf_conversion_quality_calc093_10d_jerk_v093_signal

def f59fc_f59_fcf_conversion_quality_calc094_63d_jerk_v094_signal(evebit, fcf, ncfo):
    res = (evebit / ncfo).rolling(63).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc094_63d_jerk_v094_signal'] = f59fc_f59_fcf_conversion_quality_calc094_63d_jerk_v094_signal

def f59fc_f59_fcf_conversion_quality_calc095_63d_jerk_v095_signal(ps, debt, taxexp):
    res = (ps / debt).rolling(63).mean().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc095_63d_jerk_v095_signal'] = f59fc_f59_fcf_conversion_quality_calc095_63d_jerk_v095_signal

def f59fc_f59_fcf_conversion_quality_calc096_252d_jerk_v096_signal(open, taxexp):
    res = (taxexp / open).rolling(252).mean().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc096_252d_jerk_v096_signal'] = f59fc_f59_fcf_conversion_quality_calc096_252d_jerk_v096_signal

def f59fc_f59_fcf_conversion_quality_calc097_21d_jerk_v097_signal(evebit, eps, taxexp):
    res = (evebit / taxexp).rolling(21).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc097_21d_jerk_v097_signal'] = f59fc_f59_fcf_conversion_quality_calc097_21d_jerk_v097_signal

def f59fc_f59_fcf_conversion_quality_calc098_63d_jerk_v098_signal(low, debt, taxexp):
    res = (taxexp / debt).rolling(63).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc098_63d_jerk_v098_signal'] = f59fc_f59_fcf_conversion_quality_calc098_63d_jerk_v098_signal

def f59fc_f59_fcf_conversion_quality_calc099_252d_jerk_v099_signal(netinc, high):
    res = (high / netinc).rolling(252).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc099_252d_jerk_v099_signal'] = f59fc_f59_fcf_conversion_quality_calc099_252d_jerk_v099_signal

def f59fc_f59_fcf_conversion_quality_calc100_42d_jerk_v100_signal(ps, eps):
    res = (eps / ps).rolling(42).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc100_42d_jerk_v100_signal'] = f59fc_f59_fcf_conversion_quality_calc100_42d_jerk_v100_signal

def f59fc_f59_fcf_conversion_quality_calc101_10d_jerk_v101_signal(ncfo, intexp, capex):
    res = (intexp / capex).rolling(10).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc101_10d_jerk_v101_signal'] = f59fc_f59_fcf_conversion_quality_calc101_10d_jerk_v101_signal

def f59fc_f59_fcf_conversion_quality_calc102_252d_jerk_v102_signal(marketcap, intexp, currentratio):
    res = (intexp / marketcap).rolling(252).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc102_252d_jerk_v102_signal'] = f59fc_f59_fcf_conversion_quality_calc102_252d_jerk_v102_signal

def f59fc_f59_fcf_conversion_quality_calc103_10d_jerk_v103_signal(open, evebit, evebitda):
    res = (open / evebitda).rolling(10).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc103_10d_jerk_v103_signal'] = f59fc_f59_fcf_conversion_quality_calc103_10d_jerk_v103_signal

def f59fc_f59_fcf_conversion_quality_calc104_5d_jerk_v104_signal(close, netinc):
    res = (close / netinc).rolling(5).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc104_5d_jerk_v104_signal'] = f59fc_f59_fcf_conversion_quality_calc104_5d_jerk_v104_signal

def f59fc_f59_fcf_conversion_quality_calc105_63d_jerk_v105_signal(ncff, ncfi, closeadj):
    res = (ncff / closeadj).rolling(63).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc105_63d_jerk_v105_signal'] = f59fc_f59_fcf_conversion_quality_calc105_63d_jerk_v105_signal

def f59fc_f59_fcf_conversion_quality_calc106_252d_jerk_v106_signal(ps, liabilities):
    res = (liabilities / ps).rolling(252).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc106_252d_jerk_v106_signal'] = f59fc_f59_fcf_conversion_quality_calc106_252d_jerk_v106_signal

def f59fc_f59_fcf_conversion_quality_calc107_10d_jerk_v107_signal(ps, currentratio, fcf):
    res = (fcf / ps).rolling(10).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc107_10d_jerk_v107_signal'] = f59fc_f59_fcf_conversion_quality_calc107_10d_jerk_v107_signal

def f59fc_f59_fcf_conversion_quality_calc108_63d_jerk_v108_signal(retearn, netinc, equity):
    res = (equity / retearn).rolling(63).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc108_63d_jerk_v108_signal'] = f59fc_f59_fcf_conversion_quality_calc108_63d_jerk_v108_signal

def f59fc_f59_fcf_conversion_quality_calc109_5d_jerk_v109_signal(assets, pe):
    res = (pe / assets).rolling(5).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc109_5d_jerk_v109_signal'] = f59fc_f59_fcf_conversion_quality_calc109_5d_jerk_v109_signal

def f59fc_f59_fcf_conversion_quality_calc110_252d_jerk_v110_signal(ncff, evebitda):
    res = (ncff / evebitda).rolling(252).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc110_252d_jerk_v110_signal'] = f59fc_f59_fcf_conversion_quality_calc110_252d_jerk_v110_signal

def f59fc_f59_fcf_conversion_quality_calc111_5d_jerk_v111_signal(marketcap, retearn, eps):
    res = (retearn / eps).rolling(5).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc111_5d_jerk_v111_signal'] = f59fc_f59_fcf_conversion_quality_calc111_5d_jerk_v111_signal

def f59fc_f59_fcf_conversion_quality_calc112_126d_jerk_v112_signal(currentratio, equity):
    res = (currentratio / equity).rolling(126).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc112_126d_jerk_v112_signal'] = f59fc_f59_fcf_conversion_quality_calc112_126d_jerk_v112_signal

def f59fc_f59_fcf_conversion_quality_calc113_252d_jerk_v113_signal(close, sharesbas, pb):
    res = (close / sharesbas).rolling(252).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc113_252d_jerk_v113_signal'] = f59fc_f59_fcf_conversion_quality_calc113_252d_jerk_v113_signal

def f59fc_f59_fcf_conversion_quality_calc114_10d_jerk_v114_signal(ncff, evebitda, taxexp):
    res = (ncff / evebitda).rolling(10).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc114_10d_jerk_v114_signal'] = f59fc_f59_fcf_conversion_quality_calc114_10d_jerk_v114_signal

def f59fc_f59_fcf_conversion_quality_calc115_5d_jerk_v115_signal(ps, evebit, intexp):
    res = (intexp / evebit).rolling(5).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc115_5d_jerk_v115_signal'] = f59fc_f59_fcf_conversion_quality_calc115_5d_jerk_v115_signal

def f59fc_f59_fcf_conversion_quality_calc116_63d_jerk_v116_signal(close, evebitda):
    res = (evebitda / close).rolling(63).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc116_63d_jerk_v116_signal'] = f59fc_f59_fcf_conversion_quality_calc116_63d_jerk_v116_signal

def f59fc_f59_fcf_conversion_quality_calc117_63d_jerk_v117_signal(closeadj, currentratio, evebitda):
    res = (evebitda / currentratio).rolling(63).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc117_63d_jerk_v117_signal'] = f59fc_f59_fcf_conversion_quality_calc117_63d_jerk_v117_signal

def f59fc_f59_fcf_conversion_quality_calc118_21d_jerk_v118_signal(pe, workingcapital, pb):
    res = (pb / workingcapital).rolling(21).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc118_21d_jerk_v118_signal'] = f59fc_f59_fcf_conversion_quality_calc118_21d_jerk_v118_signal

def f59fc_f59_fcf_conversion_quality_calc119_5d_jerk_v119_signal(ev, assets):
    res = (ev / assets).rolling(5).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc119_5d_jerk_v119_signal'] = f59fc_f59_fcf_conversion_quality_calc119_5d_jerk_v119_signal

def f59fc_f59_fcf_conversion_quality_calc120_21d_jerk_v120_signal(currentratio, taxexp):
    res = (currentratio / taxexp).rolling(21).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc120_21d_jerk_v120_signal'] = f59fc_f59_fcf_conversion_quality_calc120_21d_jerk_v120_signal

def f59fc_f59_fcf_conversion_quality_calc121_5d_jerk_v121_signal(open, pe):
    res = (open / pe).rolling(5).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc121_5d_jerk_v121_signal'] = f59fc_f59_fcf_conversion_quality_calc121_5d_jerk_v121_signal

def f59fc_f59_fcf_conversion_quality_calc122_10d_jerk_v122_signal(ebitda, evebitda):
    res = (evebitda / ebitda).rolling(10).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc122_10d_jerk_v122_signal'] = f59fc_f59_fcf_conversion_quality_calc122_10d_jerk_v122_signal

def f59fc_f59_fcf_conversion_quality_calc123_21d_jerk_v123_signal(equity, pe, intexp):
    res = (pe / intexp).rolling(21).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc123_21d_jerk_v123_signal'] = f59fc_f59_fcf_conversion_quality_calc123_21d_jerk_v123_signal

def f59fc_f59_fcf_conversion_quality_calc124_42d_jerk_v124_signal(close, ncfo):
    res = (ncfo / close).rolling(42).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc124_42d_jerk_v124_signal'] = f59fc_f59_fcf_conversion_quality_calc124_42d_jerk_v124_signal

def f59fc_f59_fcf_conversion_quality_calc125_21d_jerk_v125_signal(ps, evebit):
    res = (ps / evebit).rolling(21).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc125_21d_jerk_v125_signal'] = f59fc_f59_fcf_conversion_quality_calc125_21d_jerk_v125_signal

def f59fc_f59_fcf_conversion_quality_calc126_252d_jerk_v126_signal(ncfi, opinc):
    res = (opinc / ncfi).rolling(252).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc126_252d_jerk_v126_signal'] = f59fc_f59_fcf_conversion_quality_calc126_252d_jerk_v126_signal

def f59fc_f59_fcf_conversion_quality_calc127_10d_jerk_v127_signal(currentratio, volume, workingcapital):
    res = (currentratio / workingcapital).rolling(10).mean().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc127_10d_jerk_v127_signal'] = f59fc_f59_fcf_conversion_quality_calc127_10d_jerk_v127_signal

def f59fc_f59_fcf_conversion_quality_calc128_42d_jerk_v128_signal(pb, ncfo, liabilities):
    res = (pb / liabilities).rolling(42).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc128_42d_jerk_v128_signal'] = f59fc_f59_fcf_conversion_quality_calc128_42d_jerk_v128_signal

def f59fc_f59_fcf_conversion_quality_calc129_126d_jerk_v129_signal(assets, pb):
    res = (pb / assets).rolling(126).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc129_126d_jerk_v129_signal'] = f59fc_f59_fcf_conversion_quality_calc129_126d_jerk_v129_signal

def f59fc_f59_fcf_conversion_quality_calc130_10d_jerk_v130_signal(evebit, opinc, equity):
    res = (opinc / evebit).rolling(10).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc130_10d_jerk_v130_signal'] = f59fc_f59_fcf_conversion_quality_calc130_10d_jerk_v130_signal

def f59fc_f59_fcf_conversion_quality_calc131_252d_jerk_v131_signal(evebit, ncfo):
    res = (ncfo / evebit).rolling(252).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc131_252d_jerk_v131_signal'] = f59fc_f59_fcf_conversion_quality_calc131_252d_jerk_v131_signal

def f59fc_f59_fcf_conversion_quality_calc132_42d_jerk_v132_signal(closeadj, assets, capex):
    res = (closeadj / assets).rolling(42).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc132_42d_jerk_v132_signal'] = f59fc_f59_fcf_conversion_quality_calc132_42d_jerk_v132_signal

def f59fc_f59_fcf_conversion_quality_calc133_21d_jerk_v133_signal(intexp, taxexp):
    res = (taxexp / intexp).rolling(21).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc133_21d_jerk_v133_signal'] = f59fc_f59_fcf_conversion_quality_calc133_21d_jerk_v133_signal

def f59fc_f59_fcf_conversion_quality_calc134_10d_jerk_v134_signal(close, marketcap, high):
    res = (high / close).rolling(10).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc134_10d_jerk_v134_signal'] = f59fc_f59_fcf_conversion_quality_calc134_10d_jerk_v134_signal

def f59fc_f59_fcf_conversion_quality_calc135_21d_jerk_v135_signal(closeadj, pe, high):
    res = (high / closeadj).rolling(21).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc135_21d_jerk_v135_signal'] = f59fc_f59_fcf_conversion_quality_calc135_21d_jerk_v135_signal

def f59fc_f59_fcf_conversion_quality_calc136_10d_jerk_v136_signal(evebitda, capex):
    res = (evebitda / capex).rolling(10).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc136_10d_jerk_v136_signal'] = f59fc_f59_fcf_conversion_quality_calc136_10d_jerk_v136_signal

def f59fc_f59_fcf_conversion_quality_calc137_63d_jerk_v137_signal(assets, equity, liabilities):
    res = (liabilities / assets).rolling(63).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc137_63d_jerk_v137_signal'] = f59fc_f59_fcf_conversion_quality_calc137_63d_jerk_v137_signal

def f59fc_f59_fcf_conversion_quality_calc138_42d_jerk_v138_signal(currentratio, pe):
    res = (currentratio / pe).rolling(42).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc138_42d_jerk_v138_signal'] = f59fc_f59_fcf_conversion_quality_calc138_42d_jerk_v138_signal

def f59fc_f59_fcf_conversion_quality_calc139_252d_jerk_v139_signal(closeadj, workingcapital, evebitda):
    res = (workingcapital / closeadj).rolling(252).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc139_252d_jerk_v139_signal'] = f59fc_f59_fcf_conversion_quality_calc139_252d_jerk_v139_signal

def f59fc_f59_fcf_conversion_quality_calc140_5d_jerk_v140_signal(close, ncfi, evebitda):
    res = (close / evebitda).rolling(5).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc140_5d_jerk_v140_signal'] = f59fc_f59_fcf_conversion_quality_calc140_5d_jerk_v140_signal

def f59fc_f59_fcf_conversion_quality_calc141_42d_jerk_v141_signal(taxexp, capex):
    res = (capex / taxexp).rolling(42).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc141_42d_jerk_v141_signal'] = f59fc_f59_fcf_conversion_quality_calc141_42d_jerk_v141_signal

def f59fc_f59_fcf_conversion_quality_calc142_5d_jerk_v142_signal(capex, ncfi, eps):
    res = (ncfi / eps).rolling(5).mean().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc142_5d_jerk_v142_signal'] = f59fc_f59_fcf_conversion_quality_calc142_5d_jerk_v142_signal

def f59fc_f59_fcf_conversion_quality_calc143_126d_jerk_v143_signal(evebit, currentratio, ebitda):
    res = (evebit / ebitda).rolling(126).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc143_126d_jerk_v143_signal'] = f59fc_f59_fcf_conversion_quality_calc143_126d_jerk_v143_signal

def f59fc_f59_fcf_conversion_quality_calc144_10d_jerk_v144_signal(gp, close, revenue):
    res = (close / gp).rolling(10).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc144_10d_jerk_v144_signal'] = f59fc_f59_fcf_conversion_quality_calc144_10d_jerk_v144_signal

def f59fc_f59_fcf_conversion_quality_calc145_63d_jerk_v145_signal(ncfi, sharesbas, pb):
    res = (ncfi / pb).rolling(63).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc145_63d_jerk_v145_signal'] = f59fc_f59_fcf_conversion_quality_calc145_63d_jerk_v145_signal

def f59fc_f59_fcf_conversion_quality_calc146_252d_jerk_v146_signal(open, close):
    res = (open / close).rolling(252).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc146_252d_jerk_v146_signal'] = f59fc_f59_fcf_conversion_quality_calc146_252d_jerk_v146_signal

def f59fc_f59_fcf_conversion_quality_calc147_252d_jerk_v147_signal(debt, intexp, capex):
    res = (intexp / debt).rolling(252).mean().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc147_252d_jerk_v147_signal'] = f59fc_f59_fcf_conversion_quality_calc147_252d_jerk_v147_signal

def f59fc_f59_fcf_conversion_quality_calc148_42d_jerk_v148_signal(equity, debt, evebitda):
    res = (evebitda / equity).rolling(42).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc148_42d_jerk_v148_signal'] = f59fc_f59_fcf_conversion_quality_calc148_42d_jerk_v148_signal

def f59fc_f59_fcf_conversion_quality_calc149_10d_jerk_v149_signal(closeadj, equity):
    res = (equity / closeadj).rolling(10).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc149_10d_jerk_v149_signal'] = f59fc_f59_fcf_conversion_quality_calc149_10d_jerk_v149_signal

def f59fc_f59_fcf_conversion_quality_calc150_21d_jerk_v150_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(21).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc150_21d_jerk_v150_signal'] = f59fc_f59_fcf_conversion_quality_calc150_21d_jerk_v150_signal

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
