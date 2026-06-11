import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f60md_f60_market_cap_dominance_calc001_5d_slope_v001_signal(gp, debt, marketcap):
    res = (gp / marketcap).rolling(5).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc001_5d_slope_v001_signal'] = f60md_f60_market_cap_dominance_calc001_5d_slope_v001_signal

def f60md_f60_market_cap_dominance_calc002_126d_slope_v002_signal(low, ps):
    res = (low / ps).rolling(126).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc002_126d_slope_v002_signal'] = f60md_f60_market_cap_dominance_calc002_126d_slope_v002_signal

def f60md_f60_market_cap_dominance_calc003_252d_slope_v003_signal(taxexp, high, ncfo):
    res = (taxexp / high).rolling(252).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc003_252d_slope_v003_signal'] = f60md_f60_market_cap_dominance_calc003_252d_slope_v003_signal

def f60md_f60_market_cap_dominance_calc004_42d_slope_v004_signal(high, currentratio):
    res = (high / currentratio).rolling(42).min().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc004_42d_slope_v004_signal'] = f60md_f60_market_cap_dominance_calc004_42d_slope_v004_signal

def f60md_f60_market_cap_dominance_calc005_5d_slope_v005_signal(pe, fcf):
    res = (fcf / pe).rolling(5).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc005_5d_slope_v005_signal'] = f60md_f60_market_cap_dominance_calc005_5d_slope_v005_signal

def f60md_f60_market_cap_dominance_calc006_63d_slope_v006_signal(equity, assets, close):
    res = (equity / assets).rolling(63).min().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc006_63d_slope_v006_signal'] = f60md_f60_market_cap_dominance_calc006_63d_slope_v006_signal

def f60md_f60_market_cap_dominance_calc007_126d_slope_v007_signal(ev, netinc):
    res = (ev / netinc).rolling(126).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc007_126d_slope_v007_signal'] = f60md_f60_market_cap_dominance_calc007_126d_slope_v007_signal

def f60md_f60_market_cap_dominance_calc008_63d_slope_v008_signal(closeadj, marketcap):
    res = (marketcap / closeadj).rolling(63).min().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc008_63d_slope_v008_signal'] = f60md_f60_market_cap_dominance_calc008_63d_slope_v008_signal

def f60md_f60_market_cap_dominance_calc009_63d_slope_v009_signal(volume, evebit):
    res = (evebit / volume).rolling(63).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc009_63d_slope_v009_signal'] = f60md_f60_market_cap_dominance_calc009_63d_slope_v009_signal

def f60md_f60_market_cap_dominance_calc010_21d_slope_v010_signal(capex, ebitda, close):
    res = (capex / ebitda).rolling(21).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc010_21d_slope_v010_signal'] = f60md_f60_market_cap_dominance_calc010_21d_slope_v010_signal

def f60md_f60_market_cap_dominance_calc011_126d_slope_v011_signal(ncff, ev, taxexp):
    res = (ncff / ev).rolling(126).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc011_126d_slope_v011_signal'] = f60md_f60_market_cap_dominance_calc011_126d_slope_v011_signal

def f60md_f60_market_cap_dominance_calc012_63d_slope_v012_signal(capex, currentratio):
    res = (currentratio / capex).rolling(63).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc012_63d_slope_v012_signal'] = f60md_f60_market_cap_dominance_calc012_63d_slope_v012_signal

def f60md_f60_market_cap_dominance_calc013_42d_slope_v013_signal(netinc, currentratio, fcf):
    res = (netinc / fcf).rolling(42).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc013_42d_slope_v013_signal'] = f60md_f60_market_cap_dominance_calc013_42d_slope_v013_signal

def f60md_f60_market_cap_dominance_calc014_63d_slope_v014_signal(capex, taxexp):
    res = (capex / taxexp).rolling(63).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc014_63d_slope_v014_signal'] = f60md_f60_market_cap_dominance_calc014_63d_slope_v014_signal

def f60md_f60_market_cap_dominance_calc015_252d_slope_v015_signal(low, gp):
    res = (gp / low).rolling(252).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc015_252d_slope_v015_signal'] = f60md_f60_market_cap_dominance_calc015_252d_slope_v015_signal

def f60md_f60_market_cap_dominance_calc016_5d_slope_v016_signal(workingcapital, ps, marketcap):
    res = (marketcap / ps).rolling(5).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc016_5d_slope_v016_signal'] = f60md_f60_market_cap_dominance_calc016_5d_slope_v016_signal

def f60md_f60_market_cap_dominance_calc017_63d_slope_v017_signal(intexp, eps):
    res = (intexp / eps).rolling(63).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc017_63d_slope_v017_signal'] = f60md_f60_market_cap_dominance_calc017_63d_slope_v017_signal

def f60md_f60_market_cap_dominance_calc018_63d_slope_v018_signal(assets, ncfo):
    res = (assets / ncfo).rolling(63).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc018_63d_slope_v018_signal'] = f60md_f60_market_cap_dominance_calc018_63d_slope_v018_signal

def f60md_f60_market_cap_dominance_calc019_252d_slope_v019_signal(volume, open):
    res = (volume / open).rolling(252).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc019_252d_slope_v019_signal'] = f60md_f60_market_cap_dominance_calc019_252d_slope_v019_signal

def f60md_f60_market_cap_dominance_calc020_252d_slope_v020_signal(capex, ev):
    res = (capex / ev).rolling(252).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc020_252d_slope_v020_signal'] = f60md_f60_market_cap_dominance_calc020_252d_slope_v020_signal

def f60md_f60_market_cap_dominance_calc021_10d_slope_v021_signal(taxexp, intexp):
    res = (taxexp / intexp).rolling(10).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc021_10d_slope_v021_signal'] = f60md_f60_market_cap_dominance_calc021_10d_slope_v021_signal

def f60md_f60_market_cap_dominance_calc022_126d_slope_v022_signal(capex, high, assets):
    res = (high / capex).rolling(126).max().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc022_126d_slope_v022_signal'] = f60md_f60_market_cap_dominance_calc022_126d_slope_v022_signal

def f60md_f60_market_cap_dominance_calc023_63d_slope_v023_signal(capex, high):
    res = (capex / high).rolling(63).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc023_63d_slope_v023_signal'] = f60md_f60_market_cap_dominance_calc023_63d_slope_v023_signal

def f60md_f60_market_cap_dominance_calc024_126d_slope_v024_signal(pe, netinc):
    res = (pe / netinc).rolling(126).max().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc024_126d_slope_v024_signal'] = f60md_f60_market_cap_dominance_calc024_126d_slope_v024_signal

def f60md_f60_market_cap_dominance_calc025_252d_slope_v025_signal(pe, ncfo):
    res = (ncfo / pe).rolling(252).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc025_252d_slope_v025_signal'] = f60md_f60_market_cap_dominance_calc025_252d_slope_v025_signal

def f60md_f60_market_cap_dominance_calc026_42d_slope_v026_signal(taxexp, currentratio):
    res = (taxexp / currentratio).rolling(42).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc026_42d_slope_v026_signal'] = f60md_f60_market_cap_dominance_calc026_42d_slope_v026_signal

def f60md_f60_market_cap_dominance_calc027_21d_slope_v027_signal(pb, high):
    res = (pb / high).rolling(21).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc027_21d_slope_v027_signal'] = f60md_f60_market_cap_dominance_calc027_21d_slope_v027_signal

def f60md_f60_market_cap_dominance_calc028_10d_slope_v028_signal(revenue, debt):
    res = (revenue / debt).rolling(10).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc028_10d_slope_v028_signal'] = f60md_f60_market_cap_dominance_calc028_10d_slope_v028_signal

def f60md_f60_market_cap_dominance_calc029_42d_slope_v029_signal(taxexp, evebitda):
    res = (evebitda / taxexp).rolling(42).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc029_42d_slope_v029_signal'] = f60md_f60_market_cap_dominance_calc029_42d_slope_v029_signal

def f60md_f60_market_cap_dominance_calc030_63d_slope_v030_signal(liabilities, pe, marketcap):
    res = (marketcap / pe).rolling(63).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc030_63d_slope_v030_signal'] = f60md_f60_market_cap_dominance_calc030_63d_slope_v030_signal

def f60md_f60_market_cap_dominance_calc031_252d_slope_v031_signal(ev, revenue):
    res = (revenue / ev).rolling(252).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc031_252d_slope_v031_signal'] = f60md_f60_market_cap_dominance_calc031_252d_slope_v031_signal

def f60md_f60_market_cap_dominance_calc032_10d_slope_v032_signal(evebitda, fcf, close):
    res = (close / evebitda).rolling(10).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc032_10d_slope_v032_signal'] = f60md_f60_market_cap_dominance_calc032_10d_slope_v032_signal

def f60md_f60_market_cap_dominance_calc033_252d_slope_v033_signal(taxexp, pe):
    res = (pe / taxexp).rolling(252).min().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc033_252d_slope_v033_signal'] = f60md_f60_market_cap_dominance_calc033_252d_slope_v033_signal

def f60md_f60_market_cap_dominance_calc034_63d_slope_v034_signal(netinc, currentratio, ncfo):
    res = (currentratio / ncfo).rolling(63).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc034_63d_slope_v034_signal'] = f60md_f60_market_cap_dominance_calc034_63d_slope_v034_signal

def f60md_f60_market_cap_dominance_calc035_126d_slope_v035_signal(low, assets, marketcap):
    res = (low / assets).rolling(126).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc035_126d_slope_v035_signal'] = f60md_f60_market_cap_dominance_calc035_126d_slope_v035_signal

def f60md_f60_market_cap_dominance_calc036_10d_slope_v036_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(10).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc036_10d_slope_v036_signal'] = f60md_f60_market_cap_dominance_calc036_10d_slope_v036_signal

def f60md_f60_market_cap_dominance_calc037_252d_slope_v037_signal(pe, assets, marketcap):
    res = (marketcap / assets).rolling(252).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc037_252d_slope_v037_signal'] = f60md_f60_market_cap_dominance_calc037_252d_slope_v037_signal

def f60md_f60_market_cap_dominance_calc038_5d_slope_v038_signal(capex, ncfo):
    res = (ncfo / capex).rolling(5).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc038_5d_slope_v038_signal'] = f60md_f60_market_cap_dominance_calc038_5d_slope_v038_signal

def f60md_f60_market_cap_dominance_calc039_63d_slope_v039_signal(low, revenue, ebitda):
    res = (low / revenue).rolling(63).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc039_63d_slope_v039_signal'] = f60md_f60_market_cap_dominance_calc039_63d_slope_v039_signal

def f60md_f60_market_cap_dominance_calc040_63d_slope_v040_signal(currentratio, gp):
    res = (gp / currentratio).rolling(63).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc040_63d_slope_v040_signal'] = f60md_f60_market_cap_dominance_calc040_63d_slope_v040_signal

def f60md_f60_market_cap_dominance_calc041_42d_slope_v041_signal(capex, marketcap):
    res = (marketcap / capex).rolling(42).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc041_42d_slope_v041_signal'] = f60md_f60_market_cap_dominance_calc041_42d_slope_v041_signal

def f60md_f60_market_cap_dominance_calc042_126d_slope_v042_signal(open, ncfo):
    res = (open / ncfo).rolling(126).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc042_126d_slope_v042_signal'] = f60md_f60_market_cap_dominance_calc042_126d_slope_v042_signal

def f60md_f60_market_cap_dominance_calc043_5d_slope_v043_signal(liabilities, pe, assets):
    res = (liabilities / pe).rolling(5).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc043_5d_slope_v043_signal'] = f60md_f60_market_cap_dominance_calc043_5d_slope_v043_signal

def f60md_f60_market_cap_dominance_calc044_10d_slope_v044_signal(evebitda, opinc):
    res = (evebitda / opinc).rolling(10).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc044_10d_slope_v044_signal'] = f60md_f60_market_cap_dominance_calc044_10d_slope_v044_signal

def f60md_f60_market_cap_dominance_calc045_10d_slope_v045_signal(ev, currentratio):
    res = (currentratio / ev).rolling(10).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc045_10d_slope_v045_signal'] = f60md_f60_market_cap_dominance_calc045_10d_slope_v045_signal

def f60md_f60_market_cap_dominance_calc046_42d_slope_v046_signal(pb, pe, currentratio):
    res = (currentratio / pe).rolling(42).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc046_42d_slope_v046_signal'] = f60md_f60_market_cap_dominance_calc046_42d_slope_v046_signal

def f60md_f60_market_cap_dominance_calc047_252d_slope_v047_signal(closeadj, fcf):
    res = (fcf / closeadj).rolling(252).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc047_252d_slope_v047_signal'] = f60md_f60_market_cap_dominance_calc047_252d_slope_v047_signal

def f60md_f60_market_cap_dominance_calc048_21d_slope_v048_signal(volume, assets):
    res = (assets / volume).rolling(21).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc048_21d_slope_v048_signal'] = f60md_f60_market_cap_dominance_calc048_21d_slope_v048_signal

def f60md_f60_market_cap_dominance_calc049_252d_slope_v049_signal(taxexp, eps, evebit):
    res = (evebit / taxexp).rolling(252).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc049_252d_slope_v049_signal'] = f60md_f60_market_cap_dominance_calc049_252d_slope_v049_signal

def f60md_f60_market_cap_dominance_calc050_5d_slope_v050_signal(sharesbas, intexp, ev):
    res = (intexp / sharesbas).rolling(5).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc050_5d_slope_v050_signal'] = f60md_f60_market_cap_dominance_calc050_5d_slope_v050_signal

def f60md_f60_market_cap_dominance_calc051_42d_slope_v051_signal(intexp, closeadj, equity):
    res = (closeadj / equity).rolling(42).max().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc051_42d_slope_v051_signal'] = f60md_f60_market_cap_dominance_calc051_42d_slope_v051_signal

def f60md_f60_market_cap_dominance_calc052_42d_slope_v052_signal(evebitda, pe, high):
    res = (pe / high).rolling(42).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc052_42d_slope_v052_signal'] = f60md_f60_market_cap_dominance_calc052_42d_slope_v052_signal

def f60md_f60_market_cap_dominance_calc053_10d_slope_v053_signal(ncff, evebitda, debt):
    res = (ncff / evebitda).rolling(10).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc053_10d_slope_v053_signal'] = f60md_f60_market_cap_dominance_calc053_10d_slope_v053_signal

def f60md_f60_market_cap_dominance_calc054_42d_slope_v054_signal(ncfi, close):
    res = (close / ncfi).rolling(42).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc054_42d_slope_v054_signal'] = f60md_f60_market_cap_dominance_calc054_42d_slope_v054_signal

def f60md_f60_market_cap_dominance_calc055_21d_slope_v055_signal(evebitda, eps, ncfo):
    res = (ncfo / evebitda).rolling(21).min().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc055_21d_slope_v055_signal'] = f60md_f60_market_cap_dominance_calc055_21d_slope_v055_signal

def f60md_f60_market_cap_dominance_calc056_126d_slope_v056_signal(capex, close):
    res = (close / capex).rolling(126).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc056_126d_slope_v056_signal'] = f60md_f60_market_cap_dominance_calc056_126d_slope_v056_signal

def f60md_f60_market_cap_dominance_calc057_21d_slope_v057_signal(sharesbas, ev):
    res = (sharesbas / ev).rolling(21).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc057_21d_slope_v057_signal'] = f60md_f60_market_cap_dominance_calc057_21d_slope_v057_signal

def f60md_f60_market_cap_dominance_calc058_5d_slope_v058_signal(volume, low, equity):
    res = (volume / low).rolling(5).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc058_5d_slope_v058_signal'] = f60md_f60_market_cap_dominance_calc058_5d_slope_v058_signal

def f60md_f60_market_cap_dominance_calc059_252d_slope_v059_signal(capex, ncfi, volume):
    res = (volume / capex).rolling(252).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc059_252d_slope_v059_signal'] = f60md_f60_market_cap_dominance_calc059_252d_slope_v059_signal

def f60md_f60_market_cap_dominance_calc060_63d_slope_v060_signal(capex, ev, assets):
    res = (ev / assets).rolling(63).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc060_63d_slope_v060_signal'] = f60md_f60_market_cap_dominance_calc060_63d_slope_v060_signal

def f60md_f60_market_cap_dominance_calc061_10d_slope_v061_signal(pe, closeadj, currentratio):
    res = (currentratio / pe).rolling(10).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc061_10d_slope_v061_signal'] = f60md_f60_market_cap_dominance_calc061_10d_slope_v061_signal

def f60md_f60_market_cap_dominance_calc062_10d_slope_v062_signal(ncfi, ps):
    res = (ps / ncfi).rolling(10).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc062_10d_slope_v062_signal'] = f60md_f60_market_cap_dominance_calc062_10d_slope_v062_signal

def f60md_f60_market_cap_dominance_calc063_10d_slope_v063_signal(volume, equity, fcf):
    res = (volume / equity).rolling(10).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc063_10d_slope_v063_signal'] = f60md_f60_market_cap_dominance_calc063_10d_slope_v063_signal

def f60md_f60_market_cap_dominance_calc064_10d_slope_v064_signal(liabilities, currentratio):
    res = (currentratio / liabilities).rolling(10).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc064_10d_slope_v064_signal'] = f60md_f60_market_cap_dominance_calc064_10d_slope_v064_signal

def f60md_f60_market_cap_dominance_calc065_126d_slope_v065_signal(capex, intexp, workingcapital):
    res = (intexp / workingcapital).rolling(126).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc065_126d_slope_v065_signal'] = f60md_f60_market_cap_dominance_calc065_126d_slope_v065_signal

def f60md_f60_market_cap_dominance_calc066_252d_slope_v066_signal(ncff, taxexp):
    res = (ncff / taxexp).rolling(252).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc066_252d_slope_v066_signal'] = f60md_f60_market_cap_dominance_calc066_252d_slope_v066_signal

def f60md_f60_market_cap_dominance_calc067_252d_slope_v067_signal(evebit, ebitda, fcf):
    res = (ebitda / evebit).rolling(252).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc067_252d_slope_v067_signal'] = f60md_f60_market_cap_dominance_calc067_252d_slope_v067_signal

def f60md_f60_market_cap_dominance_calc068_10d_slope_v068_signal(ev, currentratio):
    res = (currentratio / ev).rolling(10).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc068_10d_slope_v068_signal'] = f60md_f60_market_cap_dominance_calc068_10d_slope_v068_signal

def f60md_f60_market_cap_dominance_calc069_21d_slope_v069_signal(pb, low, workingcapital):
    res = (workingcapital / low).rolling(21).max().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc069_21d_slope_v069_signal'] = f60md_f60_market_cap_dominance_calc069_21d_slope_v069_signal

def f60md_f60_market_cap_dominance_calc070_252d_slope_v070_signal(ev, volume, revenue):
    res = (volume / revenue).rolling(252).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc070_252d_slope_v070_signal'] = f60md_f60_market_cap_dominance_calc070_252d_slope_v070_signal

def f60md_f60_market_cap_dominance_calc071_5d_slope_v071_signal(currentratio, ps, ncfo):
    res = (ncfo / ps).rolling(5).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc071_5d_slope_v071_signal'] = f60md_f60_market_cap_dominance_calc071_5d_slope_v071_signal

def f60md_f60_market_cap_dominance_calc072_42d_slope_v072_signal(ncff, ncfo, taxexp):
    res = (ncff / taxexp).rolling(42).max().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc072_42d_slope_v072_signal'] = f60md_f60_market_cap_dominance_calc072_42d_slope_v072_signal

def f60md_f60_market_cap_dominance_calc073_252d_slope_v073_signal(intexp, open):
    res = (intexp / open).rolling(252).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc073_252d_slope_v073_signal'] = f60md_f60_market_cap_dominance_calc073_252d_slope_v073_signal

def f60md_f60_market_cap_dominance_calc074_126d_slope_v074_signal(opinc, low):
    res = (low / opinc).rolling(126).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc074_126d_slope_v074_signal'] = f60md_f60_market_cap_dominance_calc074_126d_slope_v074_signal

def f60md_f60_market_cap_dominance_calc075_5d_slope_v075_signal(pb, high, eps):
    res = (eps / high).rolling(5).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc075_5d_slope_v075_signal'] = f60md_f60_market_cap_dominance_calc075_5d_slope_v075_signal

def f60md_f60_market_cap_dominance_calc076_10d_slope_v076_signal(evebitda, assets):
    res = (assets / evebitda).rolling(10).min().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc076_10d_slope_v076_signal'] = f60md_f60_market_cap_dominance_calc076_10d_slope_v076_signal

def f60md_f60_market_cap_dominance_calc077_21d_slope_v077_signal(capex, currentratio):
    res = (currentratio / capex).rolling(21).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc077_21d_slope_v077_signal'] = f60md_f60_market_cap_dominance_calc077_21d_slope_v077_signal

def f60md_f60_market_cap_dominance_calc078_252d_slope_v078_signal(opinc, low, workingcapital):
    res = (opinc / low).rolling(252).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc078_252d_slope_v078_signal'] = f60md_f60_market_cap_dominance_calc078_252d_slope_v078_signal

def f60md_f60_market_cap_dominance_calc079_5d_slope_v079_signal(pe, revenue):
    res = (pe / revenue).rolling(5).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc079_5d_slope_v079_signal'] = f60md_f60_market_cap_dominance_calc079_5d_slope_v079_signal

def f60md_f60_market_cap_dominance_calc080_21d_slope_v080_signal(low, ps):
    res = (low / ps).rolling(21).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc080_21d_slope_v080_signal'] = f60md_f60_market_cap_dominance_calc080_21d_slope_v080_signal

def f60md_f60_market_cap_dominance_calc081_63d_slope_v081_signal(ncfo, close):
    res = (close / ncfo).rolling(63).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc081_63d_slope_v081_signal'] = f60md_f60_market_cap_dominance_calc081_63d_slope_v081_signal

def f60md_f60_market_cap_dominance_calc082_126d_slope_v082_signal(debt, ncfo):
    res = (ncfo / debt).rolling(126).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc082_126d_slope_v082_signal'] = f60md_f60_market_cap_dominance_calc082_126d_slope_v082_signal

def f60md_f60_market_cap_dominance_calc083_5d_slope_v083_signal(pe, equity):
    res = (equity / pe).rolling(5).max().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc083_5d_slope_v083_signal'] = f60md_f60_market_cap_dominance_calc083_5d_slope_v083_signal

def f60md_f60_market_cap_dominance_calc084_21d_slope_v084_signal(liabilities, intexp):
    res = (liabilities / intexp).rolling(21).min().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc084_21d_slope_v084_signal'] = f60md_f60_market_cap_dominance_calc084_21d_slope_v084_signal

def f60md_f60_market_cap_dominance_calc085_252d_slope_v085_signal(pb, low):
    res = (low / pb).rolling(252).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc085_252d_slope_v085_signal'] = f60md_f60_market_cap_dominance_calc085_252d_slope_v085_signal

def f60md_f60_market_cap_dominance_calc086_42d_slope_v086_signal(pb, opinc, gp):
    res = (opinc / pb).rolling(42).max().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc086_42d_slope_v086_signal'] = f60md_f60_market_cap_dominance_calc086_42d_slope_v086_signal

def f60md_f60_market_cap_dominance_calc087_21d_slope_v087_signal(liabilities, fcf):
    res = (liabilities / fcf).rolling(21).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc087_21d_slope_v087_signal'] = f60md_f60_market_cap_dominance_calc087_21d_slope_v087_signal

def f60md_f60_market_cap_dominance_calc088_5d_slope_v088_signal(ncfi, equity):
    res = (ncfi / equity).rolling(5).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc088_5d_slope_v088_signal'] = f60md_f60_market_cap_dominance_calc088_5d_slope_v088_signal

def f60md_f60_market_cap_dominance_calc089_10d_slope_v089_signal(netinc, revenue, equity):
    res = (revenue / equity).rolling(10).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc089_10d_slope_v089_signal'] = f60md_f60_market_cap_dominance_calc089_10d_slope_v089_signal

def f60md_f60_market_cap_dominance_calc090_5d_slope_v090_signal(volume, high, currentratio):
    res = (volume / high).rolling(5).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc090_5d_slope_v090_signal'] = f60md_f60_market_cap_dominance_calc090_5d_slope_v090_signal

def f60md_f60_market_cap_dominance_calc091_10d_slope_v091_signal(retearn, fcf, workingcapital):
    res = (retearn / fcf).rolling(10).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc091_10d_slope_v091_signal'] = f60md_f60_market_cap_dominance_calc091_10d_slope_v091_signal

def f60md_f60_market_cap_dominance_calc092_10d_slope_v092_signal(intexp, high, fcf):
    res = (high / fcf).rolling(10).min().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc092_10d_slope_v092_signal'] = f60md_f60_market_cap_dominance_calc092_10d_slope_v092_signal

def f60md_f60_market_cap_dominance_calc093_126d_slope_v093_signal(closeadj, eps, close):
    res = (close / eps).rolling(126).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc093_126d_slope_v093_signal'] = f60md_f60_market_cap_dominance_calc093_126d_slope_v093_signal

def f60md_f60_market_cap_dominance_calc094_21d_slope_v094_signal(sharesbas, pb, intexp):
    res = (sharesbas / pb).rolling(21).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc094_21d_slope_v094_signal'] = f60md_f60_market_cap_dominance_calc094_21d_slope_v094_signal

def f60md_f60_market_cap_dominance_calc095_252d_slope_v095_signal(taxexp, intexp):
    res = (taxexp / intexp).rolling(252).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc095_252d_slope_v095_signal'] = f60md_f60_market_cap_dominance_calc095_252d_slope_v095_signal

def f60md_f60_market_cap_dominance_calc096_126d_slope_v096_signal(open, evebit):
    res = (evebit / open).rolling(126).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc096_126d_slope_v096_signal'] = f60md_f60_market_cap_dominance_calc096_126d_slope_v096_signal

def f60md_f60_market_cap_dominance_calc097_5d_slope_v097_signal(sharesbas, liabilities, workingcapital):
    res = (workingcapital / sharesbas).rolling(5).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc097_5d_slope_v097_signal'] = f60md_f60_market_cap_dominance_calc097_5d_slope_v097_signal

def f60md_f60_market_cap_dominance_calc098_10d_slope_v098_signal(opinc, intexp, ps):
    res = (opinc / intexp).rolling(10).mean().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc098_10d_slope_v098_signal'] = f60md_f60_market_cap_dominance_calc098_10d_slope_v098_signal

def f60md_f60_market_cap_dominance_calc099_126d_slope_v099_signal(capex, assets):
    res = (assets / capex).rolling(126).max().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc099_126d_slope_v099_signal'] = f60md_f60_market_cap_dominance_calc099_126d_slope_v099_signal

def f60md_f60_market_cap_dominance_calc100_63d_slope_v100_signal(ncfi, pe, fcf):
    res = (pe / ncfi).rolling(63).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc100_63d_slope_v100_signal'] = f60md_f60_market_cap_dominance_calc100_63d_slope_v100_signal

def f60md_f60_market_cap_dominance_calc101_42d_slope_v101_signal(revenue, close, marketcap):
    res = (marketcap / revenue).rolling(42).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc101_42d_slope_v101_signal'] = f60md_f60_market_cap_dominance_calc101_42d_slope_v101_signal

def f60md_f60_market_cap_dominance_calc102_21d_slope_v102_signal(assets, ps):
    res = (ps / assets).rolling(21).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc102_21d_slope_v102_signal'] = f60md_f60_market_cap_dominance_calc102_21d_slope_v102_signal

def f60md_f60_market_cap_dominance_calc103_10d_slope_v103_signal(revenue, evebit):
    res = (revenue / evebit).rolling(10).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc103_10d_slope_v103_signal'] = f60md_f60_market_cap_dominance_calc103_10d_slope_v103_signal

def f60md_f60_market_cap_dominance_calc104_5d_slope_v104_signal(opinc, workingcapital):
    res = (workingcapital / opinc).rolling(5).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc104_5d_slope_v104_signal'] = f60md_f60_market_cap_dominance_calc104_5d_slope_v104_signal

def f60md_f60_market_cap_dominance_calc105_5d_slope_v105_signal(closeadj, assets):
    res = (assets / closeadj).rolling(5).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc105_5d_slope_v105_signal'] = f60md_f60_market_cap_dominance_calc105_5d_slope_v105_signal

def f60md_f60_market_cap_dominance_calc106_63d_slope_v106_signal(sharesbas, ncfi, gp):
    res = (ncfi / gp).rolling(63).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc106_63d_slope_v106_signal'] = f60md_f60_market_cap_dominance_calc106_63d_slope_v106_signal

def f60md_f60_market_cap_dominance_calc107_252d_slope_v107_signal(ncff, gp):
    res = (ncff / gp).rolling(252).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc107_252d_slope_v107_signal'] = f60md_f60_market_cap_dominance_calc107_252d_slope_v107_signal

def f60md_f60_market_cap_dominance_calc108_63d_slope_v108_signal(retearn, ev, fcf):
    res = (fcf / ev).rolling(63).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc108_63d_slope_v108_signal'] = f60md_f60_market_cap_dominance_calc108_63d_slope_v108_signal

def f60md_f60_market_cap_dominance_calc109_63d_slope_v109_signal(retearn, intexp):
    res = (retearn / intexp).rolling(63).min().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc109_63d_slope_v109_signal'] = f60md_f60_market_cap_dominance_calc109_63d_slope_v109_signal

def f60md_f60_market_cap_dominance_calc110_252d_slope_v110_signal(intexp, revenue):
    res = (revenue / intexp).rolling(252).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc110_252d_slope_v110_signal'] = f60md_f60_market_cap_dominance_calc110_252d_slope_v110_signal

def f60md_f60_market_cap_dominance_calc111_5d_slope_v111_signal(evebit, debt):
    res = (evebit / debt).rolling(5).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc111_5d_slope_v111_signal'] = f60md_f60_market_cap_dominance_calc111_5d_slope_v111_signal

def f60md_f60_market_cap_dominance_calc112_5d_slope_v112_signal(netinc, eps):
    res = (eps / netinc).rolling(5).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc112_5d_slope_v112_signal'] = f60md_f60_market_cap_dominance_calc112_5d_slope_v112_signal

def f60md_f60_market_cap_dominance_calc113_5d_slope_v113_signal(sharesbas, fcf, ps):
    res = (sharesbas / ps).rolling(5).min().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc113_5d_slope_v113_signal'] = f60md_f60_market_cap_dominance_calc113_5d_slope_v113_signal

def f60md_f60_market_cap_dominance_calc114_42d_slope_v114_signal(sharesbas, eps, marketcap):
    res = (eps / sharesbas).rolling(42).min().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc114_42d_slope_v114_signal'] = f60md_f60_market_cap_dominance_calc114_42d_slope_v114_signal

def f60md_f60_market_cap_dominance_calc115_10d_slope_v115_signal(liabilities, ev, ps):
    res = (ev / ps).rolling(10).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc115_10d_slope_v115_signal'] = f60md_f60_market_cap_dominance_calc115_10d_slope_v115_signal

def f60md_f60_market_cap_dominance_calc116_63d_slope_v116_signal(opinc, assets):
    res = (assets / opinc).rolling(63).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc116_63d_slope_v116_signal'] = f60md_f60_market_cap_dominance_calc116_63d_slope_v116_signal

def f60md_f60_market_cap_dominance_calc117_252d_slope_v117_signal(evebitda, pe, debt):
    res = (debt / pe).rolling(252).min().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc117_252d_slope_v117_signal'] = f60md_f60_market_cap_dominance_calc117_252d_slope_v117_signal

def f60md_f60_market_cap_dominance_calc118_10d_slope_v118_signal(sharesbas, evebit):
    res = (evebit / sharesbas).rolling(10).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc118_10d_slope_v118_signal'] = f60md_f60_market_cap_dominance_calc118_10d_slope_v118_signal

def f60md_f60_market_cap_dominance_calc119_5d_slope_v119_signal(ncff, close):
    res = (close / ncff).rolling(5).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc119_5d_slope_v119_signal'] = f60md_f60_market_cap_dominance_calc119_5d_slope_v119_signal

def f60md_f60_market_cap_dominance_calc120_126d_slope_v120_signal(capex, debt):
    res = (capex / debt).rolling(126).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc120_126d_slope_v120_signal'] = f60md_f60_market_cap_dominance_calc120_126d_slope_v120_signal

def f60md_f60_market_cap_dominance_calc121_10d_slope_v121_signal(taxexp, capex):
    res = (taxexp / capex).rolling(10).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc121_10d_slope_v121_signal'] = f60md_f60_market_cap_dominance_calc121_10d_slope_v121_signal

def f60md_f60_market_cap_dominance_calc122_5d_slope_v122_signal(retearn, netinc):
    res = (retearn / netinc).rolling(5).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc122_5d_slope_v122_signal'] = f60md_f60_market_cap_dominance_calc122_5d_slope_v122_signal

def f60md_f60_market_cap_dominance_calc123_10d_slope_v123_signal(capex, evebitda):
    res = (evebitda / capex).rolling(10).mean().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc123_10d_slope_v123_signal'] = f60md_f60_market_cap_dominance_calc123_10d_slope_v123_signal

def f60md_f60_market_cap_dominance_calc124_252d_slope_v124_signal(retearn, netinc):
    res = (retearn / netinc).rolling(252).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc124_252d_slope_v124_signal'] = f60md_f60_market_cap_dominance_calc124_252d_slope_v124_signal

def f60md_f60_market_cap_dominance_calc125_126d_slope_v125_signal(intexp, high):
    res = (intexp / high).rolling(126).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc125_126d_slope_v125_signal'] = f60md_f60_market_cap_dominance_calc125_126d_slope_v125_signal

def f60md_f60_market_cap_dominance_calc126_126d_slope_v126_signal(ps, ncfo):
    res = (ncfo / ps).rolling(126).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc126_126d_slope_v126_signal'] = f60md_f60_market_cap_dominance_calc126_126d_slope_v126_signal

def f60md_f60_market_cap_dominance_calc127_42d_slope_v127_signal(liabilities, volume, ps):
    res = (liabilities / ps).rolling(42).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc127_42d_slope_v127_signal'] = f60md_f60_market_cap_dominance_calc127_42d_slope_v127_signal

def f60md_f60_market_cap_dominance_calc128_252d_slope_v128_signal(taxexp, intexp, ev):
    res = (ev / taxexp).rolling(252).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc128_252d_slope_v128_signal'] = f60md_f60_market_cap_dominance_calc128_252d_slope_v128_signal

def f60md_f60_market_cap_dominance_calc129_10d_slope_v129_signal(opinc, revenue):
    res = (revenue / opinc).rolling(10).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc129_10d_slope_v129_signal'] = f60md_f60_market_cap_dominance_calc129_10d_slope_v129_signal

def f60md_f60_market_cap_dominance_calc130_10d_slope_v130_signal(liabilities, closeadj):
    res = (liabilities / closeadj).rolling(10).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc130_10d_slope_v130_signal'] = f60md_f60_market_cap_dominance_calc130_10d_slope_v130_signal

def f60md_f60_market_cap_dominance_calc131_5d_slope_v131_signal(pb, high, closeadj):
    res = (high / pb).rolling(5).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc131_5d_slope_v131_signal'] = f60md_f60_market_cap_dominance_calc131_5d_slope_v131_signal

def f60md_f60_market_cap_dominance_calc132_63d_slope_v132_signal(taxexp, ps, ncfo):
    res = (ncfo / taxexp).rolling(63).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc132_63d_slope_v132_signal'] = f60md_f60_market_cap_dominance_calc132_63d_slope_v132_signal

def f60md_f60_market_cap_dominance_calc133_252d_slope_v133_signal(liabilities, volume, ebitda):
    res = (ebitda / liabilities).rolling(252).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc133_252d_slope_v133_signal'] = f60md_f60_market_cap_dominance_calc133_252d_slope_v133_signal

def f60md_f60_market_cap_dominance_calc134_5d_slope_v134_signal(liabilities, high, eps):
    res = (high / liabilities).rolling(5).max().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc134_5d_slope_v134_signal'] = f60md_f60_market_cap_dominance_calc134_5d_slope_v134_signal

def f60md_f60_market_cap_dominance_calc135_252d_slope_v135_signal(evebitda, netinc, retearn):
    res = (evebitda / retearn).rolling(252).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc135_252d_slope_v135_signal'] = f60md_f60_market_cap_dominance_calc135_252d_slope_v135_signal

def f60md_f60_market_cap_dominance_calc136_21d_slope_v136_signal(taxexp, low, ps):
    res = (taxexp / low).rolling(21).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc136_21d_slope_v136_signal'] = f60md_f60_market_cap_dominance_calc136_21d_slope_v136_signal

def f60md_f60_market_cap_dominance_calc137_63d_slope_v137_signal(pe, low, ev):
    res = (ev / low).rolling(63).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc137_63d_slope_v137_signal'] = f60md_f60_market_cap_dominance_calc137_63d_slope_v137_signal

def f60md_f60_market_cap_dominance_calc138_5d_slope_v138_signal(ncfi, close):
    res = (ncfi / close).rolling(5).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc138_5d_slope_v138_signal'] = f60md_f60_market_cap_dominance_calc138_5d_slope_v138_signal

def f60md_f60_market_cap_dominance_calc139_252d_slope_v139_signal(capex, ev, sharesbas):
    res = (ev / capex).rolling(252).std().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc139_252d_slope_v139_signal'] = f60md_f60_market_cap_dominance_calc139_252d_slope_v139_signal

def f60md_f60_market_cap_dominance_calc140_5d_slope_v140_signal(taxexp, revenue):
    res = (revenue / taxexp).rolling(5).var().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc140_5d_slope_v140_signal'] = f60md_f60_market_cap_dominance_calc140_5d_slope_v140_signal

def f60md_f60_market_cap_dominance_calc141_126d_slope_v141_signal(pb, netinc, ncfo):
    res = (pb / netinc).rolling(126).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc141_126d_slope_v141_signal'] = f60md_f60_market_cap_dominance_calc141_126d_slope_v141_signal

def f60md_f60_market_cap_dominance_calc142_10d_slope_v142_signal(sharesbas, currentratio, taxexp):
    res = (sharesbas / currentratio).rolling(10).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc142_10d_slope_v142_signal'] = f60md_f60_market_cap_dominance_calc142_10d_slope_v142_signal

def f60md_f60_market_cap_dominance_calc143_10d_slope_v143_signal(revenue, closeadj, workingcapital):
    res = (revenue / workingcapital).rolling(10).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc143_10d_slope_v143_signal'] = f60md_f60_market_cap_dominance_calc143_10d_slope_v143_signal

def f60md_f60_market_cap_dominance_calc144_21d_slope_v144_signal(revenue, currentratio):
    res = (currentratio / revenue).rolling(21).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc144_21d_slope_v144_signal'] = f60md_f60_market_cap_dominance_calc144_21d_slope_v144_signal

def f60md_f60_market_cap_dominance_calc145_63d_slope_v145_signal(high, workingcapital):
    res = (workingcapital / high).rolling(63).std().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc145_63d_slope_v145_signal'] = f60md_f60_market_cap_dominance_calc145_63d_slope_v145_signal

def f60md_f60_market_cap_dominance_calc146_42d_slope_v146_signal(open, revenue, marketcap):
    res = (revenue / marketcap).rolling(42).max().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc146_42d_slope_v146_signal'] = f60md_f60_market_cap_dominance_calc146_42d_slope_v146_signal

def f60md_f60_market_cap_dominance_calc147_10d_slope_v147_signal(evebit, gp, currentratio):
    res = (currentratio / gp).rolling(10).var().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc147_10d_slope_v147_signal'] = f60md_f60_market_cap_dominance_calc147_10d_slope_v147_signal

def f60md_f60_market_cap_dominance_calc148_5d_slope_v148_signal(evebitda, low):
    res = (low / evebitda).rolling(5).max().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc148_5d_slope_v148_signal'] = f60md_f60_market_cap_dominance_calc148_5d_slope_v148_signal

def f60md_f60_market_cap_dominance_calc149_126d_slope_v149_signal(ev, high, currentratio):
    res = (high / currentratio).rolling(126).min().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc149_126d_slope_v149_signal'] = f60md_f60_market_cap_dominance_calc149_126d_slope_v149_signal

def f60md_f60_market_cap_dominance_calc150_63d_slope_v150_signal(open, equity):
    res = (open / equity).rolling(63).var().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc150_63d_slope_v150_signal'] = f60md_f60_market_cap_dominance_calc150_63d_slope_v150_signal

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
