import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f202e_f202_ebitda_per_share_growth_regime_calc001_5d_slope_v001_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 6.2708)).rolling(37).mean().rolling(16).std() * 0.527010).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc001_5d_slope_v001_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc001_5d_slope_v001_signal

def f202e_f202_ebitda_per_share_growth_regime_calc002_21d_slope_v002_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(24).std().diff(17).rolling(50).var().rolling(46).mean() * 0.467740).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc002_21d_slope_v002_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc002_21d_slope_v002_signal

def f202e_f202_ebitda_per_share_growth_regime_calc003_200d_slope_v003_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.4062)).rolling(6).max().rolling(12).std().rolling(2).std() * 0.924479).diff(7).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc003_200d_slope_v003_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc003_200d_slope_v003_signal

def f202e_f202_ebitda_per_share_growth_regime_calc004_105d_slope_v004_signal(ebitda, sharesbas):
    res = ((ebitda * 9.8772 - sharesbas).rolling(7).std().rolling(32).std() * 0.747190).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc004_105d_slope_v004_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc004_105d_slope_v004_signal

def f202e_f202_ebitda_per_share_growth_regime_calc005_105d_slope_v005_signal(ebitda, sharesbas):
    res = ((ebitda.diff(4) / (sharesbas.shift(5) + 8.1822)).rolling(22).mean().diff(47).diff(45) * 0.283860).diff(12).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc005_105d_slope_v005_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc005_105d_slope_v005_signal

def f202e_f202_ebitda_per_share_growth_regime_calc006_84d_slope_v006_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 5.2864)).rolling(27).mean().rolling(50).std() * 0.694394).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc006_84d_slope_v006_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc006_84d_slope_v006_signal

def f202e_f202_ebitda_per_share_growth_regime_calc007_10d_slope_v007_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 5.3785)).diff(44).rolling(28).mean().rolling(16).mean().pct_change(39) * 0.325053).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc007_10d_slope_v007_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc007_10d_slope_v007_signal

def f202e_f202_ebitda_per_share_growth_regime_calc008_105d_slope_v008_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.7523)).rolling(33).var().rolling(5).min().pct_change(34) * 0.700521).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc008_105d_slope_v008_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc008_105d_slope_v008_signal

def f202e_f202_ebitda_per_share_growth_regime_calc009_10d_slope_v009_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.4606)).rolling(26).mean().rolling(10).var() * 0.791515).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc009_10d_slope_v009_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc009_10d_slope_v009_signal

def f202e_f202_ebitda_per_share_growth_regime_calc010_63d_slope_v010_signal(ebitda, sharesbas):
    res = ((ebitda * 0.3530 - sharesbas).diff(21).diff(3) * 0.494703).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc010_63d_slope_v010_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc010_63d_slope_v010_signal

def f202e_f202_ebitda_per_share_growth_regime_calc011_200d_slope_v011_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(2) + 5.8131)).rolling(2).std().rolling(41).mean() * 0.201861).diff(2).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc011_200d_slope_v011_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc011_200d_slope_v011_signal

def f202e_f202_ebitda_per_share_growth_regime_calc012_252d_slope_v012_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.5783)).rolling(12).mean().rolling(21).var() * 0.841371).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc012_252d_slope_v012_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc012_252d_slope_v012_signal

def f202e_f202_ebitda_per_share_growth_regime_calc013_10d_slope_v013_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(21).std().rolling(40).max() * 0.990698).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc013_10d_slope_v013_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc013_10d_slope_v013_signal

def f202e_f202_ebitda_per_share_growth_regime_calc014_21d_slope_v014_signal(ebitda, sharesbas):
    res = ((ebitda * 3.4676 - sharesbas).rolling(42).max().diff(29).rolling(37).var() * 0.017331).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc014_21d_slope_v014_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc014_21d_slope_v014_signal

def f202e_f202_ebitda_per_share_growth_regime_calc015_63d_slope_v015_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.5706)).rolling(2).var().diff(4).rolling(20).var() * 0.514821).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc015_63d_slope_v015_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc015_63d_slope_v015_signal

def f202e_f202_ebitda_per_share_growth_regime_calc016_84d_slope_v016_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 0.2661)).rolling(38).var().pct_change(24).rolling(49).min().rolling(31).var() * 0.889329).diff(14).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc016_84d_slope_v016_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc016_84d_slope_v016_signal

def f202e_f202_ebitda_per_share_growth_regime_calc017_105d_slope_v017_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 0.9608)).pct_change(43).rolling(32).mean().rolling(21).std() * 0.619947).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc017_105d_slope_v017_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc017_105d_slope_v017_signal

def f202e_f202_ebitda_per_share_growth_regime_calc018_252d_slope_v018_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 3.4687)).rolling(3).std().diff(31).rolling(25).min().rolling(8).std() * 0.888360).diff(19).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc018_252d_slope_v018_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc018_252d_slope_v018_signal

def f202e_f202_ebitda_per_share_growth_regime_calc019_42d_slope_v019_signal(ebitda, sharesbas):
    res = ((ebitda.diff(4) / (sharesbas.shift(2) + 3.8520)).rolling(35).min().pct_change(14) * 0.718762).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc019_42d_slope_v019_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc019_42d_slope_v019_signal

def f202e_f202_ebitda_per_share_growth_regime_calc020_5d_slope_v020_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(1) + 5.8447)).rolling(11).min().rolling(11).min() * 0.011860).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc020_5d_slope_v020_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc020_5d_slope_v020_signal

def f202e_f202_ebitda_per_share_growth_regime_calc021_5d_slope_v021_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 9.1725)).rolling(7).max().rolling(26).max().pct_change(49).diff(12) * 0.024387).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc021_5d_slope_v021_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc021_5d_slope_v021_signal

def f202e_f202_ebitda_per_share_growth_regime_calc022_126d_slope_v022_signal(ebitda, sharesbas):
    res = ((ebitda * 4.7013 - sharesbas).rolling(25).var().rolling(19).std() * 0.055336).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc022_126d_slope_v022_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc022_126d_slope_v022_signal

def f202e_f202_ebitda_per_share_growth_regime_calc023_150d_slope_v023_signal(ebitda, sharesbas):
    res = ((ebitda * 8.5610 - sharesbas).rolling(20).mean().rolling(23).std().pct_change(39).diff(12) * 0.011967).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc023_150d_slope_v023_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc023_150d_slope_v023_signal

def f202e_f202_ebitda_per_share_growth_regime_calc024_150d_slope_v024_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(4) + 1.0218)).rolling(17).min().rolling(40).var().rolling(45).min().rolling(30).var() * 0.882205).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc024_150d_slope_v024_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc024_150d_slope_v024_signal

def f202e_f202_ebitda_per_share_growth_regime_calc025_150d_slope_v025_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 5.8470)).rolling(42).std().rolling(19).std().rolling(23).std() * 0.506868).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc025_150d_slope_v025_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc025_150d_slope_v025_signal

def f202e_f202_ebitda_per_share_growth_regime_calc026_84d_slope_v026_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.0138)).rolling(30).std().rolling(20).max().pct_change(9) * 0.575197).diff(10).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc026_84d_slope_v026_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc026_84d_slope_v026_signal

def f202e_f202_ebitda_per_share_growth_regime_calc027_5d_slope_v027_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(5) + 5.6034)).rolling(46).std().rolling(12).mean().rolling(25).min() * 0.188888).diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc027_5d_slope_v027_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc027_5d_slope_v027_signal

def f202e_f202_ebitda_per_share_growth_regime_calc028_252d_slope_v028_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 0.6140)).pct_change(47).rolling(10).max().pct_change(25) * 0.445953).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc028_252d_slope_v028_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc028_252d_slope_v028_signal

def f202e_f202_ebitda_per_share_growth_regime_calc029_84d_slope_v029_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.0391)).rolling(44).min().rolling(3).var() * 0.639107).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc029_84d_slope_v029_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc029_84d_slope_v029_signal

def f202e_f202_ebitda_per_share_growth_regime_calc030_21d_slope_v030_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(3) + 0.8353)).rolling(47).max().rolling(21).var().rolling(47).max().rolling(10).min() * 0.429610).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc030_21d_slope_v030_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc030_21d_slope_v030_signal

def f202e_f202_ebitda_per_share_growth_regime_calc031_126d_slope_v031_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(6).std().rolling(10).std().diff(43) * 0.370273).diff(19).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc031_126d_slope_v031_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc031_126d_slope_v031_signal

def f202e_f202_ebitda_per_share_growth_regime_calc032_63d_slope_v032_signal(ebitda, sharesbas):
    res = ((ebitda * 7.1143 - sharesbas).rolling(17).var().rolling(42).min().rolling(8).max().rolling(19).var() * 0.759329).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc032_63d_slope_v032_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc032_63d_slope_v032_signal

def f202e_f202_ebitda_per_share_growth_regime_calc033_5d_slope_v033_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(5) + 8.6703)).rolling(8).std().rolling(43).var().rolling(28).min() * 0.874819).diff(15).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc033_5d_slope_v033_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc033_5d_slope_v033_signal

def f202e_f202_ebitda_per_share_growth_regime_calc034_105d_slope_v034_signal(ebitda, sharesbas):
    res = ((ebitda * 6.7450 - sharesbas).rolling(50).std().diff(35).diff(43).rolling(41).std() * 0.449663).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc034_105d_slope_v034_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc034_105d_slope_v034_signal

def f202e_f202_ebitda_per_share_growth_regime_calc035_252d_slope_v035_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(26).mean().rolling(49).min().rolling(5).std().rolling(35).std() * 0.478438).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc035_252d_slope_v035_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc035_252d_slope_v035_signal

def f202e_f202_ebitda_per_share_growth_regime_calc036_10d_slope_v036_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(2) + 1.1648)).rolling(21).min().diff(35).rolling(9).std() * 0.400872).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc036_10d_slope_v036_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc036_10d_slope_v036_signal

def f202e_f202_ebitda_per_share_growth_regime_calc037_63d_slope_v037_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.4710)).rolling(12).max().rolling(32).mean().rolling(12).mean() * 0.415989).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc037_63d_slope_v037_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc037_63d_slope_v037_signal

def f202e_f202_ebitda_per_share_growth_regime_calc038_84d_slope_v038_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 3.1693)).rolling(42).min().diff(4).rolling(29).var() * 0.142092).diff(7).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc038_84d_slope_v038_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc038_84d_slope_v038_signal

def f202e_f202_ebitda_per_share_growth_regime_calc039_63d_slope_v039_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.6308)).rolling(4).min().rolling(45).max() * 0.229466).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc039_63d_slope_v039_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc039_63d_slope_v039_signal

def f202e_f202_ebitda_per_share_growth_regime_calc040_21d_slope_v040_signal(ebitda, sharesbas):
    res = ((ebitda * 4.5233 - sharesbas).rolling(13).mean().rolling(48).min() * 0.731984).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc040_21d_slope_v040_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc040_21d_slope_v040_signal

def f202e_f202_ebitda_per_share_growth_regime_calc041_84d_slope_v041_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.5137)).rolling(11).min().pct_change(36) * 0.235962).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc041_84d_slope_v041_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc041_84d_slope_v041_signal

def f202e_f202_ebitda_per_share_growth_regime_calc042_10d_slope_v042_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(21).min().rolling(34).max().rolling(4).std().rolling(39).min() * 0.172178).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc042_10d_slope_v042_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc042_10d_slope_v042_signal

def f202e_f202_ebitda_per_share_growth_regime_calc043_252d_slope_v043_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(49).rolling(22).max() * 0.418533).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc043_252d_slope_v043_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc043_252d_slope_v043_signal

def f202e_f202_ebitda_per_share_growth_regime_calc044_84d_slope_v044_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(1) + 4.6642)).rolling(49).max().rolling(17).mean() * 0.106856).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc044_84d_slope_v044_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc044_84d_slope_v044_signal

def f202e_f202_ebitda_per_share_growth_regime_calc045_5d_slope_v045_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(1) + 0.5802)).rolling(42).max().rolling(7).min() * 0.262900).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc045_5d_slope_v045_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc045_5d_slope_v045_signal

def f202e_f202_ebitda_per_share_growth_regime_calc046_5d_slope_v046_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(15).std().rolling(45).max().rolling(9).min().rolling(16).min() * 0.073186).diff(10).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc046_5d_slope_v046_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc046_5d_slope_v046_signal

def f202e_f202_ebitda_per_share_growth_regime_calc047_63d_slope_v047_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(36).mean().rolling(15).min().rolling(14).min().rolling(48).max() * 0.159501).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc047_63d_slope_v047_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc047_63d_slope_v047_signal

def f202e_f202_ebitda_per_share_growth_regime_calc048_21d_slope_v048_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.4496)).rolling(45).max().rolling(6).var().pct_change(33) * 0.997182).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc048_21d_slope_v048_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc048_21d_slope_v048_signal

def f202e_f202_ebitda_per_share_growth_regime_calc049_5d_slope_v049_signal(ebitda, sharesbas):
    res = ((ebitda * 8.6260 - sharesbas).rolling(32).min().diff(49).rolling(49).std() * 0.044247).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc049_5d_slope_v049_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc049_5d_slope_v049_signal

def f202e_f202_ebitda_per_share_growth_regime_calc050_200d_slope_v050_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.1936)).rolling(50).std().rolling(43).var().rolling(37).var().rolling(16).std() * 0.237905).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc050_200d_slope_v050_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc050_200d_slope_v050_signal

def f202e_f202_ebitda_per_share_growth_regime_calc051_5d_slope_v051_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(22).var().pct_change(35) * 0.223697).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc051_5d_slope_v051_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc051_5d_slope_v051_signal

def f202e_f202_ebitda_per_share_growth_regime_calc052_84d_slope_v052_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.8988)).rolling(6).mean().rolling(15).std().rolling(40).var() * 0.879468).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc052_84d_slope_v052_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc052_84d_slope_v052_signal

def f202e_f202_ebitda_per_share_growth_regime_calc053_84d_slope_v053_signal(ebitda, sharesbas):
    res = ((ebitda * 5.4129 - sharesbas).pct_change(43).rolling(6).var() * 0.973920).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc053_84d_slope_v053_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc053_84d_slope_v053_signal

def f202e_f202_ebitda_per_share_growth_regime_calc054_105d_slope_v054_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 5.8919)).rolling(12).mean().rolling(44).var().rolling(20).min() * 0.735593).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc054_105d_slope_v054_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc054_105d_slope_v054_signal

def f202e_f202_ebitda_per_share_growth_regime_calc055_84d_slope_v055_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(43).mean().rolling(14).min() * 0.577588).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc055_84d_slope_v055_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc055_84d_slope_v055_signal

def f202e_f202_ebitda_per_share_growth_regime_calc056_5d_slope_v056_signal(ebitda, sharesbas):
    res = ((ebitda.diff(9) / (sharesbas.shift(2) + 9.7831)).rolling(29).std().pct_change(50) * 0.830778).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc056_5d_slope_v056_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc056_5d_slope_v056_signal

def f202e_f202_ebitda_per_share_growth_regime_calc057_42d_slope_v057_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.0956)).rolling(28).min().rolling(31).mean() * 0.881366).diff(6).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc057_42d_slope_v057_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc057_42d_slope_v057_signal

def f202e_f202_ebitda_per_share_growth_regime_calc058_84d_slope_v058_signal(ebitda, sharesbas):
    res = ((ebitda.diff(3) / (sharesbas.shift(2) + 9.9839)).rolling(24).mean().rolling(50).var().rolling(43).max() * 0.092430).diff(7).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc058_84d_slope_v058_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc058_84d_slope_v058_signal

def f202e_f202_ebitda_per_share_growth_regime_calc059_126d_slope_v059_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.3409)).rolling(16).min().rolling(28).mean().rolling(8).max().rolling(4).mean() * 0.265893).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc059_126d_slope_v059_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc059_126d_slope_v059_signal

def f202e_f202_ebitda_per_share_growth_regime_calc060_252d_slope_v060_signal(ebitda, sharesbas):
    res = ((ebitda.diff(4) / (sharesbas.shift(1) + 0.9505)).rolling(30).min().rolling(35).var().rolling(30).min() * 0.771371).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc060_252d_slope_v060_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc060_252d_slope_v060_signal

def f202e_f202_ebitda_per_share_growth_regime_calc061_126d_slope_v061_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.3622)).pct_change(6).rolling(42).mean().rolling(28).var().pct_change(34) * 0.180134).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc061_126d_slope_v061_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc061_126d_slope_v061_signal

def f202e_f202_ebitda_per_share_growth_regime_calc062_5d_slope_v062_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(5) + 2.8548)).pct_change(8).diff(49).rolling(23).mean().rolling(37).max() * 0.489686).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc062_5d_slope_v062_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc062_5d_slope_v062_signal

def f202e_f202_ebitda_per_share_growth_regime_calc063_200d_slope_v063_signal(ebitda, sharesbas):
    res = ((ebitda * 6.3488 - sharesbas).rolling(20).min().rolling(33).var() * 0.451004).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc063_200d_slope_v063_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc063_200d_slope_v063_signal

def f202e_f202_ebitda_per_share_growth_regime_calc064_126d_slope_v064_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(2) + 3.3245)).rolling(40).std().pct_change(15) * 0.555644).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc064_126d_slope_v064_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc064_126d_slope_v064_signal

def f202e_f202_ebitda_per_share_growth_regime_calc065_200d_slope_v065_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 3.9161)).rolling(49).mean().rolling(48).max().rolling(17).var().rolling(20).max() * 0.021161).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc065_200d_slope_v065_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc065_200d_slope_v065_signal

def f202e_f202_ebitda_per_share_growth_regime_calc066_105d_slope_v066_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 2.0305)).rolling(27).mean().rolling(7).std().pct_change(6) * 0.088774).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc066_105d_slope_v066_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc066_105d_slope_v066_signal

def f202e_f202_ebitda_per_share_growth_regime_calc067_21d_slope_v067_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(41).mean().pct_change(11).rolling(8).std() * 0.603860).diff(13).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc067_21d_slope_v067_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc067_21d_slope_v067_signal

def f202e_f202_ebitda_per_share_growth_regime_calc068_84d_slope_v068_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 9.4307)).rolling(37).var().rolling(9).max().rolling(15).min() * 0.409751).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc068_84d_slope_v068_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc068_84d_slope_v068_signal

def f202e_f202_ebitda_per_share_growth_regime_calc069_126d_slope_v069_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(1) + 9.0375)).rolling(33).min().rolling(2).std().rolling(17).std().rolling(35).std() * 0.471478).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc069_126d_slope_v069_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc069_126d_slope_v069_signal

def f202e_f202_ebitda_per_share_growth_regime_calc070_21d_slope_v070_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.3436)).rolling(16).min().rolling(31).std().rolling(12).std().pct_change(16) * 0.515788).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc070_21d_slope_v070_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc070_21d_slope_v070_signal

def f202e_f202_ebitda_per_share_growth_regime_calc071_150d_slope_v071_signal(ebitda, sharesbas):
    res = ((ebitda * 5.4146 - sharesbas).rolling(29).std().pct_change(3).rolling(28).std().diff(2) * 0.425237).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc071_150d_slope_v071_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc071_150d_slope_v071_signal

def f202e_f202_ebitda_per_share_growth_regime_calc072_84d_slope_v072_signal(ebitda, sharesbas):
    res = ((ebitda * 9.9917 - sharesbas).rolling(2).var().rolling(27).mean().pct_change(46).rolling(11).var() * 0.421969).diff(19).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc072_84d_slope_v072_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc072_84d_slope_v072_signal

def f202e_f202_ebitda_per_share_growth_regime_calc073_84d_slope_v073_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(2) + 7.7592)).rolling(37).var().pct_change(29).rolling(37).min().rolling(23).var() * 0.900473).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc073_84d_slope_v073_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc073_84d_slope_v073_signal

def f202e_f202_ebitda_per_share_growth_regime_calc074_21d_slope_v074_signal(ebitda, sharesbas):
    res = ((ebitda * 0.1924 - sharesbas).rolling(31).max().rolling(6).std().rolling(31).max().rolling(7).min() * 0.855334).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc074_21d_slope_v074_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc074_21d_slope_v074_signal

def f202e_f202_ebitda_per_share_growth_regime_calc075_10d_slope_v075_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(32).max().pct_change(4).rolling(12).var() * 0.598735).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc075_10d_slope_v075_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc075_10d_slope_v075_signal

def f202e_f202_ebitda_per_share_growth_regime_calc076_63d_slope_v076_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 8.3482)).rolling(21).mean().rolling(26).var().rolling(18).min() * 0.903309).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc076_63d_slope_v076_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc076_63d_slope_v076_signal

def f202e_f202_ebitda_per_share_growth_regime_calc077_42d_slope_v077_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(8).rolling(45).std().rolling(15).std().diff(24) * 0.986226).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc077_42d_slope_v077_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc077_42d_slope_v077_signal

def f202e_f202_ebitda_per_share_growth_regime_calc078_63d_slope_v078_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.8778)).diff(28).rolling(23).min().diff(13) * 0.302540).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc078_63d_slope_v078_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc078_63d_slope_v078_signal

def f202e_f202_ebitda_per_share_growth_regime_calc079_252d_slope_v079_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 9.9540)).rolling(5).mean().rolling(49).var().diff(12).rolling(40).std() * 0.648441).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc079_252d_slope_v079_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc079_252d_slope_v079_signal

def f202e_f202_ebitda_per_share_growth_regime_calc080_84d_slope_v080_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(25).diff(39).pct_change(33).rolling(13).max() * 0.687313).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc080_84d_slope_v080_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc080_84d_slope_v080_signal

def f202e_f202_ebitda_per_share_growth_regime_calc081_150d_slope_v081_signal(ebitda, sharesbas):
    res = ((ebitda * 9.1853 - sharesbas).rolling(26).var().diff(30).rolling(26).var().rolling(6).std() * 0.805310).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc081_150d_slope_v081_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc081_150d_slope_v081_signal

def f202e_f202_ebitda_per_share_growth_regime_calc082_126d_slope_v082_signal(ebitda, sharesbas):
    res = ((ebitda.diff(3) / (sharesbas.shift(3) + 0.9965)).rolling(23).std().rolling(3).max().rolling(34).std() * 0.678956).diff(9).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc082_126d_slope_v082_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc082_126d_slope_v082_signal

def f202e_f202_ebitda_per_share_growth_regime_calc083_150d_slope_v083_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 6.9346)).rolling(36).mean().diff(48).rolling(27).max() * 0.200964).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc083_150d_slope_v083_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc083_150d_slope_v083_signal

def f202e_f202_ebitda_per_share_growth_regime_calc084_63d_slope_v084_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(26).mean().rolling(49).std() * 0.459614).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc084_63d_slope_v084_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc084_63d_slope_v084_signal

def f202e_f202_ebitda_per_share_growth_regime_calc085_150d_slope_v085_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 2.5044)).pct_change(49).pct_change(18) * 0.928392).diff(20).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc085_150d_slope_v085_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc085_150d_slope_v085_signal

def f202e_f202_ebitda_per_share_growth_regime_calc086_105d_slope_v086_signal(ebitda, sharesbas):
    res = ((ebitda * 6.6363 - sharesbas).diff(30).rolling(3).var() * 0.964770).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc086_105d_slope_v086_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc086_105d_slope_v086_signal

def f202e_f202_ebitda_per_share_growth_regime_calc087_63d_slope_v087_signal(ebitda, sharesbas):
    res = ((ebitda * 5.1261 - sharesbas).rolling(23).std().rolling(25).mean().rolling(19).mean() * 0.252588).diff(9).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc087_63d_slope_v087_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc087_63d_slope_v087_signal

def f202e_f202_ebitda_per_share_growth_regime_calc088_63d_slope_v088_signal(ebitda, sharesbas):
    res = ((ebitda * 0.7926 - sharesbas).rolling(21).max().rolling(24).min().diff(36) * 0.798630).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc088_63d_slope_v088_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc088_63d_slope_v088_signal

def f202e_f202_ebitda_per_share_growth_regime_calc089_5d_slope_v089_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(22).var().rolling(36).mean().pct_change(43) * 0.675730).diff(10).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc089_5d_slope_v089_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc089_5d_slope_v089_signal

def f202e_f202_ebitda_per_share_growth_regime_calc090_126d_slope_v090_signal(ebitda, sharesbas):
    res = ((ebitda * 0.1061 - sharesbas).rolling(27).max().rolling(41).min() * 0.051275).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc090_126d_slope_v090_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc090_126d_slope_v090_signal

def f202e_f202_ebitda_per_share_growth_regime_calc091_5d_slope_v091_signal(ebitda, sharesbas):
    res = ((ebitda * 9.8761 - sharesbas).rolling(21).mean().rolling(32).mean().rolling(41).max() * 0.944897).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc091_5d_slope_v091_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc091_5d_slope_v091_signal

def f202e_f202_ebitda_per_share_growth_regime_calc092_5d_slope_v092_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(3) + 9.7165)).diff(6).rolling(20).std().rolling(42).max().pct_change(4) * 0.992308).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc092_5d_slope_v092_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc092_5d_slope_v092_signal

def f202e_f202_ebitda_per_share_growth_regime_calc093_10d_slope_v093_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(4) + 8.4355)).rolling(14).var().rolling(9).min().diff(3) * 0.247234).diff(3).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc093_10d_slope_v093_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc093_10d_slope_v093_signal

def f202e_f202_ebitda_per_share_growth_regime_calc094_63d_slope_v094_signal(ebitda, sharesbas):
    res = ((ebitda * 4.7635 - sharesbas).rolling(21).min().rolling(17).min() * 0.835282).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc094_63d_slope_v094_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc094_63d_slope_v094_signal

def f202e_f202_ebitda_per_share_growth_regime_calc095_21d_slope_v095_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(4) + 1.8577)).pct_change(39).rolling(31).var().pct_change(4).diff(42) * 0.592798).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc095_21d_slope_v095_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc095_21d_slope_v095_signal

def f202e_f202_ebitda_per_share_growth_regime_calc096_105d_slope_v096_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 7.8557)).diff(24).rolling(22).std().rolling(21).min() * 0.387066).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc096_105d_slope_v096_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc096_105d_slope_v096_signal

def f202e_f202_ebitda_per_share_growth_regime_calc097_150d_slope_v097_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.5635)).rolling(46).mean().rolling(41).std().rolling(24).max().pct_change(5) * 0.093571).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc097_150d_slope_v097_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc097_150d_slope_v097_signal

def f202e_f202_ebitda_per_share_growth_regime_calc098_84d_slope_v098_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(2) + 9.4885)).rolling(36).std().rolling(40).mean().rolling(7).std() * 0.530566).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc098_84d_slope_v098_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc098_84d_slope_v098_signal

def f202e_f202_ebitda_per_share_growth_regime_calc099_84d_slope_v099_signal(ebitda, sharesbas):
    res = ((ebitda * 1.3342 - sharesbas).rolling(46).mean().diff(26) * 0.280798).diff(2).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc099_84d_slope_v099_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc099_84d_slope_v099_signal

def f202e_f202_ebitda_per_share_growth_regime_calc100_126d_slope_v100_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.4567)).rolling(43).var().rolling(45).std().rolling(3).max().rolling(16).var() * 0.160539).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc100_126d_slope_v100_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc100_126d_slope_v100_signal

def f202e_f202_ebitda_per_share_growth_regime_calc101_10d_slope_v101_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(38).min().diff(5).rolling(45).min() * 0.792220).diff(12).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc101_10d_slope_v101_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc101_10d_slope_v101_signal

def f202e_f202_ebitda_per_share_growth_regime_calc102_63d_slope_v102_signal(ebitda, sharesbas):
    res = ((ebitda.diff(3) / (sharesbas.shift(4) + 5.8752)).rolling(38).max().rolling(4).max() * 0.986756).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc102_63d_slope_v102_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc102_63d_slope_v102_signal

def f202e_f202_ebitda_per_share_growth_regime_calc103_42d_slope_v103_signal(ebitda, sharesbas):
    res = ((ebitda.diff(5) / (sharesbas.shift(5) + 7.8757)).diff(27).diff(14).diff(14) * 0.650683).diff(16).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc103_42d_slope_v103_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc103_42d_slope_v103_signal

def f202e_f202_ebitda_per_share_growth_regime_calc104_42d_slope_v104_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 2.4970)).rolling(9).var().rolling(33).max().diff(11) * 0.922479).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc104_42d_slope_v104_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc104_42d_slope_v104_signal

def f202e_f202_ebitda_per_share_growth_regime_calc105_252d_slope_v105_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(48).std().rolling(48).max().diff(42) * 0.329519).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc105_252d_slope_v105_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc105_252d_slope_v105_signal

def f202e_f202_ebitda_per_share_growth_regime_calc106_252d_slope_v106_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(21).pct_change(41).pct_change(17).rolling(2).var() * 0.838845).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc106_252d_slope_v106_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc106_252d_slope_v106_signal

def f202e_f202_ebitda_per_share_growth_regime_calc107_63d_slope_v107_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(5) + 3.7612)).rolling(26).max().pct_change(46).diff(24).rolling(48).max() * 0.863825).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc107_63d_slope_v107_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc107_63d_slope_v107_signal

def f202e_f202_ebitda_per_share_growth_regime_calc108_252d_slope_v108_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(8).var().pct_change(22) * 0.861465).diff(4).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc108_252d_slope_v108_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc108_252d_slope_v108_signal

def f202e_f202_ebitda_per_share_growth_regime_calc109_252d_slope_v109_signal(ebitda, sharesbas):
    res = ((ebitda * 5.2627 - sharesbas).rolling(45).max().rolling(30).std().rolling(25).min() * 0.853474).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc109_252d_slope_v109_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc109_252d_slope_v109_signal

def f202e_f202_ebitda_per_share_growth_regime_calc110_150d_slope_v110_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.3552)).rolling(9).max().rolling(36).max().diff(6).diff(14) * 0.211316).diff(7).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc110_150d_slope_v110_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc110_150d_slope_v110_signal

def f202e_f202_ebitda_per_share_growth_regime_calc111_252d_slope_v111_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.3119)).diff(12).rolling(21).min().rolling(34).var() * 0.402234).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc111_252d_slope_v111_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc111_252d_slope_v111_signal

def f202e_f202_ebitda_per_share_growth_regime_calc112_105d_slope_v112_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 0.4583)).rolling(26).std().rolling(11).min().rolling(27).mean() * 0.772950).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc112_105d_slope_v112_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc112_105d_slope_v112_signal

def f202e_f202_ebitda_per_share_growth_regime_calc113_10d_slope_v113_signal(ebitda, sharesbas):
    res = ((ebitda * 5.6506 - sharesbas).diff(49).rolling(21).max().pct_change(10) * 0.302993).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc113_10d_slope_v113_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc113_10d_slope_v113_signal

def f202e_f202_ebitda_per_share_growth_regime_calc114_200d_slope_v114_signal(ebitda, sharesbas):
    res = ((ebitda * 0.4903 - sharesbas).rolling(49).min().rolling(26).max().rolling(39).max() * 0.238038).diff(18).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc114_200d_slope_v114_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc114_200d_slope_v114_signal

def f202e_f202_ebitda_per_share_growth_regime_calc115_200d_slope_v115_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.8866)).rolling(14).max().rolling(2).var() * 0.767280).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc115_200d_slope_v115_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc115_200d_slope_v115_signal

def f202e_f202_ebitda_per_share_growth_regime_calc116_63d_slope_v116_signal(ebitda, sharesbas):
    res = ((ebitda * 3.9851 - sharesbas).rolling(12).min().pct_change(4).rolling(18).var().rolling(24).min() * 0.956444).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc116_63d_slope_v116_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc116_63d_slope_v116_signal

def f202e_f202_ebitda_per_share_growth_regime_calc117_42d_slope_v117_signal(ebitda, sharesbas):
    res = ((ebitda * 9.3824 - sharesbas).rolling(42).max().rolling(24).min() * 0.063382).diff(15).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc117_42d_slope_v117_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc117_42d_slope_v117_signal

def f202e_f202_ebitda_per_share_growth_regime_calc118_63d_slope_v118_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.5004)).rolling(49).std().rolling(38).std() * 0.489803).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc118_63d_slope_v118_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc118_63d_slope_v118_signal

def f202e_f202_ebitda_per_share_growth_regime_calc119_42d_slope_v119_signal(ebitda, sharesbas):
    res = ((ebitda * 1.8123 - sharesbas).rolling(12).std().diff(5) * 0.635467).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc119_42d_slope_v119_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc119_42d_slope_v119_signal

def f202e_f202_ebitda_per_share_growth_regime_calc120_5d_slope_v120_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(16).min().diff(37) * 0.662964).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc120_5d_slope_v120_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc120_5d_slope_v120_signal

def f202e_f202_ebitda_per_share_growth_regime_calc121_84d_slope_v121_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 5.2162)).rolling(23).var().rolling(9).std().rolling(29).min().rolling(24).max() * 0.197559).diff(8).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc121_84d_slope_v121_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc121_84d_slope_v121_signal

def f202e_f202_ebitda_per_share_growth_regime_calc122_105d_slope_v122_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(44).std().rolling(33).var() * 0.906664).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc122_105d_slope_v122_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc122_105d_slope_v122_signal

def f202e_f202_ebitda_per_share_growth_regime_calc123_63d_slope_v123_signal(ebitda, sharesbas):
    res = ((ebitda * 5.2394 - sharesbas).rolling(32).max().rolling(37).std().rolling(34).mean() * 0.582885).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc123_63d_slope_v123_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc123_63d_slope_v123_signal

def f202e_f202_ebitda_per_share_growth_regime_calc124_10d_slope_v124_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(5) + 5.0025)).pct_change(18).rolling(16).var().pct_change(4) * 0.275106).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc124_10d_slope_v124_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc124_10d_slope_v124_signal

def f202e_f202_ebitda_per_share_growth_regime_calc125_42d_slope_v125_signal(ebitda, sharesbas):
    res = ((ebitda * 7.4968 - sharesbas).rolling(18).min().rolling(26).var().pct_change(18) * 0.626481).diff(9).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc125_42d_slope_v125_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc125_42d_slope_v125_signal

def f202e_f202_ebitda_per_share_growth_regime_calc126_252d_slope_v126_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(9).mean().rolling(24).std() * 0.942942).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc126_252d_slope_v126_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc126_252d_slope_v126_signal

def f202e_f202_ebitda_per_share_growth_regime_calc127_150d_slope_v127_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(43).min().rolling(41).var().pct_change(50) * 0.373820).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc127_150d_slope_v127_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc127_150d_slope_v127_signal

def f202e_f202_ebitda_per_share_growth_regime_calc128_63d_slope_v128_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.2787)).pct_change(33).rolling(43).max().rolling(7).min() * 0.469139).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc128_63d_slope_v128_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc128_63d_slope_v128_signal

def f202e_f202_ebitda_per_share_growth_regime_calc129_252d_slope_v129_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(4) + 3.9530)).pct_change(50).diff(44) * 0.416686).diff(6).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc129_252d_slope_v129_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc129_252d_slope_v129_signal

def f202e_f202_ebitda_per_share_growth_regime_calc130_126d_slope_v130_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.1731)).rolling(36).var().pct_change(38) * 0.803364).diff(9).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc130_126d_slope_v130_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc130_126d_slope_v130_signal

def f202e_f202_ebitda_per_share_growth_regime_calc131_5d_slope_v131_signal(ebitda, sharesbas):
    res = ((ebitda * 7.7650 - sharesbas).rolling(4).std().rolling(20).max().rolling(42).max() * 0.441959).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc131_5d_slope_v131_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc131_5d_slope_v131_signal

def f202e_f202_ebitda_per_share_growth_regime_calc132_63d_slope_v132_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(31).min().pct_change(18).pct_change(30).rolling(31).max() * 0.511319).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc132_63d_slope_v132_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc132_63d_slope_v132_signal

def f202e_f202_ebitda_per_share_growth_regime_calc133_150d_slope_v133_signal(ebitda, sharesbas):
    res = ((ebitda * 6.2855 - sharesbas).rolling(5).min().rolling(22).min() * 0.562830).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc133_150d_slope_v133_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc133_150d_slope_v133_signal

def f202e_f202_ebitda_per_share_growth_regime_calc134_200d_slope_v134_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 8.0932)).rolling(37).min().rolling(37).max().rolling(49).mean() * 0.357596).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc134_200d_slope_v134_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc134_200d_slope_v134_signal

def f202e_f202_ebitda_per_share_growth_regime_calc135_21d_slope_v135_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(1) + 3.5394)).rolling(5).max().pct_change(18).diff(30) * 0.512817).diff(11).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc135_21d_slope_v135_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc135_21d_slope_v135_signal

def f202e_f202_ebitda_per_share_growth_regime_calc136_126d_slope_v136_signal(ebitda, sharesbas):
    res = ((ebitda * 5.0982 - sharesbas).rolling(30).max().rolling(23).std().rolling(38).std() * 0.969303).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc136_126d_slope_v136_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc136_126d_slope_v136_signal

def f202e_f202_ebitda_per_share_growth_regime_calc137_105d_slope_v137_signal(ebitda, sharesbas):
    res = ((ebitda * 8.8628 - sharesbas).rolling(31).var().rolling(41).mean().diff(13).rolling(23).std() * 0.535661).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc137_105d_slope_v137_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc137_105d_slope_v137_signal

def f202e_f202_ebitda_per_share_growth_regime_calc138_105d_slope_v138_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.9629)).diff(42).rolling(20).max().rolling(5).max() * 0.785169).diff(20).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc138_105d_slope_v138_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc138_105d_slope_v138_signal

def f202e_f202_ebitda_per_share_growth_regime_calc139_200d_slope_v139_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 2.4851)).rolling(2).std().rolling(48).var().diff(49) * 0.995242).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc139_200d_slope_v139_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc139_200d_slope_v139_signal

def f202e_f202_ebitda_per_share_growth_regime_calc140_5d_slope_v140_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.2271)).diff(10).rolling(31).mean() * 0.396322).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc140_5d_slope_v140_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc140_5d_slope_v140_signal

def f202e_f202_ebitda_per_share_growth_regime_calc141_150d_slope_v141_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(3) + 3.8831)).rolling(39).min().rolling(39).var().rolling(22).max().rolling(29).std() * 0.503786).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc141_150d_slope_v141_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc141_150d_slope_v141_signal

def f202e_f202_ebitda_per_share_growth_regime_calc142_252d_slope_v142_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 2.8155)).diff(14).rolling(25).min() * 0.727327).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc142_252d_slope_v142_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc142_252d_slope_v142_signal

def f202e_f202_ebitda_per_share_growth_regime_calc143_42d_slope_v143_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(38).var().pct_change(28).rolling(18).min() * 0.460930).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc143_42d_slope_v143_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc143_42d_slope_v143_signal

def f202e_f202_ebitda_per_share_growth_regime_calc144_126d_slope_v144_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.3458)).rolling(4).mean().diff(9).rolling(49).std().rolling(42).max() * 0.723320).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc144_126d_slope_v144_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc144_126d_slope_v144_signal

def f202e_f202_ebitda_per_share_growth_regime_calc145_10d_slope_v145_signal(ebitda, sharesbas):
    res = ((ebitda * 5.9580 - sharesbas).pct_change(42).rolling(28).std() * 0.992709).diff(18).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc145_10d_slope_v145_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc145_10d_slope_v145_signal

def f202e_f202_ebitda_per_share_growth_regime_calc146_5d_slope_v146_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.7508)).diff(10).rolling(30).max() * 0.727694).diff(4).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc146_5d_slope_v146_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc146_5d_slope_v146_signal

def f202e_f202_ebitda_per_share_growth_regime_calc147_21d_slope_v147_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(20).std().rolling(8).var().rolling(19).max() * 0.228942).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc147_21d_slope_v147_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc147_21d_slope_v147_signal

def f202e_f202_ebitda_per_share_growth_regime_calc148_126d_slope_v148_signal(ebitda, sharesbas):
    res = ((ebitda.diff(9) / (sharesbas.shift(4) + 0.2480)).rolling(33).mean().rolling(31).max().pct_change(24).rolling(7).max() * 0.231001).diff(15).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc148_126d_slope_v148_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc148_126d_slope_v148_signal

def f202e_f202_ebitda_per_share_growth_regime_calc149_200d_slope_v149_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.7353)).rolling(38).min().diff(3).rolling(33).min().rolling(37).min() * 0.270457).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc149_200d_slope_v149_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc149_200d_slope_v149_signal

def f202e_f202_ebitda_per_share_growth_regime_calc150_105d_slope_v150_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 6.4141)).rolling(11).max().pct_change(31).rolling(3).min() * 0.942900).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc150_105d_slope_v150_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc150_105d_slope_v150_signal


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
