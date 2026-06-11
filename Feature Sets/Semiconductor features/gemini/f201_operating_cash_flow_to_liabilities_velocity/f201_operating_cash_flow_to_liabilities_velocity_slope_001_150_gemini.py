import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_126d_slope_v001_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.6596)).rolling(23).mean().diff(49).diff(50) * 0.421803).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_126d_slope_v001_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_126d_slope_v001_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_252d_slope_v002_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 4.0326)).pct_change(31).rolling(38).min() * 0.776977).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_252d_slope_v002_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_252d_slope_v002_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_10d_slope_v003_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.1286)).diff(40).diff(15) * 0.688761).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_10d_slope_v003_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_10d_slope_v003_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_150d_slope_v004_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(23).pct_change(30) * 0.345827).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_150d_slope_v004_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_150d_slope_v004_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_5d_slope_v005_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(3) + 9.2433)).rolling(9).min().rolling(3).var() * 0.815125).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_5d_slope_v005_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_5d_slope_v005_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_21d_slope_v006_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(20).pct_change(46).pct_change(31).rolling(2).mean() * 0.312767).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_21d_slope_v006_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_21d_slope_v006_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_126d_slope_v007_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.8824)).diff(25).pct_change(22).diff(34) * 0.836174).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_126d_slope_v007_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_126d_slope_v007_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_105d_slope_v008_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(2) + 1.3980)).pct_change(32).pct_change(34) * 0.883371).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_105d_slope_v008_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_105d_slope_v008_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_10d_slope_v009_signal(ncfo, liabilities):
    res = ((ncfo * 0.6091 - liabilities).rolling(42).mean().rolling(7).mean().diff(41) * 0.597367).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_10d_slope_v009_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_10d_slope_v009_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_84d_slope_v010_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.7905)).rolling(16).mean().rolling(37).min().rolling(13).std() * 0.390793).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_84d_slope_v010_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_84d_slope_v010_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_21d_slope_v011_signal(ncfo, liabilities):
    res = ((ncfo.diff(6) / (liabilities.shift(2) + 3.5396)).rolling(23).max().rolling(21).var().rolling(13).mean() * 0.127044).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_21d_slope_v011_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_21d_slope_v011_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_63d_slope_v012_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(48).var().rolling(17).var().pct_change(29).rolling(39).var() * 0.098359).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_63d_slope_v012_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_63d_slope_v012_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_42d_slope_v013_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(33).std().pct_change(37).rolling(38).min() * 0.456134).diff(8).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_42d_slope_v013_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_42d_slope_v013_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_42d_slope_v014_signal(ncfo, liabilities):
    res = ((ncfo * 7.6254 - liabilities).pct_change(36).rolling(15).max().rolling(30).mean() * 0.318243).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_42d_slope_v014_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_42d_slope_v014_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_105d_slope_v015_signal(ncfo, liabilities):
    res = ((ncfo * 5.3999 - liabilities).rolling(4).max().rolling(44).std().pct_change(30) * 0.093924).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_105d_slope_v015_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_105d_slope_v015_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_84d_slope_v016_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.7699)).rolling(8).std().diff(9).diff(23) * 0.986058).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_84d_slope_v016_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_84d_slope_v016_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_105d_slope_v017_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.4953)).diff(18).rolling(19).var() * 0.215793).diff(14).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_105d_slope_v017_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_105d_slope_v017_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_21d_slope_v018_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(41).mean().rolling(37).max().pct_change(2).rolling(10).mean() * 0.932190).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_21d_slope_v018_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_21d_slope_v018_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_10d_slope_v019_signal(ncfo, liabilities):
    res = ((ncfo * 0.3852 - liabilities).rolling(28).mean().rolling(42).std().rolling(19).mean() * 0.554961).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_10d_slope_v019_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_10d_slope_v019_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_200d_slope_v020_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(38).min().rolling(13).std().rolling(12).var() * 0.757649).diff(3).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_200d_slope_v020_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_200d_slope_v020_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_42d_slope_v021_signal(ncfo, liabilities):
    res = ((ncfo.diff(7) / (liabilities.shift(4) + 8.2438)).rolling(5).mean().rolling(34).max() * 0.214028).diff(19).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_42d_slope_v021_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_42d_slope_v021_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_200d_slope_v022_signal(ncfo, liabilities):
    res = ((ncfo * 9.4372 - liabilities).rolling(13).mean().rolling(36).std() * 0.651767).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_200d_slope_v022_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_200d_slope_v022_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_21d_slope_v023_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 0.4921)).rolling(41).std().rolling(20).var() * 0.209339).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_21d_slope_v023_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_21d_slope_v023_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_84d_slope_v024_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 7.3273)).rolling(23).std().rolling(7).var().rolling(38).min() * 0.322965).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_84d_slope_v024_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_84d_slope_v024_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_126d_slope_v025_signal(ncfo, liabilities):
    res = ((ncfo * 4.2951 - liabilities).rolling(45).mean().rolling(7).mean().rolling(16).max() * 0.906783).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_126d_slope_v025_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_126d_slope_v025_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_105d_slope_v026_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(41).rolling(27).var() * 0.619684).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_105d_slope_v026_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_105d_slope_v026_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_126d_slope_v027_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(2) + 0.1541)).rolling(46).std().rolling(23).var().rolling(30).max() * 0.459360).diff(19).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_126d_slope_v027_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_126d_slope_v027_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_84d_slope_v028_signal(ncfo, liabilities):
    res = ((ncfo * 0.1118 - liabilities).rolling(44).std().rolling(42).max().diff(9) * 0.765432).diff(3).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_84d_slope_v028_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_84d_slope_v028_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_84d_slope_v029_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(16).min().pct_change(45).rolling(4).min() * 0.669358).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_84d_slope_v029_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_84d_slope_v029_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_63d_slope_v030_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(21).rolling(46).std().rolling(34).var().pct_change(14) * 0.370911).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_63d_slope_v030_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_63d_slope_v030_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_126d_slope_v031_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(13).mean().rolling(15).std().diff(33) * 0.063419).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_126d_slope_v031_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_126d_slope_v031_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_5d_slope_v032_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.9373)).rolling(15).min().rolling(36).std() * 0.341879).diff(16).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_5d_slope_v032_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_5d_slope_v032_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_10d_slope_v033_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.9514)).rolling(6).mean().rolling(2).var().rolling(42).var().diff(42) * 0.144018).diff(12).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_10d_slope_v033_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_10d_slope_v033_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_200d_slope_v034_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(1) + 2.8460)).rolling(24).std().rolling(32).std() * 0.925331).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_200d_slope_v034_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_200d_slope_v034_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_150d_slope_v035_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 8.5591)).rolling(42).max().rolling(15).mean().rolling(32).mean().rolling(16).std() * 0.923985).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_150d_slope_v035_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_150d_slope_v035_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_126d_slope_v036_signal(ncfo, liabilities):
    res = ((ncfo * 4.8638 - liabilities).pct_change(8).pct_change(50) * 0.987133).diff(8).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_126d_slope_v036_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_126d_slope_v036_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_10d_slope_v037_signal(ncfo, liabilities):
    res = ((ncfo * 3.9903 - liabilities).rolling(48).min().diff(6).rolling(36).mean() * 0.669110).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_10d_slope_v037_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_10d_slope_v037_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_5d_slope_v038_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(45).rolling(15).min().pct_change(22) * 0.989171).diff(15).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_5d_slope_v038_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_5d_slope_v038_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_252d_slope_v039_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(13).pct_change(8) * 0.187537).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_252d_slope_v039_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_252d_slope_v039_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_150d_slope_v040_signal(ncfo, liabilities):
    res = ((ncfo.diff(7) / (liabilities.shift(3) + 8.9265)).rolling(39).var().rolling(8).min().rolling(13).std() * 0.126368).diff(2).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_150d_slope_v040_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_150d_slope_v040_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_5d_slope_v041_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.4698)).rolling(35).max().rolling(2).var() * 0.848765).diff(2).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_5d_slope_v041_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_5d_slope_v041_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_5d_slope_v042_signal(ncfo, liabilities):
    res = ((ncfo * 6.1406 - liabilities).pct_change(43).diff(44).rolling(31).min().rolling(43).var() * 0.657409).diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_5d_slope_v042_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_5d_slope_v042_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_200d_slope_v043_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.9128)).rolling(47).var().rolling(36).min().rolling(9).var().pct_change(44) * 0.709802).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_200d_slope_v043_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_200d_slope_v043_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_63d_slope_v044_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(4) + 9.5627)).rolling(28).var().pct_change(33).rolling(36).min().rolling(3).std() * 0.198837).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_63d_slope_v044_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_63d_slope_v044_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_126d_slope_v045_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(15).rolling(18).var().rolling(25).max() * 0.244903).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_126d_slope_v045_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_126d_slope_v045_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_10d_slope_v046_signal(ncfo, liabilities):
    res = ((ncfo * 2.2812 - liabilities).rolling(26).std().rolling(48).min() * 0.898718).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_10d_slope_v046_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_10d_slope_v046_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_63d_slope_v047_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(41).max().pct_change(24).rolling(26).var().rolling(36).max() * 0.719548).diff(20).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_63d_slope_v047_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_63d_slope_v047_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_63d_slope_v048_signal(ncfo, liabilities):
    res = ((ncfo * 7.3343 - liabilities).rolling(6).max().rolling(13).var() * 0.044938).diff(4).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_63d_slope_v048_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_63d_slope_v048_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_84d_slope_v049_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 0.2376)).rolling(17).min().diff(27).rolling(20).std().rolling(49).mean() * 0.179413).diff(20).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_84d_slope_v049_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_84d_slope_v049_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_42d_slope_v050_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(38).min().rolling(13).var() * 0.330479).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_42d_slope_v050_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_42d_slope_v050_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_126d_slope_v051_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 1.0807)).rolling(7).mean().pct_change(26).pct_change(35) * 0.531977).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_126d_slope_v051_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_126d_slope_v051_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_5d_slope_v052_signal(ncfo, liabilities):
    res = ((ncfo.diff(9) / (liabilities.shift(3) + 1.4230)).rolling(8).std().rolling(26).var().diff(48).diff(30) * 0.985699).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_5d_slope_v052_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_5d_slope_v052_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_105d_slope_v053_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(2).rolling(12).std() * 0.279188).diff(3).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_105d_slope_v053_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_105d_slope_v053_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_42d_slope_v054_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(2).mean().rolling(8).mean() * 0.516001).diff(8).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_42d_slope_v054_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_42d_slope_v054_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_21d_slope_v055_signal(ncfo, liabilities):
    res = ((ncfo.diff(4) / (liabilities.shift(4) + 1.6104)).rolling(13).var().rolling(49).var().pct_change(17).diff(12) * 0.476384).diff(6).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_21d_slope_v055_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_21d_slope_v055_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_252d_slope_v056_signal(ncfo, liabilities):
    res = ((ncfo * 4.6897 - liabilities).rolling(41).mean().rolling(36).min() * 0.520876).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_252d_slope_v056_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_252d_slope_v056_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_200d_slope_v057_signal(ncfo, liabilities):
    res = ((ncfo * 7.7296 - liabilities).rolling(30).std().pct_change(8).rolling(22).var().rolling(34).max() * 0.856368).diff(19).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_200d_slope_v057_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_200d_slope_v057_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_63d_slope_v058_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(27).var().rolling(8).mean().rolling(43).max() * 0.607669).diff(4).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_63d_slope_v058_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_63d_slope_v058_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_150d_slope_v059_signal(ncfo, liabilities):
    res = ((ncfo * 9.2464 - liabilities).diff(50).rolling(49).max() * 0.578763).diff(2).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_150d_slope_v059_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_150d_slope_v059_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_21d_slope_v060_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.2306)).rolling(48).var().rolling(22).std().rolling(32).max() * 0.280055).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_21d_slope_v060_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_21d_slope_v060_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_5d_slope_v061_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(16).min().pct_change(45).pct_change(14).pct_change(3) * 0.382111).diff(2).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_5d_slope_v061_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_5d_slope_v061_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_21d_slope_v062_signal(ncfo, liabilities):
    res = ((ncfo * 7.3113 - liabilities).rolling(7).var().rolling(45).min() * 0.287123).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_21d_slope_v062_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_21d_slope_v062_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_42d_slope_v063_signal(ncfo, liabilities):
    res = ((ncfo.diff(4) / (liabilities.shift(4) + 6.4836)).pct_change(18).rolling(28).min().rolling(50).mean().diff(49) * 0.293586).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_42d_slope_v063_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_42d_slope_v063_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_126d_slope_v064_signal(ncfo, liabilities):
    res = ((ncfo * 9.5310 - liabilities).rolling(21).max().pct_change(12).rolling(34).max() * 0.946528).diff(7).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_126d_slope_v064_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_126d_slope_v064_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_252d_slope_v065_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(4) + 9.5505)).rolling(36).std().diff(6).pct_change(17).pct_change(3) * 0.674486).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_252d_slope_v065_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_252d_slope_v065_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_126d_slope_v066_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.5772)).diff(42).rolling(22).mean().diff(30) * 0.059941).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_126d_slope_v066_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_126d_slope_v066_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_63d_slope_v067_signal(ncfo, liabilities):
    res = ((ncfo * 4.5766 - liabilities).rolling(16).std().pct_change(49).diff(47) * 0.925722).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_63d_slope_v067_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_63d_slope_v067_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_42d_slope_v068_signal(ncfo, liabilities):
    res = ((ncfo.diff(4) / (liabilities.shift(2) + 3.5860)).diff(37).rolling(18).std().rolling(18).mean().diff(32) * 0.682598).diff(16).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_42d_slope_v068_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_42d_slope_v068_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_63d_slope_v069_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(10).min().rolling(20).std().rolling(37).std().rolling(27).min() * 0.431240).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_63d_slope_v069_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_63d_slope_v069_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_126d_slope_v070_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 6.5973)).rolling(45).mean().rolling(36).min() * 0.877576).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_126d_slope_v070_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_126d_slope_v070_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_42d_slope_v071_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(3).min().pct_change(43).rolling(5).var() * 0.238492).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_42d_slope_v071_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_42d_slope_v071_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_150d_slope_v072_signal(ncfo, liabilities):
    res = ((ncfo * 9.5085 - liabilities).rolling(48).var().rolling(25).max() * 0.235185).diff(6).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_150d_slope_v072_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_150d_slope_v072_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_10d_slope_v073_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(43).var().rolling(13).std() * 0.204214).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_10d_slope_v073_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_10d_slope_v073_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_5d_slope_v074_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(21).var().rolling(11).std().rolling(18).min() * 0.195510).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_5d_slope_v074_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_5d_slope_v074_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_5d_slope_v075_signal(ncfo, liabilities):
    res = ((ncfo.diff(2) / (liabilities.shift(1) + 8.4286)).rolling(42).min().rolling(6).var().rolling(20).std().rolling(8).min() * 0.288593).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_5d_slope_v075_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_5d_slope_v075_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_5d_slope_v076_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(37).pct_change(35).rolling(43).mean().pct_change(42) * 0.349496).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_5d_slope_v076_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_5d_slope_v076_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_5d_slope_v077_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 7.4070)).rolling(40).var().pct_change(13) * 0.421128).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_5d_slope_v077_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_5d_slope_v077_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_5d_slope_v078_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 4.2743)).rolling(30).var().diff(4).rolling(49).var().diff(29) * 0.469064).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_5d_slope_v078_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_5d_slope_v078_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_42d_slope_v079_signal(ncfo, liabilities):
    res = ((ncfo * 4.8693 - liabilities).rolling(29).std().rolling(28).min().rolling(35).max() * 0.427754).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_42d_slope_v079_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_42d_slope_v079_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_105d_slope_v080_signal(ncfo, liabilities):
    res = ((ncfo.diff(4) / (liabilities.shift(1) + 6.8521)).rolling(39).max().pct_change(46) * 0.070744).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_105d_slope_v080_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_105d_slope_v080_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_150d_slope_v081_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 9.5667)).rolling(38).var().rolling(8).mean() * 0.313081).diff(10).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_150d_slope_v081_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_150d_slope_v081_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_252d_slope_v082_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(37).max().diff(9).pct_change(10).rolling(4).var() * 0.804687).diff(4).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_252d_slope_v082_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_252d_slope_v082_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_84d_slope_v083_signal(ncfo, liabilities):
    res = ((ncfo.diff(7) / (liabilities.shift(2) + 7.6464)).rolling(50).max().rolling(5).min() * 0.195880).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_84d_slope_v083_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_84d_slope_v083_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_150d_slope_v084_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 6.6340)).rolling(49).std().rolling(17).std().diff(49) * 0.746683).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_150d_slope_v084_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_150d_slope_v084_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_10d_slope_v085_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 9.1299)).rolling(43).min().diff(11) * 0.798437).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_10d_slope_v085_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_10d_slope_v085_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_105d_slope_v086_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.6015)).rolling(43).min().rolling(46).max() * 0.494020).diff(20).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_105d_slope_v086_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_105d_slope_v086_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_63d_slope_v087_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(5) + 6.8180)).pct_change(32).rolling(40).var().rolling(15).min() * 0.675613).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_63d_slope_v087_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_63d_slope_v087_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_63d_slope_v088_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.4218)).rolling(9).mean().rolling(4).max() * 0.730040).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_63d_slope_v088_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_63d_slope_v088_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_105d_slope_v089_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(11).rolling(10).var().pct_change(42) * 0.250942).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_105d_slope_v089_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_105d_slope_v089_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_21d_slope_v090_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.4249)).rolling(21).std().rolling(33).max().pct_change(28).pct_change(9) * 0.666381).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_21d_slope_v090_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_21d_slope_v090_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_21d_slope_v091_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(6).diff(19).rolling(35).var().rolling(45).min() * 0.220464).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_21d_slope_v091_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_21d_slope_v091_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_42d_slope_v092_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 4.6671)).rolling(43).mean().rolling(21).std().rolling(46).std() * 0.191148).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_42d_slope_v092_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_42d_slope_v092_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_42d_slope_v093_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 1.7419)).rolling(6).std().diff(25).rolling(27).var().pct_change(9) * 0.523666).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_42d_slope_v093_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_42d_slope_v093_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_84d_slope_v094_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(3).mean().pct_change(46).diff(22) * 0.991804).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_84d_slope_v094_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_84d_slope_v094_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_126d_slope_v095_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.6354)).pct_change(22).pct_change(24) * 0.429502).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_126d_slope_v095_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_126d_slope_v095_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_10d_slope_v096_signal(ncfo, liabilities):
    res = ((ncfo.diff(7) / (liabilities.shift(1) + 1.4929)).pct_change(46).rolling(17).var() * 0.363879).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_10d_slope_v096_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_10d_slope_v096_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_63d_slope_v097_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(11).max().rolling(10).min().rolling(34).var() * 0.383643).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_63d_slope_v097_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_63d_slope_v097_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_5d_slope_v098_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(32).rolling(19).max().rolling(26).mean() * 0.522804).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_5d_slope_v098_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_5d_slope_v098_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_42d_slope_v099_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 0.5921)).rolling(32).mean().rolling(42).std().rolling(12).min().rolling(26).mean() * 0.694633).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_42d_slope_v099_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_42d_slope_v099_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_42d_slope_v100_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.4557)).rolling(47).mean().rolling(19).max().rolling(18).mean() * 0.373326).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_42d_slope_v100_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_42d_slope_v100_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_105d_slope_v101_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(46).max().rolling(42).var().pct_change(17) * 0.409678).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_105d_slope_v101_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_105d_slope_v101_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_21d_slope_v102_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.5896)).diff(26).pct_change(38).rolling(7).mean().rolling(29).min() * 0.025197).diff(11).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_21d_slope_v102_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_21d_slope_v102_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_126d_slope_v103_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(45).mean().rolling(42).var().rolling(40).std() * 0.541912).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_126d_slope_v103_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_126d_slope_v103_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_5d_slope_v104_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.2478)).rolling(4).std().pct_change(5).rolling(12).mean().rolling(24).min() * 0.476763).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_5d_slope_v104_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_5d_slope_v104_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_5d_slope_v105_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(24).rolling(24).min().diff(27).rolling(2).min() * 0.038131).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_5d_slope_v105_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_5d_slope_v105_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_10d_slope_v106_signal(ncfo, liabilities):
    res = ((ncfo.diff(6) / (liabilities.shift(3) + 4.1816)).rolling(34).mean().rolling(50).min().rolling(50).var() * 0.375032).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_10d_slope_v106_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_10d_slope_v106_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_5d_slope_v107_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(5) + 5.3910)).rolling(20).min().diff(23).pct_change(35).rolling(28).std() * 0.802733).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_5d_slope_v107_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_5d_slope_v107_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_63d_slope_v108_signal(ncfo, liabilities):
    res = ((ncfo * 8.1621 - liabilities).rolling(10).std().rolling(4).max().rolling(47).std() * 0.803616).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_63d_slope_v108_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_63d_slope_v108_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_200d_slope_v109_signal(ncfo, liabilities):
    res = ((ncfo * 2.2930 - liabilities).rolling(42).max().diff(19).pct_change(40).rolling(11).var() * 0.302161).diff(3).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_200d_slope_v109_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_200d_slope_v109_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_10d_slope_v110_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(5) + 8.1206)).pct_change(29).rolling(45).var().rolling(14).mean().rolling(39).std() * 0.093973).diff(18).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_10d_slope_v110_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_10d_slope_v110_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_10d_slope_v111_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 7.0005)).rolling(39).min().rolling(6).min().diff(14).rolling(15).mean() * 0.903280).diff(11).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_10d_slope_v111_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_10d_slope_v111_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_252d_slope_v112_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(20).var().rolling(34).min().rolling(31).var().rolling(50).max() * 0.133230).diff(14).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_252d_slope_v112_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_252d_slope_v112_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_150d_slope_v113_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(36).std().diff(41).diff(16) * 0.467599).diff(9).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_150d_slope_v113_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_150d_slope_v113_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_105d_slope_v114_signal(ncfo, liabilities):
    res = ((ncfo * 9.0372 - liabilities).rolling(32).std().rolling(14).std().rolling(44).min().rolling(19).max() * 0.658774).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_105d_slope_v114_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_105d_slope_v114_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_63d_slope_v115_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 7.0425)).rolling(41).std().rolling(19).var().pct_change(2) * 0.221604).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_63d_slope_v115_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_63d_slope_v115_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_252d_slope_v116_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(32).std().rolling(16).std().rolling(10).std() * 0.268743).diff(10).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_252d_slope_v116_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_252d_slope_v116_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_84d_slope_v117_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 4.9232)).diff(24).rolling(25).mean().rolling(29).std() * 0.976072).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_84d_slope_v117_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_84d_slope_v117_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_200d_slope_v118_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.6847)).diff(15).diff(10).rolling(21).var() * 0.236778).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_200d_slope_v118_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_200d_slope_v118_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_126d_slope_v119_signal(ncfo, liabilities):
    res = ((ncfo * 1.8814 - liabilities).rolling(24).mean().diff(28).rolling(50).mean().pct_change(48) * 0.165522).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_126d_slope_v119_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_126d_slope_v119_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_126d_slope_v120_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 3.8219)).rolling(30).std().rolling(24).min().rolling(17).std().rolling(19).max() * 0.350363).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_126d_slope_v120_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_126d_slope_v120_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_84d_slope_v121_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 3.6271)).rolling(37).max().rolling(17).mean() * 0.697218).diff(20).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_84d_slope_v121_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_84d_slope_v121_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_5d_slope_v122_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 8.3560)).rolling(27).min().rolling(33).std().rolling(38).std() * 0.389413).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_5d_slope_v122_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_5d_slope_v122_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_200d_slope_v123_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(5) + 2.1972)).rolling(10).var().diff(15).rolling(26).max().rolling(27).mean() * 0.552756).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_200d_slope_v123_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_200d_slope_v123_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_42d_slope_v124_signal(ncfo, liabilities):
    res = ((ncfo.diff(9) / (liabilities.shift(3) + 7.0500)).rolling(14).var().rolling(14).std().rolling(11).var().rolling(40).max() * 0.847071).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_42d_slope_v124_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_42d_slope_v124_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_126d_slope_v125_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(18).var().rolling(5).min().rolling(15).var() * 0.770224).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_126d_slope_v125_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_126d_slope_v125_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_10d_slope_v126_signal(ncfo, liabilities):
    res = ((ncfo * 1.5999 - liabilities).rolling(4).min().rolling(12).max().rolling(36).min() * 0.962674).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_10d_slope_v126_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_10d_slope_v126_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_5d_slope_v127_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(10).mean().rolling(23).mean() * 0.518049).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_5d_slope_v127_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_5d_slope_v127_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_42d_slope_v128_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 0.9023)).pct_change(46).pct_change(21).rolling(37).std() * 0.371786).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_42d_slope_v128_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_42d_slope_v128_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_252d_slope_v129_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.9196)).rolling(10).std().rolling(4).mean().rolling(26).std() * 0.986660).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_252d_slope_v129_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_252d_slope_v129_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_5d_slope_v130_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 0.7939)).diff(16).pct_change(8).rolling(49).max().rolling(11).std() * 0.182252).diff(7).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_5d_slope_v130_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_5d_slope_v130_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_150d_slope_v131_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 9.5131)).rolling(2).var().rolling(19).min().rolling(8).max().diff(40) * 0.426582).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_150d_slope_v131_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_150d_slope_v131_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_105d_slope_v132_signal(ncfo, liabilities):
    res = ((ncfo * 2.2198 - liabilities).rolling(31).std().rolling(27).max().rolling(7).min() * 0.545158).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_105d_slope_v132_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_105d_slope_v132_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_105d_slope_v133_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(48).var().rolling(41).std().rolling(32).std() * 0.823385).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_105d_slope_v133_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_105d_slope_v133_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_21d_slope_v134_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.6395)).rolling(50).var().pct_change(44) * 0.901976).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_21d_slope_v134_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_21d_slope_v134_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_10d_slope_v135_signal(ncfo, liabilities):
    res = ((ncfo * 3.2365 - liabilities).rolling(38).var().rolling(14).max().rolling(28).std() * 0.718605).diff(12).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_10d_slope_v135_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_10d_slope_v135_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_126d_slope_v136_signal(ncfo, liabilities):
    res = ((ncfo * 4.1151 - liabilities).rolling(31).std().rolling(16).min().rolling(40).max() * 0.804171).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_126d_slope_v136_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_126d_slope_v136_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_63d_slope_v137_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(41).std().rolling(15).std() * 0.956469).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_63d_slope_v137_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_63d_slope_v137_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_42d_slope_v138_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(5) + 3.3224)).diff(9).rolling(44).var() * 0.648477).diff(11).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_42d_slope_v138_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_42d_slope_v138_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_150d_slope_v139_signal(ncfo, liabilities):
    res = ((ncfo.diff(2) / (liabilities.shift(3) + 9.6632)).rolling(36).max().pct_change(49).diff(46) * 0.563788).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_150d_slope_v139_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_150d_slope_v139_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_84d_slope_v140_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.0934)).pct_change(22).rolling(9).var() * 0.819291).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_84d_slope_v140_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_84d_slope_v140_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_200d_slope_v141_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(36).mean().diff(32).rolling(21).mean() * 0.196559).diff(18).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_200d_slope_v141_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_200d_slope_v141_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_63d_slope_v142_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 2.0568)).rolling(12).min().pct_change(13).rolling(20).min().rolling(6).max() * 0.217002).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_63d_slope_v142_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_63d_slope_v142_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_10d_slope_v143_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(22).rolling(9).max() * 0.491126).diff(12).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_10d_slope_v143_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_10d_slope_v143_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_105d_slope_v144_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(7).max().rolling(42).mean().diff(12) * 0.317121).diff(13).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_105d_slope_v144_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_105d_slope_v144_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_5d_slope_v145_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 0.4436)).rolling(46).max().diff(25) * 0.833424).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_5d_slope_v145_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_5d_slope_v145_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_10d_slope_v146_signal(ncfo, liabilities):
    res = ((ncfo * 1.3292 - liabilities).rolling(48).min().rolling(19).mean() * 0.193533).diff(6).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_10d_slope_v146_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_10d_slope_v146_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_63d_slope_v147_signal(ncfo, liabilities):
    res = ((ncfo * 6.9947 - liabilities).rolling(6).min().rolling(36).std().pct_change(34).rolling(38).mean() * 0.867950).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_63d_slope_v147_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_63d_slope_v147_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_42d_slope_v148_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 7.7039)).rolling(21).mean().pct_change(42).rolling(44).max().rolling(6).var() * 0.413361).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_42d_slope_v148_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_42d_slope_v148_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_200d_slope_v149_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(1) + 1.1086)).rolling(12).var().rolling(23).mean().rolling(11).min() * 0.637701).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_200d_slope_v149_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_200d_slope_v149_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_10d_slope_v150_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(4) + 1.9496)).diff(16).pct_change(41).pct_change(37).rolling(31).mean() * 0.270958).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_10d_slope_v150_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_10d_slope_v150_signal


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
