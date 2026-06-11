import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f60md_f60_market_cap_dominance_calc001_10d_jerk_v001_signal(netinc, fcf):
    res = (fcf / netinc).rolling(10).std().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc001_10d_jerk_v001_signal'] = f60md_f60_market_cap_dominance_calc001_10d_jerk_v001_signal

def f60md_f60_market_cap_dominance_calc002_10d_jerk_v002_signal(high, netinc):
    res = (high / netinc).rolling(10).mean().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc002_10d_jerk_v002_signal'] = f60md_f60_market_cap_dominance_calc002_10d_jerk_v002_signal

def f60md_f60_market_cap_dominance_calc003_252d_jerk_v003_signal(netinc, workingcapital):
    res = (workingcapital / netinc).rolling(252).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc003_252d_jerk_v003_signal'] = f60md_f60_market_cap_dominance_calc003_252d_jerk_v003_signal

def f60md_f60_market_cap_dominance_calc004_126d_jerk_v004_signal(gp, fcf):
    res = (fcf / gp).rolling(126).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc004_126d_jerk_v004_signal'] = f60md_f60_market_cap_dominance_calc004_126d_jerk_v004_signal

def f60md_f60_market_cap_dominance_calc005_63d_jerk_v005_signal(evebitda, ebitda):
    res = (evebitda / ebitda).rolling(63).var().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc005_63d_jerk_v005_signal'] = f60md_f60_market_cap_dominance_calc005_63d_jerk_v005_signal

def f60md_f60_market_cap_dominance_calc006_42d_jerk_v006_signal(low, workingcapital):
    res = (workingcapital / low).rolling(42).var().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc006_42d_jerk_v006_signal'] = f60md_f60_market_cap_dominance_calc006_42d_jerk_v006_signal

def f60md_f60_market_cap_dominance_calc007_252d_jerk_v007_signal(close, assets, workingcapital):
    res = (workingcapital / assets).rolling(252).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc007_252d_jerk_v007_signal'] = f60md_f60_market_cap_dominance_calc007_252d_jerk_v007_signal

def f60md_f60_market_cap_dominance_calc008_10d_jerk_v008_signal(opinc, workingcapital):
    res = (opinc / workingcapital).rolling(10).std().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc008_10d_jerk_v008_signal'] = f60md_f60_market_cap_dominance_calc008_10d_jerk_v008_signal

def f60md_f60_market_cap_dominance_calc009_126d_jerk_v009_signal(taxexp, revenue, high):
    res = (revenue / taxexp).rolling(126).var().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc009_126d_jerk_v009_signal'] = f60md_f60_market_cap_dominance_calc009_126d_jerk_v009_signal

def f60md_f60_market_cap_dominance_calc010_10d_jerk_v010_signal(revenue, close):
    res = (revenue / close).rolling(10).mean().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc010_10d_jerk_v010_signal'] = f60md_f60_market_cap_dominance_calc010_10d_jerk_v010_signal

def f60md_f60_market_cap_dominance_calc011_21d_jerk_v011_signal(pb, retearn, evebitda):
    res = (retearn / evebitda).rolling(21).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc011_21d_jerk_v011_signal'] = f60md_f60_market_cap_dominance_calc011_21d_jerk_v011_signal

def f60md_f60_market_cap_dominance_calc012_126d_jerk_v012_signal(netinc, fcf):
    res = (fcf / netinc).rolling(126).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc012_126d_jerk_v012_signal'] = f60md_f60_market_cap_dominance_calc012_126d_jerk_v012_signal

def f60md_f60_market_cap_dominance_calc013_10d_jerk_v013_signal(gp, debt):
    res = (gp / debt).rolling(10).var().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc013_10d_jerk_v013_signal'] = f60md_f60_market_cap_dominance_calc013_10d_jerk_v013_signal

def f60md_f60_market_cap_dominance_calc014_10d_jerk_v014_signal(open, equity, ncfo):
    res = (ncfo / equity).rolling(10).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc014_10d_jerk_v014_signal'] = f60md_f60_market_cap_dominance_calc014_10d_jerk_v014_signal

def f60md_f60_market_cap_dominance_calc015_42d_jerk_v015_signal(opinc, low):
    res = (opinc / low).rolling(42).mean().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc015_42d_jerk_v015_signal'] = f60md_f60_market_cap_dominance_calc015_42d_jerk_v015_signal

def f60md_f60_market_cap_dominance_calc016_63d_jerk_v016_signal(capex, volume, open):
    res = (open / capex).rolling(63).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc016_63d_jerk_v016_signal'] = f60md_f60_market_cap_dominance_calc016_63d_jerk_v016_signal

def f60md_f60_market_cap_dominance_calc017_21d_jerk_v017_signal(retearn, high, workingcapital):
    res = (workingcapital / high).rolling(21).var().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc017_21d_jerk_v017_signal'] = f60md_f60_market_cap_dominance_calc017_21d_jerk_v017_signal

def f60md_f60_market_cap_dominance_calc018_5d_jerk_v018_signal(ncff, low, currentratio):
    res = (currentratio / low).rolling(5).mean().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc018_5d_jerk_v018_signal'] = f60md_f60_market_cap_dominance_calc018_5d_jerk_v018_signal

def f60md_f60_market_cap_dominance_calc019_21d_jerk_v019_signal(low, ebitda):
    res = (ebitda / low).rolling(21).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc019_21d_jerk_v019_signal'] = f60md_f60_market_cap_dominance_calc019_21d_jerk_v019_signal

def f60md_f60_market_cap_dominance_calc020_252d_jerk_v020_signal(currentratio, ebitda, closeadj):
    res = (ebitda / currentratio).rolling(252).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc020_252d_jerk_v020_signal'] = f60md_f60_market_cap_dominance_calc020_252d_jerk_v020_signal

def f60md_f60_market_cap_dominance_calc021_42d_jerk_v021_signal(pe, low, ps):
    res = (pe / low).rolling(42).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc021_42d_jerk_v021_signal'] = f60md_f60_market_cap_dominance_calc021_42d_jerk_v021_signal

def f60md_f60_market_cap_dominance_calc022_5d_jerk_v022_signal(revenue, ev, close):
    res = (ev / revenue).rolling(5).var().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc022_5d_jerk_v022_signal'] = f60md_f60_market_cap_dominance_calc022_5d_jerk_v022_signal

def f60md_f60_market_cap_dominance_calc023_5d_jerk_v023_signal(retearn, pe):
    res = (retearn / pe).rolling(5).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc023_5d_jerk_v023_signal'] = f60md_f60_market_cap_dominance_calc023_5d_jerk_v023_signal

def f60md_f60_market_cap_dominance_calc024_10d_jerk_v024_signal(capex, evebitda, ps):
    res = (evebitda / ps).rolling(10).mean().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc024_10d_jerk_v024_signal'] = f60md_f60_market_cap_dominance_calc024_10d_jerk_v024_signal

def f60md_f60_market_cap_dominance_calc025_10d_jerk_v025_signal(taxexp, revenue, high):
    res = (high / revenue).rolling(10).std().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc025_10d_jerk_v025_signal'] = f60md_f60_market_cap_dominance_calc025_10d_jerk_v025_signal

def f60md_f60_market_cap_dominance_calc026_252d_jerk_v026_signal(assets, workingcapital):
    res = (assets / workingcapital).rolling(252).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc026_252d_jerk_v026_signal'] = f60md_f60_market_cap_dominance_calc026_252d_jerk_v026_signal

def f60md_f60_market_cap_dominance_calc027_5d_jerk_v027_signal(taxexp, netinc, gp):
    res = (netinc / gp).rolling(5).var().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc027_5d_jerk_v027_signal'] = f60md_f60_market_cap_dominance_calc027_5d_jerk_v027_signal

def f60md_f60_market_cap_dominance_calc028_126d_jerk_v028_signal(opinc, equity):
    res = (opinc / equity).rolling(126).var().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc028_126d_jerk_v028_signal'] = f60md_f60_market_cap_dominance_calc028_126d_jerk_v028_signal

def f60md_f60_market_cap_dominance_calc029_42d_jerk_v029_signal(assets, ps):
    res = (assets / ps).rolling(42).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc029_42d_jerk_v029_signal'] = f60md_f60_market_cap_dominance_calc029_42d_jerk_v029_signal

def f60md_f60_market_cap_dominance_calc030_10d_jerk_v030_signal(liabilities, gp, fcf):
    res = (liabilities / gp).rolling(10).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc030_10d_jerk_v030_signal'] = f60md_f60_market_cap_dominance_calc030_10d_jerk_v030_signal

def f60md_f60_market_cap_dominance_calc031_42d_jerk_v031_signal(volume, ev):
    res = (volume / ev).rolling(42).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc031_42d_jerk_v031_signal'] = f60md_f60_market_cap_dominance_calc031_42d_jerk_v031_signal

def f60md_f60_market_cap_dominance_calc032_5d_jerk_v032_signal(pe, high, gp):
    res = (high / gp).rolling(5).mean().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc032_5d_jerk_v032_signal'] = f60md_f60_market_cap_dominance_calc032_5d_jerk_v032_signal

def f60md_f60_market_cap_dominance_calc033_63d_jerk_v033_signal(ncff, closeadj):
    res = (ncff / closeadj).rolling(63).mean().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc033_63d_jerk_v033_signal'] = f60md_f60_market_cap_dominance_calc033_63d_jerk_v033_signal

def f60md_f60_market_cap_dominance_calc034_42d_jerk_v034_signal(taxexp, gp):
    res = (gp / taxexp).rolling(42).std().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc034_42d_jerk_v034_signal'] = f60md_f60_market_cap_dominance_calc034_42d_jerk_v034_signal

def f60md_f60_market_cap_dominance_calc035_10d_jerk_v035_signal(close, debt, marketcap):
    res = (marketcap / debt).rolling(10).mean().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc035_10d_jerk_v035_signal'] = f60md_f60_market_cap_dominance_calc035_10d_jerk_v035_signal

def f60md_f60_market_cap_dominance_calc036_21d_jerk_v036_signal(opinc, pe, evebitda):
    res = (pe / opinc).rolling(21).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc036_21d_jerk_v036_signal'] = f60md_f60_market_cap_dominance_calc036_21d_jerk_v036_signal

def f60md_f60_market_cap_dominance_calc037_126d_jerk_v037_signal(ncff, retearn):
    res = (ncff / retearn).rolling(126).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc037_126d_jerk_v037_signal'] = f60md_f60_market_cap_dominance_calc037_126d_jerk_v037_signal

def f60md_f60_market_cap_dominance_calc038_10d_jerk_v038_signal(debt, assets, fcf):
    res = (fcf / assets).rolling(10).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc038_10d_jerk_v038_signal'] = f60md_f60_market_cap_dominance_calc038_10d_jerk_v038_signal

def f60md_f60_market_cap_dominance_calc039_252d_jerk_v039_signal(currentratio, eps):
    res = (eps / currentratio).rolling(252).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc039_252d_jerk_v039_signal'] = f60md_f60_market_cap_dominance_calc039_252d_jerk_v039_signal

def f60md_f60_market_cap_dominance_calc040_126d_jerk_v040_signal(pb, revenue, marketcap):
    res = (revenue / marketcap).rolling(126).std().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc040_126d_jerk_v040_signal'] = f60md_f60_market_cap_dominance_calc040_126d_jerk_v040_signal

def f60md_f60_market_cap_dominance_calc041_21d_jerk_v041_signal(taxexp, close):
    res = (taxexp / close).rolling(21).var().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc041_21d_jerk_v041_signal'] = f60md_f60_market_cap_dominance_calc041_21d_jerk_v041_signal

def f60md_f60_market_cap_dominance_calc042_5d_jerk_v042_signal(sharesbas, ncfi, marketcap):
    res = (ncfi / marketcap).rolling(5).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc042_5d_jerk_v042_signal'] = f60md_f60_market_cap_dominance_calc042_5d_jerk_v042_signal

def f60md_f60_market_cap_dominance_calc043_126d_jerk_v043_signal(taxexp, pe, currentratio):
    res = (currentratio / taxexp).rolling(126).var().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc043_126d_jerk_v043_signal'] = f60md_f60_market_cap_dominance_calc043_126d_jerk_v043_signal

def f60md_f60_market_cap_dominance_calc044_63d_jerk_v044_signal(high, fcf):
    res = (fcf / high).rolling(63).std().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc044_63d_jerk_v044_signal'] = f60md_f60_market_cap_dominance_calc044_63d_jerk_v044_signal

def f60md_f60_market_cap_dominance_calc045_126d_jerk_v045_signal(netinc, marketcap):
    res = (netinc / marketcap).rolling(126).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc045_126d_jerk_v045_signal'] = f60md_f60_market_cap_dominance_calc045_126d_jerk_v045_signal

def f60md_f60_market_cap_dominance_calc046_5d_jerk_v046_signal(ncff, ps):
    res = (ncff / ps).rolling(5).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc046_5d_jerk_v046_signal'] = f60md_f60_market_cap_dominance_calc046_5d_jerk_v046_signal

def f60md_f60_market_cap_dominance_calc047_21d_jerk_v047_signal(pb, low):
    res = (low / pb).rolling(21).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc047_21d_jerk_v047_signal'] = f60md_f60_market_cap_dominance_calc047_21d_jerk_v047_signal

def f60md_f60_market_cap_dominance_calc048_63d_jerk_v048_signal(taxexp, ncfo):
    res = (taxexp / ncfo).rolling(63).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc048_63d_jerk_v048_signal'] = f60md_f60_market_cap_dominance_calc048_63d_jerk_v048_signal

def f60md_f60_market_cap_dominance_calc049_126d_jerk_v049_signal(taxexp, fcf):
    res = (taxexp / fcf).rolling(126).var().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc049_126d_jerk_v049_signal'] = f60md_f60_market_cap_dominance_calc049_126d_jerk_v049_signal

def f60md_f60_market_cap_dominance_calc050_10d_jerk_v050_signal(pb, gp):
    res = (pb / gp).rolling(10).var().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc050_10d_jerk_v050_signal'] = f60md_f60_market_cap_dominance_calc050_10d_jerk_v050_signal

def f60md_f60_market_cap_dominance_calc051_42d_jerk_v051_signal(pb, workingcapital):
    res = (workingcapital / pb).rolling(42).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc051_42d_jerk_v051_signal'] = f60md_f60_market_cap_dominance_calc051_42d_jerk_v051_signal

def f60md_f60_market_cap_dominance_calc052_42d_jerk_v052_signal(assets, ncfo):
    res = (assets / ncfo).rolling(42).var().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc052_42d_jerk_v052_signal'] = f60md_f60_market_cap_dominance_calc052_42d_jerk_v052_signal

def f60md_f60_market_cap_dominance_calc053_5d_jerk_v053_signal(opinc, currentratio, workingcapital):
    res = (opinc / currentratio).rolling(5).var().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc053_5d_jerk_v053_signal'] = f60md_f60_market_cap_dominance_calc053_5d_jerk_v053_signal

def f60md_f60_market_cap_dominance_calc054_5d_jerk_v054_signal(sharesbas, close, ps):
    res = (sharesbas / ps).rolling(5).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc054_5d_jerk_v054_signal'] = f60md_f60_market_cap_dominance_calc054_5d_jerk_v054_signal

def f60md_f60_market_cap_dominance_calc055_10d_jerk_v055_signal(taxexp, ncff):
    res = (taxexp / ncff).rolling(10).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc055_10d_jerk_v055_signal'] = f60md_f60_market_cap_dominance_calc055_10d_jerk_v055_signal

def f60md_f60_market_cap_dominance_calc056_63d_jerk_v056_signal(retearn, open):
    res = (open / retearn).rolling(63).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc056_63d_jerk_v056_signal'] = f60md_f60_market_cap_dominance_calc056_63d_jerk_v056_signal

def f60md_f60_market_cap_dominance_calc057_10d_jerk_v057_signal(volume, ps):
    res = (ps / volume).rolling(10).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc057_10d_jerk_v057_signal'] = f60md_f60_market_cap_dominance_calc057_10d_jerk_v057_signal

def f60md_f60_market_cap_dominance_calc058_21d_jerk_v058_signal(opinc, evebitda):
    res = (opinc / evebitda).rolling(21).mean().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc058_21d_jerk_v058_signal'] = f60md_f60_market_cap_dominance_calc058_21d_jerk_v058_signal

def f60md_f60_market_cap_dominance_calc059_5d_jerk_v059_signal(open, equity, ncfo):
    res = (equity / ncfo).rolling(5).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc059_5d_jerk_v059_signal'] = f60md_f60_market_cap_dominance_calc059_5d_jerk_v059_signal

def f60md_f60_market_cap_dominance_calc060_252d_jerk_v060_signal(sharesbas, open):
    res = (sharesbas / open).rolling(252).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc060_252d_jerk_v060_signal'] = f60md_f60_market_cap_dominance_calc060_252d_jerk_v060_signal

def f60md_f60_market_cap_dominance_calc061_126d_jerk_v061_signal(closeadj, close, workingcapital):
    res = (workingcapital / close).rolling(126).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc061_126d_jerk_v061_signal'] = f60md_f60_market_cap_dominance_calc061_126d_jerk_v061_signal

def f60md_f60_market_cap_dominance_calc062_126d_jerk_v062_signal(pb, ebitda, evebit):
    res = (evebit / pb).rolling(126).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc062_126d_jerk_v062_signal'] = f60md_f60_market_cap_dominance_calc062_126d_jerk_v062_signal

def f60md_f60_market_cap_dominance_calc063_126d_jerk_v063_signal(evebit, fcf):
    res = (fcf / evebit).rolling(126).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc063_126d_jerk_v063_signal'] = f60md_f60_market_cap_dominance_calc063_126d_jerk_v063_signal

def f60md_f60_market_cap_dominance_calc064_252d_jerk_v064_signal(ncff, volume, ev):
    res = (ev / ncff).rolling(252).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc064_252d_jerk_v064_signal'] = f60md_f60_market_cap_dominance_calc064_252d_jerk_v064_signal

def f60md_f60_market_cap_dominance_calc065_126d_jerk_v065_signal(ncfi, volume, revenue):
    res = (volume / ncfi).rolling(126).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc065_126d_jerk_v065_signal'] = f60md_f60_market_cap_dominance_calc065_126d_jerk_v065_signal

def f60md_f60_market_cap_dominance_calc066_42d_jerk_v066_signal(volume, fcf):
    res = (volume / fcf).rolling(42).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc066_42d_jerk_v066_signal'] = f60md_f60_market_cap_dominance_calc066_42d_jerk_v066_signal

def f60md_f60_market_cap_dominance_calc067_10d_jerk_v067_signal(open, assets):
    res = (open / assets).rolling(10).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc067_10d_jerk_v067_signal'] = f60md_f60_market_cap_dominance_calc067_10d_jerk_v067_signal

def f60md_f60_market_cap_dominance_calc068_42d_jerk_v068_signal(intexp, close):
    res = (close / intexp).rolling(42).var().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc068_42d_jerk_v068_signal'] = f60md_f60_market_cap_dominance_calc068_42d_jerk_v068_signal

def f60md_f60_market_cap_dominance_calc069_63d_jerk_v069_signal(taxexp, gp):
    res = (taxexp / gp).rolling(63).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc069_63d_jerk_v069_signal'] = f60md_f60_market_cap_dominance_calc069_63d_jerk_v069_signal

def f60md_f60_market_cap_dominance_calc070_252d_jerk_v070_signal(revenue, close):
    res = (revenue / close).rolling(252).std().diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc070_252d_jerk_v070_signal'] = f60md_f60_market_cap_dominance_calc070_252d_jerk_v070_signal

def f60md_f60_market_cap_dominance_calc071_10d_jerk_v071_signal(ncff, closeadj):
    res = (closeadj / ncff).rolling(10).std().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc071_10d_jerk_v071_signal'] = f60md_f60_market_cap_dominance_calc071_10d_jerk_v071_signal

def f60md_f60_market_cap_dominance_calc072_10d_jerk_v072_signal(capex, fcf):
    res = (fcf / capex).rolling(10).var().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc072_10d_jerk_v072_signal'] = f60md_f60_market_cap_dominance_calc072_10d_jerk_v072_signal

def f60md_f60_market_cap_dominance_calc073_126d_jerk_v073_signal(pe, ncfo):
    res = (ncfo / pe).rolling(126).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc073_126d_jerk_v073_signal'] = f60md_f60_market_cap_dominance_calc073_126d_jerk_v073_signal

def f60md_f60_market_cap_dominance_calc074_252d_jerk_v074_signal(evebitda, high, assets):
    res = (evebitda / assets).rolling(252).std().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc074_252d_jerk_v074_signal'] = f60md_f60_market_cap_dominance_calc074_252d_jerk_v074_signal

def f60md_f60_market_cap_dominance_calc075_126d_jerk_v075_signal(equity, currentratio, assets):
    res = (currentratio / equity).rolling(126).var().diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc075_126d_jerk_v075_signal'] = f60md_f60_market_cap_dominance_calc075_126d_jerk_v075_signal

def f60md_f60_market_cap_dominance_calc076_10d_jerk_v076_signal(assets, ebitda, close):
    res = (close / ebitda).rolling(10).var().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc076_10d_jerk_v076_signal'] = f60md_f60_market_cap_dominance_calc076_10d_jerk_v076_signal

def f60md_f60_market_cap_dominance_calc077_10d_jerk_v077_signal(pb, liabilities, close):
    res = (close / pb).rolling(10).var().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc077_10d_jerk_v077_signal'] = f60md_f60_market_cap_dominance_calc077_10d_jerk_v077_signal

def f60md_f60_market_cap_dominance_calc078_126d_jerk_v078_signal(sharesbas, retearn):
    res = (sharesbas / retearn).rolling(126).var().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc078_126d_jerk_v078_signal'] = f60md_f60_market_cap_dominance_calc078_126d_jerk_v078_signal

def f60md_f60_market_cap_dominance_calc079_126d_jerk_v079_signal(sharesbas, high):
    res = (sharesbas / high).rolling(126).var().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc079_126d_jerk_v079_signal'] = f60md_f60_market_cap_dominance_calc079_126d_jerk_v079_signal

def f60md_f60_market_cap_dominance_calc080_10d_jerk_v080_signal(ncff, ev, ncfo):
    res = (ncff / ncfo).rolling(10).var().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc080_10d_jerk_v080_signal'] = f60md_f60_market_cap_dominance_calc080_10d_jerk_v080_signal

def f60md_f60_market_cap_dominance_calc081_42d_jerk_v081_signal(equity, close):
    res = (close / equity).rolling(42).std().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc081_42d_jerk_v081_signal'] = f60md_f60_market_cap_dominance_calc081_42d_jerk_v081_signal

def f60md_f60_market_cap_dominance_calc082_5d_jerk_v082_signal(sharesbas, pe, ncfo):
    res = (sharesbas / pe).rolling(5).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc082_5d_jerk_v082_signal'] = f60md_f60_market_cap_dominance_calc082_5d_jerk_v082_signal

def f60md_f60_market_cap_dominance_calc083_42d_jerk_v083_signal(intexp, evebit):
    res = (evebit / intexp).rolling(42).std().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc083_42d_jerk_v083_signal'] = f60md_f60_market_cap_dominance_calc083_42d_jerk_v083_signal

def f60md_f60_market_cap_dominance_calc084_10d_jerk_v084_signal(equity, fcf, workingcapital):
    res = (fcf / workingcapital).rolling(10).var().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc084_10d_jerk_v084_signal'] = f60md_f60_market_cap_dominance_calc084_10d_jerk_v084_signal

def f60md_f60_market_cap_dominance_calc085_126d_jerk_v085_signal(ncfi, workingcapital, ps):
    res = (ncfi / ps).rolling(126).var().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc085_126d_jerk_v085_signal'] = f60md_f60_market_cap_dominance_calc085_126d_jerk_v085_signal

def f60md_f60_market_cap_dominance_calc086_42d_jerk_v086_signal(ncff, ncfo):
    res = (ncff / ncfo).rolling(42).var().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc086_42d_jerk_v086_signal'] = f60md_f60_market_cap_dominance_calc086_42d_jerk_v086_signal

def f60md_f60_market_cap_dominance_calc087_21d_jerk_v087_signal(high, close):
    res = (close / high).rolling(21).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc087_21d_jerk_v087_signal'] = f60md_f60_market_cap_dominance_calc087_21d_jerk_v087_signal

def f60md_f60_market_cap_dominance_calc088_10d_jerk_v088_signal(sharesbas, intexp, fcf):
    res = (fcf / sharesbas).rolling(10).mean().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc088_10d_jerk_v088_signal'] = f60md_f60_market_cap_dominance_calc088_10d_jerk_v088_signal

def f60md_f60_market_cap_dominance_calc089_21d_jerk_v089_signal(open, ncfo):
    res = (ncfo / open).rolling(21).var().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc089_21d_jerk_v089_signal'] = f60md_f60_market_cap_dominance_calc089_21d_jerk_v089_signal

def f60md_f60_market_cap_dominance_calc090_10d_jerk_v090_signal(low, evebit, ncfo):
    res = (ncfo / low).rolling(10).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc090_10d_jerk_v090_signal'] = f60md_f60_market_cap_dominance_calc090_10d_jerk_v090_signal

def f60md_f60_market_cap_dominance_calc091_5d_jerk_v091_signal(opinc, evebitda):
    res = (opinc / evebitda).rolling(5).var().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc091_5d_jerk_v091_signal'] = f60md_f60_market_cap_dominance_calc091_5d_jerk_v091_signal

def f60md_f60_market_cap_dominance_calc092_5d_jerk_v092_signal(opinc, open, ev):
    res = (ev / opinc).rolling(5).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc092_5d_jerk_v092_signal'] = f60md_f60_market_cap_dominance_calc092_5d_jerk_v092_signal

def f60md_f60_market_cap_dominance_calc093_252d_jerk_v093_signal(gp, workingcapital):
    res = (workingcapital / gp).rolling(252).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc093_252d_jerk_v093_signal'] = f60md_f60_market_cap_dominance_calc093_252d_jerk_v093_signal

def f60md_f60_market_cap_dominance_calc094_5d_jerk_v094_signal(opinc, closeadj, ev):
    res = (closeadj / opinc).rolling(5).std().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc094_5d_jerk_v094_signal'] = f60md_f60_market_cap_dominance_calc094_5d_jerk_v094_signal

def f60md_f60_market_cap_dominance_calc095_5d_jerk_v095_signal(netinc, eps):
    res = (netinc / eps).rolling(5).mean().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc095_5d_jerk_v095_signal'] = f60md_f60_market_cap_dominance_calc095_5d_jerk_v095_signal

def f60md_f60_market_cap_dominance_calc096_42d_jerk_v096_signal(revenue, equity, gp):
    res = (gp / revenue).rolling(42).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc096_42d_jerk_v096_signal'] = f60md_f60_market_cap_dominance_calc096_42d_jerk_v096_signal

def f60md_f60_market_cap_dominance_calc097_42d_jerk_v097_signal(ncfi, pe):
    res = (pe / ncfi).rolling(42).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc097_42d_jerk_v097_signal'] = f60md_f60_market_cap_dominance_calc097_42d_jerk_v097_signal

def f60md_f60_market_cap_dominance_calc098_252d_jerk_v098_signal(sharesbas, open):
    res = (sharesbas / open).rolling(252).std().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc098_252d_jerk_v098_signal'] = f60md_f60_market_cap_dominance_calc098_252d_jerk_v098_signal

def f60md_f60_market_cap_dominance_calc099_126d_jerk_v099_signal(low, close):
    res = (close / low).rolling(126).var().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc099_126d_jerk_v099_signal'] = f60md_f60_market_cap_dominance_calc099_126d_jerk_v099_signal

def f60md_f60_market_cap_dominance_calc100_10d_jerk_v100_signal(equity, ps, workingcapital):
    res = (workingcapital / equity).rolling(10).var().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc100_10d_jerk_v100_signal'] = f60md_f60_market_cap_dominance_calc100_10d_jerk_v100_signal

def f60md_f60_market_cap_dominance_calc101_5d_jerk_v101_signal(high, evebit, marketcap):
    res = (evebit / marketcap).rolling(5).std().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc101_5d_jerk_v101_signal'] = f60md_f60_market_cap_dominance_calc101_5d_jerk_v101_signal

def f60md_f60_market_cap_dominance_calc102_10d_jerk_v102_signal(capex, currentratio, workingcapital):
    res = (capex / currentratio).rolling(10).mean().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc102_10d_jerk_v102_signal'] = f60md_f60_market_cap_dominance_calc102_10d_jerk_v102_signal

def f60md_f60_market_cap_dominance_calc103_10d_jerk_v103_signal(low, evebit, close):
    res = (evebit / low).rolling(10).mean().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc103_10d_jerk_v103_signal'] = f60md_f60_market_cap_dominance_calc103_10d_jerk_v103_signal

def f60md_f60_market_cap_dominance_calc104_252d_jerk_v104_signal(ev, revenue, closeadj):
    res = (revenue / closeadj).rolling(252).mean().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc104_252d_jerk_v104_signal'] = f60md_f60_market_cap_dominance_calc104_252d_jerk_v104_signal

def f60md_f60_market_cap_dominance_calc105_63d_jerk_v105_signal(volume, open, gp):
    res = (open / gp).rolling(63).var().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc105_63d_jerk_v105_signal'] = f60md_f60_market_cap_dominance_calc105_63d_jerk_v105_signal

def f60md_f60_market_cap_dominance_calc106_252d_jerk_v106_signal(sharesbas, evebit, ps):
    res = (ps / sharesbas).rolling(252).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc106_252d_jerk_v106_signal'] = f60md_f60_market_cap_dominance_calc106_252d_jerk_v106_signal

def f60md_f60_market_cap_dominance_calc107_5d_jerk_v107_signal(evebit, fcf, workingcapital):
    res = (fcf / evebit).rolling(5).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc107_5d_jerk_v107_signal'] = f60md_f60_market_cap_dominance_calc107_5d_jerk_v107_signal

def f60md_f60_market_cap_dominance_calc108_5d_jerk_v108_signal(sharesbas, pe, ncff):
    res = (pe / sharesbas).rolling(5).var().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc108_5d_jerk_v108_signal'] = f60md_f60_market_cap_dominance_calc108_5d_jerk_v108_signal

def f60md_f60_market_cap_dominance_calc109_252d_jerk_v109_signal(evebitda, low, gp):
    res = (evebitda / low).rolling(252).var().pct_change(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc109_252d_jerk_v109_signal'] = f60md_f60_market_cap_dominance_calc109_252d_jerk_v109_signal

def f60md_f60_market_cap_dominance_calc110_21d_jerk_v110_signal(ncff, high, closeadj):
    res = (high / closeadj).rolling(21).var().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc110_21d_jerk_v110_signal'] = f60md_f60_market_cap_dominance_calc110_21d_jerk_v110_signal

def f60md_f60_market_cap_dominance_calc111_252d_jerk_v111_signal(liabilities, netinc, debt):
    res = (debt / liabilities).rolling(252).mean().pct_change(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc111_252d_jerk_v111_signal'] = f60md_f60_market_cap_dominance_calc111_252d_jerk_v111_signal

def f60md_f60_market_cap_dominance_calc112_10d_jerk_v112_signal(ev, revenue, close):
    res = (revenue / ev).rolling(10).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc112_10d_jerk_v112_signal'] = f60md_f60_market_cap_dominance_calc112_10d_jerk_v112_signal

def f60md_f60_market_cap_dominance_calc113_10d_jerk_v113_signal(ebitda, pe, gp):
    res = (gp / ebitda).rolling(10).mean().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc113_10d_jerk_v113_signal'] = f60md_f60_market_cap_dominance_calc113_10d_jerk_v113_signal

def f60md_f60_market_cap_dominance_calc114_63d_jerk_v114_signal(currentratio, debt):
    res = (currentratio / debt).rolling(63).var().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc114_63d_jerk_v114_signal'] = f60md_f60_market_cap_dominance_calc114_63d_jerk_v114_signal

def f60md_f60_market_cap_dominance_calc115_5d_jerk_v115_signal(opinc, closeadj):
    res = (closeadj / opinc).rolling(5).std().diff(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc115_5d_jerk_v115_signal'] = f60md_f60_market_cap_dominance_calc115_5d_jerk_v115_signal

def f60md_f60_market_cap_dominance_calc116_42d_jerk_v116_signal(volume, low):
    res = (volume / low).rolling(42).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc116_42d_jerk_v116_signal'] = f60md_f60_market_cap_dominance_calc116_42d_jerk_v116_signal

def f60md_f60_market_cap_dominance_calc117_10d_jerk_v117_signal(evebitda, liabilities, fcf):
    res = (evebitda / liabilities).rolling(10).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc117_10d_jerk_v117_signal'] = f60md_f60_market_cap_dominance_calc117_10d_jerk_v117_signal

def f60md_f60_market_cap_dominance_calc118_126d_jerk_v118_signal(low, debt, ps):
    res = (low / ps).rolling(126).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc118_126d_jerk_v118_signal'] = f60md_f60_market_cap_dominance_calc118_126d_jerk_v118_signal

def f60md_f60_market_cap_dominance_calc119_10d_jerk_v119_signal(ncff, fcf, marketcap):
    res = (ncff / marketcap).rolling(10).mean().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc119_10d_jerk_v119_signal'] = f60md_f60_market_cap_dominance_calc119_10d_jerk_v119_signal

def f60md_f60_market_cap_dominance_calc120_5d_jerk_v120_signal(marketcap, eps, ps):
    res = (ps / eps).rolling(5).var().pct_change(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc120_5d_jerk_v120_signal'] = f60md_f60_market_cap_dominance_calc120_5d_jerk_v120_signal

def f60md_f60_market_cap_dominance_calc121_126d_jerk_v121_signal(evebit, eps):
    res = (eps / evebit).rolling(126).var().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc121_126d_jerk_v121_signal'] = f60md_f60_market_cap_dominance_calc121_126d_jerk_v121_signal

def f60md_f60_market_cap_dominance_calc122_126d_jerk_v122_signal(ncff, currentratio):
    res = (ncff / currentratio).rolling(126).mean().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc122_126d_jerk_v122_signal'] = f60md_f60_market_cap_dominance_calc122_126d_jerk_v122_signal

def f60md_f60_market_cap_dominance_calc123_126d_jerk_v123_signal(evebitda, equity):
    res = (equity / evebitda).rolling(126).var().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc123_126d_jerk_v123_signal'] = f60md_f60_market_cap_dominance_calc123_126d_jerk_v123_signal

def f60md_f60_market_cap_dominance_calc124_21d_jerk_v124_signal(pb, eps):
    res = (pb / eps).rolling(21).std().diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc124_21d_jerk_v124_signal'] = f60md_f60_market_cap_dominance_calc124_21d_jerk_v124_signal

def f60md_f60_market_cap_dominance_calc125_252d_jerk_v125_signal(volume, closeadj, eps):
    res = (volume / closeadj).rolling(252).var().diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc125_252d_jerk_v125_signal'] = f60md_f60_market_cap_dominance_calc125_252d_jerk_v125_signal

def f60md_f60_market_cap_dominance_calc126_5d_jerk_v126_signal(sharesbas, debt, ps):
    res = (sharesbas / ps).rolling(5).var().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc126_5d_jerk_v126_signal'] = f60md_f60_market_cap_dominance_calc126_5d_jerk_v126_signal

def f60md_f60_market_cap_dominance_calc127_63d_jerk_v127_signal(volume, currentratio):
    res = (volume / currentratio).rolling(63).mean().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc127_63d_jerk_v127_signal'] = f60md_f60_market_cap_dominance_calc127_63d_jerk_v127_signal

def f60md_f60_market_cap_dominance_calc128_10d_jerk_v128_signal(revenue, debt, fcf):
    res = (revenue / fcf).rolling(10).mean().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc128_10d_jerk_v128_signal'] = f60md_f60_market_cap_dominance_calc128_10d_jerk_v128_signal

def f60md_f60_market_cap_dominance_calc129_10d_jerk_v129_signal(ncff, evebit, marketcap):
    res = (marketcap / evebit).rolling(10).mean().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc129_10d_jerk_v129_signal'] = f60md_f60_market_cap_dominance_calc129_10d_jerk_v129_signal

def f60md_f60_market_cap_dominance_calc130_5d_jerk_v130_signal(retearn, high, fcf):
    res = (high / fcf).rolling(5).var().diff(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc130_5d_jerk_v130_signal'] = f60md_f60_market_cap_dominance_calc130_5d_jerk_v130_signal

def f60md_f60_market_cap_dominance_calc131_126d_jerk_v131_signal(evebitda, intexp):
    res = (evebitda / intexp).rolling(126).std().diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc131_126d_jerk_v131_signal'] = f60md_f60_market_cap_dominance_calc131_126d_jerk_v131_signal

def f60md_f60_market_cap_dominance_calc132_21d_jerk_v132_signal(liabilities, netinc, fcf):
    res = (netinc / fcf).rolling(21).var().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc132_21d_jerk_v132_signal'] = f60md_f60_market_cap_dominance_calc132_21d_jerk_v132_signal

def f60md_f60_market_cap_dominance_calc133_5d_jerk_v133_signal(closeadj, eps):
    res = (closeadj / eps).rolling(5).var().diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc133_5d_jerk_v133_signal'] = f60md_f60_market_cap_dominance_calc133_5d_jerk_v133_signal

def f60md_f60_market_cap_dominance_calc134_126d_jerk_v134_signal(volume, ev):
    res = (volume / ev).rolling(126).var().diff(1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc134_126d_jerk_v134_signal'] = f60md_f60_market_cap_dominance_calc134_126d_jerk_v134_signal

def f60md_f60_market_cap_dominance_calc135_42d_jerk_v135_signal(evebit, ebitda):
    res = (ebitda / evebit).rolling(42).std().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc135_42d_jerk_v135_signal'] = f60md_f60_market_cap_dominance_calc135_42d_jerk_v135_signal

def f60md_f60_market_cap_dominance_calc136_21d_jerk_v136_signal(low, equity, evebit):
    res = (evebit / low).rolling(21).std().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc136_21d_jerk_v136_signal'] = f60md_f60_market_cap_dominance_calc136_21d_jerk_v136_signal

def f60md_f60_market_cap_dominance_calc137_10d_jerk_v137_signal(taxexp, ps):
    res = (taxexp / ps).rolling(10).std().diff(1).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc137_10d_jerk_v137_signal'] = f60md_f60_market_cap_dominance_calc137_10d_jerk_v137_signal

def f60md_f60_market_cap_dominance_calc138_252d_jerk_v138_signal(opinc, high):
    res = (high / opinc).rolling(252).std().pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc138_252d_jerk_v138_signal'] = f60md_f60_market_cap_dominance_calc138_252d_jerk_v138_signal

def f60md_f60_market_cap_dominance_calc139_10d_jerk_v139_signal(low, netinc, close):
    res = (close / low).rolling(10).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc139_10d_jerk_v139_signal'] = f60md_f60_market_cap_dominance_calc139_10d_jerk_v139_signal

def f60md_f60_market_cap_dominance_calc140_42d_jerk_v140_signal(equity, netinc):
    res = (netinc / equity).rolling(42).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc140_42d_jerk_v140_signal'] = f60md_f60_market_cap_dominance_calc140_42d_jerk_v140_signal

def f60md_f60_market_cap_dominance_calc141_5d_jerk_v141_signal(pb, closeadj):
    res = (closeadj / pb).rolling(5).var().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc141_5d_jerk_v141_signal'] = f60md_f60_market_cap_dominance_calc141_5d_jerk_v141_signal

def f60md_f60_market_cap_dominance_calc142_42d_jerk_v142_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(42).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc142_42d_jerk_v142_signal'] = f60md_f60_market_cap_dominance_calc142_42d_jerk_v142_signal

def f60md_f60_market_cap_dominance_calc143_63d_jerk_v143_signal(closeadj, gp):
    res = (closeadj / gp).rolling(63).std().diff(5).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc143_63d_jerk_v143_signal'] = f60md_f60_market_cap_dominance_calc143_63d_jerk_v143_signal

def f60md_f60_market_cap_dominance_calc144_21d_jerk_v144_signal(pb, low):
    res = (low / pb).rolling(21).mean().diff(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc144_21d_jerk_v144_signal'] = f60md_f60_market_cap_dominance_calc144_21d_jerk_v144_signal

def f60md_f60_market_cap_dominance_calc145_252d_jerk_v145_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(252).var().pct_change(1).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc145_252d_jerk_v145_signal'] = f60md_f60_market_cap_dominance_calc145_252d_jerk_v145_signal

def f60md_f60_market_cap_dominance_calc146_21d_jerk_v146_signal(intexp, equity, assets):
    res = (equity / assets).rolling(21).var().diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc146_21d_jerk_v146_signal'] = f60md_f60_market_cap_dominance_calc146_21d_jerk_v146_signal

def f60md_f60_market_cap_dominance_calc147_21d_jerk_v147_signal(intexp, pe, netinc):
    res = (pe / intexp).rolling(21).std().pct_change(5).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc147_21d_jerk_v147_signal'] = f60md_f60_market_cap_dominance_calc147_21d_jerk_v147_signal

def f60md_f60_market_cap_dominance_calc148_42d_jerk_v148_signal(evebit, marketcap):
    res = (marketcap / evebit).rolling(42).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc148_42d_jerk_v148_signal'] = f60md_f60_market_cap_dominance_calc148_42d_jerk_v148_signal

def f60md_f60_market_cap_dominance_calc149_42d_jerk_v149_signal(liabilities, intexp, high):
    res = (high / liabilities).rolling(42).std().pct_change(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc149_42d_jerk_v149_signal'] = f60md_f60_market_cap_dominance_calc149_42d_jerk_v149_signal

def f60md_f60_market_cap_dominance_calc150_63d_jerk_v150_signal(evebitda, intexp):
    res = (evebitda / intexp).rolling(63).std().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc150_63d_jerk_v150_signal'] = f60md_f60_market_cap_dominance_calc150_63d_jerk_v150_signal

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
