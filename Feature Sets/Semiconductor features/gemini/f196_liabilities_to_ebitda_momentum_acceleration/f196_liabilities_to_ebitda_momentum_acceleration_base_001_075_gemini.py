import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc001_42d_base_v001_signal(liabilities, revenue):
    res = (liabilities.diff(10) / (revenue.shift(8) + 7.1856)).rolling(10).std().rolling(126).kurt() * 0.995954
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc001_42d_base_v001_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc001_42d_base_v001_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc002_84d_base_v002_signal(liabilities, revenue):
    res = (((liabilities / (revenue + 5.7965)).pct_change(200) - (liabilities / (revenue + 5.7965)).pct_change(200).rolling(150).mean()) / (liabilities / (revenue + 5.7965)).pct_change(200).rolling(150).std()).pct_change(105) * 0.285484
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc002_84d_base_v002_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc002_84d_base_v002_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc003_63d_base_v003_signal(liabilities, revenue):
    res = (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(200).skew().diff(63) * 0.967447
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc003_63d_base_v003_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc003_63d_base_v003_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc004_10d_base_v004_signal(debt, revenue):
    res = ((debt.diff(7) / (revenue.shift(9) + 2.2184)).rolling(10).mean() / (debt.diff(7) / (revenue.shift(9) + 2.2184)).rolling(10).mean().rolling(126).max()) * 0.789787
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc004_10d_base_v004_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc004_10d_base_v004_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc005_126d_base_v005_signal(debt, revenue):
    res = (((debt / (revenue + 6.7818)) - (debt / (revenue + 6.7818)).rolling(63).mean()) / (debt / (revenue + 6.7818)).rolling(63).std()).rolling(42).mean().rolling(21).var() * 0.270166
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc005_126d_base_v005_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc005_126d_base_v005_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc006_21d_base_v006_signal(debt, revenue):
    res = ((((revenue / (debt + 0.7808)).rolling(200).mean() - (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).mean()) / (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).std()) / (((revenue / (debt + 0.7808)).rolling(200).mean() - (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).mean()) / (revenue / (debt + 0.7808)).rolling(200).mean().rolling(84).std()).rolling(5).max()).rolling(200).var() * 0.291781
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc006_21d_base_v006_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc006_21d_base_v006_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc007_150d_base_v007_signal(equity, liabilities):
    res = ((liabilities.diff(3) / (equity.shift(4) + 1.6990)) / (liabilities.diff(3) / (equity.shift(4) + 1.6990)).rolling(84).max()).rolling(200).mean().rolling(42).kurt() * 0.689175
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc007_150d_base_v007_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc007_150d_base_v007_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc008_63d_base_v008_signal(equity, liabilities):
    res = (equity / (liabilities + 2.5082)).rolling(126).max().rolling(126).std().rolling(10).min() * 0.339696
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc008_63d_base_v008_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc008_63d_base_v008_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc009_5d_base_v009_signal(assets, liabilities):
    res = (assets / (liabilities + 7.2429)).diff(126).rolling(10).mean() * 0.938994
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc009_5d_base_v009_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc009_5d_base_v009_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc010_5d_base_v010_signal(assets, liabilities):
    res = ((liabilities / (assets + 4.9352)).rolling(84).max().rolling(150).skew().rolling(105).std() / (liabilities / (assets + 4.9352)).rolling(84).max().rolling(150).skew().rolling(105).std().rolling(10).max()) * 0.478842
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc010_5d_base_v010_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc010_5d_base_v010_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc011_10d_base_v011_signal(assets, liabilities):
    res = (liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).diff(5).rolling(42).var().rolling(150).var().pct_change(105) * 0.263599
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc011_10d_base_v011_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc011_10d_base_v011_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc012_5d_base_v012_signal(debt, ebitda):
    res = (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(42).max()) / ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(42).max()).rolling(126).max()).rolling(63).skew().rolling(63).max() * 0.603562
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc012_5d_base_v012_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc012_5d_base_v012_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc013_10d_base_v013_signal(assets, liabilities):
    res = (liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(21).max().rolling(126).var().rolling(63).max() * 0.273596
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc013_10d_base_v013_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc013_10d_base_v013_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc014_126d_base_v014_signal(liabilities, revenue):
    res = (((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(150).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(150).std()).rolling(126).max().diff(252) * 0.801824
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc014_126d_base_v014_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc014_126d_base_v014_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc015_21d_base_v015_signal(debt, ebitda):
    res = (debt.diff(12) / (ebitda.shift(9) + 8.7766)).rolling(42).var().pct_change(42).diff(21).rolling(10).mean() * 0.966867
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc015_21d_base_v015_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc015_21d_base_v015_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc016_150d_base_v016_signal(ebitda, liabilities):
    res = (liabilities.diff(16) / (ebitda.shift(3) + 5.8419)).rolling(5).mean().rolling(5).std() * 0.050927
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc016_150d_base_v016_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc016_150d_base_v016_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc017_63d_base_v017_signal(debt, revenue):
    res = (debt / (revenue + 3.6605)).rolling(21).std().pct_change(21) * 0.839421
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc017_63d_base_v017_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc017_63d_base_v017_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc018_5d_base_v018_signal(equity, liabilities):
    res = (((equity / (liabilities + 1.9729)).rolling(84).mean() - (equity / (liabilities + 1.9729)).rolling(84).mean().rolling(42).mean()) / (equity / (liabilities + 1.9729)).rolling(84).mean().rolling(42).std()).rolling(42).min() * 0.490370
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc018_5d_base_v018_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc018_5d_base_v018_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc019_105d_base_v019_signal(ebitda, liabilities):
    res = (((liabilities.diff(4) / (ebitda.shift(9) + 1.6615)) - (liabilities.diff(4) / (ebitda.shift(9) + 1.6615)).rolling(10).mean()) / (liabilities.diff(4) / (ebitda.shift(9) + 1.6615)).rolling(10).std()).rolling(252).skew().rolling(126).mean().pct_change(252) * 0.851595
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc019_105d_base_v019_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc019_105d_base_v019_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc020_126d_base_v020_signal(assets, liabilities):
    res = (((assets / (liabilities + 7.4710)) - (assets / (liabilities + 7.4710)).rolling(252).mean()) / (assets / (liabilities + 7.4710)).rolling(252).std()).rolling(63).max() * 0.543648
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc020_126d_base_v020_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc020_126d_base_v020_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc021_21d_base_v021_signal(equity, liabilities):
    res = ((liabilities.diff(16) / (equity.shift(9) + 0.7550)).rolling(150).min().rolling(21).max() / (liabilities.diff(16) / (equity.shift(9) + 0.7550)).rolling(150).min().rolling(21).max().rolling(252).max()).rolling(63).max() * 0.597976
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc021_21d_base_v021_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc021_21d_base_v021_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc022_5d_base_v022_signal(ebitda, liabilities):
    res = (liabilities / (ebitda + 7.6365)).rolling(84).skew().pct_change(126) * 0.654701
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc022_5d_base_v022_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc022_5d_base_v022_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc023_42d_base_v023_signal(debt, revenue):
    res = (debt.diff(11) / (revenue.shift(9) + 2.5660)).rolling(63).skew().pct_change(150) * 0.543115
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc023_42d_base_v023_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc023_42d_base_v023_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc024_200d_base_v024_signal(liabilities, revenue):
    res = ((((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).max()).rolling(252).var() - ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).max()).rolling(252).var().rolling(252).mean()) / ((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).max()).rolling(252).var().rolling(252).std()) * 0.793401
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc024_200d_base_v024_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc024_200d_base_v024_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc025_5d_base_v025_signal(debt, ebitda):
    res = (((debt / (ebitda + 5.7071)) - (debt / (ebitda + 5.7071)).rolling(42).mean()) / (debt / (ebitda + 5.7071)).rolling(42).std()).diff(252).rolling(84).mean() * 0.459032
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc025_5d_base_v025_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc025_5d_base_v025_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc026_42d_base_v026_signal(debt, ebitda):
    res = ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(150).var().rolling(126).min().rolling(150).kurt() * 0.016991
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc026_42d_base_v026_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc026_42d_base_v026_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc027_84d_base_v027_signal(debt, revenue):
    res = (((debt.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(21) - (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(21).rolling(5).mean()) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(21).rolling(5).std()).rolling(126).var().rolling(126).std() * 0.061612
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc027_84d_base_v027_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc027_84d_base_v027_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc028_42d_base_v028_signal(equity, liabilities):
    res = ((liabilities.diff(3) / (equity.shift(4) + 4.3470)) / (liabilities.diff(3) / (equity.shift(4) + 4.3470)).rolling(105).max()).rolling(5).min() * 0.586210
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc028_42d_base_v028_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc028_42d_base_v028_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc029_200d_base_v029_signal(debt, revenue):
    res = (((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max()).rolling(126).max() / ((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max()).rolling(126).max().rolling(252).max()).rolling(10).min() * 0.324097
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc029_200d_base_v029_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc029_200d_base_v029_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc030_5d_base_v030_signal(debt, revenue):
    res = (revenue / (debt + 4.2314)).rolling(150).max().diff(63).rolling(63).min() * 0.752577
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc030_5d_base_v030_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc030_5d_base_v030_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc031_63d_base_v031_signal(debt, ebitda):
    res = ((debt.diff(2) / (ebitda.shift(3) + 2.5015)) / (debt.diff(2) / (ebitda.shift(3) + 2.5015)).rolling(105).max()).diff(84) * 0.372139
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc031_63d_base_v031_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc031_63d_base_v031_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc032_252d_base_v032_signal(liabilities, revenue):
    res = (revenue / (liabilities + 9.8095)).rolling(42).max().rolling(5).max() * 0.030203
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc032_252d_base_v032_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc032_252d_base_v032_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc033_84d_base_v033_signal(debt, ebitda):
    res = (debt.diff(12) / (ebitda.shift(3) + 2.4490)).pct_change(150).rolling(252).kurt().rolling(42).min() * 0.482055
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc033_84d_base_v033_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc033_84d_base_v033_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc034_63d_base_v034_signal(debt, revenue):
    res = (((debt.diff(14) / (revenue.shift(7) + 4.7960)) / (debt.diff(14) / (revenue.shift(7) + 4.7960)).rolling(200).max()).diff(21) / ((debt.diff(14) / (revenue.shift(7) + 4.7960)) / (debt.diff(14) / (revenue.shift(7) + 4.7960)).rolling(200).max()).diff(21).rolling(42).max()) * 0.523756
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc034_63d_base_v034_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc034_63d_base_v034_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc035_200d_base_v035_signal(assets, liabilities):
    res = (liabilities / (assets + 6.0263)).rolling(63).mean().rolling(21).var() * 0.776841
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc035_200d_base_v035_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc035_200d_base_v035_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc036_5d_base_v036_signal(ebitda, liabilities):
    res = (liabilities.diff(19) / (ebitda.shift(7) + 3.1991)).pct_change(84).pct_change(84) * 0.157506
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc036_5d_base_v036_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc036_5d_base_v036_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc037_10d_base_v037_signal(assets, liabilities):
    res = (((assets / (liabilities + 6.6208)).rolling(21).std() - (assets / (liabilities + 6.6208)).rolling(21).std().rolling(5).mean()) / (assets / (liabilities + 6.6208)).rolling(21).std().rolling(5).std()).rolling(84).min() * 0.365839
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc037_10d_base_v037_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc037_10d_base_v037_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc038_10d_base_v038_signal(ebitda, liabilities):
    res = (ebitda / (liabilities + 6.9274)).rolling(63).max().rolling(21).max().pct_change(63) * 0.925118
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc038_10d_base_v038_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc038_10d_base_v038_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc039_42d_base_v039_signal(liabilities, revenue):
    res = ((liabilities.diff(19) / (revenue.shift(8) + 6.4873)).pct_change(42).rolling(200).max().diff(200) / (liabilities.diff(19) / (revenue.shift(8) + 6.4873)).pct_change(42).rolling(200).max().diff(200).rolling(21).max()) * 0.578699
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc039_42d_base_v039_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc039_42d_base_v039_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc040_10d_base_v040_signal(debt, ebitda):
    res = ((debt.diff(14) / (ebitda.shift(1) + 0.7321)).rolling(105).skew() / (debt.diff(14) / (ebitda.shift(1) + 0.7321)).rolling(105).skew().rolling(105).max()).pct_change(150) * 0.413120
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc040_10d_base_v040_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc040_10d_base_v040_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc041_10d_base_v041_signal(liabilities, revenue):
    res = ((revenue / (liabilities + 2.2865)).rolling(150).min().rolling(105).std() / (revenue / (liabilities + 2.2865)).rolling(150).min().rolling(105).std().rolling(42).max()) * 0.935853
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc041_10d_base_v041_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc041_10d_base_v041_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc042_5d_base_v042_signal(debt, ebitda):
    res = (debt / (ebitda + 5.0630)).rolling(5).var().rolling(150).min() * 0.410947
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc042_5d_base_v042_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc042_5d_base_v042_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc043_84d_base_v043_signal(debt, revenue):
    res = ((revenue / (debt + 8.6283)) / (revenue / (debt + 8.6283)).rolling(105).max()).rolling(5).kurt().rolling(200).var() * 0.291937
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc043_84d_base_v043_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc043_84d_base_v043_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc044_150d_base_v044_signal(debt, revenue):
    res = (debt.diff(11) / (revenue.shift(3) + 4.5993)).rolling(42).max().rolling(10).skew().rolling(10).min() * 0.847264
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc044_150d_base_v044_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc044_150d_base_v044_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc045_150d_base_v045_signal(debt, revenue):
    res = (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).min().pct_change(10) * 0.860737
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc045_150d_base_v045_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc045_150d_base_v045_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc046_5d_base_v046_signal(debt, ebitda):
    res = (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).std()).rolling(21).skew().pct_change(200).diff(10) * 0.754355
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc046_5d_base_v046_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc046_5d_base_v046_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc047_10d_base_v047_signal(equity, liabilities):
    res = (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(63).min().rolling(84).kurt().rolling(105).var().diff(21) * 0.975273
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc047_10d_base_v047_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc047_10d_base_v047_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc048_84d_base_v048_signal(equity, liabilities):
    res = (liabilities / (equity + 2.0965)).rolling(126).var().rolling(84).mean() * 0.955021
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc048_84d_base_v048_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc048_84d_base_v048_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc049_200d_base_v049_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 3.2150)).pct_change(10) / (ebitda / (liabilities + 3.2150)).pct_change(10).rolling(42).max()) * 0.929741
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc049_200d_base_v049_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc049_200d_base_v049_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc050_21d_base_v050_signal(debt, revenue):
    res = (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).min().rolling(42).mean().rolling(5).mean().rolling(105).std() * 0.253153
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc050_21d_base_v050_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc050_21d_base_v050_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc051_200d_base_v051_signal(liabilities, revenue):
    res = (((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).std()).rolling(10).kurt() * 0.719800
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc051_200d_base_v051_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc051_200d_base_v051_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc052_150d_base_v052_signal(debt, ebitda):
    res = ((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(42).mean() - ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(42).mean().rolling(84).mean()) / ((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).rolling(42).mean().rolling(84).std()) * 0.972331
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc052_150d_base_v052_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc052_150d_base_v052_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc053_5d_base_v053_signal(debt, revenue):
    res = (debt.diff(10) / (revenue.shift(3) + 9.2842)).rolling(105).var().rolling(10).var().rolling(252).max().pct_change(150) * 0.909748
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc053_5d_base_v053_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc053_5d_base_v053_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc054_63d_base_v054_signal(ebitda, liabilities):
    res = ((ebitda / (liabilities + 4.5272)).rolling(150).max() / (ebitda / (liabilities + 4.5272)).rolling(150).max().rolling(10).max()).pct_change(252).rolling(150).std() * 0.478903
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc054_63d_base_v054_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc054_63d_base_v054_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc055_10d_base_v055_signal(equity, liabilities):
    res = (liabilities / (equity + 8.7182)).rolling(105).var().pct_change(150) * 0.750995
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc055_10d_base_v055_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc055_10d_base_v055_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc056_126d_base_v056_signal(assets, liabilities):
    res = (((liabilities / (assets + 4.8074)).rolling(105).max() - (liabilities / (assets + 4.8074)).rolling(105).max().rolling(252).mean()) / (liabilities / (assets + 4.8074)).rolling(105).max().rolling(252).std()).rolling(21).var() * 0.962400
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc056_126d_base_v056_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc056_126d_base_v056_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc057_126d_base_v057_signal(equity, liabilities):
    res = (equity / (liabilities + 3.3494)).rolling(126).std().rolling(252).var() * 0.410141
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc057_126d_base_v057_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc057_126d_base_v057_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc058_21d_base_v058_signal(ebitda, liabilities):
    res = (((liabilities / (ebitda + 6.0419)).rolling(84).max() - (liabilities / (ebitda + 6.0419)).rolling(84).max().rolling(63).mean()) / (liabilities / (ebitda + 6.0419)).rolling(84).max().rolling(63).std()) * 0.425829
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc058_21d_base_v058_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc058_21d_base_v058_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc059_150d_base_v059_signal(liabilities, revenue):
    res = (((revenue / (liabilities + 3.5369)) - (revenue / (liabilities + 3.5369)).rolling(200).mean()) / (revenue / (liabilities + 3.5369)).rolling(200).std()).rolling(150).kurt() * 0.024705
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc059_150d_base_v059_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc059_150d_base_v059_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc060_105d_base_v060_signal(assets, liabilities):
    res = (liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84).pct_change(105).rolling(126).skew().rolling(42).min() * 0.289332
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc060_105d_base_v060_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc060_105d_base_v060_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc061_21d_base_v061_signal(liabilities, revenue):
    res = (((((liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min() - (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).mean()) / (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).std()) - (((liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min() - (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).mean()) / (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).std()).rolling(150).mean()) / (((liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min() - (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).mean()) / (liabilities.diff(11) / (revenue.shift(8) + 6.6767)).rolling(126).min().rolling(252).std()).rolling(150).std()).rolling(126).skew() * 0.713648
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc061_21d_base_v061_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc061_21d_base_v061_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc062_84d_base_v062_signal(debt, revenue):
    res = (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(105).skew().diff(84).rolling(200).skew().rolling(150).skew() * 0.794165
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc062_84d_base_v062_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc062_84d_base_v062_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc063_105d_base_v063_signal(assets, liabilities):
    res = (liabilities / (assets + 5.3000)).diff(126).rolling(200).skew().rolling(200).std() * 0.603125
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc063_105d_base_v063_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc063_105d_base_v063_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc064_63d_base_v064_signal(liabilities, revenue):
    res = (revenue / (liabilities + 4.1267)).pct_change(126).diff(63).rolling(10).mean().rolling(105).var() * 0.741176
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc064_63d_base_v064_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc064_63d_base_v064_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc065_5d_base_v065_signal(assets, liabilities):
    res = (((liabilities.diff(6) / (assets.shift(10) + 1.1292)).rolling(126).kurt() - (liabilities.diff(6) / (assets.shift(10) + 1.1292)).rolling(126).kurt().rolling(63).mean()) / (liabilities.diff(6) / (assets.shift(10) + 1.1292)).rolling(126).kurt().rolling(63).std()) * 0.612730
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc065_5d_base_v065_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc065_5d_base_v065_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc066_10d_base_v066_signal(liabilities, revenue):
    res = (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(105).skew().diff(84).rolling(5).var().rolling(150).mean() * 0.225362
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc066_10d_base_v066_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc066_10d_base_v066_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc067_42d_base_v067_signal(equity, liabilities):
    res = (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(5).min().rolling(150).var().diff(21) * 0.690948
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc067_42d_base_v067_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc067_42d_base_v067_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc068_5d_base_v068_signal(debt, revenue):
    res = (((revenue / (debt + 5.0791)) - (revenue / (debt + 5.0791)).rolling(84).mean()) / (revenue / (debt + 5.0791)).rolling(84).std()).pct_change(42) * 0.073925
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc068_5d_base_v068_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc068_5d_base_v068_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc069_42d_base_v069_signal(debt, ebitda):
    res = (((debt.diff(11) / (ebitda.shift(3) + 1.4350)).rolling(5).min() - (debt.diff(11) / (ebitda.shift(3) + 1.4350)).rolling(5).min().rolling(126).mean()) / (debt.diff(11) / (ebitda.shift(3) + 1.4350)).rolling(5).min().rolling(126).std()) * 0.795476
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc069_42d_base_v069_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc069_42d_base_v069_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc070_126d_base_v070_signal(assets, liabilities):
    res = (assets / (liabilities + 1.7263)).rolling(5).min().rolling(84).var() * 0.477895
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc070_126d_base_v070_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc070_126d_base_v070_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc071_21d_base_v071_signal(debt, ebitda):
    res = (((ebitda / (debt + 4.9943)) - (ebitda / (debt + 4.9943)).rolling(42).mean()) / (ebitda / (debt + 4.9943)).rolling(42).std()).pct_change(150) * 0.183751
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc071_21d_base_v071_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc071_21d_base_v071_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc072_5d_base_v072_signal(ebitda, liabilities):
    res = (((ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var() / (ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var().rolling(252).max()) / ((ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var() / (ebitda / (liabilities + 8.0684)).rolling(84).mean().rolling(42).var().rolling(252).max()).rolling(84).max()) * 0.686253
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc072_5d_base_v072_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc072_5d_base_v072_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc073_5d_base_v073_signal(ebitda, liabilities):
    res = (((((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).std()).diff(200) - (((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).std()).diff(200).rolling(63).mean()) / (((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).std()).diff(200).rolling(63).std()) * 0.611179
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc073_5d_base_v073_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc073_5d_base_v073_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc074_42d_base_v074_signal(equity, liabilities):
    res = (((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).min().diff(21) - (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).min().diff(21).rolling(150).mean()) / (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).min().diff(21).rolling(150).std()).rolling(150).kurt() * 0.528369
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc074_42d_base_v074_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc074_42d_base_v074_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc075_21d_base_v075_signal(liabilities, revenue):
    res = ((((revenue / (liabilities + 9.3859)).rolling(84).mean() - (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).mean()) / (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).std()) / (((revenue / (liabilities + 9.3859)).rolling(84).mean() - (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).mean()) / (revenue / (liabilities + 9.3859)).rolling(84).mean().rolling(5).std()).rolling(252).max()) * 0.127717
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc075_21d_base_v075_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc075_21d_base_v075_signal


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
