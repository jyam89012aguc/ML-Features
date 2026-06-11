import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f59fc_f59_fcf_conversion_quality_calc001_5d_base_v001_signal(intexp, debt):
    res = np.log((debt / intexp).abs().replace(0, np.nan)).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc001_5d_base_v001_signal'] = f59fc_f59_fcf_conversion_quality_calc001_5d_base_v001_signal

def f59fc_f59_fcf_conversion_quality_calc002_5d_base_v002_signal(ev, gp, ebitda):
    res = np.log((gp / ebitda).abs().replace(0, np.nan)).rolling(5).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc002_5d_base_v002_signal'] = f59fc_f59_fcf_conversion_quality_calc002_5d_base_v002_signal

def f59fc_f59_fcf_conversion_quality_calc003_126d_base_v003_signal(liabilities, pe):
    res = (pe / liabilities).diff(1).rolling(126).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc003_126d_base_v003_signal'] = f59fc_f59_fcf_conversion_quality_calc003_126d_base_v003_signal

def f59fc_f59_fcf_conversion_quality_calc004_42d_base_v004_signal(netinc, revenue, assets):
    res = (netinc * revenue / assets).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc004_42d_base_v004_signal'] = f59fc_f59_fcf_conversion_quality_calc004_42d_base_v004_signal

def f59fc_f59_fcf_conversion_quality_calc005_252d_base_v005_signal(opinc, evebitda):
    res = np.log((evebitda / opinc).abs().replace(0, np.nan)).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc005_252d_base_v005_signal'] = f59fc_f59_fcf_conversion_quality_calc005_252d_base_v005_signal

def f59fc_f59_fcf_conversion_quality_calc006_21d_base_v006_signal(opinc, pb):
    res = (opinc / pb).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc006_21d_base_v006_signal'] = f59fc_f59_fcf_conversion_quality_calc006_21d_base_v006_signal

def f59fc_f59_fcf_conversion_quality_calc007_5d_base_v007_signal(ncfi, retearn, assets):
    res = (ncfi * retearn / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc007_5d_base_v007_signal'] = f59fc_f59_fcf_conversion_quality_calc007_5d_base_v007_signal

def f59fc_f59_fcf_conversion_quality_calc008_21d_base_v008_signal(ncff, evebit, workingcapital):
    res = (((evebit / ncff) - (evebit / ncff).rolling(21).mean()) / (evebit / ncff).rolling(21).std()).rolling(21).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc008_21d_base_v008_signal'] = f59fc_f59_fcf_conversion_quality_calc008_21d_base_v008_signal

def f59fc_f59_fcf_conversion_quality_calc009_126d_base_v009_signal(fcf, taxexp, ps):
    res = np.log((fcf / ps).abs().replace(0, np.nan)).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc009_126d_base_v009_signal'] = f59fc_f59_fcf_conversion_quality_calc009_126d_base_v009_signal

def f59fc_f59_fcf_conversion_quality_calc010_42d_base_v010_signal(low, assets):
    res = (low * assets / assets).rolling(42).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc010_42d_base_v010_signal'] = f59fc_f59_fcf_conversion_quality_calc010_42d_base_v010_signal

def f59fc_f59_fcf_conversion_quality_calc011_42d_base_v011_signal(low, netinc, ev):
    res = (low / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc011_42d_base_v011_signal'] = f59fc_f59_fcf_conversion_quality_calc011_42d_base_v011_signal

def f59fc_f59_fcf_conversion_quality_calc012_5d_base_v012_signal(opinc, evebit, ncfo):
    res = (ncfo / evebit).diff(1).rolling(5).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc012_5d_base_v012_signal'] = f59fc_f59_fcf_conversion_quality_calc012_5d_base_v012_signal

def f59fc_f59_fcf_conversion_quality_calc013_21d_base_v013_signal(pb, high, assets):
    res = (high * pb / assets).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc013_21d_base_v013_signal'] = f59fc_f59_fcf_conversion_quality_calc013_21d_base_v013_signal

def f59fc_f59_fcf_conversion_quality_calc014_252d_base_v014_signal(evebit, close):
    res = (close / evebit).diff(1).rolling(252).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc014_252d_base_v014_signal'] = f59fc_f59_fcf_conversion_quality_calc014_252d_base_v014_signal

def f59fc_f59_fcf_conversion_quality_calc015_63d_base_v015_signal(low, ps):
    res = (((ps / low) - (ps / low).rolling(63).mean()) / (ps / low).rolling(63).std()).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc015_63d_base_v015_signal'] = f59fc_f59_fcf_conversion_quality_calc015_63d_base_v015_signal

def f59fc_f59_fcf_conversion_quality_calc016_21d_base_v016_signal(volume, ev, high):
    res = (ev / high).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc016_21d_base_v016_signal'] = f59fc_f59_fcf_conversion_quality_calc016_21d_base_v016_signal

def f59fc_f59_fcf_conversion_quality_calc017_252d_base_v017_signal(netinc, pb):
    res = (pb / netinc).diff(1).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc017_252d_base_v017_signal'] = f59fc_f59_fcf_conversion_quality_calc017_252d_base_v017_signal

def f59fc_f59_fcf_conversion_quality_calc018_5d_base_v018_signal(intexp, assets):
    res = (assets * intexp / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc018_5d_base_v018_signal'] = f59fc_f59_fcf_conversion_quality_calc018_5d_base_v018_signal

def f59fc_f59_fcf_conversion_quality_calc019_252d_base_v019_signal(revenue, pe):
    res = (pe / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc019_252d_base_v019_signal'] = f59fc_f59_fcf_conversion_quality_calc019_252d_base_v019_signal

def f59fc_f59_fcf_conversion_quality_calc020_5d_base_v020_signal(retearn, high):
    res = (high / retearn).diff(5).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc020_5d_base_v020_signal'] = f59fc_f59_fcf_conversion_quality_calc020_5d_base_v020_signal

def f59fc_f59_fcf_conversion_quality_calc021_42d_base_v021_signal(retearn, liabilities, assets):
    res = (liabilities * retearn / assets).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc021_42d_base_v021_signal'] = f59fc_f59_fcf_conversion_quality_calc021_42d_base_v021_signal

def f59fc_f59_fcf_conversion_quality_calc022_42d_base_v022_signal(netinc, workingcapital):
    res = (netinc / workingcapital).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc022_42d_base_v022_signal'] = f59fc_f59_fcf_conversion_quality_calc022_42d_base_v022_signal

def f59fc_f59_fcf_conversion_quality_calc023_63d_base_v023_signal(evebit, gp):
    res = np.log((evebit / gp).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc023_63d_base_v023_signal'] = f59fc_f59_fcf_conversion_quality_calc023_63d_base_v023_signal

def f59fc_f59_fcf_conversion_quality_calc024_42d_base_v024_signal(fcf, ncfo, eps):
    res = (eps * fcf / ncfo).rolling(42).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc024_42d_base_v024_signal'] = f59fc_f59_fcf_conversion_quality_calc024_42d_base_v024_signal

def f59fc_f59_fcf_conversion_quality_calc025_10d_base_v025_signal(evebitda, pe):
    res = (((evebitda / pe) - (evebitda / pe).rolling(10).mean()) / (evebitda / pe).rolling(10).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc025_10d_base_v025_signal'] = f59fc_f59_fcf_conversion_quality_calc025_10d_base_v025_signal

def f59fc_f59_fcf_conversion_quality_calc026_126d_base_v026_signal(marketcap, equity):
    res = (marketcap / equity).pct_change(1).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc026_126d_base_v026_signal'] = f59fc_f59_fcf_conversion_quality_calc026_126d_base_v026_signal

def f59fc_f59_fcf_conversion_quality_calc027_21d_base_v027_signal(debt, workingcapital, assets):
    res = (debt * workingcapital / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc027_21d_base_v027_signal'] = f59fc_f59_fcf_conversion_quality_calc027_21d_base_v027_signal

def f59fc_f59_fcf_conversion_quality_calc028_63d_base_v028_signal(sharesbas, revenue):
    res = (sharesbas / revenue).rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc028_63d_base_v028_signal'] = f59fc_f59_fcf_conversion_quality_calc028_63d_base_v028_signal

def f59fc_f59_fcf_conversion_quality_calc029_42d_base_v029_signal(evebit, fcf, ncfo):
    res = (ncfo / evebit).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc029_42d_base_v029_signal'] = f59fc_f59_fcf_conversion_quality_calc029_42d_base_v029_signal

def f59fc_f59_fcf_conversion_quality_calc030_126d_base_v030_signal(ncff, ev, ebitda):
    res = np.log((ncff / ev).abs().replace(0, np.nan)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc030_126d_base_v030_signal'] = f59fc_f59_fcf_conversion_quality_calc030_126d_base_v030_signal

def f59fc_f59_fcf_conversion_quality_calc031_21d_base_v031_signal(closeadj, currentratio):
    res = (currentratio / closeadj)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc031_21d_base_v031_signal'] = f59fc_f59_fcf_conversion_quality_calc031_21d_base_v031_signal

def f59fc_f59_fcf_conversion_quality_calc032_42d_base_v032_signal(sharesbas, open):
    res = (sharesbas / open).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc032_42d_base_v032_signal'] = f59fc_f59_fcf_conversion_quality_calc032_42d_base_v032_signal

def f59fc_f59_fcf_conversion_quality_calc033_5d_base_v033_signal(ev, taxexp, high):
    res = (high * ev / taxexp)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc033_5d_base_v033_signal'] = f59fc_f59_fcf_conversion_quality_calc033_5d_base_v033_signal

def f59fc_f59_fcf_conversion_quality_calc034_21d_base_v034_signal(ncfo, gp):
    res = (ncfo / gp).pct_change(21).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc034_21d_base_v034_signal'] = f59fc_f59_fcf_conversion_quality_calc034_21d_base_v034_signal

def f59fc_f59_fcf_conversion_quality_calc035_21d_base_v035_signal(open, capex):
    res = (open / capex).diff(21).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc035_21d_base_v035_signal'] = f59fc_f59_fcf_conversion_quality_calc035_21d_base_v035_signal

def f59fc_f59_fcf_conversion_quality_calc036_5d_base_v036_signal(currentratio, ebitda):
    res = np.log((ebitda / currentratio).abs().replace(0, np.nan)).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc036_5d_base_v036_signal'] = f59fc_f59_fcf_conversion_quality_calc036_5d_base_v036_signal

def f59fc_f59_fcf_conversion_quality_calc037_5d_base_v037_signal(sharesbas, open):
    res = (((sharesbas / open) - (sharesbas / open).rolling(5).mean()) / (sharesbas / open).rolling(5).std()).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc037_5d_base_v037_signal'] = f59fc_f59_fcf_conversion_quality_calc037_5d_base_v037_signal

def f59fc_f59_fcf_conversion_quality_calc038_21d_base_v038_signal(opinc, debt, assets):
    res = (debt / opinc).pct_change(21).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc038_21d_base_v038_signal'] = f59fc_f59_fcf_conversion_quality_calc038_21d_base_v038_signal

def f59fc_f59_fcf_conversion_quality_calc039_5d_base_v039_signal(liabilities, pb):
    res = (pb / liabilities)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc039_5d_base_v039_signal'] = f59fc_f59_fcf_conversion_quality_calc039_5d_base_v039_signal

def f59fc_f59_fcf_conversion_quality_calc040_5d_base_v040_signal(volume, assets):
    res = (assets / volume)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc040_5d_base_v040_signal'] = f59fc_f59_fcf_conversion_quality_calc040_5d_base_v040_signal

def f59fc_f59_fcf_conversion_quality_calc041_10d_base_v041_signal(ncfo, pe, capex):
    res = (ncfo * capex / pe)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc041_10d_base_v041_signal'] = f59fc_f59_fcf_conversion_quality_calc041_10d_base_v041_signal

def f59fc_f59_fcf_conversion_quality_calc042_252d_base_v042_signal(marketcap, close):
    res = (((marketcap / close) - (marketcap / close).rolling(252).mean()) / (marketcap / close).rolling(252).std()).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc042_252d_base_v042_signal'] = f59fc_f59_fcf_conversion_quality_calc042_252d_base_v042_signal

def f59fc_f59_fcf_conversion_quality_calc043_126d_base_v043_signal(currentratio, gp, ebitda):
    res = (currentratio / ebitda).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc043_126d_base_v043_signal'] = f59fc_f59_fcf_conversion_quality_calc043_126d_base_v043_signal

def f59fc_f59_fcf_conversion_quality_calc044_42d_base_v044_signal(currentratio, pe):
    res = (currentratio / pe).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc044_42d_base_v044_signal'] = f59fc_f59_fcf_conversion_quality_calc044_42d_base_v044_signal

def f59fc_f59_fcf_conversion_quality_calc045_21d_base_v045_signal(pb, capex):
    res = (pb / capex).diff(21).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc045_21d_base_v045_signal'] = f59fc_f59_fcf_conversion_quality_calc045_21d_base_v045_signal

def f59fc_f59_fcf_conversion_quality_calc046_63d_base_v046_signal(ncfi, intexp, high):
    res = (high / intexp).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc046_63d_base_v046_signal'] = f59fc_f59_fcf_conversion_quality_calc046_63d_base_v046_signal

def f59fc_f59_fcf_conversion_quality_calc047_252d_base_v047_signal(liabilities, assets):
    res = np.log((liabilities / assets).abs().replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc047_252d_base_v047_signal'] = f59fc_f59_fcf_conversion_quality_calc047_252d_base_v047_signal

def f59fc_f59_fcf_conversion_quality_calc048_21d_base_v048_signal(opinc, close):
    res = (opinc / close)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc048_21d_base_v048_signal'] = f59fc_f59_fcf_conversion_quality_calc048_21d_base_v048_signal

def f59fc_f59_fcf_conversion_quality_calc049_5d_base_v049_signal(open, taxexp):
    res = (((taxexp / open) - (taxexp / open).rolling(5).mean()) / (taxexp / open).rolling(5).std()).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc049_5d_base_v049_signal'] = f59fc_f59_fcf_conversion_quality_calc049_5d_base_v049_signal

def f59fc_f59_fcf_conversion_quality_calc050_5d_base_v050_signal(opinc, taxexp):
    res = (taxexp / opinc).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc050_5d_base_v050_signal'] = f59fc_f59_fcf_conversion_quality_calc050_5d_base_v050_signal

def f59fc_f59_fcf_conversion_quality_calc051_126d_base_v051_signal(debt, netinc):
    res = (debt / netinc).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc051_126d_base_v051_signal'] = f59fc_f59_fcf_conversion_quality_calc051_126d_base_v051_signal

def f59fc_f59_fcf_conversion_quality_calc052_252d_base_v052_signal(ev, ps):
    res = (ev / ps).diff(21).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc052_252d_base_v052_signal'] = f59fc_f59_fcf_conversion_quality_calc052_252d_base_v052_signal

def f59fc_f59_fcf_conversion_quality_calc053_126d_base_v053_signal(debt, evebit):
    res = (debt / evebit).diff(1).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc053_126d_base_v053_signal'] = f59fc_f59_fcf_conversion_quality_calc053_126d_base_v053_signal

def f59fc_f59_fcf_conversion_quality_calc054_126d_base_v054_signal(ebitda, workingcapital):
    res = (((workingcapital / ebitda) - (workingcapital / ebitda).rolling(126).mean()) / (workingcapital / ebitda).rolling(126).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc054_126d_base_v054_signal'] = f59fc_f59_fcf_conversion_quality_calc054_126d_base_v054_signal

def f59fc_f59_fcf_conversion_quality_calc055_252d_base_v055_signal(fcf, eps):
    res = (eps / fcf).pct_change(21).rolling(252).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc055_252d_base_v055_signal'] = f59fc_f59_fcf_conversion_quality_calc055_252d_base_v055_signal

def f59fc_f59_fcf_conversion_quality_calc056_42d_base_v056_signal(ncfi, workingcapital):
    res = (((ncfi / workingcapital) - (ncfi / workingcapital).rolling(42).mean()) / (ncfi / workingcapital).rolling(42).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc056_42d_base_v056_signal'] = f59fc_f59_fcf_conversion_quality_calc056_42d_base_v056_signal

def f59fc_f59_fcf_conversion_quality_calc057_126d_base_v057_signal(intexp, debt):
    res = np.log((intexp / debt).abs().replace(0, np.nan)).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc057_126d_base_v057_signal'] = f59fc_f59_fcf_conversion_quality_calc057_126d_base_v057_signal

def f59fc_f59_fcf_conversion_quality_calc058_252d_base_v058_signal(revenue, closeadj, pb):
    res = (pb / revenue).pct_change(5).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc058_252d_base_v058_signal'] = f59fc_f59_fcf_conversion_quality_calc058_252d_base_v058_signal

def f59fc_f59_fcf_conversion_quality_calc059_63d_base_v059_signal(netinc, equity, high):
    res = (netinc / equity).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc059_63d_base_v059_signal'] = f59fc_f59_fcf_conversion_quality_calc059_63d_base_v059_signal

def f59fc_f59_fcf_conversion_quality_calc060_63d_base_v060_signal(ncfi, closeadj):
    res = (closeadj / ncfi).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc060_63d_base_v060_signal'] = f59fc_f59_fcf_conversion_quality_calc060_63d_base_v060_signal

def f59fc_f59_fcf_conversion_quality_calc061_63d_base_v061_signal(evebitda, currentratio, assets):
    res = (evebitda * currentratio / assets).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc061_63d_base_v061_signal'] = f59fc_f59_fcf_conversion_quality_calc061_63d_base_v061_signal

def f59fc_f59_fcf_conversion_quality_calc062_42d_base_v062_signal(taxexp, currentratio, assets):
    res = (taxexp * currentratio / assets).rolling(42).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc062_42d_base_v062_signal'] = f59fc_f59_fcf_conversion_quality_calc062_42d_base_v062_signal

def f59fc_f59_fcf_conversion_quality_calc063_5d_base_v063_signal(open, liabilities, opinc):
    res = (open / liabilities).rolling(5).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc063_5d_base_v063_signal'] = f59fc_f59_fcf_conversion_quality_calc063_5d_base_v063_signal

def f59fc_f59_fcf_conversion_quality_calc064_21d_base_v064_signal(evebit, gp):
    res = (evebit / gp).pct_change(21).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc064_21d_base_v064_signal'] = f59fc_f59_fcf_conversion_quality_calc064_21d_base_v064_signal

def f59fc_f59_fcf_conversion_quality_calc065_63d_base_v065_signal(evebit, assets, capex):
    res = np.log((assets / capex).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc065_63d_base_v065_signal'] = f59fc_f59_fcf_conversion_quality_calc065_63d_base_v065_signal

def f59fc_f59_fcf_conversion_quality_calc066_126d_base_v066_signal(equity, ev, gp):
    res = np.log((gp / equity).abs().replace(0, np.nan)).rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc066_126d_base_v066_signal'] = f59fc_f59_fcf_conversion_quality_calc066_126d_base_v066_signal

def f59fc_f59_fcf_conversion_quality_calc067_5d_base_v067_signal(fcf, evebitda):
    res = (fcf / evebitda).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc067_5d_base_v067_signal'] = f59fc_f59_fcf_conversion_quality_calc067_5d_base_v067_signal

def f59fc_f59_fcf_conversion_quality_calc068_42d_base_v068_signal(sharesbas, assets):
    res = (sharesbas / assets).diff(5).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc068_42d_base_v068_signal'] = f59fc_f59_fcf_conversion_quality_calc068_42d_base_v068_signal

def f59fc_f59_fcf_conversion_quality_calc069_63d_base_v069_signal(sharesbas, pe):
    res = np.log((pe / sharesbas).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc069_63d_base_v069_signal'] = f59fc_f59_fcf_conversion_quality_calc069_63d_base_v069_signal

def f59fc_f59_fcf_conversion_quality_calc070_10d_base_v070_signal(retearn, liabilities, capex):
    res = np.log((capex / retearn).abs().replace(0, np.nan)).rolling(10).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc070_10d_base_v070_signal'] = f59fc_f59_fcf_conversion_quality_calc070_10d_base_v070_signal

def f59fc_f59_fcf_conversion_quality_calc071_10d_base_v071_signal(intexp, netinc, taxexp):
    res = (netinc / taxexp).diff(1).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc071_10d_base_v071_signal'] = f59fc_f59_fcf_conversion_quality_calc071_10d_base_v071_signal

def f59fc_f59_fcf_conversion_quality_calc072_252d_base_v072_signal(intexp, workingcapital, assets):
    res = (workingcapital * intexp / assets).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc072_252d_base_v072_signal'] = f59fc_f59_fcf_conversion_quality_calc072_252d_base_v072_signal

def f59fc_f59_fcf_conversion_quality_calc073_42d_base_v073_signal(ev, high):
    res = (high / ev).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc073_42d_base_v073_signal'] = f59fc_f59_fcf_conversion_quality_calc073_42d_base_v073_signal

def f59fc_f59_fcf_conversion_quality_calc074_252d_base_v074_signal(retearn, gp, ebitda):
    res = (gp / retearn).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc074_252d_base_v074_signal'] = f59fc_f59_fcf_conversion_quality_calc074_252d_base_v074_signal

def f59fc_f59_fcf_conversion_quality_calc075_5d_base_v075_signal(retearn, sharesbas):
    res = (((retearn / sharesbas) - (retearn / sharesbas).rolling(5).mean()) / (retearn / sharesbas).rolling(5).std()).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc075_5d_base_v075_signal'] = f59fc_f59_fcf_conversion_quality_calc075_5d_base_v075_signal

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
