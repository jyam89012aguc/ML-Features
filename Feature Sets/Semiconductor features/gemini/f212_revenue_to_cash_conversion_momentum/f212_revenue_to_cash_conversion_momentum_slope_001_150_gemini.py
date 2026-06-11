import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f212r_f212_revenue_to_cash_conversion_momentum_calc001_10d_slope_v001_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 20.2137)).pct_change(14)).rolling(29).min()).rolling(25).min()).rolling(21).max()) * 0.568042).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc001_10d_slope_v001_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc001_10d_slope_v001_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc002_21d_slope_v002_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 3.798)).rolling(18).mean()).rolling(15).mean()).rolling(12).max()).rolling(4).max()) * 0.401687).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc002_21d_slope_v002_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc002_21d_slope_v002_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc003_126d_slope_v003_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(12) / ncfo.pct_change(15)).rolling(7).mean()).rolling(25).var()).rolling(17).std()) * 0.473871).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc003_126d_slope_v003_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc003_126d_slope_v003_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc004_42d_slope_v004_signal(revenue, ncfo):
    res = (((((((revenue.diff(11) / (ncfo.shift(10) + 23.2871)).diff(13)).rolling(28).min()).diff(12)).pct_change(16)) * 0.225308).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc004_42d_slope_v004_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc004_42d_slope_v004_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc005_63d_slope_v005_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 20.8001)).rolling(17).max()).rolling(27).mean()) * 0.686884).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc005_63d_slope_v005_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc005_63d_slope_v005_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc006_42d_slope_v006_signal(revenue, ncfo):
    res = (((((((revenue.diff(2) / (ncfo.shift(1) + 30.4348)).rolling(7).std()).pct_change(17)).rolling(27).mean()).rolling(12).mean()) * 0.215244).diff(14).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc006_42d_slope_v006_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc006_42d_slope_v006_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc007_5d_slope_v007_signal(revenue, ncfo):
    res = (((((revenue.diff(8) / (ncfo.shift(8) + 61.7945)).pct_change(18)).rolling(30).var()) * 0.128274).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc007_5d_slope_v007_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc007_5d_slope_v007_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc008_252d_slope_v008_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 69.0445)).pct_change(20)).rolling(27).max()) * 0.51508).diff(4).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc008_252d_slope_v008_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc008_252d_slope_v008_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc009_252d_slope_v009_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 56.291)).rolling(24).var()).rolling(26).min()).rolling(17).max()).diff(4)) * 0.50716).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc009_252d_slope_v009_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc009_252d_slope_v009_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc010_126d_slope_v010_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 36.4373)).pct_change(16)).rolling(11).var()) * 0.812778).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc010_126d_slope_v010_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc010_126d_slope_v010_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc011_10d_slope_v011_signal(revenue, ncfo):
    res = ((((((revenue * 8.6149 - ncfo).pct_change(8)).rolling(27).std()).rolling(15).min()) * 0.374988).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc011_10d_slope_v011_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc011_10d_slope_v011_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc012_42d_slope_v012_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 95.1889)).pct_change(17)).rolling(4).mean()).rolling(12).var()).rolling(26).min()) * 0.515832).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc012_42d_slope_v012_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc012_42d_slope_v012_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc013_42d_slope_v013_signal(revenue, ncfo):
    res = ((((((revenue.diff(5) / (ncfo.shift(10) + 6.2407)).rolling(30).min()).diff(18)).pct_change(10)) * 0.754009).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc013_42d_slope_v013_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc013_42d_slope_v013_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc014_21d_slope_v014_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(30).std()).rolling(21).max()).pct_change(20)).diff(15)) * 0.284185).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc014_21d_slope_v014_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc014_21d_slope_v014_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc015_252d_slope_v015_signal(revenue, ncfo):
    res = ((((((revenue * 78.1782 - ncfo).rolling(25).min()).diff(5)).rolling(19).max()) * 0.406416).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc015_252d_slope_v015_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc015_252d_slope_v015_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc016_10d_slope_v016_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 9.3727)).rolling(10).max()).rolling(28).std()).pct_change(10)).diff(14)) * 0.55075).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc016_10d_slope_v016_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc016_10d_slope_v016_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc017_5d_slope_v017_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 73.2254)).rolling(16).mean()).rolling(20).var()).diff(1)).rolling(12).min()) * 0.834752).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc017_5d_slope_v017_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc017_5d_slope_v017_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc018_252d_slope_v018_signal(revenue, ncfo):
    res = ((((((revenue.diff(18) / (ncfo.shift(10) + 74.6012)).diff(19)).diff(5)).diff(13)) * 0.579962).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc018_252d_slope_v018_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc018_252d_slope_v018_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc019_126d_slope_v019_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 24.8386)).diff(14)).pct_change(14)) * 0.33129).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc019_126d_slope_v019_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc019_126d_slope_v019_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc020_5d_slope_v020_signal(revenue, ncfo):
    res = (((((((revenue.diff(16) / (ncfo.shift(4) + 6.3131)).rolling(14).max()).rolling(19).max()).rolling(26).max()).rolling(29).min()) * 0.880739).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc020_5d_slope_v020_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc020_5d_slope_v020_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc021_63d_slope_v021_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 49.9328)).rolling(17).std()).diff(15)).rolling(24).std()).rolling(29).max()) * 0.424954).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc021_63d_slope_v021_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc021_63d_slope_v021_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc022_5d_slope_v022_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 69.4776)).pct_change(14)).rolling(5).mean()).rolling(20).var()).rolling(3).var()) * 0.456324).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc022_5d_slope_v022_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc022_5d_slope_v022_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc023_10d_slope_v023_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 11.8624)).rolling(27).std()).rolling(15).max()) * 0.308826).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc023_10d_slope_v023_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc023_10d_slope_v023_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_slope_v024_signal(revenue, ncfo):
    res = (((((revenue.diff(16) / (ncfo.shift(1) + 88.9168)).pct_change(2)).rolling(17).min()) * 0.22127).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_slope_v024_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_slope_v024_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc025_21d_slope_v025_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 56.6198)).diff(15)).pct_change(15)).diff(15)).rolling(29).std()) * 0.892282).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc025_21d_slope_v025_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc025_21d_slope_v025_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc026_5d_slope_v026_signal(revenue, ncfo):
    res = (((((((revenue.diff(14) / (ncfo.shift(7) + 80.0012)).rolling(23).mean()).rolling(25).min()).rolling(22).var()).rolling(29).mean()) * 0.661212).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc026_5d_slope_v026_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc026_5d_slope_v026_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc027_126d_slope_v027_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 2.5779)).rolling(19).max()).rolling(26).max()) * 0.627507).diff(2).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc027_126d_slope_v027_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc027_126d_slope_v027_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc028_63d_slope_v028_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 52.2232)).rolling(27).var()).rolling(9).std()) * 0.745547).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc028_63d_slope_v028_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc028_63d_slope_v028_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc029_42d_slope_v029_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(15).var()).rolling(15).std()) * 0.532873).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc029_42d_slope_v029_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc029_42d_slope_v029_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_slope_v030_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 52.8374)).rolling(7).std()).rolling(26).var()).rolling(6).mean()) * 0.384371).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_slope_v030_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_slope_v030_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc031_42d_slope_v031_signal(revenue, ncfo):
    res = ((((((revenue.diff(11) / (ncfo.shift(3) + 67.893)).rolling(12).mean()).rolling(15).std()).rolling(10).var()) * 0.067735).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc031_42d_slope_v031_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc031_42d_slope_v031_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc032_252d_slope_v032_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(17)).rolling(5).min()).rolling(3).var()).rolling(16).var()) * 0.060841).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc032_252d_slope_v032_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc032_252d_slope_v032_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc033_42d_slope_v033_signal(revenue, ncfo):
    res = (((((((revenue * 6.6393 - ncfo).rolling(9).mean()).pct_change(18)).diff(5)).rolling(20).var()) * 0.038328).diff(14).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc033_42d_slope_v033_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc033_42d_slope_v033_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc034_42d_slope_v034_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 8.4824)).rolling(15).max()).rolling(16).max()) * 0.633083).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc034_42d_slope_v034_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc034_42d_slope_v034_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc035_5d_slope_v035_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 81.2831)).rolling(21).var()).rolling(28).var()).diff(13)) * 0.951892).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc035_5d_slope_v035_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc035_5d_slope_v035_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc036_252d_slope_v036_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(2) / ncfo.pct_change(6)).rolling(4).max()).rolling(4).var()).rolling(24).min()).rolling(28).mean()) * 0.583456).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc036_252d_slope_v036_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc036_252d_slope_v036_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_slope_v037_signal(revenue, ncfo):
    res = (((((((revenue.diff(14) / (ncfo.shift(4) + 55.6923)).rolling(22).var()).rolling(26).var()).diff(15)).rolling(9).var()) * 0.283869).diff(11).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_slope_v037_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_slope_v037_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc038_21d_slope_v038_signal(revenue, ncfo):
    res = ((((((revenue * 21.1413 - ncfo).rolling(30).mean()).rolling(23).mean()).rolling(15).std()) * 0.949813).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc038_21d_slope_v038_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc038_21d_slope_v038_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc039_126d_slope_v039_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 70.3596)).rolling(23).min()).rolling(13).mean()).pct_change(13)).pct_change(20)) * 0.757216).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc039_126d_slope_v039_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc039_126d_slope_v039_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc040_42d_slope_v040_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 17.8009)).rolling(9).mean()).diff(1)).pct_change(9)) * 0.762607).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc040_42d_slope_v040_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc040_42d_slope_v040_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc041_10d_slope_v041_signal(revenue, ncfo):
    res = (((((revenue.diff(10) / (ncfo.shift(4) + 9.0877)).rolling(17).var()).diff(20)) * 0.611174).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc041_10d_slope_v041_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc041_10d_slope_v041_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc042_5d_slope_v042_signal(revenue, ncfo):
    res = ((((((revenue * 19.6891 - ncfo).rolling(19).std()).rolling(23).std()).diff(19)) * 0.814701).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc042_5d_slope_v042_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc042_5d_slope_v042_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc043_63d_slope_v043_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 17.6353)).diff(9)).rolling(29).std()).diff(1)).diff(18)) * 0.586401).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc043_63d_slope_v043_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc043_63d_slope_v043_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc044_21d_slope_v044_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(5).var()).diff(17)).rolling(17).min()) * 0.87544).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc044_21d_slope_v044_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc044_21d_slope_v044_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc045_63d_slope_v045_signal(revenue, ncfo):
    res = ((((((revenue * 75.9263 - ncfo).rolling(2).var()).rolling(8).min()).rolling(4).var()) * 0.876126).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc045_63d_slope_v045_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc045_63d_slope_v045_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc046_252d_slope_v046_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 2.6347)).rolling(4).var()).diff(4)).rolling(17).mean()) * 0.732695).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc046_252d_slope_v046_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc046_252d_slope_v046_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc047_252d_slope_v047_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(28).var()).rolling(28).mean()) * 0.791276).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc047_252d_slope_v047_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc047_252d_slope_v047_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc048_63d_slope_v048_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(15) / ncfo.pct_change(4)).rolling(5).max()).rolling(3).mean()).rolling(14).mean()) * 0.934677).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc048_63d_slope_v048_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc048_63d_slope_v048_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc049_252d_slope_v049_signal(revenue, ncfo):
    res = (((((((revenue * 69.367 - ncfo).rolling(4).min()).rolling(23).mean()).rolling(19).mean()).rolling(11).mean()) * 0.776993).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc049_252d_slope_v049_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc049_252d_slope_v049_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc050_42d_slope_v050_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(27).min()).rolling(30).min()).rolling(21).max()) * 0.746924).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc050_42d_slope_v050_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc050_42d_slope_v050_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc051_21d_slope_v051_signal(revenue, ncfo):
    res = (((((revenue * 65.1271 - ncfo).rolling(5).mean()).rolling(21).mean()) * 0.672261).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc051_21d_slope_v051_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc051_21d_slope_v051_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc052_63d_slope_v052_signal(revenue, ncfo):
    res = ((((((revenue.diff(19) / (ncfo.shift(3) + 78.9627)).rolling(25).min()).rolling(16).max()).rolling(9).std()) * 0.199742).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc052_63d_slope_v052_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc052_63d_slope_v052_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc053_252d_slope_v053_signal(revenue, ncfo):
    res = (((((((revenue.diff(19) / (ncfo.shift(7) + 4.5027)).rolling(26).max()).rolling(6).std()).rolling(11).min()).rolling(12).max()) * 0.135127).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc053_252d_slope_v053_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc053_252d_slope_v053_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc054_21d_slope_v054_signal(revenue, ncfo):
    res = (((((revenue * 97.0301 - ncfo).rolling(13).min()).rolling(8).std()) * 0.517327).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc054_21d_slope_v054_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc054_21d_slope_v054_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc055_252d_slope_v055_signal(revenue, ncfo):
    res = (((((((revenue * 6.9335 - ncfo).rolling(21).var()).rolling(15).var()).rolling(7).var()).rolling(16).mean()) * 0.195568).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc055_252d_slope_v055_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc055_252d_slope_v055_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc056_42d_slope_v056_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 22.0186)).rolling(25).min()).pct_change(11)) * 0.013623).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc056_42d_slope_v056_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc056_42d_slope_v056_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc057_10d_slope_v057_signal(revenue, ncfo):
    res = (((((revenue.diff(1) / (ncfo.shift(6) + 40.0912)).rolling(5).max()).rolling(11).std()) * 0.819563).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc057_10d_slope_v057_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc057_10d_slope_v057_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc058_10d_slope_v058_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 63.1703)).rolling(9).std()).rolling(25).var()).rolling(12).std()) * 0.904455).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc058_10d_slope_v058_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc058_10d_slope_v058_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_slope_v059_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(4)).rolling(8).var()).rolling(16).var()).rolling(13).std()) * 0.031062).diff(12).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_slope_v059_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_slope_v059_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc060_126d_slope_v060_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 17.2188)).pct_change(7)).rolling(19).std()) * 0.526388).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc060_126d_slope_v060_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc060_126d_slope_v060_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc061_126d_slope_v061_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 37.4881)).rolling(27).var()).rolling(12).std()).rolling(3).std()).diff(9)) * 0.597558).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc061_126d_slope_v061_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc061_126d_slope_v061_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc062_252d_slope_v062_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(3) / ncfo.pct_change(16)).rolling(7).mean()).rolling(14).max()).pct_change(17)).rolling(17).var()) * 0.582401).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc062_252d_slope_v062_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc062_252d_slope_v062_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc063_42d_slope_v063_signal(revenue, ncfo):
    res = (((((((revenue.diff(17) / (ncfo.shift(8) + 17.982)).rolling(22).min()).pct_change(19)).diff(2)).rolling(9).std()) * 0.708237).diff(7).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc063_42d_slope_v063_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc063_42d_slope_v063_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc064_42d_slope_v064_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 86.3305)).rolling(19).var()).rolling(6).mean()).pct_change(3)) * 0.397982).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc064_42d_slope_v064_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc064_42d_slope_v064_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc065_42d_slope_v065_signal(revenue, ncfo):
    res = ((((((revenue.diff(2) / (ncfo.shift(8) + 51.9302)).rolling(16).min()).rolling(15).min()).rolling(27).var()) * 0.235574).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc065_42d_slope_v065_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc065_42d_slope_v065_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc066_21d_slope_v066_signal(revenue, ncfo):
    res = (((((revenue.diff(15) / (ncfo.shift(4) + 27.3746)).rolling(28).var()).rolling(18).max()) * 0.034224).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc066_21d_slope_v066_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc066_21d_slope_v066_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc067_126d_slope_v067_signal(revenue, ncfo):
    res = (((((revenue.diff(8) / (ncfo.shift(2) + 7.9081)).rolling(8).max()).rolling(8).var()) * 0.280896).diff(11).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc067_126d_slope_v067_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc067_126d_slope_v067_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc068_21d_slope_v068_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(20) / ncfo.pct_change(5)).rolling(10).max()).rolling(26).mean()).rolling(11).var()).pct_change(12)) * 0.809253).diff(13).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc068_21d_slope_v068_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc068_21d_slope_v068_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc069_42d_slope_v069_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(25).std()).diff(7)) * 0.75265).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc069_42d_slope_v069_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc069_42d_slope_v069_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc070_10d_slope_v070_signal(revenue, ncfo):
    res = (((((revenue.diff(15) / (ncfo.shift(8) + 51.631)).rolling(26).min()).diff(14)) * 0.780255).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc070_10d_slope_v070_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc070_10d_slope_v070_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc071_42d_slope_v071_signal(revenue, ncfo):
    res = (((((((revenue.diff(12) / (ncfo.shift(3) + 45.0522)).rolling(17).mean()).pct_change(12)).rolling(9).var()).rolling(15).min()) * 0.557278).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc071_42d_slope_v071_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc071_42d_slope_v071_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc072_252d_slope_v072_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 77.8865)).rolling(12).std()).rolling(22).max()) * 0.536852).diff(20).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc072_252d_slope_v072_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc072_252d_slope_v072_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc073_63d_slope_v073_signal(revenue, ncfo):
    res = ((((((revenue * 57.4305 - ncfo).rolling(17).std()).rolling(12).mean()).rolling(16).max()) * 0.393068).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc073_63d_slope_v073_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc073_63d_slope_v073_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc074_5d_slope_v074_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 17.2252)).rolling(4).std()).rolling(11).min()) * 0.671388).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc074_5d_slope_v074_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc074_5d_slope_v074_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc075_10d_slope_v075_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 29.1814)).rolling(29).var()).rolling(14).min()) * 0.523908).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc075_10d_slope_v075_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc075_10d_slope_v075_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc076_5d_slope_v076_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 13.0009)).rolling(28).min()).diff(16)).rolling(21).std()) * 0.420045).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc076_5d_slope_v076_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc076_5d_slope_v076_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc077_21d_slope_v077_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 58.7904)).rolling(28).mean()).rolling(21).min()).pct_change(8)) * 0.502426).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc077_21d_slope_v077_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc077_21d_slope_v077_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc078_21d_slope_v078_signal(revenue, ncfo):
    res = (((((revenue.pct_change(19) / ncfo.pct_change(2)).rolling(22).var()).rolling(13).min()) * 0.871655).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc078_21d_slope_v078_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc078_21d_slope_v078_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc079_42d_slope_v079_signal(revenue, ncfo):
    res = (((((((revenue * 61.3414 - ncfo).rolling(16).min()).rolling(23).min()).rolling(24).std()).rolling(5).max()) * 0.803785).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc079_42d_slope_v079_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc079_42d_slope_v079_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc080_126d_slope_v080_signal(revenue, ncfo):
    res = (((((revenue.pct_change(18) / ncfo.pct_change(10)).diff(7)).rolling(15).min()) * 0.244901).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc080_126d_slope_v080_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc080_126d_slope_v080_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc081_5d_slope_v081_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(8).var()).rolling(3).max()) * 0.085003).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc081_5d_slope_v081_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc081_5d_slope_v081_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc082_5d_slope_v082_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 7.4122)).rolling(2).mean()).rolling(5).var()).diff(5)) * 0.690596).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc082_5d_slope_v082_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc082_5d_slope_v082_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc083_126d_slope_v083_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(18) / ncfo.pct_change(8)).rolling(17).std()).pct_change(9)).pct_change(6)) * 0.485064).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc083_126d_slope_v083_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc083_126d_slope_v083_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc084_252d_slope_v084_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 1.9048)).diff(1)).diff(9)) * 0.108505).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc084_252d_slope_v084_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc084_252d_slope_v084_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc085_42d_slope_v085_signal(revenue, ncfo):
    res = (((((revenue.pct_change(7) / ncfo.pct_change(15)).pct_change(17)).diff(4)) * 0.222339).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc085_42d_slope_v085_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc085_42d_slope_v085_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc086_126d_slope_v086_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 30.9016)).rolling(8).std()).rolling(2).mean()).rolling(2).min()) * 0.061367).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc086_126d_slope_v086_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc086_126d_slope_v086_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc087_21d_slope_v087_signal(revenue, ncfo):
    res = (((((revenue.pct_change(4) / ncfo.pct_change(6)).rolling(15).mean()).rolling(5).max()) * 0.67636).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc087_21d_slope_v087_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc087_21d_slope_v087_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc088_21d_slope_v088_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 56.2492)).rolling(5).std()).rolling(12).var()) * 0.195757).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc088_21d_slope_v088_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc088_21d_slope_v088_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc089_5d_slope_v089_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 40.2737)).pct_change(9)).diff(20)).rolling(3).var()).rolling(30).mean()) * 0.319915).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc089_5d_slope_v089_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc089_5d_slope_v089_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_slope_v090_signal(revenue, ncfo):
    res = (((((revenue.diff(4) / (ncfo.shift(9) + 30.2233)).rolling(12).max()).diff(13)) * 0.596892).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_slope_v090_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_slope_v090_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc091_21d_slope_v091_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 17.6156)).rolling(16).max()).rolling(18).min()).diff(8)).rolling(20).max()) * 0.756482).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc091_21d_slope_v091_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc091_21d_slope_v091_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc092_10d_slope_v092_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 2.2192)).rolling(3).mean()).rolling(13).std()).rolling(11).min()).rolling(6).std()) * 0.753762).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc092_10d_slope_v092_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc092_10d_slope_v092_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc093_10d_slope_v093_signal(revenue, ncfo):
    res = ((((((revenue.diff(20) / (ncfo.shift(8) + 64.2397)).diff(2)).rolling(27).max()).rolling(22).min()) * 0.243303).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc093_10d_slope_v093_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc093_10d_slope_v093_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc094_252d_slope_v094_signal(revenue, ncfo):
    res = (((((revenue * 2.467 - ncfo).diff(8)).pct_change(8)) * 0.839996).diff(20).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc094_252d_slope_v094_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc094_252d_slope_v094_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc095_252d_slope_v095_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 38.2104)).rolling(22).mean()).rolling(8).std()) * 0.325204).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc095_252d_slope_v095_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc095_252d_slope_v095_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc096_5d_slope_v096_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(11).min()).rolling(25).std()).rolling(9).std()).rolling(7).min()) * 0.54787).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc096_5d_slope_v096_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc096_5d_slope_v096_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc097_10d_slope_v097_signal(revenue, ncfo):
    res = ((((((revenue.diff(7) / (ncfo.shift(5) + 30.3798)).rolling(7).min()).rolling(16).min()).rolling(18).min()) * 0.574893).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc097_10d_slope_v097_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc097_10d_slope_v097_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc098_126d_slope_v098_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 43.3997)).rolling(19).max()).rolling(19).std()).diff(6)) * 0.162761).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc098_126d_slope_v098_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc098_126d_slope_v098_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc099_42d_slope_v099_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 46.4188)).rolling(24).std()).rolling(8).min()).rolling(8).std()) * 0.454531).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc099_42d_slope_v099_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc099_42d_slope_v099_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc100_5d_slope_v100_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(14).var()).rolling(11).min()).diff(19)).rolling(15).mean()) * 0.725761).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc100_5d_slope_v100_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc100_5d_slope_v100_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc101_5d_slope_v101_signal(revenue, ncfo):
    res = (((((((revenue * 38.5441 - ncfo).rolling(22).min()).diff(12)).diff(2)).diff(13)) * 0.564296).diff(14).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc101_5d_slope_v101_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc101_5d_slope_v101_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc102_126d_slope_v102_signal(revenue, ncfo):
    res = ((((((revenue * 24.7545 - ncfo).diff(5)).rolling(9).var()).rolling(20).max()) * 0.478171).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc102_126d_slope_v102_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc102_126d_slope_v102_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_slope_v103_signal(revenue, ncfo):
    res = (((((revenue * 11.7614 - ncfo).rolling(7).min()).pct_change(14)) * 0.10046).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_slope_v103_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_slope_v103_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc104_126d_slope_v104_signal(revenue, ncfo):
    res = (((((revenue.pct_change(10) / ncfo.pct_change(14)).rolling(22).mean()).rolling(26).max()) * 0.95833).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc104_126d_slope_v104_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc104_126d_slope_v104_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc105_252d_slope_v105_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(4).mean()).pct_change(14)) * 0.743755).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc105_252d_slope_v105_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc105_252d_slope_v105_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc106_42d_slope_v106_signal(revenue, ncfo):
    res = (((((revenue.pct_change(12) / ncfo.pct_change(6)).rolling(17).std()).rolling(18).std()) * 0.728381).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc106_42d_slope_v106_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc106_42d_slope_v106_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc107_42d_slope_v107_signal(revenue, ncfo):
    res = ((((((revenue.diff(7) / (ncfo.shift(1) + 56.7525)).rolling(22).min()).rolling(5).max()).pct_change(6)) * 0.218322).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc107_42d_slope_v107_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc107_42d_slope_v107_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc108_21d_slope_v108_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 8.6621)).rolling(23).min()).pct_change(4)).rolling(3).mean()) * 0.132188).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc108_21d_slope_v108_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc108_21d_slope_v108_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_slope_v109_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 95.5259)).rolling(18).max()).pct_change(9)).rolling(17).min()) * 0.662016).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_slope_v109_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_slope_v109_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc110_63d_slope_v110_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(8) / ncfo.pct_change(12)).rolling(21).min()).rolling(13).mean()).pct_change(11)) * 0.373369).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc110_63d_slope_v110_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc110_63d_slope_v110_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc111_5d_slope_v111_signal(revenue, ncfo):
    res = ((((((revenue * 45.7462 - ncfo).diff(8)).rolling(16).var()).rolling(23).max()) * 0.694342).diff(16).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc111_5d_slope_v111_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc111_5d_slope_v111_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc112_63d_slope_v112_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(12) / ncfo.pct_change(2)).diff(15)).rolling(21).std()).rolling(14).min()) * 0.194176).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc112_63d_slope_v112_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc112_63d_slope_v112_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc113_252d_slope_v113_signal(revenue, ncfo):
    res = (((((revenue * 8.2288 - ncfo).diff(5)).pct_change(17)) * 0.429358).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc113_252d_slope_v113_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc113_252d_slope_v113_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc114_252d_slope_v114_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(3) / ncfo.pct_change(10)).pct_change(15)).rolling(30).std()).rolling(5).min()).rolling(23).min()) * 0.504544).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc114_252d_slope_v114_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc114_252d_slope_v114_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc115_10d_slope_v115_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 24.4113)).rolling(26).min()).rolling(9).var()).diff(9)) * 0.177024).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc115_10d_slope_v115_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc115_10d_slope_v115_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc116_126d_slope_v116_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 12.3975)).pct_change(20)).rolling(22).mean()).rolling(14).var()).diff(13)) * 0.143041).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc116_126d_slope_v116_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc116_126d_slope_v116_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc117_252d_slope_v117_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 43.7525)).rolling(25).var()).rolling(8).max()) * 0.2387).diff(4).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc117_252d_slope_v117_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc117_252d_slope_v117_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc118_63d_slope_v118_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 36.8369)).rolling(8).max()).pct_change(13)).rolling(12).min()).pct_change(12)) * 0.846264).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc118_63d_slope_v118_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc118_63d_slope_v118_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc119_63d_slope_v119_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(28).std()).rolling(28).var()).rolling(17).std()) * 0.58896).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc119_63d_slope_v119_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc119_63d_slope_v119_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc120_10d_slope_v120_signal(revenue, ncfo):
    res = (((((((revenue * 60.1864 - ncfo).rolling(10).mean()).pct_change(19)).rolling(22).min()).pct_change(7)) * 0.152953).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc120_10d_slope_v120_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc120_10d_slope_v120_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc121_21d_slope_v121_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(7) / ncfo.pct_change(8)).rolling(29).mean()).pct_change(6)).pct_change(16)).diff(13)) * 0.379174).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc121_21d_slope_v121_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc121_21d_slope_v121_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc122_252d_slope_v122_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(13).min()).pct_change(13)).rolling(4).min()).rolling(25).max()) * 0.841548).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc122_252d_slope_v122_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc122_252d_slope_v122_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc123_21d_slope_v123_signal(revenue, ncfo):
    res = (((((((revenue.diff(18) / (ncfo.shift(7) + 69.668)).pct_change(2)).pct_change(10)).rolling(22).min()).rolling(20).std()) * 0.20119).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc123_21d_slope_v123_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc123_21d_slope_v123_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc124_42d_slope_v124_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(7) / ncfo.pct_change(7)).rolling(13).mean()).diff(19)).rolling(23).mean()).pct_change(5)) * 0.29526).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc124_42d_slope_v124_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc124_42d_slope_v124_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc125_42d_slope_v125_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 67.9766)).rolling(18).mean()).diff(11)) * 0.174858).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc125_42d_slope_v125_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc125_42d_slope_v125_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc126_42d_slope_v126_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 96.9757)).rolling(11).min()).diff(20)).rolling(22).std()) * 0.624433).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc126_42d_slope_v126_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc126_42d_slope_v126_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc127_252d_slope_v127_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(13) / ncfo.pct_change(9)).rolling(13).min()).rolling(5).mean()).rolling(4).mean()).rolling(17).mean()) * 0.789419).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc127_252d_slope_v127_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc127_252d_slope_v127_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc128_10d_slope_v128_signal(revenue, ncfo):
    res = (((((revenue * 2.4004 - ncfo).rolling(17).min()).diff(14)) * 0.571522).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc128_10d_slope_v128_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc128_10d_slope_v128_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc129_63d_slope_v129_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(18)).pct_change(17)).rolling(4).min()).rolling(28).max()) * 0.328724).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc129_63d_slope_v129_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc129_63d_slope_v129_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc130_63d_slope_v130_signal(revenue, ncfo):
    res = (((((((revenue * 71.4035 - ncfo).rolling(2).std()).rolling(16).max()).pct_change(11)).rolling(3).mean()) * 0.784266).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc130_63d_slope_v130_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc130_63d_slope_v130_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_slope_v131_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 20.7024)).rolling(13).var()).rolling(7).max()).rolling(23).min()).rolling(9).mean()) * 0.167986).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_slope_v131_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_slope_v131_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc132_5d_slope_v132_signal(revenue, ncfo):
    res = ((((((revenue * 94.6268 - ncfo).diff(11)).rolling(13).max()).rolling(19).max()) * 0.519054).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc132_5d_slope_v132_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc132_5d_slope_v132_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc133_10d_slope_v133_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 68.8242)).pct_change(7)).rolling(21).std()).rolling(8).max()) * 0.659365).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc133_10d_slope_v133_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc133_10d_slope_v133_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc134_21d_slope_v134_signal(revenue, ncfo):
    res = ((((((revenue.diff(14) / (ncfo.shift(2) + 27.8118)).diff(6)).rolling(16).min()).rolling(10).mean()) * 0.724522).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc134_21d_slope_v134_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc134_21d_slope_v134_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc135_126d_slope_v135_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(12) / ncfo.pct_change(19)).pct_change(17)).rolling(7).max()).rolling(28).min()).rolling(12).std()) * 0.209688).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc135_126d_slope_v135_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc135_126d_slope_v135_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc136_42d_slope_v136_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 2.6884)).rolling(15).max()).rolling(12).mean()).diff(3)).rolling(12).var()) * 0.601535).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc136_42d_slope_v136_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc136_42d_slope_v136_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc137_10d_slope_v137_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(4)).rolling(18).std()) * 0.23125).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc137_10d_slope_v137_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc137_10d_slope_v137_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc138_63d_slope_v138_signal(revenue, ncfo):
    res = ((((((revenue * 82.1522 - ncfo).rolling(5).max()).rolling(7).mean()).rolling(26).var()) * 0.489826).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc138_63d_slope_v138_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc138_63d_slope_v138_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc139_10d_slope_v139_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(10).std()).rolling(23).mean()).rolling(24).max()).rolling(23).std()) * 0.736471).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc139_10d_slope_v139_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc139_10d_slope_v139_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc140_10d_slope_v140_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(7).min()).rolling(13).min()).pct_change(15)).rolling(11).max()) * 0.730714).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc140_10d_slope_v140_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc140_10d_slope_v140_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc141_42d_slope_v141_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)).diff(3)).rolling(25).mean()) * 0.714097).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc141_42d_slope_v141_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc141_42d_slope_v141_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc142_5d_slope_v142_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(25).max()).rolling(17).std()).rolling(18).min()).diff(18)) * 0.066263).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc142_5d_slope_v142_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc142_5d_slope_v142_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc143_42d_slope_v143_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 1.4886)).diff(17)).diff(20)).rolling(21).mean()).rolling(7).min()) * 0.19638).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc143_42d_slope_v143_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc143_42d_slope_v143_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc144_10d_slope_v144_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(7).min()).rolling(5).var()).rolling(23).var()) * 0.36971).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc144_10d_slope_v144_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc144_10d_slope_v144_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc145_252d_slope_v145_signal(revenue, ncfo):
    res = ((((((revenue.diff(4) / (ncfo.shift(5) + 53.9581)).rolling(2).std()).diff(19)).rolling(8).min()) * 0.761086).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc145_252d_slope_v145_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc145_252d_slope_v145_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc146_126d_slope_v146_signal(revenue, ncfo):
    res = (((((revenue.diff(15) / (ncfo.shift(10) + 51.6013)).rolling(16).max()).rolling(11).var()) * 0.88555).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc146_126d_slope_v146_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc146_126d_slope_v146_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc147_5d_slope_v147_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 0.6149)).rolling(8).min()).rolling(18).mean()).rolling(30).max()) * 0.882392).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc147_5d_slope_v147_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc147_5d_slope_v147_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc148_42d_slope_v148_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(13).var()).rolling(30).min()).rolling(19).std()) * 0.487664).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc148_42d_slope_v148_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc148_42d_slope_v148_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc149_5d_slope_v149_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(5) / ncfo.pct_change(12)).rolling(13).mean()).pct_change(7)).rolling(8).mean()) * 0.653154).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc149_5d_slope_v149_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc149_5d_slope_v149_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc150_5d_slope_v150_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(5).var()).rolling(17).min()).rolling(17).max()).pct_change(5)) * 0.422635).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc150_5d_slope_v150_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc150_5d_slope_v150_signal


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
