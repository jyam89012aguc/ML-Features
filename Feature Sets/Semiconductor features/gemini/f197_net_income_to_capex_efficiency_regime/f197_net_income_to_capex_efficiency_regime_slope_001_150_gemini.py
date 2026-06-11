import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f197n_f197_net_income_to_capex_efficiency_regime_calc001_42d_slope_v001_signal(assets, netinc):
    res = ((((((netinc / (assets + 1.0531)) - (netinc / (assets + 1.0531)).rolling(42).mean()) / (netinc / (assets + 1.0531)).rolling(42).std()) - (((netinc / (assets + 1.0531)) - (netinc / (assets + 1.0531)).rolling(42).mean()) / (netinc / (assets + 1.0531)).rolling(42).std()).rolling(5).mean()) / (((netinc / (assets + 1.0531)) - (netinc / (assets + 1.0531)).rolling(42).mean()) / (netinc / (assets + 1.0531)).rolling(42).std()).rolling(5).std()).rolling(84).var() * 0.167692).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc001_42d_slope_v001_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc001_42d_slope_v001_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc002_105d_slope_v002_signal(assets, fcf):
    res = ((fcf / (assets + 6.3389)).rolling(105).mean().pct_change(105).rolling(105).min() * 0.730673).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc002_105d_slope_v002_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc002_105d_slope_v002_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc003_21d_slope_v003_signal(equity, netinc):
    res = ((((equity / (netinc + 7.2931)).rolling(84).kurt() / (equity / (netinc + 7.2931)).rolling(84).kurt().rolling(10).max()) / ((equity / (netinc + 7.2931)).rolling(84).kurt() / (equity / (netinc + 7.2931)).rolling(84).kurt().rolling(10).max()).rolling(84).max()) * 0.947867).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc003_21d_slope_v003_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc003_21d_slope_v003_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc004_63d_slope_v004_signal(netinc, revenue):
    res = (((netinc.diff(3) / (revenue.shift(2) + 3.9070)).rolling(5).std() / (netinc.diff(3) / (revenue.shift(2) + 3.9070)).rolling(5).std().rolling(252).max()).diff(42) * 0.496320).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc004_63d_slope_v004_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc004_63d_slope_v004_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc005_150d_slope_v005_signal(capex, netinc):
    res = (((((netinc / (capex + 9.4197)) - (netinc / (capex + 9.4197)).rolling(63).mean()) / (netinc / (capex + 9.4197)).rolling(63).std()) / (((netinc / (capex + 9.4197)) - (netinc / (capex + 9.4197)).rolling(63).mean()) / (netinc / (capex + 9.4197)).rolling(63).std()).rolling(5).max()).rolling(252).std() * 0.066686).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc005_150d_slope_v005_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc005_150d_slope_v005_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc006_150d_slope_v006_signal(capex, fcf):
    res = ((((fcf.diff(14) / (capex.shift(1) + 2.4911)).rolling(105).mean() - (fcf.diff(14) / (capex.shift(1) + 2.4911)).rolling(105).mean().rolling(84).mean()) / (fcf.diff(14) / (capex.shift(1) + 2.4911)).rolling(105).mean().rolling(84).std()).diff(105) * 0.672780).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc006_150d_slope_v006_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc006_150d_slope_v006_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc007_5d_slope_v007_signal(netinc, revenue):
    res = ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(10).diff(126).rolling(5).mean() * 0.054221).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc007_5d_slope_v007_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc007_5d_slope_v007_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc008_42d_slope_v008_signal(assets, netinc):
    res = ((netinc / (assets + 4.3324)).rolling(10).min().diff(10).diff(200).rolling(10).var() * 0.353357).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc008_42d_slope_v008_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc008_42d_slope_v008_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc009_252d_slope_v009_signal(assets, netinc):
    res = ((netinc.diff(11) / (assets.shift(8) + 2.2615)).diff(126).rolling(200).var().diff(200) * 0.563092).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc009_252d_slope_v009_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc009_252d_slope_v009_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc010_42d_slope_v010_signal(equity, netinc):
    res = ((equity / (netinc + 4.3820)).rolling(126).var().rolling(105).std() * 0.792016).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc010_42d_slope_v010_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc010_42d_slope_v010_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc011_5d_slope_v011_signal(netinc, revenue):
    res = (((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).std() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).std().rolling(42).max()) * 0.240380).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc011_5d_slope_v011_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc011_5d_slope_v011_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc012_10d_slope_v012_signal(netinc, revenue):
    res = ((revenue / (netinc + 8.5273)).rolling(10).mean().rolling(63).var().diff(63).rolling(42).mean() * 0.701549).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc012_10d_slope_v012_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc012_10d_slope_v012_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc013_150d_slope_v013_signal(capex, fcf):
    res = ((fcf.diff(3) / (capex.shift(6) + 8.9814)).rolling(252).skew().rolling(150).max().pct_change(252).rolling(5).max() * 0.794468).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc013_150d_slope_v013_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc013_150d_slope_v013_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc014_105d_slope_v014_signal(netinc, revenue):
    res = (((revenue / (netinc + 8.8969)).rolling(63).mean().rolling(105).var().diff(200) / (revenue / (netinc + 8.8969)).rolling(63).mean().rolling(105).var().diff(200).rolling(5).max()) * 0.918774).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc014_105d_slope_v014_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc014_105d_slope_v014_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc015_126d_slope_v015_signal(equity, netinc):
    res = ((equity / (netinc + 5.6989)).rolling(10).kurt().diff(5).rolling(105).min().diff(200) * 0.524684).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc015_126d_slope_v015_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc015_126d_slope_v015_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc016_5d_slope_v016_signal(assets, netinc):
    res = (((netinc.diff(18) / (assets.shift(1) + 8.6904)) / (netinc.diff(18) / (assets.shift(1) + 8.6904)).rolling(126).max()).rolling(105).mean().rolling(10).skew().rolling(21).std() * 0.858437).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc016_5d_slope_v016_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc016_5d_slope_v016_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc017_200d_slope_v017_signal(capex, netinc):
    res = ((((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).skew() - (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).skew().rolling(21).mean()) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).skew().rolling(21).std()).rolling(10).kurt() * 0.118974).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc017_200d_slope_v017_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc017_200d_slope_v017_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc018_10d_slope_v018_signal(netinc, revenue):
    res = ((((((revenue / (netinc + 3.8072)) - (revenue / (netinc + 3.8072)).rolling(84).mean()) / (revenue / (netinc + 3.8072)).rolling(84).std()) - (((revenue / (netinc + 3.8072)) - (revenue / (netinc + 3.8072)).rolling(84).mean()) / (revenue / (netinc + 3.8072)).rolling(84).std()).rolling(200).mean()) / (((revenue / (netinc + 3.8072)) - (revenue / (netinc + 3.8072)).rolling(84).mean()) / (revenue / (netinc + 3.8072)).rolling(84).std()).rolling(200).std()).diff(105).rolling(126).mean() * 0.722813).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc018_10d_slope_v018_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc018_10d_slope_v018_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc019_252d_slope_v019_signal(assets, fcf):
    res = (((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(150).max()).rolling(5).std() * 0.638116).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc019_252d_slope_v019_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc019_252d_slope_v019_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc020_63d_slope_v020_signal(assets, fcf):
    res = ((fcf / (assets + 7.7504)).rolling(21).min().diff(105).diff(42) * 0.493330).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc020_63d_slope_v020_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc020_63d_slope_v020_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc021_252d_slope_v021_signal(capex, netinc):
    res = ((netinc / (capex + 9.4830)).diff(21).rolling(21).skew() * 0.388037).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc021_252d_slope_v021_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc021_252d_slope_v021_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc022_84d_slope_v022_signal(equity, netinc):
    res = ((netinc / (equity + 8.5177)).rolling(126).std().rolling(63).mean() * 0.989685).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc022_84d_slope_v022_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc022_84d_slope_v022_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc023_10d_slope_v023_signal(capex, fcf):
    res = (((capex / (fcf + 3.7729)) / (capex / (fcf + 3.7729)).rolling(21).max()).rolling(5).mean() * 0.109177).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc023_10d_slope_v023_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc023_10d_slope_v023_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc024_10d_slope_v024_signal(assets, netinc):
    res = ((((((netinc / (assets + 0.7027)) - (netinc / (assets + 0.7027)).rolling(105).mean()) / (netinc / (assets + 0.7027)).rolling(105).std()) - (((netinc / (assets + 0.7027)) - (netinc / (assets + 0.7027)).rolling(105).mean()) / (netinc / (assets + 0.7027)).rolling(105).std()).rolling(84).mean()) / (((netinc / (assets + 0.7027)) - (netinc / (assets + 0.7027)).rolling(105).mean()) / (netinc / (assets + 0.7027)).rolling(105).std()).rolling(84).std()) * 0.893775).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc024_10d_slope_v024_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc024_10d_slope_v024_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc025_5d_slope_v025_signal(equity, netinc):
    res = ((netinc / (equity + 3.0881)).rolling(10).skew().rolling(200).skew() * 0.373041).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc025_5d_slope_v025_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc025_5d_slope_v025_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc026_42d_slope_v026_signal(capex, fcf):
    res = ((fcf.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(5).max().rolling(150).max().pct_change(5) * 0.229371).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc026_42d_slope_v026_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc026_42d_slope_v026_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc027_42d_slope_v027_signal(assets, netinc):
    res = ((((netinc / (assets + 6.9524)) - (netinc / (assets + 6.9524)).rolling(200).mean()) / (netinc / (assets + 6.9524)).rolling(200).std()).rolling(84).kurt().rolling(126).kurt().rolling(84).std() * 0.931604).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc027_42d_slope_v027_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc027_42d_slope_v027_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc028_126d_slope_v028_signal(assets, netinc):
    res = ((netinc / (assets + 8.7432)).rolling(21).mean().rolling(105).max().rolling(126).skew() * 0.928342).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc028_126d_slope_v028_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc028_126d_slope_v028_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc029_126d_slope_v029_signal(assets, fcf):
    res = ((((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(126).max()) / ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(126).max()).rolling(63).max()) * 0.403778).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc029_126d_slope_v029_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc029_126d_slope_v029_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc030_105d_slope_v030_signal(assets, fcf):
    res = (((fcf.diff(11) / (assets.shift(1) + 1.1795)).diff(200) / (fcf.diff(11) / (assets.shift(1) + 1.1795)).diff(200).rolling(150).max()).rolling(252).kurt() * 0.141945).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc030_105d_slope_v030_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc030_105d_slope_v030_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc031_42d_slope_v031_signal(assets, fcf):
    res = (((assets / (fcf + 2.1437)) / (assets / (fcf + 2.1437)).rolling(105).max()).rolling(252).max().rolling(84).var().rolling(63).kurt() * 0.017498).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc031_42d_slope_v031_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc031_42d_slope_v031_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc032_126d_slope_v032_signal(equity, netinc):
    res = ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).mean().diff(126).rolling(10).min().diff(126) * 0.799106).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc032_126d_slope_v032_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc032_126d_slope_v032_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc033_200d_slope_v033_signal(netinc, revenue):
    res = ((((revenue / (netinc + 5.8740)).rolling(63).std() - (revenue / (netinc + 5.8740)).rolling(63).std().rolling(126).mean()) / (revenue / (netinc + 5.8740)).rolling(63).std().rolling(126).std()).rolling(200).skew() * 0.262643).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc033_200d_slope_v033_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc033_200d_slope_v033_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc034_150d_slope_v034_signal(assets, fcf):
    res = ((((fcf.diff(4) / (assets.shift(4) + 2.7824)) - (fcf.diff(4) / (assets.shift(4) + 2.7824)).rolling(105).mean()) / (fcf.diff(4) / (assets.shift(4) + 2.7824)).rolling(105).std()).rolling(105).std().rolling(63).kurt() * 0.161073).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc034_150d_slope_v034_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc034_150d_slope_v034_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc035_42d_slope_v035_signal(capex, fcf):
    res = ((fcf.diff(13) / (capex.shift(3) + 5.7689)).rolling(105).var().rolling(126).kurt().rolling(84).mean() * 0.974803).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc035_42d_slope_v035_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc035_42d_slope_v035_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc036_252d_slope_v036_signal(assets, netinc):
    res = ((netinc.diff(17) / (assets.shift(2) + 5.0789)).rolling(63).kurt().rolling(252).mean().rolling(42).min() * 0.572372).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc036_252d_slope_v036_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc036_252d_slope_v036_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc037_10d_slope_v037_signal(assets, netinc):
    res = ((netinc / (assets + 4.5571)).rolling(5).mean().rolling(200).kurt().pct_change(10).pct_change(150) * 0.484961).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc037_10d_slope_v037_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc037_10d_slope_v037_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc038_126d_slope_v038_signal(assets, fcf):
    res = ((((assets / (fcf + 2.5333)).diff(252).rolling(84).var() - (assets / (fcf + 2.5333)).diff(252).rolling(84).var().rolling(126).mean()) / (assets / (fcf + 2.5333)).diff(252).rolling(84).var().rolling(126).std()).rolling(42).min() * 0.829475).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc038_126d_slope_v038_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc038_126d_slope_v038_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc039_63d_slope_v039_signal(assets, fcf):
    res = ((fcf / (assets + 4.1657)).rolling(84).var().rolling(63).kurt().rolling(5).min() * 0.466796).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc039_63d_slope_v039_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc039_63d_slope_v039_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc040_105d_slope_v040_signal(assets, fcf):
    res = ((((assets / (fcf + 8.4148)).rolling(150).std() - (assets / (fcf + 8.4148)).rolling(150).std().rolling(10).mean()) / (assets / (fcf + 8.4148)).rolling(150).std().rolling(10).std()).rolling(252).skew() * 0.757920).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc040_105d_slope_v040_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc040_105d_slope_v040_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc041_200d_slope_v041_signal(capex, fcf):
    res = ((capex / (fcf + 6.2431)).rolling(84).skew().rolling(5).max().rolling(5).skew().pct_change(5) * 0.658476).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc041_200d_slope_v041_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc041_200d_slope_v041_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc042_126d_slope_v042_signal(netinc, revenue):
    res = ((((netinc.diff(13) / (revenue.shift(6) + 3.8457)).rolling(126).kurt() - (netinc.diff(13) / (revenue.shift(6) + 3.8457)).rolling(126).kurt().rolling(63).mean()) / (netinc.diff(13) / (revenue.shift(6) + 3.8457)).rolling(126).kurt().rolling(63).std()).rolling(84).var() * 0.479529).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc042_126d_slope_v042_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc042_126d_slope_v042_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc043_252d_slope_v043_signal(capex, netinc):
    res = ((netinc / (capex + 0.6666)).rolling(150).std().rolling(126).kurt().rolling(126).skew() * 0.925757).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc043_252d_slope_v043_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc043_252d_slope_v043_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc044_252d_slope_v044_signal(netinc, revenue):
    res = (((netinc / (revenue + 4.8917)).rolling(84).mean().rolling(126).std() / (netinc / (revenue + 4.8917)).rolling(84).mean().rolling(126).std().rolling(150).max()).rolling(63).min() * 0.495648).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc044_252d_slope_v044_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc044_252d_slope_v044_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc045_21d_slope_v045_signal(equity, netinc):
    res = (((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(84).max()).rolling(5).mean().rolling(84).mean() * 0.507696).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc045_21d_slope_v045_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc045_21d_slope_v045_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc046_105d_slope_v046_signal(assets, fcf):
    res = ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)).diff(10).rolling(5).std().rolling(200).min() * 0.945988).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc046_105d_slope_v046_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc046_105d_slope_v046_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc047_252d_slope_v047_signal(assets, netinc):
    res = ((netinc / (assets + 3.4670)).rolling(105).skew().rolling(252).kurt().rolling(200).std().rolling(10).std() * 0.626835).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc047_252d_slope_v047_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc047_252d_slope_v047_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc048_84d_slope_v048_signal(netinc, revenue):
    res = ((((netinc.diff(12) / (revenue.shift(6) + 5.1562)) - (netinc.diff(12) / (revenue.shift(6) + 5.1562)).rolling(126).mean()) / (netinc.diff(12) / (revenue.shift(6) + 5.1562)).rolling(126).std()).rolling(105).kurt().pct_change(126) * 0.997629).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc048_84d_slope_v048_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc048_84d_slope_v048_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc049_42d_slope_v049_signal(capex, netinc):
    res = ((netinc.diff(7) / (capex.shift(4) + 2.1936)).rolling(5).var().rolling(200).min() * 0.301460).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc049_42d_slope_v049_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc049_42d_slope_v049_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc050_5d_slope_v050_signal(assets, fcf):
    res = ((assets / (fcf + 2.2511)).rolling(42).skew().rolling(10).var() * 0.331943).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc050_5d_slope_v050_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc050_5d_slope_v050_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc051_200d_slope_v051_signal(capex, fcf):
    res = ((fcf.diff(4) / (capex.shift(7) + 8.9872)).pct_change(42).pct_change(21) * 0.116383).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc051_200d_slope_v051_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc051_200d_slope_v051_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc052_252d_slope_v052_signal(assets, fcf):
    res = ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).kurt().rolling(10).skew().rolling(252).min().rolling(150).kurt() * 0.584312).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc052_252d_slope_v052_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc052_252d_slope_v052_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc053_21d_slope_v053_signal(netinc, revenue):
    res = ((netinc / (revenue + 5.7369)).rolling(105).max().rolling(126).std() * 0.339921).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc053_21d_slope_v053_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc053_21d_slope_v053_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc054_10d_slope_v054_signal(equity, netinc):
    res = ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(21).min().rolling(150).max().rolling(63).max() * 0.879273).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc054_10d_slope_v054_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc054_10d_slope_v054_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc055_63d_slope_v055_signal(equity, netinc):
    res = (((((equity / (netinc + 7.5832)) / (equity / (netinc + 7.5832)).rolling(5).max()).rolling(42).mean() - ((equity / (netinc + 7.5832)) / (equity / (netinc + 7.5832)).rolling(5).max()).rolling(42).mean().rolling(84).mean()) / ((equity / (netinc + 7.5832)) / (equity / (netinc + 7.5832)).rolling(5).max()).rolling(42).mean().rolling(84).std()) * 0.436953).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc055_63d_slope_v055_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc055_63d_slope_v055_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc056_105d_slope_v056_signal(assets, netinc):
    res = ((assets / (netinc + 3.9895)).rolling(84).max().diff(150) * 0.902895).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc056_105d_slope_v056_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc056_105d_slope_v056_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc057_63d_slope_v057_signal(equity, netinc):
    res = (((equity / (netinc + 4.3506)).rolling(42).mean() / (equity / (netinc + 4.3506)).rolling(42).mean().rolling(252).max()).rolling(252).min().rolling(21).var() * 0.026313).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc057_63d_slope_v057_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc057_63d_slope_v057_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc058_126d_slope_v058_signal(assets, netinc):
    res = ((netinc / (assets + 2.4602)).rolling(105).kurt().rolling(252).kurt() * 0.067804).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc058_126d_slope_v058_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc058_126d_slope_v058_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc059_63d_slope_v059_signal(capex, fcf):
    res = ((((fcf / (capex + 9.8524)).rolling(63).min().rolling(126).skew().rolling(126).min() - (fcf / (capex + 9.8524)).rolling(63).min().rolling(126).skew().rolling(126).min().rolling(150).mean()) / (fcf / (capex + 9.8524)).rolling(63).min().rolling(126).skew().rolling(126).min().rolling(150).std()) * 0.790397).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc059_63d_slope_v059_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc059_63d_slope_v059_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc060_126d_slope_v060_signal(capex, netinc):
    res = ((capex / (netinc + 4.4350)).rolling(5).std().rolling(5).max() * 0.199045).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc060_126d_slope_v060_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc060_126d_slope_v060_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc061_10d_slope_v061_signal(assets, netinc):
    res = ((netinc.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(252).var().rolling(150).var() * 0.278731).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc061_10d_slope_v061_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc061_10d_slope_v061_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc062_84d_slope_v062_signal(netinc, revenue):
    res = ((((revenue / (netinc + 6.2704)) - (revenue / (netinc + 6.2704)).rolling(200).mean()) / (revenue / (netinc + 6.2704)).rolling(200).std()).diff(42).rolling(5).skew().diff(200) * 0.688862).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc062_84d_slope_v062_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc062_84d_slope_v062_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc063_42d_slope_v063_signal(capex, netinc):
    res = (((capex / (netinc + 0.7559)) / (capex / (netinc + 0.7559)).rolling(42).max()).rolling(21).var() * 0.434079).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc063_42d_slope_v063_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc063_42d_slope_v063_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc064_84d_slope_v064_signal(equity, netinc):
    res = ((((equity / (netinc + 1.7351)) - (equity / (netinc + 1.7351)).rolling(63).mean()) / (equity / (netinc + 1.7351)).rolling(63).std()).pct_change(63) * 0.770554).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc064_84d_slope_v064_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc064_84d_slope_v064_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc065_150d_slope_v065_signal(assets, netinc):
    res = ((netinc / (assets + 1.9757)).rolling(10).mean().rolling(21).mean() * 0.745250).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc065_150d_slope_v065_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc065_150d_slope_v065_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc066_150d_slope_v066_signal(assets, fcf):
    res = ((((fcf.replace(0, np.nan) / assets.replace(0, np.nan)) - (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).mean()) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).std()).rolling(200).std().rolling(105).skew().rolling(252).kurt() * 0.295777).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc066_150d_slope_v066_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc066_150d_slope_v066_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc067_126d_slope_v067_signal(capex, netinc):
    res = ((((capex / (netinc + 5.4906)).rolling(126).var() - (capex / (netinc + 5.4906)).rolling(126).var().rolling(63).mean()) / (capex / (netinc + 5.4906)).rolling(126).var().rolling(63).std()).rolling(5).var().rolling(126).max() * 0.867502).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc067_126d_slope_v067_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc067_126d_slope_v067_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc068_5d_slope_v068_signal(assets, fcf):
    res = (((fcf.diff(15) / (assets.shift(3) + 1.4281)).diff(200) / (fcf.diff(15) / (assets.shift(3) + 1.4281)).diff(200).rolling(126).max()).pct_change(10).diff(105) * 0.390908).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc068_5d_slope_v068_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc068_5d_slope_v068_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc069_252d_slope_v069_signal(capex, netinc):
    res = ((((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(21).std() - (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(21).std().rolling(84).mean()) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(21).std().rolling(84).std()) * 0.397040).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc069_252d_slope_v069_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc069_252d_slope_v069_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc070_252d_slope_v070_signal(assets, netinc):
    res = ((netinc.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(126).rolling(84).mean() * 0.284543).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc070_252d_slope_v070_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc070_252d_slope_v070_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc071_105d_slope_v071_signal(capex, fcf):
    res = ((capex / (fcf + 0.8645)).rolling(200).skew().rolling(200).skew() * 0.823734).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc071_105d_slope_v071_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc071_105d_slope_v071_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc072_63d_slope_v072_signal(equity, netinc):
    res = ((((equity / (netinc + 2.4422)) - (equity / (netinc + 2.4422)).rolling(10).mean()) / (equity / (netinc + 2.4422)).rolling(10).std()).rolling(105).kurt().rolling(105).var().diff(10) * 0.680881).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc072_63d_slope_v072_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc072_63d_slope_v072_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc073_252d_slope_v073_signal(capex, netinc):
    res = ((netinc / (capex + 3.4235)).rolling(10).min().rolling(126).skew() * 0.742475).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc073_252d_slope_v073_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc073_252d_slope_v073_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc074_150d_slope_v074_signal(capex, netinc):
    res = ((((capex / (netinc + 1.5274)).rolling(42).kurt().rolling(200).min() - (capex / (netinc + 1.5274)).rolling(42).kurt().rolling(200).min().rolling(200).mean()) / (capex / (netinc + 1.5274)).rolling(42).kurt().rolling(200).min().rolling(200).std()).rolling(10).kurt() * 0.303126).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc074_150d_slope_v074_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc074_150d_slope_v074_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc075_252d_slope_v075_signal(equity, netinc):
    res = ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).min().diff(5).rolling(252).std() * 0.959767).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc075_252d_slope_v075_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc075_252d_slope_v075_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc076_63d_slope_v076_signal(assets, netinc):
    res = ((netinc / (assets + 4.7730)).rolling(105).min().rolling(42).mean() * 0.732126).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc076_63d_slope_v076_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc076_63d_slope_v076_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc077_252d_slope_v077_signal(capex, netinc):
    res = ((netinc / (capex + 0.7374)).rolling(10).std().rolling(10).mean().rolling(126).std().pct_change(5) * 0.146431).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc077_252d_slope_v077_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc077_252d_slope_v077_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc078_150d_slope_v078_signal(netinc, revenue):
    res = ((netinc.diff(18) / (revenue.shift(7) + 9.3809)).rolling(5).mean().rolling(126).skew() * 0.462395).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc078_150d_slope_v078_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc078_150d_slope_v078_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc079_252d_slope_v079_signal(assets, netinc):
    res = ((netinc.diff(9) / (assets.shift(3) + 6.5092)).rolling(84).min().rolling(252).min() * 0.847241).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc079_252d_slope_v079_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc079_252d_slope_v079_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc080_10d_slope_v080_signal(netinc, revenue):
    res = ((netinc.diff(13) / (revenue.shift(7) + 3.8914)).rolling(10).kurt().rolling(42).std().rolling(5).kurt() * 0.830752).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc080_10d_slope_v080_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc080_10d_slope_v080_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc081_5d_slope_v081_signal(assets, netinc):
    res = ((((netinc.diff(11) / (assets.shift(4) + 5.4009)).rolling(126).max().rolling(21).std().rolling(150).skew() - (netinc.diff(11) / (assets.shift(4) + 5.4009)).rolling(126).max().rolling(21).std().rolling(150).skew().rolling(5).mean()) / (netinc.diff(11) / (assets.shift(4) + 5.4009)).rolling(126).max().rolling(21).std().rolling(150).skew().rolling(5).std()) * 0.295594).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc081_5d_slope_v081_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc081_5d_slope_v081_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc082_10d_slope_v082_signal(assets, fcf):
    res = (((assets / (fcf + 3.4037)).rolling(21).max().pct_change(10) / (assets / (fcf + 3.4037)).rolling(21).max().pct_change(10).rolling(5).max()) * 0.569192).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc082_10d_slope_v082_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc082_10d_slope_v082_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc083_5d_slope_v083_signal(assets, fcf):
    res = ((fcf.diff(20) / (assets.shift(4) + 8.8666)).rolling(105).skew().pct_change(84).rolling(10).skew() * 0.069250).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc083_5d_slope_v083_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc083_5d_slope_v083_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc084_10d_slope_v084_signal(capex, netinc):
    res = (((netinc / (capex + 3.9259)) / (netinc / (capex + 3.9259)).rolling(126).max()).rolling(10).min().rolling(126).kurt() * 0.820719).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc084_10d_slope_v084_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc084_10d_slope_v084_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc085_126d_slope_v085_signal(capex, netinc):
    res = ((netinc.diff(9) / (capex.shift(8) + 8.1498)).rolling(21).mean().pct_change(5) * 0.689457).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc085_126d_slope_v085_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc085_126d_slope_v085_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc086_150d_slope_v086_signal(capex, fcf):
    res = ((fcf.diff(13) / (capex.shift(7) + 8.0253)).rolling(42).min().rolling(252).min().rolling(10).var().rolling(252).min() * 0.600156).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc086_150d_slope_v086_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc086_150d_slope_v086_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc087_21d_slope_v087_signal(netinc, revenue):
    res = ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(105).max().rolling(105).var().rolling(63).std() * 0.254153).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc087_21d_slope_v087_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc087_21d_slope_v087_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc088_84d_slope_v088_signal(assets, netinc):
    res = ((netinc.diff(7) / (assets.shift(1) + 1.8947)).pct_change(105).rolling(5).std().rolling(42).max() * 0.466596).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc088_84d_slope_v088_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc088_84d_slope_v088_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc089_150d_slope_v089_signal(capex, netinc):
    res = (((netinc / (capex + 2.4658)).rolling(126).max() / (netinc / (capex + 2.4658)).rolling(126).max().rolling(84).max()) * 0.459917).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc089_150d_slope_v089_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc089_150d_slope_v089_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc090_200d_slope_v090_signal(capex, netinc):
    res = ((((capex / (netinc + 3.4242)).rolling(150).kurt() - (capex / (netinc + 3.4242)).rolling(150).kurt().rolling(200).mean()) / (capex / (netinc + 3.4242)).rolling(150).kurt().rolling(200).std()).rolling(84).mean().rolling(200).min() * 0.049511).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc090_200d_slope_v090_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc090_200d_slope_v090_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc091_42d_slope_v091_signal(assets, netinc):
    res = ((assets / (netinc + 0.9773)).rolling(10).mean().rolling(252).max().rolling(150).mean() * 0.978221).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc091_42d_slope_v091_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc091_42d_slope_v091_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc092_252d_slope_v092_signal(netinc, revenue):
    res = (((((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max().rolling(10).max()).rolling(5).kurt() - ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max().rolling(10).max()).rolling(5).kurt().rolling(63).mean()) / ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max().rolling(10).max()).rolling(5).kurt().rolling(63).std()) * 0.976821).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc092_252d_slope_v092_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc092_252d_slope_v092_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc093_5d_slope_v093_signal(netinc, revenue):
    res = ((netinc / (revenue + 3.0361)).rolling(126).max().rolling(63).min().rolling(42).skew() * 0.213977).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc093_5d_slope_v093_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc093_5d_slope_v093_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc094_252d_slope_v094_signal(equity, netinc):
    res = (((netinc.diff(3) / (equity.shift(5) + 3.1710)).rolling(42).max().diff(21) / (netinc.diff(3) / (equity.shift(5) + 3.1710)).rolling(42).max().diff(21).rolling(105).max()) * 0.914013).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc094_252d_slope_v094_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc094_252d_slope_v094_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc095_150d_slope_v095_signal(assets, fcf):
    res = ((((fcf / (assets + 8.6720)) - (fcf / (assets + 8.6720)).rolling(105).mean()) / (fcf / (assets + 8.6720)).rolling(105).std()).rolling(105).skew().rolling(200).kurt() * 0.904991).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc095_150d_slope_v095_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc095_150d_slope_v095_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc096_150d_slope_v096_signal(capex, fcf):
    res = ((((fcf / (capex + 8.6534)).rolling(252).var().rolling(105).min() - (fcf / (capex + 8.6534)).rolling(252).var().rolling(105).min().rolling(10).mean()) / (fcf / (capex + 8.6534)).rolling(252).var().rolling(105).min().rolling(10).std()) * 0.682674).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc096_150d_slope_v096_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc096_150d_slope_v096_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc097_84d_slope_v097_signal(capex, netinc):
    res = ((capex / (netinc + 7.9435)).rolling(84).min().rolling(200).var().rolling(5).skew() * 0.479569).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc097_84d_slope_v097_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc097_84d_slope_v097_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc098_126d_slope_v098_signal(assets, netinc):
    res = ((netinc.diff(11) / (assets.shift(7) + 8.5853)).diff(63).rolling(21).mean().diff(42).rolling(200).std() * 0.788808).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc098_126d_slope_v098_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc098_126d_slope_v098_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc099_63d_slope_v099_signal(equity, netinc):
    res = ((netinc / (equity + 8.6245)).rolling(21).kurt().rolling(42).kurt().rolling(150).std() * 0.725028).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc099_63d_slope_v099_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc099_63d_slope_v099_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc100_150d_slope_v100_signal(netinc, revenue):
    res = ((((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).kurt() - (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).kurt().rolling(21).mean()) / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).kurt().rolling(21).std()).rolling(126).mean().rolling(5).mean() * 0.220534).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc100_150d_slope_v100_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc100_150d_slope_v100_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc101_10d_slope_v101_signal(equity, netinc):
    res = (((((((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min() - ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).mean()) / ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).std()) - ((((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min() - ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).mean()) / ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).std()).rolling(150).mean()) / ((((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min() - ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).mean()) / ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).std()).rolling(150).std()) * 0.762855).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc101_10d_slope_v101_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc101_10d_slope_v101_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc102_42d_slope_v102_signal(assets, fcf):
    res = (((fcf.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(105) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(105).rolling(10).max()) * 0.502283).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc102_42d_slope_v102_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc102_42d_slope_v102_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc103_105d_slope_v103_signal(capex, netinc):
    res = ((((netinc.diff(18) / (capex.shift(4) + 0.1513)) - (netinc.diff(18) / (capex.shift(4) + 0.1513)).rolling(252).mean()) / (netinc.diff(18) / (capex.shift(4) + 0.1513)).rolling(252).std()).rolling(126).kurt() * 0.947949).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc103_105d_slope_v103_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc103_105d_slope_v103_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc104_63d_slope_v104_signal(netinc, revenue):
    res = (((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(200).min() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(200).min().rolling(63).max()) * 0.569774).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc104_63d_slope_v104_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc104_63d_slope_v104_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc105_63d_slope_v105_signal(assets, fcf):
    res = ((fcf / (assets + 6.7824)).pct_change(200).rolling(42).skew().pct_change(63).rolling(84).skew() * 0.310764).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc105_63d_slope_v105_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc105_63d_slope_v105_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc106_10d_slope_v106_signal(equity, netinc):
    res = (((netinc.diff(4) / (equity.shift(9) + 0.5342)).rolling(21).mean() / (netinc.diff(4) / (equity.shift(9) + 0.5342)).rolling(21).mean().rolling(252).max()) * 0.510001).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc106_10d_slope_v106_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc106_10d_slope_v106_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc107_10d_slope_v107_signal(capex, netinc):
    res = (((((netinc.replace(0, np.nan) / capex.replace(0, np.nan)) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).max()) - ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).max()).rolling(126).mean()) / ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).max()).rolling(126).std()).diff(150).rolling(200).kurt() * 0.185516).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc107_10d_slope_v107_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc107_10d_slope_v107_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc108_21d_slope_v108_signal(capex, fcf):
    res = ((fcf.diff(15) / (capex.shift(3) + 1.6561)).rolling(126).skew().rolling(126).var().rolling(10).mean().rolling(252).std() * 0.136573).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc108_21d_slope_v108_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc108_21d_slope_v108_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc109_200d_slope_v109_signal(capex, netinc):
    res = ((((netinc.diff(15) / (capex.shift(6) + 3.6347)).diff(200) - (netinc.diff(15) / (capex.shift(6) + 3.6347)).diff(200).rolling(105).mean()) / (netinc.diff(15) / (capex.shift(6) + 3.6347)).diff(200).rolling(105).std()) * 0.916250).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc109_200d_slope_v109_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc109_200d_slope_v109_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc110_10d_slope_v110_signal(assets, netinc):
    res = ((((netinc.diff(11) / (assets.shift(2) + 2.1393)).pct_change(21).rolling(42).std() - (netinc.diff(11) / (assets.shift(2) + 2.1393)).pct_change(21).rolling(42).std().rolling(5).mean()) / (netinc.diff(11) / (assets.shift(2) + 2.1393)).pct_change(21).rolling(42).std().rolling(5).std()).diff(5) * 0.555256).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc110_10d_slope_v110_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc110_10d_slope_v110_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc111_105d_slope_v111_signal(capex, fcf):
    res = ((fcf.diff(11) / (capex.shift(5) + 6.4423)).pct_change(21).rolling(150).min().diff(150) * 0.647963).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc111_105d_slope_v111_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc111_105d_slope_v111_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc112_105d_slope_v112_signal(netinc, revenue):
    res = ((netinc.diff(20) / (revenue.shift(1) + 5.5662)).rolling(150).kurt().rolling(105).mean().pct_change(63) * 0.450177).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc112_105d_slope_v112_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc112_105d_slope_v112_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc113_200d_slope_v113_signal(assets, netinc):
    res = ((netinc.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).kurt().rolling(150).std().rolling(252).min().rolling(21).max() * 0.366162).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc113_200d_slope_v113_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc113_200d_slope_v113_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc114_42d_slope_v114_signal(assets, fcf):
    res = ((((fcf.diff(4) / (assets.shift(9) + 3.0419)).rolling(200).min().rolling(21).var() - (fcf.diff(4) / (assets.shift(9) + 3.0419)).rolling(200).min().rolling(21).var().rolling(63).mean()) / (fcf.diff(4) / (assets.shift(9) + 3.0419)).rolling(200).min().rolling(21).var().rolling(63).std()).rolling(5).min() * 0.323035).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc114_42d_slope_v114_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc114_42d_slope_v114_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc115_5d_slope_v115_signal(assets, netinc):
    res = ((assets / (netinc + 6.9262)).pct_change(21).rolling(84).kurt().rolling(63).std() * 0.386910).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc115_5d_slope_v115_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc115_5d_slope_v115_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc116_126d_slope_v116_signal(netinc, revenue):
    res = (((netinc / (revenue + 8.8968)).rolling(63).std().diff(200) / (netinc / (revenue + 8.8968)).rolling(63).std().diff(200).rolling(84).max()).rolling(150).max() * 0.597587).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc116_126d_slope_v116_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc116_126d_slope_v116_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc117_252d_slope_v117_signal(capex, fcf):
    res = ((fcf.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(5).skew().rolling(21).kurt() * 0.785057).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc117_252d_slope_v117_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc117_252d_slope_v117_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc118_5d_slope_v118_signal(equity, netinc):
    res = ((netinc.diff(2) / (equity.shift(4) + 8.0130)).rolling(21).skew().rolling(200).max().rolling(5).var().rolling(126).min() * 0.817033).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc118_5d_slope_v118_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc118_5d_slope_v118_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc119_105d_slope_v119_signal(capex, netinc):
    res = ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(126).max().rolling(126).max().pct_change(63).rolling(126).mean() * 0.193043).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc119_105d_slope_v119_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc119_105d_slope_v119_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc120_10d_slope_v120_signal(capex, netinc):
    res = ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(84).rolling(126).skew() * 0.685345).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc120_10d_slope_v120_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc120_10d_slope_v120_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc121_252d_slope_v121_signal(assets, fcf):
    res = ((((fcf.diff(13) / (assets.shift(2) + 4.7238)).rolling(42).mean().rolling(150).kurt() - (fcf.diff(13) / (assets.shift(2) + 4.7238)).rolling(42).mean().rolling(150).kurt().rolling(63).mean()) / (fcf.diff(13) / (assets.shift(2) + 4.7238)).rolling(42).mean().rolling(150).kurt().rolling(63).std()).pct_change(42) * 0.153637).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc121_252d_slope_v121_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc121_252d_slope_v121_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc122_126d_slope_v122_signal(capex, netinc):
    res = ((netinc / (capex + 9.4101)).pct_change(42).rolling(63).std() * 0.642776).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc122_126d_slope_v122_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc122_126d_slope_v122_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc123_21d_slope_v123_signal(netinc, revenue):
    res = ((revenue / (netinc + 9.5502)).rolling(105).kurt().rolling(63).max().pct_change(5) * 0.592332).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc123_21d_slope_v123_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc123_21d_slope_v123_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc124_84d_slope_v124_signal(netinc, revenue):
    res = ((revenue / (netinc + 3.0676)).rolling(105).kurt().rolling(84).skew() * 0.102345).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc124_84d_slope_v124_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc124_84d_slope_v124_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc125_200d_slope_v125_signal(capex, fcf):
    res = ((fcf.diff(2) / (capex.shift(4) + 6.2115)).rolling(63).mean().diff(63) * 0.580018).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc125_200d_slope_v125_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc125_200d_slope_v125_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc126_42d_slope_v126_signal(assets, fcf):
    res = ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).min().rolling(21).kurt() * 0.733531).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc126_42d_slope_v126_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc126_42d_slope_v126_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc127_63d_slope_v127_signal(netinc, revenue):
    res = ((netinc.diff(6) / (revenue.shift(2) + 3.0594)).rolling(105).var().rolling(63).skew() * 0.310645).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc127_63d_slope_v127_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc127_63d_slope_v127_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc128_5d_slope_v128_signal(capex, netinc):
    res = ((capex / (netinc + 1.5371)).diff(63).rolling(105).mean().rolling(105).min() * 0.461165).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc128_5d_slope_v128_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc128_5d_slope_v128_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc129_5d_slope_v129_signal(equity, netinc):
    res = (((netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).var().rolling(150).max() / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).var().rolling(150).max().rolling(63).max()) * 0.504683).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc129_5d_slope_v129_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc129_5d_slope_v129_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc130_21d_slope_v130_signal(capex, fcf):
    res = ((((((fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew() - (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).mean()) / (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).std()) - (((fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew() - (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).mean()) / (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).std()).rolling(63).mean()) / (((fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew() - (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).mean()) / (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).std()).rolling(63).std()) * 0.524889).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc130_21d_slope_v130_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc130_21d_slope_v130_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc131_84d_slope_v131_signal(capex, netinc):
    res = ((capex / (netinc + 4.3435)).rolling(10).mean().rolling(126).var().rolling(21).min().rolling(126).skew() * 0.932171).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc131_84d_slope_v131_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc131_84d_slope_v131_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc132_200d_slope_v132_signal(assets, fcf):
    res = ((fcf.diff(20) / (assets.shift(5) + 5.8420)).diff(63).pct_change(42) * 0.590621).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc132_200d_slope_v132_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc132_200d_slope_v132_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc133_42d_slope_v133_signal(assets, fcf):
    res = (((assets / (fcf + 2.4659)).rolling(252).min().rolling(200).kurt().rolling(84).std() / (assets / (fcf + 2.4659)).rolling(252).min().rolling(200).kurt().rolling(84).std().rolling(200).max()) * 0.199438).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc133_42d_slope_v133_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc133_42d_slope_v133_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc134_63d_slope_v134_signal(assets, netinc):
    res = ((netinc.diff(16) / (assets.shift(10) + 3.5239)).rolling(21).kurt().rolling(200).skew() * 0.419334).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc134_63d_slope_v134_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc134_63d_slope_v134_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc135_10d_slope_v135_signal(assets, netinc):
    res = ((netinc / (assets + 7.8601)).rolling(84).min().pct_change(105).pct_change(21) * 0.527036).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc135_10d_slope_v135_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc135_10d_slope_v135_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc136_126d_slope_v136_signal(equity, netinc):
    res = (((netinc / (equity + 4.9327)).rolling(21).skew().diff(42).rolling(63).var() / (netinc / (equity + 4.9327)).rolling(21).skew().diff(42).rolling(63).var().rolling(63).max()) * 0.917847).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc136_126d_slope_v136_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc136_126d_slope_v136_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc137_126d_slope_v137_signal(assets, netinc):
    res = ((assets / (netinc + 8.5824)).rolling(63).max().rolling(105).min().rolling(10).skew().rolling(21).skew() * 0.156009).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc137_126d_slope_v137_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc137_126d_slope_v137_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc138_21d_slope_v138_signal(assets, fcf):
    res = ((fcf.diff(16) / (assets.shift(7) + 9.8435)).rolling(252).kurt().diff(10).rolling(5).min().rolling(5).kurt() * 0.341082).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc138_21d_slope_v138_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc138_21d_slope_v138_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc139_42d_slope_v139_signal(assets, fcf):
    res = (((fcf / (assets + 9.6460)).rolling(10).max().pct_change(150) / (fcf / (assets + 9.6460)).rolling(10).max().pct_change(150).rolling(150).max()) * 0.312081).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc139_42d_slope_v139_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc139_42d_slope_v139_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc140_105d_slope_v140_signal(capex, netinc):
    res = ((((netinc / (capex + 4.4955)).rolling(10).min().diff(21) - (netinc / (capex + 4.4955)).rolling(10).min().diff(21).rolling(42).mean()) / (netinc / (capex + 4.4955)).rolling(10).min().diff(21).rolling(42).std()).rolling(63).skew() * 0.807438).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc140_105d_slope_v140_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc140_105d_slope_v140_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc141_200d_slope_v141_signal(capex, netinc):
    res = (((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).max()).pct_change(63).rolling(200).kurt() * 0.980844).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc141_200d_slope_v141_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc141_200d_slope_v141_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc142_84d_slope_v142_signal(netinc, revenue):
    res = ((((revenue / (netinc + 1.0836)).rolling(21).kurt().rolling(84).kurt().diff(150) - (revenue / (netinc + 1.0836)).rolling(21).kurt().rolling(84).kurt().diff(150).rolling(21).mean()) / (revenue / (netinc + 1.0836)).rolling(21).kurt().rolling(84).kurt().diff(150).rolling(21).std()) * 0.102390).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc142_84d_slope_v142_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc142_84d_slope_v142_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc143_5d_slope_v143_signal(equity, netinc):
    res = (((netinc / (equity + 9.4292)).rolling(42).mean() / (netinc / (equity + 9.4292)).rolling(42).mean().rolling(42).max()) * 0.793236).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc143_5d_slope_v143_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc143_5d_slope_v143_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc144_63d_slope_v144_signal(netinc, revenue):
    res = ((netinc / (revenue + 0.5397)).rolling(63).var().rolling(252).std().diff(126) * 0.272528).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc144_63d_slope_v144_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc144_63d_slope_v144_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc145_126d_slope_v145_signal(capex, netinc):
    res = ((capex / (netinc + 9.3753)).rolling(126).min().rolling(105).std() * 0.984115).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc145_126d_slope_v145_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc145_126d_slope_v145_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc146_105d_slope_v146_signal(assets, netinc):
    res = ((netinc / (assets + 1.1772)).rolling(84).skew().rolling(42).var() * 0.435040).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc146_105d_slope_v146_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc146_105d_slope_v146_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc147_63d_slope_v147_signal(capex, fcf):
    res = (((((fcf.diff(14) / (capex.shift(2) + 6.4991)) / (fcf.diff(14) / (capex.shift(2) + 6.4991)).rolling(5).max()).diff(126).rolling(200).kurt() - ((fcf.diff(14) / (capex.shift(2) + 6.4991)) / (fcf.diff(14) / (capex.shift(2) + 6.4991)).rolling(5).max()).diff(126).rolling(200).kurt().rolling(200).mean()) / ((fcf.diff(14) / (capex.shift(2) + 6.4991)) / (fcf.diff(14) / (capex.shift(2) + 6.4991)).rolling(5).max()).diff(126).rolling(200).kurt().rolling(200).std()) * 0.431490).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc147_63d_slope_v147_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc147_63d_slope_v147_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc148_252d_slope_v148_signal(netinc, revenue):
    res = ((netinc.diff(4) / (revenue.shift(4) + 3.4211)).diff(42).rolling(42).skew() * 0.261206).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc148_252d_slope_v148_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc148_252d_slope_v148_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc149_5d_slope_v149_signal(assets, fcf):
    res = ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(126).min().rolling(21).kurt().rolling(21).max().rolling(63).kurt() * 0.788069).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc149_5d_slope_v149_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc149_5d_slope_v149_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc150_150d_slope_v150_signal(netinc, revenue):
    res = ((netinc.diff(11) / (revenue.shift(6) + 6.6418)).rolling(126).skew().rolling(126).min() * 0.725247).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc150_150d_slope_v150_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc150_150d_slope_v150_signal


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
