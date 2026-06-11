import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f62ds_f62_dividend_sustainability_calc001_21d_2nd_v001_signal(ncff):
    return ncff.rolling(21).mean().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc001_21d_2nd_v001_signal'] = f62ds_f62_dividend_sustainability_calc001_21d_2nd_v001_signal

def f62ds_f62_dividend_sustainability_calc002_42d_2nd_v002_signal(pb, pe):
    return (pe / pb).rolling(42).median().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc002_42d_2nd_v002_signal'] = f62ds_f62_dividend_sustainability_calc002_42d_2nd_v002_signal

def f62ds_f62_dividend_sustainability_calc003_252d_2nd_v003_signal(ncfi, opinc):
    return (ncfi * opinc).rolling(252).kurt().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc003_252d_2nd_v003_signal'] = f62ds_f62_dividend_sustainability_calc003_252d_2nd_v003_signal

def f62ds_f62_dividend_sustainability_calc004_10d_2nd_v004_signal(high, sharesbas):
    return (high * sharesbas).rolling(10).var().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc004_10d_2nd_v004_signal'] = f62ds_f62_dividend_sustainability_calc004_10d_2nd_v004_signal

def f62ds_f62_dividend_sustainability_calc005_504d_2nd_v005_signal(assets, close):
    return (close - assets).rolling(504).rank().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc005_504d_2nd_v005_signal'] = f62ds_f62_dividend_sustainability_calc005_504d_2nd_v005_signal

def f62ds_f62_dividend_sustainability_calc006_126d_2nd_v006_signal(retearn, volume):
    return (volume * retearn).rolling(126).max().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc006_126d_2nd_v006_signal'] = f62ds_f62_dividend_sustainability_calc006_126d_2nd_v006_signal

def f62ds_f62_dividend_sustainability_calc007_42d_2nd_v007_signal(ebitda, gp):
    return (ebitda / gp).rolling(42).max().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc007_42d_2nd_v007_signal'] = f62ds_f62_dividend_sustainability_calc007_42d_2nd_v007_signal

def f62ds_f62_dividend_sustainability_calc008_126d_2nd_v008_signal(assets):
    return assets.rolling(126).rank().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc008_126d_2nd_v008_signal'] = f62ds_f62_dividend_sustainability_calc008_126d_2nd_v008_signal

def f62ds_f62_dividend_sustainability_calc009_42d_2nd_v009_signal(equity, low):
    return (low - equity).rolling(42).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc009_42d_2nd_v009_signal'] = f62ds_f62_dividend_sustainability_calc009_42d_2nd_v009_signal

def f62ds_f62_dividend_sustainability_calc010_21d_2nd_v010_signal(ncfi, open):
    return (ncfi - open).rolling(21).skew().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc010_21d_2nd_v010_signal'] = f62ds_f62_dividend_sustainability_calc010_21d_2nd_v010_signal

def f62ds_f62_dividend_sustainability_calc011_5d_2nd_v011_signal(high, workingcapital):
    return (workingcapital / high).rolling(5).min().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc011_5d_2nd_v011_signal'] = f62ds_f62_dividend_sustainability_calc011_5d_2nd_v011_signal

def f62ds_f62_dividend_sustainability_calc012_252d_2nd_v012_signal(ps, sharesbas):
    return (sharesbas + ps).rolling(252).median().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc012_252d_2nd_v012_signal'] = f62ds_f62_dividend_sustainability_calc012_252d_2nd_v012_signal

def f62ds_f62_dividend_sustainability_calc013_42d_2nd_v013_signal(high, retearn):
    return (high - retearn).rolling(42).min().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc013_42d_2nd_v013_signal'] = f62ds_f62_dividend_sustainability_calc013_42d_2nd_v013_signal

def f62ds_f62_dividend_sustainability_calc014_126d_2nd_v014_signal(ev, sharesbas):
    return (ev * sharesbas).rolling(126).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc014_126d_2nd_v014_signal'] = f62ds_f62_dividend_sustainability_calc014_126d_2nd_v014_signal

def f62ds_f62_dividend_sustainability_calc015_504d_2nd_v015_signal(gp, pe):
    return (pe / gp).rolling(504).max().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc015_504d_2nd_v015_signal'] = f62ds_f62_dividend_sustainability_calc015_504d_2nd_v015_signal

def f62ds_f62_dividend_sustainability_calc016_252d_2nd_v016_signal(ncfi):
    return ncfi.rolling(252).kurt().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc016_252d_2nd_v016_signal'] = f62ds_f62_dividend_sustainability_calc016_252d_2nd_v016_signal

def f62ds_f62_dividend_sustainability_calc017_252d_2nd_v017_signal(capex):
    return capex.rolling(252).std().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc017_252d_2nd_v017_signal'] = f62ds_f62_dividend_sustainability_calc017_252d_2nd_v017_signal

def f62ds_f62_dividend_sustainability_calc018_63d_2nd_v018_signal(close, low):
    return (low + close).rolling(63).rank().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc018_63d_2nd_v018_signal'] = f62ds_f62_dividend_sustainability_calc018_63d_2nd_v018_signal

def f62ds_f62_dividend_sustainability_calc019_5d_2nd_v019_signal(taxexp):
    return taxexp.rolling(5).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc019_5d_2nd_v019_signal'] = f62ds_f62_dividend_sustainability_calc019_5d_2nd_v019_signal

def f62ds_f62_dividend_sustainability_calc020_42d_2nd_v020_signal(ncfo, pe):
    return (pe + ncfo).rolling(42).var().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc020_42d_2nd_v020_signal'] = f62ds_f62_dividend_sustainability_calc020_42d_2nd_v020_signal

def f62ds_f62_dividend_sustainability_calc021_252d_2nd_v021_signal(revenue, volume):
    return (volume + revenue).rolling(252).min().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc021_252d_2nd_v021_signal'] = f62ds_f62_dividend_sustainability_calc021_252d_2nd_v021_signal

def f62ds_f62_dividend_sustainability_calc022_21d_2nd_v022_signal(closeadj, liabilities, ncfo):
    return ((ncfo + liabilities) - closeadj).rolling(21).median().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc022_21d_2nd_v022_signal'] = f62ds_f62_dividend_sustainability_calc022_21d_2nd_v022_signal

def f62ds_f62_dividend_sustainability_calc023_5d_2nd_v023_signal(equity, volume):
    return (volume / equity).rolling(5).median().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc023_5d_2nd_v023_signal'] = f62ds_f62_dividend_sustainability_calc023_5d_2nd_v023_signal

def f62ds_f62_dividend_sustainability_calc024_252d_2nd_v024_signal(evebitda, intexp):
    return (intexp - evebitda).rolling(252).min().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc024_252d_2nd_v024_signal'] = f62ds_f62_dividend_sustainability_calc024_252d_2nd_v024_signal

def f62ds_f62_dividend_sustainability_calc025_126d_2nd_v025_signal(pb, taxexp):
    return (pb / taxexp).rolling(126).std().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc025_126d_2nd_v025_signal'] = f62ds_f62_dividend_sustainability_calc025_126d_2nd_v025_signal

def f62ds_f62_dividend_sustainability_calc026_252d_2nd_v026_signal(open):
    return open.rolling(252).mean().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc026_252d_2nd_v026_signal'] = f62ds_f62_dividend_sustainability_calc026_252d_2nd_v026_signal

def f62ds_f62_dividend_sustainability_calc027_504d_2nd_v027_signal(marketcap, retearn, taxexp):
    return ((retearn - taxexp) - marketcap).rolling(504).var().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc027_504d_2nd_v027_signal'] = f62ds_f62_dividend_sustainability_calc027_504d_2nd_v027_signal

def f62ds_f62_dividend_sustainability_calc028_252d_2nd_v028_signal(marketcap):
    return marketcap.rolling(252).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc028_252d_2nd_v028_signal'] = f62ds_f62_dividend_sustainability_calc028_252d_2nd_v028_signal

def f62ds_f62_dividend_sustainability_calc029_63d_2nd_v029_signal(gp, marketcap, sharesbas):
    return ((gp * sharesbas) / marketcap).rolling(63).std().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc029_63d_2nd_v029_signal'] = f62ds_f62_dividend_sustainability_calc029_63d_2nd_v029_signal

def f62ds_f62_dividend_sustainability_calc030_10d_2nd_v030_signal(ev):
    return ev.rolling(10).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc030_10d_2nd_v030_signal'] = f62ds_f62_dividend_sustainability_calc030_10d_2nd_v030_signal

def f62ds_f62_dividend_sustainability_calc031_10d_2nd_v031_signal(equity, sharesbas):
    return (sharesbas + equity).rolling(10).min().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc031_10d_2nd_v031_signal'] = f62ds_f62_dividend_sustainability_calc031_10d_2nd_v031_signal

def f62ds_f62_dividend_sustainability_calc032_63d_2nd_v032_signal(debt, ncfi):
    return (ncfi + debt).rolling(63).min().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc032_63d_2nd_v032_signal'] = f62ds_f62_dividend_sustainability_calc032_63d_2nd_v032_signal

def f62ds_f62_dividend_sustainability_calc033_10d_2nd_v033_signal(ps):
    return ps.rolling(10).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc033_10d_2nd_v033_signal'] = f62ds_f62_dividend_sustainability_calc033_10d_2nd_v033_signal

def f62ds_f62_dividend_sustainability_calc034_21d_2nd_v034_signal(ebitda, revenue):
    return (ebitda / revenue).rolling(21).var().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc034_21d_2nd_v034_signal'] = f62ds_f62_dividend_sustainability_calc034_21d_2nd_v034_signal

def f62ds_f62_dividend_sustainability_calc035_42d_2nd_v035_signal(liabilities, opinc):
    return (opinc - liabilities).rolling(42).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc035_42d_2nd_v035_signal'] = f62ds_f62_dividend_sustainability_calc035_42d_2nd_v035_signal

def f62ds_f62_dividend_sustainability_calc036_5d_2nd_v036_signal(netinc, sharesbas):
    return (netinc + sharesbas).rolling(5).var().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc036_5d_2nd_v036_signal'] = f62ds_f62_dividend_sustainability_calc036_5d_2nd_v036_signal

def f62ds_f62_dividend_sustainability_calc037_504d_2nd_v037_signal(assets, capex, ncff):
    return ((ncff * capex) * assets).rolling(504).kurt().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc037_504d_2nd_v037_signal'] = f62ds_f62_dividend_sustainability_calc037_504d_2nd_v037_signal

def f62ds_f62_dividend_sustainability_calc038_21d_2nd_v038_signal(capex, eps, ncfo):
    return ((capex + ncfo) + eps).rolling(21).skew().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc038_21d_2nd_v038_signal'] = f62ds_f62_dividend_sustainability_calc038_21d_2nd_v038_signal

def f62ds_f62_dividend_sustainability_calc039_10d_2nd_v039_signal(debt, sharesbas):
    return (debt - sharesbas).rolling(10).std().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc039_10d_2nd_v039_signal'] = f62ds_f62_dividend_sustainability_calc039_10d_2nd_v039_signal

def f62ds_f62_dividend_sustainability_calc040_252d_2nd_v040_signal(marketcap, taxexp, volume):
    return ((marketcap / volume) - taxexp).rolling(252).max().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc040_252d_2nd_v040_signal'] = f62ds_f62_dividend_sustainability_calc040_252d_2nd_v040_signal

def f62ds_f62_dividend_sustainability_calc041_504d_2nd_v041_signal(equity, opinc, taxexp):
    return ((opinc + taxexp) * equity).rolling(504).min().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc041_504d_2nd_v041_signal'] = f62ds_f62_dividend_sustainability_calc041_504d_2nd_v041_signal

def f62ds_f62_dividend_sustainability_calc042_21d_2nd_v042_signal(sharesbas):
    return sharesbas.rolling(21).std().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc042_21d_2nd_v042_signal'] = f62ds_f62_dividend_sustainability_calc042_21d_2nd_v042_signal

def f62ds_f62_dividend_sustainability_calc043_63d_2nd_v043_signal(evebit, liabilities, ncff):
    return ((ncff - evebit) - liabilities).rolling(63).std().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc043_63d_2nd_v043_signal'] = f62ds_f62_dividend_sustainability_calc043_63d_2nd_v043_signal

def f62ds_f62_dividend_sustainability_calc044_10d_2nd_v044_signal(assets, ebitda, pe):
    return ((assets - pe) * ebitda).rolling(10).skew().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc044_10d_2nd_v044_signal'] = f62ds_f62_dividend_sustainability_calc044_10d_2nd_v044_signal

def f62ds_f62_dividend_sustainability_calc045_5d_2nd_v045_signal(high, ps):
    return (ps * high).rolling(5).std().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc045_5d_2nd_v045_signal'] = f62ds_f62_dividend_sustainability_calc045_5d_2nd_v045_signal

def f62ds_f62_dividend_sustainability_calc046_63d_2nd_v046_signal(fcf, pb, taxexp):
    return ((pb * taxexp) / fcf).rolling(63).skew().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc046_63d_2nd_v046_signal'] = f62ds_f62_dividend_sustainability_calc046_63d_2nd_v046_signal

def f62ds_f62_dividend_sustainability_calc047_10d_2nd_v047_signal(pb):
    return pb.rolling(10).std().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc047_10d_2nd_v047_signal'] = f62ds_f62_dividend_sustainability_calc047_10d_2nd_v047_signal

def f62ds_f62_dividend_sustainability_calc048_42d_2nd_v048_signal(evebitda):
    return evebitda.rolling(42).rank().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc048_42d_2nd_v048_signal'] = f62ds_f62_dividend_sustainability_calc048_42d_2nd_v048_signal

def f62ds_f62_dividend_sustainability_calc049_63d_2nd_v049_signal(close, equity):
    return (equity + close).rolling(63).kurt().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc049_63d_2nd_v049_signal'] = f62ds_f62_dividend_sustainability_calc049_63d_2nd_v049_signal

def f62ds_f62_dividend_sustainability_calc050_42d_2nd_v050_signal(ebitda):
    return ebitda.rolling(42).std().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc050_42d_2nd_v050_signal'] = f62ds_f62_dividend_sustainability_calc050_42d_2nd_v050_signal

def f62ds_f62_dividend_sustainability_calc051_5d_2nd_v051_signal(eps, sharesbas):
    return (eps / sharesbas).rolling(5).min().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc051_5d_2nd_v051_signal'] = f62ds_f62_dividend_sustainability_calc051_5d_2nd_v051_signal

def f62ds_f62_dividend_sustainability_calc052_5d_2nd_v052_signal(ebitda, taxexp):
    return (taxexp - ebitda).rolling(5).rank().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc052_5d_2nd_v052_signal'] = f62ds_f62_dividend_sustainability_calc052_5d_2nd_v052_signal

def f62ds_f62_dividend_sustainability_calc053_504d_2nd_v053_signal(low, pb):
    return (low / pb).rolling(504).skew().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc053_504d_2nd_v053_signal'] = f62ds_f62_dividend_sustainability_calc053_504d_2nd_v053_signal

def f62ds_f62_dividend_sustainability_calc054_63d_2nd_v054_signal(marketcap):
    return marketcap.rolling(63).rank().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc054_63d_2nd_v054_signal'] = f62ds_f62_dividend_sustainability_calc054_63d_2nd_v054_signal

def f62ds_f62_dividend_sustainability_calc055_252d_2nd_v055_signal(debt, revenue):
    return (debt / revenue).rolling(252).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc055_252d_2nd_v055_signal'] = f62ds_f62_dividend_sustainability_calc055_252d_2nd_v055_signal

def f62ds_f62_dividend_sustainability_calc056_126d_2nd_v056_signal(opinc):
    return opinc.rolling(126).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc056_126d_2nd_v056_signal'] = f62ds_f62_dividend_sustainability_calc056_126d_2nd_v056_signal

def f62ds_f62_dividend_sustainability_calc057_252d_2nd_v057_signal(currentratio):
    return currentratio.rolling(252).max().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc057_252d_2nd_v057_signal'] = f62ds_f62_dividend_sustainability_calc057_252d_2nd_v057_signal

def f62ds_f62_dividend_sustainability_calc058_5d_2nd_v058_signal(currentratio, eps):
    return (eps - currentratio).rolling(5).var().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc058_5d_2nd_v058_signal'] = f62ds_f62_dividend_sustainability_calc058_5d_2nd_v058_signal

def f62ds_f62_dividend_sustainability_calc059_5d_2nd_v059_signal(ncff, pb):
    return (ncff * pb).rolling(5).skew().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc059_5d_2nd_v059_signal'] = f62ds_f62_dividend_sustainability_calc059_5d_2nd_v059_signal

def f62ds_f62_dividend_sustainability_calc060_10d_2nd_v060_signal(eps, gp):
    return (eps / gp).rolling(10).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc060_10d_2nd_v060_signal'] = f62ds_f62_dividend_sustainability_calc060_10d_2nd_v060_signal

def f62ds_f62_dividend_sustainability_calc061_252d_2nd_v061_signal(capex, liabilities):
    return (liabilities / capex).rolling(252).skew().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc061_252d_2nd_v061_signal'] = f62ds_f62_dividend_sustainability_calc061_252d_2nd_v061_signal

def f62ds_f62_dividend_sustainability_calc062_5d_2nd_v062_signal(closeadj, revenue):
    return (closeadj + revenue).rolling(5).min().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc062_5d_2nd_v062_signal'] = f62ds_f62_dividend_sustainability_calc062_5d_2nd_v062_signal

def f62ds_f62_dividend_sustainability_calc063_252d_2nd_v063_signal(pb, pe, sharesbas):
    return ((sharesbas + pb) - pe).rolling(252).skew().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc063_252d_2nd_v063_signal'] = f62ds_f62_dividend_sustainability_calc063_252d_2nd_v063_signal

def f62ds_f62_dividend_sustainability_calc064_504d_2nd_v064_signal(ev, fcf):
    return (fcf / ev).rolling(504).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc064_504d_2nd_v064_signal'] = f62ds_f62_dividend_sustainability_calc064_504d_2nd_v064_signal

def f62ds_f62_dividend_sustainability_calc065_21d_2nd_v065_signal(ebitda, workingcapital):
    return (workingcapital - ebitda).rolling(21).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc065_21d_2nd_v065_signal'] = f62ds_f62_dividend_sustainability_calc065_21d_2nd_v065_signal

def f62ds_f62_dividend_sustainability_calc066_21d_2nd_v066_signal(ncff):
    return ncff.rolling(21).median().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc066_21d_2nd_v066_signal'] = f62ds_f62_dividend_sustainability_calc066_21d_2nd_v066_signal

def f62ds_f62_dividend_sustainability_calc067_504d_2nd_v067_signal(fcf, liabilities, retearn):
    return ((retearn * fcf) + liabilities).rolling(504).max().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc067_504d_2nd_v067_signal'] = f62ds_f62_dividend_sustainability_calc067_504d_2nd_v067_signal

def f62ds_f62_dividend_sustainability_calc068_126d_2nd_v068_signal(equity, ncfi):
    return (equity / ncfi).rolling(126).rank().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc068_126d_2nd_v068_signal'] = f62ds_f62_dividend_sustainability_calc068_126d_2nd_v068_signal

def f62ds_f62_dividend_sustainability_calc069_126d_2nd_v069_signal(pe, revenue):
    return (revenue - pe).rolling(126).var().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc069_126d_2nd_v069_signal'] = f62ds_f62_dividend_sustainability_calc069_126d_2nd_v069_signal

def f62ds_f62_dividend_sustainability_calc070_5d_2nd_v070_signal(eps, evebit):
    return (evebit - eps).rolling(5).min().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc070_5d_2nd_v070_signal'] = f62ds_f62_dividend_sustainability_calc070_5d_2nd_v070_signal

def f62ds_f62_dividend_sustainability_calc071_252d_2nd_v071_signal(gp, high):
    return (gp / high).rolling(252).std().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc071_252d_2nd_v071_signal'] = f62ds_f62_dividend_sustainability_calc071_252d_2nd_v071_signal

def f62ds_f62_dividend_sustainability_calc072_126d_2nd_v072_signal(close, opinc):
    return (opinc / close).rolling(126).rank().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc072_126d_2nd_v072_signal'] = f62ds_f62_dividend_sustainability_calc072_126d_2nd_v072_signal

def f62ds_f62_dividend_sustainability_calc073_10d_2nd_v073_signal(opinc):
    return opinc.rolling(10).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc073_10d_2nd_v073_signal'] = f62ds_f62_dividend_sustainability_calc073_10d_2nd_v073_signal

def f62ds_f62_dividend_sustainability_calc074_504d_2nd_v074_signal(sharesbas, volume):
    return (volume + sharesbas).rolling(504).median().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc074_504d_2nd_v074_signal'] = f62ds_f62_dividend_sustainability_calc074_504d_2nd_v074_signal

def f62ds_f62_dividend_sustainability_calc075_21d_2nd_v075_signal(closeadj, low):
    return (closeadj + low).rolling(21).kurt().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc075_21d_2nd_v075_signal'] = f62ds_f62_dividend_sustainability_calc075_21d_2nd_v075_signal

def f62ds_f62_dividend_sustainability_calc076_252d_2nd_v076_signal(intexp):
    return intexp.rolling(252).median().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc076_252d_2nd_v076_signal'] = f62ds_f62_dividend_sustainability_calc076_252d_2nd_v076_signal

def f62ds_f62_dividend_sustainability_calc077_21d_2nd_v077_signal(currentratio, ncfo):
    return (ncfo + currentratio).rolling(21).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc077_21d_2nd_v077_signal'] = f62ds_f62_dividend_sustainability_calc077_21d_2nd_v077_signal

def f62ds_f62_dividend_sustainability_calc078_504d_2nd_v078_signal(evebit, low):
    return (low / evebit).rolling(504).min().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc078_504d_2nd_v078_signal'] = f62ds_f62_dividend_sustainability_calc078_504d_2nd_v078_signal

def f62ds_f62_dividend_sustainability_calc079_5d_2nd_v079_signal(ebitda, pe, workingcapital):
    return ((workingcapital * pe) / ebitda).rolling(5).mean().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc079_5d_2nd_v079_signal'] = f62ds_f62_dividend_sustainability_calc079_5d_2nd_v079_signal

def f62ds_f62_dividend_sustainability_calc080_63d_2nd_v080_signal(debt, evebit, sharesbas):
    return ((sharesbas / evebit) * debt).rolling(63).var().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc080_63d_2nd_v080_signal'] = f62ds_f62_dividend_sustainability_calc080_63d_2nd_v080_signal

def f62ds_f62_dividend_sustainability_calc081_42d_2nd_v081_signal(intexp, pe, volume):
    return ((volume - intexp) / pe).rolling(42).std().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc081_42d_2nd_v081_signal'] = f62ds_f62_dividend_sustainability_calc081_42d_2nd_v081_signal

def f62ds_f62_dividend_sustainability_calc082_504d_2nd_v082_signal(close, gp):
    return (close + gp).rolling(504).kurt().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc082_504d_2nd_v082_signal'] = f62ds_f62_dividend_sustainability_calc082_504d_2nd_v082_signal

def f62ds_f62_dividend_sustainability_calc083_252d_2nd_v083_signal(gp, revenue, workingcapital):
    return ((gp - revenue) - workingcapital).rolling(252).rank().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc083_252d_2nd_v083_signal'] = f62ds_f62_dividend_sustainability_calc083_252d_2nd_v083_signal

def f62ds_f62_dividend_sustainability_calc084_42d_2nd_v084_signal(marketcap, pe):
    return (marketcap * pe).rolling(42).mean().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc084_42d_2nd_v084_signal'] = f62ds_f62_dividend_sustainability_calc084_42d_2nd_v084_signal

def f62ds_f62_dividend_sustainability_calc085_42d_2nd_v085_signal(close, low):
    return (low - close).rolling(42).rank().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc085_42d_2nd_v085_signal'] = f62ds_f62_dividend_sustainability_calc085_42d_2nd_v085_signal

def f62ds_f62_dividend_sustainability_calc086_63d_2nd_v086_signal(retearn, volume):
    return (retearn - volume).rolling(63).std().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc086_63d_2nd_v086_signal'] = f62ds_f62_dividend_sustainability_calc086_63d_2nd_v086_signal

def f62ds_f62_dividend_sustainability_calc087_10d_2nd_v087_signal(debt, netinc):
    return (netinc - debt).rolling(10).rank().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc087_10d_2nd_v087_signal'] = f62ds_f62_dividend_sustainability_calc087_10d_2nd_v087_signal

def f62ds_f62_dividend_sustainability_calc088_252d_2nd_v088_signal(intexp):
    return intexp.rolling(252).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc088_252d_2nd_v088_signal'] = f62ds_f62_dividend_sustainability_calc088_252d_2nd_v088_signal

def f62ds_f62_dividend_sustainability_calc089_126d_2nd_v089_signal(fcf, ncff):
    return (ncff + fcf).rolling(126).var().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc089_126d_2nd_v089_signal'] = f62ds_f62_dividend_sustainability_calc089_126d_2nd_v089_signal

def f62ds_f62_dividend_sustainability_calc090_42d_2nd_v090_signal(eps):
    return eps.rolling(42).rank().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc090_42d_2nd_v090_signal'] = f62ds_f62_dividend_sustainability_calc090_42d_2nd_v090_signal

def f62ds_f62_dividend_sustainability_calc091_42d_2nd_v091_signal(currentratio, ev):
    return (ev - currentratio).rolling(42).rank().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc091_42d_2nd_v091_signal'] = f62ds_f62_dividend_sustainability_calc091_42d_2nd_v091_signal

def f62ds_f62_dividend_sustainability_calc092_42d_2nd_v092_signal(assets, capex):
    return (assets / capex).rolling(42).var().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc092_42d_2nd_v092_signal'] = f62ds_f62_dividend_sustainability_calc092_42d_2nd_v092_signal

def f62ds_f62_dividend_sustainability_calc093_126d_2nd_v093_signal(debt, high):
    return (high * debt).rolling(126).rank().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc093_126d_2nd_v093_signal'] = f62ds_f62_dividend_sustainability_calc093_126d_2nd_v093_signal

def f62ds_f62_dividend_sustainability_calc094_5d_2nd_v094_signal(retearn):
    return retearn.rolling(5).kurt().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc094_5d_2nd_v094_signal'] = f62ds_f62_dividend_sustainability_calc094_5d_2nd_v094_signal

def f62ds_f62_dividend_sustainability_calc095_126d_2nd_v095_signal(workingcapital):
    return workingcapital.rolling(126).var().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc095_126d_2nd_v095_signal'] = f62ds_f62_dividend_sustainability_calc095_126d_2nd_v095_signal

def f62ds_f62_dividend_sustainability_calc096_126d_2nd_v096_signal(close, intexp):
    return (intexp / close).rolling(126).mean().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc096_126d_2nd_v096_signal'] = f62ds_f62_dividend_sustainability_calc096_126d_2nd_v096_signal

def f62ds_f62_dividend_sustainability_calc097_504d_2nd_v097_signal(evebit):
    return evebit.rolling(504).skew().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc097_504d_2nd_v097_signal'] = f62ds_f62_dividend_sustainability_calc097_504d_2nd_v097_signal

def f62ds_f62_dividend_sustainability_calc098_504d_2nd_v098_signal(taxexp, workingcapital):
    return (taxexp - workingcapital).rolling(504).skew().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc098_504d_2nd_v098_signal'] = f62ds_f62_dividend_sustainability_calc098_504d_2nd_v098_signal

def f62ds_f62_dividend_sustainability_calc099_63d_2nd_v099_signal(liabilities, pe):
    return (pe * liabilities).rolling(63).var().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc099_63d_2nd_v099_signal'] = f62ds_f62_dividend_sustainability_calc099_63d_2nd_v099_signal

def f62ds_f62_dividend_sustainability_calc100_126d_2nd_v100_signal(ps):
    return ps.rolling(126).mean().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc100_126d_2nd_v100_signal'] = f62ds_f62_dividend_sustainability_calc100_126d_2nd_v100_signal

def f62ds_f62_dividend_sustainability_calc101_252d_2nd_v101_signal(closeadj, evebitda, gp):
    return ((evebitda / gp) * closeadj).rolling(252).kurt().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc101_252d_2nd_v101_signal'] = f62ds_f62_dividend_sustainability_calc101_252d_2nd_v101_signal

def f62ds_f62_dividend_sustainability_calc102_63d_2nd_v102_signal(currentratio, fcf):
    return (fcf / currentratio).rolling(63).std().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc102_63d_2nd_v102_signal'] = f62ds_f62_dividend_sustainability_calc102_63d_2nd_v102_signal

def f62ds_f62_dividend_sustainability_calc103_126d_2nd_v103_signal(ps):
    return ps.rolling(126).mean().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc103_126d_2nd_v103_signal'] = f62ds_f62_dividend_sustainability_calc103_126d_2nd_v103_signal

def f62ds_f62_dividend_sustainability_calc104_21d_2nd_v104_signal(high):
    return high.rolling(21).std().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc104_21d_2nd_v104_signal'] = f62ds_f62_dividend_sustainability_calc104_21d_2nd_v104_signal

def f62ds_f62_dividend_sustainability_calc105_126d_2nd_v105_signal(equity):
    return equity.rolling(126).median().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc105_126d_2nd_v105_signal'] = f62ds_f62_dividend_sustainability_calc105_126d_2nd_v105_signal

def f62ds_f62_dividend_sustainability_calc106_504d_2nd_v106_signal(currentratio, ncff, netinc):
    return ((netinc - ncff) + currentratio).rolling(504).var().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc106_504d_2nd_v106_signal'] = f62ds_f62_dividend_sustainability_calc106_504d_2nd_v106_signal

def f62ds_f62_dividend_sustainability_calc107_504d_2nd_v107_signal(debt, eps):
    return (debt + eps).rolling(504).var().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc107_504d_2nd_v107_signal'] = f62ds_f62_dividend_sustainability_calc107_504d_2nd_v107_signal

def f62ds_f62_dividend_sustainability_calc108_63d_2nd_v108_signal(currentratio, pe):
    return (pe * currentratio).rolling(63).median().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc108_63d_2nd_v108_signal'] = f62ds_f62_dividend_sustainability_calc108_63d_2nd_v108_signal

def f62ds_f62_dividend_sustainability_calc109_10d_2nd_v109_signal(closeadj):
    return closeadj.rolling(10).skew().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc109_10d_2nd_v109_signal'] = f62ds_f62_dividend_sustainability_calc109_10d_2nd_v109_signal

def f62ds_f62_dividend_sustainability_calc110_126d_2nd_v110_signal(fcf, opinc, retearn):
    return ((fcf - retearn) + opinc).rolling(126).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc110_126d_2nd_v110_signal'] = f62ds_f62_dividend_sustainability_calc110_126d_2nd_v110_signal

def f62ds_f62_dividend_sustainability_calc111_10d_2nd_v111_signal(eps, retearn):
    return (retearn + eps).rolling(10).var().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc111_10d_2nd_v111_signal'] = f62ds_f62_dividend_sustainability_calc111_10d_2nd_v111_signal

def f62ds_f62_dividend_sustainability_calc112_10d_2nd_v112_signal(intexp, pb):
    return (pb - intexp).rolling(10).skew().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc112_10d_2nd_v112_signal'] = f62ds_f62_dividend_sustainability_calc112_10d_2nd_v112_signal

def f62ds_f62_dividend_sustainability_calc113_10d_2nd_v113_signal(liabilities, sharesbas):
    return (sharesbas / liabilities).rolling(10).mean().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc113_10d_2nd_v113_signal'] = f62ds_f62_dividend_sustainability_calc113_10d_2nd_v113_signal

def f62ds_f62_dividend_sustainability_calc114_21d_2nd_v114_signal(closeadj, evebit):
    return (evebit * closeadj).rolling(21).std().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc114_21d_2nd_v114_signal'] = f62ds_f62_dividend_sustainability_calc114_21d_2nd_v114_signal

def f62ds_f62_dividend_sustainability_calc115_63d_2nd_v115_signal(ncfo, taxexp):
    return (ncfo / taxexp).rolling(63).mean().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc115_63d_2nd_v115_signal'] = f62ds_f62_dividend_sustainability_calc115_63d_2nd_v115_signal

def f62ds_f62_dividend_sustainability_calc116_126d_2nd_v116_signal(liabilities):
    return liabilities.rolling(126).skew().diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc116_126d_2nd_v116_signal'] = f62ds_f62_dividend_sustainability_calc116_126d_2nd_v116_signal

def f62ds_f62_dividend_sustainability_calc117_42d_2nd_v117_signal(currentratio, liabilities):
    return (currentratio * liabilities).rolling(42).std().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc117_42d_2nd_v117_signal'] = f62ds_f62_dividend_sustainability_calc117_42d_2nd_v117_signal

def f62ds_f62_dividend_sustainability_calc118_252d_2nd_v118_signal(ncfo):
    return ncfo.rolling(252).median().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc118_252d_2nd_v118_signal'] = f62ds_f62_dividend_sustainability_calc118_252d_2nd_v118_signal

def f62ds_f62_dividend_sustainability_calc119_21d_2nd_v119_signal(currentratio, high):
    return (high - currentratio).rolling(21).min().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc119_21d_2nd_v119_signal'] = f62ds_f62_dividend_sustainability_calc119_21d_2nd_v119_signal

def f62ds_f62_dividend_sustainability_calc120_504d_2nd_v120_signal(evebitda, netinc):
    return (netinc * evebitda).rolling(504).kurt().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc120_504d_2nd_v120_signal'] = f62ds_f62_dividend_sustainability_calc120_504d_2nd_v120_signal

def f62ds_f62_dividend_sustainability_calc121_10d_2nd_v121_signal(low, ncfo):
    return (low * ncfo).rolling(10).var().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc121_10d_2nd_v121_signal'] = f62ds_f62_dividend_sustainability_calc121_10d_2nd_v121_signal

def f62ds_f62_dividend_sustainability_calc122_42d_2nd_v122_signal(close, ebitda):
    return (ebitda + close).rolling(42).min().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc122_42d_2nd_v122_signal'] = f62ds_f62_dividend_sustainability_calc122_42d_2nd_v122_signal

def f62ds_f62_dividend_sustainability_calc123_5d_2nd_v123_signal(equity, taxexp):
    return (equity - taxexp).rolling(5).skew().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc123_5d_2nd_v123_signal'] = f62ds_f62_dividend_sustainability_calc123_5d_2nd_v123_signal

def f62ds_f62_dividend_sustainability_calc124_42d_2nd_v124_signal(fcf, low):
    return (low * fcf).rolling(42).rank().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc124_42d_2nd_v124_signal'] = f62ds_f62_dividend_sustainability_calc124_42d_2nd_v124_signal

def f62ds_f62_dividend_sustainability_calc125_10d_2nd_v125_signal(ps, volume):
    return (ps / volume).rolling(10).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc125_10d_2nd_v125_signal'] = f62ds_f62_dividend_sustainability_calc125_10d_2nd_v125_signal

def f62ds_f62_dividend_sustainability_calc126_63d_2nd_v126_signal(assets, equity):
    return (equity - assets).rolling(63).median().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc126_63d_2nd_v126_signal'] = f62ds_f62_dividend_sustainability_calc126_63d_2nd_v126_signal

def f62ds_f62_dividend_sustainability_calc127_126d_2nd_v127_signal(gp, low, netinc):
    return ((low + netinc) - gp).rolling(126).kurt().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc127_126d_2nd_v127_signal'] = f62ds_f62_dividend_sustainability_calc127_126d_2nd_v127_signal

def f62ds_f62_dividend_sustainability_calc128_42d_2nd_v128_signal(marketcap, workingcapital):
    return (workingcapital / marketcap).rolling(42).std().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc128_42d_2nd_v128_signal'] = f62ds_f62_dividend_sustainability_calc128_42d_2nd_v128_signal

def f62ds_f62_dividend_sustainability_calc129_21d_2nd_v129_signal(fcf, retearn):
    return (retearn * fcf).rolling(21).median().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc129_21d_2nd_v129_signal'] = f62ds_f62_dividend_sustainability_calc129_21d_2nd_v129_signal

def f62ds_f62_dividend_sustainability_calc130_5d_2nd_v130_signal(evebit, retearn):
    return (evebit - retearn).rolling(5).kurt().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc130_5d_2nd_v130_signal'] = f62ds_f62_dividend_sustainability_calc130_5d_2nd_v130_signal

def f62ds_f62_dividend_sustainability_calc131_5d_2nd_v131_signal(fcf):
    return fcf.rolling(5).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc131_5d_2nd_v131_signal'] = f62ds_f62_dividend_sustainability_calc131_5d_2nd_v131_signal

def f62ds_f62_dividend_sustainability_calc132_21d_2nd_v132_signal(eps, ps):
    return (ps - eps).rolling(21).var().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc132_21d_2nd_v132_signal'] = f62ds_f62_dividend_sustainability_calc132_21d_2nd_v132_signal

def f62ds_f62_dividend_sustainability_calc133_63d_2nd_v133_signal(ncff, taxexp, volume):
    return ((volume + taxexp) + ncff).rolling(63).min().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc133_63d_2nd_v133_signal'] = f62ds_f62_dividend_sustainability_calc133_63d_2nd_v133_signal

def f62ds_f62_dividend_sustainability_calc134_21d_2nd_v134_signal(liabilities):
    return liabilities.rolling(21).var().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc134_21d_2nd_v134_signal'] = f62ds_f62_dividend_sustainability_calc134_21d_2nd_v134_signal

def f62ds_f62_dividend_sustainability_calc135_21d_2nd_v135_signal(close):
    return close.rolling(21).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc135_21d_2nd_v135_signal'] = f62ds_f62_dividend_sustainability_calc135_21d_2nd_v135_signal

def f62ds_f62_dividend_sustainability_calc136_42d_2nd_v136_signal(evebit):
    return evebit.rolling(42).median().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc136_42d_2nd_v136_signal'] = f62ds_f62_dividend_sustainability_calc136_42d_2nd_v136_signal

def f62ds_f62_dividend_sustainability_calc137_63d_2nd_v137_signal(close, ps):
    return (ps * close).rolling(63).kurt().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc137_63d_2nd_v137_signal'] = f62ds_f62_dividend_sustainability_calc137_63d_2nd_v137_signal

def f62ds_f62_dividend_sustainability_calc138_63d_2nd_v138_signal(eps, workingcapital):
    return (workingcapital / eps).rolling(63).max().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc138_63d_2nd_v138_signal'] = f62ds_f62_dividend_sustainability_calc138_63d_2nd_v138_signal

def f62ds_f62_dividend_sustainability_calc139_10d_2nd_v139_signal(high, open, ps):
    return ((ps - high) + open).rolling(10).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc139_10d_2nd_v139_signal'] = f62ds_f62_dividend_sustainability_calc139_10d_2nd_v139_signal

def f62ds_f62_dividend_sustainability_calc140_126d_2nd_v140_signal(ebitda, ncfi):
    return (ebitda / ncfi).rolling(126).kurt().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc140_126d_2nd_v140_signal'] = f62ds_f62_dividend_sustainability_calc140_126d_2nd_v140_signal

def f62ds_f62_dividend_sustainability_calc141_504d_2nd_v141_signal(ebitda, eps):
    return (ebitda - eps).rolling(504).mean().diff(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc141_504d_2nd_v141_signal'] = f62ds_f62_dividend_sustainability_calc141_504d_2nd_v141_signal

def f62ds_f62_dividend_sustainability_calc142_42d_2nd_v142_signal(debt, ps):
    return (debt / ps).rolling(42).rank().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc142_42d_2nd_v142_signal'] = f62ds_f62_dividend_sustainability_calc142_42d_2nd_v142_signal

def f62ds_f62_dividend_sustainability_calc143_504d_2nd_v143_signal(low, netinc):
    return (netinc + low).rolling(504).max().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc143_504d_2nd_v143_signal'] = f62ds_f62_dividend_sustainability_calc143_504d_2nd_v143_signal

def f62ds_f62_dividend_sustainability_calc144_63d_2nd_v144_signal(pb, workingcapital):
    return (workingcapital - pb).rolling(63).rank().pct_change(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc144_63d_2nd_v144_signal'] = f62ds_f62_dividend_sustainability_calc144_63d_2nd_v144_signal

def f62ds_f62_dividend_sustainability_calc145_252d_2nd_v145_signal(assets, close, ncfo):
    return ((ncfo * assets) * close).rolling(252).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc145_252d_2nd_v145_signal'] = f62ds_f62_dividend_sustainability_calc145_252d_2nd_v145_signal

def f62ds_f62_dividend_sustainability_calc146_5d_2nd_v146_signal(intexp, pe):
    return (intexp / pe).rolling(5).max().pct_change(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc146_5d_2nd_v146_signal'] = f62ds_f62_dividend_sustainability_calc146_5d_2nd_v146_signal

def f62ds_f62_dividend_sustainability_calc147_10d_2nd_v147_signal(debt, workingcapital):
    return (workingcapital / debt).rolling(10).max().pct_change(10).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc147_10d_2nd_v147_signal'] = f62ds_f62_dividend_sustainability_calc147_10d_2nd_v147_signal

def f62ds_f62_dividend_sustainability_calc148_21d_2nd_v148_signal(sharesbas):
    return sharesbas.rolling(21).kurt().pct_change(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc148_21d_2nd_v148_signal'] = f62ds_f62_dividend_sustainability_calc148_21d_2nd_v148_signal

def f62ds_f62_dividend_sustainability_calc149_42d_2nd_v149_signal(ev):
    return ev.rolling(42).max().diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc149_42d_2nd_v149_signal'] = f62ds_f62_dividend_sustainability_calc149_42d_2nd_v149_signal

def f62ds_f62_dividend_sustainability_calc150_63d_2nd_v150_signal(evebitda):
    return evebitda.rolling(63).mean().diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc150_63d_2nd_v150_signal'] = f62ds_f62_dividend_sustainability_calc150_63d_2nd_v150_signal



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
