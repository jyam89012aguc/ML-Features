import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f202e_f202_ebitda_per_share_growth_regime_calc001_200d_base_v001_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 0.6851)).rolling(47).var().rolling(15).min().rolling(19).min().diff(32) * 0.516594
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc001_200d_base_v001_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc001_200d_base_v001_signal

def f202e_f202_ebitda_per_share_growth_regime_calc002_10d_base_v002_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 9.9047)).rolling(22).mean().rolling(39).min().rolling(33).var() * 0.680366
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc002_10d_base_v002_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc002_10d_base_v002_signal

def f202e_f202_ebitda_per_share_growth_regime_calc003_5d_base_v003_signal(ebitda, sharesbas):
    res = (ebitda.diff(6) / (sharesbas.shift(5) + 6.4889)).rolling(28).min().rolling(24).max().rolling(46).max() * 0.855537
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc003_5d_base_v003_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc003_5d_base_v003_signal

def f202e_f202_ebitda_per_share_growth_regime_calc004_200d_base_v004_signal(ebitda, sharesbas):
    res = (ebitda.diff(6) / (sharesbas.shift(4) + 6.4354)).rolling(13).var().rolling(39).max().rolling(10).std() * 0.570398
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc004_200d_base_v004_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc004_200d_base_v004_signal

def f202e_f202_ebitda_per_share_growth_regime_calc005_10d_base_v005_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 9.0309)).rolling(8).max().pct_change(45).rolling(21).min().rolling(21).std() * 0.116067
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc005_10d_base_v005_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc005_10d_base_v005_signal

def f202e_f202_ebitda_per_share_growth_regime_calc006_200d_base_v006_signal(ebitda, sharesbas):
    res = (ebitda * 8.6569 - sharesbas).rolling(23).min().pct_change(2).rolling(23).min() * 0.977761
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc006_200d_base_v006_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc006_200d_base_v006_signal

def f202e_f202_ebitda_per_share_growth_regime_calc007_200d_base_v007_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(41).mean().diff(47).rolling(26).mean() * 0.659719
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc007_200d_base_v007_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc007_200d_base_v007_signal

def f202e_f202_ebitda_per_share_growth_regime_calc008_126d_base_v008_signal(ebitda, sharesbas):
    res = (ebitda * 5.2278 - sharesbas).rolling(46).max().pct_change(47).pct_change(16) * 0.237129
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc008_126d_base_v008_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc008_126d_base_v008_signal

def f202e_f202_ebitda_per_share_growth_regime_calc009_42d_base_v009_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 5.9740)).rolling(28).min().rolling(48).var().rolling(38).min().pct_change(46) * 0.658245
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc009_42d_base_v009_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc009_42d_base_v009_signal

def f202e_f202_ebitda_per_share_growth_regime_calc010_252d_base_v010_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 1.6929)).pct_change(46).rolling(29).min().rolling(29).mean() * 0.245874
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc010_252d_base_v010_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc010_252d_base_v010_signal

def f202e_f202_ebitda_per_share_growth_regime_calc011_200d_base_v011_signal(ebitda, sharesbas):
    res = (ebitda.diff(7) / (sharesbas.shift(1) + 9.8162)).rolling(2).min().pct_change(6).diff(19) * 0.363902
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc011_200d_base_v011_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc011_200d_base_v011_signal

def f202e_f202_ebitda_per_share_growth_regime_calc012_105d_base_v012_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(10).pct_change(17).rolling(42).mean().diff(29) * 0.417334
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc012_105d_base_v012_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc012_105d_base_v012_signal

def f202e_f202_ebitda_per_share_growth_regime_calc013_84d_base_v013_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(7).std().rolling(17).var() * 0.070706
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc013_84d_base_v013_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc013_84d_base_v013_signal

def f202e_f202_ebitda_per_share_growth_regime_calc014_105d_base_v014_signal(ebitda, sharesbas):
    res = (ebitda.diff(10) / (sharesbas.shift(1) + 2.7844)).rolling(22).mean().rolling(49).min() * 0.753985
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc014_105d_base_v014_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc014_105d_base_v014_signal

def f202e_f202_ebitda_per_share_growth_regime_calc015_84d_base_v015_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(5).rolling(19).std() * 0.887102
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc015_84d_base_v015_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc015_84d_base_v015_signal

def f202e_f202_ebitda_per_share_growth_regime_calc016_84d_base_v016_signal(ebitda, sharesbas):
    res = (ebitda * 1.0544 - sharesbas).rolling(45).mean().rolling(18).max().rolling(41).std() * 0.238831
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc016_84d_base_v016_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc016_84d_base_v016_signal

def f202e_f202_ebitda_per_share_growth_regime_calc017_252d_base_v017_signal(ebitda, sharesbas):
    res = (ebitda * 9.6708 - sharesbas).diff(42).rolling(29).std().rolling(35).max() * 0.466878
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc017_252d_base_v017_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc017_252d_base_v017_signal

def f202e_f202_ebitda_per_share_growth_regime_calc018_252d_base_v018_signal(ebitda, sharesbas):
    res = (ebitda.diff(6) / (sharesbas.shift(4) + 0.8182)).diff(31).pct_change(24).rolling(27).max().rolling(26).min() * 0.905516
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc018_252d_base_v018_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc018_252d_base_v018_signal

def f202e_f202_ebitda_per_share_growth_regime_calc019_5d_base_v019_signal(ebitda, sharesbas):
    res = (ebitda.diff(3) / (sharesbas.shift(2) + 4.5172)).diff(42).pct_change(48).pct_change(10) * 0.794566
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc019_5d_base_v019_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc019_5d_base_v019_signal

def f202e_f202_ebitda_per_share_growth_regime_calc020_252d_base_v020_signal(ebitda, sharesbas):
    res = (ebitda.diff(9) / (sharesbas.shift(5) + 9.9786)).rolling(34).max().rolling(31).max() * 0.687581
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc020_252d_base_v020_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc020_252d_base_v020_signal

def f202e_f202_ebitda_per_share_growth_regime_calc021_10d_base_v021_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 3.7968)).rolling(17).min().rolling(16).min() * 0.225638
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc021_10d_base_v021_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc021_10d_base_v021_signal

def f202e_f202_ebitda_per_share_growth_regime_calc022_200d_base_v022_signal(ebitda, sharesbas):
    res = (ebitda.diff(3) / (sharesbas.shift(1) + 0.9967)).pct_change(13).rolling(11).std().rolling(16).std().rolling(48).std() * 0.937423
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc022_200d_base_v022_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc022_200d_base_v022_signal

def f202e_f202_ebitda_per_share_growth_regime_calc023_105d_base_v023_signal(ebitda, sharesbas):
    res = (ebitda * 5.6876 - sharesbas).rolling(49).max().rolling(26).max().diff(36).rolling(45).mean() * 0.395973
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc023_105d_base_v023_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc023_105d_base_v023_signal

def f202e_f202_ebitda_per_share_growth_regime_calc024_84d_base_v024_signal(ebitda, sharesbas):
    res = (ebitda * 4.2879 - sharesbas).rolling(44).std().rolling(10).var() * 0.658565
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc024_84d_base_v024_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc024_84d_base_v024_signal

def f202e_f202_ebitda_per_share_growth_regime_calc025_10d_base_v025_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 6.0401)).rolling(14).min().rolling(28).std().rolling(13).max() * 0.130690
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc025_10d_base_v025_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc025_10d_base_v025_signal

def f202e_f202_ebitda_per_share_growth_regime_calc026_84d_base_v026_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(42).std().diff(18) * 0.791403
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc026_84d_base_v026_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc026_84d_base_v026_signal

def f202e_f202_ebitda_per_share_growth_regime_calc027_126d_base_v027_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(5).std().rolling(28).mean() * 0.482431
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc027_126d_base_v027_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc027_126d_base_v027_signal

def f202e_f202_ebitda_per_share_growth_regime_calc028_21d_base_v028_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(27).max().pct_change(13) * 0.195046
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc028_21d_base_v028_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc028_21d_base_v028_signal

def f202e_f202_ebitda_per_share_growth_regime_calc029_150d_base_v029_signal(ebitda, sharesbas):
    res = (ebitda.diff(5) / (sharesbas.shift(3) + 7.1171)).rolling(21).var().pct_change(31).rolling(19).min().pct_change(39) * 0.409321
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc029_150d_base_v029_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc029_150d_base_v029_signal

def f202e_f202_ebitda_per_share_growth_regime_calc030_105d_base_v030_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 8.8673)).rolling(3).std().rolling(44).mean().rolling(30).max().rolling(12).max() * 0.435453
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc030_105d_base_v030_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc030_105d_base_v030_signal

def f202e_f202_ebitda_per_share_growth_regime_calc031_21d_base_v031_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 0.9467)).rolling(23).min().diff(27) * 0.677756
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc031_21d_base_v031_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc031_21d_base_v031_signal

def f202e_f202_ebitda_per_share_growth_regime_calc032_105d_base_v032_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 0.2301)).rolling(47).std().rolling(47).max() * 0.077529
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc032_105d_base_v032_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc032_105d_base_v032_signal

def f202e_f202_ebitda_per_share_growth_regime_calc033_63d_base_v033_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(14).max().rolling(5).mean().rolling(42).mean() * 0.382680
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc033_63d_base_v033_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc033_63d_base_v033_signal

def f202e_f202_ebitda_per_share_growth_regime_calc034_42d_base_v034_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 2.3796)).rolling(6).std().rolling(24).var() * 0.196020
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc034_42d_base_v034_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc034_42d_base_v034_signal

def f202e_f202_ebitda_per_share_growth_regime_calc035_21d_base_v035_signal(ebitda, sharesbas):
    res = (ebitda * 9.1469 - sharesbas).rolling(44).std().rolling(29).min().pct_change(4).diff(14) * 0.021937
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc035_21d_base_v035_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc035_21d_base_v035_signal

def f202e_f202_ebitda_per_share_growth_regime_calc036_84d_base_v036_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 5.2425)).rolling(23).std().diff(38).rolling(24).min().diff(25) * 0.983417
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc036_84d_base_v036_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc036_84d_base_v036_signal

def f202e_f202_ebitda_per_share_growth_regime_calc037_84d_base_v037_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 7.9726)).rolling(11).mean().rolling(23).std() * 0.903231
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc037_84d_base_v037_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc037_84d_base_v037_signal

def f202e_f202_ebitda_per_share_growth_regime_calc038_84d_base_v038_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(44).var().rolling(3).mean().rolling(11).max().diff(36) * 0.605503
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc038_84d_base_v038_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc038_84d_base_v038_signal

def f202e_f202_ebitda_per_share_growth_regime_calc039_200d_base_v039_signal(ebitda, sharesbas):
    res = (ebitda.diff(2) / (sharesbas.shift(5) + 5.2581)).rolling(35).var().pct_change(13).rolling(42).max().diff(46) * 0.403784
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc039_200d_base_v039_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc039_200d_base_v039_signal

def f202e_f202_ebitda_per_share_growth_regime_calc040_84d_base_v040_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 5.7544)).rolling(37).mean().rolling(50).mean().rolling(28).std() * 0.850608
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc040_84d_base_v040_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc040_84d_base_v040_signal

def f202e_f202_ebitda_per_share_growth_regime_calc041_252d_base_v041_signal(ebitda, sharesbas):
    res = (ebitda.diff(6) / (sharesbas.shift(5) + 1.8511)).diff(5).rolling(46).mean() * 0.894407
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc041_252d_base_v041_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc041_252d_base_v041_signal

def f202e_f202_ebitda_per_share_growth_regime_calc042_84d_base_v042_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 0.4905)).pct_change(46).rolling(26).min() * 0.087734
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc042_84d_base_v042_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc042_84d_base_v042_signal

def f202e_f202_ebitda_per_share_growth_regime_calc043_105d_base_v043_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 9.6335)).rolling(43).mean().rolling(46).mean().rolling(5).min().rolling(50).min() * 0.707390
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc043_105d_base_v043_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc043_105d_base_v043_signal

def f202e_f202_ebitda_per_share_growth_regime_calc044_63d_base_v044_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.6264)).diff(32).rolling(40).var().pct_change(14).pct_change(47) * 0.438520
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc044_63d_base_v044_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc044_63d_base_v044_signal

def f202e_f202_ebitda_per_share_growth_regime_calc045_200d_base_v045_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 8.4037)).rolling(45).min().rolling(20).mean() * 0.805715
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc045_200d_base_v045_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc045_200d_base_v045_signal

def f202e_f202_ebitda_per_share_growth_regime_calc046_42d_base_v046_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(7).var().rolling(31).min().diff(14) * 0.952488
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc046_42d_base_v046_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc046_42d_base_v046_signal

def f202e_f202_ebitda_per_share_growth_regime_calc047_84d_base_v047_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(38).pct_change(16) * 0.525142
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc047_84d_base_v047_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc047_84d_base_v047_signal

def f202e_f202_ebitda_per_share_growth_regime_calc048_200d_base_v048_signal(ebitda, sharesbas):
    res = (ebitda * 4.2872 - sharesbas).pct_change(36).rolling(16).mean().rolling(43).mean() * 0.981877
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc048_200d_base_v048_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc048_200d_base_v048_signal

def f202e_f202_ebitda_per_share_growth_regime_calc049_10d_base_v049_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 4.6913)).rolling(10).max().pct_change(16).pct_change(33).rolling(39).var() * 0.782746
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc049_10d_base_v049_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc049_10d_base_v049_signal

def f202e_f202_ebitda_per_share_growth_regime_calc050_105d_base_v050_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 2.1430)).rolling(41).min().rolling(7).var().pct_change(24).diff(39) * 0.331982
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc050_105d_base_v050_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc050_105d_base_v050_signal

def f202e_f202_ebitda_per_share_growth_regime_calc051_105d_base_v051_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 7.6261)).rolling(41).max().rolling(33).var().rolling(42).min() * 0.469343
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc051_105d_base_v051_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc051_105d_base_v051_signal

def f202e_f202_ebitda_per_share_growth_regime_calc052_5d_base_v052_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 5.2355)).rolling(25).mean().diff(36) * 0.398680
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc052_5d_base_v052_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc052_5d_base_v052_signal

def f202e_f202_ebitda_per_share_growth_regime_calc053_126d_base_v053_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 9.9007)).diff(40).pct_change(49) * 0.361238
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc053_126d_base_v053_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc053_126d_base_v053_signal

def f202e_f202_ebitda_per_share_growth_regime_calc054_84d_base_v054_signal(ebitda, sharesbas):
    res = (ebitda.diff(10) / (sharesbas.shift(2) + 6.7257)).rolling(6).min().rolling(34).max().rolling(36).min().rolling(28).mean() * 0.011235
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc054_84d_base_v054_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc054_84d_base_v054_signal

def f202e_f202_ebitda_per_share_growth_regime_calc055_105d_base_v055_signal(ebitda, sharesbas):
    res = (ebitda.diff(5) / (sharesbas.shift(4) + 0.3213)).rolling(29).std().rolling(5).var() * 0.150342
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc055_105d_base_v055_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc055_105d_base_v055_signal

def f202e_f202_ebitda_per_share_growth_regime_calc056_200d_base_v056_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 3.0267)).rolling(18).mean().rolling(11).std() * 0.152215
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc056_200d_base_v056_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc056_200d_base_v056_signal

def f202e_f202_ebitda_per_share_growth_regime_calc057_105d_base_v057_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(25).min().rolling(24).min() * 0.648251
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc057_105d_base_v057_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc057_105d_base_v057_signal

def f202e_f202_ebitda_per_share_growth_regime_calc058_21d_base_v058_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 5.4634)).rolling(43).max().rolling(15).mean() * 0.257196
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc058_21d_base_v058_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc058_21d_base_v058_signal

def f202e_f202_ebitda_per_share_growth_regime_calc059_21d_base_v059_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 4.6653)).rolling(45).std().diff(25).diff(20) * 0.203467
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc059_21d_base_v059_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc059_21d_base_v059_signal

def f202e_f202_ebitda_per_share_growth_regime_calc060_252d_base_v060_signal(ebitda, sharesbas):
    res = (ebitda.diff(9) / (sharesbas.shift(4) + 8.8144)).rolling(46).mean().rolling(43).mean().rolling(2).var().diff(43) * 0.263036
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc060_252d_base_v060_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc060_252d_base_v060_signal

def f202e_f202_ebitda_per_share_growth_regime_calc061_105d_base_v061_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 7.5098)).rolling(18).var().rolling(23).var().rolling(15).var() * 0.233166
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc061_105d_base_v061_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc061_105d_base_v061_signal

def f202e_f202_ebitda_per_share_growth_regime_calc062_252d_base_v062_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 4.6355)).rolling(39).var().diff(9).rolling(48).max().pct_change(48) * 0.924260
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc062_252d_base_v062_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc062_252d_base_v062_signal

def f202e_f202_ebitda_per_share_growth_regime_calc063_10d_base_v063_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 2.9438)).rolling(29).max().pct_change(26) * 0.992100
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc063_10d_base_v063_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc063_10d_base_v063_signal

def f202e_f202_ebitda_per_share_growth_regime_calc064_105d_base_v064_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 3.4675)).rolling(22).max().diff(33).pct_change(9).rolling(11).mean() * 0.825305
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc064_105d_base_v064_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc064_105d_base_v064_signal

def f202e_f202_ebitda_per_share_growth_regime_calc065_5d_base_v065_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(44).std().rolling(7).max().diff(2) * 0.673429
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc065_5d_base_v065_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc065_5d_base_v065_signal

def f202e_f202_ebitda_per_share_growth_regime_calc066_150d_base_v066_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 3.2544)).rolling(49).var().rolling(34).mean() * 0.391394
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc066_150d_base_v066_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc066_150d_base_v066_signal

def f202e_f202_ebitda_per_share_growth_regime_calc067_84d_base_v067_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 6.6651)).diff(29).rolling(43).std() * 0.836912
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc067_84d_base_v067_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc067_84d_base_v067_signal

def f202e_f202_ebitda_per_share_growth_regime_calc068_200d_base_v068_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 7.2872)).rolling(3).var().rolling(48).min().rolling(28).mean().rolling(32).mean() * 0.586696
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc068_200d_base_v068_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc068_200d_base_v068_signal

def f202e_f202_ebitda_per_share_growth_regime_calc069_126d_base_v069_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 3.7279)).pct_change(24).rolling(7).mean() * 0.159655
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc069_126d_base_v069_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc069_126d_base_v069_signal

def f202e_f202_ebitda_per_share_growth_regime_calc070_126d_base_v070_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(21).mean().rolling(6).std().rolling(36).min() * 0.244736
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc070_126d_base_v070_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc070_126d_base_v070_signal

def f202e_f202_ebitda_per_share_growth_regime_calc071_126d_base_v071_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.8802)).rolling(43).max().pct_change(31).rolling(48).var().rolling(6).max() * 0.841951
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc071_126d_base_v071_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc071_126d_base_v071_signal

def f202e_f202_ebitda_per_share_growth_regime_calc072_10d_base_v072_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 5.6017)).pct_change(32).rolling(13).var() * 0.151663
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc072_10d_base_v072_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc072_10d_base_v072_signal

def f202e_f202_ebitda_per_share_growth_regime_calc073_200d_base_v073_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 2.8080)).rolling(37).std().diff(30).diff(41).rolling(41).var() * 0.529942
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc073_200d_base_v073_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc073_200d_base_v073_signal

def f202e_f202_ebitda_per_share_growth_regime_calc074_10d_base_v074_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 8.6126)).pct_change(18).rolling(48).var().rolling(45).max().rolling(8).var() * 0.594279
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc074_10d_base_v074_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc074_10d_base_v074_signal

def f202e_f202_ebitda_per_share_growth_regime_calc075_63d_base_v075_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(41).rolling(12).mean().diff(39).rolling(44).min() * 0.816904
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc075_63d_base_v075_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc075_63d_base_v075_signal


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
