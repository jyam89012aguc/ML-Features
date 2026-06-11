import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_21d_base_v001_signal(ncfo, liabilities):
    res = (ncfo.diff(10) / (liabilities.shift(5) + 7.6147)).diff(39).rolling(34).var().rolling(2).min().rolling(36).var() * 0.992721
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_21d_base_v001_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_21d_base_v001_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_105d_base_v002_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(6).rolling(13).min() * 0.749410
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_105d_base_v002_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_105d_base_v002_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_10d_base_v003_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 0.4793)).pct_change(30).diff(43).pct_change(37) * 0.424041
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_10d_base_v003_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_10d_base_v003_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_10d_base_v004_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 9.8881)).rolling(13).min().rolling(32).min().rolling(45).max() * 0.699454
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_10d_base_v004_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_10d_base_v004_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_63d_base_v005_signal(ncfo, liabilities):
    res = (ncfo.diff(3) / (liabilities.shift(2) + 1.1889)).rolling(38).min().rolling(32).max() * 0.697919
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_63d_base_v005_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_63d_base_v005_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_21d_base_v006_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.4703)).rolling(22).std().rolling(21).mean().rolling(24).var() * 0.695288
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_21d_base_v006_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_21d_base_v006_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_126d_base_v007_signal(ncfo, liabilities):
    res = (ncfo.diff(9) / (liabilities.shift(3) + 3.4246)).rolling(9).min().rolling(33).min() * 0.617546
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_126d_base_v007_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_126d_base_v007_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_21d_base_v008_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 0.3515)).rolling(36).std().rolling(9).std().rolling(9).var() * 0.435774
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_21d_base_v008_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_21d_base_v008_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_84d_base_v009_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 1.9157)).pct_change(36).rolling(38).mean().rolling(47).mean().rolling(42).min() * 0.214860
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_84d_base_v009_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_84d_base_v009_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_252d_base_v010_signal(ncfo, liabilities):
    res = (ncfo * 7.7454 - liabilities).rolling(35).min().rolling(42).var().rolling(45).var() * 0.245400
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_252d_base_v010_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_252d_base_v010_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_126d_base_v011_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(8).max().rolling(41).max().rolling(9).min() * 0.490037
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_126d_base_v011_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_126d_base_v011_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_5d_base_v012_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(31).min().rolling(42).std().rolling(32).std().pct_change(30) * 0.044799
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_5d_base_v012_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_5d_base_v012_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_200d_base_v013_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(48).var().rolling(43).std().rolling(3).std().rolling(39).std() * 0.724498
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_200d_base_v013_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_200d_base_v013_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_42d_base_v014_signal(ncfo, liabilities):
    res = (ncfo * 9.4680 - liabilities).pct_change(45).diff(17) * 0.908841
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_42d_base_v014_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_42d_base_v014_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_252d_base_v015_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 6.6970)).rolling(21).min().rolling(35).min().pct_change(45).rolling(45).min() * 0.219828
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_252d_base_v015_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_252d_base_v015_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_21d_base_v016_signal(ncfo, liabilities):
    res = (ncfo.diff(3) / (liabilities.shift(4) + 4.3992)).rolling(44).var().pct_change(9).diff(38) * 0.435357
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_21d_base_v016_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_21d_base_v016_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_21d_base_v017_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(32).min().rolling(28).std().rolling(16).mean() * 0.728926
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_21d_base_v017_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_21d_base_v017_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_150d_base_v018_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 5.3383)).rolling(26).max().rolling(47).std() * 0.293654
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_150d_base_v018_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_150d_base_v018_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_21d_base_v019_signal(ncfo, liabilities):
    res = (ncfo * 8.6899 - liabilities).rolling(8).mean().rolling(23).mean().pct_change(16).rolling(15).mean() * 0.669063
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_21d_base_v019_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_21d_base_v019_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_21d_base_v020_signal(ncfo, liabilities):
    res = (ncfo * 6.7115 - liabilities).rolling(22).max().pct_change(32).rolling(31).mean() * 0.660902
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_21d_base_v020_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_21d_base_v020_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_200d_base_v021_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(26).std().rolling(46).mean().rolling(38).std() * 0.413429
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_200d_base_v021_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_200d_base_v021_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_150d_base_v022_signal(ncfo, liabilities):
    res = (ncfo * 3.0018 - liabilities).rolling(34).var().rolling(22).var().rolling(47).mean() * 0.673432
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_150d_base_v022_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_150d_base_v022_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_252d_base_v023_signal(ncfo, liabilities):
    res = (ncfo.diff(2) / (liabilities.shift(1) + 0.4120)).rolling(38).max().rolling(23).max().diff(41) * 0.929879
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_252d_base_v023_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_252d_base_v023_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_42d_base_v024_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 7.1759)).diff(6).pct_change(40).diff(35).rolling(45).mean() * 0.794501
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_42d_base_v024_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_42d_base_v024_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_42d_base_v025_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(43).min().rolling(23).std().rolling(23).std().rolling(16).std() * 0.115716
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_42d_base_v025_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_42d_base_v025_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_105d_base_v026_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 7.6828)).rolling(44).std().rolling(3).var().rolling(43).min() * 0.362436
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_105d_base_v026_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_105d_base_v026_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_105d_base_v027_signal(ncfo, liabilities):
    res = (ncfo.diff(3) / (liabilities.shift(1) + 8.4718)).rolling(3).var().rolling(9).std() * 0.034677
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_105d_base_v027_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_105d_base_v027_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_5d_base_v028_signal(ncfo, liabilities):
    res = (ncfo * 8.3036 - liabilities).rolling(43).min().rolling(24).max().rolling(20).std().diff(33) * 0.444359
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_5d_base_v028_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_5d_base_v028_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_126d_base_v029_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(14).pct_change(50).rolling(36).var() * 0.758328
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_126d_base_v029_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_126d_base_v029_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_63d_base_v030_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(22).diff(13) * 0.679912
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_63d_base_v030_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_63d_base_v030_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_105d_base_v031_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 1.5087)).rolling(13).min().rolling(9).min().rolling(13).var().pct_change(37) * 0.478476
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_105d_base_v031_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_105d_base_v031_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_5d_base_v032_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(28).rolling(13).std() * 0.911572
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_5d_base_v032_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_5d_base_v032_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_200d_base_v033_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(35).var().rolling(50).var().diff(24).rolling(35).var() * 0.313526
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_200d_base_v033_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_200d_base_v033_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_42d_base_v034_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(14).rolling(48).mean().pct_change(46) * 0.997741
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_42d_base_v034_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_42d_base_v034_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_63d_base_v035_signal(ncfo, liabilities):
    res = (ncfo.diff(4) / (liabilities.shift(5) + 8.0141)).rolling(44).std().rolling(25).mean().rolling(26).min() * 0.865850
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_63d_base_v035_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_63d_base_v035_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_200d_base_v036_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(14).max().rolling(23).mean().pct_change(41) * 0.333421
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_200d_base_v036_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_200d_base_v036_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_150d_base_v037_signal(ncfo, liabilities):
    res = (ncfo.diff(5) / (liabilities.shift(4) + 8.1040)).diff(33).diff(48).pct_change(26) * 0.948358
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_150d_base_v037_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_150d_base_v037_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_150d_base_v038_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(5).var().rolling(48).max() * 0.058624
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_150d_base_v038_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_150d_base_v038_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_200d_base_v039_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 5.9113)).rolling(25).std().diff(12) * 0.056960
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_200d_base_v039_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_200d_base_v039_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_84d_base_v040_signal(ncfo, liabilities):
    res = (ncfo.diff(2) / (liabilities.shift(2) + 3.5569)).pct_change(36).rolling(16).var() * 0.430456
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_84d_base_v040_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_84d_base_v040_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_10d_base_v041_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 5.7626)).rolling(39).var().rolling(11).std().rolling(11).mean() * 0.375392
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_10d_base_v041_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_10d_base_v041_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_150d_base_v042_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 6.8643)).rolling(17).std().pct_change(37) * 0.195411
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_150d_base_v042_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_150d_base_v042_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_252d_base_v043_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 9.8565)).rolling(16).std().rolling(24).max() * 0.155748
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_252d_base_v043_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_252d_base_v043_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_63d_base_v044_signal(ncfo, liabilities):
    res = (ncfo.diff(10) / (liabilities.shift(1) + 7.8309)).diff(39).rolling(16).std().diff(33) * 0.189803
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_63d_base_v044_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_63d_base_v044_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_252d_base_v045_signal(ncfo, liabilities):
    res = (ncfo * 9.2549 - liabilities).diff(23).pct_change(8).rolling(13).std().diff(41) * 0.603160
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_252d_base_v045_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_252d_base_v045_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_63d_base_v046_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 1.6353)).pct_change(36).diff(26) * 0.084796
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_63d_base_v046_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_63d_base_v046_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_150d_base_v047_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(40).pct_change(9) * 0.856886
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_150d_base_v047_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_150d_base_v047_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_42d_base_v048_signal(ncfo, liabilities):
    res = (ncfo.diff(8) / (liabilities.shift(2) + 6.1728)).rolling(47).max().rolling(22).mean().rolling(34).var().rolling(32).min() * 0.637198
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_42d_base_v048_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_42d_base_v048_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_10d_base_v049_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 1.2895)).diff(8).diff(36).rolling(48).max().diff(43) * 0.527835
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_10d_base_v049_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_10d_base_v049_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_5d_base_v050_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 6.1508)).pct_change(49).pct_change(13).diff(10) * 0.475763
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_5d_base_v050_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_5d_base_v050_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_150d_base_v051_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 6.6979)).rolling(35).mean().diff(16) * 0.444258
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_150d_base_v051_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_150d_base_v051_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_21d_base_v052_signal(ncfo, liabilities):
    res = (ncfo.diff(5) / (liabilities.shift(1) + 7.4527)).rolling(47).mean().rolling(38).mean() * 0.802867
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_21d_base_v052_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_21d_base_v052_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_252d_base_v053_signal(ncfo, liabilities):
    res = (ncfo.diff(3) / (liabilities.shift(4) + 6.3478)).rolling(19).var().rolling(39).max() * 0.561609
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_252d_base_v053_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_252d_base_v053_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_5d_base_v054_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 6.6017)).rolling(50).max().rolling(15).min().rolling(7).std() * 0.964765
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_5d_base_v054_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_5d_base_v054_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_150d_base_v055_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(7).min().pct_change(42) * 0.644722
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_150d_base_v055_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_150d_base_v055_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_200d_base_v056_signal(ncfo, liabilities):
    res = (ncfo * 2.0105 - liabilities).pct_change(19).rolling(25).min() * 0.720308
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_200d_base_v056_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_200d_base_v056_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_21d_base_v057_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 9.4713)).rolling(32).min().rolling(43).var().rolling(7).var().pct_change(36) * 0.116360
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_21d_base_v057_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_21d_base_v057_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_200d_base_v058_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 9.1886)).rolling(30).var().rolling(14).mean() * 0.481003
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_200d_base_v058_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_200d_base_v058_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_84d_base_v059_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 9.4917)).diff(32).rolling(26).var() * 0.033182
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_84d_base_v059_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_84d_base_v059_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_84d_base_v060_signal(ncfo, liabilities):
    res = (ncfo.diff(2) / (liabilities.shift(3) + 0.6856)).rolling(15).std().rolling(31).var().rolling(21).std().diff(32) * 0.276008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_84d_base_v060_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_84d_base_v060_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_21d_base_v061_signal(ncfo, liabilities):
    res = (ncfo.diff(9) / (liabilities.shift(2) + 1.3020)).rolling(40).min().rolling(42).max().rolling(46).min().rolling(3).max() * 0.901767
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_21d_base_v061_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_21d_base_v061_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_84d_base_v062_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(31).rolling(2).min().diff(31).rolling(20).max() * 0.281882
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_84d_base_v062_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_84d_base_v062_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_63d_base_v063_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 7.3731)).rolling(30).max().pct_change(27).rolling(23).min() * 0.985043
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_63d_base_v063_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_63d_base_v063_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_21d_base_v064_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(13).max().rolling(8).max() * 0.939866
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_21d_base_v064_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_21d_base_v064_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_150d_base_v065_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(39).mean().rolling(8).std().rolling(24).min().pct_change(37) * 0.209284
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_150d_base_v065_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_150d_base_v065_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_10d_base_v066_signal(ncfo, liabilities):
    res = (ncfo * 7.6440 - liabilities).rolling(25).max().rolling(44).mean().rolling(2).min().rolling(42).min() * 0.759041
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_10d_base_v066_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_10d_base_v066_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_63d_base_v067_signal(ncfo, liabilities):
    res = (ncfo.diff(2) / (liabilities.shift(5) + 4.2063)).rolling(45).min().rolling(41).std().pct_change(19).pct_change(38) * 0.765342
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_63d_base_v067_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_63d_base_v067_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_126d_base_v068_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(50).var().rolling(25).mean().rolling(7).std() * 0.918626
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_126d_base_v068_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_126d_base_v068_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_105d_base_v069_signal(ncfo, liabilities):
    res = (ncfo.diff(10) / (liabilities.shift(2) + 8.9948)).rolling(22).min().rolling(20).max() * 0.336551
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_105d_base_v069_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_105d_base_v069_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_150d_base_v070_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 4.6425)).diff(49).rolling(22).mean() * 0.300218
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_150d_base_v070_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_150d_base_v070_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_84d_base_v071_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 8.9439)).rolling(48).std().rolling(40).var() * 0.237017
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_84d_base_v071_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_84d_base_v071_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_252d_base_v072_signal(ncfo, liabilities):
    res = (ncfo * 8.7917 - liabilities).rolling(39).min().rolling(19).min().rolling(31).max().rolling(31).var() * 0.927194
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_252d_base_v072_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_252d_base_v072_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_42d_base_v073_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(46).diff(40) * 0.141153
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_42d_base_v073_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_42d_base_v073_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_105d_base_v074_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 3.8982)).rolling(32).var().rolling(41).max().pct_change(23) * 0.784632
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_105d_base_v074_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_105d_base_v074_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_10d_base_v075_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 5.3164)).rolling(31).var().diff(3).pct_change(27).rolling(3).min() * 0.053098
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_10d_base_v075_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_10d_base_v075_signal


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
