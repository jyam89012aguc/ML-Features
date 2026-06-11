import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f59fc_f59_fcf_conversion_quality_calc001_5d_slope_v001_signal(low, equity):
    res = (low / equity).rolling(5).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc001_5d_slope_v001_signal'] = f59fc_f59_fcf_conversion_quality_calc001_5d_slope_v001_signal

def f59fc_f59_fcf_conversion_quality_calc002_42d_slope_v002_signal(intexp, equity):
    res = (equity / intexp).rolling(42).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc002_42d_slope_v002_signal'] = f59fc_f59_fcf_conversion_quality_calc002_42d_slope_v002_signal

def f59fc_f59_fcf_conversion_quality_calc003_126d_slope_v003_signal(ps, marketcap, ncfo):
    res = (ncfo / marketcap).rolling(126).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc003_126d_slope_v003_signal'] = f59fc_f59_fcf_conversion_quality_calc003_126d_slope_v003_signal

def f59fc_f59_fcf_conversion_quality_calc004_21d_slope_v004_signal(ps, close, ncfo):
    res = (ncfo / ps).rolling(21).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc004_21d_slope_v004_signal'] = f59fc_f59_fcf_conversion_quality_calc004_21d_slope_v004_signal

def f59fc_f59_fcf_conversion_quality_calc005_252d_slope_v005_signal(ps, sharesbas, taxexp):
    res = (taxexp / ps).rolling(252).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc005_252d_slope_v005_signal'] = f59fc_f59_fcf_conversion_quality_calc005_252d_slope_v005_signal

def f59fc_f59_fcf_conversion_quality_calc006_21d_slope_v006_signal(sharesbas, evebitda):
    res = (sharesbas / evebitda).rolling(21).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc006_21d_slope_v006_signal'] = f59fc_f59_fcf_conversion_quality_calc006_21d_slope_v006_signal

def f59fc_f59_fcf_conversion_quality_calc007_21d_slope_v007_signal(volume, netinc):
    res = (netinc / volume).rolling(21).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc007_21d_slope_v007_signal'] = f59fc_f59_fcf_conversion_quality_calc007_21d_slope_v007_signal

def f59fc_f59_fcf_conversion_quality_calc008_42d_slope_v008_signal(open, ebitda, high):
    res = (open / high).rolling(42).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc008_42d_slope_v008_signal'] = f59fc_f59_fcf_conversion_quality_calc008_42d_slope_v008_signal

def f59fc_f59_fcf_conversion_quality_calc009_63d_slope_v009_signal(low, ncfi, assets):
    res = (low / ncfi).rolling(63).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc009_63d_slope_v009_signal'] = f59fc_f59_fcf_conversion_quality_calc009_63d_slope_v009_signal

def f59fc_f59_fcf_conversion_quality_calc010_42d_slope_v010_signal(opinc, currentratio):
    res = (currentratio / opinc).rolling(42).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc010_42d_slope_v010_signal'] = f59fc_f59_fcf_conversion_quality_calc010_42d_slope_v010_signal

def f59fc_f59_fcf_conversion_quality_calc011_5d_slope_v011_signal(ncff, evebitda):
    res = (ncff / evebitda).rolling(5).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc011_5d_slope_v011_signal'] = f59fc_f59_fcf_conversion_quality_calc011_5d_slope_v011_signal

def f59fc_f59_fcf_conversion_quality_calc012_21d_slope_v012_signal(low, assets, pe):
    res = (assets / pe).rolling(21).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc012_21d_slope_v012_signal'] = f59fc_f59_fcf_conversion_quality_calc012_21d_slope_v012_signal

def f59fc_f59_fcf_conversion_quality_calc013_10d_slope_v013_signal(low, volume, revenue):
    res = (revenue / low).rolling(10).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc013_10d_slope_v013_signal'] = f59fc_f59_fcf_conversion_quality_calc013_10d_slope_v013_signal

def f59fc_f59_fcf_conversion_quality_calc014_5d_slope_v014_signal(debt, evebitda):
    res = (debt / evebitda).rolling(5).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc014_5d_slope_v014_signal'] = f59fc_f59_fcf_conversion_quality_calc014_5d_slope_v014_signal

def f59fc_f59_fcf_conversion_quality_calc015_42d_slope_v015_signal(opinc, marketcap):
    res = (marketcap / opinc).rolling(42).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc015_42d_slope_v015_signal'] = f59fc_f59_fcf_conversion_quality_calc015_42d_slope_v015_signal

def f59fc_f59_fcf_conversion_quality_calc016_21d_slope_v016_signal(open, volume):
    res = (volume / open).rolling(21).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc016_21d_slope_v016_signal'] = f59fc_f59_fcf_conversion_quality_calc016_21d_slope_v016_signal

def f59fc_f59_fcf_conversion_quality_calc017_126d_slope_v017_signal(debt, pb, ebitda):
    res = (debt / ebitda).rolling(126).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc017_126d_slope_v017_signal'] = f59fc_f59_fcf_conversion_quality_calc017_126d_slope_v017_signal

def f59fc_f59_fcf_conversion_quality_calc018_252d_slope_v018_signal(assets, high):
    res = (assets / high).rolling(252).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc018_252d_slope_v018_signal'] = f59fc_f59_fcf_conversion_quality_calc018_252d_slope_v018_signal

def f59fc_f59_fcf_conversion_quality_calc019_252d_slope_v019_signal(closeadj, ebitda, high):
    res = (ebitda / high).rolling(252).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc019_252d_slope_v019_signal'] = f59fc_f59_fcf_conversion_quality_calc019_252d_slope_v019_signal

def f59fc_f59_fcf_conversion_quality_calc020_10d_slope_v020_signal(evebit, ncfi, intexp):
    res = (ncfi / evebit).rolling(10).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc020_10d_slope_v020_signal'] = f59fc_f59_fcf_conversion_quality_calc020_10d_slope_v020_signal

def f59fc_f59_fcf_conversion_quality_calc021_5d_slope_v021_signal(low, pb, equity):
    res = (equity / low).rolling(5).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc021_5d_slope_v021_signal'] = f59fc_f59_fcf_conversion_quality_calc021_5d_slope_v021_signal

def f59fc_f59_fcf_conversion_quality_calc022_10d_slope_v022_signal(taxexp, retearn, eps):
    res = (eps / retearn).rolling(10).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc022_10d_slope_v022_signal'] = f59fc_f59_fcf_conversion_quality_calc022_10d_slope_v022_signal

def f59fc_f59_fcf_conversion_quality_calc023_21d_slope_v023_signal(ncfi, pe, liabilities):
    res = (ncfi / liabilities).rolling(21).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc023_21d_slope_v023_signal'] = f59fc_f59_fcf_conversion_quality_calc023_21d_slope_v023_signal

def f59fc_f59_fcf_conversion_quality_calc024_21d_slope_v024_signal(ps, closeadj):
    res = (ps / closeadj).rolling(21).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc024_21d_slope_v024_signal'] = f59fc_f59_fcf_conversion_quality_calc024_21d_slope_v024_signal

def f59fc_f59_fcf_conversion_quality_calc025_10d_slope_v025_signal(pe, liabilities):
    res = (liabilities / pe).rolling(10).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc025_10d_slope_v025_signal'] = f59fc_f59_fcf_conversion_quality_calc025_10d_slope_v025_signal

def f59fc_f59_fcf_conversion_quality_calc026_252d_slope_v026_signal(open, capex):
    res = (open / capex).rolling(252).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc026_252d_slope_v026_signal'] = f59fc_f59_fcf_conversion_quality_calc026_252d_slope_v026_signal

def f59fc_f59_fcf_conversion_quality_calc027_42d_slope_v027_signal(evebit, retearn):
    res = (retearn / evebit).rolling(42).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc027_42d_slope_v027_signal'] = f59fc_f59_fcf_conversion_quality_calc027_42d_slope_v027_signal

def f59fc_f59_fcf_conversion_quality_calc028_126d_slope_v028_signal(low, fcf, intexp):
    res = (low / fcf).rolling(126).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc028_126d_slope_v028_signal'] = f59fc_f59_fcf_conversion_quality_calc028_126d_slope_v028_signal

def f59fc_f59_fcf_conversion_quality_calc029_42d_slope_v029_signal(netinc, equity, capex):
    res = (netinc / equity).rolling(42).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc029_42d_slope_v029_signal'] = f59fc_f59_fcf_conversion_quality_calc029_42d_slope_v029_signal

def f59fc_f59_fcf_conversion_quality_calc030_42d_slope_v030_signal(assets, pb, volume):
    res = (assets / pb).rolling(42).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc030_42d_slope_v030_signal'] = f59fc_f59_fcf_conversion_quality_calc030_42d_slope_v030_signal

def f59fc_f59_fcf_conversion_quality_calc031_21d_slope_v031_signal(evebit, revenue):
    res = (revenue / evebit).rolling(21).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc031_21d_slope_v031_signal'] = f59fc_f59_fcf_conversion_quality_calc031_21d_slope_v031_signal

def f59fc_f59_fcf_conversion_quality_calc032_42d_slope_v032_signal(low, assets, capex):
    res = (low / assets).rolling(42).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc032_42d_slope_v032_signal'] = f59fc_f59_fcf_conversion_quality_calc032_42d_slope_v032_signal

def f59fc_f59_fcf_conversion_quality_calc033_10d_slope_v033_signal(ev, ncff, sharesbas):
    res = (sharesbas / ev).rolling(10).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc033_10d_slope_v033_signal'] = f59fc_f59_fcf_conversion_quality_calc033_10d_slope_v033_signal

def f59fc_f59_fcf_conversion_quality_calc034_63d_slope_v034_signal(sharesbas, evebitda, revenue):
    res = (sharesbas / evebitda).rolling(63).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc034_63d_slope_v034_signal'] = f59fc_f59_fcf_conversion_quality_calc034_63d_slope_v034_signal

def f59fc_f59_fcf_conversion_quality_calc035_5d_slope_v035_signal(low, eps):
    res = (low / eps).rolling(5).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc035_5d_slope_v035_signal'] = f59fc_f59_fcf_conversion_quality_calc035_5d_slope_v035_signal

def f59fc_f59_fcf_conversion_quality_calc036_126d_slope_v036_signal(closeadj, sharesbas, high):
    res = (closeadj / high).rolling(126).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc036_126d_slope_v036_signal'] = f59fc_f59_fcf_conversion_quality_calc036_126d_slope_v036_signal

def f59fc_f59_fcf_conversion_quality_calc037_10d_slope_v037_signal(low, sharesbas, liabilities):
    res = (liabilities / low).rolling(10).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc037_10d_slope_v037_signal'] = f59fc_f59_fcf_conversion_quality_calc037_10d_slope_v037_signal

def f59fc_f59_fcf_conversion_quality_calc038_63d_slope_v038_signal(close, eps, taxexp):
    res = (taxexp / close).rolling(63).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc038_63d_slope_v038_signal'] = f59fc_f59_fcf_conversion_quality_calc038_63d_slope_v038_signal

def f59fc_f59_fcf_conversion_quality_calc039_10d_slope_v039_signal(evebit, liabilities):
    res = (liabilities / evebit).rolling(10).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc039_10d_slope_v039_signal'] = f59fc_f59_fcf_conversion_quality_calc039_10d_slope_v039_signal

def f59fc_f59_fcf_conversion_quality_calc040_63d_slope_v040_signal(ncff, ncfi, ncfo):
    res = (ncff / ncfo).rolling(63).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc040_63d_slope_v040_signal'] = f59fc_f59_fcf_conversion_quality_calc040_63d_slope_v040_signal

def f59fc_f59_fcf_conversion_quality_calc041_10d_slope_v041_signal(close, evebitda):
    res = (close / evebitda).rolling(10).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc041_10d_slope_v041_signal'] = f59fc_f59_fcf_conversion_quality_calc041_10d_slope_v041_signal

def f59fc_f59_fcf_conversion_quality_calc042_63d_slope_v042_signal(ev, ncff):
    res = (ev / ncff).rolling(63).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc042_63d_slope_v042_signal'] = f59fc_f59_fcf_conversion_quality_calc042_63d_slope_v042_signal

def f59fc_f59_fcf_conversion_quality_calc043_42d_slope_v043_signal(ev, currentratio, low):
    res = (currentratio / ev).rolling(42).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc043_42d_slope_v043_signal'] = f59fc_f59_fcf_conversion_quality_calc043_42d_slope_v043_signal

def f59fc_f59_fcf_conversion_quality_calc044_21d_slope_v044_signal(ncfi, currentratio, assets):
    res = (assets / currentratio).rolling(21).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc044_21d_slope_v044_signal'] = f59fc_f59_fcf_conversion_quality_calc044_21d_slope_v044_signal

def f59fc_f59_fcf_conversion_quality_calc045_126d_slope_v045_signal(closeadj, revenue):
    res = (closeadj / revenue).rolling(126).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc045_126d_slope_v045_signal'] = f59fc_f59_fcf_conversion_quality_calc045_126d_slope_v045_signal

def f59fc_f59_fcf_conversion_quality_calc046_42d_slope_v046_signal(ev, ncfo):
    res = (ev / ncfo).rolling(42).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc046_42d_slope_v046_signal'] = f59fc_f59_fcf_conversion_quality_calc046_42d_slope_v046_signal

def f59fc_f59_fcf_conversion_quality_calc047_63d_slope_v047_signal(ncfi, currentratio):
    res = (currentratio / ncfi).rolling(63).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc047_63d_slope_v047_signal'] = f59fc_f59_fcf_conversion_quality_calc047_63d_slope_v047_signal

def f59fc_f59_fcf_conversion_quality_calc048_252d_slope_v048_signal(debt, retearn, sharesbas):
    res = (retearn / sharesbas).rolling(252).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc048_252d_slope_v048_signal'] = f59fc_f59_fcf_conversion_quality_calc048_252d_slope_v048_signal

def f59fc_f59_fcf_conversion_quality_calc049_42d_slope_v049_signal(currentratio, high):
    res = (high / currentratio).rolling(42).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc049_42d_slope_v049_signal'] = f59fc_f59_fcf_conversion_quality_calc049_42d_slope_v049_signal

def f59fc_f59_fcf_conversion_quality_calc050_5d_slope_v050_signal(equity, ncfo):
    res = (ncfo / equity).rolling(5).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc050_5d_slope_v050_signal'] = f59fc_f59_fcf_conversion_quality_calc050_5d_slope_v050_signal

def f59fc_f59_fcf_conversion_quality_calc051_42d_slope_v051_signal(pe, ncfo, liabilities):
    res = (ncfo / liabilities).rolling(42).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc051_42d_slope_v051_signal'] = f59fc_f59_fcf_conversion_quality_calc051_42d_slope_v051_signal

def f59fc_f59_fcf_conversion_quality_calc052_63d_slope_v052_signal(ncfi, high, eps):
    res = (eps / ncfi).rolling(63).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc052_63d_slope_v052_signal'] = f59fc_f59_fcf_conversion_quality_calc052_63d_slope_v052_signal

def f59fc_f59_fcf_conversion_quality_calc053_252d_slope_v053_signal(marketcap, ebitda, capex):
    res = (marketcap / capex).rolling(252).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc053_252d_slope_v053_signal'] = f59fc_f59_fcf_conversion_quality_calc053_252d_slope_v053_signal

def f59fc_f59_fcf_conversion_quality_calc054_63d_slope_v054_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(63).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc054_63d_slope_v054_signal'] = f59fc_f59_fcf_conversion_quality_calc054_63d_slope_v054_signal

def f59fc_f59_fcf_conversion_quality_calc055_126d_slope_v055_signal(closeadj, intexp):
    res = (closeadj / intexp).rolling(126).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc055_126d_slope_v055_signal'] = f59fc_f59_fcf_conversion_quality_calc055_126d_slope_v055_signal

def f59fc_f59_fcf_conversion_quality_calc056_252d_slope_v056_signal(ncff, capex):
    res = (capex / ncff).rolling(252).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc056_252d_slope_v056_signal'] = f59fc_f59_fcf_conversion_quality_calc056_252d_slope_v056_signal

def f59fc_f59_fcf_conversion_quality_calc057_5d_slope_v057_signal(close, retearn):
    res = (retearn / close).rolling(5).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc057_5d_slope_v057_signal'] = f59fc_f59_fcf_conversion_quality_calc057_5d_slope_v057_signal

def f59fc_f59_fcf_conversion_quality_calc058_252d_slope_v058_signal(closeadj, equity, ebitda):
    res = (ebitda / equity).rolling(252).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc058_252d_slope_v058_signal'] = f59fc_f59_fcf_conversion_quality_calc058_252d_slope_v058_signal

def f59fc_f59_fcf_conversion_quality_calc059_21d_slope_v059_signal(ev, ncff):
    res = (ncff / ev).rolling(21).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc059_21d_slope_v059_signal'] = f59fc_f59_fcf_conversion_quality_calc059_21d_slope_v059_signal

def f59fc_f59_fcf_conversion_quality_calc060_252d_slope_v060_signal(pb, ncfo, high):
    res = (pb / ncfo).rolling(252).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc060_252d_slope_v060_signal'] = f59fc_f59_fcf_conversion_quality_calc060_252d_slope_v060_signal

def f59fc_f59_fcf_conversion_quality_calc061_42d_slope_v061_signal(ev, opinc, equity):
    res = (opinc / equity).rolling(42).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc061_42d_slope_v061_signal'] = f59fc_f59_fcf_conversion_quality_calc061_42d_slope_v061_signal

def f59fc_f59_fcf_conversion_quality_calc062_63d_slope_v062_signal(ncfi, fcf, capex):
    res = (ncfi / fcf).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc062_63d_slope_v062_signal'] = f59fc_f59_fcf_conversion_quality_calc062_63d_slope_v062_signal

def f59fc_f59_fcf_conversion_quality_calc063_42d_slope_v063_signal(closeadj, currentratio):
    res = (currentratio / closeadj).rolling(42).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc063_42d_slope_v063_signal'] = f59fc_f59_fcf_conversion_quality_calc063_42d_slope_v063_signal

def f59fc_f59_fcf_conversion_quality_calc064_63d_slope_v064_signal(workingcapital, equity):
    res = (workingcapital / equity).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc064_63d_slope_v064_signal'] = f59fc_f59_fcf_conversion_quality_calc064_63d_slope_v064_signal

def f59fc_f59_fcf_conversion_quality_calc065_10d_slope_v065_signal(gp, ncfo, capex):
    res = (gp / capex).rolling(10).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc065_10d_slope_v065_signal'] = f59fc_f59_fcf_conversion_quality_calc065_10d_slope_v065_signal

def f59fc_f59_fcf_conversion_quality_calc066_5d_slope_v066_signal(pe, taxexp):
    res = (taxexp / pe).rolling(5).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc066_5d_slope_v066_signal'] = f59fc_f59_fcf_conversion_quality_calc066_5d_slope_v066_signal

def f59fc_f59_fcf_conversion_quality_calc067_5d_slope_v067_signal(currentratio, pe):
    res = (pe / currentratio).rolling(5).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc067_5d_slope_v067_signal'] = f59fc_f59_fcf_conversion_quality_calc067_5d_slope_v067_signal

def f59fc_f59_fcf_conversion_quality_calc068_42d_slope_v068_signal(ncfo, volume, equity):
    res = (volume / equity).rolling(42).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc068_42d_slope_v068_signal'] = f59fc_f59_fcf_conversion_quality_calc068_42d_slope_v068_signal

def f59fc_f59_fcf_conversion_quality_calc069_42d_slope_v069_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(42).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc069_42d_slope_v069_signal'] = f59fc_f59_fcf_conversion_quality_calc069_42d_slope_v069_signal

def f59fc_f59_fcf_conversion_quality_calc070_63d_slope_v070_signal(currentratio, eps, capex):
    res = (capex / currentratio).rolling(63).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc070_63d_slope_v070_signal'] = f59fc_f59_fcf_conversion_quality_calc070_63d_slope_v070_signal

def f59fc_f59_fcf_conversion_quality_calc071_252d_slope_v071_signal(currentratio, pe, intexp):
    res = (pe / intexp).rolling(252).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc071_252d_slope_v071_signal'] = f59fc_f59_fcf_conversion_quality_calc071_252d_slope_v071_signal

def f59fc_f59_fcf_conversion_quality_calc072_21d_slope_v072_signal(taxexp, assets, capex):
    res = (capex / assets).rolling(21).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc072_21d_slope_v072_signal'] = f59fc_f59_fcf_conversion_quality_calc072_21d_slope_v072_signal

def f59fc_f59_fcf_conversion_quality_calc073_5d_slope_v073_signal(opinc, marketcap, pb):
    res = (marketcap / opinc).rolling(5).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc073_5d_slope_v073_signal'] = f59fc_f59_fcf_conversion_quality_calc073_5d_slope_v073_signal

def f59fc_f59_fcf_conversion_quality_calc074_63d_slope_v074_signal(fcf, eps):
    res = (eps / fcf).rolling(63).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc074_63d_slope_v074_signal'] = f59fc_f59_fcf_conversion_quality_calc074_63d_slope_v074_signal

def f59fc_f59_fcf_conversion_quality_calc075_5d_slope_v075_signal(gp, pe):
    res = (pe / gp).rolling(5).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc075_5d_slope_v075_signal'] = f59fc_f59_fcf_conversion_quality_calc075_5d_slope_v075_signal

def f59fc_f59_fcf_conversion_quality_calc076_42d_slope_v076_signal(evebit, retearn, equity):
    res = (evebit / retearn).rolling(42).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc076_42d_slope_v076_signal'] = f59fc_f59_fcf_conversion_quality_calc076_42d_slope_v076_signal

def f59fc_f59_fcf_conversion_quality_calc077_10d_slope_v077_signal(ncff, assets, taxexp):
    res = (taxexp / ncff).rolling(10).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc077_10d_slope_v077_signal'] = f59fc_f59_fcf_conversion_quality_calc077_10d_slope_v077_signal

def f59fc_f59_fcf_conversion_quality_calc078_42d_slope_v078_signal(gp, liabilities):
    res = (liabilities / gp).rolling(42).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc078_42d_slope_v078_signal'] = f59fc_f59_fcf_conversion_quality_calc078_42d_slope_v078_signal

def f59fc_f59_fcf_conversion_quality_calc079_126d_slope_v079_signal(opinc, volume, liabilities):
    res = (opinc / volume).rolling(126).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc079_126d_slope_v079_signal'] = f59fc_f59_fcf_conversion_quality_calc079_126d_slope_v079_signal

def f59fc_f59_fcf_conversion_quality_calc080_126d_slope_v080_signal(evebit, opinc, volume):
    res = (evebit / opinc).rolling(126).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc080_126d_slope_v080_signal'] = f59fc_f59_fcf_conversion_quality_calc080_126d_slope_v080_signal

def f59fc_f59_fcf_conversion_quality_calc081_252d_slope_v081_signal(close, ncfo):
    res = (ncfo / close).rolling(252).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc081_252d_slope_v081_signal'] = f59fc_f59_fcf_conversion_quality_calc081_252d_slope_v081_signal

def f59fc_f59_fcf_conversion_quality_calc082_42d_slope_v082_signal(ev, equity):
    res = (ev / equity).rolling(42).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc082_42d_slope_v082_signal'] = f59fc_f59_fcf_conversion_quality_calc082_42d_slope_v082_signal

def f59fc_f59_fcf_conversion_quality_calc083_5d_slope_v083_signal(marketcap, ncfo):
    res = (ncfo / marketcap).rolling(5).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc083_5d_slope_v083_signal'] = f59fc_f59_fcf_conversion_quality_calc083_5d_slope_v083_signal

def f59fc_f59_fcf_conversion_quality_calc084_21d_slope_v084_signal(marketcap, netinc, ncfo):
    res = (marketcap / ncfo).rolling(21).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc084_21d_slope_v084_signal'] = f59fc_f59_fcf_conversion_quality_calc084_21d_slope_v084_signal

def f59fc_f59_fcf_conversion_quality_calc085_42d_slope_v085_signal(ncff, debt, closeadj):
    res = (ncff / debt).rolling(42).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc085_42d_slope_v085_signal'] = f59fc_f59_fcf_conversion_quality_calc085_42d_slope_v085_signal

def f59fc_f59_fcf_conversion_quality_calc086_126d_slope_v086_signal(volume, fcf):
    res = (volume / fcf).rolling(126).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc086_126d_slope_v086_signal'] = f59fc_f59_fcf_conversion_quality_calc086_126d_slope_v086_signal

def f59fc_f59_fcf_conversion_quality_calc087_126d_slope_v087_signal(pb, retearn, netinc):
    res = (netinc / retearn).rolling(126).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc087_126d_slope_v087_signal'] = f59fc_f59_fcf_conversion_quality_calc087_126d_slope_v087_signal

def f59fc_f59_fcf_conversion_quality_calc088_5d_slope_v088_signal(retearn, equity):
    res = (retearn / equity).rolling(5).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc088_5d_slope_v088_signal'] = f59fc_f59_fcf_conversion_quality_calc088_5d_slope_v088_signal

def f59fc_f59_fcf_conversion_quality_calc089_21d_slope_v089_signal(currentratio, netinc, capex):
    res = (capex / currentratio).rolling(21).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc089_21d_slope_v089_signal'] = f59fc_f59_fcf_conversion_quality_calc089_21d_slope_v089_signal

def f59fc_f59_fcf_conversion_quality_calc090_42d_slope_v090_signal(ev, capex, high):
    res = (high / capex).rolling(42).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc090_42d_slope_v090_signal'] = f59fc_f59_fcf_conversion_quality_calc090_42d_slope_v090_signal

def f59fc_f59_fcf_conversion_quality_calc091_21d_slope_v091_signal(low, ps, open):
    res = (low / open).rolling(21).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc091_21d_slope_v091_signal'] = f59fc_f59_fcf_conversion_quality_calc091_21d_slope_v091_signal

def f59fc_f59_fcf_conversion_quality_calc092_126d_slope_v092_signal(gp, evebitda):
    res = (evebitda / gp).rolling(126).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc092_126d_slope_v092_signal'] = f59fc_f59_fcf_conversion_quality_calc092_126d_slope_v092_signal

def f59fc_f59_fcf_conversion_quality_calc093_21d_slope_v093_signal(ev, pe):
    res = (pe / ev).rolling(21).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc093_21d_slope_v093_signal'] = f59fc_f59_fcf_conversion_quality_calc093_21d_slope_v093_signal

def f59fc_f59_fcf_conversion_quality_calc094_252d_slope_v094_signal(netinc, revenue):
    res = (revenue / netinc).rolling(252).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc094_252d_slope_v094_signal'] = f59fc_f59_fcf_conversion_quality_calc094_252d_slope_v094_signal

def f59fc_f59_fcf_conversion_quality_calc095_63d_slope_v095_signal(ps, close, liabilities):
    res = (ps / liabilities).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc095_63d_slope_v095_signal'] = f59fc_f59_fcf_conversion_quality_calc095_63d_slope_v095_signal

def f59fc_f59_fcf_conversion_quality_calc096_126d_slope_v096_signal(open, ncff):
    res = (ncff / open).rolling(126).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc096_126d_slope_v096_signal'] = f59fc_f59_fcf_conversion_quality_calc096_126d_slope_v096_signal

def f59fc_f59_fcf_conversion_quality_calc097_126d_slope_v097_signal(close, fcf, high):
    res = (fcf / close).rolling(126).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc097_126d_slope_v097_signal'] = f59fc_f59_fcf_conversion_quality_calc097_126d_slope_v097_signal

def f59fc_f59_fcf_conversion_quality_calc098_21d_slope_v098_signal(low, netinc):
    res = (low / netinc).rolling(21).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc098_21d_slope_v098_signal'] = f59fc_f59_fcf_conversion_quality_calc098_21d_slope_v098_signal

def f59fc_f59_fcf_conversion_quality_calc099_10d_slope_v099_signal(ebitda, ncfo):
    res = (ncfo / ebitda).rolling(10).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc099_10d_slope_v099_signal'] = f59fc_f59_fcf_conversion_quality_calc099_10d_slope_v099_signal

def f59fc_f59_fcf_conversion_quality_calc100_63d_slope_v100_signal(marketcap, fcf, liabilities):
    res = (liabilities / marketcap).rolling(63).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc100_63d_slope_v100_signal'] = f59fc_f59_fcf_conversion_quality_calc100_63d_slope_v100_signal

def f59fc_f59_fcf_conversion_quality_calc101_10d_slope_v101_signal(close, fcf):
    res = (close / fcf).rolling(10).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc101_10d_slope_v101_signal'] = f59fc_f59_fcf_conversion_quality_calc101_10d_slope_v101_signal

def f59fc_f59_fcf_conversion_quality_calc102_252d_slope_v102_signal(sharesbas, fcf):
    res = (sharesbas / fcf).rolling(252).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc102_252d_slope_v102_signal'] = f59fc_f59_fcf_conversion_quality_calc102_252d_slope_v102_signal

def f59fc_f59_fcf_conversion_quality_calc103_126d_slope_v103_signal(low, evebit, assets):
    res = (low / assets).rolling(126).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc103_126d_slope_v103_signal'] = f59fc_f59_fcf_conversion_quality_calc103_126d_slope_v103_signal

def f59fc_f59_fcf_conversion_quality_calc104_10d_slope_v104_signal(ev, sharesbas):
    res = (ev / sharesbas).rolling(10).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc104_10d_slope_v104_signal'] = f59fc_f59_fcf_conversion_quality_calc104_10d_slope_v104_signal

def f59fc_f59_fcf_conversion_quality_calc105_126d_slope_v105_signal(close, retearn):
    res = (retearn / close).rolling(126).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc105_126d_slope_v105_signal'] = f59fc_f59_fcf_conversion_quality_calc105_126d_slope_v105_signal

def f59fc_f59_fcf_conversion_quality_calc106_42d_slope_v106_signal(closeadj, volume, pe):
    res = (closeadj / volume).rolling(42).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc106_42d_slope_v106_signal'] = f59fc_f59_fcf_conversion_quality_calc106_42d_slope_v106_signal

def f59fc_f59_fcf_conversion_quality_calc107_10d_slope_v107_signal(gp, netinc):
    res = (netinc / gp).rolling(10).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc107_10d_slope_v107_signal'] = f59fc_f59_fcf_conversion_quality_calc107_10d_slope_v107_signal

def f59fc_f59_fcf_conversion_quality_calc108_5d_slope_v108_signal(currentratio, sharesbas, ebitda):
    res = (sharesbas / ebitda).rolling(5).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc108_5d_slope_v108_signal'] = f59fc_f59_fcf_conversion_quality_calc108_5d_slope_v108_signal

def f59fc_f59_fcf_conversion_quality_calc109_5d_slope_v109_signal(currentratio, pb):
    res = (pb / currentratio).rolling(5).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc109_5d_slope_v109_signal'] = f59fc_f59_fcf_conversion_quality_calc109_5d_slope_v109_signal

def f59fc_f59_fcf_conversion_quality_calc110_21d_slope_v110_signal(opinc, ncfo):
    res = (opinc / ncfo).rolling(21).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc110_21d_slope_v110_signal'] = f59fc_f59_fcf_conversion_quality_calc110_21d_slope_v110_signal

def f59fc_f59_fcf_conversion_quality_calc111_126d_slope_v111_signal(closeadj, assets, pe):
    res = (closeadj / pe).rolling(126).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc111_126d_slope_v111_signal'] = f59fc_f59_fcf_conversion_quality_calc111_126d_slope_v111_signal

def f59fc_f59_fcf_conversion_quality_calc112_63d_slope_v112_signal(low, workingcapital):
    res = (workingcapital / low).rolling(63).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc112_63d_slope_v112_signal'] = f59fc_f59_fcf_conversion_quality_calc112_63d_slope_v112_signal

def f59fc_f59_fcf_conversion_quality_calc113_10d_slope_v113_signal(gp, sharesbas):
    res = (sharesbas / gp).rolling(10).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc113_10d_slope_v113_signal'] = f59fc_f59_fcf_conversion_quality_calc113_10d_slope_v113_signal

def f59fc_f59_fcf_conversion_quality_calc114_42d_slope_v114_signal(marketcap, ncfo):
    res = (ncfo / marketcap).rolling(42).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc114_42d_slope_v114_signal'] = f59fc_f59_fcf_conversion_quality_calc114_42d_slope_v114_signal

def f59fc_f59_fcf_conversion_quality_calc115_252d_slope_v115_signal(currentratio, volume, eps):
    res = (currentratio / eps).rolling(252).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc115_252d_slope_v115_signal'] = f59fc_f59_fcf_conversion_quality_calc115_252d_slope_v115_signal

def f59fc_f59_fcf_conversion_quality_calc116_126d_slope_v116_signal(gp, ncfi):
    res = (ncfi / gp).rolling(126).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc116_126d_slope_v116_signal'] = f59fc_f59_fcf_conversion_quality_calc116_126d_slope_v116_signal

def f59fc_f59_fcf_conversion_quality_calc117_10d_slope_v117_signal(workingcapital, equity, taxexp):
    res = (equity / taxexp).rolling(10).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc117_10d_slope_v117_signal'] = f59fc_f59_fcf_conversion_quality_calc117_10d_slope_v117_signal

def f59fc_f59_fcf_conversion_quality_calc118_10d_slope_v118_signal(gp, pe):
    res = (gp / pe).rolling(10).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc118_10d_slope_v118_signal'] = f59fc_f59_fcf_conversion_quality_calc118_10d_slope_v118_signal

def f59fc_f59_fcf_conversion_quality_calc119_5d_slope_v119_signal(close, sharesbas):
    res = (sharesbas / close).rolling(5).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc119_5d_slope_v119_signal'] = f59fc_f59_fcf_conversion_quality_calc119_5d_slope_v119_signal

def f59fc_f59_fcf_conversion_quality_calc120_63d_slope_v120_signal(marketcap, eps):
    res = (marketcap / eps).rolling(63).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc120_63d_slope_v120_signal'] = f59fc_f59_fcf_conversion_quality_calc120_63d_slope_v120_signal

def f59fc_f59_fcf_conversion_quality_calc121_252d_slope_v121_signal(ev, sharesbas, netinc):
    res = (netinc / ev).rolling(252).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc121_252d_slope_v121_signal'] = f59fc_f59_fcf_conversion_quality_calc121_252d_slope_v121_signal

def f59fc_f59_fcf_conversion_quality_calc122_21d_slope_v122_signal(intexp, revenue):
    res = (intexp / revenue).rolling(21).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc122_21d_slope_v122_signal'] = f59fc_f59_fcf_conversion_quality_calc122_21d_slope_v122_signal

def f59fc_f59_fcf_conversion_quality_calc123_42d_slope_v123_signal(ev, gp):
    res = (gp / ev).rolling(42).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc123_42d_slope_v123_signal'] = f59fc_f59_fcf_conversion_quality_calc123_42d_slope_v123_signal

def f59fc_f59_fcf_conversion_quality_calc124_252d_slope_v124_signal(evebit, taxexp):
    res = (taxexp / evebit).rolling(252).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc124_252d_slope_v124_signal'] = f59fc_f59_fcf_conversion_quality_calc124_252d_slope_v124_signal

def f59fc_f59_fcf_conversion_quality_calc125_42d_slope_v125_signal(ncff, fcf):
    res = (fcf / ncff).rolling(42).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc125_42d_slope_v125_signal'] = f59fc_f59_fcf_conversion_quality_calc125_42d_slope_v125_signal

def f59fc_f59_fcf_conversion_quality_calc126_42d_slope_v126_signal(low, workingcapital):
    res = (low / workingcapital).rolling(42).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc126_42d_slope_v126_signal'] = f59fc_f59_fcf_conversion_quality_calc126_42d_slope_v126_signal

def f59fc_f59_fcf_conversion_quality_calc127_252d_slope_v127_signal(low, ncfi, assets):
    res = (ncfi / assets).rolling(252).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc127_252d_slope_v127_signal'] = f59fc_f59_fcf_conversion_quality_calc127_252d_slope_v127_signal

def f59fc_f59_fcf_conversion_quality_calc128_21d_slope_v128_signal(closeadj, evebitda):
    res = (closeadj / evebitda).rolling(21).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc128_21d_slope_v128_signal'] = f59fc_f59_fcf_conversion_quality_calc128_21d_slope_v128_signal

def f59fc_f59_fcf_conversion_quality_calc129_10d_slope_v129_signal(sharesbas, fcf, intexp):
    res = (fcf / intexp).rolling(10).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc129_10d_slope_v129_signal'] = f59fc_f59_fcf_conversion_quality_calc129_10d_slope_v129_signal

def f59fc_f59_fcf_conversion_quality_calc130_10d_slope_v130_signal(close, debt):
    res = (close / debt).rolling(10).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc130_10d_slope_v130_signal'] = f59fc_f59_fcf_conversion_quality_calc130_10d_slope_v130_signal

def f59fc_f59_fcf_conversion_quality_calc131_21d_slope_v131_signal(ps, currentratio, netinc):
    res = (currentratio / netinc).rolling(21).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc131_21d_slope_v131_signal'] = f59fc_f59_fcf_conversion_quality_calc131_21d_slope_v131_signal

def f59fc_f59_fcf_conversion_quality_calc132_5d_slope_v132_signal(volume, liabilities):
    res = (liabilities / volume).rolling(5).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc132_5d_slope_v132_signal'] = f59fc_f59_fcf_conversion_quality_calc132_5d_slope_v132_signal

def f59fc_f59_fcf_conversion_quality_calc133_5d_slope_v133_signal(ps, sharesbas):
    res = (sharesbas / ps).rolling(5).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc133_5d_slope_v133_signal'] = f59fc_f59_fcf_conversion_quality_calc133_5d_slope_v133_signal

def f59fc_f59_fcf_conversion_quality_calc134_252d_slope_v134_signal(ncff, evebit):
    res = (evebit / ncff).rolling(252).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc134_252d_slope_v134_signal'] = f59fc_f59_fcf_conversion_quality_calc134_252d_slope_v134_signal

def f59fc_f59_fcf_conversion_quality_calc135_252d_slope_v135_signal(ebitda, capex):
    res = (ebitda / capex).rolling(252).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc135_252d_slope_v135_signal'] = f59fc_f59_fcf_conversion_quality_calc135_252d_slope_v135_signal

def f59fc_f59_fcf_conversion_quality_calc136_42d_slope_v136_signal(ps, marketcap, pb):
    res = (marketcap / ps).rolling(42).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc136_42d_slope_v136_signal'] = f59fc_f59_fcf_conversion_quality_calc136_42d_slope_v136_signal

def f59fc_f59_fcf_conversion_quality_calc137_63d_slope_v137_signal(closeadj, ncfo, liabilities):
    res = (ncfo / liabilities).rolling(63).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc137_63d_slope_v137_signal'] = f59fc_f59_fcf_conversion_quality_calc137_63d_slope_v137_signal

def f59fc_f59_fcf_conversion_quality_calc138_21d_slope_v138_signal(opinc, eps, taxexp):
    res = (taxexp / opinc).rolling(21).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc138_21d_slope_v138_signal'] = f59fc_f59_fcf_conversion_quality_calc138_21d_slope_v138_signal

def f59fc_f59_fcf_conversion_quality_calc139_5d_slope_v139_signal(ncff, sharesbas, equity):
    res = (equity / sharesbas).rolling(5).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc139_5d_slope_v139_signal'] = f59fc_f59_fcf_conversion_quality_calc139_5d_slope_v139_signal

def f59fc_f59_fcf_conversion_quality_calc140_10d_slope_v140_signal(sharesbas, ncfo):
    res = (sharesbas / ncfo).rolling(10).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc140_10d_slope_v140_signal'] = f59fc_f59_fcf_conversion_quality_calc140_10d_slope_v140_signal

def f59fc_f59_fcf_conversion_quality_calc141_5d_slope_v141_signal(netinc, intexp, liabilities):
    res = (intexp / liabilities).rolling(5).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc141_5d_slope_v141_signal'] = f59fc_f59_fcf_conversion_quality_calc141_5d_slope_v141_signal

def f59fc_f59_fcf_conversion_quality_calc142_126d_slope_v142_signal(evebit, close, ebitda):
    res = (ebitda / close).rolling(126).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc142_126d_slope_v142_signal'] = f59fc_f59_fcf_conversion_quality_calc142_126d_slope_v142_signal

def f59fc_f59_fcf_conversion_quality_calc143_21d_slope_v143_signal(opinc, retearn, revenue):
    res = (revenue / retearn).rolling(21).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc143_21d_slope_v143_signal'] = f59fc_f59_fcf_conversion_quality_calc143_21d_slope_v143_signal

def f59fc_f59_fcf_conversion_quality_calc144_252d_slope_v144_signal(fcf, ncfo, liabilities):
    res = (ncfo / liabilities).rolling(252).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc144_252d_slope_v144_signal'] = f59fc_f59_fcf_conversion_quality_calc144_252d_slope_v144_signal

def f59fc_f59_fcf_conversion_quality_calc145_5d_slope_v145_signal(assets, ncfo, revenue):
    res = (assets / revenue).rolling(5).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc145_5d_slope_v145_signal'] = f59fc_f59_fcf_conversion_quality_calc145_5d_slope_v145_signal

def f59fc_f59_fcf_conversion_quality_calc146_5d_slope_v146_signal(evebit, capex):
    res = (evebit / capex).rolling(5).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc146_5d_slope_v146_signal'] = f59fc_f59_fcf_conversion_quality_calc146_5d_slope_v146_signal

def f59fc_f59_fcf_conversion_quality_calc147_21d_slope_v147_signal(equity, eps):
    res = (eps / equity).rolling(21).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc147_21d_slope_v147_signal'] = f59fc_f59_fcf_conversion_quality_calc147_21d_slope_v147_signal

def f59fc_f59_fcf_conversion_quality_calc148_5d_slope_v148_signal(ncfi, high, revenue):
    res = (revenue / high).rolling(5).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc148_5d_slope_v148_signal'] = f59fc_f59_fcf_conversion_quality_calc148_5d_slope_v148_signal

def f59fc_f59_fcf_conversion_quality_calc149_42d_slope_v149_signal(marketcap, intexp, capex):
    res = (capex / marketcap).rolling(42).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc149_42d_slope_v149_signal'] = f59fc_f59_fcf_conversion_quality_calc149_42d_slope_v149_signal

def f59fc_f59_fcf_conversion_quality_calc150_10d_slope_v150_signal(assets, netinc, taxexp):
    res = (assets / netinc).rolling(10).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc150_10d_slope_v150_signal'] = f59fc_f59_fcf_conversion_quality_calc150_10d_slope_v150_signal

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
