import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc001_84d_jerk_v001_signal(assets, ebitda):
    res = ((ebitda.diff(9) / (assets.shift(4) + 0.9886)).pct_change(252).rolling(150).var() * 0.677609).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc001_84d_jerk_v001_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc001_84d_jerk_v001_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc002_150d_jerk_v002_signal(assets, capex):
    res = ((assets / (capex + 7.2175)).rolling(42).skew().diff(21) * 0.454948).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc002_150d_jerk_v002_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc002_150d_jerk_v002_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc003_21d_jerk_v003_signal(assets, ebitda):
    res = ((((ebitda / (assets + 9.8946)).pct_change(5).rolling(10).var().rolling(126).var() - (ebitda / (assets + 9.8946)).pct_change(5).rolling(10).var().rolling(126).var().rolling(150).mean()) / (ebitda / (assets + 9.8946)).pct_change(5).rolling(10).var().rolling(126).var().rolling(150).std()) * 0.536477).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc003_21d_jerk_v003_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc003_21d_jerk_v003_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc004_200d_jerk_v004_signal(capex, revenue):
    res = ((revenue / (capex + 1.2081)).rolling(42).var().rolling(42).skew().pct_change(200).diff(126) * 0.710648).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc004_200d_jerk_v004_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc004_200d_jerk_v004_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc005_200d_jerk_v005_signal(capex, revenue):
    res = ((capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(42).max().rolling(21).max().rolling(150).kurt().pct_change(200) * 0.076758).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc005_200d_jerk_v005_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc005_200d_jerk_v005_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc006_10d_jerk_v006_signal(ebitda, equity):
    res = (((((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std().rolling(10).max()) - ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std().rolling(10).max()).rolling(105).mean()) / ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).std().rolling(10).max()).rolling(105).std()) * 0.942544).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc006_10d_jerk_v006_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc006_10d_jerk_v006_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc007_252d_jerk_v007_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 7.6868)) - (revenue / (ebitda + 7.6868)).rolling(200).mean()) / (revenue / (ebitda + 7.6868)).rolling(200).std()) / (((revenue / (ebitda + 7.6868)) - (revenue / (ebitda + 7.6868)).rolling(200).mean()) / (revenue / (ebitda + 7.6868)).rolling(200).std()).rolling(10).max()) * 0.959994).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc007_252d_jerk_v007_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc007_252d_jerk_v007_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc008_200d_jerk_v008_signal(ebitda, equity):
    res = ((ebitda.diff(4) / (equity.shift(5) + 4.6718)).pct_change(63).rolling(200).skew().rolling(10).kurt().diff(126) * 0.959795).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc008_200d_jerk_v008_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc008_200d_jerk_v008_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc009_200d_jerk_v009_signal(ebitda, equity):
    res = ((ebitda / (equity + 8.1130)).rolling(126).kurt().rolling(63).std() * 0.890221).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc009_200d_jerk_v009_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc009_200d_jerk_v009_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc010_21d_jerk_v010_signal(ebitda, equity):
    res = ((((equity / (ebitda + 4.8047)).rolling(5).var().rolling(105).min().rolling(63).mean() - (equity / (ebitda + 4.8047)).rolling(5).var().rolling(105).min().rolling(63).mean().rolling(21).mean()) / (equity / (ebitda + 4.8047)).rolling(5).var().rolling(105).min().rolling(63).mean().rolling(21).std()) * 0.679563).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc010_21d_jerk_v010_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc010_21d_jerk_v010_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc011_84d_jerk_v011_signal(capex, revenue):
    res = ((revenue / (capex + 2.8976)).rolling(10).min().rolling(252).std().pct_change(150) * 0.595175).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc011_84d_jerk_v011_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc011_84d_jerk_v011_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc012_126d_jerk_v012_signal(ebitda, revenue):
    res = (((revenue / (ebitda + 1.3706)).rolling(252).min().rolling(63).kurt() / (revenue / (ebitda + 1.3706)).rolling(252).min().rolling(63).kurt().rolling(5).max()).rolling(63).kurt() * 0.436993).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc012_126d_jerk_v012_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc012_126d_jerk_v012_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc013_84d_jerk_v013_signal(ebitda, equity):
    res = ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).max().rolling(21).kurt() * 0.711208).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc013_84d_jerk_v013_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc013_84d_jerk_v013_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc014_200d_jerk_v014_signal(assets, capex):
    res = ((capex.diff(11) / (assets.shift(7) + 5.9407)).rolling(10).skew().rolling(10).std().rolling(84).mean() * 0.515688).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc014_200d_jerk_v014_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc014_200d_jerk_v014_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc015_200d_jerk_v015_signal(assets, capex):
    res = ((((((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min() - (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).mean()) / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).std()) - (((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min() - (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).mean()) / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).std()).rolling(126).mean()) / (((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min() - (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).mean()) / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).min().rolling(84).std()).rolling(126).std()) * 0.174815).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc015_200d_jerk_v015_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc015_200d_jerk_v015_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc016_5d_jerk_v016_signal(capex, ebitda):
    res = ((ebitda / (capex + 9.0971)).rolling(42).skew().diff(21).rolling(126).min().rolling(84).skew() * 0.670623).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc016_5d_jerk_v016_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc016_5d_jerk_v016_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc017_105d_jerk_v017_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).diff(105).rolling(84).min().rolling(126).max().rolling(126).std() * 0.133562).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc017_105d_jerk_v017_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc017_105d_jerk_v017_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc018_21d_jerk_v018_signal(assets, capex):
    res = ((assets / (capex + 4.8827)).rolling(252).skew().rolling(21).skew().rolling(150).mean() * 0.480381).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc018_21d_jerk_v018_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc018_21d_jerk_v018_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc019_200d_jerk_v019_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(63).rolling(21).std().rolling(10).kurt() * 0.871573).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc019_200d_jerk_v019_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc019_200d_jerk_v019_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc020_200d_jerk_v020_signal(ebitda, revenue):
    res = ((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(150).var().rolling(105).std().rolling(150).mean() * 0.098472).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc020_200d_jerk_v020_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc020_200d_jerk_v020_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc021_63d_jerk_v021_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).std().rolling(10).mean() * 0.656523).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc021_63d_jerk_v021_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc021_63d_jerk_v021_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc022_200d_jerk_v022_signal(assets, capex):
    res = ((capex.diff(15) / (assets.shift(5) + 7.5819)).rolling(200).min().rolling(200).std().diff(105).rolling(105).mean() * 0.927678).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc022_200d_jerk_v022_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc022_200d_jerk_v022_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc023_42d_jerk_v023_signal(capex, ebitda):
    res = (((capex / (ebitda + 4.2036)) / (capex / (ebitda + 4.2036)).rolling(150).max()).rolling(21).kurt() * 0.208069).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc023_42d_jerk_v023_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc023_42d_jerk_v023_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc024_84d_jerk_v024_signal(ebitda, equity):
    res = ((((ebitda / (equity + 7.2802)).diff(21) - (ebitda / (equity + 7.2802)).diff(21).rolling(84).mean()) / (ebitda / (equity + 7.2802)).diff(21).rolling(84).std()) * 0.790925).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc024_84d_jerk_v024_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc024_84d_jerk_v024_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc025_10d_jerk_v025_signal(capex, revenue):
    res = (((revenue / (capex + 6.0755)) / (revenue / (capex + 6.0755)).rolling(150).max()).rolling(105).skew().pct_change(63) * 0.620853).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc025_10d_jerk_v025_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc025_10d_jerk_v025_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc026_63d_jerk_v026_signal(capex, revenue):
    res = ((capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(42).skew().rolling(21).max().rolling(5).mean().rolling(63).max() * 0.018746).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc026_63d_jerk_v026_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc026_63d_jerk_v026_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc027_10d_jerk_v027_signal(capex, ebitda):
    res = ((ebitda / (capex + 7.8220)).rolling(42).std().rolling(126).std() * 0.318720).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc027_10d_jerk_v027_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc027_10d_jerk_v027_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc028_10d_jerk_v028_signal(capex, ebitda):
    res = (((ebitda.diff(5) / (capex.shift(10) + 2.1143)) / (ebitda.diff(5) / (capex.shift(10) + 2.1143)).rolling(10).max()).rolling(21).mean() * 0.140564).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc028_10d_jerk_v028_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc028_10d_jerk_v028_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc029_5d_jerk_v029_signal(capex, ebitda):
    res = ((capex / (ebitda + 4.9087)).rolling(150).mean().pct_change(84).rolling(42).min().rolling(42).min() * 0.761992).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc029_5d_jerk_v029_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc029_5d_jerk_v029_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc030_105d_jerk_v030_signal(capex, ebitda):
    res = ((ebitda / (capex + 3.9029)).rolling(252).mean().rolling(200).skew().rolling(21).min().rolling(252).std() * 0.577413).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc030_105d_jerk_v030_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc030_105d_jerk_v030_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc031_126d_jerk_v031_signal(capex, ebitda):
    res = ((((ebitda.diff(12) / (capex.shift(7) + 2.5619)).rolling(10).skew().diff(21) - (ebitda.diff(12) / (capex.shift(7) + 2.5619)).rolling(10).skew().diff(21).rolling(200).mean()) / (ebitda.diff(12) / (capex.shift(7) + 2.5619)).rolling(10).skew().diff(21).rolling(200).std()) * 0.851170).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc031_126d_jerk_v031_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc031_126d_jerk_v031_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc032_5d_jerk_v032_signal(ebitda, revenue):
    res = ((ebitda.diff(20) / (revenue.shift(9) + 4.4847)).rolling(10).std().rolling(105).skew().diff(21) * 0.749891).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc032_5d_jerk_v032_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc032_5d_jerk_v032_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc033_42d_jerk_v033_signal(ebitda, equity):
    res = ((((ebitda.diff(8) / (equity.shift(1) + 8.0140)).diff(63) - (ebitda.diff(8) / (equity.shift(1) + 8.0140)).diff(63).rolling(252).mean()) / (ebitda.diff(8) / (equity.shift(1) + 8.0140)).diff(63).rolling(252).std()).rolling(200).skew().pct_change(10) * 0.976469).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc033_42d_jerk_v033_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc033_42d_jerk_v033_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc034_105d_jerk_v034_signal(assets, ebitda):
    res = ((ebitda.diff(19) / (assets.shift(3) + 5.1034)).pct_change(126).pct_change(84) * 0.362921).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc034_105d_jerk_v034_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc034_105d_jerk_v034_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc035_200d_jerk_v035_signal(assets, capex):
    res = ((((capex.diff(8) / (assets.shift(3) + 3.9587)) - (capex.diff(8) / (assets.shift(3) + 3.9587)).rolling(42).mean()) / (capex.diff(8) / (assets.shift(3) + 3.9587)).rolling(42).std()).rolling(126).std() * 0.030219).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc035_200d_jerk_v035_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc035_200d_jerk_v035_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc036_10d_jerk_v036_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).diff(126).pct_change(84).rolling(21).max().rolling(105).mean() * 0.067358).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc036_10d_jerk_v036_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc036_10d_jerk_v036_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc037_10d_jerk_v037_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(200).rolling(21).skew() * 0.781184).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc037_10d_jerk_v037_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc037_10d_jerk_v037_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc038_105d_jerk_v038_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).kurt().rolling(200).skew().rolling(200).max() * 0.286032).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc038_105d_jerk_v038_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc038_105d_jerk_v038_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc039_84d_jerk_v039_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 2.6849)).rolling(105).max().rolling(63).std() - (ebitda / (revenue + 2.6849)).rolling(105).max().rolling(63).std().rolling(105).mean()) / (ebitda / (revenue + 2.6849)).rolling(105).max().rolling(63).std().rolling(105).std()).rolling(84).mean() * 0.842894).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc039_84d_jerk_v039_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc039_84d_jerk_v039_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc040_105d_jerk_v040_signal(capex, revenue):
    res = ((capex / (revenue + 8.8940)).rolling(21).min().rolling(5).skew() * 0.913919).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc040_105d_jerk_v040_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc040_105d_jerk_v040_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc041_200d_jerk_v041_signal(capex, revenue):
    res = ((((capex / (revenue + 0.3915)).pct_change(105) - (capex / (revenue + 0.3915)).pct_change(105).rolling(42).mean()) / (capex / (revenue + 0.3915)).pct_change(105).rolling(42).std()).rolling(105).min() * 0.560603).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc041_200d_jerk_v041_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc041_200d_jerk_v041_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc042_42d_jerk_v042_signal(assets, capex):
    res = ((capex / (assets + 7.2727)).pct_change(21).rolling(5).max() * 0.655739).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc042_42d_jerk_v042_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc042_42d_jerk_v042_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc043_200d_jerk_v043_signal(ebitda, equity):
    res = ((((ebitda.diff(16) / (equity.shift(8) + 8.6178)).rolling(150).var().rolling(105).min().rolling(10).skew() - (ebitda.diff(16) / (equity.shift(8) + 8.6178)).rolling(150).var().rolling(105).min().rolling(10).skew().rolling(5).mean()) / (ebitda.diff(16) / (equity.shift(8) + 8.6178)).rolling(150).var().rolling(105).min().rolling(10).skew().rolling(5).std()) * 0.236999).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc043_200d_jerk_v043_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc043_200d_jerk_v043_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc044_42d_jerk_v044_signal(ebitda, revenue):
    res = ((revenue / (ebitda + 0.9698)).rolling(84).std().rolling(84).std().rolling(21).mean() * 0.782002).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc044_42d_jerk_v044_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc044_42d_jerk_v044_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc045_5d_jerk_v045_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84).rolling(252).max() * 0.895867).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc045_5d_jerk_v045_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc045_5d_jerk_v045_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc046_5d_jerk_v046_signal(assets, capex):
    res = (((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).kurt().rolling(63).kurt() / (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).kurt().rolling(63).kurt().rolling(252).max()) * 0.568653).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc046_5d_jerk_v046_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc046_5d_jerk_v046_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc047_63d_jerk_v047_signal(ebitda, equity):
    res = (((((equity / (ebitda + 1.7104)) - (equity / (ebitda + 1.7104)).rolling(200).mean()) / (equity / (ebitda + 1.7104)).rolling(200).std()) / (((equity / (ebitda + 1.7104)) - (equity / (ebitda + 1.7104)).rolling(200).mean()) / (equity / (ebitda + 1.7104)).rolling(200).std()).rolling(42).max()) * 0.960236).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc047_63d_jerk_v047_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc047_63d_jerk_v047_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc048_150d_jerk_v048_signal(ebitda, revenue):
    res = ((revenue / (ebitda + 3.6616)).rolling(252).var().rolling(84).skew() * 0.342976).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc048_150d_jerk_v048_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc048_150d_jerk_v048_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc049_105d_jerk_v049_signal(ebitda, revenue):
    res = (((revenue / (ebitda + 0.4750)).rolling(10).skew() / (revenue / (ebitda + 0.4750)).rolling(10).skew().rolling(126).max()) * 0.602281).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc049_105d_jerk_v049_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc049_105d_jerk_v049_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc050_42d_jerk_v050_signal(capex, ebitda):
    res = (((ebitda / (capex + 6.0215)).rolling(126).mean() / (ebitda / (capex + 6.0215)).rolling(126).mean().rolling(10).max()).rolling(42).kurt() * 0.505313).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc050_42d_jerk_v050_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc050_42d_jerk_v050_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc051_200d_jerk_v051_signal(ebitda, revenue):
    res = ((revenue / (ebitda + 5.9647)).rolling(150).var().diff(200) * 0.070220).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc051_200d_jerk_v051_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc051_200d_jerk_v051_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc052_84d_jerk_v052_signal(ebitda, revenue):
    res = (((ebitda.diff(2) / (revenue.shift(4) + 4.7365)) / (ebitda.diff(2) / (revenue.shift(4) + 4.7365)).rolling(10).max()).pct_change(252).rolling(10).min().rolling(126).max() * 0.152931).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc052_84d_jerk_v052_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc052_84d_jerk_v052_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc053_21d_jerk_v053_signal(capex, revenue):
    res = (((capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).var().rolling(10).mean() / (capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).var().rolling(10).mean().rolling(42).max()) * 0.925335).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc053_21d_jerk_v053_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc053_21d_jerk_v053_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc054_21d_jerk_v054_signal(ebitda, equity):
    res = ((ebitda / (equity + 5.9806)).rolling(252).mean().rolling(200).skew().rolling(63).max() * 0.271273).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc054_21d_jerk_v054_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc054_21d_jerk_v054_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc055_42d_jerk_v055_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)) - (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).mean()) / (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).std()).diff(105) / (((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)) - (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).mean()) / (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).std()).diff(105).rolling(84).max()) * 0.004972).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc055_42d_jerk_v055_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc055_42d_jerk_v055_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc056_42d_jerk_v056_signal(ebitda, equity):
    res = ((equity / (ebitda + 5.3287)).rolling(84).kurt().rolling(150).skew() * 0.725070).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc056_42d_jerk_v056_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc056_42d_jerk_v056_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc057_84d_jerk_v057_signal(ebitda, equity):
    res = (((((ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10) / (ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10).rolling(84).max()) - ((ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10) / (ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10).rolling(84).max()).rolling(105).mean()) / ((ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10) / (ebitda.diff(18) / (equity.shift(2) + 8.4083)).diff(10).rolling(84).max()).rolling(105).std()).pct_change(21) * 0.181470).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc057_84d_jerk_v057_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc057_84d_jerk_v057_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc058_42d_jerk_v058_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(42).min().rolling(21).std() * 0.159573).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc058_42d_jerk_v058_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc058_42d_jerk_v058_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc059_105d_jerk_v059_signal(ebitda, revenue):
    res = ((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).skew().rolling(252).skew().pct_change(105) * 0.239639).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc059_105d_jerk_v059_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc059_105d_jerk_v059_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc060_42d_jerk_v060_signal(ebitda, revenue):
    res = ((ebitda / (revenue + 9.9402)).rolling(105).max().diff(200) * 0.116314).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc060_42d_jerk_v060_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc060_42d_jerk_v060_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc061_21d_jerk_v061_signal(capex, revenue):
    res = ((capex / (revenue + 2.1972)).pct_change(21).rolling(200).var().rolling(5).kurt() * 0.573416).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc061_21d_jerk_v061_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc061_21d_jerk_v061_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc062_200d_jerk_v062_signal(capex, revenue):
    res = ((capex / (revenue + 2.0128)).rolling(63).skew().rolling(252).skew().rolling(200).var().rolling(200).skew() * 0.492826).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc062_200d_jerk_v062_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc062_200d_jerk_v062_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc063_5d_jerk_v063_signal(assets, ebitda):
    res = ((((assets / (ebitda + 0.5419)).diff(84).rolling(126).skew().rolling(105).mean() - (assets / (ebitda + 0.5419)).diff(84).rolling(126).skew().rolling(105).mean().rolling(42).mean()) / (assets / (ebitda + 0.5419)).diff(84).rolling(126).skew().rolling(105).mean().rolling(42).std()) * 0.792891).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc063_5d_jerk_v063_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc063_5d_jerk_v063_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc064_84d_jerk_v064_signal(assets, ebitda):
    res = (((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).skew().rolling(105).skew().rolling(21).kurt() / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(63).skew().rolling(105).skew().rolling(21).kurt().rolling(252).max()) * 0.510823).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc064_84d_jerk_v064_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc064_84d_jerk_v064_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc065_63d_jerk_v065_signal(ebitda, revenue):
    res = ((ebitda.diff(5) / (revenue.shift(5) + 7.8333)).rolling(42).std().rolling(126).skew() * 0.148638).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc065_63d_jerk_v065_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc065_63d_jerk_v065_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc066_63d_jerk_v066_signal(assets, capex):
    res = ((((((assets / (capex + 4.5724)) - (assets / (capex + 4.5724)).rolling(21).mean()) / (assets / (capex + 4.5724)).rolling(21).std()).rolling(63).min() - (((assets / (capex + 4.5724)) - (assets / (capex + 4.5724)).rolling(21).mean()) / (assets / (capex + 4.5724)).rolling(21).std()).rolling(63).min().rolling(10).mean()) / (((assets / (capex + 4.5724)) - (assets / (capex + 4.5724)).rolling(21).mean()) / (assets / (capex + 4.5724)).rolling(21).std()).rolling(63).min().rolling(10).std()) * 0.603504).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc066_63d_jerk_v066_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc066_63d_jerk_v066_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc067_10d_jerk_v067_signal(assets, ebitda):
    res = ((ebitda.diff(6) / (assets.shift(3) + 0.3377)).rolling(10).std().rolling(42).skew().diff(126).rolling(150).skew() * 0.995230).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc067_10d_jerk_v067_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc067_10d_jerk_v067_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc068_252d_jerk_v068_signal(capex, ebitda):
    res = ((ebitda.diff(17) / (capex.shift(10) + 1.4872)).diff(10).diff(84).rolling(84).var() * 0.677496).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc068_252d_jerk_v068_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc068_252d_jerk_v068_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc069_126d_jerk_v069_signal(assets, capex):
    res = (((((capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew() / (capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew().rolling(5).max()).rolling(252).var() - ((capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew() / (capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew().rolling(5).max()).rolling(252).var().rolling(105).mean()) / ((capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew() / (capex.diff(15) / (assets.shift(8) + 5.6028)).rolling(21).skew().rolling(5).max()).rolling(252).var().rolling(105).std()) * 0.921777).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc069_126d_jerk_v069_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc069_126d_jerk_v069_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc070_200d_jerk_v070_signal(ebitda, equity):
    res = ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max().rolling(10).mean() * 0.402183).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc070_200d_jerk_v070_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc070_200d_jerk_v070_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc071_10d_jerk_v071_signal(capex, ebitda):
    res = (((((ebitda / (capex + 7.3313)).rolling(63).kurt() / (ebitda / (capex + 7.3313)).rolling(63).kurt().rolling(105).max()).rolling(105).kurt() - ((ebitda / (capex + 7.3313)).rolling(63).kurt() / (ebitda / (capex + 7.3313)).rolling(63).kurt().rolling(105).max()).rolling(105).kurt().rolling(21).mean()) / ((ebitda / (capex + 7.3313)).rolling(63).kurt() / (ebitda / (capex + 7.3313)).rolling(63).kurt().rolling(105).max()).rolling(105).kurt().rolling(21).std()) * 0.642063).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc071_10d_jerk_v071_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc071_10d_jerk_v071_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc072_150d_jerk_v072_signal(ebitda, equity):
    res = ((ebitda / (equity + 7.9578)).rolling(5).skew().pct_change(105) * 0.642573).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc072_150d_jerk_v072_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc072_150d_jerk_v072_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc073_63d_jerk_v073_signal(ebitda, equity):
    res = (((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).var() / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(252).var().rolling(200).max()) * 0.775752).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc073_63d_jerk_v073_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc073_63d_jerk_v073_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc074_42d_jerk_v074_signal(assets, capex):
    res = (((assets / (capex + 7.7742)) / (assets / (capex + 7.7742)).rolling(126).max()).rolling(105).min().rolling(126).max() * 0.347632).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc074_42d_jerk_v074_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc074_42d_jerk_v074_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc075_21d_jerk_v075_signal(assets, capex):
    res = ((assets / (capex + 0.8209)).rolling(42).mean().rolling(126).max() * 0.484494).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc075_21d_jerk_v075_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc075_21d_jerk_v075_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc076_126d_jerk_v076_signal(assets, capex):
    res = ((capex.diff(12) / (assets.shift(7) + 6.2394)).rolling(150).kurt().pct_change(84) * 0.923371).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc076_126d_jerk_v076_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc076_126d_jerk_v076_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc077_150d_jerk_v077_signal(capex, ebitda):
    res = ((ebitda / (capex + 9.9071)).rolling(84).kurt().rolling(150).kurt().rolling(63).skew() * 0.516607).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc077_150d_jerk_v077_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc077_150d_jerk_v077_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc078_105d_jerk_v078_signal(capex, revenue):
    res = (((capex / (revenue + 4.9528)) / (capex / (revenue + 4.9528)).rolling(21).max()).rolling(105).var() * 0.591189).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc078_105d_jerk_v078_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc078_105d_jerk_v078_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc079_150d_jerk_v079_signal(ebitda, revenue):
    res = (((((ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew() / (ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew().rolling(63).max()) - ((ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew() / (ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew().rolling(63).max()).rolling(84).mean()) / ((ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew() / (ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew().rolling(63).max()).rolling(84).std()) * 0.913350).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc079_150d_jerk_v079_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc079_150d_jerk_v079_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc080_10d_jerk_v080_signal(ebitda, revenue):
    res = ((ebitda.diff(6) / (revenue.shift(4) + 1.9631)).rolling(252).std().rolling(5).skew().diff(252).rolling(105).var() * 0.260506).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc080_10d_jerk_v080_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc080_10d_jerk_v080_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc081_126d_jerk_v081_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(42).diff(84).pct_change(150) * 0.402329).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc081_126d_jerk_v081_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc081_126d_jerk_v081_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc082_63d_jerk_v082_signal(assets, capex):
    res = ((capex.diff(8) / (assets.shift(10) + 9.9627)).rolling(126).std().rolling(42).skew().pct_change(10) * 0.600091).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc082_63d_jerk_v082_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc082_63d_jerk_v082_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc083_252d_jerk_v083_signal(ebitda, revenue):
    res = ((((ebitda.diff(2) / (revenue.shift(9) + 0.6557)) - (ebitda.diff(2) / (revenue.shift(9) + 0.6557)).rolling(5).mean()) / (ebitda.diff(2) / (revenue.shift(9) + 0.6557)).rolling(5).std()).rolling(42).kurt() * 0.507662).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc083_252d_jerk_v083_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc083_252d_jerk_v083_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc084_21d_jerk_v084_signal(capex, ebitda):
    res = (((ebitda / (capex + 9.3518)).rolling(21).kurt().rolling(5).std() / (ebitda / (capex + 9.3518)).rolling(21).kurt().rolling(5).std().rolling(10).max()).rolling(5).var() * 0.985757).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc084_21d_jerk_v084_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc084_21d_jerk_v084_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc085_150d_jerk_v085_signal(capex, ebitda):
    res = ((((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(63).rolling(105).skew().rolling(150).mean() - (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(63).rolling(105).skew().rolling(150).mean().rolling(150).mean()) / (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(63).rolling(105).skew().rolling(150).mean().rolling(150).std()) * 0.587545).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc085_150d_jerk_v085_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc085_150d_jerk_v085_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc086_252d_jerk_v086_signal(capex, ebitda):
    res = ((ebitda.diff(2) / (capex.shift(7) + 0.4442)).rolling(105).mean().diff(200) * 0.897664).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc086_252d_jerk_v086_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc086_252d_jerk_v086_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc087_252d_jerk_v087_signal(capex, ebitda):
    res = ((capex / (ebitda + 7.5143)).rolling(10).min().rolling(200).mean() * 0.090459).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc087_252d_jerk_v087_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc087_252d_jerk_v087_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc088_21d_jerk_v088_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(252).std().pct_change(5).rolling(5).skew() * 0.487779).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc088_21d_jerk_v088_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc088_21d_jerk_v088_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc089_5d_jerk_v089_signal(ebitda, equity):
    res = ((equity / (ebitda + 2.1153)).rolling(252).mean().rolling(21).min().rolling(150).mean() * 0.418822).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc089_5d_jerk_v089_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc089_5d_jerk_v089_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc090_105d_jerk_v090_signal(assets, ebitda):
    res = ((((ebitda / (assets + 5.8032)).rolling(42).var().rolling(84).std().rolling(150).std() - (ebitda / (assets + 5.8032)).rolling(42).var().rolling(84).std().rolling(150).std().rolling(200).mean()) / (ebitda / (assets + 5.8032)).rolling(42).var().rolling(84).std().rolling(150).std().rolling(200).std()) * 0.392835).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc090_105d_jerk_v090_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc090_105d_jerk_v090_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc091_252d_jerk_v091_signal(assets, ebitda):
    res = ((ebitda.diff(18) / (assets.shift(2) + 5.5322)).diff(10).rolling(126).skew().rolling(105).std().rolling(105).skew() * 0.890463).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc091_252d_jerk_v091_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc091_252d_jerk_v091_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc092_126d_jerk_v092_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(10).kurt().rolling(21).skew() * 0.513115).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc092_126d_jerk_v092_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc092_126d_jerk_v092_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc093_84d_jerk_v093_signal(ebitda, revenue):
    res = ((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).max().pct_change(126) * 0.606085).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc093_84d_jerk_v093_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc093_84d_jerk_v093_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc094_105d_jerk_v094_signal(assets, ebitda):
    res = ((ebitda.diff(10) / (assets.shift(3) + 4.3857)).rolling(10).skew().rolling(63).max().rolling(150).kurt() * 0.617554).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc094_105d_jerk_v094_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc094_105d_jerk_v094_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc095_84d_jerk_v095_signal(ebitda, revenue):
    res = ((revenue / (ebitda + 7.2218)).rolling(10).skew().diff(105) * 0.889859).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc095_84d_jerk_v095_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc095_84d_jerk_v095_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc096_5d_jerk_v096_signal(capex, ebitda):
    res = ((capex / (ebitda + 2.3352)).rolling(63).kurt().rolling(21).var().rolling(63).var() * 0.277582).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc096_5d_jerk_v096_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc096_5d_jerk_v096_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc097_84d_jerk_v097_signal(ebitda, revenue):
    res = ((((ebitda.diff(8) / (revenue.shift(8) + 0.4417)).rolling(150).std() - (ebitda.diff(8) / (revenue.shift(8) + 0.4417)).rolling(150).std().rolling(5).mean()) / (ebitda.diff(8) / (revenue.shift(8) + 0.4417)).rolling(150).std().rolling(5).std()) * 0.929915).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc097_84d_jerk_v097_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc097_84d_jerk_v097_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc098_42d_jerk_v098_signal(ebitda, equity):
    res = ((ebitda / (equity + 6.3007)).rolling(42).var().rolling(126).mean().rolling(10).var().pct_change(84) * 0.393435).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc098_42d_jerk_v098_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc098_42d_jerk_v098_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc099_105d_jerk_v099_signal(capex, ebitda):
    res = ((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(63).var().rolling(42).min().rolling(5).mean().diff(21) * 0.252059).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc099_105d_jerk_v099_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc099_105d_jerk_v099_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc100_10d_jerk_v100_signal(ebitda, equity):
    res = (((equity / (ebitda + 6.1921)).rolling(21).skew() / (equity / (ebitda + 6.1921)).rolling(21).skew().rolling(84).max()).rolling(105).var().rolling(105).max() * 0.962743).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc100_10d_jerk_v100_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc100_10d_jerk_v100_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc101_5d_jerk_v101_signal(capex, revenue):
    res = (((revenue / (capex + 8.0185)).rolling(10).var().rolling(5).min() / (revenue / (capex + 8.0185)).rolling(10).var().rolling(5).min().rolling(42).max()) * 0.110869).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc101_5d_jerk_v101_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc101_5d_jerk_v101_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc102_105d_jerk_v102_signal(ebitda, equity):
    res = ((ebitda.diff(10) / (equity.shift(7) + 8.8892)).rolling(150).kurt().rolling(126).kurt() * 0.671986).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc102_105d_jerk_v102_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc102_105d_jerk_v102_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc103_150d_jerk_v103_signal(capex, ebitda):
    res = ((capex / (ebitda + 3.1580)).diff(252).pct_change(126) * 0.577531).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc103_150d_jerk_v103_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc103_150d_jerk_v103_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc104_150d_jerk_v104_signal(assets, ebitda):
    res = ((assets / (ebitda + 7.4265)).diff(21).diff(63) * 0.720452).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc104_150d_jerk_v104_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc104_150d_jerk_v104_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc105_126d_jerk_v105_signal(capex, ebitda):
    res = ((ebitda / (capex + 5.7244)).rolling(63).skew().rolling(84).kurt().rolling(42).var() * 0.746235).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc105_126d_jerk_v105_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc105_126d_jerk_v105_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc106_200d_jerk_v106_signal(capex, revenue):
    res = ((capex / (revenue + 8.9945)).rolling(63).skew().rolling(63).var() * 0.064339).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc106_200d_jerk_v106_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc106_200d_jerk_v106_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc107_42d_jerk_v107_signal(capex, ebitda):
    res = ((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).std().pct_change(21) * 0.715730).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc107_42d_jerk_v107_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc107_42d_jerk_v107_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc108_200d_jerk_v108_signal(capex, revenue):
    res = ((((((revenue / (capex + 7.5081)) - (revenue / (capex + 7.5081)).rolling(5).mean()) / (revenue / (capex + 7.5081)).rolling(5).std()) - (((revenue / (capex + 7.5081)) - (revenue / (capex + 7.5081)).rolling(5).mean()) / (revenue / (capex + 7.5081)).rolling(5).std()).rolling(200).mean()) / (((revenue / (capex + 7.5081)) - (revenue / (capex + 7.5081)).rolling(5).mean()) / (revenue / (capex + 7.5081)).rolling(5).std()).rolling(200).std()).diff(200) * 0.173233).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc108_200d_jerk_v108_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc108_200d_jerk_v108_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc109_63d_jerk_v109_signal(assets, ebitda):
    res = (((((assets / (ebitda + 3.0884)) / (assets / (ebitda + 3.0884)).rolling(63).max()).rolling(105).mean() - ((assets / (ebitda + 3.0884)) / (assets / (ebitda + 3.0884)).rolling(63).max()).rolling(105).mean().rolling(84).mean()) / ((assets / (ebitda + 3.0884)) / (assets / (ebitda + 3.0884)).rolling(63).max()).rolling(105).mean().rolling(84).std()) * 0.967906).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc109_63d_jerk_v109_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc109_63d_jerk_v109_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc110_42d_jerk_v110_signal(capex, ebitda):
    res = (((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).kurt() / (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).kurt().rolling(5).max()).rolling(200).kurt().rolling(10).skew() * 0.355045).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc110_42d_jerk_v110_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc110_42d_jerk_v110_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc111_21d_jerk_v111_signal(assets, capex):
    res = ((capex.diff(9) / (assets.shift(4) + 8.7051)).rolling(200).std().pct_change(200).pct_change(42).rolling(105).skew() * 0.330329).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc111_21d_jerk_v111_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc111_21d_jerk_v111_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc112_150d_jerk_v112_signal(capex, revenue):
    res = ((capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(252).var().diff(200) * 0.562451).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc112_150d_jerk_v112_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc112_150d_jerk_v112_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc113_84d_jerk_v113_signal(assets, ebitda):
    res = ((ebitda.diff(17) / (assets.shift(8) + 8.4936)).rolling(200).skew().rolling(42).std() * 0.309893).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc113_84d_jerk_v113_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc113_84d_jerk_v113_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc114_5d_jerk_v114_signal(ebitda, revenue):
    res = (((ebitda / (revenue + 9.5823)).rolling(42).skew().rolling(21).skew() / (ebitda / (revenue + 9.5823)).rolling(42).skew().rolling(21).skew().rolling(10).max()) * 0.022423).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc114_5d_jerk_v114_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc114_5d_jerk_v114_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc115_63d_jerk_v115_signal(capex, ebitda):
    res = ((capex / (ebitda + 3.6195)).rolling(126).var().rolling(5).kurt() * 0.402111).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc115_63d_jerk_v115_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc115_63d_jerk_v115_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc116_42d_jerk_v116_signal(ebitda, equity):
    res = ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).var().rolling(5).max() * 0.938118).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc116_42d_jerk_v116_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc116_42d_jerk_v116_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc117_84d_jerk_v117_signal(capex, revenue):
    res = ((((capex / (revenue + 2.8352)) - (capex / (revenue + 2.8352)).rolling(150).mean()) / (capex / (revenue + 2.8352)).rolling(150).std()).rolling(5).min().rolling(150).max() * 0.902025).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc117_84d_jerk_v117_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc117_84d_jerk_v117_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc118_150d_jerk_v118_signal(ebitda, revenue):
    res = ((((ebitda.diff(20) / (revenue.shift(1) + 5.2998)).diff(252).rolling(84).max() - (ebitda.diff(20) / (revenue.shift(1) + 5.2998)).diff(252).rolling(84).max().rolling(150).mean()) / (ebitda.diff(20) / (revenue.shift(1) + 5.2998)).diff(252).rolling(84).max().rolling(150).std()) * 0.901535).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc118_150d_jerk_v118_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc118_150d_jerk_v118_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc119_126d_jerk_v119_signal(capex, ebitda):
    res = (((ebitda / (capex + 7.6284)) / (ebitda / (capex + 7.6284)).rolling(252).max()).rolling(10).std().rolling(105).min() * 0.634717).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc119_126d_jerk_v119_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc119_126d_jerk_v119_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc120_21d_jerk_v120_signal(ebitda, equity):
    res = ((equity / (ebitda + 9.2208)).rolling(42).min().pct_change(200).diff(150) * 0.359558).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc120_21d_jerk_v120_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc120_21d_jerk_v120_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc121_21d_jerk_v121_signal(assets, ebitda):
    res = ((((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).skew() - (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).skew().rolling(21).mean()) / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).skew().rolling(21).std()) * 0.799494).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc121_21d_jerk_v121_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc121_21d_jerk_v121_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc122_105d_jerk_v122_signal(capex, ebitda):
    res = ((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(5).rolling(126).mean().diff(10).pct_change(200) * 0.078428).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc122_105d_jerk_v122_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc122_105d_jerk_v122_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc123_84d_jerk_v123_signal(assets, capex):
    res = ((assets / (capex + 2.2010)).pct_change(126).pct_change(105) * 0.095197).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc123_84d_jerk_v123_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc123_84d_jerk_v123_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc124_5d_jerk_v124_signal(ebitda, revenue):
    res = ((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).mean().rolling(42).skew().rolling(252).skew().rolling(200).kurt() * 0.127785).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc124_5d_jerk_v124_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc124_5d_jerk_v124_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc125_126d_jerk_v125_signal(capex, revenue):
    res = ((revenue / (capex + 4.3919)).rolling(105).mean().rolling(200).min().rolling(252).min() * 0.201913).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc125_126d_jerk_v125_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc125_126d_jerk_v125_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc126_126d_jerk_v126_signal(ebitda, equity):
    res = ((((equity / (ebitda + 4.7894)) / (equity / (ebitda + 4.7894)).rolling(200).max()).rolling(200).mean().rolling(63).kurt() / ((equity / (ebitda + 4.7894)) / (equity / (ebitda + 4.7894)).rolling(200).max()).rolling(200).mean().rolling(63).kurt().rolling(21).max()) * 0.308888).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc126_126d_jerk_v126_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc126_126d_jerk_v126_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc127_252d_jerk_v127_signal(capex, revenue):
    res = ((capex.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(252).rolling(84).mean() * 0.972021).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc127_252d_jerk_v127_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc127_252d_jerk_v127_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc128_10d_jerk_v128_signal(assets, ebitda):
    res = (((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84) / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84).rolling(10).max()).rolling(5).var().diff(63) * 0.667974).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc128_10d_jerk_v128_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc128_10d_jerk_v128_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc129_126d_jerk_v129_signal(assets, ebitda):
    res = ((assets / (ebitda + 2.2248)).rolling(105).min().rolling(42).max().rolling(105).kurt().diff(42) * 0.626632).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc129_126d_jerk_v129_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc129_126d_jerk_v129_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc130_252d_jerk_v130_signal(capex, revenue):
    res = ((capex.diff(12) / (revenue.shift(4) + 6.4102)).rolling(105).kurt().rolling(10).skew().rolling(150).mean() * 0.139018).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc130_252d_jerk_v130_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc130_252d_jerk_v130_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc131_150d_jerk_v131_signal(assets, ebitda):
    res = ((assets / (ebitda + 0.1573)).rolling(105).min().rolling(5).var() * 0.226510).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc131_150d_jerk_v131_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc131_150d_jerk_v131_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc132_63d_jerk_v132_signal(ebitda, revenue):
    res = (((ebitda.diff(5) / (revenue.shift(2) + 3.0213)).rolling(105).std().rolling(63).kurt() / (ebitda.diff(5) / (revenue.shift(2) + 3.0213)).rolling(105).std().rolling(63).kurt().rolling(21).max()).rolling(200).min() * 0.737445).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc132_63d_jerk_v132_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc132_63d_jerk_v132_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc133_10d_jerk_v133_signal(capex, revenue):
    res = ((revenue / (capex + 6.4916)).rolling(252).skew().rolling(63).kurt() * 0.659672).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc133_10d_jerk_v133_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc133_10d_jerk_v133_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc134_10d_jerk_v134_signal(assets, capex):
    res = ((capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(42).kurt().rolling(200).min().rolling(21).std() * 0.511956).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc134_10d_jerk_v134_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc134_10d_jerk_v134_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc135_42d_jerk_v135_signal(assets, capex):
    res = ((capex / (assets + 7.2799)).rolling(126).mean().rolling(150).min().diff(10).rolling(105).min() * 0.646241).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc135_42d_jerk_v135_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc135_42d_jerk_v135_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc136_126d_jerk_v136_signal(ebitda, equity):
    res = ((ebitda.diff(19) / (equity.shift(6) + 9.6002)).rolling(200).max().rolling(150).std().rolling(84).skew().diff(200) * 0.827966).diff(5).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc136_126d_jerk_v136_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc136_126d_jerk_v136_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc137_21d_jerk_v137_signal(assets, capex):
    res = ((assets / (capex + 3.7175)).rolling(63).var().rolling(21).std().rolling(252).mean().rolling(150).min() * 0.793852).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc137_21d_jerk_v137_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc137_21d_jerk_v137_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc138_10d_jerk_v138_signal(capex, revenue):
    res = ((revenue / (capex + 7.0482)).rolling(105).kurt().pct_change(21).rolling(21).max() * 0.007207).diff(5).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc138_10d_jerk_v138_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc138_10d_jerk_v138_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc139_21d_jerk_v139_signal(assets, ebitda):
    res = ((assets / (ebitda + 1.0393)).rolling(5).max().rolling(10).max() * 0.603379).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc139_21d_jerk_v139_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc139_21d_jerk_v139_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc140_42d_jerk_v140_signal(ebitda, equity):
    res = (((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)) / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).max()).rolling(105).kurt() * 0.427952).diff(5).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc140_42d_jerk_v140_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc140_42d_jerk_v140_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc141_150d_jerk_v141_signal(ebitda, revenue):
    res = ((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(200).diff(42) * 0.084271).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc141_150d_jerk_v141_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc141_150d_jerk_v141_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc142_63d_jerk_v142_signal(ebitda, equity):
    res = ((ebitda / (equity + 8.5415)).diff(200).diff(10) * 0.610009).diff(5).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc142_63d_jerk_v142_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc142_63d_jerk_v142_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc143_84d_jerk_v143_signal(capex, ebitda):
    res = ((ebitda / (capex + 2.8613)).rolling(200).var().rolling(200).std().rolling(42).std() * 0.586546).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc143_84d_jerk_v143_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc143_84d_jerk_v143_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc144_105d_jerk_v144_signal(capex, revenue):
    res = ((((capex.diff(15) / (revenue.shift(2) + 9.4811)).rolling(42).std() - (capex.diff(15) / (revenue.shift(2) + 9.4811)).rolling(42).std().rolling(21).mean()) / (capex.diff(15) / (revenue.shift(2) + 9.4811)).rolling(42).std().rolling(21).std()) * 0.232542).diff(5).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc144_105d_jerk_v144_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc144_105d_jerk_v144_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc145_200d_jerk_v145_signal(ebitda, revenue):
    res = ((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).max().rolling(21).skew().diff(150).diff(84) * 0.413187).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc145_200d_jerk_v145_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc145_200d_jerk_v145_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc146_252d_jerk_v146_signal(ebitda, equity):
    res = (((ebitda / (equity + 8.2773)) / (ebitda / (equity + 8.2773)).rolling(21).max()).rolling(252).var() * 0.765635).diff(5).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc146_252d_jerk_v146_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc146_252d_jerk_v146_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc147_5d_jerk_v147_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 6.1541)).rolling(21).kurt() - (ebitda / (revenue + 6.1541)).rolling(21).kurt().rolling(105).mean()) / (ebitda / (revenue + 6.1541)).rolling(21).kurt().rolling(105).std()) * 0.994372).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc147_5d_jerk_v147_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc147_5d_jerk_v147_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc148_21d_jerk_v148_signal(ebitda, equity):
    res = ((equity / (ebitda + 0.3393)).rolling(5).max().rolling(105).kurt().rolling(252).kurt() * 0.502462).diff(5).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc148_21d_jerk_v148_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc148_21d_jerk_v148_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc149_200d_jerk_v149_signal(assets, ebitda):
    res = ((((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)) - (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).mean()) / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).std()).rolling(10).max() * 0.600844).diff(5).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc149_200d_jerk_v149_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc149_200d_jerk_v149_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc150_5d_jerk_v150_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(150).kurt().rolling(150).max() * 0.856302).diff(5).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc150_5d_jerk_v150_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc150_5d_jerk_v150_signal


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
