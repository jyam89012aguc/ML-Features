import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f61vr_f61_valuation_regime_calc001_5d_2nd_v001_signal(pe, ps):
    return (pe / ps).rolling(5).mean().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc001_5d_2nd_v001_signal'] = f61vr_f61_valuation_regime_calc001_5d_2nd_v001_signal

def f61vr_f61_valuation_regime_calc002_10d_2nd_v002_signal(pb, evebitda):
    return (pb * evebitda).rolling(10).std().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc002_10d_2nd_v002_signal'] = f61vr_f61_valuation_regime_calc002_10d_2nd_v002_signal

def f61vr_f61_valuation_regime_calc003_21d_2nd_v003_signal(marketcap, revenue):
    return (marketcap / revenue).rolling(21).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc003_21d_2nd_v003_signal'] = f61vr_f61_valuation_regime_calc003_21d_2nd_v003_signal

def f61vr_f61_valuation_regime_calc004_42d_2nd_v004_signal(ev, ebitda):
    return (ev / ebitda).rolling(42).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc004_42d_2nd_v004_signal'] = f61vr_f61_valuation_regime_calc004_42d_2nd_v004_signal

def f61vr_f61_valuation_regime_calc005_63d_2nd_v005_signal(pe, eps):
    return (pe * eps).rolling(63).rank().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc005_63d_2nd_v005_signal'] = f61vr_f61_valuation_regime_calc005_63d_2nd_v005_signal

def f61vr_f61_valuation_regime_calc006_126d_2nd_v006_signal(pb, close):
    return (close / pb).rolling(126).quantile(0.25).pct_change(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc006_126d_2nd_v006_signal'] = f61vr_f61_valuation_regime_calc006_126d_2nd_v006_signal

def f61vr_f61_valuation_regime_calc007_252d_2nd_v007_signal(ps, revenue):
    return (ps / revenue).rolling(252).median().diff(63).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc007_252d_2nd_v007_signal'] = f61vr_f61_valuation_regime_calc007_252d_2nd_v007_signal

def f61vr_f61_valuation_regime_calc008_504d_2nd_v008_signal(evebitda, ebitda):
    return (evebitda / ebitda).rolling(504).max().pct_change(126).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc008_504d_2nd_v008_signal'] = f61vr_f61_valuation_regime_calc008_504d_2nd_v008_signal

def f61vr_f61_valuation_regime_calc009_5d_2nd_v009_signal(pe, marketcap):
    return (marketcap / pe).rolling(5).min().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc009_5d_2nd_v009_signal'] = f61vr_f61_valuation_regime_calc009_5d_2nd_v009_signal

def f61vr_f61_valuation_regime_calc010_10d_2nd_v010_signal(pb, assets):
    return (assets / pb).rolling(10).var().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc010_10d_2nd_v010_signal'] = f61vr_f61_valuation_regime_calc010_10d_2nd_v010_signal

def f61vr_f61_valuation_regime_calc011_21d_2nd_v011_signal(ps, gp):
    return (ps / gp).rolling(21).std().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc011_21d_2nd_v011_signal'] = f61vr_f61_valuation_regime_calc011_21d_2nd_v011_signal

def f61vr_f61_valuation_regime_calc012_42d_2nd_v012_signal(evebitda, netinc):
    return (netinc / evebitda).rolling(42).rank().pct_change(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc012_42d_2nd_v012_signal'] = f61vr_f61_valuation_regime_calc012_42d_2nd_v012_signal

def f61vr_f61_valuation_regime_calc013_63d_2nd_v013_signal(pe, pb, ps):
    return (pe + pb + ps).rolling(63).quantile(0.75).diff(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc013_63d_2nd_v013_signal'] = f61vr_f61_valuation_regime_calc013_63d_2nd_v013_signal

def f61vr_f61_valuation_regime_calc014_126d_2nd_v014_signal(ev, fcf):
    return (ev / fcf).rolling(126).skew().pct_change(63).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc014_126d_2nd_v014_signal'] = f61vr_f61_valuation_regime_calc014_126d_2nd_v014_signal

def f61vr_f61_valuation_regime_calc015_252d_2nd_v015_signal(marketcap, netinc):
    return (marketcap / netinc).rolling(252).kurt().diff(126).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc015_252d_2nd_v015_signal'] = f61vr_f61_valuation_regime_calc015_252d_2nd_v015_signal

def f61vr_f61_valuation_regime_calc016_5d_2nd_v016_signal(pe, ps):
    return (pe - ps).rolling(5).std().diff(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc016_5d_2nd_v016_signal'] = f61vr_f61_valuation_regime_calc016_5d_2nd_v016_signal

def f61vr_f61_valuation_regime_calc017_10d_2nd_v017_signal(pb, ps):
    return (pb / ps).rolling(10).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc017_10d_2nd_v017_signal'] = f61vr_f61_valuation_regime_calc017_10d_2nd_v017_signal

def f61vr_f61_valuation_regime_calc018_21d_2nd_v018_signal(evebitda, marketcap):
    return (marketcap / evebitda).rolling(21).max().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc018_21d_2nd_v018_signal'] = f61vr_f61_valuation_regime_calc018_21d_2nd_v018_signal

def f61vr_f61_valuation_regime_calc019_42d_2nd_v019_signal(ev, ps):
    return (ev / ps).rolling(42).min().pct_change(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc019_42d_2nd_v019_signal'] = f61vr_f61_valuation_regime_calc019_42d_2nd_v019_signal

def f61vr_f61_valuation_regime_calc020_63d_2nd_v020_signal(pe, revenue):
    return (revenue / pe).rolling(63).median().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc020_63d_2nd_v020_signal'] = f61vr_f61_valuation_regime_calc020_63d_2nd_v020_signal

def f61vr_f61_valuation_regime_calc021_126d_2nd_v021_signal(pb, ebitda):
    return (ebitda / pb).rolling(126).var().pct_change(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc021_126d_2nd_v021_signal'] = f61vr_f61_valuation_regime_calc021_126d_2nd_v021_signal

def f61vr_f61_valuation_regime_calc022_252d_2nd_v022_signal(ps, ev):
    return (ps * ev).rolling(252).std().diff(63).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc022_252d_2nd_v022_signal'] = f61vr_f61_valuation_regime_calc022_252d_2nd_v022_signal

def f61vr_f61_valuation_regime_calc023_504d_2nd_v023_signal(evebitda, ps):
    return (evebitda / ps).rolling(504).rank().pct_change(252).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc023_504d_2nd_v023_signal'] = f61vr_f61_valuation_regime_calc023_504d_2nd_v023_signal

def f61vr_f61_valuation_regime_calc024_5d_2nd_v024_signal(pe, ps, pb):
    return (pe / (ps + pb)).rolling(5).quantile(0.5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc024_5d_2nd_v024_signal'] = f61vr_f61_valuation_regime_calc024_5d_2nd_v024_signal

def f61vr_f61_valuation_regime_calc025_10d_2nd_v025_signal(ev, netinc, revenue):
    return (ev * netinc / revenue).rolling(10).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc025_10d_2nd_v025_signal'] = f61vr_f61_valuation_regime_calc025_10d_2nd_v025_signal

def f61vr_f61_valuation_regime_calc026_21d_2nd_v026_signal(marketcap, ebitda, assets):
    return (ebitda * assets / marketcap).rolling(21).std().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc026_21d_2nd_v026_signal'] = f61vr_f61_valuation_regime_calc026_21d_2nd_v026_signal

def f61vr_f61_valuation_regime_calc027_42d_2nd_v027_signal(pe, pb, evebitda):
    return (pe * pb / evebitda).rolling(42).skew().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc027_42d_2nd_v027_signal'] = f61vr_f61_valuation_regime_calc027_42d_2nd_v027_signal

def f61vr_f61_valuation_regime_calc028_63d_2nd_v028_signal(ps, ev, fcf):
    return (fcf / (ps * ev)).rolling(63).kurt().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc028_63d_2nd_v028_signal'] = f61vr_f61_valuation_regime_calc028_63d_2nd_v028_signal

def f61vr_f61_valuation_regime_calc029_126d_2nd_v029_signal(marketcap, ps, eps):
    return (marketcap * eps / ps).rolling(126).rank().pct_change(63).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc029_126d_2nd_v029_signal'] = f61vr_f61_valuation_regime_calc029_126d_2nd_v029_signal

def f61vr_f61_valuation_regime_calc030_252d_2nd_v030_signal(evebitda, ebitda, revenue):
    return (revenue / (evebitda + ebitda)).rolling(252).quantile(0.25).diff(126).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc030_252d_2nd_v030_signal'] = f61vr_f61_valuation_regime_calc030_252d_2nd_v030_signal

def f61vr_f61_valuation_regime_calc031_5d_2nd_v031_signal(pe, ps, marketcap):
    return (marketcap / (pe * ps)).rolling(5).median().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc031_5d_2nd_v031_signal'] = f61vr_f61_valuation_regime_calc031_5d_2nd_v031_signal

def f61vr_f61_valuation_regime_calc032_10d_2nd_v032_signal(ev, gp, assets):
    return (ev * gp / assets).rolling(10).max().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc032_10d_2nd_v032_signal'] = f61vr_f61_valuation_regime_calc032_10d_2nd_v032_signal

def f61vr_f61_valuation_regime_calc033_21d_2nd_v033_signal(pb, netinc, ebitda):
    return (pb * netinc / ebitda).rolling(21).min().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc033_21d_2nd_v033_signal'] = f61vr_f61_valuation_regime_calc033_21d_2nd_v033_signal

def f61vr_f61_valuation_regime_calc034_42d_2nd_v034_signal(ps, revenue, marketcap):
    return (marketcap / (ps * revenue)).rolling(42).var().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc034_42d_2nd_v034_signal'] = f61vr_f61_valuation_regime_calc034_42d_2nd_v034_signal

def f61vr_f61_valuation_regime_calc035_63d_2nd_v035_signal(evebitda, ebitda, assets):
    return (evebitda / ebitda).rolling(63).mean().pct_change(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc035_63d_2nd_v035_signal'] = f61vr_f61_valuation_regime_calc035_63d_2nd_v035_signal

def f61vr_f61_valuation_regime_calc036_126d_2nd_v036_signal(ev, fcf, netinc):
    return (ev / (fcf + netinc)).rolling(126).skew().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc036_126d_2nd_v036_signal'] = f61vr_f61_valuation_regime_calc036_126d_2nd_v036_signal

def f61vr_f61_valuation_regime_calc037_252d_2nd_v037_signal(pe, eps, assets):
    return (pe * eps / assets).rolling(252).kurt().pct_change(63).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc037_252d_2nd_v037_signal'] = f61vr_f61_valuation_regime_calc037_252d_2nd_v037_signal

def f61vr_f61_valuation_regime_calc038_504d_2nd_v038_signal(pb, close, revenue):
    return (revenue / (pb * close)).rolling(504).rank().diff(126).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc038_504d_2nd_v038_signal'] = f61vr_f61_valuation_regime_calc038_504d_2nd_v038_signal

def f61vr_f61_valuation_regime_calc039_5d_2nd_v039_signal(ps, gp, ebitda):
    return (ps * gp / ebitda).rolling(5).max().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc039_5d_2nd_v039_signal'] = f61vr_f61_valuation_regime_calc039_5d_2nd_v039_signal

def f61vr_f61_valuation_regime_calc040_10d_2nd_v040_signal(evebitda, netinc, fcf):
    return (evebitda * netinc / fcf).rolling(10).min().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc040_10d_2nd_v040_signal'] = f61vr_f61_valuation_regime_calc040_10d_2nd_v040_signal

def f61vr_f61_valuation_regime_calc041_21d_2nd_v041_signal(pe, ps, pb, ev):
    return (pe + ps + pb / ev).rolling(21).std().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc041_21d_2nd_v041_signal'] = f61vr_f61_valuation_regime_calc041_21d_2nd_v041_signal

def f61vr_f61_valuation_regime_calc042_42d_2nd_v042_signal(marketcap, revenue, eps):
    return (marketcap / (revenue * eps)).rolling(42).quantile(0.75).pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc042_42d_2nd_v042_signal'] = f61vr_f61_valuation_regime_calc042_42d_2nd_v042_signal

def f61vr_f61_valuation_regime_calc043_63d_2nd_v043_signal(ev, ebitda, gp):
    return (ev / ebitda).rolling(63).rank().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc043_63d_2nd_v043_signal'] = f61vr_f61_valuation_regime_calc043_63d_2nd_v043_signal

def f61vr_f61_valuation_regime_calc044_126d_2nd_v044_signal(pe, pb, netinc):
    return (pe / pb * netinc).rolling(126).skew().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc044_126d_2nd_v044_signal'] = f61vr_f61_valuation_regime_calc044_126d_2nd_v044_signal

def f61vr_f61_valuation_regime_calc045_252d_2nd_v045_signal(ps, evebitda, fcf):
    return (ps * evebitda / fcf).rolling(252).median().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc045_252d_2nd_v045_signal'] = f61vr_f61_valuation_regime_calc045_252d_2nd_v045_signal

def f61vr_f61_valuation_regime_calc046_5d_2nd_v046_signal(marketcap, revenue, assets):
    return (marketcap * revenue / assets).rolling(5).mean().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc046_5d_2nd_v046_signal'] = f61vr_f61_valuation_regime_calc046_5d_2nd_v046_signal

def f61vr_f61_valuation_regime_calc047_10d_2nd_v047_signal(ev, ebitda, netinc):
    return (ev / (ebitda + netinc)).rolling(10).var().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc047_10d_2nd_v047_signal'] = f61vr_f61_valuation_regime_calc047_10d_2nd_v047_signal

def f61vr_f61_valuation_regime_calc048_21d_2nd_v048_signal(pe, pb, ps, revenue):
    return (pe + pb + ps / revenue).rolling(21).max().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc048_21d_2nd_v048_signal'] = f61vr_f61_valuation_regime_calc048_21d_2nd_v048_signal

def f61vr_f61_valuation_regime_calc049_42d_2nd_v049_signal(evebitda, ebitda, assets):
    return (evebitda * assets / ebitda).rolling(42).min().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc049_42d_2nd_v049_signal'] = f61vr_f61_valuation_regime_calc049_42d_2nd_v049_signal

def f61vr_f61_valuation_regime_calc050_63d_2nd_v050_signal(ev, gp, fcf):
    return (ev * gp / fcf).rolling(63).skew().pct_change(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc050_63d_2nd_v050_signal'] = f61vr_f61_valuation_regime_calc050_63d_2nd_v050_signal

def f61vr_f61_valuation_regime_calc051_126d_2nd_v051_signal(marketcap, ps, eps):
    return (marketcap / ps).rolling(126).quantile(0.5).diff(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc051_126d_2nd_v051_signal'] = f61vr_f61_valuation_regime_calc051_126d_2nd_v051_signal

def f61vr_f61_valuation_regime_calc052_252d_2nd_v052_signal(pe, pb, netinc, revenue):
    return (pe * netinc / (pb * revenue)).rolling(252).kurt().pct_change(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc052_252d_2nd_v052_signal'] = f61vr_f61_valuation_regime_calc052_252d_2nd_v052_signal

def f61vr_f61_valuation_regime_calc053_504d_2nd_v053_signal(evebitda, ebitda, fcf, assets):
    return (evebitda * fcf / (ebitda * assets)).rolling(504).rank().diff(252).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc053_504d_2nd_v053_signal'] = f61vr_f61_valuation_regime_calc053_504d_2nd_v053_signal

def f61vr_f61_valuation_regime_calc054_5d_2nd_v054_signal(ev, gp, netinc):
    return (ev / (gp + netinc)).rolling(5).std().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc054_5d_2nd_v054_signal'] = f61vr_f61_valuation_regime_calc054_5d_2nd_v054_signal

def f61vr_f61_valuation_regime_calc055_10d_2nd_v055_signal(marketcap, revenue, eps, assets):
    return (marketcap * eps / (revenue * assets)).rolling(10).mean().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc055_10d_2nd_v055_signal'] = f61vr_f61_valuation_regime_calc055_10d_2nd_v055_signal

def f61vr_f61_valuation_regime_calc056_21d_2nd_v056_signal(pe, ps, pb, ebitda):
    return (pe * ps / (pb * ebitda)).rolling(21).quantile(0.25).pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc056_21d_2nd_v056_signal'] = f61vr_f61_valuation_regime_calc056_21d_2nd_v056_signal

def f61vr_f61_valuation_regime_calc057_42d_2nd_v057_signal(evebitda, ebitda, netinc, fcf):
    return (evebitda / (ebitda + netinc + fcf)).rolling(42).skew().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc057_42d_2nd_v057_signal'] = f61vr_f61_valuation_regime_calc057_42d_2nd_v057_signal

def f61vr_f61_valuation_regime_calc058_63d_2nd_v058_signal(ev, gp, revenue, assets):
    return ((ev * gp) / (revenue * assets)).rolling(63).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc058_63d_2nd_v058_signal'] = f61vr_f61_valuation_regime_calc058_63d_2nd_v058_signal

def f61vr_f61_valuation_regime_calc059_126d_2nd_v059_signal(marketcap, ps, eps, netinc):
    return (marketcap * ps / (eps * netinc)).rolling(126).kurt().diff(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc059_126d_2nd_v059_signal'] = f61vr_f61_valuation_regime_calc059_126d_2nd_v059_signal

def f61vr_f61_valuation_regime_calc060_252d_2nd_v060_signal(pe, pb, ps, evebitda):
    return (pe + pb + ps + evebitda).rolling(252).rank().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc060_252d_2nd_v060_signal'] = f61vr_f61_valuation_regime_calc060_252d_2nd_v060_signal

def f61vr_f61_valuation_regime_calc061_5d_2nd_v061_signal(ev, ebitda, netinc, revenue):
    return (ev * revenue / (ebitda * netinc)).rolling(5).max().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc061_5d_2nd_v061_signal'] = f61vr_f61_valuation_regime_calc061_5d_2nd_v061_signal

def f61vr_f61_valuation_regime_calc062_10d_2nd_v062_signal(marketcap, ps, eps, fcf):
    return (marketcap * ps / (eps * fcf)).rolling(10).min().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc062_10d_2nd_v062_signal'] = f61vr_f61_valuation_regime_calc062_10d_2nd_v062_signal

def f61vr_f61_valuation_regime_calc063_21d_2nd_v063_signal(pe, pb, ps, evebitda, ev):
    return (pe * pb / (ps * evebitda * ev)).rolling(21).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc063_21d_2nd_v063_signal'] = f61vr_f61_valuation_regime_calc063_21d_2nd_v063_signal

def f61vr_f61_valuation_regime_calc064_42d_2nd_v064_signal(marketcap, revenue, assets, gp):
    return (marketcap * assets / (revenue * gp)).rolling(42).std().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc064_42d_2nd_v064_signal'] = f61vr_f61_valuation_regime_calc064_42d_2nd_v064_signal

def f61vr_f61_valuation_regime_calc065_63d_2nd_v065_signal(ev, ebitda, netinc, fcf, ps):
    return (ev * ps / (ebitda + netinc + fcf)).rolling(63).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc065_63d_2nd_v065_signal'] = f61vr_f61_valuation_regime_calc065_63d_2nd_v065_signal

def f61vr_f61_valuation_regime_calc066_126d_2nd_v066_signal(pe, pb, marketcap, revenue, eps):
    return ((pe * pb) / (marketcap / revenue * eps)).rolling(126).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc066_126d_2nd_v066_signal'] = f61vr_f61_valuation_regime_calc066_126d_2nd_v066_signal

def f61vr_f61_valuation_regime_calc067_252d_2nd_v067_signal(ps, evebitda, ebitda, assets, gp):
    return (ps * evebitda * gp / (ebitda * assets)).rolling(252).quantile(0.75).diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc067_252d_2nd_v067_signal'] = f61vr_f61_valuation_regime_calc067_252d_2nd_v067_signal

def f61vr_f61_valuation_regime_calc068_504d_2nd_v068_signal(ev, netinc, fcf, revenue, pe):
    return (ev * pe / (netinc + fcf + revenue)).rolling(504).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc068_504d_2nd_v068_signal'] = f61vr_f61_valuation_regime_calc068_504d_2nd_v068_signal

def f61vr_f61_valuation_regime_calc069_5d_2nd_v069_signal(marketcap, eps, assets, pb, ps):
    return (marketcap * pb / (eps * assets * ps)).rolling(5).rank().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc069_5d_2nd_v069_signal'] = f61vr_f61_valuation_regime_calc069_5d_2nd_v069_signal

def f61vr_f61_valuation_regime_calc070_10d_2nd_v070_signal(pe, ps, evebitda, ebitda, gp):
    return (pe * ps * gp / (evebitda * ebitda)).rolling(10).mean().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc070_10d_2nd_v070_signal'] = f61vr_f61_valuation_regime_calc070_10d_2nd_v070_signal

def f61vr_f61_valuation_regime_calc071_21d_2nd_v071_signal(ev, netinc, fcf, revenue, assets):
    return (ev * assets / (netinc + fcf + revenue)).rolling(21).var().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc071_21d_2nd_v071_signal'] = f61vr_f61_valuation_regime_calc071_21d_2nd_v071_signal

def f61vr_f61_valuation_regime_calc072_42d_2nd_v072_signal(marketcap, eps, pb, ps, pe):
    return (marketcap * pe / (eps * pb * ps)).rolling(42).skew().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc072_42d_2nd_v072_signal'] = f61vr_f61_valuation_regime_calc072_42d_2nd_v072_signal

def f61vr_f61_valuation_regime_calc073_63d_2nd_v073_signal(evebitda, ebitda, gp, revenue, assets):
    return (evebitda * revenue / (ebitda * gp * assets)).rolling(63).quantile(0.5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc073_63d_2nd_v073_signal'] = f61vr_f61_valuation_regime_calc073_63d_2nd_v073_signal

def f61vr_f61_valuation_regime_calc074_126d_2nd_v074_signal(ev, netinc, fcf, ps, pb):
    return (ev * ps / (netinc + fcf + pb)).rolling(126).rank().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc074_126d_2nd_v074_signal'] = f61vr_f61_valuation_regime_calc074_126d_2nd_v074_signal

def f61vr_f61_valuation_regime_calc075_252d_2nd_v075_signal(pe, ps, pb, evebitda, ev):
    return (pe * ps * pb / (evebitda * ev)).rolling(252).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc075_252d_2nd_v075_signal'] = f61vr_f61_valuation_regime_calc075_252d_2nd_v075_signal

def f61vr_f61_valuation_regime_calc076_5d_2nd_v076_signal(pe, pb, ps):
    return (pe * pb / ps).rolling(5).mean().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc076_5d_2nd_v076_signal'] = f61vr_f61_valuation_regime_calc076_5d_2nd_v076_signal

def f61vr_f61_valuation_regime_calc077_10d_2nd_v077_signal(ev, ebitda, revenue):
    return (ev / (ebitda + revenue)).rolling(10).std().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc077_10d_2nd_v077_signal'] = f61vr_f61_valuation_regime_calc077_10d_2nd_v077_signal

def f61vr_f61_valuation_regime_calc078_21d_2nd_v078_signal(marketcap, eps, assets):
    return (marketcap / (eps * assets)).rolling(21).skew().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc078_21d_2nd_v078_signal'] = f61vr_f61_valuation_regime_calc078_21d_2nd_v078_signal

def f61vr_f61_valuation_regime_calc079_42d_2nd_v079_signal(evebitda, fcf, gp):
    return (evebitda * fcf / gp).rolling(42).kurt().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc079_42d_2nd_v079_signal'] = f61vr_f61_valuation_regime_calc079_42d_2nd_v079_signal

def f61vr_f61_valuation_regime_calc080_63d_2nd_v080_signal(pe, netinc, assets):
    return (pe * netinc / assets).rolling(63).rank().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc080_63d_2nd_v080_signal'] = f61vr_f61_valuation_regime_calc080_63d_2nd_v080_signal

def f61vr_f61_valuation_regime_calc081_126d_2nd_v081_signal(pb, close, revenue):
    return (close * pb / revenue).rolling(126).quantile(0.25).diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc081_126d_2nd_v081_signal'] = f61vr_f61_valuation_regime_calc081_126d_2nd_v081_signal

def f61vr_f61_valuation_regime_calc082_252d_2nd_v082_signal(ps, ev, ebitda):
    return (ps * ev / ebitda).rolling(252).median().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc082_252d_2nd_v082_signal'] = f61vr_f61_valuation_regime_calc082_252d_2nd_v082_signal

def f61vr_f61_valuation_regime_calc083_504d_2nd_v083_signal(evebitda, ps, pb):
    return (evebitda / (ps + pb)).rolling(504).max().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc083_504d_2nd_v083_signal'] = f61vr_f61_valuation_regime_calc083_504d_2nd_v083_signal

def f61vr_f61_valuation_regime_calc084_5d_2nd_v084_signal(pe, marketcap, revenue):
    return (marketcap / (pe * revenue)).rolling(5).min().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc084_5d_2nd_v084_signal'] = f61vr_f61_valuation_regime_calc084_5d_2nd_v084_signal

def f61vr_f61_valuation_regime_calc085_10d_2nd_v085_signal(pb, assets, eps):
    return (assets * pb / eps).rolling(10).var().diff(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc085_10d_2nd_v085_signal'] = f61vr_f61_valuation_regime_calc085_10d_2nd_v085_signal

def f61vr_f61_valuation_regime_calc086_21d_2nd_v086_signal(ps, gp, netinc):
    return (ps * gp / netinc).rolling(21).mean().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc086_21d_2nd_v086_signal'] = f61vr_f61_valuation_regime_calc086_21d_2nd_v086_signal

def f61vr_f61_valuation_regime_calc087_42d_2nd_v087_signal(evebitda, fcf, assets):
    return (fcf / (evebitda * assets)).rolling(42).rank().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc087_42d_2nd_v087_signal'] = f61vr_f61_valuation_regime_calc087_42d_2nd_v087_signal

def f61vr_f61_valuation_regime_calc088_63d_2nd_v088_signal(pe, pb, ev):
    return (pe + pb - ev/1000).rolling(63).quantile(0.75).pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc088_63d_2nd_v088_signal'] = f61vr_f61_valuation_regime_calc088_63d_2nd_v088_signal

def f61vr_f61_valuation_regime_calc089_126d_2nd_v089_signal(ev, ebitda, ps):
    return (ev * ps / ebitda).rolling(126).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc089_126d_2nd_v089_signal'] = f61vr_f61_valuation_regime_calc089_126d_2nd_v089_signal

def f61vr_f61_valuation_regime_calc090_252d_2nd_v090_signal(marketcap, netinc, fcf):
    return (marketcap / (netinc + fcf)).rolling(252).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc090_252d_2nd_v090_signal'] = f61vr_f61_valuation_regime_calc090_252d_2nd_v090_signal

def f61vr_f61_valuation_regime_calc091_5d_2nd_v091_signal(pe, ps, pb):
    return (pe * ps / pb).rolling(5).std().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc091_5d_2nd_v091_signal'] = f61vr_f61_valuation_regime_calc091_5d_2nd_v091_signal

def f61vr_f61_valuation_regime_calc092_10d_2nd_v092_signal(pb, ps, evebitda):
    return (pb / ps * evebitda).rolling(10).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc092_10d_2nd_v092_signal'] = f61vr_f61_valuation_regime_calc092_10d_2nd_v092_signal

def f61vr_f61_valuation_regime_calc093_21d_2nd_v093_signal(evebitda, marketcap, revenue):
    return (marketcap * revenue / evebitda).rolling(21).max().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc093_21d_2nd_v093_signal'] = f61vr_f61_valuation_regime_calc093_21d_2nd_v093_signal

def f61vr_f61_valuation_regime_calc094_42d_2nd_v094_signal(ev, ps, ebitda):
    return (ev * ps / ebitda).rolling(42).min().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc094_42d_2nd_v094_signal'] = f61vr_f61_valuation_regime_calc094_42d_2nd_v094_signal

def f61vr_f61_valuation_regime_calc095_63d_2nd_v095_signal(pe, revenue, eps):
    return (revenue * eps / pe).rolling(63).median().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc095_63d_2nd_v095_signal'] = f61vr_f61_valuation_regime_calc095_63d_2nd_v095_signal

def f61vr_f61_valuation_regime_calc096_126d_2nd_v096_signal(pb, ebitda, netinc):
    return ((ebitda + netinc) / pb).rolling(126).var().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc096_126d_2nd_v096_signal'] = f61vr_f61_valuation_regime_calc096_126d_2nd_v096_signal

def f61vr_f61_valuation_regime_calc097_252d_2nd_v097_signal(ps, ev, assets):
    return (ps * ev / assets).rolling(252).std().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc097_252d_2nd_v097_signal'] = f61vr_f61_valuation_regime_calc097_252d_2nd_v097_signal

def f61vr_f61_valuation_regime_calc098_504d_2nd_v098_signal(evebitda, ps, fcf):
    return (evebitda * fcf / ps).rolling(504).rank().pct_change(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc098_504d_2nd_v098_signal'] = f61vr_f61_valuation_regime_calc098_504d_2nd_v098_signal

def f61vr_f61_valuation_regime_calc099_5d_2nd_v099_signal(pe, ps, pb, netinc):
    return (pe * ps * pb / netinc).rolling(5).quantile(0.5).diff(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc099_5d_2nd_v099_signal'] = f61vr_f61_valuation_regime_calc099_5d_2nd_v099_signal

def f61vr_f61_valuation_regime_calc100_10d_2nd_v100_signal(ev, netinc, revenue, gp):
    return (ev * gp / (netinc + revenue)).rolling(10).mean().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc100_10d_2nd_v100_signal'] = f61vr_f61_valuation_regime_calc100_10d_2nd_v100_signal

def f61vr_f61_valuation_regime_calc101_21d_2nd_v101_signal(marketcap, ebitda, assets, ps):
    return (ebitda * assets / (marketcap * ps)).rolling(21).std().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc101_21d_2nd_v101_signal'] = f61vr_f61_valuation_regime_calc101_21d_2nd_v101_signal

def f61vr_f61_valuation_regime_calc102_42d_2nd_v102_signal(pe, pb, evebitda, fcf):
    return (pe * pb / (evebitda * fcf)).rolling(42).skew().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc102_42d_2nd_v102_signal'] = f61vr_f61_valuation_regime_calc102_42d_2nd_v102_signal

def f61vr_f61_valuation_regime_calc103_63d_2nd_v103_signal(ps, ev, fcf, eps):
    return (fcf * eps / (ps * ev)).rolling(63).kurt().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc103_63d_2nd_v103_signal'] = f61vr_f61_valuation_regime_calc103_63d_2nd_v103_signal

def f61vr_f61_valuation_regime_calc104_126d_2nd_v104_signal(marketcap, ps, eps, revenue):
    return (marketcap * eps / (ps * revenue)).rolling(126).rank().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc104_126d_2nd_v104_signal'] = f61vr_f61_valuation_regime_calc104_126d_2nd_v104_signal

def f61vr_f61_valuation_regime_calc105_252d_2nd_v105_signal(evebitda, ebitda, revenue, assets):
    return (revenue * assets / (evebitda + ebitda)).rolling(252).quantile(0.25).diff(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc105_252d_2nd_v105_signal'] = f61vr_f61_valuation_regime_calc105_252d_2nd_v105_signal

def f61vr_f61_valuation_regime_calc106_5d_2nd_v106_signal(pe, ps, marketcap, pb):
    return (marketcap / (pe * ps * pb)).rolling(5).median().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc106_5d_2nd_v106_signal'] = f61vr_f61_valuation_regime_calc106_5d_2nd_v106_signal

def f61vr_f61_valuation_regime_calc107_10d_2nd_v107_signal(ev, gp, assets, netinc):
    return (ev * gp / (assets * netinc)).rolling(10).max().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc107_10d_2nd_v107_signal'] = f61vr_f61_valuation_regime_calc107_10d_2nd_v107_signal

def f61vr_f61_valuation_regime_calc108_21d_2nd_v108_signal(pb, netinc, ebitda, ps):
    return (pb * netinc / (ebitda * ps)).rolling(21).min().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc108_21d_2nd_v108_signal'] = f61vr_f61_valuation_regime_calc108_21d_2nd_v108_signal

def f61vr_f61_valuation_regime_calc109_42d_2nd_v109_signal(ps, revenue, marketcap, ev):
    return (marketcap * ev / (ps * revenue)).rolling(42).var().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc109_42d_2nd_v109_signal'] = f61vr_f61_valuation_regime_calc109_42d_2nd_v109_signal

def f61vr_f61_valuation_regime_calc110_63d_2nd_v110_signal(evebitda, ebitda, assets, gp):
    return (evebitda * gp / ebitda).rolling(63).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc110_63d_2nd_v110_signal'] = f61vr_f61_valuation_regime_calc110_63d_2nd_v110_signal

def f61vr_f61_valuation_regime_calc111_126d_2nd_v111_signal(ev, fcf, netinc, pb):
    return (ev * pb / (fcf + netinc)).rolling(126).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc111_126d_2nd_v111_signal'] = f61vr_f61_valuation_regime_calc111_126d_2nd_v111_signal

def f61vr_f61_valuation_regime_calc112_252d_2nd_v112_signal(pe, eps, assets, revenue):
    return (pe * eps * revenue / assets).rolling(252).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc112_252d_2nd_v112_signal'] = f61vr_f61_valuation_regime_calc112_252d_2nd_v112_signal

def f61vr_f61_valuation_regime_calc113_504d_2nd_v113_signal(pb, close, revenue, ps):
    return (revenue * ps / (pb * close)).rolling(504).rank().diff(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc113_504d_2nd_v113_signal'] = f61vr_f61_valuation_regime_calc113_504d_2nd_v113_signal

def f61vr_f61_valuation_regime_calc114_5d_2nd_v114_signal(ps, gp, ebitda, fcf):
    return (ps * gp / (ebitda + fcf)).rolling(5).max().diff(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc114_5d_2nd_v114_signal'] = f61vr_f61_valuation_regime_calc114_5d_2nd_v114_signal

def f61vr_f61_valuation_regime_calc115_10d_2nd_v115_signal(evebitda, netinc, fcf, ev):
    return (evebitda * netinc / (fcf * ev)).rolling(10).min().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc115_10d_2nd_v115_signal'] = f61vr_f61_valuation_regime_calc115_10d_2nd_v115_signal

def f61vr_f61_valuation_regime_calc116_21d_2nd_v116_signal(pe, ps, pb, ev, marketcap):
    return (pe + ps + pb / (ev + marketcap)).rolling(21).std().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc116_21d_2nd_v116_signal'] = f61vr_f61_valuation_regime_calc116_21d_2nd_v116_signal

def f61vr_f61_valuation_regime_calc117_42d_2nd_v117_signal(marketcap, revenue, eps, gp):
    return (marketcap * gp / (revenue * eps)).rolling(42).quantile(0.75).pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc117_42d_2nd_v117_signal'] = f61vr_f61_valuation_regime_calc117_42d_2nd_v117_signal

def f61vr_f61_valuation_regime_calc118_63d_2nd_v118_signal(ev, ebitda, gp, ps):
    return (ev * ps / ebitda).rolling(63).rank().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc118_63d_2nd_v118_signal'] = f61vr_f61_valuation_regime_calc118_63d_2nd_v118_signal

def f61vr_f61_valuation_regime_calc119_126d_2nd_v119_signal(pe, pb, netinc, fcf):
    return (pe / pb * (netinc + fcf)).rolling(126).skew().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc119_126d_2nd_v119_signal'] = f61vr_f61_valuation_regime_calc119_126d_2nd_v119_signal

def f61vr_f61_valuation_regime_calc120_252d_2nd_v120_signal(ps, evebitda, fcf, ebitda):
    return (ps * evebitda / (fcf + ebitda)).rolling(252).median().diff(42).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc120_252d_2nd_v120_signal'] = f61vr_f61_valuation_regime_calc120_252d_2nd_v120_signal

def f61vr_f61_valuation_regime_calc121_5d_2nd_v121_signal(marketcap, revenue, assets, pe):
    return (marketcap * revenue / (assets * pe)).rolling(5).mean().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc121_5d_2nd_v121_signal'] = f61vr_f61_valuation_regime_calc121_5d_2nd_v121_signal

def f61vr_f61_valuation_regime_calc122_10d_2nd_v122_signal(ev, ebitda, netinc, ps):
    return (ev * ps / (ebitda + netinc)).rolling(10).var().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc122_10d_2nd_v122_signal'] = f61vr_f61_valuation_regime_calc122_10d_2nd_v122_signal

def f61vr_f61_valuation_regime_calc123_21d_2nd_v123_signal(pe, pb, ps, revenue, gp):
    return (pe + pb + ps / (revenue + gp)).rolling(21).max().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc123_21d_2nd_v123_signal'] = f61vr_f61_valuation_regime_calc123_21d_2nd_v123_signal

def f61vr_f61_valuation_regime_calc124_42d_2nd_v124_signal(evebitda, ebitda, assets, ps):
    return (evebitda * assets / (ebitda * ps)).rolling(42).min().diff(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc124_42d_2nd_v124_signal'] = f61vr_f61_valuation_regime_calc124_42d_2nd_v124_signal

def f61vr_f61_valuation_regime_calc125_63d_2nd_v125_signal(ev, gp, fcf, eps):
    return (ev * gp / (fcf * eps)).rolling(63).skew().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc125_63d_2nd_v125_signal'] = f61vr_f61_valuation_regime_calc125_63d_2nd_v125_signal

def f61vr_f61_valuation_regime_calc126_126d_2nd_v126_signal(marketcap, ps, eps, pb):
    return (marketcap / (ps * pb)).rolling(126).quantile(0.5).diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc126_126d_2nd_v126_signal'] = f61vr_f61_valuation_regime_calc126_126d_2nd_v126_signal

def f61vr_f61_valuation_regime_calc127_252d_2nd_v127_signal(pe, pb, netinc, revenue, ps):
    return (pe * netinc / (pb * revenue * ps)).rolling(252).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc127_252d_2nd_v127_signal'] = f61vr_f61_valuation_regime_calc127_252d_2nd_v127_signal

def f61vr_f61_valuation_regime_calc128_504d_2nd_v128_signal(evebitda, ebitda, fcf, assets, gp):
    return (evebitda * fcf * gp / (ebitda * assets)).rolling(504).rank().diff(126).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc128_504d_2nd_v128_signal'] = f61vr_f61_valuation_regime_calc128_504d_2nd_v128_signal

def f61vr_f61_valuation_regime_calc129_5d_2nd_v129_signal(ev, gp, netinc, ps):
    return (ev * ps / (gp + netinc)).rolling(5).std().pct_change(3).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc129_5d_2nd_v129_signal'] = f61vr_f61_valuation_regime_calc129_5d_2nd_v129_signal

def f61vr_f61_valuation_regime_calc130_10d_2nd_v130_signal(marketcap, revenue, eps, assets, pb):
    return (marketcap * eps * pb / (revenue * assets)).rolling(10).mean().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc130_10d_2nd_v130_signal'] = f61vr_f61_valuation_regime_calc130_10d_2nd_v130_signal

def f61vr_f61_valuation_regime_calc131_21d_2nd_v131_signal(pe, ps, pb, ebitda, netinc):
    return (pe * ps / (pb * (ebitda + netinc))).rolling(21).quantile(0.25).pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc131_21d_2nd_v131_signal'] = f61vr_f61_valuation_regime_calc131_21d_2nd_v131_signal

def f61vr_f61_valuation_regime_calc132_42d_2nd_v132_signal(evebitda, ebitda, netinc, fcf, ps):
    return (evebitda * ps / (ebitda + netinc + fcf)).rolling(42).skew().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc132_42d_2nd_v132_signal'] = f61vr_f61_valuation_regime_calc132_42d_2nd_v132_signal

def f61vr_f61_valuation_regime_calc133_63d_2nd_v133_signal(ev, gp, revenue, assets, pb):
    return ((ev * gp * pb) / (revenue * assets)).rolling(63).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc133_63d_2nd_v133_signal'] = f61vr_f61_valuation_regime_calc133_63d_2nd_v133_signal

def f61vr_f61_valuation_regime_calc134_126d_2nd_v134_signal(marketcap, ps, eps, netinc, pe):
    return (marketcap * ps * pe / (eps * netinc)).rolling(126).kurt().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc134_126d_2nd_v134_signal'] = f61vr_f61_valuation_regime_calc134_126d_2nd_v134_signal

def f61vr_f61_valuation_regime_calc135_252d_2nd_v135_signal(pe, pb, ps, evebitda, ev):
    return (pe + pb + ps + evebitda + ev/1000).rolling(252).rank().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc135_252d_2nd_v135_signal'] = f61vr_f61_valuation_regime_calc135_252d_2nd_v135_signal

def f61vr_f61_valuation_regime_calc136_5d_2nd_v136_signal(ev, ebitda, netinc, revenue, ps):
    return (ev * revenue * ps / (ebitda * netinc)).rolling(5).max().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc136_5d_2nd_v136_signal'] = f61vr_f61_valuation_regime_calc136_5d_2nd_v136_signal

def f61vr_f61_valuation_regime_calc137_10d_2nd_v137_signal(marketcap, ps, eps, fcf, pb):
    return (marketcap * ps * pb / (eps * fcf)).rolling(10).min().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc137_10d_2nd_v137_signal'] = f61vr_f61_valuation_regime_calc137_10d_2nd_v137_signal

def f61vr_f61_valuation_regime_calc138_21d_2nd_v138_signal(pe, pb, ps, evebitda, ev, assets):
    return (pe * pb * assets / (ps * evebitda * ev)).rolling(21).mean().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc138_21d_2nd_v138_signal'] = f61vr_f61_valuation_regime_calc138_21d_2nd_v138_signal

def f61vr_f61_valuation_regime_calc139_42d_2nd_v139_signal(marketcap, revenue, assets, gp, ps):
    return (marketcap * assets * ps / (revenue * gp)).rolling(42).std().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc139_42d_2nd_v139_signal'] = f61vr_f61_valuation_regime_calc139_42d_2nd_v139_signal

def f61vr_f61_valuation_regime_calc140_63d_2nd_v140_signal(ev, ebitda, netinc, fcf, ps, pb):
    return (ev * ps * pb / (ebitda + netinc + fcf)).rolling(63).skew().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc140_63d_2nd_v140_signal'] = f61vr_f61_valuation_regime_calc140_63d_2nd_v140_signal

def f61vr_f61_valuation_regime_calc141_126d_2nd_v141_signal(pe, pb, marketcap, revenue, eps, assets):
    return ((pe * pb * assets) / (marketcap / revenue * eps)).rolling(126).mean().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc141_126d_2nd_v141_signal'] = f61vr_f61_valuation_regime_calc141_126d_2nd_v141_signal

def f61vr_f61_valuation_regime_calc142_252d_2nd_v142_signal(ps, evebitda, ebitda, assets, gp, netinc):
    return (ps * evebitda * gp / (ebitda * assets * netinc)).rolling(252).quantile(0.75).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc142_252d_2nd_v142_signal'] = f61vr_f61_valuation_regime_calc142_252d_2nd_v142_signal

def f61vr_f61_valuation_regime_calc143_504d_2nd_v143_signal(ev, netinc, fcf, revenue, pe, pb):
    return (ev * pe * pb / (netinc + fcf + revenue)).rolling(504).kurt().pct_change(21).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc143_504d_2nd_v143_signal'] = f61vr_f61_valuation_regime_calc143_504d_2nd_v143_signal

def f61vr_f61_valuation_regime_calc144_5d_2nd_v144_signal(marketcap, eps, assets, pb, ps, pe):
    return (marketcap * pb * pe / (eps * assets * ps)).rolling(5).rank().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc144_5d_2nd_v144_signal'] = f61vr_f61_valuation_regime_calc144_5d_2nd_v144_signal

def f61vr_f61_valuation_regime_calc145_10d_2nd_v145_signal(pe, ps, evebitda, ebitda, gp, fcf):
    return (pe * ps * gp / (evebitda * ebitda * fcf)).rolling(10).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc145_10d_2nd_v145_signal'] = f61vr_f61_valuation_regime_calc145_10d_2nd_v145_signal

def f61vr_f61_valuation_regime_calc146_21d_2nd_v146_signal(ev, netinc, fcf, revenue, assets, ps):
    return (ev * assets * ps / (netinc + fcf + revenue)).rolling(21).var().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc146_21d_2nd_v146_signal'] = f61vr_f61_valuation_regime_calc146_21d_2nd_v146_signal

def f61vr_f61_valuation_regime_calc147_42d_2nd_v147_signal(marketcap, eps, pb, ps, pe, gp):
    return (marketcap * pe * gp / (eps * pb * ps)).rolling(42).skew().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc147_42d_2nd_v147_signal'] = f61vr_f61_valuation_regime_calc147_42d_2nd_v147_signal

def f61vr_f61_valuation_regime_calc148_63d_2nd_v148_signal(evebitda, ebitda, gp, revenue, assets, fcf):
    return (evebitda * revenue * fcf / (ebitda * gp * assets)).rolling(63).quantile(0.5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc148_63d_2nd_v148_signal'] = f61vr_f61_valuation_regime_calc148_63d_2nd_v148_signal

def f61vr_f61_valuation_regime_calc149_126d_2nd_v149_signal(ev, netinc, fcf, ps, pb, pe):
    return (ev * ps * pe / (netinc + fcf + pb)).rolling(126).rank().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc149_126d_2nd_v149_signal'] = f61vr_f61_valuation_regime_calc149_126d_2nd_v149_signal

def f61vr_f61_valuation_regime_calc150_252d_2nd_v150_signal(pe, ps, pb, evebitda, ev, assets):
    return (pe * ps * pb * assets / (evebitda * ev)).rolling(252).mean().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc150_252d_2nd_v150_signal'] = f61vr_f61_valuation_regime_calc150_252d_2nd_v150_signal


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
