import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f204r_f204_revenue_growth_relative_to_equity_calc001_200d_jerk_v001_signal(revenue, equity):
    res = ((equity / (revenue + 0.6698)).rolling(13).mean().rolling(20).var().pct_change(18) * 0.753285).diff(11).diff(17).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc001_200d_jerk_v001_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc001_200d_jerk_v001_signal

def f204r_f204_revenue_growth_relative_to_equity_calc002_150d_jerk_v002_signal(revenue, equity):
    res = ((revenue * 3.5355 - equity).pct_change(28).rolling(23).max() * 0.702292).diff(2).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc002_150d_jerk_v002_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc002_150d_jerk_v002_signal

def f204r_f204_revenue_growth_relative_to_equity_calc003_126d_jerk_v003_signal(revenue, equity):
    res = ((equity / (revenue + 3.2076)).rolling(4).var().rolling(17).min().rolling(24).max() * 0.630743).diff(16).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc003_126d_jerk_v003_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc003_126d_jerk_v003_signal

def f204r_f204_revenue_growth_relative_to_equity_calc004_42d_jerk_v004_signal(revenue, equity):
    res = ((revenue / (equity + 8.4292)).rolling(33).var().rolling(23).var() * 0.410044).diff(8).diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc004_42d_jerk_v004_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc004_42d_jerk_v004_signal

def f204r_f204_revenue_growth_relative_to_equity_calc005_200d_jerk_v005_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(26).var().pct_change(16).rolling(47).mean() * 0.682633).diff(15).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc005_200d_jerk_v005_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc005_200d_jerk_v005_signal

def f204r_f204_revenue_growth_relative_to_equity_calc006_200d_jerk_v006_signal(revenue, equity):
    res = ((revenue * 8.5809 - equity).rolling(50).min().rolling(9).max().pct_change(10) * 0.011920).diff(15).diff(19).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc006_200d_jerk_v006_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc006_200d_jerk_v006_signal

def f204r_f204_revenue_growth_relative_to_equity_calc007_63d_jerk_v007_signal(revenue, equity):
    res = ((revenue / (equity + 4.8580)).pct_change(32).rolling(3).min().rolling(8).var() * 0.813604).diff(9).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc007_63d_jerk_v007_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc007_63d_jerk_v007_signal

def f204r_f204_revenue_growth_relative_to_equity_calc008_252d_jerk_v008_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(23).min().pct_change(35) * 0.988652).diff(15).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc008_252d_jerk_v008_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc008_252d_jerk_v008_signal

def f204r_f204_revenue_growth_relative_to_equity_calc009_126d_jerk_v009_signal(revenue, equity):
    res = ((revenue * 6.9962 - equity).diff(38).rolling(14).std().rolling(9).var() * 0.529402).diff(5).diff(8).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc009_126d_jerk_v009_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc009_126d_jerk_v009_signal

def f204r_f204_revenue_growth_relative_to_equity_calc010_200d_jerk_v010_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(17).max().rolling(49).min().rolling(45).mean() * 0.164653).diff(9).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc010_200d_jerk_v010_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc010_200d_jerk_v010_signal

def f204r_f204_revenue_growth_relative_to_equity_calc011_42d_jerk_v011_signal(revenue, equity):
    res = ((revenue / (equity + 8.3172)).rolling(11).min().rolling(27).max().diff(29) * 0.072447).diff(19).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc011_42d_jerk_v011_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc011_42d_jerk_v011_signal

def f204r_f204_revenue_growth_relative_to_equity_calc012_105d_jerk_v012_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(2) + 5.5881)).rolling(3).mean().diff(42).rolling(41).var() * 0.353744).diff(6).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc012_105d_jerk_v012_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc012_105d_jerk_v012_signal

def f204r_f204_revenue_growth_relative_to_equity_calc013_200d_jerk_v013_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(43).min().pct_change(41) * 0.704582).diff(3).diff(17).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc013_200d_jerk_v013_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc013_200d_jerk_v013_signal

def f204r_f204_revenue_growth_relative_to_equity_calc014_5d_jerk_v014_signal(revenue, equity):
    res = ((equity / (revenue + 6.5282)).diff(50).diff(42).pct_change(13) * 0.748666).diff(18).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc014_5d_jerk_v014_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc014_5d_jerk_v014_signal

def f204r_f204_revenue_growth_relative_to_equity_calc015_105d_jerk_v015_signal(revenue, equity):
    res = ((revenue * 0.2673 - equity).pct_change(42).rolling(7).mean() * 0.514053).diff(18).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc015_105d_jerk_v015_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc015_105d_jerk_v015_signal

def f204r_f204_revenue_growth_relative_to_equity_calc016_150d_jerk_v016_signal(revenue, equity):
    res = ((equity / (revenue + 8.5223)).pct_change(40).diff(18).pct_change(43) * 0.232719).diff(6).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc016_150d_jerk_v016_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc016_150d_jerk_v016_signal

def f204r_f204_revenue_growth_relative_to_equity_calc017_42d_jerk_v017_signal(revenue, equity):
    res = ((revenue / (equity + 7.8698)).rolling(9).min().rolling(42).mean().rolling(34).mean().rolling(36).min() * 0.587929).diff(9).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc017_42d_jerk_v017_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc017_42d_jerk_v017_signal

def f204r_f204_revenue_growth_relative_to_equity_calc018_84d_jerk_v018_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(4) + 0.6054)).rolling(50).std().rolling(46).mean().rolling(33).mean().pct_change(50) * 0.436266).diff(5).diff(17).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc018_84d_jerk_v018_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc018_84d_jerk_v018_signal

def f204r_f204_revenue_growth_relative_to_equity_calc019_126d_jerk_v019_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(26).min().rolling(3).max().rolling(7).max() * 0.687815).diff(8).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc019_126d_jerk_v019_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc019_126d_jerk_v019_signal

def f204r_f204_revenue_growth_relative_to_equity_calc020_21d_jerk_v020_signal(revenue, equity):
    res = ((equity / (revenue + 0.9863)).rolling(34).std().rolling(13).max() * 0.772388).diff(20).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc020_21d_jerk_v020_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc020_21d_jerk_v020_signal

def f204r_f204_revenue_growth_relative_to_equity_calc021_84d_jerk_v021_signal(revenue, equity):
    res = ((revenue / (equity + 1.7577)).diff(45).rolling(11).var().pct_change(43) * 0.292316).diff(17).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc021_84d_jerk_v021_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc021_84d_jerk_v021_signal

def f204r_f204_revenue_growth_relative_to_equity_calc022_63d_jerk_v022_signal(revenue, equity):
    res = ((equity / (revenue + 1.2226)).diff(18).rolling(35).min().rolling(19).max() * 0.425509).diff(16).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc022_63d_jerk_v022_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc022_63d_jerk_v022_signal

def f204r_f204_revenue_growth_relative_to_equity_calc023_252d_jerk_v023_signal(revenue, equity):
    res = ((revenue * 0.3680 - equity).rolling(40).var().rolling(15).max().rolling(12).var() * 0.061229).diff(18).diff(7).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc023_252d_jerk_v023_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc023_252d_jerk_v023_signal

def f204r_f204_revenue_growth_relative_to_equity_calc024_200d_jerk_v024_signal(revenue, equity):
    res = ((revenue * 7.3996 - equity).rolling(36).min().pct_change(38).diff(20) * 0.360346).diff(7).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc024_200d_jerk_v024_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc024_200d_jerk_v024_signal

def f204r_f204_revenue_growth_relative_to_equity_calc025_42d_jerk_v025_signal(revenue, equity):
    res = ((revenue / (equity + 0.2383)).rolling(45).min().rolling(11).mean().diff(32).rolling(40).std() * 0.634510).diff(10).diff(16).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc025_42d_jerk_v025_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc025_42d_jerk_v025_signal

def f204r_f204_revenue_growth_relative_to_equity_calc026_252d_jerk_v026_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(34).rolling(14).min() * 0.134748).diff(12).diff(6).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc026_252d_jerk_v026_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc026_252d_jerk_v026_signal

def f204r_f204_revenue_growth_relative_to_equity_calc027_105d_jerk_v027_signal(revenue, equity):
    res = ((revenue / (equity + 3.7489)).rolling(9).max().rolling(3).min().rolling(31).min().diff(6) * 0.912824).diff(19).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc027_105d_jerk_v027_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc027_105d_jerk_v027_signal

def f204r_f204_revenue_growth_relative_to_equity_calc028_150d_jerk_v028_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(33).max().pct_change(9).pct_change(25) * 0.962439).diff(3).diff(20).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc028_150d_jerk_v028_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc028_150d_jerk_v028_signal

def f204r_f204_revenue_growth_relative_to_equity_calc029_5d_jerk_v029_signal(revenue, equity):
    res = ((revenue * 7.1824 - equity).rolling(19).var().rolling(49).min().rolling(34).var() * 0.941179).diff(7).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc029_5d_jerk_v029_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc029_5d_jerk_v029_signal

def f204r_f204_revenue_growth_relative_to_equity_calc030_150d_jerk_v030_signal(revenue, equity):
    res = ((revenue / (equity + 0.8552)).pct_change(4).rolling(29).std().pct_change(24) * 0.909890).diff(5).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc030_150d_jerk_v030_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc030_150d_jerk_v030_signal

def f204r_f204_revenue_growth_relative_to_equity_calc031_252d_jerk_v031_signal(revenue, equity):
    res = ((revenue / (equity + 7.2115)).rolling(28).mean().rolling(27).std().rolling(12).std() * 0.803605).diff(13).diff(19).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc031_252d_jerk_v031_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc031_252d_jerk_v031_signal

def f204r_f204_revenue_growth_relative_to_equity_calc032_5d_jerk_v032_signal(revenue, equity):
    res = ((revenue * 6.1868 - equity).pct_change(23).rolling(41).var().rolling(41).var() * 0.518216).diff(18).diff(4).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc032_5d_jerk_v032_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc032_5d_jerk_v032_signal

def f204r_f204_revenue_growth_relative_to_equity_calc033_63d_jerk_v033_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(20).var().rolling(27).min().rolling(44).max().rolling(11).max() * 0.765559).diff(2).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc033_63d_jerk_v033_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc033_63d_jerk_v033_signal

def f204r_f204_revenue_growth_relative_to_equity_calc034_150d_jerk_v034_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(14).min().rolling(39).mean() * 0.436698).diff(15).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc034_150d_jerk_v034_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc034_150d_jerk_v034_signal

def f204r_f204_revenue_growth_relative_to_equity_calc035_21d_jerk_v035_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(47).mean().rolling(40).var().rolling(30).var() * 0.458336).diff(16).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc035_21d_jerk_v035_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc035_21d_jerk_v035_signal

def f204r_f204_revenue_growth_relative_to_equity_calc036_105d_jerk_v036_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(40).max().diff(39).rolling(33).std() * 0.066480).diff(7).diff(14).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc036_105d_jerk_v036_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc036_105d_jerk_v036_signal

def f204r_f204_revenue_growth_relative_to_equity_calc037_10d_jerk_v037_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(50).min().rolling(4).mean() * 0.178693).diff(19).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc037_10d_jerk_v037_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc037_10d_jerk_v037_signal

def f204r_f204_revenue_growth_relative_to_equity_calc038_42d_jerk_v038_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(2) + 5.9241)).rolling(45).max().diff(10).rolling(15).max().rolling(48).std() * 0.360355).diff(19).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc038_42d_jerk_v038_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc038_42d_jerk_v038_signal

def f204r_f204_revenue_growth_relative_to_equity_calc039_126d_jerk_v039_signal(revenue, equity):
    res = ((revenue / (equity + 9.8005)).rolling(14).var().rolling(17).mean().rolling(4).min() * 0.858626).diff(5).diff(13).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc039_126d_jerk_v039_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc039_126d_jerk_v039_signal

def f204r_f204_revenue_growth_relative_to_equity_calc040_252d_jerk_v040_signal(revenue, equity):
    res = ((equity / (revenue + 9.6877)).diff(26).rolling(34).std() * 0.204261).diff(12).diff(7).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc040_252d_jerk_v040_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc040_252d_jerk_v040_signal

def f204r_f204_revenue_growth_relative_to_equity_calc041_63d_jerk_v041_signal(revenue, equity):
    res = ((revenue / (equity + 9.2356)).rolling(36).std().rolling(19).max().rolling(45).mean().rolling(27).std() * 0.683238).diff(2).diff(20).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc041_63d_jerk_v041_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc041_63d_jerk_v041_signal

def f204r_f204_revenue_growth_relative_to_equity_calc042_84d_jerk_v042_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(2) + 5.6149)).rolling(31).mean().rolling(2).min().rolling(39).std() * 0.183937).diff(11).diff(10).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc042_84d_jerk_v042_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc042_84d_jerk_v042_signal

def f204r_f204_revenue_growth_relative_to_equity_calc043_21d_jerk_v043_signal(revenue, equity):
    res = ((revenue * 8.1780 - equity).rolling(17).std().rolling(37).max().pct_change(3).rolling(24).std() * 0.246035).diff(4).diff(6).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc043_21d_jerk_v043_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc043_21d_jerk_v043_signal

def f204r_f204_revenue_growth_relative_to_equity_calc044_63d_jerk_v044_signal(revenue, equity):
    res = ((equity / (revenue + 0.1356)).rolling(16).min().rolling(30).max().rolling(19).min() * 0.494599).diff(16).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc044_63d_jerk_v044_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc044_63d_jerk_v044_signal

def f204r_f204_revenue_growth_relative_to_equity_calc045_84d_jerk_v045_signal(revenue, equity):
    res = ((revenue * 4.7079 - equity).rolling(13).mean().rolling(29).min().rolling(19).min().pct_change(28) * 0.717645).diff(5).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc045_84d_jerk_v045_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc045_84d_jerk_v045_signal

def f204r_f204_revenue_growth_relative_to_equity_calc046_10d_jerk_v046_signal(revenue, equity):
    res = ((revenue / (equity + 5.8908)).rolling(30).mean().rolling(15).max().rolling(6).mean().rolling(46).min() * 0.142301).diff(2).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc046_10d_jerk_v046_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc046_10d_jerk_v046_signal

def f204r_f204_revenue_growth_relative_to_equity_calc047_200d_jerk_v047_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(45).std().rolling(23).mean().diff(42) * 0.868392).diff(3).diff(17).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc047_200d_jerk_v047_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc047_200d_jerk_v047_signal

def f204r_f204_revenue_growth_relative_to_equity_calc048_84d_jerk_v048_signal(revenue, equity):
    res = ((revenue / (equity + 2.8278)).rolling(35).var().rolling(13).max().rolling(21).max().rolling(7).max() * 0.119273).diff(3).diff(20).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc048_84d_jerk_v048_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc048_84d_jerk_v048_signal

def f204r_f204_revenue_growth_relative_to_equity_calc049_84d_jerk_v049_signal(revenue, equity):
    res = ((revenue * 0.5808 - equity).rolling(25).std().rolling(40).min() * 0.445939).diff(18).diff(2).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc049_84d_jerk_v049_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc049_84d_jerk_v049_signal

def f204r_f204_revenue_growth_relative_to_equity_calc050_10d_jerk_v050_signal(revenue, equity):
    res = ((revenue * 1.1608 - equity).diff(22).rolling(11).max().rolling(8).max().rolling(23).std() * 0.487286).diff(19).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc050_10d_jerk_v050_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc050_10d_jerk_v050_signal

def f204r_f204_revenue_growth_relative_to_equity_calc051_252d_jerk_v051_signal(revenue, equity):
    res = ((equity / (revenue + 4.6964)).rolling(37).max().rolling(17).max().pct_change(22).rolling(20).max() * 0.732187).diff(6).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc051_252d_jerk_v051_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc051_252d_jerk_v051_signal

def f204r_f204_revenue_growth_relative_to_equity_calc052_5d_jerk_v052_signal(revenue, equity):
    res = ((revenue / (equity + 9.8979)).pct_change(47).rolling(48).std().diff(37) * 0.100317).diff(15).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc052_5d_jerk_v052_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc052_5d_jerk_v052_signal

def f204r_f204_revenue_growth_relative_to_equity_calc053_10d_jerk_v053_signal(revenue, equity):
    res = ((revenue / (equity + 8.7457)).pct_change(31).pct_change(12) * 0.455855).diff(18).diff(6).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc053_10d_jerk_v053_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc053_10d_jerk_v053_signal

def f204r_f204_revenue_growth_relative_to_equity_calc054_200d_jerk_v054_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(3) + 2.4529)).rolling(23).max().rolling(14).max().diff(43).rolling(6).var() * 0.500140).diff(16).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc054_200d_jerk_v054_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc054_200d_jerk_v054_signal

def f204r_f204_revenue_growth_relative_to_equity_calc055_126d_jerk_v055_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(41).min().pct_change(26).rolling(33).var() * 0.138253).diff(10).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc055_126d_jerk_v055_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc055_126d_jerk_v055_signal

def f204r_f204_revenue_growth_relative_to_equity_calc056_105d_jerk_v056_signal(revenue, equity):
    res = ((revenue * 3.7262 - equity).rolling(43).max().rolling(5).std().rolling(27).max().pct_change(38) * 0.276564).diff(17).diff(14).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc056_105d_jerk_v056_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc056_105d_jerk_v056_signal

def f204r_f204_revenue_growth_relative_to_equity_calc057_63d_jerk_v057_signal(revenue, equity):
    res = ((equity / (revenue + 5.0057)).rolling(3).std().rolling(14).min() * 0.796451).diff(10).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc057_63d_jerk_v057_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc057_63d_jerk_v057_signal

def f204r_f204_revenue_growth_relative_to_equity_calc058_126d_jerk_v058_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(8).std().rolling(20).max().rolling(12).var() * 0.185333).diff(16).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc058_126d_jerk_v058_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc058_126d_jerk_v058_signal

def f204r_f204_revenue_growth_relative_to_equity_calc059_150d_jerk_v059_signal(revenue, equity):
    res = ((revenue * 2.4593 - equity).diff(39).rolling(34).max().rolling(31).mean() * 0.294569).diff(12).diff(2).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc059_150d_jerk_v059_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc059_150d_jerk_v059_signal

def f204r_f204_revenue_growth_relative_to_equity_calc060_150d_jerk_v060_signal(revenue, equity):
    res = ((equity / (revenue + 2.7221)).pct_change(16).rolling(41).mean() * 0.248278).diff(18).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc060_150d_jerk_v060_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc060_150d_jerk_v060_signal

def f204r_f204_revenue_growth_relative_to_equity_calc061_63d_jerk_v061_signal(revenue, equity):
    res = ((equity / (revenue + 4.3652)).rolling(24).std().rolling(14).std().rolling(42).var().rolling(3).min() * 0.077889).diff(11).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc061_63d_jerk_v061_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc061_63d_jerk_v061_signal

def f204r_f204_revenue_growth_relative_to_equity_calc062_126d_jerk_v062_signal(revenue, equity):
    res = ((revenue * 7.7688 - equity).rolling(21).var().pct_change(38).rolling(45).var().rolling(11).max() * 0.060657).diff(4).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc062_126d_jerk_v062_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc062_126d_jerk_v062_signal

def f204r_f204_revenue_growth_relative_to_equity_calc063_126d_jerk_v063_signal(revenue, equity):
    res = ((revenue * 3.4677 - equity).rolling(44).mean().rolling(7).max() * 0.591355).diff(4).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc063_126d_jerk_v063_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc063_126d_jerk_v063_signal

def f204r_f204_revenue_growth_relative_to_equity_calc064_105d_jerk_v064_signal(revenue, equity):
    res = ((revenue / (equity + 8.9512)).rolling(2).var().rolling(12).max().rolling(16).min() * 0.079563).diff(13).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc064_105d_jerk_v064_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc064_105d_jerk_v064_signal

def f204r_f204_revenue_growth_relative_to_equity_calc065_10d_jerk_v065_signal(revenue, equity):
    res = ((revenue * 5.7341 - equity).pct_change(24).rolling(11).var().rolling(12).max() * 0.706854).diff(12).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc065_10d_jerk_v065_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc065_10d_jerk_v065_signal

def f204r_f204_revenue_growth_relative_to_equity_calc066_150d_jerk_v066_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(3) + 7.0841)).rolling(26).min().rolling(27).mean().rolling(13).min() * 0.454197).diff(15).diff(8).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc066_150d_jerk_v066_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc066_150d_jerk_v066_signal

def f204r_f204_revenue_growth_relative_to_equity_calc067_126d_jerk_v067_signal(revenue, equity):
    res = ((revenue / (equity + 2.7748)).diff(21).rolling(9).max().diff(24) * 0.630788).diff(2).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc067_126d_jerk_v067_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc067_126d_jerk_v067_signal

def f204r_f204_revenue_growth_relative_to_equity_calc068_10d_jerk_v068_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(35).mean().rolling(47).min().rolling(19).min().rolling(43).max() * 0.013110).diff(19).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc068_10d_jerk_v068_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc068_10d_jerk_v068_signal

def f204r_f204_revenue_growth_relative_to_equity_calc069_150d_jerk_v069_signal(revenue, equity):
    res = ((revenue / (equity + 3.1165)).rolling(34).mean().rolling(24).min() * 0.415843).diff(6).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc069_150d_jerk_v069_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc069_150d_jerk_v069_signal

def f204r_f204_revenue_growth_relative_to_equity_calc070_21d_jerk_v070_signal(revenue, equity):
    res = ((revenue * 9.1259 - equity).diff(32).pct_change(23) * 0.602013).diff(16).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc070_21d_jerk_v070_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc070_21d_jerk_v070_signal

def f204r_f204_revenue_growth_relative_to_equity_calc071_5d_jerk_v071_signal(revenue, equity):
    res = ((revenue * 9.5024 - equity).rolling(9).std().rolling(19).min() * 0.389977).diff(19).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc071_5d_jerk_v071_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc071_5d_jerk_v071_signal

def f204r_f204_revenue_growth_relative_to_equity_calc072_252d_jerk_v072_signal(revenue, equity):
    res = ((revenue / (equity + 9.3218)).pct_change(45).rolling(8).min() * 0.263736).diff(20).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc072_252d_jerk_v072_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc072_252d_jerk_v072_signal

def f204r_f204_revenue_growth_relative_to_equity_calc073_21d_jerk_v073_signal(revenue, equity):
    res = ((revenue / (equity + 0.4013)).rolling(26).min().pct_change(50).rolling(25).mean().rolling(20).max() * 0.286382).diff(12).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc073_21d_jerk_v073_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc073_21d_jerk_v073_signal

def f204r_f204_revenue_growth_relative_to_equity_calc074_21d_jerk_v074_signal(revenue, equity):
    res = ((revenue.diff(4) / (equity.shift(4) + 8.2179)).rolling(32).var().rolling(10).var().pct_change(38) * 0.402955).diff(14).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc074_21d_jerk_v074_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc074_21d_jerk_v074_signal

def f204r_f204_revenue_growth_relative_to_equity_calc075_252d_jerk_v075_signal(revenue, equity):
    res = ((revenue / (equity + 4.3028)).rolling(16).max().rolling(39).min().diff(23) * 0.415380).diff(6).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc075_252d_jerk_v075_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc075_252d_jerk_v075_signal

def f204r_f204_revenue_growth_relative_to_equity_calc076_10d_jerk_v076_signal(revenue, equity):
    res = ((revenue.diff(10) / (equity.shift(5) + 5.2842)).rolling(29).min().rolling(39).std() * 0.211656).diff(11).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc076_10d_jerk_v076_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc076_10d_jerk_v076_signal

def f204r_f204_revenue_growth_relative_to_equity_calc077_84d_jerk_v077_signal(revenue, equity):
    res = ((equity / (revenue + 8.8237)).rolling(23).min().rolling(12).max() * 0.616522).diff(10).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc077_84d_jerk_v077_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc077_84d_jerk_v077_signal

def f204r_f204_revenue_growth_relative_to_equity_calc078_10d_jerk_v078_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(49).mean().rolling(8).std() * 0.651477).diff(2).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc078_10d_jerk_v078_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc078_10d_jerk_v078_signal

def f204r_f204_revenue_growth_relative_to_equity_calc079_21d_jerk_v079_signal(revenue, equity):
    res = ((revenue.diff(4) / (equity.shift(4) + 3.1788)).diff(33).rolling(25).mean().diff(34) * 0.082728).diff(2).diff(17).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc079_21d_jerk_v079_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc079_21d_jerk_v079_signal

def f204r_f204_revenue_growth_relative_to_equity_calc080_42d_jerk_v080_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(2) + 2.8973)).rolling(11).std().rolling(24).mean().rolling(5).min() * 0.072228).diff(10).diff(7).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc080_42d_jerk_v080_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc080_42d_jerk_v080_signal

def f204r_f204_revenue_growth_relative_to_equity_calc081_63d_jerk_v081_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(31).var().diff(46) * 0.477270).diff(6).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc081_63d_jerk_v081_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc081_63d_jerk_v081_signal

def f204r_f204_revenue_growth_relative_to_equity_calc082_105d_jerk_v082_signal(revenue, equity):
    res = ((revenue / (equity + 0.6640)).rolling(28).min().rolling(23).var() * 0.631189).diff(11).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc082_105d_jerk_v082_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc082_105d_jerk_v082_signal

def f204r_f204_revenue_growth_relative_to_equity_calc083_126d_jerk_v083_signal(revenue, equity):
    res = ((equity / (revenue + 1.2825)).pct_change(36).diff(36) * 0.962499).diff(7).diff(19).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc083_126d_jerk_v083_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc083_126d_jerk_v083_signal

def f204r_f204_revenue_growth_relative_to_equity_calc084_252d_jerk_v084_signal(revenue, equity):
    res = ((revenue * 5.8255 - equity).rolling(13).max().diff(19).pct_change(21).pct_change(44) * 0.892727).diff(14).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc084_252d_jerk_v084_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc084_252d_jerk_v084_signal

def f204r_f204_revenue_growth_relative_to_equity_calc085_84d_jerk_v085_signal(revenue, equity):
    res = ((revenue * 9.8771 - equity).rolling(8).min().rolling(47).min().diff(9) * 0.700739).diff(12).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc085_84d_jerk_v085_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc085_84d_jerk_v085_signal

def f204r_f204_revenue_growth_relative_to_equity_calc086_105d_jerk_v086_signal(revenue, equity):
    res = ((equity / (revenue + 1.0967)).rolling(19).mean().pct_change(19).rolling(20).mean().pct_change(50) * 0.095344).diff(11).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc086_105d_jerk_v086_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc086_105d_jerk_v086_signal

def f204r_f204_revenue_growth_relative_to_equity_calc087_63d_jerk_v087_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(39).rolling(9).mean() * 0.829348).diff(14).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc087_63d_jerk_v087_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc087_63d_jerk_v087_signal

def f204r_f204_revenue_growth_relative_to_equity_calc088_21d_jerk_v088_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(50).diff(7) * 0.869654).diff(10).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc088_21d_jerk_v088_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc088_21d_jerk_v088_signal

def f204r_f204_revenue_growth_relative_to_equity_calc089_105d_jerk_v089_signal(revenue, equity):
    res = ((revenue / (equity + 3.7121)).rolling(34).max().rolling(39).std().rolling(27).mean() * 0.932007).diff(5).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc089_105d_jerk_v089_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc089_105d_jerk_v089_signal

def f204r_f204_revenue_growth_relative_to_equity_calc090_150d_jerk_v090_signal(revenue, equity):
    res = ((revenue / (equity + 5.2081)).rolling(11).mean().rolling(36).mean() * 0.639830).diff(19).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc090_150d_jerk_v090_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc090_150d_jerk_v090_signal

def f204r_f204_revenue_growth_relative_to_equity_calc091_21d_jerk_v091_signal(revenue, equity):
    res = ((revenue.diff(10) / (equity.shift(4) + 5.5798)).rolling(11).min().pct_change(22).rolling(24).min() * 0.868419).diff(17).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc091_21d_jerk_v091_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc091_21d_jerk_v091_signal

def f204r_f204_revenue_growth_relative_to_equity_calc092_150d_jerk_v092_signal(revenue, equity):
    res = ((revenue * 5.8867 - equity).rolling(40).var().rolling(31).mean().rolling(9).min() * 0.520087).diff(6).diff(18).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc092_150d_jerk_v092_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc092_150d_jerk_v092_signal

def f204r_f204_revenue_growth_relative_to_equity_calc093_200d_jerk_v093_signal(revenue, equity):
    res = ((revenue.diff(6) / (equity.shift(4) + 7.9845)).rolling(17).max().rolling(17).max() * 0.502536).diff(8).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc093_200d_jerk_v093_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc093_200d_jerk_v093_signal

def f204r_f204_revenue_growth_relative_to_equity_calc094_84d_jerk_v094_signal(revenue, equity):
    res = ((equity / (revenue + 0.3960)).rolling(35).std().rolling(28).var().rolling(11).max().rolling(29).mean() * 0.236282).diff(5).diff(7).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc094_84d_jerk_v094_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc094_84d_jerk_v094_signal

def f204r_f204_revenue_growth_relative_to_equity_calc095_84d_jerk_v095_signal(revenue, equity):
    res = ((revenue / (equity + 7.5091)).rolling(43).max().diff(38).rolling(9).min() * 0.880986).diff(7).diff(3).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc095_84d_jerk_v095_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc095_84d_jerk_v095_signal

def f204r_f204_revenue_growth_relative_to_equity_calc096_21d_jerk_v096_signal(revenue, equity):
    res = ((equity / (revenue + 4.1773)).rolling(47).mean().rolling(18).var() * 0.156917).diff(16).diff(11).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc096_21d_jerk_v096_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc096_21d_jerk_v096_signal

def f204r_f204_revenue_growth_relative_to_equity_calc097_10d_jerk_v097_signal(revenue, equity):
    res = ((revenue * 9.9909 - equity).rolling(20).mean().pct_change(30).rolling(48).std() * 0.273353).diff(18).diff(14).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc097_10d_jerk_v097_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc097_10d_jerk_v097_signal

def f204r_f204_revenue_growth_relative_to_equity_calc098_5d_jerk_v098_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(40).diff(18).rolling(34).var() * 0.740096).diff(9).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc098_5d_jerk_v098_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc098_5d_jerk_v098_signal

def f204r_f204_revenue_growth_relative_to_equity_calc099_21d_jerk_v099_signal(revenue, equity):
    res = ((revenue / (equity + 6.1852)).pct_change(48).pct_change(33).pct_change(48).rolling(5).var() * 0.261526).diff(14).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc099_21d_jerk_v099_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc099_21d_jerk_v099_signal

def f204r_f204_revenue_growth_relative_to_equity_calc100_200d_jerk_v100_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(49).diff(22) * 0.454194).diff(6).diff(19).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc100_200d_jerk_v100_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc100_200d_jerk_v100_signal

def f204r_f204_revenue_growth_relative_to_equity_calc101_63d_jerk_v101_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(24).rolling(47).std() * 0.415815).diff(5).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc101_63d_jerk_v101_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc101_63d_jerk_v101_signal

def f204r_f204_revenue_growth_relative_to_equity_calc102_5d_jerk_v102_signal(revenue, equity):
    res = ((revenue * 1.3708 - equity).rolling(44).max().rolling(4).max() * 0.401777).diff(17).diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc102_5d_jerk_v102_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc102_5d_jerk_v102_signal

def f204r_f204_revenue_growth_relative_to_equity_calc103_105d_jerk_v103_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(33).std().rolling(37).min().rolling(11).std().rolling(11).max() * 0.262393).diff(9).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc103_105d_jerk_v103_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc103_105d_jerk_v103_signal

def f204r_f204_revenue_growth_relative_to_equity_calc104_63d_jerk_v104_signal(revenue, equity):
    res = ((equity / (revenue + 5.0351)).rolling(48).var().rolling(45).min().pct_change(11).rolling(39).min() * 0.111848).diff(12).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc104_63d_jerk_v104_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc104_63d_jerk_v104_signal

def f204r_f204_revenue_growth_relative_to_equity_calc105_126d_jerk_v105_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(2) + 4.9883)).rolling(11).mean().rolling(45).var().rolling(17).var() * 0.097460).diff(15).diff(7).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc105_126d_jerk_v105_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc105_126d_jerk_v105_signal

def f204r_f204_revenue_growth_relative_to_equity_calc106_10d_jerk_v106_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(8).min().rolling(43).mean().rolling(5).std() * 0.030299).diff(18).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc106_10d_jerk_v106_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc106_10d_jerk_v106_signal

def f204r_f204_revenue_growth_relative_to_equity_calc107_10d_jerk_v107_signal(revenue, equity):
    res = ((revenue / (equity + 3.2924)).rolling(45).min().pct_change(22).pct_change(15).pct_change(29) * 0.325765).diff(20).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc107_10d_jerk_v107_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc107_10d_jerk_v107_signal

def f204r_f204_revenue_growth_relative_to_equity_calc108_252d_jerk_v108_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(1) + 0.3344)).rolling(35).min().rolling(8).var().diff(42).rolling(19).min() * 0.768526).diff(18).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc108_252d_jerk_v108_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc108_252d_jerk_v108_signal

def f204r_f204_revenue_growth_relative_to_equity_calc109_5d_jerk_v109_signal(revenue, equity):
    res = ((revenue.diff(6) / (equity.shift(3) + 8.6130)).rolling(30).std().rolling(38).max().pct_change(3).pct_change(41) * 0.040101).diff(17).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc109_5d_jerk_v109_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc109_5d_jerk_v109_signal

def f204r_f204_revenue_growth_relative_to_equity_calc110_105d_jerk_v110_signal(revenue, equity):
    res = ((revenue * 4.5697 - equity).rolling(27).var().rolling(38).var().rolling(25).max().diff(34) * 0.380600).diff(7).diff(12).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc110_105d_jerk_v110_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc110_105d_jerk_v110_signal

def f204r_f204_revenue_growth_relative_to_equity_calc111_5d_jerk_v111_signal(revenue, equity):
    res = ((revenue * 5.6646 - equity).rolling(2).mean().rolling(35).min().rolling(42).mean() * 0.728750).diff(19).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc111_5d_jerk_v111_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc111_5d_jerk_v111_signal

def f204r_f204_revenue_growth_relative_to_equity_calc112_126d_jerk_v112_signal(revenue, equity):
    res = ((revenue / (equity + 0.8373)).pct_change(44).rolling(21).mean() * 0.253082).diff(15).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc112_126d_jerk_v112_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc112_126d_jerk_v112_signal

def f204r_f204_revenue_growth_relative_to_equity_calc113_10d_jerk_v113_signal(revenue, equity):
    res = ((revenue / (equity + 4.5367)).rolling(8).mean().diff(49).rolling(46).min().diff(28) * 0.200636).diff(18).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc113_10d_jerk_v113_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc113_10d_jerk_v113_signal

def f204r_f204_revenue_growth_relative_to_equity_calc114_105d_jerk_v114_signal(revenue, equity):
    res = ((revenue / (equity + 4.2983)).pct_change(16).rolling(30).min() * 0.782685).diff(4).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc114_105d_jerk_v114_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc114_105d_jerk_v114_signal

def f204r_f204_revenue_growth_relative_to_equity_calc115_21d_jerk_v115_signal(revenue, equity):
    res = ((revenue.diff(6) / (equity.shift(2) + 2.6961)).rolling(42).var().rolling(34).std().pct_change(28) * 0.443872).diff(3).diff(11).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc115_21d_jerk_v115_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc115_21d_jerk_v115_signal

def f204r_f204_revenue_growth_relative_to_equity_calc116_150d_jerk_v116_signal(revenue, equity):
    res = ((revenue * 3.4760 - equity).rolling(28).max().rolling(35).mean().rolling(41).max() * 0.527028).diff(6).diff(6).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc116_150d_jerk_v116_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc116_150d_jerk_v116_signal

def f204r_f204_revenue_growth_relative_to_equity_calc117_42d_jerk_v117_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(43).mean().diff(29).pct_change(13) * 0.014944).diff(19).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc117_42d_jerk_v117_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc117_42d_jerk_v117_signal

def f204r_f204_revenue_growth_relative_to_equity_calc118_105d_jerk_v118_signal(revenue, equity):
    res = ((revenue * 6.7676 - equity).diff(10).rolling(22).max().diff(38) * 0.404887).diff(6).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc118_105d_jerk_v118_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc118_105d_jerk_v118_signal

def f204r_f204_revenue_growth_relative_to_equity_calc119_84d_jerk_v119_signal(revenue, equity):
    res = ((revenue / (equity + 1.1887)).rolling(7).std().diff(14).rolling(47).var().rolling(15).max() * 0.602349).diff(14).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc119_84d_jerk_v119_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc119_84d_jerk_v119_signal

def f204r_f204_revenue_growth_relative_to_equity_calc120_63d_jerk_v120_signal(revenue, equity):
    res = ((revenue / (equity + 5.4846)).rolling(13).var().rolling(33).var().rolling(23).std().rolling(37).std() * 0.186837).diff(16).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc120_63d_jerk_v120_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc120_63d_jerk_v120_signal

def f204r_f204_revenue_growth_relative_to_equity_calc121_126d_jerk_v121_signal(revenue, equity):
    res = ((equity / (revenue + 6.0315)).rolling(10).var().rolling(47).std().rolling(28).mean() * 0.508058).diff(3).diff(19).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc121_126d_jerk_v121_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc121_126d_jerk_v121_signal

def f204r_f204_revenue_growth_relative_to_equity_calc122_42d_jerk_v122_signal(revenue, equity):
    res = ((equity / (revenue + 8.7538)).pct_change(9).rolling(48).min().rolling(49).var() * 0.962358).diff(14).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc122_42d_jerk_v122_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc122_42d_jerk_v122_signal

def f204r_f204_revenue_growth_relative_to_equity_calc123_252d_jerk_v123_signal(revenue, equity):
    res = ((equity / (revenue + 1.1943)).rolling(2).max().diff(24).rolling(14).min().diff(3) * 0.925447).diff(14).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc123_252d_jerk_v123_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc123_252d_jerk_v123_signal

def f204r_f204_revenue_growth_relative_to_equity_calc124_200d_jerk_v124_signal(revenue, equity):
    res = ((revenue / (equity + 1.5411)).rolling(10).var().rolling(40).std() * 0.593426).diff(5).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc124_200d_jerk_v124_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc124_200d_jerk_v124_signal

def f204r_f204_revenue_growth_relative_to_equity_calc125_150d_jerk_v125_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(38).mean().diff(43).pct_change(14) * 0.830583).diff(3).diff(11).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc125_150d_jerk_v125_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc125_150d_jerk_v125_signal

def f204r_f204_revenue_growth_relative_to_equity_calc126_21d_jerk_v126_signal(revenue, equity):
    res = ((equity / (revenue + 3.6467)).rolling(38).mean().rolling(27).var().rolling(25).var().rolling(4).mean() * 0.918336).diff(13).diff(3).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc126_21d_jerk_v126_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc126_21d_jerk_v126_signal

def f204r_f204_revenue_growth_relative_to_equity_calc127_21d_jerk_v127_signal(revenue, equity):
    res = ((revenue / (equity + 2.7017)).diff(21).diff(30) * 0.597908).diff(5).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc127_21d_jerk_v127_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc127_21d_jerk_v127_signal

def f204r_f204_revenue_growth_relative_to_equity_calc128_126d_jerk_v128_signal(revenue, equity):
    res = ((equity / (revenue + 8.4882)).rolling(24).mean().diff(24).rolling(21).max() * 0.302325).diff(18).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc128_126d_jerk_v128_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc128_126d_jerk_v128_signal

def f204r_f204_revenue_growth_relative_to_equity_calc129_21d_jerk_v129_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(3) + 6.5184)).rolling(14).mean().rolling(14).mean().rolling(39).max().rolling(12).mean() * 0.560173).diff(2).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc129_21d_jerk_v129_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc129_21d_jerk_v129_signal

def f204r_f204_revenue_growth_relative_to_equity_calc130_5d_jerk_v130_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(3) + 4.1533)).diff(11).rolling(49).std().rolling(27).var() * 0.467198).diff(13).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc130_5d_jerk_v130_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc130_5d_jerk_v130_signal

def f204r_f204_revenue_growth_relative_to_equity_calc131_252d_jerk_v131_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(1) + 9.9418)).rolling(10).max().rolling(21).var() * 0.602255).diff(14).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc131_252d_jerk_v131_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc131_252d_jerk_v131_signal

def f204r_f204_revenue_growth_relative_to_equity_calc132_105d_jerk_v132_signal(revenue, equity):
    res = ((revenue.diff(10) / (equity.shift(3) + 6.3933)).rolling(17).var().pct_change(30) * 0.311781).diff(9).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc132_105d_jerk_v132_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc132_105d_jerk_v132_signal

def f204r_f204_revenue_growth_relative_to_equity_calc133_10d_jerk_v133_signal(revenue, equity):
    res = ((revenue / (equity + 9.6370)).rolling(46).var().pct_change(14).rolling(49).mean() * 0.498553).diff(17).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc133_10d_jerk_v133_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc133_10d_jerk_v133_signal

def f204r_f204_revenue_growth_relative_to_equity_calc134_150d_jerk_v134_signal(revenue, equity):
    res = ((revenue / (equity + 8.8204)).rolling(27).var().rolling(37).max().rolling(22).max().rolling(33).mean() * 0.628573).diff(19).diff(11).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc134_150d_jerk_v134_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc134_150d_jerk_v134_signal

def f204r_f204_revenue_growth_relative_to_equity_calc135_200d_jerk_v135_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(3) + 3.9022)).rolling(5).std().pct_change(33).rolling(15).max() * 0.951804).diff(8).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc135_200d_jerk_v135_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc135_200d_jerk_v135_signal

def f204r_f204_revenue_growth_relative_to_equity_calc136_63d_jerk_v136_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(9).pct_change(12) * 0.591069).diff(9).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc136_63d_jerk_v136_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc136_63d_jerk_v136_signal

def f204r_f204_revenue_growth_relative_to_equity_calc137_252d_jerk_v137_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(3) + 6.4823)).rolling(44).min().pct_change(21).pct_change(20) * 0.611132).diff(15).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc137_252d_jerk_v137_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc137_252d_jerk_v137_signal

def f204r_f204_revenue_growth_relative_to_equity_calc138_84d_jerk_v138_signal(revenue, equity):
    res = ((equity / (revenue + 9.4085)).rolling(15).mean().rolling(43).mean() * 0.211646).diff(11).diff(8).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc138_84d_jerk_v138_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc138_84d_jerk_v138_signal

def f204r_f204_revenue_growth_relative_to_equity_calc139_5d_jerk_v139_signal(revenue, equity):
    res = ((revenue / (equity + 5.8782)).rolling(30).max().rolling(42).mean() * 0.376215).diff(2).diff(16).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc139_5d_jerk_v139_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc139_5d_jerk_v139_signal

def f204r_f204_revenue_growth_relative_to_equity_calc140_21d_jerk_v140_signal(revenue, equity):
    res = ((revenue / (equity + 5.2504)).rolling(5).std().rolling(14).mean() * 0.264673).diff(18).diff(6).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc140_21d_jerk_v140_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc140_21d_jerk_v140_signal

def f204r_f204_revenue_growth_relative_to_equity_calc141_42d_jerk_v141_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(40).min().diff(12).rolling(5).std().rolling(20).var() * 0.936269).diff(2).diff(6).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc141_42d_jerk_v141_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc141_42d_jerk_v141_signal

def f204r_f204_revenue_growth_relative_to_equity_calc142_126d_jerk_v142_signal(revenue, equity):
    res = ((revenue / (equity + 0.4011)).rolling(38).std().rolling(49).mean().diff(28).rolling(33).std() * 0.218924).diff(6).diff(19).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc142_126d_jerk_v142_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc142_126d_jerk_v142_signal

def f204r_f204_revenue_growth_relative_to_equity_calc143_5d_jerk_v143_signal(revenue, equity):
    res = ((revenue * 4.4841 - equity).diff(50).diff(37).rolling(10).min() * 0.147784).diff(15).diff(14).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc143_5d_jerk_v143_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc143_5d_jerk_v143_signal

def f204r_f204_revenue_growth_relative_to_equity_calc144_150d_jerk_v144_signal(revenue, equity):
    res = ((equity / (revenue + 6.7629)).rolling(26).var().rolling(27).std().rolling(44).max() * 0.954484).diff(9).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc144_150d_jerk_v144_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc144_150d_jerk_v144_signal

def f204r_f204_revenue_growth_relative_to_equity_calc145_5d_jerk_v145_signal(revenue, equity):
    res = ((equity / (revenue + 4.0005)).rolling(3).max().diff(24) * 0.069789).diff(14).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc145_5d_jerk_v145_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc145_5d_jerk_v145_signal

def f204r_f204_revenue_growth_relative_to_equity_calc146_63d_jerk_v146_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(8).max().pct_change(22).diff(9).rolling(26).max() * 0.421723).diff(20).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc146_63d_jerk_v146_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc146_63d_jerk_v146_signal

def f204r_f204_revenue_growth_relative_to_equity_calc147_10d_jerk_v147_signal(revenue, equity):
    res = ((revenue / (equity + 3.4570)).rolling(27).max().rolling(19).min().rolling(17).std() * 0.266256).diff(9).diff(8).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc147_10d_jerk_v147_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc147_10d_jerk_v147_signal

def f204r_f204_revenue_growth_relative_to_equity_calc148_150d_jerk_v148_signal(revenue, equity):
    res = ((equity / (revenue + 7.5287)).rolling(32).std().rolling(28).var() * 0.985156).diff(20).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc148_150d_jerk_v148_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc148_150d_jerk_v148_signal

def f204r_f204_revenue_growth_relative_to_equity_calc149_105d_jerk_v149_signal(revenue, equity):
    res = ((revenue * 6.7965 - equity).rolling(27).std().rolling(39).var().rolling(10).mean() * 0.916415).diff(11).diff(3).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc149_105d_jerk_v149_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc149_105d_jerk_v149_signal

def f204r_f204_revenue_growth_relative_to_equity_calc150_5d_jerk_v150_signal(revenue, equity):
    res = ((revenue / (equity + 8.3551)).diff(6).rolling(25).var().rolling(8).std().rolling(9).std() * 0.238036).diff(9).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc150_5d_jerk_v150_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc150_5d_jerk_v150_signal


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
