import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f204r_f204_revenue_growth_relative_to_equity_calc001_21d_base_v001_signal(revenue, equity):
    res = (revenue * 2.3680 - equity).rolling(5).var().rolling(9).mean().diff(5).rolling(34).min() * 0.895141
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc001_21d_base_v001_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc001_21d_base_v001_signal

def f204r_f204_revenue_growth_relative_to_equity_calc002_150d_base_v002_signal(revenue, equity):
    res = (equity / (revenue + 8.9424)).rolling(12).min().rolling(5).var() * 0.739935
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc002_150d_base_v002_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc002_150d_base_v002_signal

def f204r_f204_revenue_growth_relative_to_equity_calc003_252d_base_v003_signal(revenue, equity):
    res = (revenue * 5.8938 - equity).pct_change(39).diff(9).rolling(10).mean().rolling(48).mean() * 0.564395
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc003_252d_base_v003_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc003_252d_base_v003_signal

def f204r_f204_revenue_growth_relative_to_equity_calc004_84d_base_v004_signal(revenue, equity):
    res = (revenue / (equity + 7.9205)).pct_change(41).diff(39).rolling(19).mean().rolling(40).var() * 0.590776
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc004_84d_base_v004_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc004_84d_base_v004_signal

def f204r_f204_revenue_growth_relative_to_equity_calc005_252d_base_v005_signal(revenue, equity):
    res = (revenue.diff(2) / (equity.shift(3) + 5.8838)).rolling(11).mean().pct_change(28).diff(15).rolling(36).mean() * 0.833384
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc005_252d_base_v005_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc005_252d_base_v005_signal

def f204r_f204_revenue_growth_relative_to_equity_calc006_105d_base_v006_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(48).diff(46).diff(48).rolling(20).var() * 0.727129
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc006_105d_base_v006_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc006_105d_base_v006_signal

def f204r_f204_revenue_growth_relative_to_equity_calc007_84d_base_v007_signal(revenue, equity):
    res = (revenue.diff(2) / (equity.shift(5) + 7.6100)).pct_change(31).rolling(40).std().rolling(34).mean() * 0.506623
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc007_84d_base_v007_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc007_84d_base_v007_signal

def f204r_f204_revenue_growth_relative_to_equity_calc008_150d_base_v008_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(26).rolling(28).std().rolling(9).max().rolling(8).max() * 0.607536
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc008_150d_base_v008_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc008_150d_base_v008_signal

def f204r_f204_revenue_growth_relative_to_equity_calc009_63d_base_v009_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(21).min().rolling(29).min() * 0.463139
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc009_63d_base_v009_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc009_63d_base_v009_signal

def f204r_f204_revenue_growth_relative_to_equity_calc010_63d_base_v010_signal(revenue, equity):
    res = (revenue.diff(2) / (equity.shift(1) + 2.7498)).rolling(26).mean().rolling(5).min().rolling(24).std().diff(38) * 0.995788
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc010_63d_base_v010_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc010_63d_base_v010_signal

def f204r_f204_revenue_growth_relative_to_equity_calc011_252d_base_v011_signal(revenue, equity):
    res = (revenue / (equity + 7.5258)).diff(8).rolling(27).mean() * 0.849814
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc011_252d_base_v011_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc011_252d_base_v011_signal

def f204r_f204_revenue_growth_relative_to_equity_calc012_150d_base_v012_signal(revenue, equity):
    res = (revenue.diff(2) / (equity.shift(5) + 3.3011)).rolling(27).min().pct_change(40).pct_change(36).pct_change(17) * 0.306708
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc012_150d_base_v012_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc012_150d_base_v012_signal

def f204r_f204_revenue_growth_relative_to_equity_calc013_10d_base_v013_signal(revenue, equity):
    res = (equity / (revenue + 0.3786)).rolling(25).max().rolling(41).var() * 0.363109
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc013_10d_base_v013_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc013_10d_base_v013_signal

def f204r_f204_revenue_growth_relative_to_equity_calc014_84d_base_v014_signal(revenue, equity):
    res = (revenue.diff(10) / (equity.shift(5) + 5.5462)).rolling(29).min().pct_change(16).pct_change(43).pct_change(14) * 0.381656
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc014_84d_base_v014_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc014_84d_base_v014_signal

def f204r_f204_revenue_growth_relative_to_equity_calc015_42d_base_v015_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(19).var().rolling(31).min() * 0.542619
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc015_42d_base_v015_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc015_42d_base_v015_signal

def f204r_f204_revenue_growth_relative_to_equity_calc016_84d_base_v016_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(22).var().rolling(40).mean().rolling(27).max() * 0.176401
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc016_84d_base_v016_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc016_84d_base_v016_signal

def f204r_f204_revenue_growth_relative_to_equity_calc017_21d_base_v017_signal(revenue, equity):
    res = (revenue * 7.3731 - equity).rolling(10).std().rolling(50).std().rolling(49).min() * 0.145536
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc017_21d_base_v017_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc017_21d_base_v017_signal

def f204r_f204_revenue_growth_relative_to_equity_calc018_105d_base_v018_signal(revenue, equity):
    res = (revenue.diff(7) / (equity.shift(4) + 0.2501)).rolling(43).min().pct_change(50).rolling(7).min() * 0.697415
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc018_105d_base_v018_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc018_105d_base_v018_signal

def f204r_f204_revenue_growth_relative_to_equity_calc019_63d_base_v019_signal(revenue, equity):
    res = (revenue * 1.1403 - equity).rolling(38).mean().rolling(49).max().diff(48) * 0.895403
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc019_63d_base_v019_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc019_63d_base_v019_signal

def f204r_f204_revenue_growth_relative_to_equity_calc020_63d_base_v020_signal(revenue, equity):
    res = (revenue * 7.0450 - equity).rolling(11).std().rolling(33).min() * 0.717000
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc020_63d_base_v020_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc020_63d_base_v020_signal

def f204r_f204_revenue_growth_relative_to_equity_calc021_252d_base_v021_signal(revenue, equity):
    res = (revenue / (equity + 8.9221)).rolling(20).mean().rolling(5).min() * 0.842819
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc021_252d_base_v021_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc021_252d_base_v021_signal

def f204r_f204_revenue_growth_relative_to_equity_calc022_63d_base_v022_signal(revenue, equity):
    res = (revenue.diff(5) / (equity.shift(3) + 7.4523)).rolling(50).mean().rolling(17).mean().rolling(5).var() * 0.702857
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc022_63d_base_v022_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc022_63d_base_v022_signal

def f204r_f204_revenue_growth_relative_to_equity_calc023_63d_base_v023_signal(revenue, equity):
    res = (equity / (revenue + 2.4481)).rolling(42).var().rolling(14).var().rolling(28).min().pct_change(2) * 0.171795
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc023_63d_base_v023_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc023_63d_base_v023_signal

def f204r_f204_revenue_growth_relative_to_equity_calc024_5d_base_v024_signal(revenue, equity):
    res = (revenue.diff(3) / (equity.shift(4) + 3.9913)).rolling(14).min().rolling(24).var().rolling(37).std() * 0.498986
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc024_5d_base_v024_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc024_5d_base_v024_signal

def f204r_f204_revenue_growth_relative_to_equity_calc025_105d_base_v025_signal(revenue, equity):
    res = (revenue / (equity + 4.1168)).diff(33).diff(25).rolling(13).max().diff(20) * 0.381111
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc025_105d_base_v025_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc025_105d_base_v025_signal

def f204r_f204_revenue_growth_relative_to_equity_calc026_105d_base_v026_signal(revenue, equity):
    res = (equity / (revenue + 3.1546)).rolling(12).var().rolling(33).mean().pct_change(6) * 0.745549
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc026_105d_base_v026_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc026_105d_base_v026_signal

def f204r_f204_revenue_growth_relative_to_equity_calc027_21d_base_v027_signal(revenue, equity):
    res = (revenue.diff(7) / (equity.shift(3) + 9.1282)).pct_change(32).rolling(23).var().pct_change(27).rolling(37).mean() * 0.099369
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc027_21d_base_v027_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc027_21d_base_v027_signal

def f204r_f204_revenue_growth_relative_to_equity_calc028_42d_base_v028_signal(revenue, equity):
    res = (revenue.diff(10) / (equity.shift(5) + 9.9975)).diff(12).pct_change(50).rolling(43).std() * 0.075380
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc028_42d_base_v028_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc028_42d_base_v028_signal

def f204r_f204_revenue_growth_relative_to_equity_calc029_42d_base_v029_signal(revenue, equity):
    res = (revenue / (equity + 8.5367)).rolling(32).max().rolling(50).max().rolling(12).std() * 0.461214
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc029_42d_base_v029_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc029_42d_base_v029_signal

def f204r_f204_revenue_growth_relative_to_equity_calc030_252d_base_v030_signal(revenue, equity):
    res = (revenue / (equity + 3.7524)).rolling(7).max().rolling(48).mean().diff(20) * 0.209886
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc030_252d_base_v030_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc030_252d_base_v030_signal

def f204r_f204_revenue_growth_relative_to_equity_calc031_10d_base_v031_signal(revenue, equity):
    res = (revenue / (equity + 0.3673)).rolling(17).var().rolling(25).min() * 0.389639
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc031_10d_base_v031_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc031_10d_base_v031_signal

def f204r_f204_revenue_growth_relative_to_equity_calc032_10d_base_v032_signal(revenue, equity):
    res = (equity / (revenue + 0.8451)).rolling(2).std().rolling(3).var() * 0.101765
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc032_10d_base_v032_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc032_10d_base_v032_signal

def f204r_f204_revenue_growth_relative_to_equity_calc033_5d_base_v033_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(41).var().rolling(14).min().rolling(26).min() * 0.871849
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc033_5d_base_v033_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc033_5d_base_v033_signal

def f204r_f204_revenue_growth_relative_to_equity_calc034_10d_base_v034_signal(revenue, equity):
    res = (revenue.diff(3) / (equity.shift(1) + 7.6299)).rolling(3).mean().rolling(37).max() * 0.586870
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc034_10d_base_v034_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc034_10d_base_v034_signal

def f204r_f204_revenue_growth_relative_to_equity_calc035_10d_base_v035_signal(revenue, equity):
    res = (revenue / (equity + 8.0688)).rolling(42).std().rolling(4).min() * 0.699838
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc035_10d_base_v035_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc035_10d_base_v035_signal

def f204r_f204_revenue_growth_relative_to_equity_calc036_200d_base_v036_signal(revenue, equity):
    res = (revenue * 7.1098 - equity).diff(17).pct_change(30).rolling(14).var().rolling(46).var() * 0.803080
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc036_200d_base_v036_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc036_200d_base_v036_signal

def f204r_f204_revenue_growth_relative_to_equity_calc037_105d_base_v037_signal(revenue, equity):
    res = (revenue / (equity + 8.8795)).rolling(37).var().pct_change(6) * 0.410081
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc037_105d_base_v037_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc037_105d_base_v037_signal

def f204r_f204_revenue_growth_relative_to_equity_calc038_5d_base_v038_signal(revenue, equity):
    res = (revenue * 7.1874 - equity).rolling(38).mean().rolling(38).min() * 0.064710
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc038_5d_base_v038_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc038_5d_base_v038_signal

def f204r_f204_revenue_growth_relative_to_equity_calc039_63d_base_v039_signal(revenue, equity):
    res = (revenue * 3.7750 - equity).rolling(28).min().rolling(12).var().rolling(33).min().diff(25) * 0.216548
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc039_63d_base_v039_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc039_63d_base_v039_signal

def f204r_f204_revenue_growth_relative_to_equity_calc040_42d_base_v040_signal(revenue, equity):
    res = (revenue.diff(10) / (equity.shift(4) + 6.0148)).rolling(9).std().rolling(22).std().rolling(36).std().rolling(31).max() * 0.175531
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc040_42d_base_v040_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc040_42d_base_v040_signal

def f204r_f204_revenue_growth_relative_to_equity_calc041_21d_base_v041_signal(revenue, equity):
    res = (revenue * 4.5117 - equity).rolling(17).max().rolling(11).min() * 0.267954
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc041_21d_base_v041_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc041_21d_base_v041_signal

def f204r_f204_revenue_growth_relative_to_equity_calc042_126d_base_v042_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(3).mean().rolling(11).std() * 0.530474
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc042_126d_base_v042_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc042_126d_base_v042_signal

def f204r_f204_revenue_growth_relative_to_equity_calc043_63d_base_v043_signal(revenue, equity):
    res = (revenue.diff(4) / (equity.shift(3) + 4.8337)).pct_change(7).rolling(9).var().diff(8) * 0.323488
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc043_63d_base_v043_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc043_63d_base_v043_signal

def f204r_f204_revenue_growth_relative_to_equity_calc044_84d_base_v044_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(30).pct_change(39) * 0.208714
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc044_84d_base_v044_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc044_84d_base_v044_signal

def f204r_f204_revenue_growth_relative_to_equity_calc045_84d_base_v045_signal(revenue, equity):
    res = (revenue / (equity + 9.2686)).rolling(12).max().pct_change(30).rolling(18).max().rolling(7).min() * 0.655138
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc045_84d_base_v045_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc045_84d_base_v045_signal

def f204r_f204_revenue_growth_relative_to_equity_calc046_126d_base_v046_signal(revenue, equity):
    res = (revenue / (equity + 2.1224)).rolling(8).mean().rolling(41).std().rolling(49).mean() * 0.222808
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc046_126d_base_v046_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc046_126d_base_v046_signal

def f204r_f204_revenue_growth_relative_to_equity_calc047_150d_base_v047_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(29).std().diff(2).rolling(43).max() * 0.540158
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc047_150d_base_v047_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc047_150d_base_v047_signal

def f204r_f204_revenue_growth_relative_to_equity_calc048_150d_base_v048_signal(revenue, equity):
    res = (revenue * 3.9370 - equity).rolling(16).max().pct_change(27).rolling(35).mean() * 0.203060
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc048_150d_base_v048_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc048_150d_base_v048_signal

def f204r_f204_revenue_growth_relative_to_equity_calc049_21d_base_v049_signal(revenue, equity):
    res = (revenue.diff(8) / (equity.shift(4) + 5.9626)).rolling(42).max().rolling(16).max().rolling(41).mean() * 0.630364
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc049_21d_base_v049_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc049_21d_base_v049_signal

def f204r_f204_revenue_growth_relative_to_equity_calc050_105d_base_v050_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(22).std().rolling(37).mean().pct_change(16).rolling(44).mean() * 0.772946
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc050_105d_base_v050_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc050_105d_base_v050_signal

def f204r_f204_revenue_growth_relative_to_equity_calc051_84d_base_v051_signal(revenue, equity):
    res = (revenue * 1.1315 - equity).diff(38).rolling(17).var().rolling(30).max().rolling(37).max() * 0.432908
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc051_84d_base_v051_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc051_84d_base_v051_signal

def f204r_f204_revenue_growth_relative_to_equity_calc052_84d_base_v052_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(26).pct_change(3) * 0.700105
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc052_84d_base_v052_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc052_84d_base_v052_signal

def f204r_f204_revenue_growth_relative_to_equity_calc053_21d_base_v053_signal(revenue, equity):
    res = (revenue * 2.8267 - equity).rolling(31).mean().pct_change(20).rolling(10).min().diff(36) * 0.882986
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc053_21d_base_v053_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc053_21d_base_v053_signal

def f204r_f204_revenue_growth_relative_to_equity_calc054_150d_base_v054_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(35).std().rolling(23).var() * 0.196673
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc054_150d_base_v054_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc054_150d_base_v054_signal

def f204r_f204_revenue_growth_relative_to_equity_calc055_5d_base_v055_signal(revenue, equity):
    res = (revenue.diff(6) / (equity.shift(2) + 9.0740)).rolling(7).max().rolling(6).std().pct_change(8).rolling(20).mean() * 0.970878
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc055_5d_base_v055_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc055_5d_base_v055_signal

def f204r_f204_revenue_growth_relative_to_equity_calc056_21d_base_v056_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(36).std().rolling(27).var().rolling(26).min() * 0.392578
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc056_21d_base_v056_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc056_21d_base_v056_signal

def f204r_f204_revenue_growth_relative_to_equity_calc057_84d_base_v057_signal(revenue, equity):
    res = (revenue.diff(2) / (equity.shift(3) + 3.4592)).rolling(25).min().rolling(44).var().pct_change(39).rolling(24).min() * 0.150841
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc057_84d_base_v057_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc057_84d_base_v057_signal

def f204r_f204_revenue_growth_relative_to_equity_calc058_126d_base_v058_signal(revenue, equity):
    res = (revenue * 1.0565 - equity).rolling(6).std().rolling(16).mean().rolling(35).min() * 0.708962
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc058_126d_base_v058_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc058_126d_base_v058_signal

def f204r_f204_revenue_growth_relative_to_equity_calc059_42d_base_v059_signal(revenue, equity):
    res = (revenue / (equity + 9.3289)).rolling(45).var().rolling(31).mean().rolling(22).max().pct_change(3) * 0.145426
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc059_42d_base_v059_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc059_42d_base_v059_signal

def f204r_f204_revenue_growth_relative_to_equity_calc060_10d_base_v060_signal(revenue, equity):
    res = (equity / (revenue + 9.1291)).rolling(35).mean().rolling(23).std().rolling(4).min().pct_change(4) * 0.220111
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc060_10d_base_v060_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc060_10d_base_v060_signal

def f204r_f204_revenue_growth_relative_to_equity_calc061_63d_base_v061_signal(revenue, equity):
    res = (revenue * 9.4925 - equity).diff(43).pct_change(12).rolling(49).min() * 0.154882
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc061_63d_base_v061_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc061_63d_base_v061_signal

def f204r_f204_revenue_growth_relative_to_equity_calc062_42d_base_v062_signal(revenue, equity):
    res = (equity / (revenue + 6.8416)).rolling(49).std().rolling(4).var() * 0.546511
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc062_42d_base_v062_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc062_42d_base_v062_signal

def f204r_f204_revenue_growth_relative_to_equity_calc063_126d_base_v063_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(44).std().pct_change(6).rolling(48).max() * 0.109852
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc063_126d_base_v063_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc063_126d_base_v063_signal

def f204r_f204_revenue_growth_relative_to_equity_calc064_200d_base_v064_signal(revenue, equity):
    res = (equity / (revenue + 7.9198)).rolling(7).var().rolling(41).var().rolling(26).std().rolling(18).min() * 0.523374
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc064_200d_base_v064_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc064_200d_base_v064_signal

def f204r_f204_revenue_growth_relative_to_equity_calc065_150d_base_v065_signal(revenue, equity):
    res = (revenue / (equity + 2.0251)).rolling(50).std().rolling(29).std().rolling(32).min() * 0.549815
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc065_150d_base_v065_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc065_150d_base_v065_signal

def f204r_f204_revenue_growth_relative_to_equity_calc066_126d_base_v066_signal(revenue, equity):
    res = (equity / (revenue + 0.1351)).rolling(37).var().rolling(5).std().rolling(11).min().rolling(32).min() * 0.820221
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc066_126d_base_v066_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc066_126d_base_v066_signal

def f204r_f204_revenue_growth_relative_to_equity_calc067_126d_base_v067_signal(revenue, equity):
    res = (revenue / (equity + 8.4768)).pct_change(12).rolling(28).std().rolling(33).var() * 0.144389
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc067_126d_base_v067_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc067_126d_base_v067_signal

def f204r_f204_revenue_growth_relative_to_equity_calc068_63d_base_v068_signal(revenue, equity):
    res = (revenue.diff(4) / (equity.shift(4) + 9.8319)).rolling(22).var().rolling(23).max() * 0.644228
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc068_63d_base_v068_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc068_63d_base_v068_signal

def f204r_f204_revenue_growth_relative_to_equity_calc069_10d_base_v069_signal(revenue, equity):
    res = (revenue / (equity + 5.0863)).rolling(32).max().rolling(50).var() * 0.917714
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc069_10d_base_v069_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc069_10d_base_v069_signal

def f204r_f204_revenue_growth_relative_to_equity_calc070_5d_base_v070_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(12).rolling(10).min().rolling(7).mean() * 0.901328
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc070_5d_base_v070_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc070_5d_base_v070_signal

def f204r_f204_revenue_growth_relative_to_equity_calc071_5d_base_v071_signal(revenue, equity):
    res = (equity / (revenue + 9.7740)).rolling(14).max().rolling(13).std().diff(14) * 0.239812
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc071_5d_base_v071_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc071_5d_base_v071_signal

def f204r_f204_revenue_growth_relative_to_equity_calc072_126d_base_v072_signal(revenue, equity):
    res = (revenue * 4.1931 - equity).rolling(9).max().pct_change(24).rolling(28).var() * 0.891813
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc072_126d_base_v072_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc072_126d_base_v072_signal

def f204r_f204_revenue_growth_relative_to_equity_calc073_84d_base_v073_signal(revenue, equity):
    res = (equity / (revenue + 2.7514)).pct_change(26).diff(26).pct_change(42) * 0.328825
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc073_84d_base_v073_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc073_84d_base_v073_signal

def f204r_f204_revenue_growth_relative_to_equity_calc074_150d_base_v074_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(19).diff(5).diff(43) * 0.362935
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc074_150d_base_v074_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc074_150d_base_v074_signal

def f204r_f204_revenue_growth_relative_to_equity_calc075_150d_base_v075_signal(revenue, equity):
    res = (revenue * 3.2125 - equity).diff(39).rolling(7).mean().rolling(19).max() * 0.075320
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc075_150d_base_v075_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc075_150d_base_v075_signal


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
