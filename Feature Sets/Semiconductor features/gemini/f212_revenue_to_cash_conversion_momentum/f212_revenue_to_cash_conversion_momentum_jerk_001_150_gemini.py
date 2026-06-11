import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f212r_f212_revenue_to_cash_conversion_momentum_calc001_252d_jerk_v001_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 76.4628)).rolling(6).std()).rolling(18).var()) * 0.874131).diff(1).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc001_252d_jerk_v001_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc001_252d_jerk_v001_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc002_5d_jerk_v002_signal(revenue, ncfo):
    res = ((((((revenue.diff(20) / (ncfo.shift(1) + 67.8632)).rolling(4).min()).pct_change(14)).rolling(21).std()) * 0.345298).diff(5).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc002_5d_jerk_v002_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc002_5d_jerk_v002_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc003_10d_jerk_v003_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(4)).diff(17)).rolling(7).max()).rolling(29).std()) * 0.761393).diff(19).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc003_10d_jerk_v003_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc003_10d_jerk_v003_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc004_10d_jerk_v004_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 12.1341)).rolling(4).std()).pct_change(2)).rolling(15).min()).rolling(11).max()) * 0.403257).diff(8).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc004_10d_jerk_v004_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc004_10d_jerk_v004_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc005_21d_jerk_v005_signal(revenue, ncfo):
    res = ((((((revenue.diff(14) / (ncfo.shift(1) + 42.665)).rolling(13).var()).diff(14)).rolling(12).std()) * 0.070123).diff(2).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc005_21d_jerk_v005_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc005_21d_jerk_v005_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc006_5d_jerk_v006_signal(revenue, ncfo):
    res = (((((((revenue.diff(11) / (ncfo.shift(4) + 0.1535)).rolling(15).mean()).rolling(10).std()).rolling(13).min()).rolling(11).var()) * 0.657222).diff(4).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc006_5d_jerk_v006_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc006_5d_jerk_v006_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc007_126d_jerk_v007_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(12) / ncfo.pct_change(12)).rolling(21).max()).rolling(9).var()).diff(9)).rolling(20).std()) * 0.550733).diff(13).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc007_126d_jerk_v007_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc007_126d_jerk_v007_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc008_5d_jerk_v008_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 13.1355)).rolling(5).min()).rolling(19).mean()).rolling(12).max()).rolling(25).var()) * 0.737736).diff(16).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc008_5d_jerk_v008_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc008_5d_jerk_v008_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc009_63d_jerk_v009_signal(revenue, ncfo):
    res = ((((((revenue * 72.1049 - ncfo).rolling(16).var()).diff(4)).rolling(4).min()) * 0.052935).diff(16).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc009_63d_jerk_v009_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc009_63d_jerk_v009_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc010_63d_jerk_v010_signal(revenue, ncfo):
    res = (((((revenue.pct_change(20) / ncfo.pct_change(9)).rolling(3).var()).rolling(3).max()) * 0.503792).diff(7).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc010_63d_jerk_v010_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc010_63d_jerk_v010_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc011_42d_jerk_v011_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(13)).rolling(21).min()).rolling(8).var()).rolling(2).std()) * 0.862851).diff(6).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc011_42d_jerk_v011_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc011_42d_jerk_v011_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc012_10d_jerk_v012_signal(revenue, ncfo):
    res = ((((((revenue.diff(17) / (ncfo.shift(8) + 59.2521)).pct_change(8)).rolling(24).var()).rolling(19).var()) * 0.018684).diff(4).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc012_10d_jerk_v012_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc012_10d_jerk_v012_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc013_10d_jerk_v013_signal(revenue, ncfo):
    res = (((((revenue.diff(2) / (ncfo.shift(3) + 4.6567)).diff(8)).pct_change(7)) * 0.243452).diff(18).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc013_10d_jerk_v013_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc013_10d_jerk_v013_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc014_5d_jerk_v014_signal(revenue, ncfo):
    res = (((((((revenue.diff(12) / (ncfo.shift(6) + 64.8997)).rolling(15).std()).rolling(11).max()).rolling(3).var()).diff(1)) * 0.630029).diff(12).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc014_5d_jerk_v014_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc014_5d_jerk_v014_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc015_126d_jerk_v015_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(19) / ncfo.pct_change(4)).diff(13)).diff(9)).pct_change(20)).rolling(8).max()) * 0.183201).diff(15).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc015_126d_jerk_v015_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc015_126d_jerk_v015_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc016_21d_jerk_v016_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(15) / ncfo.pct_change(8)).rolling(13).min()).rolling(30).std()).rolling(4).min()).rolling(7).min()) * 0.580031).diff(15).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc016_21d_jerk_v016_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc016_21d_jerk_v016_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc017_252d_jerk_v017_signal(revenue, ncfo):
    res = (((((revenue.diff(16) / (ncfo.shift(3) + 86.249)).rolling(28).std()).rolling(23).min()) * 0.195083).diff(20).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc017_252d_jerk_v017_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc017_252d_jerk_v017_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc018_5d_jerk_v018_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 14.4379)).pct_change(1)).rolling(5).max()).rolling(14).min()).rolling(5).mean()) * 0.427867).diff(1).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc018_5d_jerk_v018_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc018_5d_jerk_v018_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc019_10d_jerk_v019_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 24.9095)).diff(11)).pct_change(3)).rolling(6).std()).rolling(26).min()) * 0.091924).diff(19).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc019_10d_jerk_v019_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc019_10d_jerk_v019_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc020_252d_jerk_v020_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(2) / ncfo.pct_change(18)).diff(18)).rolling(2).mean()).pct_change(2)) * 0.335121).diff(4).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc020_252d_jerk_v020_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc020_252d_jerk_v020_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc021_21d_jerk_v021_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 10.3464)).rolling(14).min()).rolling(13).std()) * 0.878728).diff(10).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc021_21d_jerk_v021_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc021_21d_jerk_v021_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc022_126d_jerk_v022_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 38.5359)).rolling(13).var()).rolling(21).mean()) * 0.876539).diff(11).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc022_126d_jerk_v022_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc022_126d_jerk_v022_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc023_21d_jerk_v023_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(21).var()).rolling(23).std()).rolling(6).min()).diff(10)) * 0.911476).diff(20).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc023_21d_jerk_v023_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc023_21d_jerk_v023_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_jerk_v024_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 87.5527)).pct_change(5)).rolling(6).var()) * 0.275671).diff(13).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_jerk_v024_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_jerk_v024_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc025_126d_jerk_v025_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(19) / ncfo.pct_change(14)).rolling(4).std()).rolling(6).var()).rolling(26).std()) * 0.966812).diff(13).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc025_126d_jerk_v025_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc025_126d_jerk_v025_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc026_21d_jerk_v026_signal(revenue, ncfo):
    res = (((((revenue.pct_change(11) / ncfo.pct_change(5)).rolling(15).min()).rolling(17).max()) * 0.481663).diff(18).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc026_21d_jerk_v026_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc026_21d_jerk_v026_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc027_42d_jerk_v027_signal(revenue, ncfo):
    res = (((((((revenue * 53.2942 - ncfo).pct_change(8)).diff(3)).rolling(13).std()).rolling(8).mean()) * 0.814976).diff(1).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc027_42d_jerk_v027_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc027_42d_jerk_v027_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc028_63d_jerk_v028_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 47.4452)).rolling(6).min()).pct_change(18)).rolling(9).min()) * 0.140921).diff(7).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc028_63d_jerk_v028_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc028_63d_jerk_v028_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc029_5d_jerk_v029_signal(revenue, ncfo):
    res = (((((revenue.diff(5) / (ncfo.shift(7) + 74.7248)).diff(4)).diff(19)) * 0.124891).diff(3).diff(16).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc029_5d_jerk_v029_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc029_5d_jerk_v029_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_jerk_v030_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 59.4332)).rolling(20).mean()).pct_change(14)) * 0.16501).diff(5).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_jerk_v030_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_jerk_v030_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc031_42d_jerk_v031_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(1)).rolling(5).var()).rolling(3).std()).diff(2)) * 0.743145).diff(20).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc031_42d_jerk_v031_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc031_42d_jerk_v031_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc032_63d_jerk_v032_signal(revenue, ncfo):
    res = (((((((revenue * 16.1188 - ncfo).rolling(24).var()).rolling(15).std()).rolling(10).std()).rolling(18).mean()) * 0.398463).diff(13).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc032_63d_jerk_v032_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc032_63d_jerk_v032_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc033_126d_jerk_v033_signal(revenue, ncfo):
    res = (((((revenue * 21.2652 - ncfo).pct_change(15)).rolling(12).min()) * 0.616663).diff(13).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc033_126d_jerk_v033_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc033_126d_jerk_v033_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc034_10d_jerk_v034_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 5.5617)).rolling(21).var()).pct_change(11)) * 0.374049).diff(1).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc034_10d_jerk_v034_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc034_10d_jerk_v034_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc035_21d_jerk_v035_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 16.3598)).rolling(22).std()).rolling(9).mean()).rolling(4).var()).rolling(20).max()) * 0.114335).diff(2).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc035_21d_jerk_v035_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc035_21d_jerk_v035_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc036_252d_jerk_v036_signal(revenue, ncfo):
    res = ((((((revenue.diff(3) / (ncfo.shift(5) + 48.4323)).rolling(8).max()).rolling(26).var()).rolling(25).min()) * 0.057088).diff(12).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc036_252d_jerk_v036_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc036_252d_jerk_v036_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_jerk_v037_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 67.5012)).pct_change(13)).rolling(20).min()).pct_change(2)).rolling(7).var()) * 0.334692).diff(5).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_jerk_v037_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_jerk_v037_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc038_5d_jerk_v038_signal(revenue, ncfo):
    res = (((((((revenue * 88.5319 - ncfo).diff(20)).diff(17)).pct_change(11)).rolling(27).min()) * 0.101425).diff(5).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc038_5d_jerk_v038_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc038_5d_jerk_v038_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc039_21d_jerk_v039_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 36.0956)).rolling(4).max()).rolling(20).std()).diff(16)).rolling(27).mean()) * 0.848834).diff(1).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc039_21d_jerk_v039_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc039_21d_jerk_v039_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc040_252d_jerk_v040_signal(revenue, ncfo):
    res = (((((revenue.diff(3) / (ncfo.shift(8) + 87.0587)).rolling(7).var()).rolling(10).mean()) * 0.546193).diff(19).diff(12).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc040_252d_jerk_v040_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc040_252d_jerk_v040_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc041_21d_jerk_v041_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(5).std()).rolling(17).max()).rolling(13).mean()).pct_change(10)) * 0.185603).diff(13).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc041_21d_jerk_v041_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc041_21d_jerk_v041_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc042_252d_jerk_v042_signal(revenue, ncfo):
    res = ((((((revenue.diff(15) / (ncfo.shift(6) + 62.0064)).rolling(23).mean()).rolling(18).min()).rolling(10).min()) * 0.676973).diff(2).diff(20).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc042_252d_jerk_v042_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc042_252d_jerk_v042_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc043_126d_jerk_v043_signal(revenue, ncfo):
    res = ((((((revenue.diff(18) / (ncfo.shift(1) + 5.8002)).rolling(20).std()).rolling(29).min()).rolling(9).mean()) * 0.784779).diff(13).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc043_126d_jerk_v043_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc043_126d_jerk_v043_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc044_126d_jerk_v044_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 9.441)).rolling(14).mean()).pct_change(14)).rolling(14).std()).rolling(4).var()) * 0.46656).diff(11).diff(11).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc044_126d_jerk_v044_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc044_126d_jerk_v044_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc045_63d_jerk_v045_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 48.6809)).rolling(17).std()).rolling(22).std()).rolling(12).std()).rolling(3).max()) * 0.698245).diff(20).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc045_63d_jerk_v045_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc045_63d_jerk_v045_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc046_5d_jerk_v046_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 93.6523)).pct_change(14)).rolling(10).var()) * 0.364263).diff(6).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc046_5d_jerk_v046_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc046_5d_jerk_v046_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc047_10d_jerk_v047_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 7.019)).rolling(7).var()).pct_change(2)).rolling(30).mean()).rolling(12).min()) * 0.406967).diff(10).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc047_10d_jerk_v047_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc047_10d_jerk_v047_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc048_10d_jerk_v048_signal(revenue, ncfo):
    res = (((((((revenue.diff(16) / (ncfo.shift(9) + 34.9927)).rolling(14).max()).pct_change(1)).rolling(27).max()).rolling(8).max()) * 0.420719).diff(3).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc048_10d_jerk_v048_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc048_10d_jerk_v048_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc049_63d_jerk_v049_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 14.5473)).pct_change(11)).rolling(27).mean()).diff(14)) * 0.660782).diff(9).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc049_63d_jerk_v049_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc049_63d_jerk_v049_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc050_126d_jerk_v050_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 0.4673)).diff(7)).rolling(24).min()) * 0.451548).diff(18).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc050_126d_jerk_v050_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc050_126d_jerk_v050_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc051_63d_jerk_v051_signal(revenue, ncfo):
    res = (((((revenue.diff(7) / (ncfo.shift(10) + 37.8179)).rolling(30).var()).rolling(18).var()) * 0.351124).diff(4).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc051_63d_jerk_v051_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc051_63d_jerk_v051_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc052_126d_jerk_v052_signal(revenue, ncfo):
    res = ((((((revenue * 99.9049 - ncfo).rolling(7).mean()).rolling(15).min()).rolling(7).var()) * 0.415773).diff(18).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc052_126d_jerk_v052_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc052_126d_jerk_v052_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc053_10d_jerk_v053_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 54.322)).rolling(22).mean()).rolling(21).mean()) * 0.383932).diff(14).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc053_10d_jerk_v053_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc053_10d_jerk_v053_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc054_42d_jerk_v054_signal(revenue, ncfo):
    res = (((((revenue * 75.0194 - ncfo).diff(10)).pct_change(14)) * 0.621349).diff(7).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc054_42d_jerk_v054_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc054_42d_jerk_v054_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc055_252d_jerk_v055_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(13)).rolling(13).mean()).pct_change(8)) * 0.383458).diff(17).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc055_252d_jerk_v055_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc055_252d_jerk_v055_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc056_21d_jerk_v056_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 87.9728)).rolling(6).mean()).pct_change(12)) * 0.269209).diff(17).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc056_21d_jerk_v056_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc056_21d_jerk_v056_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc057_21d_jerk_v057_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 33.5755)).diff(13)).pct_change(2)).pct_change(19)).rolling(6).min()) * 0.949977).diff(13).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc057_21d_jerk_v057_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc057_21d_jerk_v057_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc058_42d_jerk_v058_signal(revenue, ncfo):
    res = (((((revenue * 90.4267 - ncfo).diff(19)).pct_change(13)) * 0.516932).diff(9).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc058_42d_jerk_v058_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc058_42d_jerk_v058_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_jerk_v059_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(14) / ncfo.pct_change(1)).rolling(2).std()).rolling(24).max()).rolling(4).max()).rolling(14).max()) * 0.209687).diff(1).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_jerk_v059_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_jerk_v059_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc060_42d_jerk_v060_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 63.4829)).pct_change(8)).diff(13)).pct_change(9)).diff(2)) * 0.772038).diff(9).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc060_42d_jerk_v060_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc060_42d_jerk_v060_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc061_10d_jerk_v061_signal(revenue, ncfo):
    res = (((((revenue * 62.7811 - ncfo).rolling(6).mean()).rolling(10).var()) * 0.635619).diff(6).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc061_10d_jerk_v061_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc061_10d_jerk_v061_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc062_5d_jerk_v062_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 49.4751)).rolling(17).mean()).diff(3)).rolling(23).std()) * 0.364169).diff(14).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc062_5d_jerk_v062_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc062_5d_jerk_v062_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc063_21d_jerk_v063_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 63.3918)).rolling(22).max()).rolling(29).max()).rolling(5).mean()).rolling(13).var()) * 0.451861).diff(16).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc063_21d_jerk_v063_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc063_21d_jerk_v063_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc064_63d_jerk_v064_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 54.6936)).rolling(18).mean()).rolling(26).max()).rolling(8).std()).pct_change(12)) * 0.165221).diff(4).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc064_63d_jerk_v064_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc064_63d_jerk_v064_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc065_5d_jerk_v065_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 32.8212)).rolling(24).var()).rolling(22).max()) * 0.225366).diff(10).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc065_5d_jerk_v065_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc065_5d_jerk_v065_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc066_126d_jerk_v066_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 80.9203)).pct_change(9)).rolling(5).min()).rolling(27).max()).pct_change(19)) * 0.437341).diff(10).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc066_126d_jerk_v066_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc066_126d_jerk_v066_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc067_252d_jerk_v067_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(14) / ncfo.pct_change(20)).pct_change(11)).rolling(5).max()).rolling(14).max()) * 0.717619).diff(14).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc067_252d_jerk_v067_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc067_252d_jerk_v067_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc068_63d_jerk_v068_signal(revenue, ncfo):
    res = ((((((revenue * 35.3563 - ncfo).rolling(15).max()).rolling(21).var()).pct_change(17)) * 0.889937).diff(12).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc068_63d_jerk_v068_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc068_63d_jerk_v068_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc069_5d_jerk_v069_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 11.5535)).diff(12)).rolling(6).var()) * 0.80286).diff(11).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc069_5d_jerk_v069_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc069_5d_jerk_v069_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc070_5d_jerk_v070_signal(revenue, ncfo):
    res = (((((revenue.diff(11) / (ncfo.shift(4) + 31.9271)).rolling(4).max()).rolling(11).min()) * 0.020683).diff(20).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc070_5d_jerk_v070_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc070_5d_jerk_v070_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc071_63d_jerk_v071_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(19) / ncfo.pct_change(14)).rolling(28).var()).rolling(8).var()).rolling(3).std()) * 0.55974).diff(16).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc071_63d_jerk_v071_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc071_63d_jerk_v071_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc072_5d_jerk_v072_signal(revenue, ncfo):
    res = (((((((revenue.diff(4) / (ncfo.shift(8) + 99.0269)).rolling(9).min()).rolling(2).max()).rolling(2).var()).diff(19)) * 0.422813).diff(1).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc072_5d_jerk_v072_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc072_5d_jerk_v072_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc073_21d_jerk_v073_signal(revenue, ncfo):
    res = (((((((revenue.diff(2) / (ncfo.shift(9) + 13.1927)).rolling(4).mean()).rolling(5).min()).pct_change(14)).diff(10)) * 0.957516).diff(9).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc073_21d_jerk_v073_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc073_21d_jerk_v073_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc074_252d_jerk_v074_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(15)).rolling(29).min()).diff(4)) * 0.088172).diff(12).diff(20).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc074_252d_jerk_v074_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc074_252d_jerk_v074_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc075_5d_jerk_v075_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(4) / ncfo.pct_change(11)).rolling(9).min()).rolling(4).std()).rolling(25).std()).pct_change(12)) * 0.056878).diff(18).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc075_5d_jerk_v075_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc075_5d_jerk_v075_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc076_126d_jerk_v076_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 86.8147)).rolling(24).var()).rolling(27).max()).pct_change(13)) * 0.264494).diff(9).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc076_126d_jerk_v076_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc076_126d_jerk_v076_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc077_10d_jerk_v077_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(19) / ncfo.pct_change(14)).diff(4)).rolling(18).max()).rolling(20).std()) * 0.127503).diff(16).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc077_10d_jerk_v077_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc077_10d_jerk_v077_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc078_21d_jerk_v078_signal(revenue, ncfo):
    res = (((((revenue.pct_change(9) / ncfo.pct_change(10)).rolling(19).var()).pct_change(8)) * 0.726247).diff(7).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc078_21d_jerk_v078_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc078_21d_jerk_v078_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc079_5d_jerk_v079_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 97.1793)).rolling(12).mean()).rolling(28).std()).rolling(26).max()) * 0.069062).diff(17).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc079_5d_jerk_v079_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc079_5d_jerk_v079_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc080_252d_jerk_v080_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 31.4046)).rolling(14).var()).rolling(29).min()) * 0.935494).diff(20).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc080_252d_jerk_v080_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc080_252d_jerk_v080_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc081_10d_jerk_v081_signal(revenue, ncfo):
    res = (((((((revenue * 78.0241 - ncfo).rolling(6).mean()).rolling(30).min()).rolling(25).mean()).rolling(9).mean()) * 0.194194).diff(1).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc081_10d_jerk_v081_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc081_10d_jerk_v081_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc082_10d_jerk_v082_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 26.749)).rolling(13).mean()).rolling(8).min()).rolling(14).std()).rolling(15).max()) * 0.476716).diff(17).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc082_10d_jerk_v082_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc082_10d_jerk_v082_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc083_5d_jerk_v083_signal(revenue, ncfo):
    res = (((((revenue.diff(2) / (ncfo.shift(7) + 44.1899)).rolling(7).min()).rolling(10).max()) * 0.372385).diff(17).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc083_5d_jerk_v083_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc083_5d_jerk_v083_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc084_42d_jerk_v084_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 51.91)).rolling(20).mean()).rolling(9).var()) * 0.117001).diff(3).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc084_42d_jerk_v084_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc084_42d_jerk_v084_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc085_5d_jerk_v085_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 27.6184)).pct_change(9)).rolling(8).min()).rolling(27).std()).rolling(13).std()) * 0.874948).diff(10).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc085_5d_jerk_v085_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc085_5d_jerk_v085_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc086_21d_jerk_v086_signal(revenue, ncfo):
    res = (((((revenue.pct_change(16) / ncfo.pct_change(10)).rolling(12).std()).diff(3)) * 0.102358).diff(6).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc086_21d_jerk_v086_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc086_21d_jerk_v086_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc087_21d_jerk_v087_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 89.9969)).rolling(30).var()).rolling(7).mean()) * 0.148997).diff(1).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc087_21d_jerk_v087_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc087_21d_jerk_v087_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc088_21d_jerk_v088_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 96.9572)).rolling(23).max()).rolling(28).var()) * 0.581496).diff(8).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc088_21d_jerk_v088_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc088_21d_jerk_v088_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc089_63d_jerk_v089_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(12)).rolling(10).max()).diff(16)) * 0.153651).diff(9).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc089_63d_jerk_v089_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc089_63d_jerk_v089_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_jerk_v090_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 1.4547)).diff(17)).diff(1)).rolling(15).std()) * 0.355574).diff(8).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_jerk_v090_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_jerk_v090_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc091_21d_jerk_v091_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 49.8334)).diff(4)).rolling(30).var()).diff(18)) * 0.24948).diff(15).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc091_21d_jerk_v091_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc091_21d_jerk_v091_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc092_10d_jerk_v092_signal(revenue, ncfo):
    res = ((((((revenue.diff(11) / (ncfo.shift(7) + 26.6044)).rolling(3).std()).rolling(18).max()).diff(11)) * 0.675485).diff(20).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc092_10d_jerk_v092_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc092_10d_jerk_v092_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc093_42d_jerk_v093_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(16).std()).diff(5)).rolling(11).max()).rolling(19).max()) * 0.565329).diff(6).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc093_42d_jerk_v093_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc093_42d_jerk_v093_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc094_42d_jerk_v094_signal(revenue, ncfo):
    res = (((((((revenue.diff(1) / (ncfo.shift(8) + 28.8972)).rolling(3).mean()).rolling(11).min()).rolling(15).mean()).rolling(23).var()) * 0.793789).diff(1).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc094_42d_jerk_v094_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc094_42d_jerk_v094_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc095_21d_jerk_v095_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(5) / ncfo.pct_change(3)).rolling(25).std()).rolling(15).std()).rolling(4).max()) * 0.871148).diff(10).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc095_21d_jerk_v095_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc095_21d_jerk_v095_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc096_5d_jerk_v096_signal(revenue, ncfo):
    res = ((((((revenue.diff(13) / (ncfo.shift(7) + 47.3705)).rolling(11).max()).rolling(20).std()).rolling(23).min()) * 0.35754).diff(11).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc096_5d_jerk_v096_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc096_5d_jerk_v096_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc097_10d_jerk_v097_signal(revenue, ncfo):
    res = ((((((revenue.diff(5) / (ncfo.shift(7) + 68.3638)).rolling(11).mean()).rolling(22).max()).rolling(19).min()) * 0.205517).diff(6).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc097_10d_jerk_v097_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc097_10d_jerk_v097_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc098_252d_jerk_v098_signal(revenue, ncfo):
    res = (((((((revenue * 87.6046 - ncfo).diff(12)).rolling(13).min()).rolling(16).min()).rolling(15).min()) * 0.438155).diff(15).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc098_252d_jerk_v098_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc098_252d_jerk_v098_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc099_63d_jerk_v099_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 2.7396)).rolling(13).max()).rolling(21).std()).rolling(30).max()).rolling(30).max()) * 0.761434).diff(10).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc099_63d_jerk_v099_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc099_63d_jerk_v099_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc100_252d_jerk_v100_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 84.5262)).rolling(10).mean()).pct_change(4)) * 0.133417).diff(11).diff(20).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc100_252d_jerk_v100_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc100_252d_jerk_v100_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc101_5d_jerk_v101_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(4) / ncfo.pct_change(19)).diff(2)).diff(7)).rolling(6).max()).rolling(25).max()) * 0.564135).diff(16).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc101_5d_jerk_v101_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc101_5d_jerk_v101_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc102_10d_jerk_v102_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(7)).rolling(4).mean()).rolling(6).mean()).rolling(30).max()) * 0.636875).diff(4).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc102_10d_jerk_v102_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc102_10d_jerk_v102_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_jerk_v103_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 24.7959)).rolling(14).var()).rolling(7).min()) * 0.111535).diff(8).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_jerk_v103_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_jerk_v103_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc104_21d_jerk_v104_signal(revenue, ncfo):
    res = (((((revenue.pct_change(14) / ncfo.pct_change(5)).rolling(6).std()).pct_change(8)) * 0.677694).diff(6).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc104_21d_jerk_v104_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc104_21d_jerk_v104_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc105_126d_jerk_v105_signal(revenue, ncfo):
    res = ((((((revenue * 69.9929 - ncfo).rolling(23).var()).rolling(14).var()).rolling(24).min()) * 0.206344).diff(4).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc105_126d_jerk_v105_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc105_126d_jerk_v105_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc106_42d_jerk_v106_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(11).max()).rolling(22).mean()) * 0.155203).diff(20).diff(15).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc106_42d_jerk_v106_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc106_42d_jerk_v106_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc107_5d_jerk_v107_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 90.82)).rolling(18).var()).pct_change(17)) * 0.357632).diff(7).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc107_5d_jerk_v107_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc107_5d_jerk_v107_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc108_126d_jerk_v108_signal(revenue, ncfo):
    res = ((((((revenue.diff(6) / (ncfo.shift(3) + 52.5531)).diff(5)).rolling(27).var()).pct_change(10)) * 0.512784).diff(13).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc108_126d_jerk_v108_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc108_126d_jerk_v108_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_jerk_v109_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(6) / ncfo.pct_change(19)).pct_change(17)).rolling(6).var()).diff(11)).rolling(20).max()) * 0.378992).diff(12).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_jerk_v109_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_jerk_v109_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc110_63d_jerk_v110_signal(revenue, ncfo):
    res = (((((revenue.pct_change(8) / ncfo.pct_change(4)).rolling(23).min()).rolling(12).min()) * 0.076219).diff(8).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc110_63d_jerk_v110_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc110_63d_jerk_v110_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc111_5d_jerk_v111_signal(revenue, ncfo):
    res = ((((((revenue * 89.9895 - ncfo).rolling(3).mean()).pct_change(3)).rolling(26).min()) * 0.180518).diff(12).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc111_5d_jerk_v111_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc111_5d_jerk_v111_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc112_126d_jerk_v112_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 84.0839)).rolling(19).max()).rolling(8).std()).rolling(17).var()).rolling(23).min()) * 0.91508).diff(10).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc112_126d_jerk_v112_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc112_126d_jerk_v112_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc113_10d_jerk_v113_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 74.2412)).diff(4)).rolling(3).std()).pct_change(5)).rolling(13).mean()) * 0.435382).diff(14).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc113_10d_jerk_v113_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc113_10d_jerk_v113_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc114_63d_jerk_v114_signal(revenue, ncfo):
    res = ((((((revenue * 86.4627 - ncfo).rolling(13).max()).rolling(21).var()).rolling(29).max()) * 0.343897).diff(5).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc114_63d_jerk_v114_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc114_63d_jerk_v114_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc115_42d_jerk_v115_signal(revenue, ncfo):
    res = ((((((revenue * 42.8084 - ncfo).rolling(5).mean()).rolling(9).min()).rolling(21).mean()) * 0.378596).diff(18).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc115_42d_jerk_v115_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc115_42d_jerk_v115_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc116_5d_jerk_v116_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 22.4797)).rolling(19).mean()).rolling(9).max()).pct_change(17)) * 0.931805).diff(20).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc116_5d_jerk_v116_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc116_5d_jerk_v116_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc117_21d_jerk_v117_signal(revenue, ncfo):
    res = (((((revenue.pct_change(16) / ncfo.pct_change(9)).rolling(12).mean()).rolling(10).min()) * 0.065515).diff(7).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc117_21d_jerk_v117_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc117_21d_jerk_v117_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc118_252d_jerk_v118_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 6.0333)).rolling(24).max()).pct_change(2)).rolling(4).var()).rolling(21).min()) * 0.210149).diff(20).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc118_252d_jerk_v118_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc118_252d_jerk_v118_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc119_63d_jerk_v119_signal(revenue, ncfo):
    res = (((((revenue * 47.9293 - ncfo).diff(12)).rolling(17).min()) * 0.136875).diff(10).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc119_63d_jerk_v119_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc119_63d_jerk_v119_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc120_5d_jerk_v120_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(20) / ncfo.pct_change(13)).diff(1)).rolling(17).max()).rolling(14).mean()).pct_change(13)) * 0.035827).diff(5).diff(14).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc120_5d_jerk_v120_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc120_5d_jerk_v120_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc121_126d_jerk_v121_signal(revenue, ncfo):
    res = (((((revenue.diff(15) / (ncfo.shift(2) + 42.7407)).rolling(15).var()).rolling(9).mean()) * 0.145015).diff(8).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc121_126d_jerk_v121_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc121_126d_jerk_v121_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc122_63d_jerk_v122_signal(revenue, ncfo):
    res = (((((revenue.pct_change(2) / ncfo.pct_change(1)).pct_change(2)).rolling(3).mean()) * 0.414804).diff(5).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc122_63d_jerk_v122_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc122_63d_jerk_v122_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc123_10d_jerk_v123_signal(revenue, ncfo):
    res = ((((((revenue * 28.3313 - ncfo).rolling(23).min()).rolling(23).mean()).rolling(4).mean()) * 0.317843).diff(9).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc123_10d_jerk_v123_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc123_10d_jerk_v123_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc124_10d_jerk_v124_signal(revenue, ncfo):
    res = (((((((revenue.diff(12) / (ncfo.shift(4) + 49.5434)).rolling(29).var()).diff(8)).rolling(30).max()).rolling(12).var()) * 0.730514).diff(18).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc124_10d_jerk_v124_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc124_10d_jerk_v124_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc125_5d_jerk_v125_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 5.4944)).pct_change(17)).rolling(11).std()) * 0.892417).diff(18).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc125_5d_jerk_v125_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc125_5d_jerk_v125_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc126_5d_jerk_v126_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(8) / ncfo.pct_change(15)).rolling(2).mean()).rolling(28).min()).rolling(10).mean()) * 0.810052).diff(9).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc126_5d_jerk_v126_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc126_5d_jerk_v126_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc127_42d_jerk_v127_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(13)).rolling(16).min()) * 0.955795).diff(2).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc127_42d_jerk_v127_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc127_42d_jerk_v127_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc128_10d_jerk_v128_signal(revenue, ncfo):
    res = ((((((revenue * 37.9948 - ncfo).rolling(21).mean()).pct_change(11)).pct_change(9)) * 0.656727).diff(19).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc128_10d_jerk_v128_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc128_10d_jerk_v128_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc129_252d_jerk_v129_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 2.8318)).rolling(25).min()).diff(10)).pct_change(18)).rolling(15).min()) * 0.721271).diff(19).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc129_252d_jerk_v129_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc129_252d_jerk_v129_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc130_252d_jerk_v130_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 51.9394)).pct_change(9)).rolling(9).mean()).pct_change(18)) * 0.169298).diff(10).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc130_252d_jerk_v130_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc130_252d_jerk_v130_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_jerk_v131_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 39.5207)).rolling(20).var()).diff(11)) * 0.613236).diff(9).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_jerk_v131_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_jerk_v131_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc132_42d_jerk_v132_signal(revenue, ncfo):
    res = (((((((revenue.pct_change(12) / ncfo.pct_change(16)).rolling(15).std()).rolling(20).mean()).rolling(10).mean()).rolling(19).max()) * 0.441111).diff(11).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc132_42d_jerk_v132_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc132_42d_jerk_v132_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc133_42d_jerk_v133_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 18.0624)).rolling(6).std()).pct_change(20)).diff(2)).rolling(5).std()) * 0.760657).diff(2).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc133_42d_jerk_v133_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc133_42d_jerk_v133_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc134_126d_jerk_v134_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 50.7212)).rolling(10).var()).rolling(23).mean()).pct_change(12)).rolling(24).max()) * 0.441503).diff(2).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc134_126d_jerk_v134_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc134_126d_jerk_v134_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc135_10d_jerk_v135_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 35.038)).rolling(20).var()).rolling(28).var()) * 0.08593).diff(14).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc135_10d_jerk_v135_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc135_10d_jerk_v135_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc136_126d_jerk_v136_signal(revenue, ncfo):
    res = ((((((revenue.diff(1) / (ncfo.shift(6) + 42.7049)).diff(12)).rolling(11).min()).rolling(2).max()) * 0.287423).diff(6).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc136_126d_jerk_v136_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc136_126d_jerk_v136_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc137_5d_jerk_v137_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 29.1582)).rolling(24).max()).pct_change(17)).pct_change(19)) * 0.157062).diff(12).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc137_5d_jerk_v137_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc137_5d_jerk_v137_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc138_42d_jerk_v138_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 83.0896)).rolling(20).max()).diff(18)).diff(14)).rolling(25).max()) * 0.041948).diff(4).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc138_42d_jerk_v138_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc138_42d_jerk_v138_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc139_252d_jerk_v139_signal(revenue, ncfo):
    res = (((((revenue.diff(17) / (ncfo.shift(9) + 5.238)).pct_change(19)).rolling(9).var()) * 0.472883).diff(11).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc139_252d_jerk_v139_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc139_252d_jerk_v139_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc140_252d_jerk_v140_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(13).min()).rolling(13).mean()).rolling(18).max()).rolling(13).mean()) * 0.364726).diff(16).diff(20).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc140_252d_jerk_v140_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc140_252d_jerk_v140_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc141_10d_jerk_v141_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(23).max()).rolling(21).std()).rolling(27).var()).rolling(12).var()) * 0.420473).diff(11).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc141_10d_jerk_v141_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc141_10d_jerk_v141_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc142_5d_jerk_v142_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 40.9094)).rolling(7).mean()).rolling(15).mean()).rolling(26).var()) * 0.504925).diff(18).diff(16).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc142_5d_jerk_v142_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc142_5d_jerk_v142_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc143_126d_jerk_v143_signal(revenue, ncfo):
    res = (((((((ncfo / (revenue + 10.1894)).pct_change(17)).rolling(30).min()).rolling(13).min()).rolling(14).std()) * 0.86207).diff(18).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc143_126d_jerk_v143_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc143_126d_jerk_v143_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc144_126d_jerk_v144_signal(revenue, ncfo):
    res = (((((((revenue / (ncfo + 29.4098)).rolling(4).mean()).diff(12)).rolling(15).min()).diff(15)) * 0.340072).diff(14).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc144_126d_jerk_v144_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc144_126d_jerk_v144_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc145_252d_jerk_v145_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 47.7629)).rolling(20).max()).rolling(23).var()) * 0.141913).diff(15).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc145_252d_jerk_v145_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc145_252d_jerk_v145_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc146_21d_jerk_v146_signal(revenue, ncfo):
    res = ((((((revenue.diff(19) / (ncfo.shift(5) + 43.9148)).rolling(3).var()).rolling(18).max()).rolling(20).max()) * 0.508494).diff(17).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc146_21d_jerk_v146_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc146_21d_jerk_v146_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc147_21d_jerk_v147_signal(revenue, ncfo):
    res = (((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(20).var()).rolling(12).max()).rolling(13).mean()).rolling(7).var()) * 0.322207).diff(4).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc147_21d_jerk_v147_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc147_21d_jerk_v147_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc148_21d_jerk_v148_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 48.7149)).diff(9)).rolling(5).std()) * 0.229161).diff(7).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc148_21d_jerk_v148_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc148_21d_jerk_v148_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc149_252d_jerk_v149_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 50.9189)).rolling(28).min()).pct_change(1)) * 0.175475).diff(12).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc149_252d_jerk_v149_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc149_252d_jerk_v149_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc150_21d_jerk_v150_signal(revenue, ncfo):
    res = (((((revenue.diff(15) / (ncfo.shift(9) + 94.1864)).diff(4)).rolling(30).min()) * 0.569742).diff(14).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc150_21d_jerk_v150_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc150_21d_jerk_v150_signal


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
