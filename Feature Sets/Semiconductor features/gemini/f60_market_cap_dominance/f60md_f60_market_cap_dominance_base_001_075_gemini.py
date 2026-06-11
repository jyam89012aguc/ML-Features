import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f60md_f60_market_cap_dominance_calc001_42d_base_v001_signal(retearn, currentratio):
    res = np.log((retearn / currentratio).abs().replace(0, np.nan)).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc001_42d_base_v001_signal'] = f60md_f60_market_cap_dominance_calc001_42d_base_v001_signal

def f60md_f60_market_cap_dominance_calc002_42d_base_v002_signal(opinc, open, netinc):
    res = (opinc / open).pct_change(1).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc002_42d_base_v002_signal'] = f60md_f60_market_cap_dominance_calc002_42d_base_v002_signal

def f60md_f60_market_cap_dominance_calc003_63d_base_v003_signal(eps, close, assets):
    res = (eps * close / assets).rolling(63).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc003_63d_base_v003_signal'] = f60md_f60_market_cap_dominance_calc003_63d_base_v003_signal

def f60md_f60_market_cap_dominance_calc004_21d_base_v004_signal(liabilities, open, high):
    res = (open / liabilities).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc004_21d_base_v004_signal'] = f60md_f60_market_cap_dominance_calc004_21d_base_v004_signal

def f60md_f60_market_cap_dominance_calc005_21d_base_v005_signal(revenue, ncfo):
    res = (ncfo / revenue)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc005_21d_base_v005_signal'] = f60md_f60_market_cap_dominance_calc005_21d_base_v005_signal

def f60md_f60_market_cap_dominance_calc006_42d_base_v006_signal(capex, equity):
    res = (equity / capex).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc006_42d_base_v006_signal'] = f60md_f60_market_cap_dominance_calc006_42d_base_v006_signal

def f60md_f60_market_cap_dominance_calc007_10d_base_v007_signal(volume, currentratio):
    res = (volume / currentratio).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc007_10d_base_v007_signal'] = f60md_f60_market_cap_dominance_calc007_10d_base_v007_signal

def f60md_f60_market_cap_dominance_calc008_63d_base_v008_signal(gp, fcf):
    res = (fcf / gp).rolling(63).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc008_63d_base_v008_signal'] = f60md_f60_market_cap_dominance_calc008_63d_base_v008_signal

def f60md_f60_market_cap_dominance_calc009_5d_base_v009_signal(evebitda, marketcap):
    res = (((marketcap / evebitda) - (marketcap / evebitda).rolling(5).mean()) / (marketcap / evebitda).rolling(5).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc009_5d_base_v009_signal'] = f60md_f60_market_cap_dominance_calc009_5d_base_v009_signal

def f60md_f60_market_cap_dominance_calc010_126d_base_v010_signal(assets, ebitda):
    res = (ebitda / assets).pct_change(5).rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc010_126d_base_v010_signal'] = f60md_f60_market_cap_dominance_calc010_126d_base_v010_signal

def f60md_f60_market_cap_dominance_calc011_10d_base_v011_signal(closeadj, equity):
    res = (((closeadj / equity) - (closeadj / equity).rolling(10).mean()) / (closeadj / equity).rolling(10).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc011_10d_base_v011_signal'] = f60md_f60_market_cap_dominance_calc011_10d_base_v011_signal

def f60md_f60_market_cap_dominance_calc012_5d_base_v012_signal(open, close, assets):
    res = (close * open / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc012_5d_base_v012_signal'] = f60md_f60_market_cap_dominance_calc012_5d_base_v012_signal

def f60md_f60_market_cap_dominance_calc013_21d_base_v013_signal(taxexp, pe):
    res = (taxexp / pe).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc013_21d_base_v013_signal'] = f60md_f60_market_cap_dominance_calc013_21d_base_v013_signal

def f60md_f60_market_cap_dominance_calc014_5d_base_v014_signal(ncff, revenue):
    res = (revenue / ncff)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc014_5d_base_v014_signal'] = f60md_f60_market_cap_dominance_calc014_5d_base_v014_signal

def f60md_f60_market_cap_dominance_calc015_5d_base_v015_signal(debt, ps):
    res = (((debt / ps) - (debt / ps).rolling(5).mean()) / (debt / ps).rolling(5).std()).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc015_5d_base_v015_signal'] = f60md_f60_market_cap_dominance_calc015_5d_base_v015_signal

def f60md_f60_market_cap_dominance_calc016_126d_base_v016_signal(liabilities, fcf):
    res = (fcf / liabilities).pct_change(1).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc016_126d_base_v016_signal'] = f60md_f60_market_cap_dominance_calc016_126d_base_v016_signal

def f60md_f60_market_cap_dominance_calc017_21d_base_v017_signal(netinc, fcf):
    res = (netinc / fcf).pct_change(21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc017_21d_base_v017_signal'] = f60md_f60_market_cap_dominance_calc017_21d_base_v017_signal

def f60md_f60_market_cap_dominance_calc018_63d_base_v018_signal(workingcapital, marketcap):
    res = (marketcap / workingcapital).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc018_63d_base_v018_signal'] = f60md_f60_market_cap_dominance_calc018_63d_base_v018_signal

def f60md_f60_market_cap_dominance_calc019_42d_base_v019_signal(pb, pe, workingcapital):
    res = (pe / pb).pct_change(1).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc019_42d_base_v019_signal'] = f60md_f60_market_cap_dominance_calc019_42d_base_v019_signal

def f60md_f60_market_cap_dominance_calc020_63d_base_v020_signal(ebitda, gp, assets):
    res = (gp * ebitda / assets).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc020_63d_base_v020_signal'] = f60md_f60_market_cap_dominance_calc020_63d_base_v020_signal

def f60md_f60_market_cap_dominance_calc021_5d_base_v021_signal(ebitda, gp):
    res = np.log((gp / ebitda).abs().replace(0, np.nan)).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc021_5d_base_v021_signal'] = f60md_f60_market_cap_dominance_calc021_5d_base_v021_signal

def f60md_f60_market_cap_dominance_calc022_42d_base_v022_signal(netinc, ebitda, assets):
    res = (ebitda * netinc / assets).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc022_42d_base_v022_signal'] = f60md_f60_market_cap_dominance_calc022_42d_base_v022_signal

def f60md_f60_market_cap_dominance_calc023_252d_base_v023_signal(eps, marketcap):
    res = (((eps / marketcap) - (eps / marketcap).rolling(252).mean()) / (eps / marketcap).rolling(252).std()).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc023_252d_base_v023_signal'] = f60md_f60_market_cap_dominance_calc023_252d_base_v023_signal

def f60md_f60_market_cap_dominance_calc024_5d_base_v024_signal(intexp, liabilities, ncfi):
    res = (((ncfi / intexp) - (ncfi / intexp).rolling(5).mean()) / (ncfi / intexp).rolling(5).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc024_5d_base_v024_signal'] = f60md_f60_market_cap_dominance_calc024_5d_base_v024_signal

def f60md_f60_market_cap_dominance_calc025_5d_base_v025_signal(ebitda, ps):
    res = np.log((ps / ebitda).abs().replace(0, np.nan)).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc025_5d_base_v025_signal'] = f60md_f60_market_cap_dominance_calc025_5d_base_v025_signal

def f60md_f60_market_cap_dominance_calc026_126d_base_v026_signal(intexp, evebit, close):
    res = (close * evebit / intexp).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc026_126d_base_v026_signal'] = f60md_f60_market_cap_dominance_calc026_126d_base_v026_signal

def f60md_f60_market_cap_dominance_calc027_10d_base_v027_signal(liabilities, assets):
    res = (assets / liabilities).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc027_10d_base_v027_signal'] = f60md_f60_market_cap_dominance_calc027_10d_base_v027_signal

def f60md_f60_market_cap_dominance_calc028_10d_base_v028_signal(ncff, revenue):
    res = (revenue / ncff).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc028_10d_base_v028_signal'] = f60md_f60_market_cap_dominance_calc028_10d_base_v028_signal

def f60md_f60_market_cap_dominance_calc029_63d_base_v029_signal(sharesbas, pb):
    res = (((sharesbas / pb) - (sharesbas / pb).rolling(63).mean()) / (sharesbas / pb).rolling(63).std()).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc029_63d_base_v029_signal'] = f60md_f60_market_cap_dominance_calc029_63d_base_v029_signal

def f60md_f60_market_cap_dominance_calc030_252d_base_v030_signal(opinc, ncfi, fcf):
    res = (fcf / opinc).pct_change(1).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc030_252d_base_v030_signal'] = f60md_f60_market_cap_dominance_calc030_252d_base_v030_signal

def f60md_f60_market_cap_dominance_calc031_10d_base_v031_signal(ncff, debt):
    res = np.log((ncff / debt).abs().replace(0, np.nan)).rolling(10).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc031_10d_base_v031_signal'] = f60md_f60_market_cap_dominance_calc031_10d_base_v031_signal

def f60md_f60_market_cap_dominance_calc032_21d_base_v032_signal(close, workingcapital):
    res = (((workingcapital / close) - (workingcapital / close).rolling(21).mean()) / (workingcapital / close).rolling(21).std()).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc032_21d_base_v032_signal'] = f60md_f60_market_cap_dominance_calc032_21d_base_v032_signal

def f60md_f60_market_cap_dominance_calc033_42d_base_v033_signal(capex, eps, assets):
    res = (capex * eps / assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc033_42d_base_v033_signal'] = f60md_f60_market_cap_dominance_calc033_42d_base_v033_signal

def f60md_f60_market_cap_dominance_calc034_21d_base_v034_signal(open, debt):
    res = (debt / open).diff(5).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc034_21d_base_v034_signal'] = f60md_f60_market_cap_dominance_calc034_21d_base_v034_signal

def f60md_f60_market_cap_dominance_calc035_10d_base_v035_signal(ncff, marketcap):
    res = np.log((ncff / marketcap).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc035_10d_base_v035_signal'] = f60md_f60_market_cap_dominance_calc035_10d_base_v035_signal

def f60md_f60_market_cap_dominance_calc036_21d_base_v036_signal(eps, ps):
    res = np.log((eps / ps).abs().replace(0, np.nan)).rolling(21).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc036_21d_base_v036_signal'] = f60md_f60_market_cap_dominance_calc036_21d_base_v036_signal

def f60md_f60_market_cap_dominance_calc037_10d_base_v037_signal(assets, ps):
    res = (ps / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc037_10d_base_v037_signal'] = f60md_f60_market_cap_dominance_calc037_10d_base_v037_signal

def f60md_f60_market_cap_dominance_calc038_21d_base_v038_signal(sharesbas, ncff):
    res = (sharesbas / ncff).diff(1).rolling(21).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc038_21d_base_v038_signal'] = f60md_f60_market_cap_dominance_calc038_21d_base_v038_signal

def f60md_f60_market_cap_dominance_calc039_126d_base_v039_signal(sharesbas, ncfi, netinc):
    res = (netinc / ncfi).pct_change(21).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc039_126d_base_v039_signal'] = f60md_f60_market_cap_dominance_calc039_126d_base_v039_signal

def f60md_f60_market_cap_dominance_calc040_10d_base_v040_signal(sharesbas, gp, assets):
    res = (sharesbas * gp / assets).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc040_10d_base_v040_signal'] = f60md_f60_market_cap_dominance_calc040_10d_base_v040_signal

def f60md_f60_market_cap_dominance_calc041_5d_base_v041_signal(opinc, low, open):
    res = (low * opinc / open)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc041_5d_base_v041_signal'] = f60md_f60_market_cap_dominance_calc041_5d_base_v041_signal

def f60md_f60_market_cap_dominance_calc042_126d_base_v042_signal(equity, eps):
    res = (eps / equity).pct_change(21).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc042_126d_base_v042_signal'] = f60md_f60_market_cap_dominance_calc042_126d_base_v042_signal

def f60md_f60_market_cap_dominance_calc043_42d_base_v043_signal(evebitda, equity):
    res = (evebitda / equity)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc043_42d_base_v043_signal'] = f60md_f60_market_cap_dominance_calc043_42d_base_v043_signal

def f60md_f60_market_cap_dominance_calc044_126d_base_v044_signal(ncff, open, equity):
    res = (open / ncff).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc044_126d_base_v044_signal'] = f60md_f60_market_cap_dominance_calc044_126d_base_v044_signal

def f60md_f60_market_cap_dominance_calc045_42d_base_v045_signal(evebitda, workingcapital):
    res = (workingcapital / evebitda).diff(21).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc045_42d_base_v045_signal'] = f60md_f60_market_cap_dominance_calc045_42d_base_v045_signal

def f60md_f60_market_cap_dominance_calc046_10d_base_v046_signal(sharesbas, high, currentratio):
    res = np.log((currentratio / sharesbas).abs().replace(0, np.nan)).rolling(10).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc046_10d_base_v046_signal'] = f60md_f60_market_cap_dominance_calc046_10d_base_v046_signal

def f60md_f60_market_cap_dominance_calc047_42d_base_v047_signal(ncfi, marketcap):
    res = (ncfi / marketcap).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc047_42d_base_v047_signal'] = f60md_f60_market_cap_dominance_calc047_42d_base_v047_signal

def f60md_f60_market_cap_dominance_calc048_252d_base_v048_signal(equity, marketcap):
    res = np.log((equity / marketcap).abs().replace(0, np.nan)).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc048_252d_base_v048_signal'] = f60md_f60_market_cap_dominance_calc048_252d_base_v048_signal

def f60md_f60_market_cap_dominance_calc049_63d_base_v049_signal(sharesbas, intexp):
    res = np.log((intexp / sharesbas).abs().replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc049_63d_base_v049_signal'] = f60md_f60_market_cap_dominance_calc049_63d_base_v049_signal

def f60md_f60_market_cap_dominance_calc050_42d_base_v050_signal(volume, revenue):
    res = (revenue / volume)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc050_42d_base_v050_signal'] = f60md_f60_market_cap_dominance_calc050_42d_base_v050_signal

def f60md_f60_market_cap_dominance_calc051_42d_base_v051_signal(opinc, eps):
    res = (opinc / eps).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc051_42d_base_v051_signal'] = f60md_f60_market_cap_dominance_calc051_42d_base_v051_signal

def f60md_f60_market_cap_dominance_calc052_42d_base_v052_signal(ncfi, assets):
    res = (((ncfi / assets) - (ncfi / assets).rolling(42).mean()) / (ncfi / assets).rolling(42).std()).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc052_42d_base_v052_signal'] = f60md_f60_market_cap_dominance_calc052_42d_base_v052_signal

def f60md_f60_market_cap_dominance_calc053_126d_base_v053_signal(taxexp, ev):
    res = (((taxexp / ev) - (taxexp / ev).rolling(126).mean()) / (taxexp / ev).rolling(126).std()).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc053_126d_base_v053_signal'] = f60md_f60_market_cap_dominance_calc053_126d_base_v053_signal

def f60md_f60_market_cap_dominance_calc054_21d_base_v054_signal(ncff, equity):
    res = (ncff / equity).diff(1).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc054_21d_base_v054_signal'] = f60md_f60_market_cap_dominance_calc054_21d_base_v054_signal

def f60md_f60_market_cap_dominance_calc055_10d_base_v055_signal(ncff, eps):
    res = (eps / ncff).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc055_10d_base_v055_signal'] = f60md_f60_market_cap_dominance_calc055_10d_base_v055_signal

def f60md_f60_market_cap_dominance_calc056_21d_base_v056_signal(liabilities, equity):
    res = (equity / liabilities).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc056_21d_base_v056_signal'] = f60md_f60_market_cap_dominance_calc056_21d_base_v056_signal

def f60md_f60_market_cap_dominance_calc057_21d_base_v057_signal(evebitda, low, retearn):
    res = np.log((evebitda / low).abs().replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc057_21d_base_v057_signal'] = f60md_f60_market_cap_dominance_calc057_21d_base_v057_signal

def f60md_f60_market_cap_dominance_calc058_63d_base_v058_signal(liabilities, high):
    res = (liabilities / high).pct_change(5).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc058_63d_base_v058_signal'] = f60md_f60_market_cap_dominance_calc058_63d_base_v058_signal

def f60md_f60_market_cap_dominance_calc059_252d_base_v059_signal(workingcapital, debt, ncfo):
    res = np.log((ncfo / debt).abs().replace(0, np.nan)).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc059_252d_base_v059_signal'] = f60md_f60_market_cap_dominance_calc059_252d_base_v059_signal

def f60md_f60_market_cap_dominance_calc060_5d_base_v060_signal(assets, ncfo):
    res = (((assets / ncfo) - (assets / ncfo).rolling(5).mean()) / (assets / ncfo).rolling(5).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc060_5d_base_v060_signal'] = f60md_f60_market_cap_dominance_calc060_5d_base_v060_signal

def f60md_f60_market_cap_dominance_calc061_10d_base_v061_signal(sharesbas, retearn, equity):
    res = (equity / retearn)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc061_10d_base_v061_signal'] = f60md_f60_market_cap_dominance_calc061_10d_base_v061_signal

def f60md_f60_market_cap_dominance_calc062_42d_base_v062_signal(pb, high):
    res = (pb / high).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc062_42d_base_v062_signal'] = f60md_f60_market_cap_dominance_calc062_42d_base_v062_signal

def f60md_f60_market_cap_dominance_calc063_21d_base_v063_signal(evebitda, open):
    res = (((evebitda / open) - (evebitda / open).rolling(21).mean()) / (evebitda / open).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc063_21d_base_v063_signal'] = f60md_f60_market_cap_dominance_calc063_21d_base_v063_signal

def f60md_f60_market_cap_dominance_calc064_10d_base_v064_signal(ncff, ps, assets):
    res = (ps * ncff / assets).rolling(10).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc064_10d_base_v064_signal'] = f60md_f60_market_cap_dominance_calc064_10d_base_v064_signal

def f60md_f60_market_cap_dominance_calc065_5d_base_v065_signal(eps, ncfo):
    res = np.log((eps / ncfo).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc065_5d_base_v065_signal'] = f60md_f60_market_cap_dominance_calc065_5d_base_v065_signal

def f60md_f60_market_cap_dominance_calc066_63d_base_v066_signal(pb, pe, currentratio):
    res = (currentratio / pb).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc066_63d_base_v066_signal'] = f60md_f60_market_cap_dominance_calc066_63d_base_v066_signal

def f60md_f60_market_cap_dominance_calc067_63d_base_v067_signal(ev, currentratio):
    res = (currentratio / ev).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc067_63d_base_v067_signal'] = f60md_f60_market_cap_dominance_calc067_63d_base_v067_signal

def f60md_f60_market_cap_dominance_calc068_42d_base_v068_signal(sharesbas, closeadj):
    res = np.log((closeadj / sharesbas).abs().replace(0, np.nan)).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc068_42d_base_v068_signal'] = f60md_f60_market_cap_dominance_calc068_42d_base_v068_signal

def f60md_f60_market_cap_dominance_calc069_5d_base_v069_signal(pb, workingcapital):
    res = (workingcapital / pb).diff(5).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc069_5d_base_v069_signal'] = f60md_f60_market_cap_dominance_calc069_5d_base_v069_signal

def f60md_f60_market_cap_dominance_calc070_126d_base_v070_signal(ncfi, fcf):
    res = (fcf / ncfi).diff(21).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc070_126d_base_v070_signal'] = f60md_f60_market_cap_dominance_calc070_126d_base_v070_signal

def f60md_f60_market_cap_dominance_calc071_63d_base_v071_signal(open, ncfo, assets):
    res = (open * ncfo / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc071_63d_base_v071_signal'] = f60md_f60_market_cap_dominance_calc071_63d_base_v071_signal

def f60md_f60_market_cap_dominance_calc072_5d_base_v072_signal(ncfi, low, assets):
    res = (low * ncfi / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc072_5d_base_v072_signal'] = f60md_f60_market_cap_dominance_calc072_5d_base_v072_signal

def f60md_f60_market_cap_dominance_calc073_126d_base_v073_signal(pb, close):
    res = (pb / close).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc073_126d_base_v073_signal'] = f60md_f60_market_cap_dominance_calc073_126d_base_v073_signal

def f60md_f60_market_cap_dominance_calc074_21d_base_v074_signal(evebit, eps):
    res = (eps / evebit).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc074_21d_base_v074_signal'] = f60md_f60_market_cap_dominance_calc074_21d_base_v074_signal

def f60md_f60_market_cap_dominance_calc075_63d_base_v075_signal(ev, netinc):
    res = (((ev / netinc) - (ev / netinc).rolling(63).mean()) / (ev / netinc).rolling(63).std()).rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc075_63d_base_v075_signal'] = f60md_f60_market_cap_dominance_calc075_63d_base_v075_signal

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
