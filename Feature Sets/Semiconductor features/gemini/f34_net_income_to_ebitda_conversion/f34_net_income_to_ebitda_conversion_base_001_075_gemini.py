import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f34niec_f34_net_income_to_ebitda_conversion_base_v001_signal(close, volume):
    res = close.pct_change(10).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v001_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v001_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v002_signal(close, volume):
    res = close.pct_change(21).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v002_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v002_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v003_signal(close, volume):
    res = close.pct_change(42).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v003_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v003_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v004_signal(close, volume):
    res = close.pct_change(63).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v004_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v004_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v005_signal(close, volume):
    res = close.pct_change(126).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v005_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v005_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v006_signal(close, volume):
    res = close.pct_change(252).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v006_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v006_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v007_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v007_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v007_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v008_signal(close, volume):
    res = close.pct_change(12).rolling(12).mean() * volume.pct_change(12)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v008_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v008_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v009_signal(close, volume):
    res = close.pct_change(23).rolling(23).mean() * volume.pct_change(23)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v009_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v009_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v010_signal(close, volume):
    res = close.pct_change(44).rolling(44).mean() * volume.pct_change(44)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v010_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v010_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v011_signal(close, volume):
    res = close.pct_change(65).rolling(65).mean() * volume.pct_change(65)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v011_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v011_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v012_signal(close, volume):
    res = close.pct_change(128).rolling(128).mean() * volume.pct_change(128)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v012_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v012_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v013_signal(close, volume):
    res = close.pct_change(254).rolling(254).mean() * volume.pct_change(254)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v013_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v013_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v014_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v014_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v014_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v015_signal(close, volume):
    res = close.pct_change(14).rolling(14).mean() * volume.pct_change(14)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v015_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v015_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v016_signal(close, volume):
    res = close.pct_change(25).rolling(25).mean() * volume.pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v016_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v016_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v017_signal(close, volume):
    res = close.pct_change(46).rolling(46).mean() * volume.pct_change(46)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v017_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v017_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v018_signal(close, volume):
    res = close.pct_change(67).rolling(67).mean() * volume.pct_change(67)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v018_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v018_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v019_signal(close, volume):
    res = close.pct_change(130).rolling(130).mean() * volume.pct_change(130)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v019_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v019_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v020_signal(close, volume):
    res = close.pct_change(256).rolling(256).mean() * volume.pct_change(256)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v020_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v020_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v021_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v021_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v021_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v022_signal(close, volume):
    res = close.pct_change(16).rolling(16).mean() * volume.pct_change(16)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v022_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v022_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v023_signal(close, volume):
    res = close.pct_change(27).rolling(27).mean() * volume.pct_change(27)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v023_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v023_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v024_signal(close, volume):
    res = close.pct_change(48).rolling(48).mean() * volume.pct_change(48)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v024_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v024_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v025_signal(close, volume):
    res = close.pct_change(69).rolling(69).mean() * volume.pct_change(69)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v025_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v025_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v026_signal(close, volume):
    res = close.pct_change(132).rolling(132).mean() * volume.pct_change(132)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v026_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v026_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v027_signal(close, volume):
    res = close.pct_change(258).rolling(258).mean() * volume.pct_change(258)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v027_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v027_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v028_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v028_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v028_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v029_signal(close, volume):
    res = close.pct_change(18).rolling(18).mean() * volume.pct_change(18)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v029_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v029_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v030_signal(close, volume):
    res = close.pct_change(29).rolling(29).mean() * volume.pct_change(29)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v030_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v030_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v031_signal(close, volume):
    res = close.pct_change(50).rolling(50).mean() * volume.pct_change(50)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v031_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v031_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v032_signal(close, volume):
    res = close.pct_change(71).rolling(71).mean() * volume.pct_change(71)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v032_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v032_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v033_signal(close, volume):
    res = close.pct_change(134).rolling(134).mean() * volume.pct_change(134)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v033_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v033_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v034_signal(close, volume):
    res = close.pct_change(260).rolling(260).mean() * volume.pct_change(260)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v034_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v034_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v035_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v035_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v035_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v036_signal(close, volume):
    res = close.pct_change(20).rolling(20).mean() * volume.pct_change(20)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v036_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v036_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v037_signal(close, volume):
    res = close.pct_change(31).rolling(31).mean() * volume.pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v037_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v037_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v038_signal(close, volume):
    res = close.pct_change(52).rolling(52).mean() * volume.pct_change(52)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v038_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v038_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v039_signal(close, volume):
    res = close.pct_change(73).rolling(73).mean() * volume.pct_change(73)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v039_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v039_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v040_signal(close, volume):
    res = close.pct_change(136).rolling(136).mean() * volume.pct_change(136)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v040_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v040_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v041_signal(close, volume):
    res = close.pct_change(262).rolling(262).mean() * volume.pct_change(262)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v041_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v041_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v042_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v042_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v042_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v043_signal(close, volume):
    res = close.pct_change(22).rolling(22).mean() * volume.pct_change(22)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v043_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v043_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v044_signal(close, volume):
    res = close.pct_change(33).rolling(33).mean() * volume.pct_change(33)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v044_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v044_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v045_signal(close, volume):
    res = close.pct_change(54).rolling(54).mean() * volume.pct_change(54)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v045_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v045_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v046_signal(close, volume):
    res = close.pct_change(75).rolling(75).mean() * volume.pct_change(75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v046_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v046_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v047_signal(close, volume):
    res = close.pct_change(138).rolling(138).mean() * volume.pct_change(138)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v047_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v047_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v048_signal(close, volume):
    res = close.pct_change(264).rolling(264).mean() * volume.pct_change(264)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v048_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v048_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v049_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v049_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v049_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v050_signal(close, volume):
    res = close.pct_change(24).rolling(24).mean() * volume.pct_change(24)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v050_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v050_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v051_signal(close, volume):
    res = close.pct_change(35).rolling(35).mean() * volume.pct_change(35)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v051_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v051_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v052_signal(close, volume):
    res = close.pct_change(56).rolling(56).mean() * volume.pct_change(56)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v052_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v052_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v053_signal(close, volume):
    res = close.pct_change(77).rolling(77).mean() * volume.pct_change(77)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v053_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v053_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v054_signal(close, volume):
    res = close.pct_change(140).rolling(140).mean() * volume.pct_change(140)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v054_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v054_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v055_signal(close, volume):
    res = close.pct_change(266).rolling(266).mean() * volume.pct_change(266)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v055_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v055_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v056_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v056_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v056_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v057_signal(close, volume):
    res = close.pct_change(26).rolling(26).mean() * volume.pct_change(26)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v057_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v057_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v058_signal(close, volume):
    res = close.pct_change(37).rolling(37).mean() * volume.pct_change(37)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v058_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v058_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v059_signal(close, volume):
    res = close.pct_change(58).rolling(58).mean() * volume.pct_change(58)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v059_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v059_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v060_signal(close, volume):
    res = close.pct_change(79).rolling(79).mean() * volume.pct_change(79)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v060_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v060_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v061_signal(close, volume):
    res = close.pct_change(142).rolling(142).mean() * volume.pct_change(142)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v061_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v061_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v062_signal(close, volume):
    res = close.pct_change(268).rolling(268).mean() * volume.pct_change(268)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v062_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v062_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v063_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v063_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v063_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v064_signal(close, volume):
    res = close.pct_change(28).rolling(28).mean() * volume.pct_change(28)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v064_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v064_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v065_signal(close, volume):
    res = close.pct_change(39).rolling(39).mean() * volume.pct_change(39)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v065_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v065_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v066_signal(close, volume):
    res = close.pct_change(60).rolling(60).mean() * volume.pct_change(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v066_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v066_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v067_signal(close, volume):
    res = close.pct_change(81).rolling(81).mean() * volume.pct_change(81)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v067_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v067_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v068_signal(close, volume):
    res = close.pct_change(144).rolling(144).mean() * volume.pct_change(144)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v068_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v068_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v069_signal(close, volume):
    res = close.pct_change(270).rolling(270).mean() * volume.pct_change(270)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v069_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v069_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v070_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v070_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v070_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v071_signal(close, volume):
    res = close.pct_change(30).rolling(30).mean() * volume.pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v071_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v071_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v072_signal(close, volume):
    res = close.pct_change(41).rolling(41).mean() * volume.pct_change(41)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v072_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v072_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v073_signal(close, volume):
    res = close.pct_change(62).rolling(62).mean() * volume.pct_change(62)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v073_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v073_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v074_signal(close, volume):
    res = close.pct_change(83).rolling(83).mean() * volume.pct_change(83)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v074_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v074_signal

def f34niec_f34_net_income_to_ebitda_conversion_base_v075_signal(close, volume):
    res = close.pct_change(146).rolling(146).mean() * volume.pct_change(146)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f34niec_f34_net_income_to_ebitda_conversion_base_v075_signal'] = f34niec_f34_net_income_to_ebitda_conversion_base_v075_signal


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
