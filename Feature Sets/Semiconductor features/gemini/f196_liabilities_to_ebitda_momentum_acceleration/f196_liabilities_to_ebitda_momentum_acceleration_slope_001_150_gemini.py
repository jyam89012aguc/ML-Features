import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc001_63d_slope_v001_signal(liabilities, revenue):
    res = ((liabilities.diff(10) / (revenue.shift(8) + 7.1856)).rolling(10).std().rolling(126).kurt() * 0.995954).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc001_63d_slope_v001_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc001_63d_slope_v001_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc002_126d_slope_v002_signal(liabilities, revenue):
    res = ((((liabilities / (revenue + 5.7965)).pct_change(200) - (liabilities / (revenue + 5.7965)).pct_change(200).rolling(150).mean()) / (liabilities / (revenue + 5.7965)).pct_change(200).rolling(150).std()).pct_change(105) * 0.285484).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc002_126d_slope_v002_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc002_126d_slope_v002_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc003_10d_slope_v003_signal(liabilities, revenue):
    res = ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(200).skew().diff(63) * 0.967447).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc003_10d_slope_v003_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc003_10d_slope_v003_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc004_200d_slope_v004_signal(debt, revenue):
    res = (((debt.diff(7) / (revenue.shift(9) + 2.2184)).rolling(10).mean() / (debt.diff(7) / (revenue.shift(9) + 2.2184)).rolling(10).mean().rolling(126).max()) * 0.789787).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc004_200d_slope_v004_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc004_200d_slope_v004_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc005_84d_slope_v005_signal(debt, revenue):
    res = ((((debt / (revenue + 6.7818)) - (debt / (revenue + 6.7818)).rolling(63).mean()) / (debt / (revenue + 6.7818)).rolling(63).std()).rolling(42).mean().rolling(21).var() * 0.270166).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc005_84d_slope_v005_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc005_84d_slope_v005_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc006_200d_slope_v006_signal(debt, revenue):
    res = (((((revenue / (debt + 0.7808)).rolling(200).mean() - (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).mean()) / (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).std()) / (((revenue / (debt + 0.7808)).rolling(200).mean() - (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).mean()) / (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).std()).rolling(5).max()).rolling(200).var() * 0.291781).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc006_200d_slope_v006_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc006_200d_slope_v006_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc007_63d_slope_v007_signal(equity, liabilities):
    res = (((liabilities.diff(3) / (equity.shift(4) + 1.6990)) / (liabilities.diff(3) / (equity.shift(4) + 1.6990)).rolling(84).max()).rolling(200).mean().rolling(42).kurt() * 0.689175).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc007_63d_slope_v007_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc007_63d_slope_v007_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc008_84d_slope_v008_signal(equity, liabilities):
    res = ((equity / (liabilities + 2.5082)).rolling(126).max().rolling(126).std().rolling(10).min() * 0.339696).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc008_84d_slope_v008_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc008_84d_slope_v008_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc009_63d_slope_v009_signal(assets, liabilities):
    res = ((assets / (liabilities + 7.2429)).diff(126).rolling(10).mean() * 0.938994).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc009_63d_slope_v009_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc009_63d_slope_v009_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc010_42d_slope_v010_signal(assets, liabilities):
    res = (((liabilities / (assets + 4.9352)).rolling(84).max().rolling(150).skew().rolling(105).std() / (liabilities / (assets + 4.9352)).rolling(84).max().rolling(150).skew().rolling(105).std().rolling(10).max()) * 0.478842).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc010_42d_slope_v010_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc010_42d_slope_v010_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc011_105d_slope_v011_signal(assets, liabilities):
    res = ((liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).diff(5).rolling(42).var().rolling(150).var().pct_change(105) * 0.263599).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc011_105d_slope_v011_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc011_105d_slope_v011_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc012_150d_slope_v012_signal(debt, ebitda):
    res = ((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(42).max()) / ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(42).max()).rolling(126).max()).rolling(63).skew().rolling(63).max() * 0.603562).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc012_150d_slope_v012_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc012_150d_slope_v012_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc013_252d_slope_v013_signal(assets, liabilities):
    res = ((liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).max().rolling(126).var().rolling(63).max() * 0.273596).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc013_252d_slope_v013_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc013_252d_slope_v013_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc014_150d_slope_v014_signal(liabilities, revenue):
    res = ((((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(150).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(150).std()).rolling(126).max().diff(252) * 0.801824).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc014_150d_slope_v014_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc014_150d_slope_v014_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc015_200d_slope_v015_signal(debt, ebitda):
    res = ((debt.diff(12) / (ebitda.shift(9) + 8.7766)).rolling(42).var().pct_change(42).diff(21).rolling(10).mean() * 0.966867).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc015_200d_slope_v015_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc015_200d_slope_v015_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc016_84d_slope_v016_signal(ebitda, liabilities):
    res = ((liabilities.diff(16) / (ebitda.shift(3) + 5.8419)).rolling(5).mean().rolling(5).std() * 0.050927).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc016_84d_slope_v016_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc016_84d_slope_v016_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc017_5d_slope_v017_signal(debt, revenue):
    res = ((debt / (revenue + 3.6605)).rolling(21).std().pct_change(21) * 0.839421).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc017_5d_slope_v017_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc017_5d_slope_v017_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc018_126d_slope_v018_signal(equity, liabilities):
    res = ((((equity / (liabilities + 1.9729)).rolling(84).mean() - (equity / (liabilities + 1.9729)).rolling(84).mean().rolling(42).mean()) / (equity / (liabilities + 1.9729)).rolling(84).mean().rolling(42).std()).rolling(42).min() * 0.490370).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc018_126d_slope_v018_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc018_126d_slope_v018_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc019_42d_slope_v019_signal(ebitda, liabilities):
    res = ((((liabilities.diff(4) / (ebitda.shift(9) + 1.6615)) - (liabilities.diff(4) / (ebitda.shift(9) + 1.6615)).rolling(10).mean()) / (liabilities.diff(4) / (ebitda.shift(9) + 1.6615)).rolling(10).std()).rolling(252).skew().rolling(126).mean().pct_change(252) * 0.851595).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc019_42d_slope_v019_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc019_42d_slope_v019_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc020_63d_slope_v020_signal(assets, liabilities):
    res = ((((assets / (liabilities + 7.4710)) - (assets / (liabilities + 7.4710)).rolling(252).mean()) / (assets / (liabilities + 7.4710)).rolling(252).std()).rolling(63).max() * 0.543648).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc020_63d_slope_v020_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc020_63d_slope_v020_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc021_21d_slope_v021_signal(equity, liabilities):
    res = (((liabilities.diff(16) / (equity.shift(9) + 0.7550)).rolling(150).min().rolling(21).max() / (liabilities.diff(16) / (equity.shift(9) + 0.7550)).rolling(150).min().rolling(21).max().rolling(252).max()).rolling(63).max() * 0.597976).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc021_21d_slope_v021_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc021_21d_slope_v021_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc022_5d_slope_v022_signal(ebitda, liabilities):
    res = ((liabilities / (ebitda + 7.6365)).rolling(84).skew().pct_change(126) * 0.654701).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc022_5d_slope_v022_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc022_5d_slope_v022_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc023_126d_slope_v023_signal(debt, revenue):
    res = ((debt.diff(11) / (revenue.shift(9) + 2.5660)).rolling(63).skew().pct_change(150) * 0.543115).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc023_126d_slope_v023_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc023_126d_slope_v023_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc024_5d_slope_v024_signal(liabilities, revenue):
    res = (((((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).max()).rolling(252).var() - ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).max()).rolling(252).var().rolling(252).mean()) / ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).max()).rolling(252).var().rolling(252).std()) * 0.793401).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc024_5d_slope_v024_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc024_5d_slope_v024_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc025_63d_slope_v025_signal(debt, ebitda):
    res = ((((debt / (ebitda + 5.7071)) - (debt / (ebitda + 5.7071)).rolling(42).mean()) / (debt / (ebitda + 5.7071)).rolling(42).std()).diff(252).rolling(84).mean() * 0.459032).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc025_63d_slope_v025_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc025_63d_slope_v025_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc026_200d_slope_v026_signal(debt, ebitda):
    res = (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(150).var().rolling(126).min().rolling(150).kurt() * 0.016991).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc026_200d_slope_v026_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc026_200d_slope_v026_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc027_126d_slope_v027_signal(debt, revenue):
    res = ((((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(21) - (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(21).rolling(5).mean()) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(21).rolling(5).std()).rolling(126).var().rolling(126).std() * 0.061612).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc027_126d_slope_v027_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc027_126d_slope_v027_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc028_200d_slope_v028_signal(equity, liabilities):
    res = (((liabilities.diff(3) / (equity.shift(4) + 4.3470)) / (liabilities.diff(3) / (equity.shift(4) + 4.3470)).rolling(105).max()).rolling(5).min() * 0.586210).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc028_200d_slope_v028_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc028_200d_slope_v028_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc029_42d_slope_v029_signal(debt, revenue):
    res = ((((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max()).rolling(126).max() / ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max()).rolling(126).max().rolling(252).max()).rolling(10).min() * 0.324097).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc029_42d_slope_v029_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc029_42d_slope_v029_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc030_252d_slope_v030_signal(debt, revenue):
    res = ((revenue / (debt + 4.2314)).rolling(150).max().diff(63).rolling(63).min() * 0.752577).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc030_252d_slope_v030_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc030_252d_slope_v030_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc031_10d_slope_v031_signal(debt, ebitda):
    res = (((debt.diff(2) / (ebitda.shift(3) + 2.5015)) / (debt.diff(2) / (ebitda.shift(3) + 2.5015)).rolling(105).max()).diff(84) * 0.372139).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc031_10d_slope_v031_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc031_10d_slope_v031_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc032_84d_slope_v032_signal(liabilities, revenue):
    res = ((revenue / (liabilities + 9.8095)).rolling(42).max().rolling(5).max() * 0.030203).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc032_84d_slope_v032_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc032_84d_slope_v032_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc033_63d_slope_v033_signal(debt, ebitda):
    res = ((debt.diff(12) / (ebitda.shift(3) + 2.4490)).pct_change(150).rolling(252).kurt().rolling(42).min() * 0.482055).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc033_63d_slope_v033_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc033_63d_slope_v033_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc034_105d_slope_v034_signal(debt, revenue):
    res = ((((debt.diff(14) / (revenue.shift(7) + 4.7960)) / (debt.diff(14) / (revenue.shift(7) + 4.7960)).rolling(200).max()).diff(21) / ((debt.diff(14) / (revenue.shift(7) + 4.7960)) / (debt.diff(14) / (revenue.shift(7) + 4.7960)).rolling(200).max()).diff(21).rolling(42).max()) * 0.523756).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc034_105d_slope_v034_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc034_105d_slope_v034_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc035_200d_slope_v035_signal(assets, liabilities):
    res = ((liabilities / (assets + 6.0263)).rolling(63).mean().rolling(21).var() * 0.776841).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc035_200d_slope_v035_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc035_200d_slope_v035_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc036_21d_slope_v036_signal(ebitda, liabilities):
    res = ((liabilities.diff(19) / (ebitda.shift(7) + 3.1991)).pct_change(84).pct_change(84) * 0.157506).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc036_21d_slope_v036_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc036_21d_slope_v036_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc037_126d_slope_v037_signal(assets, liabilities):
    res = ((((assets / (liabilities + 6.6208)).rolling(21).std() - (assets / (liabilities + 6.6208)).rolling(21).std().rolling(5).mean()) / (assets / (liabilities + 6.6208)).rolling(21).std().rolling(5).std()).rolling(84).min() * 0.365839).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc037_126d_slope_v037_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc037_126d_slope_v037_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc038_252d_slope_v038_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 6.9274)).rolling(63).max().rolling(21).max().pct_change(63) * 0.925118).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc038_252d_slope_v038_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc038_252d_slope_v038_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc039_21d_slope_v039_signal(liabilities, revenue):
    res = (((liabilities.diff(19) / (revenue.shift(8) + 6.4873)).pct_change(42).rolling(200).max().diff(200) / (liabilities.diff(19) / (revenue.shift(8) + 6.4873)).pct_change(42).rolling(200).max().diff(200).rolling(21).max()) * 0.578699).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc039_21d_slope_v039_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc039_21d_slope_v039_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc040_10d_slope_v040_signal(debt, ebitda):
    res = (((debt.diff(14) / (ebitda.shift(1) + 0.7321)).rolling(105).skew() / (debt.diff(14) / (ebitda.shift(1) + 0.7321)).rolling(105).skew().rolling(105).max()).pct_change(150) * 0.413120).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc040_10d_slope_v040_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc040_10d_slope_v040_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc041_63d_slope_v041_signal(liabilities, revenue):
    res = (((revenue / (liabilities + 2.2865)).rolling(150).min().rolling(105).std() / (revenue / (liabilities + 2.2865)).rolling(150).min().rolling(105).std().rolling(42).max()) * 0.935853).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc041_63d_slope_v041_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc041_63d_slope_v041_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc042_21d_slope_v042_signal(debt, ebitda):
    res = ((debt / (ebitda + 5.0630)).rolling(5).var().rolling(150).min() * 0.410947).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc042_21d_slope_v042_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc042_21d_slope_v042_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc043_42d_slope_v043_signal(debt, revenue):
    res = (((revenue / (debt + 8.6283)) / (revenue / (debt + 8.6283)).rolling(105).max()).rolling(5).kurt().rolling(200).var() * 0.291937).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc043_42d_slope_v043_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc043_42d_slope_v043_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc044_84d_slope_v044_signal(debt, revenue):
    res = ((debt.diff(11) / (revenue.shift(3) + 4.5993)).rolling(42).max().rolling(10).skew().rolling(10).min() * 0.847264).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc044_84d_slope_v044_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc044_84d_slope_v044_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc045_200d_slope_v045_signal(debt, revenue):
    res = ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).min().pct_change(10) * 0.860737).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc045_200d_slope_v045_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc045_200d_slope_v045_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc046_84d_slope_v046_signal(debt, ebitda):
    res = ((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).std()).rolling(21).skew().pct_change(200).diff(10) * 0.754355).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc046_84d_slope_v046_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc046_84d_slope_v046_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc047_252d_slope_v047_signal(equity, liabilities):
    res = ((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(63).min().rolling(84).kurt().rolling(105).var().diff(21) * 0.975273).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc047_252d_slope_v047_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc047_252d_slope_v047_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc048_63d_slope_v048_signal(equity, liabilities):
    res = ((liabilities / (equity + 2.0965)).rolling(126).var().rolling(84).mean() * 0.955021).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc048_63d_slope_v048_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc048_63d_slope_v048_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc049_84d_slope_v049_signal(ebitda, liabilities):
    res = (((ebitda / (liabilities + 3.2150)).pct_change(10) / (ebitda / (liabilities + 3.2150)).pct_change(10).rolling(42).max()) * 0.929741).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc049_84d_slope_v049_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc049_84d_slope_v049_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc050_5d_slope_v050_signal(debt, revenue):
    res = ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).min().rolling(42).mean().rolling(5).mean().rolling(105).std() * 0.253153).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc050_5d_slope_v050_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc050_5d_slope_v050_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc051_10d_slope_v051_signal(liabilities, revenue):
    res = ((((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).std()).rolling(10).kurt() * 0.719800).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc051_10d_slope_v051_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc051_10d_slope_v051_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc052_42d_slope_v052_signal(debt, ebitda):
    res = (((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(42).mean() - ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(42).mean().rolling(84).mean()) / ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(42).mean().rolling(84).std()) * 0.972331).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc052_42d_slope_v052_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc052_42d_slope_v052_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc053_63d_slope_v053_signal(debt, revenue):
    res = ((debt.diff(10) / (revenue.shift(3) + 9.2842)).rolling(105).var().rolling(10).var().rolling(252).max().pct_change(150) * 0.909748).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc053_63d_slope_v053_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc053_63d_slope_v053_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc054_200d_slope_v054_signal(ebitda, liabilities):
    res = (((ebitda / (liabilities + 4.5272)).rolling(150).max() / (ebitda / (liabilities + 4.5272)).rolling(150).max().rolling(10).max()).pct_change(252).rolling(150).std() * 0.478903).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc054_200d_slope_v054_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc054_200d_slope_v054_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc055_252d_slope_v055_signal(equity, liabilities):
    res = ((liabilities / (equity + 8.7182)).rolling(105).var().pct_change(150) * 0.750995).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc055_252d_slope_v055_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc055_252d_slope_v055_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc056_252d_slope_v056_signal(assets, liabilities):
    res = ((((liabilities / (assets + 4.8074)).rolling(105).max() - (liabilities / (assets + 4.8074)).rolling(105).max().rolling(252).mean()) / (liabilities / (assets + 4.8074)).rolling(105).max().rolling(252).std()).rolling(21).var() * 0.962400).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc056_252d_slope_v056_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc056_252d_slope_v056_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc057_105d_slope_v057_signal(equity, liabilities):
    res = ((equity / (liabilities + 3.3494)).rolling(126).std().rolling(252).var() * 0.410141).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc057_105d_slope_v057_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc057_105d_slope_v057_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc058_63d_slope_v058_signal(ebitda, liabilities):
    res = ((((liabilities / (ebitda + 6.0419)).rolling(84).max() - (liabilities / (ebitda + 6.0419)).rolling(84).max().rolling(63).mean()) / (liabilities / (ebitda + 6.0419)).rolling(84).max().rolling(63).std()) * 0.425829).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc058_63d_slope_v058_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc058_63d_slope_v058_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc059_84d_slope_v059_signal(liabilities, revenue):
    res = ((((revenue / (liabilities + 3.5369)) - (revenue / (liabilities + 3.5369)).rolling(200).mean()) / (revenue / (liabilities + 3.5369)).rolling(200).std()).rolling(150).kurt() * 0.024705).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc059_84d_slope_v059_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc059_84d_slope_v059_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc060_84d_slope_v060_signal(assets, liabilities):
    res = ((liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84).pct_change(105).rolling(126).skew().rolling(42).min() * 0.289332).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc060_84d_slope_v060_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc060_84d_slope_v060_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc061_42d_slope_v061_signal(liabilities, revenue):
    res = ((((((liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min() - (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).mean()) / (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).std()) - (((liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min() - (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).mean()) / (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).std()).rolling(150).mean()) / (((liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min() - (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).mean()) / (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).std()).rolling(150).std()).rolling(126).skew() * 0.713648).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc061_42d_slope_v061_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc061_42d_slope_v061_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc062_10d_slope_v062_signal(debt, revenue):
    res = ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(105).skew().diff(84).rolling(200).skew().rolling(150).skew() * 0.794165).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc062_10d_slope_v062_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc062_10d_slope_v062_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc063_63d_slope_v063_signal(assets, liabilities):
    res = ((liabilities / (assets + 5.3000)).diff(126).rolling(200).skew().rolling(200).std() * 0.603125).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc063_63d_slope_v063_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc063_63d_slope_v063_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc064_200d_slope_v064_signal(liabilities, revenue):
    res = ((revenue / (liabilities + 4.1267)).pct_change(126).diff(63).rolling(10).mean().rolling(105).var() * 0.741176).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc064_200d_slope_v064_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc064_200d_slope_v064_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc065_10d_slope_v065_signal(assets, liabilities):
    res = ((((liabilities.diff(6) / (assets.shift(10) + 1.1292)).rolling(126).kurt() - (liabilities.diff(6) / (assets.shift(10) + 1.1292)).rolling(126).kurt().rolling(63).mean()) / (liabilities.diff(6) / (assets.shift(10) + 1.1292)).rolling(126).kurt().rolling(63).std()) * 0.612730).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc065_10d_slope_v065_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc065_10d_slope_v065_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc066_150d_slope_v066_signal(liabilities, revenue):
    res = ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(105).skew().diff(84).rolling(5).var().rolling(150).mean() * 0.225362).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc066_150d_slope_v066_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc066_150d_slope_v066_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc067_21d_slope_v067_signal(equity, liabilities):
    res = ((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(5).min().rolling(150).var().diff(21) * 0.690948).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc067_21d_slope_v067_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc067_21d_slope_v067_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc068_105d_slope_v068_signal(debt, revenue):
    res = ((((revenue / (debt + 5.0791)) - (revenue / (debt + 5.0791)).rolling(84).mean()) / (revenue / (debt + 5.0791)).rolling(84).std()).pct_change(42) * 0.073925).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc068_105d_slope_v068_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc068_105d_slope_v068_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc069_84d_slope_v069_signal(debt, ebitda):
    res = ((((debt.diff(11) / (ebitda.shift(3) + 1.4350)).rolling(5).min() - (debt.diff(11) / (ebitda.shift(3) + 1.4350)).rolling(5).min().rolling(126).mean()) / (debt.diff(11) / (ebitda.shift(3) + 1.4350)).rolling(5).min().rolling(126).std()) * 0.795476).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc069_84d_slope_v069_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc069_84d_slope_v069_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc070_105d_slope_v070_signal(assets, liabilities):
    res = ((assets / (liabilities + 1.7263)).rolling(5).min().rolling(84).var() * 0.477895).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc070_105d_slope_v070_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc070_105d_slope_v070_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc071_84d_slope_v071_signal(debt, ebitda):
    res = ((((ebitda / (debt + 4.9943)) - (ebitda / (debt + 4.9943)).rolling(42).mean()) / (ebitda / (debt + 4.9943)).rolling(42).std()).pct_change(150) * 0.183751).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc071_84d_slope_v071_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc071_84d_slope_v071_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc072_63d_slope_v072_signal(ebitda, liabilities):
    res = ((((ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var() / (ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var().rolling(252).max()) / ((ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var() / (ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var().rolling(252).max()).rolling(84).max()) * 0.686253).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc072_63d_slope_v072_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc072_63d_slope_v072_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc073_5d_slope_v073_signal(ebitda, liabilities):
    res = ((((((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).std()).diff(200) - (((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).std()).diff(200).rolling(63).mean()) / (((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).std()).diff(200).rolling(63).std()) * 0.611179).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc073_5d_slope_v073_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc073_5d_slope_v073_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc074_252d_slope_v074_signal(equity, liabilities):
    res = ((((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).min().diff(21) - (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).min().diff(21).rolling(150).mean()) / (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).min().diff(21).rolling(150).std()).rolling(150).kurt() * 0.528369).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc074_252d_slope_v074_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc074_252d_slope_v074_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc075_252d_slope_v075_signal(liabilities, revenue):
    res = (((((revenue / (liabilities + 9.3859)).rolling(84).mean() - (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).mean()) / (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).std()) / (((revenue / (liabilities + 9.3859)).rolling(84).mean() - (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).mean()) / (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).std()).rolling(252).max()) * 0.127717).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc075_252d_slope_v075_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc075_252d_slope_v075_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc076_10d_slope_v076_signal(ebitda, liabilities):
    res = (((liabilities / (ebitda + 7.4201)) / (liabilities / (ebitda + 7.4201)).rolling(10).max()).pct_change(150).rolling(5).mean() * 0.742833).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc076_10d_slope_v076_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc076_10d_slope_v076_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc077_150d_slope_v077_signal(debt, ebitda):
    res = ((debt.diff(8) / (ebitda.shift(3) + 1.5170)).rolling(84).var().diff(5) * 0.727933).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc077_150d_slope_v077_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc077_150d_slope_v077_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc078_21d_slope_v078_signal(debt, ebitda):
    res = ((ebitda / (debt + 8.7738)).rolling(42).mean().rolling(84).kurt().pct_change(10) * 0.462655).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc078_21d_slope_v078_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc078_21d_slope_v078_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc079_200d_slope_v079_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 8.5366)).diff(10).rolling(105).max().rolling(252).std().rolling(21).min() * 0.187151).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc079_200d_slope_v079_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc079_200d_slope_v079_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc080_150d_slope_v080_signal(debt, revenue):
    res = ((debt.diff(15) / (revenue.shift(9) + 2.6615)).rolling(84).kurt().pct_change(5) * 0.530839).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc080_150d_slope_v080_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc080_150d_slope_v080_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc081_42d_slope_v081_signal(debt, revenue):
    res = ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).skew().rolling(105).kurt() * 0.891718).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc081_42d_slope_v081_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc081_42d_slope_v081_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc082_21d_slope_v082_signal(assets, liabilities):
    res = (((liabilities / (assets + 8.1130)).diff(42).rolling(105).max() / (liabilities / (assets + 8.1130)).diff(42).rolling(105).max().rolling(105).max()).pct_change(5) * 0.751155).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc082_21d_slope_v082_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc082_21d_slope_v082_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc083_21d_slope_v083_signal(ebitda, liabilities):
    res = ((((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(84) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(84).rolling(42).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(84).rolling(42).std()).rolling(5).var() * 0.792834).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc083_21d_slope_v083_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc083_21d_slope_v083_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc084_10d_slope_v084_signal(equity, liabilities):
    res = ((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).skew().pct_change(150) * 0.897746).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc084_10d_slope_v084_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc084_10d_slope_v084_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc085_150d_slope_v085_signal(debt, ebitda):
    res = ((ebitda / (debt + 9.3708)).pct_change(252).rolling(84).var() * 0.928231).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc085_150d_slope_v085_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc085_150d_slope_v085_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc086_10d_slope_v086_signal(debt, ebitda):
    res = ((ebitda / (debt + 3.5564)).rolling(150).var().rolling(42).std() * 0.897260).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc086_10d_slope_v086_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc086_10d_slope_v086_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc087_150d_slope_v087_signal(debt, revenue):
    res = ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).std().pct_change(10) * 0.762009).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc087_150d_slope_v087_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc087_150d_slope_v087_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc088_10d_slope_v088_signal(ebitda, liabilities):
    res = ((liabilities / (ebitda + 4.0725)).diff(63).pct_change(252) * 0.475624).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc088_10d_slope_v088_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc088_10d_slope_v088_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc089_21d_slope_v089_signal(liabilities, revenue):
    res = ((liabilities / (revenue + 8.2231)).rolling(10).var().rolling(126).std() * 0.310104).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc089_21d_slope_v089_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc089_21d_slope_v089_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc090_84d_slope_v090_signal(ebitda, liabilities):
    res = ((((((liabilities / (ebitda + 4.3629)) - (liabilities / (ebitda + 4.3629)).rolling(252).mean()) / (liabilities / (ebitda + 4.3629)).rolling(252).std()) - (((liabilities / (ebitda + 4.3629)) - (liabilities / (ebitda + 4.3629)).rolling(252).mean()) / (liabilities / (ebitda + 4.3629)).rolling(252).std()).rolling(63).mean()) / (((liabilities / (ebitda + 4.3629)) - (liabilities / (ebitda + 4.3629)).rolling(252).mean()) / (liabilities / (ebitda + 4.3629)).rolling(252).std()).rolling(63).std()) * 0.629719).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc090_84d_slope_v090_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc090_84d_slope_v090_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc091_63d_slope_v091_signal(debt, ebitda):
    res = ((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).std().pct_change(105).rolling(105).kurt() - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).std().pct_change(105).rolling(105).kurt().rolling(252).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).std().pct_change(105).rolling(105).kurt().rolling(252).std()) * 0.226447).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc091_63d_slope_v091_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc091_63d_slope_v091_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc092_84d_slope_v092_signal(debt, revenue):
    res = ((((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) - (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).mean()) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).std()).rolling(42).std() * 0.840482).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc092_84d_slope_v092_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc092_84d_slope_v092_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc093_105d_slope_v093_signal(equity, liabilities):
    res = ((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(42).min().rolling(21).std().rolling(200).std() * 0.035551).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc093_105d_slope_v093_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc093_105d_slope_v093_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc094_42d_slope_v094_signal(liabilities, revenue):
    res = ((((revenue / (liabilities + 7.6366)).rolling(63).std() - (revenue / (liabilities + 7.6366)).rolling(63).std().rolling(21).mean()) / (revenue / (liabilities + 7.6366)).rolling(63).std().rolling(21).std()).rolling(5).var() * 0.476063).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc094_42d_slope_v094_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc094_42d_slope_v094_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc095_150d_slope_v095_signal(assets, liabilities):
    res = ((liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).min().rolling(21).kurt().rolling(63).var() * 0.558459).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc095_150d_slope_v095_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc095_150d_slope_v095_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc096_200d_slope_v096_signal(assets, liabilities):
    res = ((liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).std().rolling(84).skew() * 0.474606).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc096_200d_slope_v096_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc096_200d_slope_v096_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc097_63d_slope_v097_signal(debt, ebitda):
    res = ((((debt / (ebitda + 5.1841)) - (debt / (ebitda + 5.1841)).rolling(5).mean()) / (debt / (ebitda + 5.1841)).rolling(5).std()).rolling(126).var().rolling(200).skew().rolling(63).kurt() * 0.798745).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc097_63d_slope_v097_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc097_63d_slope_v097_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc098_105d_slope_v098_signal(debt, revenue):
    res = ((((debt / (revenue + 8.9380)).pct_change(105).rolling(252).mean().rolling(10).kurt() - (debt / (revenue + 8.9380)).pct_change(105).rolling(252).mean().rolling(10).kurt().rolling(21).mean()) / (debt / (revenue + 8.9380)).pct_change(105).rolling(252).mean().rolling(10).kurt().rolling(21).std()) * 0.161686).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc098_105d_slope_v098_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc098_105d_slope_v098_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc099_105d_slope_v099_signal(debt, ebitda):
    res = ((ebitda / (debt + 5.3597)).rolling(5).min().pct_change(105).rolling(150).kurt().rolling(21).skew() * 0.347775).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc099_105d_slope_v099_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc099_105d_slope_v099_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc100_63d_slope_v100_signal(liabilities, revenue):
    res = ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).std().rolling(84).max().rolling(126).var().rolling(42).skew() * 0.781441).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc100_63d_slope_v100_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc100_63d_slope_v100_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc101_150d_slope_v101_signal(liabilities, revenue):
    res = ((((liabilities / (revenue + 3.1569)).rolling(84).skew() - (liabilities / (revenue + 3.1569)).rolling(84).skew().rolling(200).mean()) / (liabilities / (revenue + 3.1569)).rolling(84).skew().rolling(200).std()).rolling(252).var().rolling(10).min() * 0.017291).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc101_150d_slope_v101_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc101_150d_slope_v101_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc102_42d_slope_v102_signal(ebitda, liabilities):
    res = (((liabilities.diff(15) / (ebitda.shift(10) + 4.6667)) / (liabilities.diff(15) / (ebitda.shift(10) + 4.6667)).rolling(126).max()).rolling(150).kurt().rolling(150).skew() * 0.466532).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc102_42d_slope_v102_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc102_42d_slope_v102_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc103_126d_slope_v103_signal(assets, liabilities):
    res = ((((liabilities / (assets + 9.8978)).rolling(84).min().rolling(200).skew() - (liabilities / (assets + 9.8978)).rolling(84).min().rolling(200).skew().rolling(105).mean()) / (liabilities / (assets + 9.8978)).rolling(84).min().rolling(200).skew().rolling(105).std()).diff(10) * 0.383565).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc103_126d_slope_v103_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc103_126d_slope_v103_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc104_105d_slope_v104_signal(ebitda, liabilities):
    res = ((((liabilities / (ebitda + 0.6226)).rolling(21).var().rolling(126).min() - (liabilities / (ebitda + 0.6226)).rolling(21).var().rolling(126).min().rolling(63).mean()) / (liabilities / (ebitda + 0.6226)).rolling(21).var().rolling(126).min().rolling(63).std()) * 0.755114).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc104_105d_slope_v104_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc104_105d_slope_v104_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc105_63d_slope_v105_signal(debt, ebitda):
    res = ((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean().rolling(10).min().rolling(84).max() - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean().rolling(10).min().rolling(84).max().rolling(200).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean().rolling(10).min().rolling(84).max().rolling(200).std()) * 0.442258).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc105_63d_slope_v105_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc105_63d_slope_v105_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc106_126d_slope_v106_signal(liabilities, revenue):
    res = (((liabilities / (revenue + 1.6407)) / (liabilities / (revenue + 1.6407)).rolling(252).max()).rolling(105).kurt() * 0.676270).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc106_126d_slope_v106_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc106_126d_slope_v106_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc107_5d_slope_v107_signal(debt, revenue):
    res = (((debt / (revenue + 9.8966)).rolling(63).kurt().diff(105) / (debt / (revenue + 9.8966)).rolling(63).kurt().diff(105).rolling(42).max()) * 0.224346).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc107_5d_slope_v107_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc107_5d_slope_v107_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc108_21d_slope_v108_signal(debt, revenue):
    res = ((revenue / (debt + 0.1757)).diff(252).pct_change(252).pct_change(10).rolling(21).std() * 0.323571).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc108_21d_slope_v108_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc108_21d_slope_v108_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc109_10d_slope_v109_signal(ebitda, liabilities):
    res = ((liabilities.diff(10) / (ebitda.shift(1) + 8.6531)).rolling(126).mean().rolling(42).mean().diff(200).rolling(126).var() * 0.921852).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc109_10d_slope_v109_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc109_10d_slope_v109_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc110_63d_slope_v110_signal(debt, revenue):
    res = ((debt.diff(13) / (revenue.shift(10) + 0.3304)).pct_change(126).rolling(21).min().rolling(126).skew().diff(84) * 0.361596).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc110_63d_slope_v110_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc110_63d_slope_v110_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc111_21d_slope_v111_signal(debt, ebitda):
    res = ((ebitda / (debt + 5.3798)).rolling(5).kurt().rolling(126).std().rolling(21).std() * 0.720343).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc111_21d_slope_v111_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc111_21d_slope_v111_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc112_84d_slope_v112_signal(liabilities, revenue):
    res = ((revenue / (liabilities + 8.5047)).rolling(10).min().rolling(84).var().rolling(105).mean().pct_change(63) * 0.350583).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc112_84d_slope_v112_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc112_84d_slope_v112_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc113_10d_slope_v113_signal(assets, liabilities):
    res = ((assets / (liabilities + 9.1024)).rolling(42).var().rolling(63).std() * 0.493172).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc113_10d_slope_v113_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc113_10d_slope_v113_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc114_150d_slope_v114_signal(equity, liabilities):
    res = ((equity / (liabilities + 5.5284)).diff(252).rolling(84).min().diff(5).diff(252) * 0.794687).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc114_150d_slope_v114_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc114_150d_slope_v114_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc115_5d_slope_v115_signal(debt, ebitda):
    res = ((((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std()).rolling(200).skew() - (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std()).rolling(200).skew().rolling(105).mean()) / (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std()).rolling(200).skew().rolling(105).std()).diff(10) * 0.036707).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc115_5d_slope_v115_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc115_5d_slope_v115_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc116_21d_slope_v116_signal(debt, revenue):
    res = ((debt.diff(20) / (revenue.shift(1) + 1.5051)).diff(84).rolling(5).var().rolling(150).kurt().rolling(5).var() * 0.077642).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc116_21d_slope_v116_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc116_21d_slope_v116_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc117_21d_slope_v117_signal(assets, liabilities):
    res = ((liabilities / (assets + 0.2676)).rolling(126).max().pct_change(150).rolling(200).mean() * 0.904476).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc117_21d_slope_v117_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc117_21d_slope_v117_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc118_21d_slope_v118_signal(debt, revenue):
    res = ((debt / (revenue + 0.5800)).rolling(252).skew().pct_change(84) * 0.859263).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc118_21d_slope_v118_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc118_21d_slope_v118_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc119_21d_slope_v119_signal(debt, revenue):
    res = ((revenue / (debt + 0.4452)).rolling(200).std().rolling(200).min().pct_change(200) * 0.083034).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc119_21d_slope_v119_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc119_21d_slope_v119_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc120_63d_slope_v120_signal(debt, ebitda):
    res = ((debt.diff(2) / (ebitda.shift(1) + 4.9124)).rolling(5).skew().rolling(21).kurt() * 0.421453).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc120_63d_slope_v120_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc120_63d_slope_v120_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc121_21d_slope_v121_signal(liabilities, revenue):
    res = ((((((liabilities.diff(9) / (revenue.shift(7) + 6.5306)) - (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).mean()) / (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).std()) - (((liabilities.diff(9) / (revenue.shift(7) + 6.5306)) - (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).mean()) / (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).std()).rolling(63).mean()) / (((liabilities.diff(9) / (revenue.shift(7) + 6.5306)) - (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).mean()) / (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).std()).rolling(63).std()) * 0.652328).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc121_21d_slope_v121_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc121_21d_slope_v121_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc122_200d_slope_v122_signal(debt, ebitda):
    res = (((((debt / (ebitda + 2.3377)) / (debt / (ebitda + 2.3377)).rolling(126).max()) - ((debt / (ebitda + 2.3377)) / (debt / (ebitda + 2.3377)).rolling(126).max()).rolling(150).mean()) / ((debt / (ebitda + 2.3377)) / (debt / (ebitda + 2.3377)).rolling(126).max()).rolling(150).std()).rolling(42).skew() * 0.851487).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc122_200d_slope_v122_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc122_200d_slope_v122_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc123_10d_slope_v123_signal(liabilities, revenue):
    res = ((liabilities.diff(3) / (revenue.shift(5) + 0.2121)).pct_change(105).rolling(42).var() * 0.928195).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc123_10d_slope_v123_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc123_10d_slope_v123_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc124_84d_slope_v124_signal(debt, revenue):
    res = ((revenue / (debt + 5.8195)).rolling(42).std().pct_change(42).pct_change(126).rolling(10).max() * 0.547762).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc124_84d_slope_v124_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc124_84d_slope_v124_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc125_105d_slope_v125_signal(liabilities, revenue):
    res = ((((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max() - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max().rolling(126).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max().rolling(126).std()).rolling(105).skew() * 0.031309).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc125_105d_slope_v125_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc125_105d_slope_v125_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc126_10d_slope_v126_signal(equity, liabilities):
    res = ((equity / (liabilities + 7.3237)).rolling(150).mean().rolling(10).min().rolling(150).skew() * 0.153351).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc126_10d_slope_v126_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc126_10d_slope_v126_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc127_105d_slope_v127_signal(equity, liabilities):
    res = ((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(200).var().diff(84).rolling(150).kurt() * 0.538948).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc127_105d_slope_v127_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc127_105d_slope_v127_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc128_63d_slope_v128_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 8.9146)).diff(5).rolling(150).max().rolling(200).kurt() * 0.718322).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc128_63d_slope_v128_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc128_63d_slope_v128_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc129_252d_slope_v129_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 1.5659)).rolling(105).max().pct_change(5).pct_change(252) * 0.544997).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc129_252d_slope_v129_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc129_252d_slope_v129_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc130_126d_slope_v130_signal(debt, ebitda):
    res = ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std().rolling(105).min().rolling(105).kurt() * 0.741869).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc130_126d_slope_v130_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc130_126d_slope_v130_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc131_21d_slope_v131_signal(liabilities, revenue):
    res = ((((liabilities / (revenue + 1.6078)) - (liabilities / (revenue + 1.6078)).rolling(150).mean()) / (liabilities / (revenue + 1.6078)).rolling(150).std()).diff(150).rolling(21).mean() * 0.723697).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc131_21d_slope_v131_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc131_21d_slope_v131_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc132_252d_slope_v132_signal(debt, revenue):
    res = ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).min().rolling(21).kurt().diff(21) * 0.600662).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc132_252d_slope_v132_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc132_252d_slope_v132_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc133_105d_slope_v133_signal(liabilities, revenue):
    res = ((revenue / (liabilities + 6.1980)).rolling(42).min().rolling(21).min().rolling(126).std().diff(10) * 0.205575).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc133_105d_slope_v133_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc133_105d_slope_v133_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc134_105d_slope_v134_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 1.6583)).rolling(42).skew().rolling(10).var() * 0.427381).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc134_105d_slope_v134_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc134_105d_slope_v134_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc135_10d_slope_v135_signal(debt, revenue):
    res = ((((((debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std() - (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).std()).rolling(42).min() - (((debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std() - (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).std()).rolling(42).min().rolling(126).mean()) / (((debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std() - (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).std()).rolling(42).min().rolling(126).std()) * 0.950305).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc135_10d_slope_v135_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc135_10d_slope_v135_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc136_150d_slope_v136_signal(equity, liabilities):
    res = ((liabilities / (equity + 9.3424)).diff(200).rolling(63).kurt() * 0.196513).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc136_150d_slope_v136_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc136_150d_slope_v136_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc137_21d_slope_v137_signal(debt, revenue):
    res = ((((debt.diff(13) / (revenue.shift(5) + 3.0013)).pct_change(150).rolling(5).skew() - (debt.diff(13) / (revenue.shift(5) + 3.0013)).pct_change(150).rolling(5).skew().rolling(63).mean()) / (debt.diff(13) / (revenue.shift(5) + 3.0013)).pct_change(150).rolling(5).skew().rolling(63).std()) * 0.324559).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc137_21d_slope_v137_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc137_21d_slope_v137_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc138_5d_slope_v138_signal(debt, ebitda):
    res = ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(105).max().diff(42).rolling(42).mean() * 0.411813).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc138_5d_slope_v138_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc138_5d_slope_v138_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc139_5d_slope_v139_signal(equity, liabilities):
    res = (((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).mean() / (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).mean().rolling(252).max()).rolling(200).kurt().rolling(63).skew() * 0.794185).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc139_5d_slope_v139_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc139_5d_slope_v139_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc140_200d_slope_v140_signal(liabilities, revenue):
    res = ((((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).skew() - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).skew().rolling(5).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).skew().rolling(5).std()).rolling(200).skew() * 0.671988).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc140_200d_slope_v140_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc140_200d_slope_v140_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc141_252d_slope_v141_signal(liabilities, revenue):
    res = ((revenue / (liabilities + 2.3718)).rolling(42).skew().rolling(126).skew().diff(63).diff(200) * 0.573062).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc141_252d_slope_v141_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc141_252d_slope_v141_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc142_63d_slope_v142_signal(debt, revenue):
    res = ((debt.diff(15) / (revenue.shift(8) + 2.4193)).rolling(84).mean().rolling(5).skew().rolling(21).max() * 0.271486).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc142_63d_slope_v142_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc142_63d_slope_v142_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc143_10d_slope_v143_signal(ebitda, liabilities):
    res = ((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(105).kurt().rolling(84).skew().pct_change(105) * 0.389605).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc143_10d_slope_v143_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc143_10d_slope_v143_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc144_105d_slope_v144_signal(debt, revenue):
    res = ((((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) - (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).mean()) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).std()).pct_change(10).diff(21) * 0.076106).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc144_105d_slope_v144_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc144_105d_slope_v144_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc145_200d_slope_v145_signal(equity, liabilities):
    res = ((liabilities.diff(10) / (equity.shift(2) + 6.7346)).rolling(200).var().diff(105) * 0.087865).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc145_200d_slope_v145_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc145_200d_slope_v145_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc146_126d_slope_v146_signal(ebitda, liabilities):
    res = ((liabilities / (ebitda + 4.7785)).rolling(252).kurt().rolling(42).skew() * 0.011452).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc146_126d_slope_v146_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc146_126d_slope_v146_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc147_126d_slope_v147_signal(debt, revenue):
    res = ((debt / (revenue + 6.7545)).pct_change(150).rolling(105).kurt() * 0.674534).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc147_126d_slope_v147_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc147_126d_slope_v147_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc148_10d_slope_v148_signal(debt, revenue):
    res = ((((debt.diff(13) / (revenue.shift(2) + 7.2969)).pct_change(84).rolling(252).kurt() - (debt.diff(13) / (revenue.shift(2) + 7.2969)).pct_change(84).rolling(252).kurt().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(2) + 7.2969)).pct_change(84).rolling(252).kurt().rolling(200).std()) * 0.612497).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc148_10d_slope_v148_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc148_10d_slope_v148_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc149_150d_slope_v149_signal(liabilities, revenue):
    res = ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(42).kurt().rolling(42).mean().rolling(105).var().rolling(84).kurt() * 0.152179).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc149_150d_slope_v149_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc149_150d_slope_v149_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc150_200d_slope_v150_signal(debt, ebitda):
    res = ((debt.diff(17) / (ebitda.shift(10) + 0.4355)).rolling(252).min().diff(84).rolling(105).var() * 0.048407).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc150_200d_slope_v150_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc150_200d_slope_v150_signal


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
