import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f61vr_f61_valuation_regime_calc001_5d_base_v001_signal(pe, pb):
    res = (pe / pb).pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc001_5d_base_v001_signal'] = f61vr_f61_valuation_regime_calc001_5d_base_v001_signal

def f61vr_f61_valuation_regime_calc002_10d_base_v002_signal(ps, evebitda):
    res = (ps * evebitda).diff(5).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc002_10d_base_v002_signal'] = f61vr_f61_valuation_regime_calc002_10d_base_v002_signal

def f61vr_f61_valuation_regime_calc003_21d_base_v003_signal(marketcap, revenue):
    res = np.log((marketcap / revenue).abs().replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc003_21d_base_v003_signal'] = f61vr_f61_valuation_regime_calc003_21d_base_v003_signal

def f61vr_f61_valuation_regime_calc004_42d_base_v004_signal(ev, ebitda):
    res = (ev / ebitda).pct_change(5).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc004_42d_base_v004_signal'] = f61vr_f61_valuation_regime_calc004_42d_base_v004_signal

def f61vr_f61_valuation_regime_calc005_63d_base_v005_signal(pe, eps):
    res = (pe * eps).diff(10).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc005_63d_base_v005_signal'] = f61vr_f61_valuation_regime_calc005_63d_base_v005_signal

def f61vr_f61_valuation_regime_calc006_126d_base_v006_signal(pb, close):
    res = (close / pb).rolling(126).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc006_126d_base_v006_signal'] = f61vr_f61_valuation_regime_calc006_126d_base_v006_signal

def f61vr_f61_valuation_regime_calc007_252d_base_v007_signal(ps, revenue):
    res = (ps / revenue).pct_change(21).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc007_252d_base_v007_signal'] = f61vr_f61_valuation_regime_calc007_252d_base_v007_signal

def f61vr_f61_valuation_regime_calc008_504d_base_v008_signal(evebitda, ebitda):
    res = (evebitda / ebitda).diff(63).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc008_504d_base_v008_signal'] = f61vr_f61_valuation_regime_calc008_504d_base_v008_signal

def f61vr_f61_valuation_regime_calc009_5d_base_v009_signal(pe, marketcap):
    res = (marketcap / pe).pct_change(1).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc009_5d_base_v009_signal'] = f61vr_f61_valuation_regime_calc009_5d_base_v009_signal

def f61vr_f61_valuation_regime_calc010_10d_base_v010_signal(pb, assets):
    res = (assets / pb).diff(1).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc010_10d_base_v010_signal'] = f61vr_f61_valuation_regime_calc010_10d_base_v010_signal

def f61vr_f61_valuation_regime_calc011_21d_base_v011_signal(ps, gp):
    res = (((ps / gp) - (ps / gp).rolling(21).mean()) / (ps / gp).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc011_21d_base_v011_signal'] = f61vr_f61_valuation_regime_calc011_21d_base_v011_signal

def f61vr_f61_valuation_regime_calc012_42d_base_v012_signal(evebitda, netinc):
    res = (netinc / evebitda).pct_change(5).rolling(42).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc012_42d_base_v012_signal'] = f61vr_f61_valuation_regime_calc012_42d_base_v012_signal

def f61vr_f61_valuation_regime_calc013_63d_base_v013_signal(pe, pb, ps):
    res = (pe + pb + ps).diff(1).rolling(63).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc013_63d_base_v013_signal'] = f61vr_f61_valuation_regime_calc013_63d_base_v013_signal

def f61vr_f61_valuation_regime_calc014_126d_base_v014_signal(ev, fcf):
    res = (ev / fcf).pct_change(10).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc014_126d_base_v014_signal'] = f61vr_f61_valuation_regime_calc014_126d_base_v014_signal

def f61vr_f61_valuation_regime_calc015_252d_base_v015_signal(marketcap, netinc):
    res = np.log((marketcap / netinc).abs().replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc015_252d_base_v015_signal'] = f61vr_f61_valuation_regime_calc015_252d_base_v015_signal

def f61vr_f61_valuation_regime_calc016_5d_base_v016_signal(pe, ps):
    res = (pe - ps).diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc016_5d_base_v016_signal'] = f61vr_f61_valuation_regime_calc016_5d_base_v016_signal

def f61vr_f61_valuation_regime_calc017_10d_base_v017_signal(pb, ps):
    res = (pb / ps).pct_change(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc017_10d_base_v017_signal'] = f61vr_f61_valuation_regime_calc017_10d_base_v017_signal

def f61vr_f61_valuation_regime_calc018_21d_base_v018_signal(evebitda, marketcap):
    res = (marketcap / evebitda).diff(5).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc018_21d_base_v018_signal'] = f61vr_f61_valuation_regime_calc018_21d_base_v018_signal

def f61vr_f61_valuation_regime_calc019_42d_base_v019_signal(ev, ps):
    res = np.log((ev / ps).abs().replace(0, np.nan)).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc019_42d_base_v019_signal'] = f61vr_f61_valuation_regime_calc019_42d_base_v019_signal

def f61vr_f61_valuation_regime_calc020_63d_base_v020_signal(pe, revenue):
    res = (revenue / pe).pct_change(10).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc020_63d_base_v020_signal'] = f61vr_f61_valuation_regime_calc020_63d_base_v020_signal

def f61vr_f61_valuation_regime_calc021_126d_base_v021_signal(pb, ebitda):
    res = (ebitda / pb).diff(21).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc021_126d_base_v021_signal'] = f61vr_f61_valuation_regime_calc021_126d_base_v021_signal

def f61vr_f61_valuation_regime_calc022_252d_base_v022_signal(ps, ev):
    res = (((ps * ev) - (ps * ev).rolling(252).mean()) / (ps * ev).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc022_252d_base_v022_signal'] = f61vr_f61_valuation_regime_calc022_252d_base_v022_signal

def f61vr_f61_valuation_regime_calc023_504d_base_v023_signal(evebitda, ps):
    res = (evebitda / ps).pct_change(63).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc023_504d_base_v023_signal'] = f61vr_f61_valuation_regime_calc023_504d_base_v023_signal

def f61vr_f61_valuation_regime_calc024_5d_base_v024_signal(pe, ps, pb):
    res = (pe / (ps + pb)).diff(1).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc024_5d_base_v024_signal'] = f61vr_f61_valuation_regime_calc024_5d_base_v024_signal

def f61vr_f61_valuation_regime_calc025_10d_base_v025_signal(ev, netinc, revenue):
    res = (ev * netinc / revenue).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc025_10d_base_v025_signal'] = f61vr_f61_valuation_regime_calc025_10d_base_v025_signal

def f61vr_f61_valuation_regime_calc026_21d_base_v026_signal(marketcap, ebitda, assets):
    res = (ebitda * assets / marketcap).pct_change(5).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc026_21d_base_v026_signal'] = f61vr_f61_valuation_regime_calc026_21d_base_v026_signal

def f61vr_f61_valuation_regime_calc027_42d_base_v027_signal(pe, pb, evebitda):
    res = np.log((pe * pb / evebitda).abs().replace(0, np.nan)).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc027_42d_base_v027_signal'] = f61vr_f61_valuation_regime_calc027_42d_base_v027_signal

def f61vr_f61_valuation_regime_calc028_63d_base_v028_signal(ps, ev, fcf):
    res = (fcf / (ps * ev)).diff(10).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc028_63d_base_v028_signal'] = f61vr_f61_valuation_regime_calc028_63d_base_v028_signal

def f61vr_f61_valuation_regime_calc029_126d_base_v029_signal(marketcap, ps, eps):
    res = (marketcap * eps / ps).pct_change(21).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc029_126d_base_v029_signal'] = f61vr_f61_valuation_regime_calc029_126d_base_v029_signal

def f61vr_f61_valuation_regime_calc030_252d_base_v030_signal(evebitda, ebitda, revenue):
    res = (revenue / (evebitda + ebitda)).rolling(252).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc030_252d_base_v030_signal'] = f61vr_f61_valuation_regime_calc030_252d_base_v030_signal

def f61vr_f61_valuation_regime_calc031_5d_base_v031_signal(pe, ps, marketcap):
    res = (marketcap / (pe * ps)).pct_change(1).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc031_5d_base_v031_signal'] = f61vr_f61_valuation_regime_calc031_5d_base_v031_signal

def f61vr_f61_valuation_regime_calc032_10d_base_v032_signal(ev, gp, assets):
    res = (ev * gp / assets).diff(2).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc032_10d_base_v032_signal'] = f61vr_f61_valuation_regime_calc032_10d_base_v032_signal

def f61vr_f61_valuation_regime_calc033_21d_base_v033_signal(pb, netinc, ebitda):
    res = np.log(((pb * netinc) / ebitda).abs().replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc033_21d_base_v033_signal'] = f61vr_f61_valuation_regime_calc033_21d_base_v033_signal

def f61vr_f61_valuation_regime_calc034_42d_base_v034_signal(ps, revenue, marketcap):
    res = (marketcap / (ps * revenue)).pct_change(5).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc034_42d_base_v034_signal'] = f61vr_f61_valuation_regime_calc034_42d_base_v034_signal

def f61vr_f61_valuation_regime_calc035_63d_base_v035_signal(evebitda, ebitda, assets):
    res = (((evebitda / ebitda) - (evebitda / ebitda).rolling(63).mean()) / (evebitda / ebitda).rolling(63).std()).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc035_63d_base_v035_signal'] = f61vr_f61_valuation_regime_calc035_63d_base_v035_signal

def f61vr_f61_valuation_regime_calc036_126d_base_v036_signal(ev, fcf, netinc):
    res = (ev / (fcf + netinc)).diff(10).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc036_126d_base_v036_signal'] = f61vr_f61_valuation_regime_calc036_126d_base_v036_signal

def f61vr_f61_valuation_regime_calc037_252d_base_v037_signal(pe, eps, assets):
    res = (pe * eps / assets).pct_change(21).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc037_252d_base_v037_signal'] = f61vr_f61_valuation_regime_calc037_252d_base_v037_signal

def f61vr_f61_valuation_regime_calc038_504d_base_v038_signal(pb, close, revenue):
    res = (revenue / (pb * close)).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc038_504d_base_v038_signal'] = f61vr_f61_valuation_regime_calc038_504d_base_v038_signal

def f61vr_f61_valuation_regime_calc039_5d_base_v039_signal(ps, gp, ebitda):
    res = (ps * gp / ebitda).diff(1).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc039_5d_base_v039_signal'] = f61vr_f61_valuation_regime_calc039_5d_base_v039_signal

def f61vr_f61_valuation_regime_calc040_10d_base_v040_signal(evebitda, netinc, fcf):
    res = np.log(((evebitda * netinc) / fcf).abs().replace(0, np.nan)).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc040_10d_base_v040_signal'] = f61vr_f61_valuation_regime_calc040_10d_base_v040_signal

def f61vr_f61_valuation_regime_calc041_21d_base_v041_signal(pe, ps, pb, ev):
    res = (pe + ps + pb / ev).pct_change(5).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc041_21d_base_v041_signal'] = f61vr_f61_valuation_regime_calc041_21d_base_v041_signal

def f61vr_f61_valuation_regime_calc042_42d_base_v042_signal(marketcap, revenue, eps):
    res = (marketcap / (revenue * eps)).diff(10).rolling(42).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc042_42d_base_v042_signal'] = f61vr_f61_valuation_regime_calc042_42d_base_v042_signal

def f61vr_f61_valuation_regime_calc043_63d_base_v043_signal(ev, ebitda, gp):
    res = (((ev / ebitda) - (ev / ebitda).rolling(63).mean()) / (ev / ebitda).rolling(63).std()).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc043_63d_base_v043_signal'] = f61vr_f61_valuation_regime_calc043_63d_base_v043_signal

def f61vr_f61_valuation_regime_calc044_126d_base_v044_signal(pe, pb, netinc):
    res = (pe / pb * netinc).pct_change(21).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc044_126d_base_v044_signal'] = f61vr_f61_valuation_regime_calc044_126d_base_v044_signal

def f61vr_f61_valuation_regime_calc045_252d_base_v045_signal(ps, evebitda, fcf):
    res = (ps * evebitda / fcf).diff(63).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc045_252d_base_v045_signal'] = f61vr_f61_valuation_regime_calc045_252d_base_v045_signal

def f61vr_f61_valuation_regime_calc046_5d_base_v046_signal(marketcap, revenue, assets):
    res = np.log((marketcap * revenue / assets).abs().replace(0, np.nan)).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc046_5d_base_v046_signal'] = f61vr_f61_valuation_regime_calc046_5d_base_v046_signal

def f61vr_f61_valuation_regime_calc047_10d_base_v047_signal(ev, ebitda, netinc):
    res = (ev / (ebitda + netinc)).pct_change(1).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc047_10d_base_v047_signal'] = f61vr_f61_valuation_regime_calc047_10d_base_v047_signal

def f61vr_f61_valuation_regime_calc048_21d_base_v048_signal(pe, pb, ps, revenue):
    res = (pe + pb + ps / revenue).diff(5).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc048_21d_base_v048_signal'] = f61vr_f61_valuation_regime_calc048_21d_base_v048_signal

def f61vr_f61_valuation_regime_calc049_42d_base_v049_signal(evebitda, ebitda, assets):
    res = (evebitda * assets / ebitda).pct_change(10).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc049_42d_base_v049_signal'] = f61vr_f61_valuation_regime_calc049_42d_base_v049_signal

def f61vr_f61_valuation_regime_calc050_63d_base_v050_signal(ev, gp, fcf):
    res = np.log((ev * gp / fcf).abs().replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc050_63d_base_v050_signal'] = f61vr_f61_valuation_regime_calc050_63d_base_v050_signal

def f61vr_f61_valuation_regime_calc051_126d_base_v051_signal(marketcap, ps, eps):
    res = (((marketcap / ps) - (marketcap / ps).rolling(126).mean()) / (marketcap / ps).rolling(126).std()).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc051_126d_base_v051_signal'] = f61vr_f61_valuation_regime_calc051_126d_base_v051_signal

def f61vr_f61_valuation_regime_calc052_252d_base_v052_signal(pe, pb, netinc, revenue):
    res = (pe * netinc / (pb * revenue)).pct_change(21).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc052_252d_base_v052_signal'] = f61vr_f61_valuation_regime_calc052_252d_base_v052_signal

def f61vr_f61_valuation_regime_calc053_504d_base_v053_signal(evebitda, ebitda, fcf, assets):
    res = (evebitda * fcf / (ebitda * assets)).diff(63).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc053_504d_base_v053_signal'] = f61vr_f61_valuation_regime_calc053_504d_base_v053_signal

def f61vr_f61_valuation_regime_calc054_5d_base_v054_signal(ev, gp, netinc):
    res = (ev / (gp + netinc)).pct_change(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc054_5d_base_v054_signal'] = f61vr_f61_valuation_regime_calc054_5d_base_v054_signal

def f61vr_f61_valuation_regime_calc055_10d_base_v055_signal(marketcap, revenue, eps, assets):
    res = np.log((marketcap * eps / (revenue * assets)).abs().replace(0, np.nan)).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc055_10d_base_v055_signal'] = f61vr_f61_valuation_regime_calc055_10d_base_v055_signal

def f61vr_f61_valuation_regime_calc056_21d_base_v056_signal(pe, ps, pb, ebitda):
    res = (pe * ps / (pb * ebitda)).diff(5).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc056_21d_base_v056_signal'] = f61vr_f61_valuation_regime_calc056_21d_base_v056_signal

def f61vr_f61_valuation_regime_calc057_42d_base_v057_signal(evebitda, ebitda, netinc, fcf):
    res = (evebitda / (ebitda + netinc + fcf)).pct_change(10).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc057_42d_base_v057_signal'] = f61vr_f61_valuation_regime_calc057_42d_base_v057_signal

def f61vr_f61_valuation_regime_calc058_63d_base_v058_signal(ev, gp, revenue, assets):
    res = (((ev * gp) / (revenue * assets)) - ((ev * gp) / (revenue * assets)).rolling(63).mean()) / ((ev * gp) / (revenue * assets)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc058_63d_base_v058_signal'] = f61vr_f61_valuation_regime_calc058_63d_base_v058_signal

def f61vr_f61_valuation_regime_calc059_126d_base_v059_signal(marketcap, ps, eps, netinc):
    res = (marketcap * ps / (eps * netinc)).diff(21).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc059_126d_base_v059_signal'] = f61vr_f61_valuation_regime_calc059_126d_base_v059_signal

def f61vr_f61_valuation_regime_calc060_252d_base_v060_signal(pe, pb, ps, evebitda):
    res = (pe + pb + ps + evebitda).pct_change(63).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc060_252d_base_v060_signal'] = f61vr_f61_valuation_regime_calc060_252d_base_v060_signal

def f61vr_f61_valuation_regime_calc061_5d_base_v061_signal(ev, ebitda, netinc, revenue):
    res = (ev * revenue / (ebitda * netinc)).diff(1).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc061_5d_base_v061_signal'] = f61vr_f61_valuation_regime_calc061_5d_base_v061_signal

def f61vr_f61_valuation_regime_calc062_10d_base_v062_signal(marketcap, ps, eps, fcf):
    res = np.log((marketcap * ps / (eps * fcf)).abs().replace(0, np.nan)).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc062_10d_base_v062_signal'] = f61vr_f61_valuation_regime_calc062_10d_base_v062_signal

def f61vr_f61_valuation_regime_calc063_21d_base_v063_signal(pe, pb, ps, evebitda, ev):
    res = (pe * pb / (ps * evebitda * ev)).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc063_21d_base_v063_signal'] = f61vr_f61_valuation_regime_calc063_21d_base_v063_signal

def f61vr_f61_valuation_regime_calc064_42d_base_v064_signal(marketcap, revenue, assets, gp):
    res = (marketcap * assets / (revenue * gp)).diff(10).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc064_42d_base_v064_signal'] = f61vr_f61_valuation_regime_calc064_42d_base_v064_signal

def f61vr_f61_valuation_regime_calc065_63d_base_v065_signal(ev, ebitda, netinc, fcf, ps):
    res = (ev * ps / (ebitda + netinc + fcf)).pct_change(21).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc065_63d_base_v065_signal'] = f61vr_f61_valuation_regime_calc065_63d_base_v065_signal

def f61vr_f61_valuation_regime_calc066_126d_base_v066_signal(pe, pb, marketcap, revenue, eps):
    res = (((pe * pb) / (marketcap / revenue * eps)) - ((pe * pb) / (marketcap / revenue * eps)).rolling(126).mean()) / ((pe * pb) / (marketcap / revenue * eps)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc066_126d_base_v066_signal'] = f61vr_f61_valuation_regime_calc066_126d_base_v066_signal

def f61vr_f61_valuation_regime_calc067_252d_base_v067_signal(ps, evebitda, ebitda, assets, gp):
    res = (ps * evebitda * gp / (ebitda * assets)).diff(63).rolling(252).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc067_252d_base_v067_signal'] = f61vr_f61_valuation_regime_calc067_252d_base_v067_signal

def f61vr_f61_valuation_regime_calc068_504d_base_v068_signal(ev, netinc, fcf, revenue, pe):
    res = np.log((ev * pe / (netinc + fcf + revenue)).abs().replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc068_504d_base_v068_signal'] = f61vr_f61_valuation_regime_calc068_504d_base_v068_signal

def f61vr_f61_valuation_regime_calc069_5d_base_v069_signal(marketcap, eps, assets, pb, ps):
    res = (marketcap * pb / (eps * assets * ps)).pct_change(1).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc069_5d_base_v069_signal'] = f61vr_f61_valuation_regime_calc069_5d_base_v069_signal

def f61vr_f61_valuation_regime_calc070_10d_base_v070_signal(pe, ps, evebitda, ebitda, gp):
    res = (pe * ps * gp / (evebitda * ebitda)).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc070_10d_base_v070_signal'] = f61vr_f61_valuation_regime_calc070_10d_base_v070_signal

def f61vr_f61_valuation_regime_calc071_21d_base_v071_signal(ev, netinc, fcf, revenue, assets):
    res = (ev * assets / (netinc + fcf + revenue)).pct_change(5).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc071_21d_base_v071_signal'] = f61vr_f61_valuation_regime_calc071_21d_base_v071_signal

def f61vr_f61_valuation_regime_calc072_42d_base_v072_signal(marketcap, eps, pb, ps, pe):
    res = np.log((marketcap * pe / (eps * pb * ps)).abs().replace(0, np.nan)).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc072_42d_base_v072_signal'] = f61vr_f61_valuation_regime_calc072_42d_base_v072_signal

def f61vr_f61_valuation_regime_calc073_63d_base_v073_signal(evebitda, ebitda, gp, revenue, assets):
    res = (evebitda * revenue / (ebitda * gp * assets)).diff(10).rolling(63).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc073_63d_base_v073_signal'] = f61vr_f61_valuation_regime_calc073_63d_base_v073_signal

def f61vr_f61_valuation_regime_calc074_126d_base_v074_signal(ev, netinc, fcf, ps, pb):
    res = (ev * ps / (netinc + fcf + pb)).pct_change(21).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc074_126d_base_v074_signal'] = f61vr_f61_valuation_regime_calc074_126d_base_v074_signal

def f61vr_f61_valuation_regime_calc075_252d_base_v075_signal(pe, ps, pb, evebitda, ev):
    res = (((pe * ps * pb) / (evebitda * ev)) - ((pe * ps * pb) / (evebitda * ev)).rolling(252).mean()) / ((pe * ps * pb) / (evebitda * ev)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc075_252d_base_v075_signal'] = f61vr_f61_valuation_regime_calc075_252d_base_v075_signal


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
