import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f204r_f204_revenue_growth_relative_to_equity_calc001_63d_slope_v001_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(3) + 2.0034)).rolling(22).std().rolling(18).std().diff(6).rolling(45).min() * 0.703379).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc001_63d_slope_v001_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc001_63d_slope_v001_signal

def f204r_f204_revenue_growth_relative_to_equity_calc002_150d_slope_v002_signal(revenue, equity):
    res = ((revenue.diff(2) / (equity.shift(4) + 9.0310)).pct_change(28).rolling(30).mean().rolling(28).min().rolling(15).var() * 0.235223).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc002_150d_slope_v002_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc002_150d_slope_v002_signal

def f204r_f204_revenue_growth_relative_to_equity_calc003_5d_slope_v003_signal(revenue, equity):
    res = ((revenue * 0.2031 - equity).rolling(44).var().rolling(10).max().rolling(12).max().pct_change(9) * 0.410745).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc003_5d_slope_v003_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc003_5d_slope_v003_signal

def f204r_f204_revenue_growth_relative_to_equity_calc004_252d_slope_v004_signal(revenue, equity):
    res = ((equity / (revenue + 3.1118)).pct_change(19).diff(25).rolling(36).min() * 0.147070).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc004_252d_slope_v004_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc004_252d_slope_v004_signal

def f204r_f204_revenue_growth_relative_to_equity_calc005_200d_slope_v005_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(3) + 5.3062)).rolling(27).mean().rolling(48).min() * 0.699090).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc005_200d_slope_v005_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc005_200d_slope_v005_signal

def f204r_f204_revenue_growth_relative_to_equity_calc006_126d_slope_v006_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(2) + 2.0648)).rolling(48).std().rolling(35).max().rolling(15).max().diff(48) * 0.594293).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc006_126d_slope_v006_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc006_126d_slope_v006_signal

def f204r_f204_revenue_growth_relative_to_equity_calc007_42d_slope_v007_signal(revenue, equity):
    res = ((equity / (revenue + 3.4591)).rolling(35).max().pct_change(22).rolling(12).min().pct_change(4) * 0.753808).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc007_42d_slope_v007_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc007_42d_slope_v007_signal

def f204r_f204_revenue_growth_relative_to_equity_calc008_252d_slope_v008_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(5) + 9.5450)).diff(9).rolling(39).min().diff(25) * 0.432733).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc008_252d_slope_v008_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc008_252d_slope_v008_signal

def f204r_f204_revenue_growth_relative_to_equity_calc009_105d_slope_v009_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(23).max().rolling(38).mean() * 0.698002).diff(17).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc009_105d_slope_v009_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc009_105d_slope_v009_signal

def f204r_f204_revenue_growth_relative_to_equity_calc010_21d_slope_v010_signal(revenue, equity):
    res = ((revenue.diff(6) / (equity.shift(2) + 8.9178)).rolling(7).std().rolling(27).min().diff(12) * 0.315306).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc010_21d_slope_v010_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc010_21d_slope_v010_signal

def f204r_f204_revenue_growth_relative_to_equity_calc011_21d_slope_v011_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(11).mean().rolling(4).mean().diff(23).pct_change(50) * 0.921640).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc011_21d_slope_v011_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc011_21d_slope_v011_signal

def f204r_f204_revenue_growth_relative_to_equity_calc012_150d_slope_v012_signal(revenue, equity):
    res = ((equity / (revenue + 4.2318)).pct_change(19).rolling(29).max().rolling(28).mean() * 0.217279).diff(4).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc012_150d_slope_v012_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc012_150d_slope_v012_signal

def f204r_f204_revenue_growth_relative_to_equity_calc013_84d_slope_v013_signal(revenue, equity):
    res = ((revenue * 4.3667 - equity).rolling(31).mean().diff(14) * 0.154787).diff(10).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc013_84d_slope_v013_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc013_84d_slope_v013_signal

def f204r_f204_revenue_growth_relative_to_equity_calc014_150d_slope_v014_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(33).rolling(26).mean().rolling(11).std().rolling(20).var() * 0.804620).diff(2).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc014_150d_slope_v014_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc014_150d_slope_v014_signal

def f204r_f204_revenue_growth_relative_to_equity_calc015_63d_slope_v015_signal(revenue, equity):
    res = ((revenue / (equity + 5.4652)).diff(9).diff(35) * 0.569865).diff(20).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc015_63d_slope_v015_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc015_63d_slope_v015_signal

def f204r_f204_revenue_growth_relative_to_equity_calc016_63d_slope_v016_signal(revenue, equity):
    res = ((equity / (revenue + 3.5350)).pct_change(13).pct_change(2) * 0.193240).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc016_63d_slope_v016_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc016_63d_slope_v016_signal

def f204r_f204_revenue_growth_relative_to_equity_calc017_5d_slope_v017_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(32).var().rolling(2).std().diff(16).pct_change(30) * 0.553063).diff(4).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc017_5d_slope_v017_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc017_5d_slope_v017_signal

def f204r_f204_revenue_growth_relative_to_equity_calc018_126d_slope_v018_signal(revenue, equity):
    res = ((revenue * 7.5300 - equity).diff(26).pct_change(50) * 0.076201).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc018_126d_slope_v018_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc018_126d_slope_v018_signal

def f204r_f204_revenue_growth_relative_to_equity_calc019_63d_slope_v019_signal(revenue, equity):
    res = ((revenue * 1.4200 - equity).rolling(46).var().rolling(21).mean().pct_change(4) * 0.092790).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc019_63d_slope_v019_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc019_63d_slope_v019_signal

def f204r_f204_revenue_growth_relative_to_equity_calc020_10d_slope_v020_signal(revenue, equity):
    res = ((equity / (revenue + 2.0329)).rolling(11).mean().rolling(7).max().pct_change(35).rolling(18).var() * 0.984813).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc020_10d_slope_v020_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc020_10d_slope_v020_signal

def f204r_f204_revenue_growth_relative_to_equity_calc021_84d_slope_v021_signal(revenue, equity):
    res = ((revenue / (equity + 7.7114)).rolling(9).var().rolling(19).std() * 0.757429).diff(19).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc021_84d_slope_v021_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc021_84d_slope_v021_signal

def f204r_f204_revenue_growth_relative_to_equity_calc022_200d_slope_v022_signal(revenue, equity):
    res = ((revenue / (equity + 9.6561)).rolling(22).min().rolling(43).max().rolling(18).min().rolling(16).mean() * 0.900558).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc022_200d_slope_v022_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc022_200d_slope_v022_signal

def f204r_f204_revenue_growth_relative_to_equity_calc023_105d_slope_v023_signal(revenue, equity):
    res = ((revenue / (equity + 0.1806)).rolling(35).std().rolling(26).max() * 0.620905).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc023_105d_slope_v023_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc023_105d_slope_v023_signal

def f204r_f204_revenue_growth_relative_to_equity_calc024_63d_slope_v024_signal(revenue, equity):
    res = ((revenue * 7.8750 - equity).pct_change(20).pct_change(21).rolling(46).min().rolling(21).mean() * 0.886368).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc024_63d_slope_v024_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc024_63d_slope_v024_signal

def f204r_f204_revenue_growth_relative_to_equity_calc025_105d_slope_v025_signal(revenue, equity):
    res = ((revenue / (equity + 5.2386)).rolling(20).std().rolling(3).var().rolling(39).max() * 0.454897).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc025_105d_slope_v025_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc025_105d_slope_v025_signal

def f204r_f204_revenue_growth_relative_to_equity_calc026_10d_slope_v026_signal(revenue, equity):
    res = ((revenue / (equity + 1.2338)).rolling(9).std().diff(31).rolling(35).min() * 0.858386).diff(18).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc026_10d_slope_v026_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc026_10d_slope_v026_signal

def f204r_f204_revenue_growth_relative_to_equity_calc027_126d_slope_v027_signal(revenue, equity):
    res = ((equity / (revenue + 6.4559)).diff(36).rolling(29).min().rolling(24).min() * 0.779962).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc027_126d_slope_v027_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc027_126d_slope_v027_signal

def f204r_f204_revenue_growth_relative_to_equity_calc028_252d_slope_v028_signal(revenue, equity):
    res = ((revenue.diff(10) / (equity.shift(1) + 6.3775)).rolling(42).std().rolling(24).mean().rolling(22).var() * 0.632265).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc028_252d_slope_v028_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc028_252d_slope_v028_signal

def f204r_f204_revenue_growth_relative_to_equity_calc029_150d_slope_v029_signal(revenue, equity):
    res = ((revenue * 7.9983 - equity).rolling(14).max().rolling(31).min().rolling(27).min() * 0.289668).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc029_150d_slope_v029_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc029_150d_slope_v029_signal

def f204r_f204_revenue_growth_relative_to_equity_calc030_252d_slope_v030_signal(revenue, equity):
    res = ((revenue / (equity + 0.9578)).rolling(31).min().pct_change(45).rolling(21).var().diff(21) * 0.389974).diff(18).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc030_252d_slope_v030_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc030_252d_slope_v030_signal

def f204r_f204_revenue_growth_relative_to_equity_calc031_63d_slope_v031_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(1) + 4.8328)).rolling(24).max().rolling(4).var() * 0.396799).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc031_63d_slope_v031_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc031_63d_slope_v031_signal

def f204r_f204_revenue_growth_relative_to_equity_calc032_105d_slope_v032_signal(revenue, equity):
    res = ((equity / (revenue + 5.4879)).rolling(11).max().diff(46) * 0.418780).diff(13).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc032_105d_slope_v032_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc032_105d_slope_v032_signal

def f204r_f204_revenue_growth_relative_to_equity_calc033_200d_slope_v033_signal(revenue, equity):
    res = ((revenue / (equity + 4.5578)).rolling(5).max().rolling(11).var() * 0.894426).diff(20).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc033_200d_slope_v033_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc033_200d_slope_v033_signal

def f204r_f204_revenue_growth_relative_to_equity_calc034_252d_slope_v034_signal(revenue, equity):
    res = ((revenue * 9.1188 - equity).rolling(37).max().rolling(44).min().pct_change(49) * 0.279972).diff(6).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc034_252d_slope_v034_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc034_252d_slope_v034_signal

def f204r_f204_revenue_growth_relative_to_equity_calc035_126d_slope_v035_signal(revenue, equity):
    res = ((equity / (revenue + 1.4097)).rolling(2).min().rolling(14).mean().rolling(26).mean().rolling(37).std() * 0.558650).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc035_126d_slope_v035_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc035_126d_slope_v035_signal

def f204r_f204_revenue_growth_relative_to_equity_calc036_150d_slope_v036_signal(revenue, equity):
    res = ((revenue / (equity + 0.3257)).rolling(46).mean().rolling(7).std().rolling(26).var().pct_change(27) * 0.490169).diff(8).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc036_150d_slope_v036_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc036_150d_slope_v036_signal

def f204r_f204_revenue_growth_relative_to_equity_calc037_84d_slope_v037_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(32).rolling(39).std() * 0.017705).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc037_84d_slope_v037_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc037_84d_slope_v037_signal

def f204r_f204_revenue_growth_relative_to_equity_calc038_5d_slope_v038_signal(revenue, equity):
    res = ((equity / (revenue + 9.3535)).diff(10).rolling(43).var().rolling(27).min().pct_change(17) * 0.961515).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc038_5d_slope_v038_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc038_5d_slope_v038_signal

def f204r_f204_revenue_growth_relative_to_equity_calc039_63d_slope_v039_signal(revenue, equity):
    res = ((revenue * 7.0271 - equity).rolling(35).min().rolling(46).min().rolling(29).min().rolling(21).var() * 0.979815).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc039_63d_slope_v039_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc039_63d_slope_v039_signal

def f204r_f204_revenue_growth_relative_to_equity_calc040_200d_slope_v040_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(2) + 4.1678)).rolling(37).std().diff(47).rolling(8).min() * 0.032243).diff(19).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc040_200d_slope_v040_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc040_200d_slope_v040_signal

def f204r_f204_revenue_growth_relative_to_equity_calc041_63d_slope_v041_signal(revenue, equity):
    res = ((revenue.diff(4) / (equity.shift(5) + 9.1416)).rolling(32).max().pct_change(34) * 0.417098).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc041_63d_slope_v041_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc041_63d_slope_v041_signal

def f204r_f204_revenue_growth_relative_to_equity_calc042_150d_slope_v042_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(5).max().rolling(24).mean() * 0.426550).diff(20).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc042_150d_slope_v042_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc042_150d_slope_v042_signal

def f204r_f204_revenue_growth_relative_to_equity_calc043_42d_slope_v043_signal(revenue, equity):
    res = ((equity / (revenue + 7.8623)).rolling(48).std().rolling(21).min().rolling(42).mean().rolling(10).max() * 0.068227).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc043_42d_slope_v043_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc043_42d_slope_v043_signal

def f204r_f204_revenue_growth_relative_to_equity_calc044_105d_slope_v044_signal(revenue, equity):
    res = ((equity / (revenue + 4.5688)).rolling(12).max().pct_change(12).rolling(26).max() * 0.154243).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc044_105d_slope_v044_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc044_105d_slope_v044_signal

def f204r_f204_revenue_growth_relative_to_equity_calc045_42d_slope_v045_signal(revenue, equity):
    res = ((revenue.diff(8) / (equity.shift(4) + 5.6791)).diff(46).rolling(14).max().rolling(21).min() * 0.558909).diff(9).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc045_42d_slope_v045_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc045_42d_slope_v045_signal

def f204r_f204_revenue_growth_relative_to_equity_calc046_150d_slope_v046_signal(revenue, equity):
    res = ((equity / (revenue + 9.5927)).diff(22).diff(34).rolling(42).min().rolling(32).min() * 0.328072).diff(18).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc046_150d_slope_v046_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc046_150d_slope_v046_signal

def f204r_f204_revenue_growth_relative_to_equity_calc047_42d_slope_v047_signal(revenue, equity):
    res = ((revenue * 5.8191 - equity).pct_change(17).rolling(42).mean().rolling(35).max().rolling(9).var() * 0.512846).diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc047_42d_slope_v047_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc047_42d_slope_v047_signal

def f204r_f204_revenue_growth_relative_to_equity_calc048_42d_slope_v048_signal(revenue, equity):
    res = ((revenue.diff(5) / (equity.shift(5) + 0.2910)).rolling(7).std().rolling(50).mean() * 0.923427).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc048_42d_slope_v048_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc048_42d_slope_v048_signal

def f204r_f204_revenue_growth_relative_to_equity_calc049_200d_slope_v049_signal(revenue, equity):
    res = ((equity / (revenue + 5.0220)).rolling(18).var().rolling(11).var().rolling(22).std().rolling(40).min() * 0.069265).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc049_200d_slope_v049_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc049_200d_slope_v049_signal

def f204r_f204_revenue_growth_relative_to_equity_calc050_63d_slope_v050_signal(revenue, equity):
    res = ((equity / (revenue + 7.6966)).rolling(48).std().rolling(24).std() * 0.479356).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc050_63d_slope_v050_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc050_63d_slope_v050_signal

def f204r_f204_revenue_growth_relative_to_equity_calc051_200d_slope_v051_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(5).max().rolling(17).min().diff(15).pct_change(9) * 0.100124).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc051_200d_slope_v051_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc051_200d_slope_v051_signal

def f204r_f204_revenue_growth_relative_to_equity_calc052_252d_slope_v052_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(49).max().rolling(40).min().pct_change(50) * 0.743605).diff(18).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc052_252d_slope_v052_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc052_252d_slope_v052_signal

def f204r_f204_revenue_growth_relative_to_equity_calc053_84d_slope_v053_signal(revenue, equity):
    res = ((revenue * 5.9386 - equity).rolling(23).min().pct_change(21).pct_change(19).rolling(48).std() * 0.387342).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc053_84d_slope_v053_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc053_84d_slope_v053_signal

def f204r_f204_revenue_growth_relative_to_equity_calc054_252d_slope_v054_signal(revenue, equity):
    res = ((revenue * 0.3066 - equity).rolling(32).var().rolling(35).std().rolling(33).var().rolling(43).max() * 0.030976).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc054_252d_slope_v054_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc054_252d_slope_v054_signal

def f204r_f204_revenue_growth_relative_to_equity_calc055_21d_slope_v055_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(3) + 1.0354)).rolling(32).std().rolling(27).mean().rolling(17).max() * 0.433417).diff(9).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc055_21d_slope_v055_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc055_21d_slope_v055_signal

def f204r_f204_revenue_growth_relative_to_equity_calc056_21d_slope_v056_signal(revenue, equity):
    res = ((revenue * 1.1055 - equity).rolling(23).max().rolling(20).max() * 0.267810).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc056_21d_slope_v056_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc056_21d_slope_v056_signal

def f204r_f204_revenue_growth_relative_to_equity_calc057_84d_slope_v057_signal(revenue, equity):
    res = ((revenue / (equity + 5.6805)).rolling(24).mean().rolling(7).var().rolling(25).min() * 0.140769).diff(20).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc057_84d_slope_v057_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc057_84d_slope_v057_signal

def f204r_f204_revenue_growth_relative_to_equity_calc058_5d_slope_v058_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(1) + 6.1281)).pct_change(24).rolling(4).std().rolling(18).std().pct_change(41) * 0.683274).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc058_5d_slope_v058_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc058_5d_slope_v058_signal

def f204r_f204_revenue_growth_relative_to_equity_calc059_42d_slope_v059_signal(revenue, equity):
    res = ((equity / (revenue + 6.2711)).diff(2).rolling(47).std().diff(15).rolling(22).mean() * 0.316711).diff(19).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc059_42d_slope_v059_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc059_42d_slope_v059_signal

def f204r_f204_revenue_growth_relative_to_equity_calc060_21d_slope_v060_signal(revenue, equity):
    res = ((revenue.diff(2) / (equity.shift(1) + 0.3226)).rolling(47).std().pct_change(22) * 0.181343).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc060_21d_slope_v060_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc060_21d_slope_v060_signal

def f204r_f204_revenue_growth_relative_to_equity_calc061_21d_slope_v061_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(3) + 1.4221)).rolling(32).max().rolling(3).mean().rolling(9).var() * 0.995791).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc061_21d_slope_v061_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc061_21d_slope_v061_signal

def f204r_f204_revenue_growth_relative_to_equity_calc062_21d_slope_v062_signal(revenue, equity):
    res = ((equity / (revenue + 8.6312)).rolling(33).max().rolling(50).max().pct_change(46).rolling(42).std() * 0.369115).diff(17).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc062_21d_slope_v062_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc062_21d_slope_v062_signal

def f204r_f204_revenue_growth_relative_to_equity_calc063_150d_slope_v063_signal(revenue, equity):
    res = ((revenue / (equity + 7.3548)).rolling(18).min().pct_change(2).rolling(9).var() * 0.561916).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc063_150d_slope_v063_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc063_150d_slope_v063_signal

def f204r_f204_revenue_growth_relative_to_equity_calc064_126d_slope_v064_signal(revenue, equity):
    res = ((revenue * 6.6200 - equity).rolling(14).var().rolling(35).mean() * 0.789256).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc064_126d_slope_v064_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc064_126d_slope_v064_signal

def f204r_f204_revenue_growth_relative_to_equity_calc065_252d_slope_v065_signal(revenue, equity):
    res = ((revenue / (equity + 9.3914)).pct_change(23).rolling(10).max() * 0.048564).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc065_252d_slope_v065_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc065_252d_slope_v065_signal

def f204r_f204_revenue_growth_relative_to_equity_calc066_252d_slope_v066_signal(revenue, equity):
    res = ((revenue * 1.5829 - equity).rolling(28).mean().rolling(41).std().rolling(27).var().rolling(45).std() * 0.783366).diff(7).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc066_252d_slope_v066_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc066_252d_slope_v066_signal

def f204r_f204_revenue_growth_relative_to_equity_calc067_42d_slope_v067_signal(revenue, equity):
    res = ((revenue * 0.9931 - equity).rolling(14).std().pct_change(46).diff(44).rolling(22).max() * 0.946916).diff(9).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc067_42d_slope_v067_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc067_42d_slope_v067_signal

def f204r_f204_revenue_growth_relative_to_equity_calc068_21d_slope_v068_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(40).std().diff(46).rolling(14).max().rolling(18).min() * 0.816516).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc068_21d_slope_v068_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc068_21d_slope_v068_signal

def f204r_f204_revenue_growth_relative_to_equity_calc069_42d_slope_v069_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(19).rolling(11).max().diff(4) * 0.504698).diff(6).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc069_42d_slope_v069_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc069_42d_slope_v069_signal

def f204r_f204_revenue_growth_relative_to_equity_calc070_252d_slope_v070_signal(revenue, equity):
    res = ((revenue.diff(5) / (equity.shift(3) + 1.7832)).rolling(13).max().rolling(32).var().rolling(17).mean() * 0.258868).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc070_252d_slope_v070_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc070_252d_slope_v070_signal

def f204r_f204_revenue_growth_relative_to_equity_calc071_105d_slope_v071_signal(revenue, equity):
    res = ((revenue / (equity + 6.1426)).rolling(11).var().rolling(4).std() * 0.317659).diff(13).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc071_105d_slope_v071_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc071_105d_slope_v071_signal

def f204r_f204_revenue_growth_relative_to_equity_calc072_63d_slope_v072_signal(revenue, equity):
    res = ((revenue * 0.2392 - equity).rolling(42).max().rolling(37).min().rolling(31).var() * 0.371928).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc072_63d_slope_v072_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc072_63d_slope_v072_signal

def f204r_f204_revenue_growth_relative_to_equity_calc073_84d_slope_v073_signal(revenue, equity):
    res = ((revenue.diff(4) / (equity.shift(2) + 7.0274)).rolling(43).min().rolling(12).std().rolling(27).var().pct_change(44) * 0.307121).diff(19).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc073_84d_slope_v073_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc073_84d_slope_v073_signal

def f204r_f204_revenue_growth_relative_to_equity_calc074_42d_slope_v074_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(1) + 3.0030)).rolling(29).max().diff(27) * 0.376334).diff(8).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc074_42d_slope_v074_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc074_42d_slope_v074_signal

def f204r_f204_revenue_growth_relative_to_equity_calc075_5d_slope_v075_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(30).rolling(43).max().diff(48) * 0.569119).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc075_5d_slope_v075_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc075_5d_slope_v075_signal

def f204r_f204_revenue_growth_relative_to_equity_calc076_126d_slope_v076_signal(revenue, equity):
    res = ((revenue.diff(10) / (equity.shift(1) + 1.6346)).rolling(41).min().rolling(29).max().rolling(2).var() * 0.844432).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc076_126d_slope_v076_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc076_126d_slope_v076_signal

def f204r_f204_revenue_growth_relative_to_equity_calc077_63d_slope_v077_signal(revenue, equity):
    res = ((equity / (revenue + 5.4297)).pct_change(25).pct_change(34).rolling(34).min() * 0.398491).diff(7).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc077_63d_slope_v077_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc077_63d_slope_v077_signal

def f204r_f204_revenue_growth_relative_to_equity_calc078_252d_slope_v078_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(5) + 0.4827)).pct_change(4).rolling(8).std().rolling(8).mean() * 0.313227).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc078_252d_slope_v078_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc078_252d_slope_v078_signal

def f204r_f204_revenue_growth_relative_to_equity_calc079_126d_slope_v079_signal(revenue, equity):
    res = ((revenue.diff(5) / (equity.shift(4) + 8.5882)).diff(11).rolling(20).max().rolling(19).max().rolling(45).std() * 0.298081).diff(9).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc079_126d_slope_v079_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc079_126d_slope_v079_signal

def f204r_f204_revenue_growth_relative_to_equity_calc080_150d_slope_v080_signal(revenue, equity):
    res = ((revenue * 5.6725 - equity).rolling(36).mean().rolling(50).mean().rolling(32).std() * 0.978597).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc080_150d_slope_v080_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc080_150d_slope_v080_signal

def f204r_f204_revenue_growth_relative_to_equity_calc081_21d_slope_v081_signal(revenue, equity):
    res = ((revenue.diff(6) / (equity.shift(4) + 6.5029)).rolling(24).min().rolling(17).std().rolling(24).std().rolling(42).min() * 0.625123).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc081_21d_slope_v081_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc081_21d_slope_v081_signal

def f204r_f204_revenue_growth_relative_to_equity_calc082_150d_slope_v082_signal(revenue, equity):
    res = ((revenue * 8.0469 - equity).rolling(11).max().rolling(39).var() * 0.956591).diff(4).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc082_150d_slope_v082_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc082_150d_slope_v082_signal

def f204r_f204_revenue_growth_relative_to_equity_calc083_105d_slope_v083_signal(revenue, equity):
    res = ((revenue / (equity + 1.3386)).rolling(36).min().diff(5).rolling(28).min().rolling(45).var() * 0.022061).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc083_105d_slope_v083_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc083_105d_slope_v083_signal

def f204r_f204_revenue_growth_relative_to_equity_calc084_5d_slope_v084_signal(revenue, equity):
    res = ((equity / (revenue + 5.9423)).rolling(20).mean().pct_change(18).rolling(46).std() * 0.745999).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc084_5d_slope_v084_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc084_5d_slope_v084_signal

def f204r_f204_revenue_growth_relative_to_equity_calc085_105d_slope_v085_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(37).var().diff(44).rolling(26).std() * 0.025677).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc085_105d_slope_v085_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc085_105d_slope_v085_signal

def f204r_f204_revenue_growth_relative_to_equity_calc086_105d_slope_v086_signal(revenue, equity):
    res = ((revenue * 4.4831 - equity).diff(46).diff(11).rolling(28).min() * 0.022666).diff(12).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc086_105d_slope_v086_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc086_105d_slope_v086_signal

def f204r_f204_revenue_growth_relative_to_equity_calc087_200d_slope_v087_signal(revenue, equity):
    res = ((revenue / (equity + 4.0523)).rolling(25).min().rolling(44).std().pct_change(6) * 0.601174).diff(7).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc087_200d_slope_v087_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc087_200d_slope_v087_signal

def f204r_f204_revenue_growth_relative_to_equity_calc088_252d_slope_v088_signal(revenue, equity):
    res = ((revenue * 9.6487 - equity).rolling(24).max().pct_change(39).rolling(14).mean() * 0.176762).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc088_252d_slope_v088_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc088_252d_slope_v088_signal

def f204r_f204_revenue_growth_relative_to_equity_calc089_200d_slope_v089_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(5) + 2.3907)).pct_change(49).rolling(18).mean().diff(14).diff(45) * 0.402220).diff(6).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc089_200d_slope_v089_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc089_200d_slope_v089_signal

def f204r_f204_revenue_growth_relative_to_equity_calc090_5d_slope_v090_signal(revenue, equity):
    res = ((revenue.diff(2) / (equity.shift(2) + 7.5190)).rolling(45).max().rolling(3).mean() * 0.905568).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc090_5d_slope_v090_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc090_5d_slope_v090_signal

def f204r_f204_revenue_growth_relative_to_equity_calc091_5d_slope_v091_signal(revenue, equity):
    res = ((revenue * 2.3299 - equity).rolling(6).std().rolling(13).min().rolling(24).var() * 0.532289).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc091_5d_slope_v091_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc091_5d_slope_v091_signal

def f204r_f204_revenue_growth_relative_to_equity_calc092_105d_slope_v092_signal(revenue, equity):
    res = ((revenue / (equity + 6.7378)).diff(50).rolling(2).mean().rolling(2).max() * 0.938426).diff(19).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc092_105d_slope_v092_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc092_105d_slope_v092_signal

def f204r_f204_revenue_growth_relative_to_equity_calc093_200d_slope_v093_signal(revenue, equity):
    res = ((revenue / (equity + 7.1239)).rolling(15).var().rolling(47).var() * 0.488570).diff(6).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc093_200d_slope_v093_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc093_200d_slope_v093_signal

def f204r_f204_revenue_growth_relative_to_equity_calc094_126d_slope_v094_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(3) + 4.0777)).rolling(17).min().rolling(34).min() * 0.903327).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc094_126d_slope_v094_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc094_126d_slope_v094_signal

def f204r_f204_revenue_growth_relative_to_equity_calc095_63d_slope_v095_signal(revenue, equity):
    res = ((revenue / (equity + 6.4338)).rolling(21).min().diff(6).rolling(7).std().rolling(35).mean() * 0.209492).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc095_63d_slope_v095_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc095_63d_slope_v095_signal

def f204r_f204_revenue_growth_relative_to_equity_calc096_21d_slope_v096_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(11).pct_change(46).pct_change(11).rolling(23).std() * 0.498167).diff(13).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc096_21d_slope_v096_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc096_21d_slope_v096_signal

def f204r_f204_revenue_growth_relative_to_equity_calc097_63d_slope_v097_signal(revenue, equity):
    res = ((revenue.diff(4) / (equity.shift(5) + 9.5515)).rolling(46).min().diff(37).rolling(28).std().rolling(48).mean() * 0.125901).diff(4).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc097_63d_slope_v097_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc097_63d_slope_v097_signal

def f204r_f204_revenue_growth_relative_to_equity_calc098_10d_slope_v098_signal(revenue, equity):
    res = ((revenue / (equity + 7.2584)).diff(45).diff(43) * 0.415504).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc098_10d_slope_v098_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc098_10d_slope_v098_signal

def f204r_f204_revenue_growth_relative_to_equity_calc099_84d_slope_v099_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(17).diff(8).diff(30).pct_change(10) * 0.944466).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc099_84d_slope_v099_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc099_84d_slope_v099_signal

def f204r_f204_revenue_growth_relative_to_equity_calc100_150d_slope_v100_signal(revenue, equity):
    res = ((equity / (revenue + 9.2225)).rolling(36).var().rolling(45).mean().rolling(46).mean().rolling(2).mean() * 0.011954).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc100_150d_slope_v100_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc100_150d_slope_v100_signal

def f204r_f204_revenue_growth_relative_to_equity_calc101_200d_slope_v101_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(3) + 5.8455)).rolling(14).mean().rolling(45).min().rolling(30).min().rolling(18).max() * 0.058657).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc101_200d_slope_v101_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc101_200d_slope_v101_signal

def f204r_f204_revenue_growth_relative_to_equity_calc102_21d_slope_v102_signal(revenue, equity):
    res = ((equity / (revenue + 1.4431)).diff(47).rolling(27).max().diff(22).rolling(34).min() * 0.318173).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc102_21d_slope_v102_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc102_21d_slope_v102_signal

def f204r_f204_revenue_growth_relative_to_equity_calc103_126d_slope_v103_signal(revenue, equity):
    res = ((equity / (revenue + 9.4739)).rolling(34).mean().pct_change(46).rolling(38).var() * 0.089686).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc103_126d_slope_v103_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc103_126d_slope_v103_signal

def f204r_f204_revenue_growth_relative_to_equity_calc104_5d_slope_v104_signal(revenue, equity):
    res = ((revenue.diff(3) / (equity.shift(3) + 3.0553)).rolling(4).var().rolling(35).min() * 0.684317).diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc104_5d_slope_v104_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc104_5d_slope_v104_signal

def f204r_f204_revenue_growth_relative_to_equity_calc105_150d_slope_v105_signal(revenue, equity):
    res = ((equity / (revenue + 9.1092)).rolling(15).var().rolling(4).std().diff(24) * 0.651568).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc105_150d_slope_v105_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc105_150d_slope_v105_signal

def f204r_f204_revenue_growth_relative_to_equity_calc106_200d_slope_v106_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(20).rolling(15).min().rolling(50).std() * 0.630701).diff(6).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc106_200d_slope_v106_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc106_200d_slope_v106_signal

def f204r_f204_revenue_growth_relative_to_equity_calc107_84d_slope_v107_signal(revenue, equity):
    res = ((revenue / (equity + 8.0041)).rolling(6).mean().pct_change(12) * 0.186892).diff(8).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc107_84d_slope_v107_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc107_84d_slope_v107_signal

def f204r_f204_revenue_growth_relative_to_equity_calc108_21d_slope_v108_signal(revenue, equity):
    res = ((equity / (revenue + 8.2565)).pct_change(50).rolling(47).mean().rolling(37).mean() * 0.511766).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc108_21d_slope_v108_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc108_21d_slope_v108_signal

def f204r_f204_revenue_growth_relative_to_equity_calc109_63d_slope_v109_signal(revenue, equity):
    res = ((revenue * 1.1614 - equity).rolling(11).var().diff(14).rolling(15).max().rolling(41).min() * 0.364935).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc109_63d_slope_v109_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc109_63d_slope_v109_signal

def f204r_f204_revenue_growth_relative_to_equity_calc110_252d_slope_v110_signal(revenue, equity):
    res = ((revenue.diff(10) / (equity.shift(1) + 3.7073)).diff(28).rolling(20).var().rolling(29).std().diff(48) * 0.723003).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc110_252d_slope_v110_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc110_252d_slope_v110_signal

def f204r_f204_revenue_growth_relative_to_equity_calc111_150d_slope_v111_signal(revenue, equity):
    res = ((revenue / (equity + 6.1906)).rolling(7).std().rolling(47).min() * 0.196100).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc111_150d_slope_v111_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc111_150d_slope_v111_signal

def f204r_f204_revenue_growth_relative_to_equity_calc112_105d_slope_v112_signal(revenue, equity):
    res = ((revenue.diff(5) / (equity.shift(1) + 0.5858)).rolling(43).min().rolling(30).mean().rolling(30).var().rolling(15).max() * 0.685177).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc112_105d_slope_v112_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc112_105d_slope_v112_signal

def f204r_f204_revenue_growth_relative_to_equity_calc113_150d_slope_v113_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(13).std().pct_change(11).rolling(11).std() * 0.315080).diff(4).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc113_150d_slope_v113_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc113_150d_slope_v113_signal

def f204r_f204_revenue_growth_relative_to_equity_calc114_84d_slope_v114_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(3).rolling(44).max() * 0.473647).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc114_84d_slope_v114_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc114_84d_slope_v114_signal

def f204r_f204_revenue_growth_relative_to_equity_calc115_10d_slope_v115_signal(revenue, equity):
    res = ((revenue * 1.2105 - equity).pct_change(22).pct_change(20).diff(21) * 0.816812).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc115_10d_slope_v115_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc115_10d_slope_v115_signal

def f204r_f204_revenue_growth_relative_to_equity_calc116_105d_slope_v116_signal(revenue, equity):
    res = ((equity / (revenue + 2.1196)).rolling(10).max().pct_change(27).rolling(30).max().rolling(8).std() * 0.953184).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc116_105d_slope_v116_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc116_105d_slope_v116_signal

def f204r_f204_revenue_growth_relative_to_equity_calc117_150d_slope_v117_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(33).rolling(7).mean().rolling(42).var().rolling(25).std() * 0.786004).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc117_150d_slope_v117_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc117_150d_slope_v117_signal

def f204r_f204_revenue_growth_relative_to_equity_calc118_42d_slope_v118_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(12).std().rolling(20).mean().rolling(2).min() * 0.513220).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc118_42d_slope_v118_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc118_42d_slope_v118_signal

def f204r_f204_revenue_growth_relative_to_equity_calc119_84d_slope_v119_signal(revenue, equity):
    res = ((revenue / (equity + 8.7202)).rolling(49).var().rolling(48).var().diff(23).pct_change(19) * 0.179139).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc119_84d_slope_v119_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc119_84d_slope_v119_signal

def f204r_f204_revenue_growth_relative_to_equity_calc120_42d_slope_v120_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(15).diff(40).rolling(9).min().pct_change(41) * 0.448115).diff(7).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc120_42d_slope_v120_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc120_42d_slope_v120_signal

def f204r_f204_revenue_growth_relative_to_equity_calc121_126d_slope_v121_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(42).max().rolling(11).std() * 0.101596).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc121_126d_slope_v121_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc121_126d_slope_v121_signal

def f204r_f204_revenue_growth_relative_to_equity_calc122_200d_slope_v122_signal(revenue, equity):
    res = ((equity / (revenue + 3.1743)).diff(26).rolling(3).mean().rolling(7).min() * 0.893186).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc122_200d_slope_v122_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc122_200d_slope_v122_signal

def f204r_f204_revenue_growth_relative_to_equity_calc123_21d_slope_v123_signal(revenue, equity):
    res = ((revenue / (equity + 1.5796)).rolling(48).var().rolling(37).std() * 0.263256).diff(3).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc123_21d_slope_v123_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc123_21d_slope_v123_signal

def f204r_f204_revenue_growth_relative_to_equity_calc124_42d_slope_v124_signal(revenue, equity):
    res = ((equity / (revenue + 3.8747)).rolling(27).var().pct_change(47).diff(35) * 0.128593).diff(8).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc124_42d_slope_v124_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc124_42d_slope_v124_signal

def f204r_f204_revenue_growth_relative_to_equity_calc125_84d_slope_v125_signal(revenue, equity):
    res = ((revenue * 2.9555 - equity).rolling(45).mean().pct_change(39) * 0.484524).diff(7).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc125_84d_slope_v125_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc125_84d_slope_v125_signal

def f204r_f204_revenue_growth_relative_to_equity_calc126_21d_slope_v126_signal(revenue, equity):
    res = ((revenue / (equity + 2.7020)).rolling(9).var().rolling(43).mean().rolling(26).var() * 0.668247).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc126_21d_slope_v126_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc126_21d_slope_v126_signal

def f204r_f204_revenue_growth_relative_to_equity_calc127_42d_slope_v127_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(25).rolling(47).min().rolling(46).min() * 0.380707).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc127_42d_slope_v127_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc127_42d_slope_v127_signal

def f204r_f204_revenue_growth_relative_to_equity_calc128_42d_slope_v128_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(22).pct_change(47).rolling(17).var().rolling(42).max() * 0.675423).diff(11).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc128_42d_slope_v128_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc128_42d_slope_v128_signal

def f204r_f204_revenue_growth_relative_to_equity_calc129_21d_slope_v129_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(15).min().rolling(28).var() * 0.739975).diff(17).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc129_21d_slope_v129_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc129_21d_slope_v129_signal

def f204r_f204_revenue_growth_relative_to_equity_calc130_200d_slope_v130_signal(revenue, equity):
    res = ((revenue * 3.6173 - equity).rolling(8).max().diff(26) * 0.042566).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc130_200d_slope_v130_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc130_200d_slope_v130_signal

def f204r_f204_revenue_growth_relative_to_equity_calc131_105d_slope_v131_signal(revenue, equity):
    res = ((revenue / (equity + 4.6443)).rolling(6).std().rolling(22).std() * 0.635002).diff(7).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc131_105d_slope_v131_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc131_105d_slope_v131_signal

def f204r_f204_revenue_growth_relative_to_equity_calc132_200d_slope_v132_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(15).max().rolling(17).mean().diff(17) * 0.917875).diff(18).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc132_200d_slope_v132_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc132_200d_slope_v132_signal

def f204r_f204_revenue_growth_relative_to_equity_calc133_252d_slope_v133_signal(revenue, equity):
    res = ((revenue * 9.9857 - equity).rolling(35).max().pct_change(38) * 0.452327).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc133_252d_slope_v133_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc133_252d_slope_v133_signal

def f204r_f204_revenue_growth_relative_to_equity_calc134_63d_slope_v134_signal(revenue, equity):
    res = ((equity / (revenue + 0.7414)).rolling(11).var().diff(35).diff(36) * 0.765509).diff(9).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc134_63d_slope_v134_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc134_63d_slope_v134_signal

def f204r_f204_revenue_growth_relative_to_equity_calc135_63d_slope_v135_signal(revenue, equity):
    res = ((equity / (revenue + 6.8688)).rolling(24).max().rolling(44).std().diff(4).diff(42) * 0.441453).diff(9).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc135_63d_slope_v135_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc135_63d_slope_v135_signal

def f204r_f204_revenue_growth_relative_to_equity_calc136_5d_slope_v136_signal(revenue, equity):
    res = ((revenue * 6.9484 - equity).rolling(29).var().diff(27) * 0.050270).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc136_5d_slope_v136_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc136_5d_slope_v136_signal

def f204r_f204_revenue_growth_relative_to_equity_calc137_63d_slope_v137_signal(revenue, equity):
    res = ((revenue * 3.7974 - equity).rolling(17).max().rolling(33).max().rolling(37).var().pct_change(14) * 0.989299).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc137_63d_slope_v137_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc137_63d_slope_v137_signal

def f204r_f204_revenue_growth_relative_to_equity_calc138_150d_slope_v138_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(24).mean().rolling(9).var().rolling(29).mean() * 0.252003).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc138_150d_slope_v138_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc138_150d_slope_v138_signal

def f204r_f204_revenue_growth_relative_to_equity_calc139_63d_slope_v139_signal(revenue, equity):
    res = ((equity / (revenue + 0.5056)).rolling(46).std().diff(50) * 0.360449).diff(9).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc139_63d_slope_v139_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc139_63d_slope_v139_signal

def f204r_f204_revenue_growth_relative_to_equity_calc140_126d_slope_v140_signal(revenue, equity):
    res = ((equity / (revenue + 2.4627)).pct_change(17).rolling(32).mean().rolling(23).var().diff(17) * 0.365502).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc140_126d_slope_v140_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc140_126d_slope_v140_signal

def f204r_f204_revenue_growth_relative_to_equity_calc141_84d_slope_v141_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(48).rolling(10).min().rolling(42).mean().rolling(32).std() * 0.440652).diff(12).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc141_84d_slope_v141_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc141_84d_slope_v141_signal

def f204r_f204_revenue_growth_relative_to_equity_calc142_126d_slope_v142_signal(revenue, equity):
    res = ((revenue * 6.4545 - equity).rolling(47).min().rolling(17).mean().rolling(26).min() * 0.883651).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc142_126d_slope_v142_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc142_126d_slope_v142_signal

def f204r_f204_revenue_growth_relative_to_equity_calc143_105d_slope_v143_signal(revenue, equity):
    res = ((revenue.diff(9) / (equity.shift(1) + 6.4592)).rolling(21).mean().rolling(43).min().rolling(22).min() * 0.388219).diff(20).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc143_105d_slope_v143_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc143_105d_slope_v143_signal

def f204r_f204_revenue_growth_relative_to_equity_calc144_105d_slope_v144_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(39).var().diff(17).rolling(5).std() * 0.620193).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc144_105d_slope_v144_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc144_105d_slope_v144_signal

def f204r_f204_revenue_growth_relative_to_equity_calc145_21d_slope_v145_signal(revenue, equity):
    res = ((equity / (revenue + 0.5068)).diff(42).rolling(45).mean().rolling(14).mean() * 0.950035).diff(13).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc145_21d_slope_v145_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc145_21d_slope_v145_signal

def f204r_f204_revenue_growth_relative_to_equity_calc146_21d_slope_v146_signal(revenue, equity):
    res = ((revenue / (equity + 5.8283)).rolling(22).mean().rolling(28).min().rolling(31).std().rolling(12).std() * 0.182112).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc146_21d_slope_v146_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc146_21d_slope_v146_signal

def f204r_f204_revenue_growth_relative_to_equity_calc147_150d_slope_v147_signal(revenue, equity):
    res = ((equity / (revenue + 1.6239)).rolling(35).min().rolling(7).mean().rolling(4).max() * 0.224929).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc147_150d_slope_v147_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc147_150d_slope_v147_signal

def f204r_f204_revenue_growth_relative_to_equity_calc148_126d_slope_v148_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(22).rolling(16).std() * 0.454464).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc148_126d_slope_v148_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc148_126d_slope_v148_signal

def f204r_f204_revenue_growth_relative_to_equity_calc149_63d_slope_v149_signal(revenue, equity):
    res = ((revenue.replace(0, np.nan) / equity.replace(0, np.nan)).pct_change(6).rolling(30).var() * 0.406449).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc149_63d_slope_v149_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc149_63d_slope_v149_signal

def f204r_f204_revenue_growth_relative_to_equity_calc150_21d_slope_v150_signal(revenue, equity):
    res = ((revenue.diff(7) / (equity.shift(3) + 9.3081)).rolling(35).max().diff(8) * 0.341071).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc150_21d_slope_v150_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc150_21d_slope_v150_signal


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
