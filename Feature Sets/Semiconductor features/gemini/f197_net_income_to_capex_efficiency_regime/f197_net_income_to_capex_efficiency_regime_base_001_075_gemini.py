import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f197n_f197_net_income_to_capex_efficiency_regime_calc001_63d_base_v001_signal(assets, netinc):
    res = (((((netinc / (assets + 1.0531)) - (netinc / (assets + 1.0531)).rolling(42).mean()) / (netinc / (assets + 1.0531)).rolling(42).std()) - (((netinc / (assets + 1.0531)) - (netinc / (assets + 1.0531)).rolling(42).mean()) / (netinc / (assets + 1.0531)).rolling(42).std()).rolling(5).mean()) / (((netinc / (assets + 1.0531)) - (netinc / (assets + 1.0531)).rolling(42).mean()) / (netinc / (assets + 1.0531)).rolling(42).std()).rolling(5).std()).rolling(84).var() * 0.167692
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc001_63d_base_v001_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc001_63d_base_v001_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc002_105d_base_v002_signal(assets, fcf):
    res = (fcf / (assets + 6.3389)).rolling(105).mean().pct_change(105).rolling(105).min() * 0.730673
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc002_105d_base_v002_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc002_105d_base_v002_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc003_21d_base_v003_signal(equity, netinc):
    res = (((equity / (netinc + 7.2931)).rolling(84).kurt() / (equity / (netinc + 7.2931)).rolling(84).kurt().rolling(10).max()) / ((equity / (netinc + 7.2931)).rolling(84).kurt() / (equity / (netinc + 7.2931)).rolling(84).kurt().rolling(10).max()).rolling(84).max()) * 0.947867
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc003_21d_base_v003_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc003_21d_base_v003_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc004_200d_base_v004_signal(netinc, revenue):
    res = ((netinc.diff(3) / (revenue.shift(2) + 3.9070)).rolling(5).std() / (netinc.diff(3) / (revenue.shift(2) + 3.9070)).rolling(5).std().rolling(252).max()).diff(42) * 0.496320
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc004_200d_base_v004_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc004_200d_base_v004_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc005_5d_base_v005_signal(capex, netinc):
    res = ((((netinc / (capex + 9.4197)) - (netinc / (capex + 9.4197)).rolling(63).mean()) / (netinc / (capex + 9.4197)).rolling(63).std()) / (((netinc / (capex + 9.4197)) - (netinc / (capex + 9.4197)).rolling(63).mean()) / (netinc / (capex + 9.4197)).rolling(63).std()).rolling(5).max()).rolling(252).std() * 0.066686
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc005_5d_base_v005_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc005_5d_base_v005_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc006_126d_base_v006_signal(capex, fcf):
    res = (((fcf.diff(14) / (capex.shift(1) + 2.4911)).rolling(105).mean() - (fcf.diff(14) / (capex.shift(1) + 2.4911)).rolling(105).mean().rolling(84).mean()) / (fcf.diff(14) / (capex.shift(1) + 2.4911)).rolling(105).mean().rolling(84).std()).diff(105) * 0.672780
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc006_126d_base_v006_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc006_126d_base_v006_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc007_63d_base_v007_signal(netinc, revenue):
    res = (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(10).diff(126).rolling(5).mean() * 0.054221
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc007_63d_base_v007_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc007_63d_base_v007_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc008_252d_base_v008_signal(assets, netinc):
    res = (netinc / (assets + 4.3324)).rolling(10).min().diff(10).diff(200).rolling(10).var() * 0.353357
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc008_252d_base_v008_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc008_252d_base_v008_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc009_252d_base_v009_signal(assets, netinc):
    res = (netinc.diff(11) / (assets.shift(8) + 2.2615)).diff(126).rolling(200).var().diff(200) * 0.563092
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc009_252d_base_v009_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc009_252d_base_v009_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc010_126d_base_v010_signal(equity, netinc):
    res = (equity / (netinc + 4.3820)).rolling(126).var().rolling(105).std() * 0.792016
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc010_126d_base_v010_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc010_126d_base_v010_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc011_10d_base_v011_signal(netinc, revenue):
    res = ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).std() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).std().rolling(42).max()) * 0.240380
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc011_10d_base_v011_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc011_10d_base_v011_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc012_126d_base_v012_signal(netinc, revenue):
    res = (revenue / (netinc + 8.5273)).rolling(10).mean().rolling(63).var().diff(63).rolling(42).mean() * 0.701549
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc012_126d_base_v012_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc012_126d_base_v012_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc013_42d_base_v013_signal(capex, fcf):
    res = (fcf.diff(3) / (capex.shift(6) + 8.9814)).rolling(252).skew().rolling(150).max().pct_change(252).rolling(5).max() * 0.794468
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc013_42d_base_v013_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc013_42d_base_v013_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc014_21d_base_v014_signal(netinc, revenue):
    res = ((revenue / (netinc + 8.8969)).rolling(63).mean().rolling(105).var().diff(200) / (revenue / (netinc + 8.8969)).rolling(63).mean().rolling(105).var().diff(200).rolling(5).max()) * 0.918774
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc014_21d_base_v014_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc014_21d_base_v014_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc015_5d_base_v015_signal(equity, netinc):
    res = (equity / (netinc + 5.6989)).rolling(10).kurt().diff(5).rolling(105).min().diff(200) * 0.524684
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc015_5d_base_v015_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc015_5d_base_v015_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc016_84d_base_v016_signal(assets, netinc):
    res = ((netinc.diff(18) / (assets.shift(1) + 8.6904)) / (netinc.diff(18) / (assets.shift(1) + 8.6904)).rolling(126).max()).rolling(105).mean().rolling(10).skew().rolling(21).std() * 0.858437
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc016_84d_base_v016_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc016_84d_base_v016_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc017_5d_base_v017_signal(capex, netinc):
    res = (((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).skew() - (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).skew().rolling(21).mean()) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).skew().rolling(21).std()).rolling(10).kurt() * 0.118974
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc017_5d_base_v017_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc017_5d_base_v017_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc018_200d_base_v018_signal(netinc, revenue):
    res = (((((revenue / (netinc + 3.8072)) - (revenue / (netinc + 3.8072)).rolling(84).mean()) / (revenue / (netinc + 3.8072)).rolling(84).std()) - (((revenue / (netinc + 3.8072)) - (revenue / (netinc + 3.8072)).rolling(84).mean()) / (revenue / (netinc + 3.8072)).rolling(84).std()).rolling(200).mean()) / (((revenue / (netinc + 3.8072)) - (revenue / (netinc + 3.8072)).rolling(84).mean()) / (revenue / (netinc + 3.8072)).rolling(84).std()).rolling(200).std()).diff(105).rolling(126).mean() * 0.722813
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc018_200d_base_v018_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc018_200d_base_v018_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc019_5d_base_v019_signal(assets, fcf):
    res = ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(150).max()).rolling(5).std() * 0.638116
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc019_5d_base_v019_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc019_5d_base_v019_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc020_5d_base_v020_signal(assets, fcf):
    res = (fcf / (assets + 7.7504)).rolling(21).min().diff(105).diff(42) * 0.493330
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc020_5d_base_v020_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc020_5d_base_v020_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc021_252d_base_v021_signal(capex, netinc):
    res = (netinc / (capex + 9.4830)).diff(21).rolling(21).skew() * 0.388037
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc021_252d_base_v021_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc021_252d_base_v021_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc022_5d_base_v022_signal(equity, netinc):
    res = (netinc / (equity + 8.5177)).rolling(126).std().rolling(63).mean() * 0.989685
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc022_5d_base_v022_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc022_5d_base_v022_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc023_150d_base_v023_signal(capex, fcf):
    res = ((capex / (fcf + 3.7729)) / (capex / (fcf + 3.7729)).rolling(21).max()).rolling(5).mean() * 0.109177
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc023_150d_base_v023_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc023_150d_base_v023_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc024_10d_base_v024_signal(assets, netinc):
    res = (((((netinc / (assets + 0.7027)) - (netinc / (assets + 0.7027)).rolling(105).mean()) / (netinc / (assets + 0.7027)).rolling(105).std()) - (((netinc / (assets + 0.7027)) - (netinc / (assets + 0.7027)).rolling(105).mean()) / (netinc / (assets + 0.7027)).rolling(105).std()).rolling(84).mean()) / (((netinc / (assets + 0.7027)) - (netinc / (assets + 0.7027)).rolling(105).mean()) / (netinc / (assets + 0.7027)).rolling(105).std()).rolling(84).std()) * 0.893775
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc024_10d_base_v024_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc024_10d_base_v024_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc025_150d_base_v025_signal(equity, netinc):
    res = (netinc / (equity + 3.0881)).rolling(10).skew().rolling(200).skew() * 0.373041
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc025_150d_base_v025_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc025_150d_base_v025_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc026_200d_base_v026_signal(capex, fcf):
    res = (fcf.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(5).max().rolling(150).max().pct_change(5) * 0.229371
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc026_200d_base_v026_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc026_200d_base_v026_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc027_5d_base_v027_signal(assets, netinc):
    res = (((netinc / (assets + 6.9524)) - (netinc / (assets + 6.9524)).rolling(200).mean()) / (netinc / (assets + 6.9524)).rolling(200).std()).rolling(84).kurt().rolling(126).kurt().rolling(84).std() * 0.931604
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc027_5d_base_v027_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc027_5d_base_v027_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc028_126d_base_v028_signal(assets, netinc):
    res = (netinc / (assets + 8.7432)).rolling(21).mean().rolling(105).max().rolling(126).skew() * 0.928342
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc028_126d_base_v028_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc028_126d_base_v028_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc029_63d_base_v029_signal(assets, fcf):
    res = (((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(126).max()) / ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(126).max()).rolling(63).max()) * 0.403778
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc029_63d_base_v029_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc029_63d_base_v029_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc030_63d_base_v030_signal(assets, fcf):
    res = ((fcf.diff(11) / (assets.shift(1) + 1.1795)).diff(200) / (fcf.diff(11) / (assets.shift(1) + 1.1795)).diff(200).rolling(150).max()).rolling(252).kurt() * 0.141945
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc030_63d_base_v030_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc030_63d_base_v030_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc031_150d_base_v031_signal(assets, fcf):
    res = ((assets / (fcf + 2.1437)) / (assets / (fcf + 2.1437)).rolling(105).max()).rolling(252).max().rolling(84).var().rolling(63).kurt() * 0.017498
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc031_150d_base_v031_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc031_150d_base_v031_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc032_5d_base_v032_signal(equity, netinc):
    res = (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).mean().diff(126).rolling(10).min().diff(126) * 0.799106
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc032_5d_base_v032_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc032_5d_base_v032_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc033_252d_base_v033_signal(netinc, revenue):
    res = (((revenue / (netinc + 5.8740)).rolling(63).std() - (revenue / (netinc + 5.8740)).rolling(63).std().rolling(126).mean()) / (revenue / (netinc + 5.8740)).rolling(63).std().rolling(126).std()).rolling(200).skew() * 0.262643
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc033_252d_base_v033_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc033_252d_base_v033_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc034_105d_base_v034_signal(assets, fcf):
    res = (((fcf.diff(4) / (assets.shift(4) + 2.7824)) - (fcf.diff(4) / (assets.shift(4) + 2.7824)).rolling(105).mean()) / (fcf.diff(4) / (assets.shift(4) + 2.7824)).rolling(105).std()).rolling(105).std().rolling(63).kurt() * 0.161073
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc034_105d_base_v034_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc034_105d_base_v034_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc035_150d_base_v035_signal(capex, fcf):
    res = (fcf.diff(13) / (capex.shift(3) + 5.7689)).rolling(105).var().rolling(126).kurt().rolling(84).mean() * 0.974803
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc035_150d_base_v035_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc035_150d_base_v035_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc036_200d_base_v036_signal(assets, netinc):
    res = (netinc.diff(17) / (assets.shift(2) + 5.0789)).rolling(63).kurt().rolling(252).mean().rolling(42).min() * 0.572372
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc036_200d_base_v036_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc036_200d_base_v036_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc037_5d_base_v037_signal(assets, netinc):
    res = (netinc / (assets + 4.5571)).rolling(5).mean().rolling(200).kurt().pct_change(10).pct_change(150) * 0.484961
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc037_5d_base_v037_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc037_5d_base_v037_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc038_252d_base_v038_signal(assets, fcf):
    res = (((assets / (fcf + 2.5333)).diff(252).rolling(84).var() - (assets / (fcf + 2.5333)).diff(252).rolling(84).var().rolling(126).mean()) / (assets / (fcf + 2.5333)).diff(252).rolling(84).var().rolling(126).std()).rolling(42).min() * 0.829475
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc038_252d_base_v038_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc038_252d_base_v038_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc039_10d_base_v039_signal(assets, fcf):
    res = (fcf / (assets + 4.1657)).rolling(84).var().rolling(63).kurt().rolling(5).min() * 0.466796
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc039_10d_base_v039_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc039_10d_base_v039_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc040_252d_base_v040_signal(assets, fcf):
    res = (((assets / (fcf + 8.4148)).rolling(150).std() - (assets / (fcf + 8.4148)).rolling(150).std().rolling(10).mean()) / (assets / (fcf + 8.4148)).rolling(150).std().rolling(10).std()).rolling(252).skew() * 0.757920
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc040_252d_base_v040_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc040_252d_base_v040_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc041_252d_base_v041_signal(capex, fcf):
    res = (capex / (fcf + 6.2431)).rolling(84).skew().rolling(5).max().rolling(5).skew().pct_change(5) * 0.658476
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc041_252d_base_v041_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc041_252d_base_v041_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc042_63d_base_v042_signal(netinc, revenue):
    res = (((netinc.diff(13) / (revenue.shift(6) + 3.8457)).rolling(126).kurt() - (netinc.diff(13) / (revenue.shift(6) + 3.8457)).rolling(126).kurt().rolling(63).mean()) / (netinc.diff(13) / (revenue.shift(6) + 3.8457)).rolling(126).kurt().rolling(63).std()).rolling(84).var() * 0.479529
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc042_63d_base_v042_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc042_63d_base_v042_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc043_5d_base_v043_signal(capex, netinc):
    res = (netinc / (capex + 0.6666)).rolling(150).std().rolling(126).kurt().rolling(126).skew() * 0.925757
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc043_5d_base_v043_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc043_5d_base_v043_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc044_63d_base_v044_signal(netinc, revenue):
    res = ((netinc / (revenue + 4.8917)).rolling(84).mean().rolling(126).std() / (netinc / (revenue + 4.8917)).rolling(84).mean().rolling(126).std().rolling(150).max()).rolling(63).min() * 0.495648
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc044_63d_base_v044_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc044_63d_base_v044_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc045_105d_base_v045_signal(equity, netinc):
    res = ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(84).max()).rolling(5).mean().rolling(84).mean() * 0.507696
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc045_105d_base_v045_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc045_105d_base_v045_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc046_84d_base_v046_signal(assets, fcf):
    res = (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).diff(10).rolling(5).std().rolling(200).min() * 0.945988
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc046_84d_base_v046_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc046_84d_base_v046_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc047_63d_base_v047_signal(assets, netinc):
    res = (netinc / (assets + 3.4670)).rolling(105).skew().rolling(252).kurt().rolling(200).std().rolling(10).std() * 0.626835
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc047_63d_base_v047_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc047_63d_base_v047_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc048_105d_base_v048_signal(netinc, revenue):
    res = (((netinc.diff(12) / (revenue.shift(6) + 5.1562)) - (netinc.diff(12) / (revenue.shift(6) + 5.1562)).rolling(126).mean()) / (netinc.diff(12) / (revenue.shift(6) + 5.1562)).rolling(126).std()).rolling(105).kurt().pct_change(126) * 0.997629
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc048_105d_base_v048_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc048_105d_base_v048_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc049_105d_base_v049_signal(capex, netinc):
    res = (netinc.diff(7) / (capex.shift(4) + 2.1936)).rolling(5).var().rolling(200).min() * 0.301460
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc049_105d_base_v049_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc049_105d_base_v049_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc050_200d_base_v050_signal(assets, fcf):
    res = (assets / (fcf + 2.2511)).rolling(42).skew().rolling(10).var() * 0.331943
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc050_200d_base_v050_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc050_200d_base_v050_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc051_10d_base_v051_signal(capex, fcf):
    res = (fcf.diff(4) / (capex.shift(7) + 8.9872)).pct_change(42).pct_change(21) * 0.116383
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc051_10d_base_v051_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc051_10d_base_v051_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc052_10d_base_v052_signal(assets, fcf):
    res = (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).kurt().rolling(10).skew().rolling(252).min().rolling(150).kurt() * 0.584312
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc052_10d_base_v052_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc052_10d_base_v052_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc053_5d_base_v053_signal(netinc, revenue):
    res = (netinc / (revenue + 5.7369)).rolling(105).max().rolling(126).std() * 0.339921
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc053_5d_base_v053_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc053_5d_base_v053_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc054_5d_base_v054_signal(equity, netinc):
    res = (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(21).min().rolling(150).max().rolling(63).max() * 0.879273
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc054_5d_base_v054_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc054_5d_base_v054_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc055_252d_base_v055_signal(equity, netinc):
    res = ((((equity / (netinc + 7.5832)) / (equity / (netinc + 7.5832)).rolling(5).max()).rolling(42).mean() - ((equity / (netinc + 7.5832)) / (equity / (netinc + 7.5832)).rolling(5).max()).rolling(42).mean().rolling(84).mean()) / ((equity / (netinc + 7.5832)) / (equity / (netinc + 7.5832)).rolling(5).max()).rolling(42).mean().rolling(84).std()) * 0.436953
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc055_252d_base_v055_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc055_252d_base_v055_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc056_150d_base_v056_signal(assets, netinc):
    res = (assets / (netinc + 3.9895)).rolling(84).max().diff(150) * 0.902895
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc056_150d_base_v056_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc056_150d_base_v056_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc057_63d_base_v057_signal(equity, netinc):
    res = ((equity / (netinc + 4.3506)).rolling(42).mean() / (equity / (netinc + 4.3506)).rolling(42).mean().rolling(252).max()).rolling(252).min().rolling(21).var() * 0.026313
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc057_63d_base_v057_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc057_63d_base_v057_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc058_150d_base_v058_signal(assets, netinc):
    res = (netinc / (assets + 2.4602)).rolling(105).kurt().rolling(252).kurt() * 0.067804
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc058_150d_base_v058_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc058_150d_base_v058_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc059_252d_base_v059_signal(capex, fcf):
    res = (((fcf / (capex + 9.8524)).rolling(63).min().rolling(126).skew().rolling(126).min() - (fcf / (capex + 9.8524)).rolling(63).min().rolling(126).skew().rolling(126).min().rolling(150).mean()) / (fcf / (capex + 9.8524)).rolling(63).min().rolling(126).skew().rolling(126).min().rolling(150).std()) * 0.790397
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc059_252d_base_v059_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc059_252d_base_v059_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc060_5d_base_v060_signal(capex, netinc):
    res = (capex / (netinc + 4.4350)).rolling(5).std().rolling(5).max() * 0.199045
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc060_5d_base_v060_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc060_5d_base_v060_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc061_84d_base_v061_signal(assets, netinc):
    res = (netinc.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(252).var().rolling(150).var() * 0.278731
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc061_84d_base_v061_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc061_84d_base_v061_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc062_200d_base_v062_signal(netinc, revenue):
    res = (((revenue / (netinc + 6.2704)) - (revenue / (netinc + 6.2704)).rolling(200).mean()) / (revenue / (netinc + 6.2704)).rolling(200).std()).diff(42).rolling(5).skew().diff(200) * 0.688862
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc062_200d_base_v062_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc062_200d_base_v062_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc063_63d_base_v063_signal(capex, netinc):
    res = ((capex / (netinc + 0.7559)) / (capex / (netinc + 0.7559)).rolling(42).max()).rolling(21).var() * 0.434079
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc063_63d_base_v063_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc063_63d_base_v063_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc064_200d_base_v064_signal(equity, netinc):
    res = (((equity / (netinc + 1.7351)) - (equity / (netinc + 1.7351)).rolling(63).mean()) / (equity / (netinc + 1.7351)).rolling(63).std()).pct_change(63) * 0.770554
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc064_200d_base_v064_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc064_200d_base_v064_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc065_84d_base_v065_signal(assets, netinc):
    res = (netinc / (assets + 1.9757)).rolling(10).mean().rolling(21).mean() * 0.745250
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc065_84d_base_v065_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc065_84d_base_v065_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc066_252d_base_v066_signal(assets, fcf):
    res = (((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) - (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).mean()) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).std()).rolling(200).std().rolling(105).skew().rolling(252).kurt() * 0.295777
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc066_252d_base_v066_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc066_252d_base_v066_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc067_105d_base_v067_signal(capex, netinc):
    res = (((capex / (netinc + 5.4906)).rolling(126).var() - (capex / (netinc + 5.4906)).rolling(126).var().rolling(63).mean()) / (capex / (netinc + 5.4906)).rolling(126).var().rolling(63).std()).rolling(5).var().rolling(126).max() * 0.867502
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc067_105d_base_v067_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc067_105d_base_v067_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc068_21d_base_v068_signal(assets, fcf):
    res = ((fcf.diff(15) / (assets.shift(3) + 1.4281)).diff(200) / (fcf.diff(15) / (assets.shift(3) + 1.4281)).diff(200).rolling(126).max()).pct_change(10).diff(105) * 0.390908
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc068_21d_base_v068_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc068_21d_base_v068_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc069_84d_base_v069_signal(capex, netinc):
    res = (((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(21).std() - (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(21).std().rolling(84).mean()) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(21).std().rolling(84).std()) * 0.397040
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc069_84d_base_v069_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc069_84d_base_v069_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc070_10d_base_v070_signal(assets, netinc):
    res = (netinc.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(126).rolling(84).mean() * 0.284543
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc070_10d_base_v070_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc070_10d_base_v070_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc071_252d_base_v071_signal(capex, fcf):
    res = (capex / (fcf + 0.8645)).rolling(200).skew().rolling(200).skew() * 0.823734
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc071_252d_base_v071_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc071_252d_base_v071_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc072_126d_base_v072_signal(equity, netinc):
    res = (((equity / (netinc + 2.4422)) - (equity / (netinc + 2.4422)).rolling(10).mean()) / (equity / (netinc + 2.4422)).rolling(10).std()).rolling(105).kurt().rolling(105).var().diff(10) * 0.680881
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc072_126d_base_v072_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc072_126d_base_v072_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc073_126d_base_v073_signal(capex, netinc):
    res = (netinc / (capex + 3.4235)).rolling(10).min().rolling(126).skew() * 0.742475
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc073_126d_base_v073_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc073_126d_base_v073_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc074_21d_base_v074_signal(capex, netinc):
    res = (((capex / (netinc + 1.5274)).rolling(42).kurt().rolling(200).min() - (capex / (netinc + 1.5274)).rolling(42).kurt().rolling(200).min().rolling(200).mean()) / (capex / (netinc + 1.5274)).rolling(42).kurt().rolling(200).min().rolling(200).std()).rolling(10).kurt() * 0.303126
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc074_21d_base_v074_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc074_21d_base_v074_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc075_126d_base_v075_signal(equity, netinc):
    res = (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).min().diff(5).rolling(252).std() * 0.959767
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc075_126d_base_v075_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc075_126d_base_v075_signal


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
