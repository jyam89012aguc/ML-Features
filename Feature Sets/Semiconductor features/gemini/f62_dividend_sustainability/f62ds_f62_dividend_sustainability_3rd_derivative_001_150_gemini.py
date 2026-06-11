import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f62ds_f62_dividend_sustainability_calc001_10d_3rd_v001_signal(intexp, ncfi):
    return (ncfi / intexp).rolling(10).std().pct_change(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc001_10d_3rd_v001_signal'] = f62ds_f62_dividend_sustainability_calc001_10d_3rd_v001_signal

def f62ds_f62_dividend_sustainability_calc002_504d_3rd_v002_signal(gp):
    return gp.rolling(504).std().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc002_504d_3rd_v002_signal'] = f62ds_f62_dividend_sustainability_calc002_504d_3rd_v002_signal

def f62ds_f62_dividend_sustainability_calc003_21d_3rd_v003_signal(intexp, taxexp):
    return (intexp / taxexp).rolling(21).std().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc003_21d_3rd_v003_signal'] = f62ds_f62_dividend_sustainability_calc003_21d_3rd_v003_signal

def f62ds_f62_dividend_sustainability_calc004_5d_3rd_v004_signal(capex, pe):
    return (capex / pe).rolling(5).var().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc004_5d_3rd_v004_signal'] = f62ds_f62_dividend_sustainability_calc004_5d_3rd_v004_signal

def f62ds_f62_dividend_sustainability_calc005_63d_3rd_v005_signal(assets, capex, low):
    return ((capex - assets) + low).rolling(63).skew().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc005_63d_3rd_v005_signal'] = f62ds_f62_dividend_sustainability_calc005_63d_3rd_v005_signal

def f62ds_f62_dividend_sustainability_calc006_5d_3rd_v006_signal(ebitda, workingcapital):
    return (workingcapital - ebitda).rolling(5).std().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc006_5d_3rd_v006_signal'] = f62ds_f62_dividend_sustainability_calc006_5d_3rd_v006_signal

def f62ds_f62_dividend_sustainability_calc007_63d_3rd_v007_signal(fcf, marketcap):
    return (fcf * marketcap).rolling(63).skew().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc007_63d_3rd_v007_signal'] = f62ds_f62_dividend_sustainability_calc007_63d_3rd_v007_signal

def f62ds_f62_dividend_sustainability_calc008_63d_3rd_v008_signal(marketcap, opinc, workingcapital):
    return ((opinc / workingcapital) / marketcap).rolling(63).median().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc008_63d_3rd_v008_signal'] = f62ds_f62_dividend_sustainability_calc008_63d_3rd_v008_signal

def f62ds_f62_dividend_sustainability_calc009_126d_3rd_v009_signal(gp, ps, sharesbas):
    return ((gp / sharesbas) + ps).rolling(126).std().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc009_126d_3rd_v009_signal'] = f62ds_f62_dividend_sustainability_calc009_126d_3rd_v009_signal

def f62ds_f62_dividend_sustainability_calc010_126d_3rd_v010_signal(closeadj, ncff):
    return (closeadj + ncff).rolling(126).min().pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc010_126d_3rd_v010_signal'] = f62ds_f62_dividend_sustainability_calc010_126d_3rd_v010_signal

def f62ds_f62_dividend_sustainability_calc011_63d_3rd_v011_signal(capex, ev, marketcap):
    return ((ev * marketcap) * capex).rolling(63).std().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc011_63d_3rd_v011_signal'] = f62ds_f62_dividend_sustainability_calc011_63d_3rd_v011_signal

def f62ds_f62_dividend_sustainability_calc012_5d_3rd_v012_signal(netinc, sharesbas):
    return (netinc * sharesbas).rolling(5).var().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc012_5d_3rd_v012_signal'] = f62ds_f62_dividend_sustainability_calc012_5d_3rd_v012_signal

def f62ds_f62_dividend_sustainability_calc013_504d_3rd_v013_signal(low, opinc, ps):
    return ((ps + low) + opinc).rolling(504).kurt().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc013_504d_3rd_v013_signal'] = f62ds_f62_dividend_sustainability_calc013_504d_3rd_v013_signal

def f62ds_f62_dividend_sustainability_calc014_21d_3rd_v014_signal(assets):
    return assets.rolling(21).median().pct_change(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc014_21d_3rd_v014_signal'] = f62ds_f62_dividend_sustainability_calc014_21d_3rd_v014_signal

def f62ds_f62_dividend_sustainability_calc015_10d_3rd_v015_signal(equity, sharesbas):
    return (equity + sharesbas).rolling(10).var().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc015_10d_3rd_v015_signal'] = f62ds_f62_dividend_sustainability_calc015_10d_3rd_v015_signal

def f62ds_f62_dividend_sustainability_calc016_126d_3rd_v016_signal(close, low):
    return (low - close).rolling(126).var().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc016_126d_3rd_v016_signal'] = f62ds_f62_dividend_sustainability_calc016_126d_3rd_v016_signal

def f62ds_f62_dividend_sustainability_calc017_21d_3rd_v017_signal(gp, netinc):
    return (gp + netinc).rolling(21).mean().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc017_21d_3rd_v017_signal'] = f62ds_f62_dividend_sustainability_calc017_21d_3rd_v017_signal

def f62ds_f62_dividend_sustainability_calc018_63d_3rd_v018_signal(evebit, gp, open):
    return ((open + gp) - evebit).rolling(63).std().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc018_63d_3rd_v018_signal'] = f62ds_f62_dividend_sustainability_calc018_63d_3rd_v018_signal

def f62ds_f62_dividend_sustainability_calc019_42d_3rd_v019_signal(gp, ncfo):
    return (gp * ncfo).rolling(42).rank().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc019_42d_3rd_v019_signal'] = f62ds_f62_dividend_sustainability_calc019_42d_3rd_v019_signal

def f62ds_f62_dividend_sustainability_calc020_42d_3rd_v020_signal(currentratio, ev, evebit):
    return ((ev - evebit) - currentratio).rolling(42).min().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc020_42d_3rd_v020_signal'] = f62ds_f62_dividend_sustainability_calc020_42d_3rd_v020_signal

def f62ds_f62_dividend_sustainability_calc021_10d_3rd_v021_signal(ev, evebit, netinc):
    return ((evebit - netinc) + ev).rolling(10).min().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc021_10d_3rd_v021_signal'] = f62ds_f62_dividend_sustainability_calc021_10d_3rd_v021_signal

def f62ds_f62_dividend_sustainability_calc022_126d_3rd_v022_signal(evebit, gp, ps):
    return ((ps + evebit) / gp).rolling(126).min().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc022_126d_3rd_v022_signal'] = f62ds_f62_dividend_sustainability_calc022_126d_3rd_v022_signal

def f62ds_f62_dividend_sustainability_calc023_252d_3rd_v023_signal(taxexp):
    return taxexp.rolling(252).min().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc023_252d_3rd_v023_signal'] = f62ds_f62_dividend_sustainability_calc023_252d_3rd_v023_signal

def f62ds_f62_dividend_sustainability_calc024_5d_3rd_v024_signal(currentratio, ncfi, sharesbas):
    return ((sharesbas + ncfi) - currentratio).rolling(5).skew().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc024_5d_3rd_v024_signal'] = f62ds_f62_dividend_sustainability_calc024_5d_3rd_v024_signal

def f62ds_f62_dividend_sustainability_calc025_5d_3rd_v025_signal(high):
    return high.rolling(5).var().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc025_5d_3rd_v025_signal'] = f62ds_f62_dividend_sustainability_calc025_5d_3rd_v025_signal

def f62ds_f62_dividend_sustainability_calc026_126d_3rd_v026_signal(ebitda, ev, pb):
    return ((pb * ev) - ebitda).rolling(126).max().pct_change(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc026_126d_3rd_v026_signal'] = f62ds_f62_dividend_sustainability_calc026_126d_3rd_v026_signal

def f62ds_f62_dividend_sustainability_calc027_5d_3rd_v027_signal(debt, equity):
    return (equity / debt).rolling(5).std().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc027_5d_3rd_v027_signal'] = f62ds_f62_dividend_sustainability_calc027_5d_3rd_v027_signal

def f62ds_f62_dividend_sustainability_calc028_504d_3rd_v028_signal(equity, open):
    return (open - equity).rolling(504).median().pct_change(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc028_504d_3rd_v028_signal'] = f62ds_f62_dividend_sustainability_calc028_504d_3rd_v028_signal

def f62ds_f62_dividend_sustainability_calc029_10d_3rd_v029_signal(intexp, opinc):
    return (intexp * opinc).rolling(10).std().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc029_10d_3rd_v029_signal'] = f62ds_f62_dividend_sustainability_calc029_10d_3rd_v029_signal

def f62ds_f62_dividend_sustainability_calc030_252d_3rd_v030_signal(close, ps):
    return (close / ps).rolling(252).std().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc030_252d_3rd_v030_signal'] = f62ds_f62_dividend_sustainability_calc030_252d_3rd_v030_signal

def f62ds_f62_dividend_sustainability_calc031_42d_3rd_v031_signal(capex, ps):
    return (ps - capex).rolling(42).mean().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc031_42d_3rd_v031_signal'] = f62ds_f62_dividend_sustainability_calc031_42d_3rd_v031_signal

def f62ds_f62_dividend_sustainability_calc032_5d_3rd_v032_signal(evebit, low):
    return (evebit * low).rolling(5).min().pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc032_5d_3rd_v032_signal'] = f62ds_f62_dividend_sustainability_calc032_5d_3rd_v032_signal

def f62ds_f62_dividend_sustainability_calc033_42d_3rd_v033_signal(evebit, intexp, liabilities):
    return ((liabilities * intexp) + evebit).rolling(42).rank().pct_change(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc033_42d_3rd_v033_signal'] = f62ds_f62_dividend_sustainability_calc033_42d_3rd_v033_signal

def f62ds_f62_dividend_sustainability_calc034_63d_3rd_v034_signal(open, opinc):
    return (open / opinc).rolling(63).kurt().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc034_63d_3rd_v034_signal'] = f62ds_f62_dividend_sustainability_calc034_63d_3rd_v034_signal

def f62ds_f62_dividend_sustainability_calc035_126d_3rd_v035_signal(marketcap):
    return marketcap.rolling(126).skew().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc035_126d_3rd_v035_signal'] = f62ds_f62_dividend_sustainability_calc035_126d_3rd_v035_signal

def f62ds_f62_dividend_sustainability_calc036_126d_3rd_v036_signal(open):
    return open.rolling(126).var().diff(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc036_126d_3rd_v036_signal'] = f62ds_f62_dividend_sustainability_calc036_126d_3rd_v036_signal

def f62ds_f62_dividend_sustainability_calc037_252d_3rd_v037_signal(assets, ncff):
    return (assets - ncff).rolling(252).std().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc037_252d_3rd_v037_signal'] = f62ds_f62_dividend_sustainability_calc037_252d_3rd_v037_signal

def f62ds_f62_dividend_sustainability_calc038_63d_3rd_v038_signal(ncff, ncfo, workingcapital):
    return ((ncfo * ncff) / workingcapital).rolling(63).max().pct_change(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc038_63d_3rd_v038_signal'] = f62ds_f62_dividend_sustainability_calc038_63d_3rd_v038_signal

def f62ds_f62_dividend_sustainability_calc039_10d_3rd_v039_signal(retearn, revenue):
    return (retearn * revenue).rolling(10).std().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc039_10d_3rd_v039_signal'] = f62ds_f62_dividend_sustainability_calc039_10d_3rd_v039_signal

def f62ds_f62_dividend_sustainability_calc040_10d_3rd_v040_signal(eps, netinc):
    return (netinc / eps).rolling(10).rank().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc040_10d_3rd_v040_signal'] = f62ds_f62_dividend_sustainability_calc040_10d_3rd_v040_signal

def f62ds_f62_dividend_sustainability_calc041_42d_3rd_v041_signal(pb, sharesbas):
    return (pb / sharesbas).rolling(42).median().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc041_42d_3rd_v041_signal'] = f62ds_f62_dividend_sustainability_calc041_42d_3rd_v041_signal

def f62ds_f62_dividend_sustainability_calc042_21d_3rd_v042_signal(ebitda, open, volume):
    return ((ebitda + volume) - open).rolling(21).std().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc042_21d_3rd_v042_signal'] = f62ds_f62_dividend_sustainability_calc042_21d_3rd_v042_signal

def f62ds_f62_dividend_sustainability_calc043_5d_3rd_v043_signal(ev, evebit):
    return (ev + evebit).rolling(5).kurt().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc043_5d_3rd_v043_signal'] = f62ds_f62_dividend_sustainability_calc043_5d_3rd_v043_signal

def f62ds_f62_dividend_sustainability_calc044_21d_3rd_v044_signal(debt, marketcap):
    return (marketcap - debt).rolling(21).max().diff(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc044_21d_3rd_v044_signal'] = f62ds_f62_dividend_sustainability_calc044_21d_3rd_v044_signal

def f62ds_f62_dividend_sustainability_calc045_63d_3rd_v045_signal(marketcap):
    return marketcap.rolling(63).skew().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc045_63d_3rd_v045_signal'] = f62ds_f62_dividend_sustainability_calc045_63d_3rd_v045_signal

def f62ds_f62_dividend_sustainability_calc046_126d_3rd_v046_signal(fcf, intexp):
    return (intexp / fcf).rolling(126).mean().diff(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc046_126d_3rd_v046_signal'] = f62ds_f62_dividend_sustainability_calc046_126d_3rd_v046_signal

def f62ds_f62_dividend_sustainability_calc047_504d_3rd_v047_signal(eps, pe):
    return (pe / eps).rolling(504).skew().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc047_504d_3rd_v047_signal'] = f62ds_f62_dividend_sustainability_calc047_504d_3rd_v047_signal

def f62ds_f62_dividend_sustainability_calc048_5d_3rd_v048_signal(capex, sharesbas, taxexp):
    return ((capex / taxexp) + sharesbas).rolling(5).skew().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc048_5d_3rd_v048_signal'] = f62ds_f62_dividend_sustainability_calc048_5d_3rd_v048_signal

def f62ds_f62_dividend_sustainability_calc049_63d_3rd_v049_signal(capex, ncff):
    return (capex + ncff).rolling(63).median().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc049_63d_3rd_v049_signal'] = f62ds_f62_dividend_sustainability_calc049_63d_3rd_v049_signal

def f62ds_f62_dividend_sustainability_calc050_126d_3rd_v050_signal(evebitda, ncfo):
    return (ncfo / evebitda).rolling(126).skew().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc050_126d_3rd_v050_signal'] = f62ds_f62_dividend_sustainability_calc050_126d_3rd_v050_signal

def f62ds_f62_dividend_sustainability_calc051_126d_3rd_v051_signal(evebitda, pb, pe):
    return ((evebitda + pe) - pb).rolling(126).mean().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc051_126d_3rd_v051_signal'] = f62ds_f62_dividend_sustainability_calc051_126d_3rd_v051_signal

def f62ds_f62_dividend_sustainability_calc052_5d_3rd_v052_signal(capex, pe):
    return (pe - capex).rolling(5).rank().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc052_5d_3rd_v052_signal'] = f62ds_f62_dividend_sustainability_calc052_5d_3rd_v052_signal

def f62ds_f62_dividend_sustainability_calc053_126d_3rd_v053_signal(ev):
    return ev.rolling(126).kurt().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc053_126d_3rd_v053_signal'] = f62ds_f62_dividend_sustainability_calc053_126d_3rd_v053_signal

def f62ds_f62_dividend_sustainability_calc054_252d_3rd_v054_signal(evebitda):
    return evebitda.rolling(252).var().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc054_252d_3rd_v054_signal'] = f62ds_f62_dividend_sustainability_calc054_252d_3rd_v054_signal

def f62ds_f62_dividend_sustainability_calc055_5d_3rd_v055_signal(pe, workingcapital):
    return (pe - workingcapital).rolling(5).skew().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc055_5d_3rd_v055_signal'] = f62ds_f62_dividend_sustainability_calc055_5d_3rd_v055_signal

def f62ds_f62_dividend_sustainability_calc056_504d_3rd_v056_signal(high, low):
    return (high / low).rolling(504).median().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc056_504d_3rd_v056_signal'] = f62ds_f62_dividend_sustainability_calc056_504d_3rd_v056_signal

def f62ds_f62_dividend_sustainability_calc057_504d_3rd_v057_signal(revenue, volume):
    return (volume + revenue).rolling(504).median().pct_change(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc057_504d_3rd_v057_signal'] = f62ds_f62_dividend_sustainability_calc057_504d_3rd_v057_signal

def f62ds_f62_dividend_sustainability_calc058_504d_3rd_v058_signal(capex, evebit, gp):
    return ((evebit / gp) / capex).rolling(504).median().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc058_504d_3rd_v058_signal'] = f62ds_f62_dividend_sustainability_calc058_504d_3rd_v058_signal

def f62ds_f62_dividend_sustainability_calc059_5d_3rd_v059_signal(ev, intexp, low):
    return ((intexp / ev) * low).rolling(5).min().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc059_5d_3rd_v059_signal'] = f62ds_f62_dividend_sustainability_calc059_5d_3rd_v059_signal

def f62ds_f62_dividend_sustainability_calc060_21d_3rd_v060_signal(liabilities, sharesbas):
    return (liabilities / sharesbas).rolling(21).kurt().pct_change(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc060_21d_3rd_v060_signal'] = f62ds_f62_dividend_sustainability_calc060_21d_3rd_v060_signal

def f62ds_f62_dividend_sustainability_calc061_504d_3rd_v061_signal(pe, retearn):
    return (retearn * pe).rolling(504).skew().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc061_504d_3rd_v061_signal'] = f62ds_f62_dividend_sustainability_calc061_504d_3rd_v061_signal

def f62ds_f62_dividend_sustainability_calc062_126d_3rd_v062_signal(ev, fcf):
    return (fcf / ev).rolling(126).var().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc062_126d_3rd_v062_signal'] = f62ds_f62_dividend_sustainability_calc062_126d_3rd_v062_signal

def f62ds_f62_dividend_sustainability_calc063_252d_3rd_v063_signal(fcf, high):
    return (fcf - high).rolling(252).rank().pct_change(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc063_252d_3rd_v063_signal'] = f62ds_f62_dividend_sustainability_calc063_252d_3rd_v063_signal

def f62ds_f62_dividend_sustainability_calc064_252d_3rd_v064_signal(equity, revenue):
    return (revenue / equity).rolling(252).var().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc064_252d_3rd_v064_signal'] = f62ds_f62_dividend_sustainability_calc064_252d_3rd_v064_signal

def f62ds_f62_dividend_sustainability_calc065_42d_3rd_v065_signal(eps):
    return eps.rolling(42).skew().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc065_42d_3rd_v065_signal'] = f62ds_f62_dividend_sustainability_calc065_42d_3rd_v065_signal

def f62ds_f62_dividend_sustainability_calc066_21d_3rd_v066_signal(assets):
    return assets.rolling(21).var().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc066_21d_3rd_v066_signal'] = f62ds_f62_dividend_sustainability_calc066_21d_3rd_v066_signal

def f62ds_f62_dividend_sustainability_calc067_42d_3rd_v067_signal(intexp, pe, workingcapital):
    return ((workingcapital * intexp) * pe).rolling(42).kurt().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc067_42d_3rd_v067_signal'] = f62ds_f62_dividend_sustainability_calc067_42d_3rd_v067_signal

def f62ds_f62_dividend_sustainability_calc068_10d_3rd_v068_signal(capex, sharesbas):
    return (capex * sharesbas).rolling(10).min().pct_change(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc068_10d_3rd_v068_signal'] = f62ds_f62_dividend_sustainability_calc068_10d_3rd_v068_signal

def f62ds_f62_dividend_sustainability_calc069_252d_3rd_v069_signal(volume, workingcapital):
    return (volume + workingcapital).rolling(252).skew().pct_change(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc069_252d_3rd_v069_signal'] = f62ds_f62_dividend_sustainability_calc069_252d_3rd_v069_signal

def f62ds_f62_dividend_sustainability_calc070_10d_3rd_v070_signal(fcf):
    return fcf.rolling(10).var().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc070_10d_3rd_v070_signal'] = f62ds_f62_dividend_sustainability_calc070_10d_3rd_v070_signal

def f62ds_f62_dividend_sustainability_calc071_63d_3rd_v071_signal(currentratio, debt):
    return (debt + currentratio).rolling(63).skew().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc071_63d_3rd_v071_signal'] = f62ds_f62_dividend_sustainability_calc071_63d_3rd_v071_signal

def f62ds_f62_dividend_sustainability_calc072_21d_3rd_v072_signal(pe):
    return pe.rolling(21).mean().pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc072_21d_3rd_v072_signal'] = f62ds_f62_dividend_sustainability_calc072_21d_3rd_v072_signal

def f62ds_f62_dividend_sustainability_calc073_10d_3rd_v073_signal(low):
    return low.rolling(10).min().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc073_10d_3rd_v073_signal'] = f62ds_f62_dividend_sustainability_calc073_10d_3rd_v073_signal

def f62ds_f62_dividend_sustainability_calc074_10d_3rd_v074_signal(equity, taxexp):
    return (taxexp / equity).rolling(10).min().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc074_10d_3rd_v074_signal'] = f62ds_f62_dividend_sustainability_calc074_10d_3rd_v074_signal

def f62ds_f62_dividend_sustainability_calc075_5d_3rd_v075_signal(gp, ps, workingcapital):
    return ((workingcapital + gp) * ps).rolling(5).min().diff(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc075_5d_3rd_v075_signal'] = f62ds_f62_dividend_sustainability_calc075_5d_3rd_v075_signal

def f62ds_f62_dividend_sustainability_calc076_21d_3rd_v076_signal(equity, evebitda, ncff):
    return ((ncff / equity) * evebitda).rolling(21).max().diff(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc076_21d_3rd_v076_signal'] = f62ds_f62_dividend_sustainability_calc076_21d_3rd_v076_signal

def f62ds_f62_dividend_sustainability_calc077_5d_3rd_v077_signal(pb):
    return pb.rolling(5).median().diff(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc077_5d_3rd_v077_signal'] = f62ds_f62_dividend_sustainability_calc077_5d_3rd_v077_signal

def f62ds_f62_dividend_sustainability_calc078_21d_3rd_v078_signal(evebitda, opinc):
    return (opinc - evebitda).rolling(21).max().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc078_21d_3rd_v078_signal'] = f62ds_f62_dividend_sustainability_calc078_21d_3rd_v078_signal

def f62ds_f62_dividend_sustainability_calc079_21d_3rd_v079_signal(capex, ncfo):
    return (capex / ncfo).rolling(21).min().pct_change(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc079_21d_3rd_v079_signal'] = f62ds_f62_dividend_sustainability_calc079_21d_3rd_v079_signal

def f62ds_f62_dividend_sustainability_calc080_10d_3rd_v080_signal(liabilities, pb):
    return (pb + liabilities).rolling(10).min().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc080_10d_3rd_v080_signal'] = f62ds_f62_dividend_sustainability_calc080_10d_3rd_v080_signal

def f62ds_f62_dividend_sustainability_calc081_252d_3rd_v081_signal(low):
    return low.rolling(252).max().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc081_252d_3rd_v081_signal'] = f62ds_f62_dividend_sustainability_calc081_252d_3rd_v081_signal

def f62ds_f62_dividend_sustainability_calc082_504d_3rd_v082_signal(equity, retearn):
    return (retearn + equity).rolling(504).skew().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc082_504d_3rd_v082_signal'] = f62ds_f62_dividend_sustainability_calc082_504d_3rd_v082_signal

def f62ds_f62_dividend_sustainability_calc083_252d_3rd_v083_signal(assets, close):
    return (close * assets).rolling(252).var().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc083_252d_3rd_v083_signal'] = f62ds_f62_dividend_sustainability_calc083_252d_3rd_v083_signal

def f62ds_f62_dividend_sustainability_calc084_10d_3rd_v084_signal(assets, ncfi, ncfo):
    return ((ncfi * assets) / ncfo).rolling(10).kurt().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc084_10d_3rd_v084_signal'] = f62ds_f62_dividend_sustainability_calc084_10d_3rd_v084_signal

def f62ds_f62_dividend_sustainability_calc085_5d_3rd_v085_signal(closeadj, ncff):
    return (closeadj / ncff).rolling(5).rank().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc085_5d_3rd_v085_signal'] = f62ds_f62_dividend_sustainability_calc085_5d_3rd_v085_signal

def f62ds_f62_dividend_sustainability_calc086_21d_3rd_v086_signal(ncfi, ps, volume):
    return ((ncfi / ps) * volume).rolling(21).rank().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc086_21d_3rd_v086_signal'] = f62ds_f62_dividend_sustainability_calc086_21d_3rd_v086_signal

def f62ds_f62_dividend_sustainability_calc087_252d_3rd_v087_signal(fcf, pb):
    return (fcf + pb).rolling(252).max().pct_change(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc087_252d_3rd_v087_signal'] = f62ds_f62_dividend_sustainability_calc087_252d_3rd_v087_signal

def f62ds_f62_dividend_sustainability_calc088_504d_3rd_v088_signal(currentratio, eps, ev):
    return ((ev + eps) / currentratio).rolling(504).median().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc088_504d_3rd_v088_signal'] = f62ds_f62_dividend_sustainability_calc088_504d_3rd_v088_signal

def f62ds_f62_dividend_sustainability_calc089_10d_3rd_v089_signal(ncfi, retearn):
    return (ncfi * retearn).rolling(10).skew().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc089_10d_3rd_v089_signal'] = f62ds_f62_dividend_sustainability_calc089_10d_3rd_v089_signal

def f62ds_f62_dividend_sustainability_calc090_42d_3rd_v090_signal(debt, eps, ev):
    return ((ev * debt) / eps).rolling(42).std().pct_change(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc090_42d_3rd_v090_signal'] = f62ds_f62_dividend_sustainability_calc090_42d_3rd_v090_signal

def f62ds_f62_dividend_sustainability_calc091_5d_3rd_v091_signal(pb, ps):
    return (ps + pb).rolling(5).rank().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc091_5d_3rd_v091_signal'] = f62ds_f62_dividend_sustainability_calc091_5d_3rd_v091_signal

def f62ds_f62_dividend_sustainability_calc092_5d_3rd_v092_signal(assets, ps, volume):
    return ((volume / ps) + assets).rolling(5).max().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc092_5d_3rd_v092_signal'] = f62ds_f62_dividend_sustainability_calc092_5d_3rd_v092_signal

def f62ds_f62_dividend_sustainability_calc093_5d_3rd_v093_signal(high, open):
    return (high - open).rolling(5).kurt().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc093_5d_3rd_v093_signal'] = f62ds_f62_dividend_sustainability_calc093_5d_3rd_v093_signal

def f62ds_f62_dividend_sustainability_calc094_42d_3rd_v094_signal(eps, ps):
    return (eps - ps).rolling(42).rank().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc094_42d_3rd_v094_signal'] = f62ds_f62_dividend_sustainability_calc094_42d_3rd_v094_signal

def f62ds_f62_dividend_sustainability_calc095_10d_3rd_v095_signal(evebitda):
    return evebitda.rolling(10).var().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc095_10d_3rd_v095_signal'] = f62ds_f62_dividend_sustainability_calc095_10d_3rd_v095_signal

def f62ds_f62_dividend_sustainability_calc096_252d_3rd_v096_signal(capex, ncfi):
    return (ncfi - capex).rolling(252).rank().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc096_252d_3rd_v096_signal'] = f62ds_f62_dividend_sustainability_calc096_252d_3rd_v096_signal

def f62ds_f62_dividend_sustainability_calc097_10d_3rd_v097_signal(low, ncfo, open):
    return ((low - ncfo) / open).rolling(10).mean().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc097_10d_3rd_v097_signal'] = f62ds_f62_dividend_sustainability_calc097_10d_3rd_v097_signal

def f62ds_f62_dividend_sustainability_calc098_21d_3rd_v098_signal(sharesbas):
    return sharesbas.rolling(21).kurt().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc098_21d_3rd_v098_signal'] = f62ds_f62_dividend_sustainability_calc098_21d_3rd_v098_signal

def f62ds_f62_dividend_sustainability_calc099_252d_3rd_v099_signal(assets, capex, liabilities):
    return ((capex * assets) + liabilities).rolling(252).mean().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc099_252d_3rd_v099_signal'] = f62ds_f62_dividend_sustainability_calc099_252d_3rd_v099_signal

def f62ds_f62_dividend_sustainability_calc100_10d_3rd_v100_signal(assets, fcf, netinc):
    return ((netinc - fcf) / assets).rolling(10).min().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc100_10d_3rd_v100_signal'] = f62ds_f62_dividend_sustainability_calc100_10d_3rd_v100_signal

def f62ds_f62_dividend_sustainability_calc101_5d_3rd_v101_signal(low, retearn):
    return (retearn * low).rolling(5).std().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc101_5d_3rd_v101_signal'] = f62ds_f62_dividend_sustainability_calc101_5d_3rd_v101_signal

def f62ds_f62_dividend_sustainability_calc102_42d_3rd_v102_signal(capex, ps, workingcapital):
    return ((ps / capex) * workingcapital).rolling(42).std().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc102_42d_3rd_v102_signal'] = f62ds_f62_dividend_sustainability_calc102_42d_3rd_v102_signal

def f62ds_f62_dividend_sustainability_calc103_504d_3rd_v103_signal(gp, opinc):
    return (opinc * gp).rolling(504).max().diff(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc103_504d_3rd_v103_signal'] = f62ds_f62_dividend_sustainability_calc103_504d_3rd_v103_signal

def f62ds_f62_dividend_sustainability_calc104_504d_3rd_v104_signal(ncff, ncfo, retearn):
    return ((retearn + ncff) / ncfo).rolling(504).kurt().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc104_504d_3rd_v104_signal'] = f62ds_f62_dividend_sustainability_calc104_504d_3rd_v104_signal

def f62ds_f62_dividend_sustainability_calc105_21d_3rd_v105_signal(eps, fcf, pe):
    return ((fcf + eps) / pe).rolling(21).std().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc105_21d_3rd_v105_signal'] = f62ds_f62_dividend_sustainability_calc105_21d_3rd_v105_signal

def f62ds_f62_dividend_sustainability_calc106_252d_3rd_v106_signal(ebitda, evebitda):
    return (evebitda * ebitda).rolling(252).skew().diff(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc106_252d_3rd_v106_signal'] = f62ds_f62_dividend_sustainability_calc106_252d_3rd_v106_signal

def f62ds_f62_dividend_sustainability_calc107_504d_3rd_v107_signal(fcf, pe):
    return (pe / fcf).rolling(504).rank().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc107_504d_3rd_v107_signal'] = f62ds_f62_dividend_sustainability_calc107_504d_3rd_v107_signal

def f62ds_f62_dividend_sustainability_calc108_42d_3rd_v108_signal(fcf, liabilities):
    return (fcf / liabilities).rolling(42).median().pct_change(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc108_42d_3rd_v108_signal'] = f62ds_f62_dividend_sustainability_calc108_42d_3rd_v108_signal

def f62ds_f62_dividend_sustainability_calc109_42d_3rd_v109_signal(equity, opinc):
    return (opinc - equity).rolling(42).var().diff(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc109_42d_3rd_v109_signal'] = f62ds_f62_dividend_sustainability_calc109_42d_3rd_v109_signal

def f62ds_f62_dividend_sustainability_calc110_252d_3rd_v110_signal(close, eps, pb):
    return ((eps - pb) + close).rolling(252).skew().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc110_252d_3rd_v110_signal'] = f62ds_f62_dividend_sustainability_calc110_252d_3rd_v110_signal

def f62ds_f62_dividend_sustainability_calc111_504d_3rd_v111_signal(ebitda):
    return ebitda.rolling(504).min().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc111_504d_3rd_v111_signal'] = f62ds_f62_dividend_sustainability_calc111_504d_3rd_v111_signal

def f62ds_f62_dividend_sustainability_calc112_5d_3rd_v112_signal(ebitda, eps):
    return (eps + ebitda).rolling(5).mean().diff(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc112_5d_3rd_v112_signal'] = f62ds_f62_dividend_sustainability_calc112_5d_3rd_v112_signal

def f62ds_f62_dividend_sustainability_calc113_504d_3rd_v113_signal(gp, netinc):
    return (gp + netinc).rolling(504).std().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc113_504d_3rd_v113_signal'] = f62ds_f62_dividend_sustainability_calc113_504d_3rd_v113_signal

def f62ds_f62_dividend_sustainability_calc114_504d_3rd_v114_signal(equity, opinc):
    return (equity - opinc).rolling(504).mean().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc114_504d_3rd_v114_signal'] = f62ds_f62_dividend_sustainability_calc114_504d_3rd_v114_signal

def f62ds_f62_dividend_sustainability_calc115_42d_3rd_v115_signal(capex, ps, volume):
    return ((capex / ps) / volume).rolling(42).rank().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc115_42d_3rd_v115_signal'] = f62ds_f62_dividend_sustainability_calc115_42d_3rd_v115_signal

def f62ds_f62_dividend_sustainability_calc116_10d_3rd_v116_signal(ev, ncfo, ps):
    return ((ps / ncfo) / ev).rolling(10).skew().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc116_10d_3rd_v116_signal'] = f62ds_f62_dividend_sustainability_calc116_10d_3rd_v116_signal

def f62ds_f62_dividend_sustainability_calc117_126d_3rd_v117_signal(gp, pb):
    return (pb * gp).rolling(126).rank().pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc117_126d_3rd_v117_signal'] = f62ds_f62_dividend_sustainability_calc117_126d_3rd_v117_signal

def f62ds_f62_dividend_sustainability_calc118_63d_3rd_v118_signal(assets, sharesbas):
    return (sharesbas - assets).rolling(63).rank().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc118_63d_3rd_v118_signal'] = f62ds_f62_dividend_sustainability_calc118_63d_3rd_v118_signal

def f62ds_f62_dividend_sustainability_calc119_126d_3rd_v119_signal(equity, low):
    return (low + equity).rolling(126).min().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc119_126d_3rd_v119_signal'] = f62ds_f62_dividend_sustainability_calc119_126d_3rd_v119_signal

def f62ds_f62_dividend_sustainability_calc120_63d_3rd_v120_signal(evebit, retearn, revenue):
    return ((revenue - retearn) - evebit).rolling(63).mean().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc120_63d_3rd_v120_signal'] = f62ds_f62_dividend_sustainability_calc120_63d_3rd_v120_signal

def f62ds_f62_dividend_sustainability_calc121_63d_3rd_v121_signal(evebit, revenue):
    return (evebit * revenue).rolling(63).max().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc121_63d_3rd_v121_signal'] = f62ds_f62_dividend_sustainability_calc121_63d_3rd_v121_signal

def f62ds_f62_dividend_sustainability_calc122_63d_3rd_v122_signal(ev, ncfo):
    return (ev * ncfo).rolling(63).var().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc122_63d_3rd_v122_signal'] = f62ds_f62_dividend_sustainability_calc122_63d_3rd_v122_signal

def f62ds_f62_dividend_sustainability_calc123_42d_3rd_v123_signal(assets):
    return assets.rolling(42).rank().pct_change(5).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc123_42d_3rd_v123_signal'] = f62ds_f62_dividend_sustainability_calc123_42d_3rd_v123_signal

def f62ds_f62_dividend_sustainability_calc124_10d_3rd_v124_signal(workingcapital):
    return workingcapital.rolling(10).std().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc124_10d_3rd_v124_signal'] = f62ds_f62_dividend_sustainability_calc124_10d_3rd_v124_signal

def f62ds_f62_dividend_sustainability_calc125_252d_3rd_v125_signal(eps, opinc, volume):
    return ((opinc * volume) * eps).rolling(252).skew().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc125_252d_3rd_v125_signal'] = f62ds_f62_dividend_sustainability_calc125_252d_3rd_v125_signal

def f62ds_f62_dividend_sustainability_calc126_126d_3rd_v126_signal(ev, gp):
    return (gp - ev).rolling(126).median().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc126_126d_3rd_v126_signal'] = f62ds_f62_dividend_sustainability_calc126_126d_3rd_v126_signal

def f62ds_f62_dividend_sustainability_calc127_5d_3rd_v127_signal(debt):
    return debt.rolling(5).var().pct_change(1).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc127_5d_3rd_v127_signal'] = f62ds_f62_dividend_sustainability_calc127_5d_3rd_v127_signal

def f62ds_f62_dividend_sustainability_calc128_21d_3rd_v128_signal(close, high, opinc):
    return ((opinc * high) / close).rolling(21).std().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc128_21d_3rd_v128_signal'] = f62ds_f62_dividend_sustainability_calc128_21d_3rd_v128_signal

def f62ds_f62_dividend_sustainability_calc129_10d_3rd_v129_signal(capex, currentratio, ncfo):
    return ((capex / ncfo) - currentratio).rolling(10).var().pct_change(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc129_10d_3rd_v129_signal'] = f62ds_f62_dividend_sustainability_calc129_10d_3rd_v129_signal

def f62ds_f62_dividend_sustainability_calc130_5d_3rd_v130_signal(ebitda, pb, revenue):
    return ((revenue / ebitda) + pb).rolling(5).median().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc130_5d_3rd_v130_signal'] = f62ds_f62_dividend_sustainability_calc130_5d_3rd_v130_signal

def f62ds_f62_dividend_sustainability_calc131_10d_3rd_v131_signal(open, pe, ps):
    return ((pe * ps) - open).rolling(10).median().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc131_10d_3rd_v131_signal'] = f62ds_f62_dividend_sustainability_calc131_10d_3rd_v131_signal

def f62ds_f62_dividend_sustainability_calc132_63d_3rd_v132_signal(currentratio, evebitda, gp):
    return ((gp * evebitda) / currentratio).rolling(63).rank().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc132_63d_3rd_v132_signal'] = f62ds_f62_dividend_sustainability_calc132_63d_3rd_v132_signal

def f62ds_f62_dividend_sustainability_calc133_126d_3rd_v133_signal(assets, close):
    return (close + assets).rolling(126).kurt().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc133_126d_3rd_v133_signal'] = f62ds_f62_dividend_sustainability_calc133_126d_3rd_v133_signal

def f62ds_f62_dividend_sustainability_calc134_5d_3rd_v134_signal(ncff):
    return ncff.rolling(5).max().pct_change(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc134_5d_3rd_v134_signal'] = f62ds_f62_dividend_sustainability_calc134_5d_3rd_v134_signal

def f62ds_f62_dividend_sustainability_calc135_5d_3rd_v135_signal(ebitda, opinc, workingcapital):
    return ((ebitda / opinc) + workingcapital).rolling(5).var().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc135_5d_3rd_v135_signal'] = f62ds_f62_dividend_sustainability_calc135_5d_3rd_v135_signal

def f62ds_f62_dividend_sustainability_calc136_63d_3rd_v136_signal(retearn):
    return retearn.rolling(63).median().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc136_63d_3rd_v136_signal'] = f62ds_f62_dividend_sustainability_calc136_63d_3rd_v136_signal

def f62ds_f62_dividend_sustainability_calc137_21d_3rd_v137_signal(gp, ncfo, netinc):
    return ((netinc * gp) * ncfo).rolling(21).min().diff(1).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc137_21d_3rd_v137_signal'] = f62ds_f62_dividend_sustainability_calc137_21d_3rd_v137_signal

def f62ds_f62_dividend_sustainability_calc138_5d_3rd_v138_signal(assets, intexp):
    return (assets - intexp).rolling(5).median().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc138_5d_3rd_v138_signal'] = f62ds_f62_dividend_sustainability_calc138_5d_3rd_v138_signal

def f62ds_f62_dividend_sustainability_calc139_252d_3rd_v139_signal(debt):
    return debt.rolling(252).min().diff(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc139_252d_3rd_v139_signal'] = f62ds_f62_dividend_sustainability_calc139_252d_3rd_v139_signal

def f62ds_f62_dividend_sustainability_calc140_21d_3rd_v140_signal(close, open):
    return (open + close).rolling(21).var().pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc140_21d_3rd_v140_signal'] = f62ds_f62_dividend_sustainability_calc140_21d_3rd_v140_signal

def f62ds_f62_dividend_sustainability_calc141_252d_3rd_v141_signal(fcf, ps):
    return (ps - fcf).rolling(252).std().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc141_252d_3rd_v141_signal'] = f62ds_f62_dividend_sustainability_calc141_252d_3rd_v141_signal

def f62ds_f62_dividend_sustainability_calc142_504d_3rd_v142_signal(opinc, sharesbas):
    return (sharesbas - opinc).rolling(504).skew().diff(2).diff(2).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc142_504d_3rd_v142_signal'] = f62ds_f62_dividend_sustainability_calc142_504d_3rd_v142_signal

def f62ds_f62_dividend_sustainability_calc143_10d_3rd_v143_signal(equity, ncff, ncfo):
    return ((equity + ncfo) - ncff).rolling(10).kurt().diff(2).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc143_10d_3rd_v143_signal'] = f62ds_f62_dividend_sustainability_calc143_10d_3rd_v143_signal

def f62ds_f62_dividend_sustainability_calc144_63d_3rd_v144_signal(revenue, workingcapital):
    return (workingcapital * revenue).rolling(63).max().diff(2).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc144_63d_3rd_v144_signal'] = f62ds_f62_dividend_sustainability_calc144_63d_3rd_v144_signal

def f62ds_f62_dividend_sustainability_calc145_126d_3rd_v145_signal(gp, high, pe):
    return ((high / gp) - pe).rolling(126).mean().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc145_126d_3rd_v145_signal'] = f62ds_f62_dividend_sustainability_calc145_126d_3rd_v145_signal

def f62ds_f62_dividend_sustainability_calc146_252d_3rd_v146_signal(ps, sharesbas):
    return (ps - sharesbas).rolling(252).rank().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc146_252d_3rd_v146_signal'] = f62ds_f62_dividend_sustainability_calc146_252d_3rd_v146_signal

def f62ds_f62_dividend_sustainability_calc147_5d_3rd_v147_signal(close, currentratio):
    return (currentratio + close).rolling(5).skew().diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc147_5d_3rd_v147_signal'] = f62ds_f62_dividend_sustainability_calc147_5d_3rd_v147_signal

def f62ds_f62_dividend_sustainability_calc148_42d_3rd_v148_signal(ev, opinc):
    return (ev / opinc).rolling(42).mean().pct_change(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc148_42d_3rd_v148_signal'] = f62ds_f62_dividend_sustainability_calc148_42d_3rd_v148_signal

def f62ds_f62_dividend_sustainability_calc149_10d_3rd_v149_signal(ncfo, opinc, sharesbas):
    return ((ncfo * opinc) - sharesbas).rolling(10).min().diff(5).diff(1).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc149_10d_3rd_v149_signal'] = f62ds_f62_dividend_sustainability_calc149_10d_3rd_v149_signal

def f62ds_f62_dividend_sustainability_calc150_5d_3rd_v150_signal(intexp, low, workingcapital):
    return ((workingcapital + intexp) - low).rolling(5).std().pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc150_5d_3rd_v150_signal'] = f62ds_f62_dividend_sustainability_calc150_5d_3rd_v150_signal



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
