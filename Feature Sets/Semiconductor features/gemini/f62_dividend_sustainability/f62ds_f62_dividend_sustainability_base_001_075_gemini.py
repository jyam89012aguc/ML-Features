import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f62ds_f62_dividend_sustainability_calc001_5d_base_v001_signal(pb, pe):
    res = (pe - pb).diff(10).rolling(5).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc001_5d_base_v001_signal'] = f62ds_f62_dividend_sustainability_calc001_5d_base_v001_signal

def f62ds_f62_dividend_sustainability_calc002_21d_base_v002_signal(close):
    res = close.diff(21).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc002_21d_base_v002_signal'] = f62ds_f62_dividend_sustainability_calc002_21d_base_v002_signal

def f62ds_f62_dividend_sustainability_calc003_5d_base_v003_signal(close, volume):
    res = (volume * close).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc003_5d_base_v003_signal'] = f62ds_f62_dividend_sustainability_calc003_5d_base_v003_signal

def f62ds_f62_dividend_sustainability_calc004_21d_base_v004_signal(ncfo, revenue):
    res = (ncfo * revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc004_21d_base_v004_signal'] = f62ds_f62_dividend_sustainability_calc004_21d_base_v004_signal

def f62ds_f62_dividend_sustainability_calc005_126d_base_v005_signal(currentratio):
    res = currentratio.rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc005_126d_base_v005_signal'] = f62ds_f62_dividend_sustainability_calc005_126d_base_v005_signal

def f62ds_f62_dividend_sustainability_calc006_504d_base_v006_signal(pb, pe):
    res = (pe / pb).pct_change(5).rolling(504).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc006_504d_base_v006_signal'] = f62ds_f62_dividend_sustainability_calc006_504d_base_v006_signal

def f62ds_f62_dividend_sustainability_calc007_252d_base_v007_signal(opinc, revenue):
    res = (opinc + revenue).pct_change(10).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc007_252d_base_v007_signal'] = f62ds_f62_dividend_sustainability_calc007_252d_base_v007_signal

def f62ds_f62_dividend_sustainability_calc008_252d_base_v008_signal(liabilities, ncff, opinc):
    res = ((liabilities / ncff) - opinc).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc008_252d_base_v008_signal'] = f62ds_f62_dividend_sustainability_calc008_252d_base_v008_signal

def f62ds_f62_dividend_sustainability_calc009_5d_base_v009_signal(pe):
    res = pe.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc009_5d_base_v009_signal'] = f62ds_f62_dividend_sustainability_calc009_5d_base_v009_signal

def f62ds_f62_dividend_sustainability_calc010_10d_base_v010_signal(eps, ncff):
    res = (ncff * eps).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc010_10d_base_v010_signal'] = f62ds_f62_dividend_sustainability_calc010_10d_base_v010_signal

def f62ds_f62_dividend_sustainability_calc011_10d_base_v011_signal(fcf, revenue):
    res = (fcf / revenue).diff(10).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc011_10d_base_v011_signal'] = f62ds_f62_dividend_sustainability_calc011_10d_base_v011_signal

def f62ds_f62_dividend_sustainability_calc012_504d_base_v012_signal(gp, open):
    res = (open - gp).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc012_504d_base_v012_signal'] = f62ds_f62_dividend_sustainability_calc012_504d_base_v012_signal

def f62ds_f62_dividend_sustainability_calc013_126d_base_v013_signal(currentratio, fcf, ncfi):
    res = ((ncfi * fcf) / currentratio).pct_change(1).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc013_126d_base_v013_signal'] = f62ds_f62_dividend_sustainability_calc013_126d_base_v013_signal

def f62ds_f62_dividend_sustainability_calc014_504d_base_v014_signal(equity, netinc):
    res = (netinc + equity).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc014_504d_base_v014_signal'] = f62ds_f62_dividend_sustainability_calc014_504d_base_v014_signal

def f62ds_f62_dividend_sustainability_calc015_42d_base_v015_signal(fcf, opinc, pb):
    res = ((opinc - pb) + fcf).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc015_42d_base_v015_signal'] = f62ds_f62_dividend_sustainability_calc015_42d_base_v015_signal

def f62ds_f62_dividend_sustainability_calc016_5d_base_v016_signal(assets, workingcapital):
    res = (workingcapital + assets).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc016_5d_base_v016_signal'] = f62ds_f62_dividend_sustainability_calc016_5d_base_v016_signal

def f62ds_f62_dividend_sustainability_calc017_10d_base_v017_signal(ncfo, pe, sharesbas):
    res = ((ncfo / pe) + sharesbas).pct_change(5).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc017_10d_base_v017_signal'] = f62ds_f62_dividend_sustainability_calc017_10d_base_v017_signal

def f62ds_f62_dividend_sustainability_calc018_42d_base_v018_signal(debt, intexp):
    res = (debt - intexp).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc018_42d_base_v018_signal'] = f62ds_f62_dividend_sustainability_calc018_42d_base_v018_signal

def f62ds_f62_dividend_sustainability_calc019_10d_base_v019_signal(netinc, revenue):
    res = (netinc / revenue).diff(5).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc019_10d_base_v019_signal'] = f62ds_f62_dividend_sustainability_calc019_10d_base_v019_signal

def f62ds_f62_dividend_sustainability_calc020_126d_base_v020_signal(assets, ncfo):
    res = (ncfo * assets).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc020_126d_base_v020_signal'] = f62ds_f62_dividend_sustainability_calc020_126d_base_v020_signal

def f62ds_f62_dividend_sustainability_calc021_63d_base_v021_signal(assets, liabilities):
    res = (liabilities + assets).diff(21).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc021_63d_base_v021_signal'] = f62ds_f62_dividend_sustainability_calc021_63d_base_v021_signal

def f62ds_f62_dividend_sustainability_calc022_504d_base_v022_signal(assets, ncfo):
    res = (ncfo * assets).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc022_504d_base_v022_signal'] = f62ds_f62_dividend_sustainability_calc022_504d_base_v022_signal

def f62ds_f62_dividend_sustainability_calc023_252d_base_v023_signal(closeadj):
    res = closeadj.rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc023_252d_base_v023_signal'] = f62ds_f62_dividend_sustainability_calc023_252d_base_v023_signal

def f62ds_f62_dividend_sustainability_calc024_10d_base_v024_signal(capex, revenue):
    res = (capex * revenue).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc024_10d_base_v024_signal'] = f62ds_f62_dividend_sustainability_calc024_10d_base_v024_signal

def f62ds_f62_dividend_sustainability_calc025_10d_base_v025_signal(volume):
    res = volume.pct_change(21).rolling(10).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc025_10d_base_v025_signal'] = f62ds_f62_dividend_sustainability_calc025_10d_base_v025_signal

def f62ds_f62_dividend_sustainability_calc026_21d_base_v026_signal(capex, close, fcf):
    res = ((capex * fcf) / close).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc026_21d_base_v026_signal'] = f62ds_f62_dividend_sustainability_calc026_21d_base_v026_signal

def f62ds_f62_dividend_sustainability_calc027_42d_base_v027_signal(assets, ncfo):
    res = (ncfo * assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc027_42d_base_v027_signal'] = f62ds_f62_dividend_sustainability_calc027_42d_base_v027_signal

def f62ds_f62_dividend_sustainability_calc028_126d_base_v028_signal(assets):
    res = assets.rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc028_126d_base_v028_signal'] = f62ds_f62_dividend_sustainability_calc028_126d_base_v028_signal

def f62ds_f62_dividend_sustainability_calc029_504d_base_v029_signal(evebit, sharesbas):
    res = (sharesbas * evebit).diff(5).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc029_504d_base_v029_signal'] = f62ds_f62_dividend_sustainability_calc029_504d_base_v029_signal

def f62ds_f62_dividend_sustainability_calc030_126d_base_v030_signal(high):
    res = high.diff(10).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc030_126d_base_v030_signal'] = f62ds_f62_dividend_sustainability_calc030_126d_base_v030_signal

def f62ds_f62_dividend_sustainability_calc031_5d_base_v031_signal(debt, equity):
    res = (debt / equity).diff(10).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc031_5d_base_v031_signal'] = f62ds_f62_dividend_sustainability_calc031_5d_base_v031_signal

def f62ds_f62_dividend_sustainability_calc032_5d_base_v032_signal(currentratio, ps):
    res = (currentratio / ps).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc032_5d_base_v032_signal'] = f62ds_f62_dividend_sustainability_calc032_5d_base_v032_signal

def f62ds_f62_dividend_sustainability_calc033_504d_base_v033_signal(assets, pe):
    res = (assets / pe).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc033_504d_base_v033_signal'] = f62ds_f62_dividend_sustainability_calc033_504d_base_v033_signal

def f62ds_f62_dividend_sustainability_calc034_42d_base_v034_signal(assets, fcf):
    res = (fcf * assets).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc034_42d_base_v034_signal'] = f62ds_f62_dividend_sustainability_calc034_42d_base_v034_signal

def f62ds_f62_dividend_sustainability_calc035_42d_base_v035_signal(close, open, volume):
    res = ((close / volume) / open).pct_change(10).rolling(42).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc035_42d_base_v035_signal'] = f62ds_f62_dividend_sustainability_calc035_42d_base_v035_signal

def f62ds_f62_dividend_sustainability_calc036_42d_base_v036_signal(assets, ncfo):
    res = (ncfo / assets).pct_change(5).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc036_42d_base_v036_signal'] = f62ds_f62_dividend_sustainability_calc036_42d_base_v036_signal

def f62ds_f62_dividend_sustainability_calc037_63d_base_v037_signal(low, retearn, sharesbas):
    res = ((retearn / low) - sharesbas).pct_change(10).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc037_63d_base_v037_signal'] = f62ds_f62_dividend_sustainability_calc037_63d_base_v037_signal

def f62ds_f62_dividend_sustainability_calc038_126d_base_v038_signal(ev, evebitda):
    res = (ev + evebitda).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc038_126d_base_v038_signal'] = f62ds_f62_dividend_sustainability_calc038_126d_base_v038_signal

def f62ds_f62_dividend_sustainability_calc039_504d_base_v039_signal(closeadj):
    res = closeadj.diff(21).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc039_504d_base_v039_signal'] = f62ds_f62_dividend_sustainability_calc039_504d_base_v039_signal

def f62ds_f62_dividend_sustainability_calc040_126d_base_v040_signal(closeadj, eps):
    res = (eps / closeadj).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc040_126d_base_v040_signal'] = f62ds_f62_dividend_sustainability_calc040_126d_base_v040_signal

def f62ds_f62_dividend_sustainability_calc041_126d_base_v041_signal(assets, netinc):
    res = (netinc - assets).pct_change(1).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc041_126d_base_v041_signal'] = f62ds_f62_dividend_sustainability_calc041_126d_base_v041_signal

def f62ds_f62_dividend_sustainability_calc042_10d_base_v042_signal(ebitda, revenue):
    res = (revenue + ebitda).rolling(10).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc042_10d_base_v042_signal'] = f62ds_f62_dividend_sustainability_calc042_10d_base_v042_signal

def f62ds_f62_dividend_sustainability_calc043_10d_base_v043_signal(evebitda):
    res = evebitda.rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc043_10d_base_v043_signal'] = f62ds_f62_dividend_sustainability_calc043_10d_base_v043_signal

def f62ds_f62_dividend_sustainability_calc044_63d_base_v044_signal(ncfo, revenue):
    res = (ncfo / revenue).diff(21).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc044_63d_base_v044_signal'] = f62ds_f62_dividend_sustainability_calc044_63d_base_v044_signal

def f62ds_f62_dividend_sustainability_calc045_10d_base_v045_signal(ncff, volume):
    res = (ncff + volume).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc045_10d_base_v045_signal'] = f62ds_f62_dividend_sustainability_calc045_10d_base_v045_signal

def f62ds_f62_dividend_sustainability_calc046_504d_base_v046_signal(liabilities, low, volume):
    res = ((low + volume) * liabilities).diff(1).rolling(504).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc046_504d_base_v046_signal'] = f62ds_f62_dividend_sustainability_calc046_504d_base_v046_signal

def f62ds_f62_dividend_sustainability_calc047_21d_base_v047_signal(capex, gp):
    res = (gp + capex).diff(21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc047_21d_base_v047_signal'] = f62ds_f62_dividend_sustainability_calc047_21d_base_v047_signal

def f62ds_f62_dividend_sustainability_calc048_21d_base_v048_signal(ncff):
    res = ncff.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc048_21d_base_v048_signal'] = f62ds_f62_dividend_sustainability_calc048_21d_base_v048_signal

def f62ds_f62_dividend_sustainability_calc049_42d_base_v049_signal(ev, fcf):
    res = (ev / fcf).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc049_42d_base_v049_signal'] = f62ds_f62_dividend_sustainability_calc049_42d_base_v049_signal

def f62ds_f62_dividend_sustainability_calc050_21d_base_v050_signal(ncfo, volume):
    res = (ncfo - volume).pct_change(21).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc050_21d_base_v050_signal'] = f62ds_f62_dividend_sustainability_calc050_21d_base_v050_signal

def f62ds_f62_dividend_sustainability_calc051_5d_base_v051_signal(close, opinc):
    res = (opinc * close).pct_change(21).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc051_5d_base_v051_signal'] = f62ds_f62_dividend_sustainability_calc051_5d_base_v051_signal

def f62ds_f62_dividend_sustainability_calc052_21d_base_v052_signal(ev, netinc):
    res = (ev - netinc).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc052_21d_base_v052_signal'] = f62ds_f62_dividend_sustainability_calc052_21d_base_v052_signal

def f62ds_f62_dividend_sustainability_calc053_252d_base_v053_signal(retearn):
    res = retearn.rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc053_252d_base_v053_signal'] = f62ds_f62_dividend_sustainability_calc053_252d_base_v053_signal

def f62ds_f62_dividend_sustainability_calc054_21d_base_v054_signal(pb):
    res = pb.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc054_21d_base_v054_signal'] = f62ds_f62_dividend_sustainability_calc054_21d_base_v054_signal

def f62ds_f62_dividend_sustainability_calc055_504d_base_v055_signal(marketcap, ncff):
    res = (ncff + marketcap).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc055_504d_base_v055_signal'] = f62ds_f62_dividend_sustainability_calc055_504d_base_v055_signal

def f62ds_f62_dividend_sustainability_calc056_10d_base_v056_signal(currentratio, ps):
    res = (currentratio * ps).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc056_10d_base_v056_signal'] = f62ds_f62_dividend_sustainability_calc056_10d_base_v056_signal

def f62ds_f62_dividend_sustainability_calc057_504d_base_v057_signal(assets):
    res = assets.pct_change(21).rolling(504).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc057_504d_base_v057_signal'] = f62ds_f62_dividend_sustainability_calc057_504d_base_v057_signal

def f62ds_f62_dividend_sustainability_calc058_504d_base_v058_signal(assets, open):
    res = (assets * open).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc058_504d_base_v058_signal'] = f62ds_f62_dividend_sustainability_calc058_504d_base_v058_signal

def f62ds_f62_dividend_sustainability_calc059_63d_base_v059_signal(assets, gp, taxexp):
    res = ((gp / taxexp) / assets).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc059_63d_base_v059_signal'] = f62ds_f62_dividend_sustainability_calc059_63d_base_v059_signal

def f62ds_f62_dividend_sustainability_calc060_21d_base_v060_signal(gp, revenue):
    res = (gp * revenue).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc060_21d_base_v060_signal'] = f62ds_f62_dividend_sustainability_calc060_21d_base_v060_signal

def f62ds_f62_dividend_sustainability_calc061_504d_base_v061_signal(opinc):
    res = opinc.pct_change(21).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc061_504d_base_v061_signal'] = f62ds_f62_dividend_sustainability_calc061_504d_base_v061_signal

def f62ds_f62_dividend_sustainability_calc062_10d_base_v062_signal(ev, ncfi):
    res = (ncfi * ev).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc062_10d_base_v062_signal'] = f62ds_f62_dividend_sustainability_calc062_10d_base_v062_signal

def f62ds_f62_dividend_sustainability_calc063_252d_base_v063_signal(ncfo):
    res = ncfo.rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc063_252d_base_v063_signal'] = f62ds_f62_dividend_sustainability_calc063_252d_base_v063_signal

def f62ds_f62_dividend_sustainability_calc064_42d_base_v064_signal(equity, netinc):
    res = (netinc / equity).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc064_42d_base_v064_signal'] = f62ds_f62_dividend_sustainability_calc064_42d_base_v064_signal

def f62ds_f62_dividend_sustainability_calc065_42d_base_v065_signal(revenue):
    res = revenue.pct_change(10).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc065_42d_base_v065_signal'] = f62ds_f62_dividend_sustainability_calc065_42d_base_v065_signal

def f62ds_f62_dividend_sustainability_calc066_42d_base_v066_signal(capex, revenue):
    res = (capex / revenue).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc066_42d_base_v066_signal'] = f62ds_f62_dividend_sustainability_calc066_42d_base_v066_signal

def f62ds_f62_dividend_sustainability_calc067_252d_base_v067_signal(eps):
    res = eps.rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc067_252d_base_v067_signal'] = f62ds_f62_dividend_sustainability_calc067_252d_base_v067_signal

def f62ds_f62_dividend_sustainability_calc068_252d_base_v068_signal(assets, evebitda):
    res = (assets / evebitda).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc068_252d_base_v068_signal'] = f62ds_f62_dividend_sustainability_calc068_252d_base_v068_signal

def f62ds_f62_dividend_sustainability_calc069_63d_base_v069_signal(closeadj, pb, taxexp):
    res = ((closeadj / pb) + taxexp).pct_change(21).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc069_63d_base_v069_signal'] = f62ds_f62_dividend_sustainability_calc069_63d_base_v069_signal

def f62ds_f62_dividend_sustainability_calc070_10d_base_v070_signal(ncfi, pb, ps):
    res = ((ncfi * pb) * ps).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc070_10d_base_v070_signal'] = f62ds_f62_dividend_sustainability_calc070_10d_base_v070_signal

def f62ds_f62_dividend_sustainability_calc071_504d_base_v071_signal(fcf, netinc):
    res = (fcf / netinc).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc071_504d_base_v071_signal'] = f62ds_f62_dividend_sustainability_calc071_504d_base_v071_signal

def f62ds_f62_dividend_sustainability_calc072_21d_base_v072_signal(debt, equity):
    res = (debt - equity).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc072_21d_base_v072_signal'] = f62ds_f62_dividend_sustainability_calc072_21d_base_v072_signal

def f62ds_f62_dividend_sustainability_calc073_252d_base_v073_signal(closeadj, ps, volume):
    res = ((volume * ps) + closeadj).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc073_252d_base_v073_signal'] = f62ds_f62_dividend_sustainability_calc073_252d_base_v073_signal

def f62ds_f62_dividend_sustainability_calc074_42d_base_v074_signal(eps):
    res = eps.pct_change(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc074_42d_base_v074_signal'] = f62ds_f62_dividend_sustainability_calc074_42d_base_v074_signal

def f62ds_f62_dividend_sustainability_calc075_63d_base_v075_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(21).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc075_63d_base_v075_signal'] = f62ds_f62_dividend_sustainability_calc075_63d_base_v075_signal



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
