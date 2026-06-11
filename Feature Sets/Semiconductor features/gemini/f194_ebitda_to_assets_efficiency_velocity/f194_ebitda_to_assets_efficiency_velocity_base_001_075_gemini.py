import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc001_10d_base_v001_signal(assets, ebitda):
    res = (ebitda.diff(9) / (assets.shift(4) + 0.9886)).pct_change(252).rolling(150).var() * 0.677609
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc001_10d_base_v001_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc001_10d_base_v001_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc002_126d_base_v002_signal(assets, capex):
    res = (assets / (capex + 7.2175)).rolling(42).skew().diff(21) * 0.454948
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc002_126d_base_v002_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc002_126d_base_v002_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc003_21d_base_v003_signal(assets, ebitda):
    res = (((ebitda / (assets + 9.8946)).pct_change(5).rolling(10).var().rolling(126).var() - (ebitda / (assets + 9.8946)).pct_change(5).rolling(10).var().rolling(126).var().rolling(150).mean()) / (ebitda / (assets + 9.8946)).pct_change(5).rolling(10).var().rolling(126).var().rolling(150).std()) * 0.536477
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc003_21d_base_v003_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc003_21d_base_v003_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc004_21d_base_v004_signal(capex, revenue):
    res = (revenue / (capex + 1.2081)).rolling(42).var().rolling(42).skew().pct_change(200).diff(126) * 0.710648
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc004_21d_base_v004_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc004_21d_base_v004_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc005_105d_base_v005_signal(capex, revenue):
    res = (capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(42).max().rolling(21).max().rolling(150).kurt().pct_change(200) * 0.076758
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc005_105d_base_v005_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc005_105d_base_v005_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc006_252d_base_v006_signal(ebitda, equity):
    res = ((((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std().rolling(10).max()) - ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std().rolling(10).max()).rolling(105).mean()) / ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std().rolling(10).max()).rolling(105).std()) * 0.942544
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc006_252d_base_v006_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc006_252d_base_v006_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc007_252d_base_v007_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 7.6868)) - (revenue / (ebitda + 7.6868)).rolling(200).mean()) / (revenue / (ebitda + 7.6868)).rolling(200).std()) / (((revenue / (ebitda + 7.6868)) - (revenue / (ebitda + 7.6868)).rolling(200).mean()) / (revenue / (ebitda + 7.6868)).rolling(200).std()).rolling(10).max()) * 0.959994
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc007_252d_base_v007_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc007_252d_base_v007_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc008_252d_base_v008_signal(ebitda, equity):
    res = (ebitda.diff(4) / (equity.shift(5) + 4.6718)).pct_change(63).rolling(200).skew().rolling(10).kurt().diff(126) * 0.959795
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc008_252d_base_v008_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc008_252d_base_v008_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc009_105d_base_v009_signal(ebitda, equity):
    res = (ebitda / (equity + 8.1130)).rolling(126).kurt().rolling(63).std() * 0.890221
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc009_105d_base_v009_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc009_105d_base_v009_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc010_126d_base_v010_signal(ebitda, equity):
    res = (((equity / (ebitda + 4.8047)).rolling(5).var().rolling(105).min().rolling(63).mean() - (equity / (ebitda + 4.8047)).rolling(5).var().rolling(105).min().rolling(63).mean().rolling(21).mean()) / (equity / (ebitda + 4.8047)).rolling(5).var().rolling(105).min().rolling(63).mean().rolling(21).std()) * 0.679563
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc010_126d_base_v010_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc010_126d_base_v010_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc011_21d_base_v011_signal(capex, revenue):
    res = (revenue / (capex + 2.8976)).rolling(10).min().rolling(252).std().pct_change(150) * 0.595175
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc011_21d_base_v011_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc011_21d_base_v011_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc012_21d_base_v012_signal(ebitda, revenue):
    res = ((revenue / (ebitda + 1.3706)).rolling(252).min().rolling(63).kurt() / (revenue / (ebitda + 1.3706)).rolling(252).min().rolling(63).kurt().rolling(5).max()).rolling(63).kurt() * 0.436993
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc012_21d_base_v012_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc012_21d_base_v012_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc013_21d_base_v013_signal(ebitda, equity):
    res = (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).max().rolling(21).kurt() * 0.711208
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc013_21d_base_v013_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc013_21d_base_v013_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc014_42d_base_v014_signal(assets, capex):
    res = (capex.diff(11) / (assets.shift(7) + 5.9407)).rolling(10).skew().rolling(10).std().rolling(84).mean() * 0.515688
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc014_42d_base_v014_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc014_42d_base_v014_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc015_150d_base_v015_signal(assets, capex):
    res = (((((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min() - (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).mean()) / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).std()) - (((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min() - (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).mean()) / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).std()).rolling(126).mean()) / (((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min() - (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).mean()) / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).std()).rolling(126).std()) * 0.174815
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc015_150d_base_v015_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc015_150d_base_v015_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc016_84d_base_v016_signal(capex, ebitda):
    res = (ebitda / (capex + 9.0971)).rolling(42).skew().diff(21).rolling(126).min().rolling(84).skew() * 0.670623
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc016_84d_base_v016_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc016_84d_base_v016_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc017_84d_base_v017_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).diff(105).rolling(84).min().rolling(126).max().rolling(126).std() * 0.133562
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc017_84d_base_v017_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc017_84d_base_v017_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc018_105d_base_v018_signal(assets, capex):
    res = (assets / (capex + 4.8827)).rolling(252).skew().rolling(21).skew().rolling(150).mean() * 0.480381
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc018_105d_base_v018_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc018_105d_base_v018_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc019_150d_base_v019_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(63).rolling(21).std().rolling(10).kurt() * 0.871573
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc019_150d_base_v019_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc019_150d_base_v019_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc020_150d_base_v020_signal(ebitda, revenue):
    res = (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(150).var().rolling(105).std().rolling(150).mean() * 0.098472
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc020_150d_base_v020_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc020_150d_base_v020_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc021_150d_base_v021_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).std().rolling(10).mean() * 0.656523
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc021_150d_base_v021_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc021_150d_base_v021_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc022_200d_base_v022_signal(assets, capex):
    res = (capex.diff(15) / (assets.shift(5) + 7.5819)).rolling(200).min().rolling(200).std().diff(105).rolling(105).mean() * 0.927678
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc022_200d_base_v022_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc022_200d_base_v022_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc023_252d_base_v023_signal(capex, ebitda):
    res = ((capex / (ebitda + 4.2036)) / (capex / (ebitda + 4.2036)).rolling(150).max()).rolling(21).kurt() * 0.208069
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc023_252d_base_v023_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc023_252d_base_v023_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc024_42d_base_v024_signal(ebitda, equity):
    res = (((ebitda / (equity + 7.2802)).diff(21) - (ebitda / (equity + 7.2802)).diff(21).rolling(84).mean()) / (ebitda / (equity + 7.2802)).diff(21).rolling(84).std()) * 0.790925
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc024_42d_base_v024_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc024_42d_base_v024_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc025_21d_base_v025_signal(capex, revenue):
    res = ((revenue / (capex + 6.0755)) / (revenue / (capex + 6.0755)).rolling(150).max()).rolling(105).skew().pct_change(63) * 0.620853
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc025_21d_base_v025_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc025_21d_base_v025_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc026_126d_base_v026_signal(capex, revenue):
    res = (capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(42).skew().rolling(21).max().rolling(5).mean().rolling(63).max() * 0.018746
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc026_126d_base_v026_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc026_126d_base_v026_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc027_5d_base_v027_signal(capex, ebitda):
    res = (ebitda / (capex + 7.8220)).rolling(42).std().rolling(126).std() * 0.318720
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc027_5d_base_v027_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc027_5d_base_v027_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc028_42d_base_v028_signal(capex, ebitda):
    res = ((ebitda.diff(5) / (capex.shift(10) + 2.1143)) / (ebitda.diff(5) / (capex.shift(10) + 2.1143)).rolling(10).max()).rolling(21).mean() * 0.140564
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc028_42d_base_v028_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc028_42d_base_v028_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc029_105d_base_v029_signal(capex, ebitda):
    res = (capex / (ebitda + 4.9087)).rolling(150).mean().pct_change(84).rolling(42).min().rolling(42).min() * 0.761992
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc029_105d_base_v029_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc029_105d_base_v029_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc030_252d_base_v030_signal(capex, ebitda):
    res = (ebitda / (capex + 3.9029)).rolling(252).mean().rolling(200).skew().rolling(21).min().rolling(252).std() * 0.577413
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc030_252d_base_v030_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc030_252d_base_v030_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc031_200d_base_v031_signal(capex, ebitda):
    res = (((ebitda.diff(12) / (capex.shift(7) + 2.5619)).rolling(10).skew().diff(21) - (ebitda.diff(12) / (capex.shift(7) + 2.5619)).rolling(10).skew().diff(21).rolling(200).mean()) / (ebitda.diff(12) / (capex.shift(7) + 2.5619)).rolling(10).skew().diff(21).rolling(200).std()) * 0.851170
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc031_200d_base_v031_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc031_200d_base_v031_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc032_150d_base_v032_signal(ebitda, revenue):
    res = (ebitda.diff(20) / (revenue.shift(9) + 4.4847)).rolling(10).std().rolling(105).skew().diff(21) * 0.749891
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc032_150d_base_v032_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc032_150d_base_v032_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc033_252d_base_v033_signal(ebitda, equity):
    res = (((ebitda.diff(8) / (equity.shift(1) + 8.0140)).diff(63) - (ebitda.diff(8) / (equity.shift(1) + 8.0140)).diff(63).rolling(252).mean()) / (ebitda.diff(8) / (equity.shift(1) + 8.0140)).diff(63).rolling(252).std()).rolling(200).skew().pct_change(10) * 0.976469
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc033_252d_base_v033_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc033_252d_base_v033_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc034_10d_base_v034_signal(assets, ebitda):
    res = (ebitda.diff(19) / (assets.shift(3) + 5.1034)).pct_change(126).pct_change(84) * 0.362921
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc034_10d_base_v034_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc034_10d_base_v034_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc035_252d_base_v035_signal(assets, capex):
    res = (((capex.diff(8) / (assets.shift(3) + 3.9587)) - (capex.diff(8) / (assets.shift(3) + 3.9587)).rolling(42).mean()) / (capex.diff(8) / (assets.shift(3) + 3.9587)).rolling(42).std()).rolling(126).std() * 0.030219
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc035_252d_base_v035_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc035_252d_base_v035_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc036_21d_base_v036_signal(assets, ebitda):
    res = (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).diff(126).pct_change(84).rolling(21).max().rolling(105).mean() * 0.067358
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc036_21d_base_v036_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc036_21d_base_v036_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc037_21d_base_v037_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(200).rolling(21).skew() * 0.781184
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc037_21d_base_v037_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc037_21d_base_v037_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc038_63d_base_v038_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).kurt().rolling(200).skew().rolling(200).max() * 0.286032
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc038_63d_base_v038_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc038_63d_base_v038_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc039_63d_base_v039_signal(ebitda, revenue):
    res = (((ebitda / (revenue + 2.6849)).rolling(105).max().rolling(63).std() - (ebitda / (revenue + 2.6849)).rolling(105).max().rolling(63).std().rolling(105).mean()) / (ebitda / (revenue + 2.6849)).rolling(105).max().rolling(63).std().rolling(105).std()).rolling(84).mean() * 0.842894
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc039_63d_base_v039_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc039_63d_base_v039_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc040_21d_base_v040_signal(capex, revenue):
    res = (capex / (revenue + 8.8940)).rolling(21).min().rolling(5).skew() * 0.913919
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc040_21d_base_v040_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc040_21d_base_v040_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc041_42d_base_v041_signal(capex, revenue):
    res = (((capex / (revenue + 0.3915)).pct_change(105) - (capex / (revenue + 0.3915)).pct_change(105).rolling(42).mean()) / (capex / (revenue + 0.3915)).pct_change(105).rolling(42).std()).rolling(105).min() * 0.560603
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc041_42d_base_v041_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc041_42d_base_v041_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc042_105d_base_v042_signal(assets, capex):
    res = (capex / (assets + 7.2727)).pct_change(21).rolling(5).max() * 0.655739
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc042_105d_base_v042_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc042_105d_base_v042_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc043_42d_base_v043_signal(ebitda, equity):
    res = (((ebitda.diff(16) / (equity.shift(8) + 8.6178)).rolling(150).var().rolling(105).min().rolling(10).skew() - (ebitda.diff(16) / (equity.shift(8) + 8.6178)).rolling(150).var().rolling(105).min().rolling(10).skew().rolling(5).mean()) / (ebitda.diff(16) / (equity.shift(8) + 8.6178)).rolling(150).var().rolling(105).min().rolling(10).skew().rolling(5).std()) * 0.236999
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc043_42d_base_v043_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc043_42d_base_v043_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc044_10d_base_v044_signal(ebitda, revenue):
    res = (revenue / (ebitda + 0.9698)).rolling(84).std().rolling(84).std().rolling(21).mean() * 0.782002
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc044_10d_base_v044_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc044_10d_base_v044_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc045_21d_base_v045_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84).rolling(252).max() * 0.895867
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc045_21d_base_v045_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc045_21d_base_v045_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc046_21d_base_v046_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).kurt().rolling(63).kurt() / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).kurt().rolling(63).kurt().rolling(252).max()) * 0.568653
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc046_21d_base_v046_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc046_21d_base_v046_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc047_200d_base_v047_signal(ebitda, equity):
    res = ((((equity / (ebitda + 1.7104)) - (equity / (ebitda + 1.7104)).rolling(200).mean()) / (equity / (ebitda + 1.7104)).rolling(200).std()) / (((equity / (ebitda + 1.7104)) - (equity / (ebitda + 1.7104)).rolling(200).mean()) / (equity / (ebitda + 1.7104)).rolling(200).std()).rolling(42).max()) * 0.960236
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc047_200d_base_v047_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc047_200d_base_v047_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc048_252d_base_v048_signal(ebitda, revenue):
    res = (revenue / (ebitda + 3.6616)).rolling(252).var().rolling(84).skew() * 0.342976
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc048_252d_base_v048_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc048_252d_base_v048_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc049_63d_base_v049_signal(ebitda, revenue):
    res = ((revenue / (ebitda + 0.4750)).rolling(10).skew() / (revenue / (ebitda + 0.4750)).rolling(10).skew().rolling(126).max()) * 0.602281
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc049_63d_base_v049_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc049_63d_base_v049_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc050_200d_base_v050_signal(capex, ebitda):
    res = ((ebitda / (capex + 6.0215)).rolling(126).mean() / (ebitda / (capex + 6.0215)).rolling(126).mean().rolling(10).max()).rolling(42).kurt() * 0.505313
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc050_200d_base_v050_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc050_200d_base_v050_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc051_150d_base_v051_signal(ebitda, revenue):
    res = (revenue / (ebitda + 5.9647)).rolling(150).var().diff(200) * 0.070220
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc051_150d_base_v051_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc051_150d_base_v051_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc052_150d_base_v052_signal(ebitda, revenue):
    res = ((ebitda.diff(2) / (revenue.shift(4) + 4.7365)) / (ebitda.diff(2) / (revenue.shift(4) + 4.7365)).rolling(10).max()).pct_change(252).rolling(10).min().rolling(126).max() * 0.152931
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc052_150d_base_v052_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc052_150d_base_v052_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc053_252d_base_v053_signal(capex, revenue):
    res = ((capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).var().rolling(10).mean() / (capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).var().rolling(10).mean().rolling(42).max()) * 0.925335
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc053_252d_base_v053_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc053_252d_base_v053_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc054_21d_base_v054_signal(ebitda, equity):
    res = (ebitda / (equity + 5.9806)).rolling(252).mean().rolling(200).skew().rolling(63).max() * 0.271273
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc054_21d_base_v054_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc054_21d_base_v054_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc055_200d_base_v055_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)) - (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).mean()) / (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).std()).diff(105) / (((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)) - (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).mean()) / (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).std()).diff(105).rolling(84).max()) * 0.004972
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc055_200d_base_v055_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc055_200d_base_v055_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc056_84d_base_v056_signal(ebitda, equity):
    res = (equity / (ebitda + 5.3287)).rolling(84).kurt().rolling(150).skew() * 0.725070
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc056_84d_base_v056_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc056_84d_base_v056_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc057_10d_base_v057_signal(ebitda, equity):
    res = ((((ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10) / (ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10).rolling(84).max()) - ((ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10) / (ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10).rolling(84).max()).rolling(105).mean()) / ((ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10) / (ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10).rolling(84).max()).rolling(105).std()).pct_change(21) * 0.181470
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc057_10d_base_v057_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc057_10d_base_v057_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc058_84d_base_v058_signal(assets, ebitda):
    res = (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(42).min().rolling(21).std() * 0.159573
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc058_84d_base_v058_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc058_84d_base_v058_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc059_84d_base_v059_signal(ebitda, revenue):
    res = (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).skew().rolling(252).skew().pct_change(105) * 0.239639
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc059_84d_base_v059_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc059_84d_base_v059_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc060_63d_base_v060_signal(ebitda, revenue):
    res = (ebitda / (revenue + 9.9402)).rolling(105).max().diff(200) * 0.116314
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc060_63d_base_v060_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc060_63d_base_v060_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc061_84d_base_v061_signal(capex, revenue):
    res = (capex / (revenue + 2.1972)).pct_change(21).rolling(200).var().rolling(5).kurt() * 0.573416
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc061_84d_base_v061_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc061_84d_base_v061_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc062_105d_base_v062_signal(capex, revenue):
    res = (capex / (revenue + 2.0128)).rolling(63).skew().rolling(252).skew().rolling(200).var().rolling(200).skew() * 0.492826
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc062_105d_base_v062_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc062_105d_base_v062_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc063_252d_base_v063_signal(assets, ebitda):
    res = (((assets / (ebitda + 0.5419)).diff(84).rolling(126).skew().rolling(105).mean() - (assets / (ebitda + 0.5419)).diff(84).rolling(126).skew().rolling(105).mean().rolling(42).mean()) / (assets / (ebitda + 0.5419)).diff(84).rolling(126).skew().rolling(105).mean().rolling(42).std()) * 0.792891
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc063_252d_base_v063_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc063_252d_base_v063_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc064_42d_base_v064_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).skew().rolling(105).skew().rolling(21).kurt() / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).skew().rolling(105).skew().rolling(21).kurt().rolling(252).max()) * 0.510823
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc064_42d_base_v064_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc064_42d_base_v064_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc065_42d_base_v065_signal(ebitda, revenue):
    res = (ebitda.diff(5) / (revenue.shift(5) + 7.8333)).rolling(42).std().rolling(126).skew() * 0.148638
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc065_42d_base_v065_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc065_42d_base_v065_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc066_150d_base_v066_signal(assets, capex):
    res = (((((assets / (capex + 4.5724)) - (assets / (capex + 4.5724)).rolling(21).mean()) / (assets / (capex + 4.5724)).rolling(21).std()).rolling(63).min() - (((assets / (capex + 4.5724)) - (assets / (capex + 4.5724)).rolling(21).mean()) / (assets / (capex + 4.5724)).rolling(21).std()).rolling(63).min().rolling(10).mean()) / (((assets / (capex + 4.5724)) - (assets / (capex + 4.5724)).rolling(21).mean()) / (assets / (capex + 4.5724)).rolling(21).std()).rolling(63).min().rolling(10).std()) * 0.603504
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc066_150d_base_v066_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc066_150d_base_v066_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc067_105d_base_v067_signal(assets, ebitda):
    res = (ebitda.diff(6) / (assets.shift(3) + 0.3377)).rolling(10).std().rolling(42).skew().diff(126).rolling(150).skew() * 0.995230
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc067_105d_base_v067_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc067_105d_base_v067_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc068_21d_base_v068_signal(capex, ebitda):
    res = (ebitda.diff(17) / (capex.shift(10) + 1.4872)).diff(10).diff(84).rolling(84).var() * 0.677496
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc068_21d_base_v068_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc068_21d_base_v068_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc069_63d_base_v069_signal(assets, capex):
    res = ((((capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew() / (capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew().rolling(5).max()).rolling(252).var() - ((capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew() / (capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew().rolling(5).max()).rolling(252).var().rolling(105).mean()) / ((capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew() / (capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew().rolling(5).max()).rolling(252).var().rolling(105).std()) * 0.921777
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc069_63d_base_v069_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc069_63d_base_v069_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc070_5d_base_v070_signal(ebitda, equity):
    res = (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max().rolling(10).mean() * 0.402183
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc070_5d_base_v070_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc070_5d_base_v070_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc071_42d_base_v071_signal(capex, ebitda):
    res = ((((ebitda / (capex + 7.3313)).rolling(63).kurt() / (ebitda / (capex + 7.3313)).rolling(63).kurt().rolling(105).max()).rolling(105).kurt() - ((ebitda / (capex + 7.3313)).rolling(63).kurt() / (ebitda / (capex + 7.3313)).rolling(63).kurt().rolling(105).max()).rolling(105).kurt().rolling(21).mean()) / ((ebitda / (capex + 7.3313)).rolling(63).kurt() / (ebitda / (capex + 7.3313)).rolling(63).kurt().rolling(105).max()).rolling(105).kurt().rolling(21).std()) * 0.642063
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc071_42d_base_v071_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc071_42d_base_v071_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc072_126d_base_v072_signal(ebitda, equity):
    res = (ebitda / (equity + 7.9578)).rolling(5).skew().pct_change(105) * 0.642573
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc072_126d_base_v072_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc072_126d_base_v072_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc073_42d_base_v073_signal(ebitda, equity):
    res = ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).var() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).var().rolling(200).max()) * 0.775752
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc073_42d_base_v073_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc073_42d_base_v073_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc074_200d_base_v074_signal(assets, capex):
    res = ((assets / (capex + 7.7742)) / (assets / (capex + 7.7742)).rolling(126).max()).rolling(105).min().rolling(126).max() * 0.347632
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc074_200d_base_v074_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc074_200d_base_v074_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc075_5d_base_v075_signal(assets, capex):
    res = (assets / (capex + 0.8209)).rolling(42).mean().rolling(126).max() * 0.484494
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc075_5d_base_v075_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc075_5d_base_v075_signal


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
