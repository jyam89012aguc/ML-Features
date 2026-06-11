import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f69oc_f69_operating_cash_flow_stability_calc001_42d_3rd_derivative_v001_signal(ncfo):
    res = ((ncfo - ncfo.shift(42)).rolling(42).skew()).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc001_42d_3rd_derivative_v001_signal'] = f69oc_f69_operating_cash_flow_stability_calc001_42d_3rd_derivative_v001_signal

def f69oc_f69_operating_cash_flow_stability_calc002_150d_3rd_derivative_v002_signal(assets, ncfo):
    res = (ncfo.rolling(150).std() / assets.replace(0, np.nan).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc002_150d_3rd_derivative_v002_signal'] = f69oc_f69_operating_cash_flow_stability_calc002_150d_3rd_derivative_v002_signal

def f69oc_f69_operating_cash_flow_stability_calc003_5d_3rd_derivative_v003_signal(ncfo, netinc):
    res = ((ncfo / netinc.replace(0, np.nan)).rolling(5).std().pct_change(1)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc003_5d_3rd_derivative_v003_signal'] = f69oc_f69_operating_cash_flow_stability_calc003_5d_3rd_derivative_v003_signal

def f69oc_f69_operating_cash_flow_stability_calc004_252d_3rd_derivative_v004_signal(ncfo):
    res = ((ncfo.rolling(252).max() / ncfo.rolling(252).min()).pct_change(5)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc004_252d_3rd_derivative_v004_signal'] = f69oc_f69_operating_cash_flow_stability_calc004_252d_3rd_derivative_v004_signal

def f69oc_f69_operating_cash_flow_stability_calc005_30d_3rd_derivative_v005_signal(currentratio, ncfo, retearn):
    res = ((ncfo.rolling(30).mean() - retearn.rolling(30).mean()) / currentratio.replace(0, np.nan).rolling(30).std()).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc005_30d_3rd_derivative_v005_signal'] = f69oc_f69_operating_cash_flow_stability_calc005_30d_3rd_derivative_v005_signal

def f69oc_f69_operating_cash_flow_stability_calc006_200d_3rd_derivative_v006_signal(ncfo):
    res = (ncfo.rolling(200).median().pct_change(40)).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc006_200d_3rd_derivative_v006_signal'] = f69oc_f69_operating_cash_flow_stability_calc006_200d_3rd_derivative_v006_signal

def f69oc_f69_operating_cash_flow_stability_calc007_15d_3rd_derivative_v007_signal(debt, ncfo):
    res = ((ncfo / debt.replace(0, np.nan)).rolling(15).quantile(0.9)).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc007_15d_3rd_derivative_v007_signal'] = f69oc_f69_operating_cash_flow_stability_calc007_15d_3rd_derivative_v007_signal

def f69oc_f69_operating_cash_flow_stability_calc008_100d_3rd_derivative_v008_signal(ncfo):
    res = (ncfo.pct_change(100).rolling(100).kurt()).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc008_100d_3rd_derivative_v008_signal'] = f69oc_f69_operating_cash_flow_stability_calc008_100d_3rd_derivative_v008_signal

def f69oc_f69_operating_cash_flow_stability_calc009_252d_3rd_derivative_v009_signal(ncfo):
    res = (ncfo.pct_change(252).rolling(252).kurt()).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc009_252d_3rd_derivative_v009_signal'] = f69oc_f69_operating_cash_flow_stability_calc009_252d_3rd_derivative_v009_signal

def f69oc_f69_operating_cash_flow_stability_calc010_100d_3rd_derivative_v010_signal(ncfo, netinc):
    res = ((ncfo * netinc).rolling(100).std() / (ncfo * netinc).rolling(100).mean().abs()).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc010_100d_3rd_derivative_v010_signal'] = f69oc_f69_operating_cash_flow_stability_calc010_100d_3rd_derivative_v010_signal

def f69oc_f69_operating_cash_flow_stability_calc011_80d_3rd_derivative_v011_signal(low, ncfo):
    res = ((low / ncfo.replace(0, np.nan)).rolling(80).mean()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc011_80d_3rd_derivative_v011_signal'] = f69oc_f69_operating_cash_flow_stability_calc011_80d_3rd_derivative_v011_signal

def f69oc_f69_operating_cash_flow_stability_calc012_126d_3rd_derivative_v012_signal(ncfo, sharesbas):
    res = ((ncfo / sharesbas.replace(0, np.nan)).rolling(126).std().pct_change(25)).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc012_126d_3rd_derivative_v012_signal'] = f69oc_f69_operating_cash_flow_stability_calc012_126d_3rd_derivative_v012_signal

def f69oc_f69_operating_cash_flow_stability_calc013_21d_3rd_derivative_v013_signal(ebitda, ncfo):
    res = ((ncfo * ebitda).rolling(21).std() / (ncfo * ebitda).rolling(21).mean().abs()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc013_21d_3rd_derivative_v013_signal'] = f69oc_f69_operating_cash_flow_stability_calc013_21d_3rd_derivative_v013_signal

def f69oc_f69_operating_cash_flow_stability_calc014_100d_3rd_derivative_v014_signal(equity, ncfo):
    res = ((ncfo.rolling(100).max() - ncfo.rolling(100).min()) / equity.replace(0, np.nan)).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc014_100d_3rd_derivative_v014_signal'] = f69oc_f69_operating_cash_flow_stability_calc014_100d_3rd_derivative_v014_signal

def f69oc_f69_operating_cash_flow_stability_calc015_10d_3rd_derivative_v015_signal(ncff, ncfo):
    res = ((ncfo - ncff.rolling(10).mean()).rolling(10).std()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc015_10d_3rd_derivative_v015_signal'] = f69oc_f69_operating_cash_flow_stability_calc015_10d_3rd_derivative_v015_signal

def f69oc_f69_operating_cash_flow_stability_calc016_5d_3rd_derivative_v016_signal(ncfo, retearn):
    res = (ncfo.rolling(5).std() / retearn.replace(0, np.nan).rolling(5).std()).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc016_5d_3rd_derivative_v016_signal'] = f69oc_f69_operating_cash_flow_stability_calc016_5d_3rd_derivative_v016_signal

def f69oc_f69_operating_cash_flow_stability_calc017_30d_3rd_derivative_v017_signal(close, ncfo):
    res = ((ncfo / close.replace(0, np.nan)).rolling(30).std().pct_change(6)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc017_30d_3rd_derivative_v017_signal'] = f69oc_f69_operating_cash_flow_stability_calc017_30d_3rd_derivative_v017_signal

def f69oc_f69_operating_cash_flow_stability_calc018_126d_3rd_derivative_v018_signal(ncfo):
    res = ((ncfo - ncfo.shift(126)).rolling(126).skew()).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc018_126d_3rd_derivative_v018_signal'] = f69oc_f69_operating_cash_flow_stability_calc018_126d_3rd_derivative_v018_signal

def f69oc_f69_operating_cash_flow_stability_calc019_21d_3rd_derivative_v019_signal(high, ncfo):
    res = ((ncfo.diff(21) / high.replace(0, np.nan).diff(21)).rolling(21).mean()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc019_21d_3rd_derivative_v019_signal'] = f69oc_f69_operating_cash_flow_stability_calc019_21d_3rd_derivative_v019_signal

def f69oc_f69_operating_cash_flow_stability_calc020_100d_3rd_derivative_v020_signal(ncfo, workingcapital):
    res = (ncfo.rolling(100).std() / workingcapital.replace(0, np.nan).rolling(100).std()).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc020_100d_3rd_derivative_v020_signal'] = f69oc_f69_operating_cash_flow_stability_calc020_100d_3rd_derivative_v020_signal

def f69oc_f69_operating_cash_flow_stability_calc021_15d_3rd_derivative_v021_signal(ncfo):
    res = ((ncfo.rolling(15).rank(pct=True)).rolling(15).std()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc021_15d_3rd_derivative_v021_signal'] = f69oc_f69_operating_cash_flow_stability_calc021_15d_3rd_derivative_v021_signal

def f69oc_f69_operating_cash_flow_stability_calc022_63d_3rd_derivative_v022_signal(close, ncfo):
    res = ((close / ncfo.replace(0, np.nan)).rolling(63).mean()).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc022_63d_3rd_derivative_v022_signal'] = f69oc_f69_operating_cash_flow_stability_calc022_63d_3rd_derivative_v022_signal

def f69oc_f69_operating_cash_flow_stability_calc023_200d_3rd_derivative_v023_signal(ncfo):
    res = ((ncfo.rolling(200).max() - ncfo.rolling(200).min()) / ncfo.replace(0, np.nan)).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc023_200d_3rd_derivative_v023_signal'] = f69oc_f69_operating_cash_flow_stability_calc023_200d_3rd_derivative_v023_signal

def f69oc_f69_operating_cash_flow_stability_calc024_63d_3rd_derivative_v024_signal(ncfo):
    res = (ncfo.rolling(63).rank(pct=True).diff(12)).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc024_63d_3rd_derivative_v024_signal'] = f69oc_f69_operating_cash_flow_stability_calc024_63d_3rd_derivative_v024_signal

def f69oc_f69_operating_cash_flow_stability_calc025_5d_3rd_derivative_v025_signal(gp, ncfo):
    res = ((ncfo - gp.rolling(5).mean()).rolling(5).std()).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc025_5d_3rd_derivative_v025_signal'] = f69oc_f69_operating_cash_flow_stability_calc025_5d_3rd_derivative_v025_signal

def f69oc_f69_operating_cash_flow_stability_calc026_42d_3rd_derivative_v026_signal(ebitda, ncfo):
    res = ((ncfo / ebitda.replace(0, np.nan)).rolling(42).mean().diff(4)).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc026_42d_3rd_derivative_v026_signal'] = f69oc_f69_operating_cash_flow_stability_calc026_42d_3rd_derivative_v026_signal

def f69oc_f69_operating_cash_flow_stability_calc027_150d_3rd_derivative_v027_signal(marketcap, ncfo):
    res = ((ncfo / marketcap.replace(0, np.nan)).rolling(150).std().pct_change(30)).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc027_150d_3rd_derivative_v027_signal'] = f69oc_f69_operating_cash_flow_stability_calc027_150d_3rd_derivative_v027_signal

def f69oc_f69_operating_cash_flow_stability_calc028_252d_3rd_derivative_v028_signal(ncfo, sharesbas):
    res = ((ncfo / sharesbas.replace(0, np.nan)).rolling(252).mean().diff(25)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc028_252d_3rd_derivative_v028_signal'] = f69oc_f69_operating_cash_flow_stability_calc028_252d_3rd_derivative_v028_signal

def f69oc_f69_operating_cash_flow_stability_calc029_150d_3rd_derivative_v029_signal(currentratio, ncfo, ps):
    res = ((ncfo * currentratio / ps.replace(0, np.nan)).pct_change(15)).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc029_150d_3rd_derivative_v029_signal'] = f69oc_f69_operating_cash_flow_stability_calc029_150d_3rd_derivative_v029_signal

def f69oc_f69_operating_cash_flow_stability_calc030_63d_3rd_derivative_v030_signal(capex, ncfo):
    res = ((ncfo / capex.replace(0, np.nan)).rolling(63).skew().diff(5)).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc030_63d_3rd_derivative_v030_signal'] = f69oc_f69_operating_cash_flow_stability_calc030_63d_3rd_derivative_v030_signal

def f69oc_f69_operating_cash_flow_stability_calc031_200d_3rd_derivative_v031_signal(ncfo):
    res = (ncfo.rolling(200).std() / ncfo.rolling(200).mean().abs()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc031_200d_3rd_derivative_v031_signal'] = f69oc_f69_operating_cash_flow_stability_calc031_200d_3rd_derivative_v031_signal

def f69oc_f69_operating_cash_flow_stability_calc032_126d_3rd_derivative_v032_signal(high, ncfo):
    res = ((ncfo / high.replace(0, np.nan)).rolling(126).std().pct_change(25)).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc032_126d_3rd_derivative_v032_signal'] = f69oc_f69_operating_cash_flow_stability_calc032_126d_3rd_derivative_v032_signal

def f69oc_f69_operating_cash_flow_stability_calc033_100d_3rd_derivative_v033_signal(low, ncfo):
    res = ((ncfo - low.rolling(100).mean()).rolling(100).std()).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc033_100d_3rd_derivative_v033_signal'] = f69oc_f69_operating_cash_flow_stability_calc033_100d_3rd_derivative_v033_signal

def f69oc_f69_operating_cash_flow_stability_calc034_5d_3rd_derivative_v034_signal(ncfo):
    res = ((ncfo - ncfo.shift(5)).rolling(5).skew()).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc034_5d_3rd_derivative_v034_signal'] = f69oc_f69_operating_cash_flow_stability_calc034_5d_3rd_derivative_v034_signal

def f69oc_f69_operating_cash_flow_stability_calc035_80d_3rd_derivative_v035_signal(ncfo, retearn):
    res = ((ncfo / retearn.replace(0, np.nan)).rolling(80).kurt()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc035_80d_3rd_derivative_v035_signal'] = f69oc_f69_operating_cash_flow_stability_calc035_80d_3rd_derivative_v035_signal

def f69oc_f69_operating_cash_flow_stability_calc036_200d_3rd_derivative_v036_signal(ncfo):
    res = (ncfo.pct_change(200).rolling(200).kurt()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc036_200d_3rd_derivative_v036_signal'] = f69oc_f69_operating_cash_flow_stability_calc036_200d_3rd_derivative_v036_signal

def f69oc_f69_operating_cash_flow_stability_calc037_5d_3rd_derivative_v037_signal(ncfo, retearn):
    res = ((ncfo.rolling(5).max() - retearn.rolling(5).min()) / retearn.rolling(5).std()).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc037_5d_3rd_derivative_v037_signal'] = f69oc_f69_operating_cash_flow_stability_calc037_5d_3rd_derivative_v037_signal

def f69oc_f69_operating_cash_flow_stability_calc038_15d_3rd_derivative_v038_signal(capex, ncfo):
    res = ((ncfo.diff(15) / capex.replace(0, np.nan).diff(15)).rolling(15).mean()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc038_15d_3rd_derivative_v038_signal'] = f69oc_f69_operating_cash_flow_stability_calc038_15d_3rd_derivative_v038_signal

def f69oc_f69_operating_cash_flow_stability_calc039_10d_3rd_derivative_v039_signal(currentratio, ncfo):
    res = ((ncfo.diff(10) / currentratio.replace(0, np.nan).diff(10)).rolling(10).mean()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc039_10d_3rd_derivative_v039_signal'] = f69oc_f69_operating_cash_flow_stability_calc039_10d_3rd_derivative_v039_signal

def f69oc_f69_operating_cash_flow_stability_calc040_252d_3rd_derivative_v040_signal(evebitda, ncfo):
    res = (np.log((ncfo.abs() + 1) / (evebitda.abs() + 1)).rolling(252).std()).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc040_252d_3rd_derivative_v040_signal'] = f69oc_f69_operating_cash_flow_stability_calc040_252d_3rd_derivative_v040_signal

def f69oc_f69_operating_cash_flow_stability_calc041_5d_3rd_derivative_v041_signal(close, ncfo):
    res = ((ncfo / close.replace(0, np.nan)).rolling(5).std().pct_change(1)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc041_5d_3rd_derivative_v041_signal'] = f69oc_f69_operating_cash_flow_stability_calc041_5d_3rd_derivative_v041_signal

def f69oc_f69_operating_cash_flow_stability_calc042_5d_3rd_derivative_v042_signal(ncfo, workingcapital):
    res = ((ncfo * workingcapital).rolling(5).std() / (ncfo * workingcapital).rolling(5).mean().abs()).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc042_5d_3rd_derivative_v042_signal'] = f69oc_f69_operating_cash_flow_stability_calc042_5d_3rd_derivative_v042_signal

def f69oc_f69_operating_cash_flow_stability_calc043_252d_3rd_derivative_v043_signal(ncfo):
    res = (ncfo.rolling(252).std() / ncfo.rolling(252).mean().abs()).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc043_252d_3rd_derivative_v043_signal'] = f69oc_f69_operating_cash_flow_stability_calc043_252d_3rd_derivative_v043_signal

def f69oc_f69_operating_cash_flow_stability_calc044_80d_3rd_derivative_v044_signal(ncfo):
    res = ((ncfo - ncfo.shift(80)).rolling(80).skew()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc044_80d_3rd_derivative_v044_signal'] = f69oc_f69_operating_cash_flow_stability_calc044_80d_3rd_derivative_v044_signal

def f69oc_f69_operating_cash_flow_stability_calc045_15d_3rd_derivative_v045_signal(assets, capex, ncfo):
    res = ((ncfo * capex / assets.replace(0, np.nan)).pct_change(1)).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc045_15d_3rd_derivative_v045_signal'] = f69oc_f69_operating_cash_flow_stability_calc045_15d_3rd_derivative_v045_signal

def f69oc_f69_operating_cash_flow_stability_calc046_42d_3rd_derivative_v046_signal(marketcap, ncfo):
    res = ((ncfo * marketcap).rolling(42).std() / (ncfo * marketcap).rolling(42).mean().abs()).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc046_42d_3rd_derivative_v046_signal'] = f69oc_f69_operating_cash_flow_stability_calc046_42d_3rd_derivative_v046_signal

def f69oc_f69_operating_cash_flow_stability_calc047_10d_3rd_derivative_v047_signal(ncfo):
    res = (ncfo.rolling(10).std() / ncfo.rolling(10).mean().abs()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc047_10d_3rd_derivative_v047_signal'] = f69oc_f69_operating_cash_flow_stability_calc047_10d_3rd_derivative_v047_signal

def f69oc_f69_operating_cash_flow_stability_calc048_63d_3rd_derivative_v048_signal(intexp, ncfo):
    res = (np.log((ncfo.abs() + 1) / (intexp.abs() + 1)).rolling(63).std()).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc048_63d_3rd_derivative_v048_signal'] = f69oc_f69_operating_cash_flow_stability_calc048_63d_3rd_derivative_v048_signal

def f69oc_f69_operating_cash_flow_stability_calc049_252d_3rd_derivative_v049_signal(ncfo):
    res = (ncfo.rolling(252).median().pct_change(50)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc049_252d_3rd_derivative_v049_signal'] = f69oc_f69_operating_cash_flow_stability_calc049_252d_3rd_derivative_v049_signal

def f69oc_f69_operating_cash_flow_stability_calc050_5d_3rd_derivative_v050_signal(ncfo):
    res = (ncfo.rolling(5).rank(pct=True).diff(1)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc050_5d_3rd_derivative_v050_signal'] = f69oc_f69_operating_cash_flow_stability_calc050_5d_3rd_derivative_v050_signal

def f69oc_f69_operating_cash_flow_stability_calc051_42d_3rd_derivative_v051_signal(ncfo, pb):
    res = ((ncfo / pb.replace(0, np.nan)).rolling(42).kurt()).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc051_42d_3rd_derivative_v051_signal'] = f69oc_f69_operating_cash_flow_stability_calc051_42d_3rd_derivative_v051_signal

def f69oc_f69_operating_cash_flow_stability_calc052_30d_3rd_derivative_v052_signal(ncfo, workingcapital):
    res = ((ncfo / workingcapital.replace(0, np.nan)).rolling(30).quantile(0.9)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc052_30d_3rd_derivative_v052_signal'] = f69oc_f69_operating_cash_flow_stability_calc052_30d_3rd_derivative_v052_signal

def f69oc_f69_operating_cash_flow_stability_calc053_15d_3rd_derivative_v053_signal(ev, ncfo):
    res = (np.log((ncfo.abs() + 1) / (ev.abs() + 1)).rolling(15).std()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc053_15d_3rd_derivative_v053_signal'] = f69oc_f69_operating_cash_flow_stability_calc053_15d_3rd_derivative_v053_signal

def f69oc_f69_operating_cash_flow_stability_calc054_80d_3rd_derivative_v054_signal(evebit, ncfo):
    res = ((ncfo - evebit.rolling(80).mean()).rolling(80).std()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc054_80d_3rd_derivative_v054_signal'] = f69oc_f69_operating_cash_flow_stability_calc054_80d_3rd_derivative_v054_signal

def f69oc_f69_operating_cash_flow_stability_calc055_252d_3rd_derivative_v055_signal(ncfo, taxexp):
    res = ((ncfo / taxexp.replace(0, np.nan)).rolling(252).mean().diff(25)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc055_252d_3rd_derivative_v055_signal'] = f69oc_f69_operating_cash_flow_stability_calc055_252d_3rd_derivative_v055_signal

def f69oc_f69_operating_cash_flow_stability_calc056_21d_3rd_derivative_v056_signal(low, ncfo):
    res = ((ncfo / low.replace(0, np.nan)).rolling(21).mean().diff(2)).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc056_21d_3rd_derivative_v056_signal'] = f69oc_f69_operating_cash_flow_stability_calc056_21d_3rd_derivative_v056_signal

def f69oc_f69_operating_cash_flow_stability_calc057_150d_3rd_derivative_v057_signal(ncfo, opinc, workingcapital):
    res = ((ncfo.rolling(150).mean() - opinc.rolling(150).mean()) / workingcapital.replace(0, np.nan).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc057_150d_3rd_derivative_v057_signal'] = f69oc_f69_operating_cash_flow_stability_calc057_150d_3rd_derivative_v057_signal

def f69oc_f69_operating_cash_flow_stability_calc058_50d_3rd_derivative_v058_signal(capex, ncfo):
    res = ((capex / ncfo.replace(0, np.nan)).rolling(50).mean()).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc058_50d_3rd_derivative_v058_signal'] = f69oc_f69_operating_cash_flow_stability_calc058_50d_3rd_derivative_v058_signal

def f69oc_f69_operating_cash_flow_stability_calc059_21d_3rd_derivative_v059_signal(low, ncfo):
    res = ((ncfo.diff(21) / low.replace(0, np.nan).diff(21)).rolling(21).mean()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc059_21d_3rd_derivative_v059_signal'] = f69oc_f69_operating_cash_flow_stability_calc059_21d_3rd_derivative_v059_signal

def f69oc_f69_operating_cash_flow_stability_calc060_50d_3rd_derivative_v060_signal(assets, ncfo):
    res = ((ncfo * assets).rolling(50).std() / (ncfo * assets).rolling(50).mean().abs()).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc060_50d_3rd_derivative_v060_signal'] = f69oc_f69_operating_cash_flow_stability_calc060_50d_3rd_derivative_v060_signal

def f69oc_f69_operating_cash_flow_stability_calc061_63d_3rd_derivative_v061_signal(evebit, ncfo):
    res = ((ncfo / evebit.replace(0, np.nan)).rolling(63).kurt()).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc061_63d_3rd_derivative_v061_signal'] = f69oc_f69_operating_cash_flow_stability_calc061_63d_3rd_derivative_v061_signal

def f69oc_f69_operating_cash_flow_stability_calc062_80d_3rd_derivative_v062_signal(liabilities, ncfo, ps):
    res = ((ncfo * ps / liabilities.replace(0, np.nan)).pct_change(8)).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc062_80d_3rd_derivative_v062_signal'] = f69oc_f69_operating_cash_flow_stability_calc062_80d_3rd_derivative_v062_signal

def f69oc_f69_operating_cash_flow_stability_calc063_5d_3rd_derivative_v063_signal(ncfo, opinc):
    res = ((ncfo / opinc.replace(0, np.nan)).rolling(5).std().pct_change(1)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc063_5d_3rd_derivative_v063_signal'] = f69oc_f69_operating_cash_flow_stability_calc063_5d_3rd_derivative_v063_signal

def f69oc_f69_operating_cash_flow_stability_calc064_21d_3rd_derivative_v064_signal(ncfo):
    res = (ncfo.pct_change(21).rolling(21).kurt()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc064_21d_3rd_derivative_v064_signal'] = f69oc_f69_operating_cash_flow_stability_calc064_21d_3rd_derivative_v064_signal

def f69oc_f69_operating_cash_flow_stability_calc065_50d_3rd_derivative_v065_signal(ncfo):
    res = ((ncfo.rolling(50).max() - ncfo.rolling(50).min()) / ncfo.rolling(50).std()).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc065_50d_3rd_derivative_v065_signal'] = f69oc_f69_operating_cash_flow_stability_calc065_50d_3rd_derivative_v065_signal

def f69oc_f69_operating_cash_flow_stability_calc066_100d_3rd_derivative_v066_signal(ncfo, revenue):
    res = ((ncfo / revenue.replace(0, np.nan)).rolling(100).quantile(0.9)).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc066_100d_3rd_derivative_v066_signal'] = f69oc_f69_operating_cash_flow_stability_calc066_100d_3rd_derivative_v066_signal

def f69oc_f69_operating_cash_flow_stability_calc067_5d_3rd_derivative_v067_signal(ncfo, workingcapital):
    res = ((ncfo / workingcapital.replace(0, np.nan)).rolling(5).skew().diff(5)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc067_5d_3rd_derivative_v067_signal'] = f69oc_f69_operating_cash_flow_stability_calc067_5d_3rd_derivative_v067_signal

def f69oc_f69_operating_cash_flow_stability_calc068_200d_3rd_derivative_v068_signal(ncfo):
    res = ((ncfo / ncfo.replace(0, np.nan)).rolling(200).quantile(0.9)).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc068_200d_3rd_derivative_v068_signal'] = f69oc_f69_operating_cash_flow_stability_calc068_200d_3rd_derivative_v068_signal

def f69oc_f69_operating_cash_flow_stability_calc069_42d_3rd_derivative_v069_signal(equity, ncfo):
    res = ((ncfo / equity.replace(0, np.nan)).rolling(42).skew().diff(5)).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc069_42d_3rd_derivative_v069_signal'] = f69oc_f69_operating_cash_flow_stability_calc069_42d_3rd_derivative_v069_signal

def f69oc_f69_operating_cash_flow_stability_calc070_50d_3rd_derivative_v070_signal(ncfo):
    res = (ncfo.rolling(50).median().pct_change(10)).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc070_50d_3rd_derivative_v070_signal'] = f69oc_f69_operating_cash_flow_stability_calc070_50d_3rd_derivative_v070_signal

def f69oc_f69_operating_cash_flow_stability_calc071_252d_3rd_derivative_v071_signal(ncfo, taxexp):
    res = (ncfo.rolling(252).var() / taxexp.rolling(252).var().replace(0, np.nan)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc071_252d_3rd_derivative_v071_signal'] = f69oc_f69_operating_cash_flow_stability_calc071_252d_3rd_derivative_v071_signal

def f69oc_f69_operating_cash_flow_stability_calc072_30d_3rd_derivative_v072_signal(marketcap, ncfo):
    res = ((ncfo / marketcap.replace(0, np.nan)).rolling(30).mean().diff(3)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc072_30d_3rd_derivative_v072_signal'] = f69oc_f69_operating_cash_flow_stability_calc072_30d_3rd_derivative_v072_signal

def f69oc_f69_operating_cash_flow_stability_calc073_42d_3rd_derivative_v073_signal(ncfo):
    res = (ncfo.pct_change(42).rolling(42).kurt()).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc073_42d_3rd_derivative_v073_signal'] = f69oc_f69_operating_cash_flow_stability_calc073_42d_3rd_derivative_v073_signal

def f69oc_f69_operating_cash_flow_stability_calc074_200d_3rd_derivative_v074_signal(ncff, ncfo):
    res = ((ncfo / ncff.replace(0, np.nan)).rolling(200).mean().diff(20)).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc074_200d_3rd_derivative_v074_signal'] = f69oc_f69_operating_cash_flow_stability_calc074_200d_3rd_derivative_v074_signal

def f69oc_f69_operating_cash_flow_stability_calc075_63d_3rd_derivative_v075_signal(ncfo):
    res = ((ncfo.rolling(63).max() / ncfo.rolling(63).min()).pct_change(5)).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc075_63d_3rd_derivative_v075_signal'] = f69oc_f69_operating_cash_flow_stability_calc075_63d_3rd_derivative_v075_signal

def f69oc_f69_operating_cash_flow_stability_calc076_10d_3rd_derivative_v076_signal(capex, ncfo):
    res = (np.log((ncfo.abs() + 1) / (capex.abs() + 1)).rolling(10).std()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc076_10d_3rd_derivative_v076_signal'] = f69oc_f69_operating_cash_flow_stability_calc076_10d_3rd_derivative_v076_signal

def f69oc_f69_operating_cash_flow_stability_calc077_10d_3rd_derivative_v077_signal(ncfo):
    res = ((ncfo.rolling(10).rank(pct=True)).rolling(10).std()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc077_10d_3rd_derivative_v077_signal'] = f69oc_f69_operating_cash_flow_stability_calc077_10d_3rd_derivative_v077_signal

def f69oc_f69_operating_cash_flow_stability_calc078_15d_3rd_derivative_v078_signal(ncfo, pe):
    res = ((ncfo / pe.replace(0, np.nan)).rolling(15).mean().diff(1)).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc078_15d_3rd_derivative_v078_signal'] = f69oc_f69_operating_cash_flow_stability_calc078_15d_3rd_derivative_v078_signal

def f69oc_f69_operating_cash_flow_stability_calc079_30d_3rd_derivative_v079_signal(assets, ncfo):
    res = ((ncfo - assets.rolling(30).mean()).rolling(30).std()).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc079_30d_3rd_derivative_v079_signal'] = f69oc_f69_operating_cash_flow_stability_calc079_30d_3rd_derivative_v079_signal

def f69oc_f69_operating_cash_flow_stability_calc080_126d_3rd_derivative_v080_signal(ncfo):
    res = (ncfo.pct_change(126).rolling(126).kurt()).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc080_126d_3rd_derivative_v080_signal'] = f69oc_f69_operating_cash_flow_stability_calc080_126d_3rd_derivative_v080_signal

def f69oc_f69_operating_cash_flow_stability_calc081_126d_3rd_derivative_v081_signal(fcf, gp, ncfo):
    res = ((ncfo * gp / fcf.replace(0, np.nan)).pct_change(12)).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc081_126d_3rd_derivative_v081_signal'] = f69oc_f69_operating_cash_flow_stability_calc081_126d_3rd_derivative_v081_signal

def f69oc_f69_operating_cash_flow_stability_calc082_200d_3rd_derivative_v082_signal(marketcap, ncfo, taxexp):
    res = ((ncfo.rolling(200).mean() - marketcap.rolling(200).mean()) / taxexp.replace(0, np.nan).rolling(200).std()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc082_200d_3rd_derivative_v082_signal'] = f69oc_f69_operating_cash_flow_stability_calc082_200d_3rd_derivative_v082_signal

def f69oc_f69_operating_cash_flow_stability_calc083_80d_3rd_derivative_v083_signal(ncfo, open):
    res = ((ncfo - open.rolling(80).mean()).rolling(80).std()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc083_80d_3rd_derivative_v083_signal'] = f69oc_f69_operating_cash_flow_stability_calc083_80d_3rd_derivative_v083_signal

def f69oc_f69_operating_cash_flow_stability_calc084_50d_3rd_derivative_v084_signal(ncfo):
    res = ((ncfo.rolling(50).max() / ncfo.rolling(50).min()).pct_change(5)).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc084_50d_3rd_derivative_v084_signal'] = f69oc_f69_operating_cash_flow_stability_calc084_50d_3rd_derivative_v084_signal

def f69oc_f69_operating_cash_flow_stability_calc085_126d_3rd_derivative_v085_signal(ncfi, ncfo):
    res = ((ncfo.rolling(126).max() - ncfo.rolling(126).min()) / ncfi.replace(0, np.nan)).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc085_126d_3rd_derivative_v085_signal'] = f69oc_f69_operating_cash_flow_stability_calc085_126d_3rd_derivative_v085_signal

def f69oc_f69_operating_cash_flow_stability_calc086_150d_3rd_derivative_v086_signal(ncfo):
    res = ((ncfo - ncfo.shift(150)).rolling(150).skew()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc086_150d_3rd_derivative_v086_signal'] = f69oc_f69_operating_cash_flow_stability_calc086_150d_3rd_derivative_v086_signal

def f69oc_f69_operating_cash_flow_stability_calc087_126d_3rd_derivative_v087_signal(ncfo):
    res = (ncfo.rolling(126).median().pct_change(25)).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc087_126d_3rd_derivative_v087_signal'] = f69oc_f69_operating_cash_flow_stability_calc087_126d_3rd_derivative_v087_signal

def f69oc_f69_operating_cash_flow_stability_calc088_80d_3rd_derivative_v088_signal(ncfo):
    res = ((ncfo.rolling(80).rank(pct=True)).rolling(80).std()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc088_80d_3rd_derivative_v088_signal'] = f69oc_f69_operating_cash_flow_stability_calc088_80d_3rd_derivative_v088_signal

def f69oc_f69_operating_cash_flow_stability_calc089_126d_3rd_derivative_v089_signal(capex, ncfo):
    res = (np.log((ncfo.abs() + 1) / (capex.abs() + 1)).rolling(126).std()).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc089_126d_3rd_derivative_v089_signal'] = f69oc_f69_operating_cash_flow_stability_calc089_126d_3rd_derivative_v089_signal

def f69oc_f69_operating_cash_flow_stability_calc090_21d_3rd_derivative_v090_signal(eps, marketcap, ncfo):
    res = ((ncfo.rolling(21).mean() - eps.rolling(21).mean()) / marketcap.replace(0, np.nan).rolling(21).std()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc090_21d_3rd_derivative_v090_signal'] = f69oc_f69_operating_cash_flow_stability_calc090_21d_3rd_derivative_v090_signal

def f69oc_f69_operating_cash_flow_stability_calc091_150d_3rd_derivative_v091_signal(ev, ncfo):
    res = ((ncfo - ev.rolling(150).mean()).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc091_150d_3rd_derivative_v091_signal'] = f69oc_f69_operating_cash_flow_stability_calc091_150d_3rd_derivative_v091_signal

def f69oc_f69_operating_cash_flow_stability_calc092_200d_3rd_derivative_v092_signal(ncfo):
    res = (ncfo.rolling(200).std() / ncfo.rolling(200).mean().abs()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc092_200d_3rd_derivative_v092_signal'] = f69oc_f69_operating_cash_flow_stability_calc092_200d_3rd_derivative_v092_signal

def f69oc_f69_operating_cash_flow_stability_calc093_15d_3rd_derivative_v093_signal(currentratio, ncfo):
    res = ((ncfo.diff(15) / currentratio.replace(0, np.nan).diff(15)).rolling(15).mean()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc093_15d_3rd_derivative_v093_signal'] = f69oc_f69_operating_cash_flow_stability_calc093_15d_3rd_derivative_v093_signal

def f69oc_f69_operating_cash_flow_stability_calc094_30d_3rd_derivative_v094_signal(ncfo, sharesbas):
    res = (ncfo.rolling(30).quantile(0.3) - sharesbas.rolling(30).quantile(0.7)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc094_30d_3rd_derivative_v094_signal'] = f69oc_f69_operating_cash_flow_stability_calc094_30d_3rd_derivative_v094_signal

def f69oc_f69_operating_cash_flow_stability_calc095_252d_3rd_derivative_v095_signal(eps, ncfo):
    res = (ncfo.rolling(252).quantile(0.3) - eps.rolling(252).quantile(0.7)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc095_252d_3rd_derivative_v095_signal'] = f69oc_f69_operating_cash_flow_stability_calc095_252d_3rd_derivative_v095_signal

def f69oc_f69_operating_cash_flow_stability_calc096_42d_3rd_derivative_v096_signal(close, ncfo):
    res = ((close / ncfo.replace(0, np.nan)).rolling(42).mean()).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc096_42d_3rd_derivative_v096_signal'] = f69oc_f69_operating_cash_flow_stability_calc096_42d_3rd_derivative_v096_signal

def f69oc_f69_operating_cash_flow_stability_calc097_150d_3rd_derivative_v097_signal(currentratio, ebitda, ncfo):
    res = ((ncfo * ebitda / currentratio.replace(0, np.nan)).pct_change(15)).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc097_150d_3rd_derivative_v097_signal'] = f69oc_f69_operating_cash_flow_stability_calc097_150d_3rd_derivative_v097_signal

def f69oc_f69_operating_cash_flow_stability_calc098_150d_3rd_derivative_v098_signal(ncfo):
    res = (np.log((ncfo.abs() + 1) / (ncfo.abs() + 1)).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc098_150d_3rd_derivative_v098_signal'] = f69oc_f69_operating_cash_flow_stability_calc098_150d_3rd_derivative_v098_signal

def f69oc_f69_operating_cash_flow_stability_calc099_80d_3rd_derivative_v099_signal(liabilities, ncfo):
    res = ((ncfo * liabilities).rolling(80).std() / (ncfo * liabilities).rolling(80).mean().abs()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc099_80d_3rd_derivative_v099_signal'] = f69oc_f69_operating_cash_flow_stability_calc099_80d_3rd_derivative_v099_signal

def f69oc_f69_operating_cash_flow_stability_calc100_50d_3rd_derivative_v100_signal(intexp, ncfo):
    res = ((ncfo / intexp.replace(0, np.nan)).rolling(50).std().pct_change(10)).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc100_50d_3rd_derivative_v100_signal'] = f69oc_f69_operating_cash_flow_stability_calc100_50d_3rd_derivative_v100_signal

def f69oc_f69_operating_cash_flow_stability_calc101_150d_3rd_derivative_v101_signal(ncfo):
    res = ((ncfo.rolling(150).rank(pct=True)).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc101_150d_3rd_derivative_v101_signal'] = f69oc_f69_operating_cash_flow_stability_calc101_150d_3rd_derivative_v101_signal

def f69oc_f69_operating_cash_flow_stability_calc102_50d_3rd_derivative_v102_signal(equity, ncfo, workingcapital):
    res = ((ncfo.rolling(50).mean() - equity.rolling(50).mean()) / workingcapital.replace(0, np.nan).rolling(50).std()).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc102_50d_3rd_derivative_v102_signal'] = f69oc_f69_operating_cash_flow_stability_calc102_50d_3rd_derivative_v102_signal

def f69oc_f69_operating_cash_flow_stability_calc103_10d_3rd_derivative_v103_signal(ncfo, pb):
    res = ((ncfo - pb).diff(10).rolling(10).mean()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc103_10d_3rd_derivative_v103_signal'] = f69oc_f69_operating_cash_flow_stability_calc103_10d_3rd_derivative_v103_signal

def f69oc_f69_operating_cash_flow_stability_calc104_30d_3rd_derivative_v104_signal(ncff, ncfo):
    res = ((ncfo / ncff.replace(0, np.nan)).rolling(30).quantile(0.9)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc104_30d_3rd_derivative_v104_signal'] = f69oc_f69_operating_cash_flow_stability_calc104_30d_3rd_derivative_v104_signal

def f69oc_f69_operating_cash_flow_stability_calc105_100d_3rd_derivative_v105_signal(ncfo, open):
    res = (ncfo.rolling(100).var() / open.rolling(100).var().replace(0, np.nan)).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc105_100d_3rd_derivative_v105_signal'] = f69oc_f69_operating_cash_flow_stability_calc105_100d_3rd_derivative_v105_signal

def f69oc_f69_operating_cash_flow_stability_calc106_252d_3rd_derivative_v106_signal(ncfo, taxexp):
    res = ((ncfo.rolling(252).max() - ncfo.rolling(252).min()) / taxexp.replace(0, np.nan)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc106_252d_3rd_derivative_v106_signal'] = f69oc_f69_operating_cash_flow_stability_calc106_252d_3rd_derivative_v106_signal

def f69oc_f69_operating_cash_flow_stability_calc107_252d_3rd_derivative_v107_signal(evebitda, ncfo):
    res = ((ncfo / evebitda.replace(0, np.nan)).rolling(252).mean().diff(25)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc107_252d_3rd_derivative_v107_signal'] = f69oc_f69_operating_cash_flow_stability_calc107_252d_3rd_derivative_v107_signal

def f69oc_f69_operating_cash_flow_stability_calc108_15d_3rd_derivative_v108_signal(intexp, ncfo):
    res = ((ncfo - intexp).diff(15).rolling(15).mean()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc108_15d_3rd_derivative_v108_signal'] = f69oc_f69_operating_cash_flow_stability_calc108_15d_3rd_derivative_v108_signal

def f69oc_f69_operating_cash_flow_stability_calc109_63d_3rd_derivative_v109_signal(intexp, ncfo):
    res = ((ncfo / intexp.replace(0, np.nan)).rolling(63).quantile(0.9)).diff(1).rolling(63).mean().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc109_63d_3rd_derivative_v109_signal'] = f69oc_f69_operating_cash_flow_stability_calc109_63d_3rd_derivative_v109_signal

def f69oc_f69_operating_cash_flow_stability_calc110_30d_3rd_derivative_v110_signal(ncfo, workingcapital):
    res = ((ncfo / workingcapital.replace(0, np.nan)).rolling(30).mean().diff(3)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc110_30d_3rd_derivative_v110_signal'] = f69oc_f69_operating_cash_flow_stability_calc110_30d_3rd_derivative_v110_signal

def f69oc_f69_operating_cash_flow_stability_calc111_10d_3rd_derivative_v111_signal(ncfo):
    res = (ncfo.rolling(10).median().pct_change(2)).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc111_10d_3rd_derivative_v111_signal'] = f69oc_f69_operating_cash_flow_stability_calc111_10d_3rd_derivative_v111_signal

def f69oc_f69_operating_cash_flow_stability_calc112_252d_3rd_derivative_v112_signal(equity, low, ncfo):
    res = ((ncfo.rolling(252).mean() - equity.rolling(252).mean()) / low.replace(0, np.nan).rolling(252).std()).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc112_252d_3rd_derivative_v112_signal'] = f69oc_f69_operating_cash_flow_stability_calc112_252d_3rd_derivative_v112_signal

def f69oc_f69_operating_cash_flow_stability_calc113_10d_3rd_derivative_v113_signal(ncfo):
    res = (ncfo.pct_change(10).rolling(10).kurt()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc113_10d_3rd_derivative_v113_signal'] = f69oc_f69_operating_cash_flow_stability_calc113_10d_3rd_derivative_v113_signal

def f69oc_f69_operating_cash_flow_stability_calc114_15d_3rd_derivative_v114_signal(fcf, ncfo):
    res = ((ncfo.diff(15) / fcf.replace(0, np.nan).diff(15)).rolling(15).mean()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc114_15d_3rd_derivative_v114_signal'] = f69oc_f69_operating_cash_flow_stability_calc114_15d_3rd_derivative_v114_signal

def f69oc_f69_operating_cash_flow_stability_calc115_150d_3rd_derivative_v115_signal(gp, ncfo):
    res = (np.log((ncfo.abs() + 1) / (gp.abs() + 1)).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc115_150d_3rd_derivative_v115_signal'] = f69oc_f69_operating_cash_flow_stability_calc115_150d_3rd_derivative_v115_signal

def f69oc_f69_operating_cash_flow_stability_calc116_15d_3rd_derivative_v116_signal(high, ncfo):
    res = ((ncfo / high.replace(0, np.nan)).rolling(15).mean().diff(1)).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc116_15d_3rd_derivative_v116_signal'] = f69oc_f69_operating_cash_flow_stability_calc116_15d_3rd_derivative_v116_signal

def f69oc_f69_operating_cash_flow_stability_calc117_42d_3rd_derivative_v117_signal(ncfo, volume):
    res = ((ncfo.rolling(42).max() - volume.rolling(42).min()) / volume.rolling(42).std()).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc117_42d_3rd_derivative_v117_signal'] = f69oc_f69_operating_cash_flow_stability_calc117_42d_3rd_derivative_v117_signal

def f69oc_f69_operating_cash_flow_stability_calc118_15d_3rd_derivative_v118_signal(ncfo):
    res = (ncfo.pct_change(15).rolling(15).kurt()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc118_15d_3rd_derivative_v118_signal'] = f69oc_f69_operating_cash_flow_stability_calc118_15d_3rd_derivative_v118_signal

def f69oc_f69_operating_cash_flow_stability_calc119_30d_3rd_derivative_v119_signal(ncfo):
    res = (ncfo.rolling(30).median().pct_change(6)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc119_30d_3rd_derivative_v119_signal'] = f69oc_f69_operating_cash_flow_stability_calc119_30d_3rd_derivative_v119_signal

def f69oc_f69_operating_cash_flow_stability_calc120_15d_3rd_derivative_v120_signal(ncfo, workingcapital):
    res = ((ncfo / workingcapital.replace(0, np.nan)).rolling(15).kurt()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc120_15d_3rd_derivative_v120_signal'] = f69oc_f69_operating_cash_flow_stability_calc120_15d_3rd_derivative_v120_signal

def f69oc_f69_operating_cash_flow_stability_calc121_100d_3rd_derivative_v121_signal(closeadj, ncfo):
    res = ((ncfo.diff(100) / closeadj.replace(0, np.nan).diff(100)).rolling(100).mean()).diff(1).rolling(100).mean().diff(1).rolling(100).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc121_100d_3rd_derivative_v121_signal'] = f69oc_f69_operating_cash_flow_stability_calc121_100d_3rd_derivative_v121_signal

def f69oc_f69_operating_cash_flow_stability_calc122_30d_3rd_derivative_v122_signal(intexp, ncfo):
    res = ((ncfo * intexp).rolling(30).std() / (ncfo * intexp).rolling(30).mean().abs()).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc122_30d_3rd_derivative_v122_signal'] = f69oc_f69_operating_cash_flow_stability_calc122_30d_3rd_derivative_v122_signal

def f69oc_f69_operating_cash_flow_stability_calc123_200d_3rd_derivative_v123_signal(ev, ncfo):
    res = ((ncfo - ev.rolling(200).mean()).rolling(200).std()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc123_200d_3rd_derivative_v123_signal'] = f69oc_f69_operating_cash_flow_stability_calc123_200d_3rd_derivative_v123_signal

def f69oc_f69_operating_cash_flow_stability_calc124_252d_3rd_derivative_v124_signal(ncff, ncfo):
    res = ((ncfo - ncff.rolling(252).mean()).rolling(252).std()).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc124_252d_3rd_derivative_v124_signal'] = f69oc_f69_operating_cash_flow_stability_calc124_252d_3rd_derivative_v124_signal

def f69oc_f69_operating_cash_flow_stability_calc125_30d_3rd_derivative_v125_signal(high, ncff, ncfo):
    res = ((ncfo * high / ncff.replace(0, np.nan)).pct_change(3)).diff(1).rolling(30).mean().diff(1).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc125_30d_3rd_derivative_v125_signal'] = f69oc_f69_operating_cash_flow_stability_calc125_30d_3rd_derivative_v125_signal

def f69oc_f69_operating_cash_flow_stability_calc126_200d_3rd_derivative_v126_signal(ncfo, taxexp):
    res = (ncfo.rolling(200).var() / taxexp.rolling(200).var().replace(0, np.nan)).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc126_200d_3rd_derivative_v126_signal'] = f69oc_f69_operating_cash_flow_stability_calc126_200d_3rd_derivative_v126_signal

def f69oc_f69_operating_cash_flow_stability_calc127_126d_3rd_derivative_v127_signal(assets, ncfo):
    res = ((ncfo / assets.replace(0, np.nan)).rolling(126).mean().diff(12)).diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc127_126d_3rd_derivative_v127_signal'] = f69oc_f69_operating_cash_flow_stability_calc127_126d_3rd_derivative_v127_signal

def f69oc_f69_operating_cash_flow_stability_calc128_200d_3rd_derivative_v128_signal(ncfi, ncfo):
    res = ((ncfo * ncfi).rolling(200).std() / (ncfo * ncfi).rolling(200).mean().abs()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc128_200d_3rd_derivative_v128_signal'] = f69oc_f69_operating_cash_flow_stability_calc128_200d_3rd_derivative_v128_signal

def f69oc_f69_operating_cash_flow_stability_calc129_21d_3rd_derivative_v129_signal(fcf, ncfo):
    res = ((ncfo / fcf.replace(0, np.nan)).rolling(21).quantile(0.9)).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc129_21d_3rd_derivative_v129_signal'] = f69oc_f69_operating_cash_flow_stability_calc129_21d_3rd_derivative_v129_signal

def f69oc_f69_operating_cash_flow_stability_calc130_15d_3rd_derivative_v130_signal(ncfo, revenue):
    res = ((ncfo / revenue.replace(0, np.nan)).rolling(15).std().pct_change(3)).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc130_15d_3rd_derivative_v130_signal'] = f69oc_f69_operating_cash_flow_stability_calc130_15d_3rd_derivative_v130_signal

def f69oc_f69_operating_cash_flow_stability_calc131_252d_3rd_derivative_v131_signal(ncfo, volume):
    res = ((ncfo / volume.replace(0, np.nan)).rolling(252).skew().diff(5)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc131_252d_3rd_derivative_v131_signal'] = f69oc_f69_operating_cash_flow_stability_calc131_252d_3rd_derivative_v131_signal

def f69oc_f69_operating_cash_flow_stability_calc132_21d_3rd_derivative_v132_signal(ncfo, opinc):
    res = ((ncfo - opinc.rolling(21).mean()).rolling(21).std()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc132_21d_3rd_derivative_v132_signal'] = f69oc_f69_operating_cash_flow_stability_calc132_21d_3rd_derivative_v132_signal

def f69oc_f69_operating_cash_flow_stability_calc133_15d_3rd_derivative_v133_signal(close, ncfo):
    res = ((ncfo / close.replace(0, np.nan)).rolling(15).kurt()).diff(1).rolling(15).mean().diff(1).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc133_15d_3rd_derivative_v133_signal'] = f69oc_f69_operating_cash_flow_stability_calc133_15d_3rd_derivative_v133_signal

def f69oc_f69_operating_cash_flow_stability_calc134_252d_3rd_derivative_v134_signal(ncfo, pe):
    res = (ncfo.rolling(252).quantile(0.3) - pe.rolling(252).quantile(0.7)).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc134_252d_3rd_derivative_v134_signal'] = f69oc_f69_operating_cash_flow_stability_calc134_252d_3rd_derivative_v134_signal

def f69oc_f69_operating_cash_flow_stability_calc135_5d_3rd_derivative_v135_signal(debt, ncfo):
    res = (ncfo.rolling(5).var() / debt.rolling(5).var().replace(0, np.nan)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc135_5d_3rd_derivative_v135_signal'] = f69oc_f69_operating_cash_flow_stability_calc135_5d_3rd_derivative_v135_signal

def f69oc_f69_operating_cash_flow_stability_calc136_252d_3rd_derivative_v136_signal(ncff, ncfo):
    res = ((ncfo / ncff.replace(0, np.nan)).rolling(252).kurt()).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc136_252d_3rd_derivative_v136_signal'] = f69oc_f69_operating_cash_flow_stability_calc136_252d_3rd_derivative_v136_signal

def f69oc_f69_operating_cash_flow_stability_calc137_21d_3rd_derivative_v137_signal(ncfo, sharesbas):
    res = (np.log((ncfo.abs() + 1) / (sharesbas.abs() + 1)).rolling(21).std()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc137_21d_3rd_derivative_v137_signal'] = f69oc_f69_operating_cash_flow_stability_calc137_21d_3rd_derivative_v137_signal

def f69oc_f69_operating_cash_flow_stability_calc138_80d_3rd_derivative_v138_signal(high, ncfo):
    res = ((ncfo.diff(80) / high.replace(0, np.nan).diff(80)).rolling(80).mean()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc138_80d_3rd_derivative_v138_signal'] = f69oc_f69_operating_cash_flow_stability_calc138_80d_3rd_derivative_v138_signal

def f69oc_f69_operating_cash_flow_stability_calc139_42d_3rd_derivative_v139_signal(eps, ncfo):
    res = ((ncfo / eps.replace(0, np.nan)).rolling(42).mean().diff(4)).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc139_42d_3rd_derivative_v139_signal'] = f69oc_f69_operating_cash_flow_stability_calc139_42d_3rd_derivative_v139_signal

def f69oc_f69_operating_cash_flow_stability_calc140_50d_3rd_derivative_v140_signal(capex, ncfo):
    res = (ncfo.rolling(50).quantile(0.3) - capex.rolling(50).quantile(0.7)).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc140_50d_3rd_derivative_v140_signal'] = f69oc_f69_operating_cash_flow_stability_calc140_50d_3rd_derivative_v140_signal

def f69oc_f69_operating_cash_flow_stability_calc141_80d_3rd_derivative_v141_signal(currentratio, ncfo):
    res = (ncfo.rolling(80).std() / currentratio.replace(0, np.nan).rolling(80).std()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc141_80d_3rd_derivative_v141_signal'] = f69oc_f69_operating_cash_flow_stability_calc141_80d_3rd_derivative_v141_signal

def f69oc_f69_operating_cash_flow_stability_calc142_200d_3rd_derivative_v142_signal(ncfo, retearn):
    res = (np.log((ncfo.abs() + 1) / (retearn.abs() + 1)).rolling(200).std()).diff(1).rolling(200).mean().diff(1).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc142_200d_3rd_derivative_v142_signal'] = f69oc_f69_operating_cash_flow_stability_calc142_200d_3rd_derivative_v142_signal

def f69oc_f69_operating_cash_flow_stability_calc143_21d_3rd_derivative_v143_signal(capex, ncfo):
    res = ((capex / ncfo.replace(0, np.nan)).rolling(21).mean()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc143_21d_3rd_derivative_v143_signal'] = f69oc_f69_operating_cash_flow_stability_calc143_21d_3rd_derivative_v143_signal

def f69oc_f69_operating_cash_flow_stability_calc144_50d_3rd_derivative_v144_signal(fcf, ncfo):
    res = (ncfo.rolling(50).quantile(0.3) - fcf.rolling(50).quantile(0.7)).diff(1).rolling(50).mean().diff(1).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc144_50d_3rd_derivative_v144_signal'] = f69oc_f69_operating_cash_flow_stability_calc144_50d_3rd_derivative_v144_signal

def f69oc_f69_operating_cash_flow_stability_calc145_5d_3rd_derivative_v145_signal(debt, ncfo):
    res = ((ncfo / debt.replace(0, np.nan)).rolling(5).skew().diff(5)).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc145_5d_3rd_derivative_v145_signal'] = f69oc_f69_operating_cash_flow_stability_calc145_5d_3rd_derivative_v145_signal

def f69oc_f69_operating_cash_flow_stability_calc146_150d_3rd_derivative_v146_signal(closeadj, evebitda, ncfo):
    res = ((ncfo.rolling(150).mean() - evebitda.rolling(150).mean()) / closeadj.replace(0, np.nan).rolling(150).std()).diff(1).rolling(150).mean().diff(1).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc146_150d_3rd_derivative_v146_signal'] = f69oc_f69_operating_cash_flow_stability_calc146_150d_3rd_derivative_v146_signal

def f69oc_f69_operating_cash_flow_stability_calc147_21d_3rd_derivative_v147_signal(ncfo, opinc):
    res = (np.log((ncfo.abs() + 1) / (opinc.abs() + 1)).rolling(21).std()).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc147_21d_3rd_derivative_v147_signal'] = f69oc_f69_operating_cash_flow_stability_calc147_21d_3rd_derivative_v147_signal

def f69oc_f69_operating_cash_flow_stability_calc148_42d_3rd_derivative_v148_signal(closeadj, ncfo):
    res = ((ncfo.rolling(42).max() - ncfo.rolling(42).min()) / closeadj.replace(0, np.nan)).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc148_42d_3rd_derivative_v148_signal'] = f69oc_f69_operating_cash_flow_stability_calc148_42d_3rd_derivative_v148_signal

def f69oc_f69_operating_cash_flow_stability_calc149_80d_3rd_derivative_v149_signal(currentratio, ncfo):
    res = ((ncfo.diff(80) / currentratio.replace(0, np.nan).diff(80)).rolling(80).mean()).diff(1).rolling(80).mean().diff(1).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc149_80d_3rd_derivative_v149_signal'] = f69oc_f69_operating_cash_flow_stability_calc149_80d_3rd_derivative_v149_signal

def f69oc_f69_operating_cash_flow_stability_calc150_10d_3rd_derivative_v150_signal(evebit, ncfo):
    res = ((evebit / ncfo.replace(0, np.nan)).rolling(10).mean()).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc150_10d_3rd_derivative_v150_signal'] = f69oc_f69_operating_cash_flow_stability_calc150_10d_3rd_derivative_v150_signal
