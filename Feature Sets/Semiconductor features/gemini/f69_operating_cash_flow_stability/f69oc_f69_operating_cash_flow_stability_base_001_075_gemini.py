import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f69oc_f69_operating_cash_flow_stability_calc001_42d_base_v001_signal(ncfo):
    res = (ncfo - ncfo.shift(42)).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc001_42d_base_v001_signal'] = f69oc_f69_operating_cash_flow_stability_calc001_42d_base_v001_signal

def f69oc_f69_operating_cash_flow_stability_calc002_150d_base_v002_signal(assets, ncfo):
    res = ncfo.rolling(150).std() / assets.replace(0, np.nan).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc002_150d_base_v002_signal'] = f69oc_f69_operating_cash_flow_stability_calc002_150d_base_v002_signal

def f69oc_f69_operating_cash_flow_stability_calc003_5d_base_v003_signal(ncfo, netinc):
    res = (ncfo / netinc.replace(0, np.nan)).rolling(5).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc003_5d_base_v003_signal'] = f69oc_f69_operating_cash_flow_stability_calc003_5d_base_v003_signal

def f69oc_f69_operating_cash_flow_stability_calc004_252d_base_v004_signal(ncfo):
    res = (ncfo.rolling(252).max() / ncfo.rolling(252).min()).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc004_252d_base_v004_signal'] = f69oc_f69_operating_cash_flow_stability_calc004_252d_base_v004_signal

def f69oc_f69_operating_cash_flow_stability_calc005_30d_base_v005_signal(currentratio, ncfo, retearn):
    res = (ncfo.rolling(30).mean() - retearn.rolling(30).mean()) / currentratio.replace(0, np.nan).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc005_30d_base_v005_signal'] = f69oc_f69_operating_cash_flow_stability_calc005_30d_base_v005_signal

def f69oc_f69_operating_cash_flow_stability_calc006_200d_base_v006_signal(ncfo):
    res = ncfo.rolling(200).median().pct_change(40)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc006_200d_base_v006_signal'] = f69oc_f69_operating_cash_flow_stability_calc006_200d_base_v006_signal

def f69oc_f69_operating_cash_flow_stability_calc007_15d_base_v007_signal(debt, ncfo):
    res = (ncfo / debt.replace(0, np.nan)).rolling(15).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc007_15d_base_v007_signal'] = f69oc_f69_operating_cash_flow_stability_calc007_15d_base_v007_signal

def f69oc_f69_operating_cash_flow_stability_calc008_100d_base_v008_signal(ncfo):
    res = ncfo.pct_change(100).rolling(100).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc008_100d_base_v008_signal'] = f69oc_f69_operating_cash_flow_stability_calc008_100d_base_v008_signal

def f69oc_f69_operating_cash_flow_stability_calc009_252d_base_v009_signal(ncfo):
    res = ncfo.pct_change(252).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc009_252d_base_v009_signal'] = f69oc_f69_operating_cash_flow_stability_calc009_252d_base_v009_signal

def f69oc_f69_operating_cash_flow_stability_calc010_100d_base_v010_signal(ncfo, netinc):
    res = (ncfo * netinc).rolling(100).std() / (ncfo * netinc).rolling(100).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc010_100d_base_v010_signal'] = f69oc_f69_operating_cash_flow_stability_calc010_100d_base_v010_signal

def f69oc_f69_operating_cash_flow_stability_calc011_80d_base_v011_signal(low, ncfo):
    res = (low / ncfo.replace(0, np.nan)).rolling(80).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc011_80d_base_v011_signal'] = f69oc_f69_operating_cash_flow_stability_calc011_80d_base_v011_signal

def f69oc_f69_operating_cash_flow_stability_calc012_126d_base_v012_signal(ncfo, sharesbas):
    res = (ncfo / sharesbas.replace(0, np.nan)).rolling(126).std().pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc012_126d_base_v012_signal'] = f69oc_f69_operating_cash_flow_stability_calc012_126d_base_v012_signal

def f69oc_f69_operating_cash_flow_stability_calc013_21d_base_v013_signal(ebitda, ncfo):
    res = (ncfo * ebitda).rolling(21).std() / (ncfo * ebitda).rolling(21).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc013_21d_base_v013_signal'] = f69oc_f69_operating_cash_flow_stability_calc013_21d_base_v013_signal

def f69oc_f69_operating_cash_flow_stability_calc014_100d_base_v014_signal(equity, ncfo):
    res = (ncfo.rolling(100).max() - ncfo.rolling(100).min()) / equity.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc014_100d_base_v014_signal'] = f69oc_f69_operating_cash_flow_stability_calc014_100d_base_v014_signal

def f69oc_f69_operating_cash_flow_stability_calc015_10d_base_v015_signal(ncff, ncfo):
    res = (ncfo - ncff.rolling(10).mean()).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc015_10d_base_v015_signal'] = f69oc_f69_operating_cash_flow_stability_calc015_10d_base_v015_signal

def f69oc_f69_operating_cash_flow_stability_calc016_5d_base_v016_signal(ncfo, retearn):
    res = ncfo.rolling(5).std() / retearn.replace(0, np.nan).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc016_5d_base_v016_signal'] = f69oc_f69_operating_cash_flow_stability_calc016_5d_base_v016_signal

def f69oc_f69_operating_cash_flow_stability_calc017_30d_base_v017_signal(close, ncfo):
    res = (ncfo / close.replace(0, np.nan)).rolling(30).std().pct_change(6)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc017_30d_base_v017_signal'] = f69oc_f69_operating_cash_flow_stability_calc017_30d_base_v017_signal

def f69oc_f69_operating_cash_flow_stability_calc018_126d_base_v018_signal(ncfo):
    res = (ncfo - ncfo.shift(126)).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc018_126d_base_v018_signal'] = f69oc_f69_operating_cash_flow_stability_calc018_126d_base_v018_signal

def f69oc_f69_operating_cash_flow_stability_calc019_21d_base_v019_signal(high, ncfo):
    res = (ncfo.diff(21) / high.replace(0, np.nan).diff(21)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc019_21d_base_v019_signal'] = f69oc_f69_operating_cash_flow_stability_calc019_21d_base_v019_signal

def f69oc_f69_operating_cash_flow_stability_calc020_100d_base_v020_signal(ncfo, workingcapital):
    res = ncfo.rolling(100).std() / workingcapital.replace(0, np.nan).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc020_100d_base_v020_signal'] = f69oc_f69_operating_cash_flow_stability_calc020_100d_base_v020_signal

def f69oc_f69_operating_cash_flow_stability_calc021_15d_base_v021_signal(ncfo):
    res = (ncfo.rolling(15).rank(pct=True)).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc021_15d_base_v021_signal'] = f69oc_f69_operating_cash_flow_stability_calc021_15d_base_v021_signal

def f69oc_f69_operating_cash_flow_stability_calc022_63d_base_v022_signal(close, ncfo):
    res = (close / ncfo.replace(0, np.nan)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc022_63d_base_v022_signal'] = f69oc_f69_operating_cash_flow_stability_calc022_63d_base_v022_signal

def f69oc_f69_operating_cash_flow_stability_calc023_200d_base_v023_signal(ncfo):
    res = (ncfo.rolling(200).max() - ncfo.rolling(200).min()) / ncfo.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc023_200d_base_v023_signal'] = f69oc_f69_operating_cash_flow_stability_calc023_200d_base_v023_signal

def f69oc_f69_operating_cash_flow_stability_calc024_63d_base_v024_signal(ncfo):
    res = ncfo.rolling(63).rank(pct=True).diff(12)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc024_63d_base_v024_signal'] = f69oc_f69_operating_cash_flow_stability_calc024_63d_base_v024_signal

def f69oc_f69_operating_cash_flow_stability_calc025_5d_base_v025_signal(gp, ncfo):
    res = (ncfo - gp.rolling(5).mean()).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc025_5d_base_v025_signal'] = f69oc_f69_operating_cash_flow_stability_calc025_5d_base_v025_signal

def f69oc_f69_operating_cash_flow_stability_calc026_42d_base_v026_signal(ebitda, ncfo):
    res = (ncfo / ebitda.replace(0, np.nan)).rolling(42).mean().diff(4)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc026_42d_base_v026_signal'] = f69oc_f69_operating_cash_flow_stability_calc026_42d_base_v026_signal

def f69oc_f69_operating_cash_flow_stability_calc027_150d_base_v027_signal(marketcap, ncfo):
    res = (ncfo / marketcap.replace(0, np.nan)).rolling(150).std().pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc027_150d_base_v027_signal'] = f69oc_f69_operating_cash_flow_stability_calc027_150d_base_v027_signal

def f69oc_f69_operating_cash_flow_stability_calc028_252d_base_v028_signal(ncfo, sharesbas):
    res = (ncfo / sharesbas.replace(0, np.nan)).rolling(252).mean().diff(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc028_252d_base_v028_signal'] = f69oc_f69_operating_cash_flow_stability_calc028_252d_base_v028_signal

def f69oc_f69_operating_cash_flow_stability_calc029_150d_base_v029_signal(currentratio, ncfo, ps):
    res = (ncfo * currentratio / ps.replace(0, np.nan)).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc029_150d_base_v029_signal'] = f69oc_f69_operating_cash_flow_stability_calc029_150d_base_v029_signal

def f69oc_f69_operating_cash_flow_stability_calc030_63d_base_v030_signal(capex, ncfo):
    res = (ncfo / capex.replace(0, np.nan)).rolling(63).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc030_63d_base_v030_signal'] = f69oc_f69_operating_cash_flow_stability_calc030_63d_base_v030_signal

def f69oc_f69_operating_cash_flow_stability_calc031_200d_base_v031_signal(ncfo):
    res = ncfo.rolling(200).std() / ncfo.rolling(200).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc031_200d_base_v031_signal'] = f69oc_f69_operating_cash_flow_stability_calc031_200d_base_v031_signal

def f69oc_f69_operating_cash_flow_stability_calc032_126d_base_v032_signal(high, ncfo):
    res = (ncfo / high.replace(0, np.nan)).rolling(126).std().pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc032_126d_base_v032_signal'] = f69oc_f69_operating_cash_flow_stability_calc032_126d_base_v032_signal

def f69oc_f69_operating_cash_flow_stability_calc033_100d_base_v033_signal(low, ncfo):
    res = (ncfo - low.rolling(100).mean()).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc033_100d_base_v033_signal'] = f69oc_f69_operating_cash_flow_stability_calc033_100d_base_v033_signal

def f69oc_f69_operating_cash_flow_stability_calc034_5d_base_v034_signal(ncfo):
    res = (ncfo - ncfo.shift(5)).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc034_5d_base_v034_signal'] = f69oc_f69_operating_cash_flow_stability_calc034_5d_base_v034_signal

def f69oc_f69_operating_cash_flow_stability_calc035_80d_base_v035_signal(ncfo, retearn):
    res = (ncfo / retearn.replace(0, np.nan)).rolling(80).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc035_80d_base_v035_signal'] = f69oc_f69_operating_cash_flow_stability_calc035_80d_base_v035_signal

def f69oc_f69_operating_cash_flow_stability_calc036_200d_base_v036_signal(ncfo):
    res = ncfo.pct_change(200).rolling(200).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc036_200d_base_v036_signal'] = f69oc_f69_operating_cash_flow_stability_calc036_200d_base_v036_signal

def f69oc_f69_operating_cash_flow_stability_calc037_5d_base_v037_signal(ncfo, retearn):
    res = (ncfo.rolling(5).max() - retearn.rolling(5).min()) / retearn.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc037_5d_base_v037_signal'] = f69oc_f69_operating_cash_flow_stability_calc037_5d_base_v037_signal

def f69oc_f69_operating_cash_flow_stability_calc038_15d_base_v038_signal(capex, ncfo):
    res = (ncfo.diff(15) / capex.replace(0, np.nan).diff(15)).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc038_15d_base_v038_signal'] = f69oc_f69_operating_cash_flow_stability_calc038_15d_base_v038_signal

def f69oc_f69_operating_cash_flow_stability_calc039_10d_base_v039_signal(currentratio, ncfo):
    res = (ncfo.diff(10) / currentratio.replace(0, np.nan).diff(10)).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc039_10d_base_v039_signal'] = f69oc_f69_operating_cash_flow_stability_calc039_10d_base_v039_signal

def f69oc_f69_operating_cash_flow_stability_calc040_252d_base_v040_signal(evebitda, ncfo):
    res = np.log((ncfo.abs() + 1) / (evebitda.abs() + 1)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc040_252d_base_v040_signal'] = f69oc_f69_operating_cash_flow_stability_calc040_252d_base_v040_signal

def f69oc_f69_operating_cash_flow_stability_calc041_5d_base_v041_signal(close, ncfo):
    res = (ncfo / close.replace(0, np.nan)).rolling(5).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc041_5d_base_v041_signal'] = f69oc_f69_operating_cash_flow_stability_calc041_5d_base_v041_signal

def f69oc_f69_operating_cash_flow_stability_calc042_5d_base_v042_signal(ncfo, workingcapital):
    res = (ncfo * workingcapital).rolling(5).std() / (ncfo * workingcapital).rolling(5).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc042_5d_base_v042_signal'] = f69oc_f69_operating_cash_flow_stability_calc042_5d_base_v042_signal

def f69oc_f69_operating_cash_flow_stability_calc043_252d_base_v043_signal(ncfo):
    res = ncfo.rolling(252).std() / ncfo.rolling(252).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc043_252d_base_v043_signal'] = f69oc_f69_operating_cash_flow_stability_calc043_252d_base_v043_signal

def f69oc_f69_operating_cash_flow_stability_calc044_80d_base_v044_signal(ncfo):
    res = (ncfo - ncfo.shift(80)).rolling(80).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc044_80d_base_v044_signal'] = f69oc_f69_operating_cash_flow_stability_calc044_80d_base_v044_signal

def f69oc_f69_operating_cash_flow_stability_calc045_15d_base_v045_signal(assets, capex, ncfo):
    res = (ncfo * capex / assets.replace(0, np.nan)).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc045_15d_base_v045_signal'] = f69oc_f69_operating_cash_flow_stability_calc045_15d_base_v045_signal

def f69oc_f69_operating_cash_flow_stability_calc046_42d_base_v046_signal(marketcap, ncfo):
    res = (ncfo * marketcap).rolling(42).std() / (ncfo * marketcap).rolling(42).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc046_42d_base_v046_signal'] = f69oc_f69_operating_cash_flow_stability_calc046_42d_base_v046_signal

def f69oc_f69_operating_cash_flow_stability_calc047_10d_base_v047_signal(ncfo):
    res = ncfo.rolling(10).std() / ncfo.rolling(10).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc047_10d_base_v047_signal'] = f69oc_f69_operating_cash_flow_stability_calc047_10d_base_v047_signal

def f69oc_f69_operating_cash_flow_stability_calc048_63d_base_v048_signal(intexp, ncfo):
    res = np.log((ncfo.abs() + 1) / (intexp.abs() + 1)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc048_63d_base_v048_signal'] = f69oc_f69_operating_cash_flow_stability_calc048_63d_base_v048_signal

def f69oc_f69_operating_cash_flow_stability_calc049_252d_base_v049_signal(ncfo):
    res = ncfo.rolling(252).median().pct_change(50)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc049_252d_base_v049_signal'] = f69oc_f69_operating_cash_flow_stability_calc049_252d_base_v049_signal

def f69oc_f69_operating_cash_flow_stability_calc050_5d_base_v050_signal(ncfo):
    res = ncfo.rolling(5).rank(pct=True).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc050_5d_base_v050_signal'] = f69oc_f69_operating_cash_flow_stability_calc050_5d_base_v050_signal

def f69oc_f69_operating_cash_flow_stability_calc051_42d_base_v051_signal(ncfo, pb):
    res = (ncfo / pb.replace(0, np.nan)).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc051_42d_base_v051_signal'] = f69oc_f69_operating_cash_flow_stability_calc051_42d_base_v051_signal

def f69oc_f69_operating_cash_flow_stability_calc052_30d_base_v052_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital.replace(0, np.nan)).rolling(30).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc052_30d_base_v052_signal'] = f69oc_f69_operating_cash_flow_stability_calc052_30d_base_v052_signal

def f69oc_f69_operating_cash_flow_stability_calc053_15d_base_v053_signal(ev, ncfo):
    res = np.log((ncfo.abs() + 1) / (ev.abs() + 1)).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc053_15d_base_v053_signal'] = f69oc_f69_operating_cash_flow_stability_calc053_15d_base_v053_signal

def f69oc_f69_operating_cash_flow_stability_calc054_80d_base_v054_signal(evebit, ncfo):
    res = (ncfo - evebit.rolling(80).mean()).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc054_80d_base_v054_signal'] = f69oc_f69_operating_cash_flow_stability_calc054_80d_base_v054_signal

def f69oc_f69_operating_cash_flow_stability_calc055_252d_base_v055_signal(ncfo, taxexp):
    res = (ncfo / taxexp.replace(0, np.nan)).rolling(252).mean().diff(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc055_252d_base_v055_signal'] = f69oc_f69_operating_cash_flow_stability_calc055_252d_base_v055_signal

def f69oc_f69_operating_cash_flow_stability_calc056_21d_base_v056_signal(low, ncfo):
    res = (ncfo / low.replace(0, np.nan)).rolling(21).mean().diff(2)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc056_21d_base_v056_signal'] = f69oc_f69_operating_cash_flow_stability_calc056_21d_base_v056_signal

def f69oc_f69_operating_cash_flow_stability_calc057_150d_base_v057_signal(ncfo, opinc, workingcapital):
    res = (ncfo.rolling(150).mean() - opinc.rolling(150).mean()) / workingcapital.replace(0, np.nan).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc057_150d_base_v057_signal'] = f69oc_f69_operating_cash_flow_stability_calc057_150d_base_v057_signal

def f69oc_f69_operating_cash_flow_stability_calc058_50d_base_v058_signal(capex, ncfo):
    res = (capex / ncfo.replace(0, np.nan)).rolling(50).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc058_50d_base_v058_signal'] = f69oc_f69_operating_cash_flow_stability_calc058_50d_base_v058_signal

def f69oc_f69_operating_cash_flow_stability_calc059_21d_base_v059_signal(low, ncfo):
    res = (ncfo.diff(21) / low.replace(0, np.nan).diff(21)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc059_21d_base_v059_signal'] = f69oc_f69_operating_cash_flow_stability_calc059_21d_base_v059_signal

def f69oc_f69_operating_cash_flow_stability_calc060_50d_base_v060_signal(assets, ncfo):
    res = (ncfo * assets).rolling(50).std() / (ncfo * assets).rolling(50).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc060_50d_base_v060_signal'] = f69oc_f69_operating_cash_flow_stability_calc060_50d_base_v060_signal

def f69oc_f69_operating_cash_flow_stability_calc061_63d_base_v061_signal(evebit, ncfo):
    res = (ncfo / evebit.replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc061_63d_base_v061_signal'] = f69oc_f69_operating_cash_flow_stability_calc061_63d_base_v061_signal

def f69oc_f69_operating_cash_flow_stability_calc062_80d_base_v062_signal(liabilities, ncfo, ps):
    res = (ncfo * ps / liabilities.replace(0, np.nan)).pct_change(8)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc062_80d_base_v062_signal'] = f69oc_f69_operating_cash_flow_stability_calc062_80d_base_v062_signal

def f69oc_f69_operating_cash_flow_stability_calc063_5d_base_v063_signal(ncfo, opinc):
    res = (ncfo / opinc.replace(0, np.nan)).rolling(5).std().pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc063_5d_base_v063_signal'] = f69oc_f69_operating_cash_flow_stability_calc063_5d_base_v063_signal

def f69oc_f69_operating_cash_flow_stability_calc064_21d_base_v064_signal(ncfo):
    res = ncfo.pct_change(21).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc064_21d_base_v064_signal'] = f69oc_f69_operating_cash_flow_stability_calc064_21d_base_v064_signal

def f69oc_f69_operating_cash_flow_stability_calc065_50d_base_v065_signal(ncfo):
    res = (ncfo.rolling(50).max() - ncfo.rolling(50).min()) / ncfo.rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc065_50d_base_v065_signal'] = f69oc_f69_operating_cash_flow_stability_calc065_50d_base_v065_signal

def f69oc_f69_operating_cash_flow_stability_calc066_100d_base_v066_signal(ncfo, revenue):
    res = (ncfo / revenue.replace(0, np.nan)).rolling(100).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc066_100d_base_v066_signal'] = f69oc_f69_operating_cash_flow_stability_calc066_100d_base_v066_signal

def f69oc_f69_operating_cash_flow_stability_calc067_5d_base_v067_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital.replace(0, np.nan)).rolling(5).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc067_5d_base_v067_signal'] = f69oc_f69_operating_cash_flow_stability_calc067_5d_base_v067_signal

def f69oc_f69_operating_cash_flow_stability_calc068_200d_base_v068_signal(ncfo):
    res = (ncfo / ncfo.replace(0, np.nan)).rolling(200).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc068_200d_base_v068_signal'] = f69oc_f69_operating_cash_flow_stability_calc068_200d_base_v068_signal

def f69oc_f69_operating_cash_flow_stability_calc069_42d_base_v069_signal(equity, ncfo):
    res = (ncfo / equity.replace(0, np.nan)).rolling(42).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc069_42d_base_v069_signal'] = f69oc_f69_operating_cash_flow_stability_calc069_42d_base_v069_signal

def f69oc_f69_operating_cash_flow_stability_calc070_50d_base_v070_signal(ncfo):
    res = ncfo.rolling(50).median().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc070_50d_base_v070_signal'] = f69oc_f69_operating_cash_flow_stability_calc070_50d_base_v070_signal

def f69oc_f69_operating_cash_flow_stability_calc071_252d_base_v071_signal(ncfo, taxexp):
    res = ncfo.rolling(252).var() / taxexp.rolling(252).var().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc071_252d_base_v071_signal'] = f69oc_f69_operating_cash_flow_stability_calc071_252d_base_v071_signal

def f69oc_f69_operating_cash_flow_stability_calc072_30d_base_v072_signal(marketcap, ncfo):
    res = (ncfo / marketcap.replace(0, np.nan)).rolling(30).mean().diff(3)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc072_30d_base_v072_signal'] = f69oc_f69_operating_cash_flow_stability_calc072_30d_base_v072_signal

def f69oc_f69_operating_cash_flow_stability_calc073_42d_base_v073_signal(ncfo):
    res = ncfo.pct_change(42).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc073_42d_base_v073_signal'] = f69oc_f69_operating_cash_flow_stability_calc073_42d_base_v073_signal

def f69oc_f69_operating_cash_flow_stability_calc074_200d_base_v074_signal(ncff, ncfo):
    res = (ncfo / ncff.replace(0, np.nan)).rolling(200).mean().diff(20)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc074_200d_base_v074_signal'] = f69oc_f69_operating_cash_flow_stability_calc074_200d_base_v074_signal

def f69oc_f69_operating_cash_flow_stability_calc075_63d_base_v075_signal(ncfo):
    res = (ncfo.rolling(63).max() / ncfo.rolling(63).min()).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc075_63d_base_v075_signal'] = f69oc_f69_operating_cash_flow_stability_calc075_63d_base_v075_signal


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
