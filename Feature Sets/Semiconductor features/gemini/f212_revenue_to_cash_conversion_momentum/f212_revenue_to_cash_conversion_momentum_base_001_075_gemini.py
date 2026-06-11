import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f212r_f212_revenue_to_cash_conversion_momentum_calc001_42d_base_v001_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 18.417)).rolling(5).min()).rolling(17).var()) * 0.908919)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc001_42d_base_v001_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc001_42d_base_v001_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc002_42d_base_v002_signal(revenue, ncfo):
    res = ((((revenue * 84.592 - ncfo).rolling(28).min()).diff(4)) * 0.286612)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc002_42d_base_v002_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc002_42d_base_v002_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc003_21d_base_v003_signal(revenue, ncfo):
    res = (((((revenue * 55.6594 - ncfo).rolling(21).std()).rolling(19).std()).rolling(17).std()) * 0.079506)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc003_21d_base_v003_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc003_21d_base_v003_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc004_42d_base_v004_signal(revenue, ncfo):
    res = ((((((revenue.diff(19) / (ncfo.shift(7) + 6.6994)).diff(8)).rolling(23).std()).diff(3)).diff(19)) * 0.214073)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc004_42d_base_v004_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc004_42d_base_v004_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc005_252d_base_v005_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(14).var()).rolling(21).mean()) * 0.59032)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc005_252d_base_v005_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc005_252d_base_v005_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc006_5d_base_v006_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 68.5823)).pct_change(5)).rolling(30).max()) * 0.594477)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc006_5d_base_v006_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc006_5d_base_v006_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc007_252d_base_v007_signal(revenue, ncfo):
    res = (((((revenue.diff(5) / (ncfo.shift(3) + 63.6497)).rolling(20).max()).rolling(8).min()).rolling(23).std()) * 0.010181)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc007_252d_base_v007_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc007_252d_base_v007_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc008_21d_base_v008_signal(revenue, ncfo):
    res = ((((revenue * 30.0436 - ncfo).rolling(18).max()).rolling(29).min()) * 0.78846)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc008_21d_base_v008_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc008_21d_base_v008_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc009_10d_base_v009_signal(revenue, ncfo):
    res = ((((revenue.diff(18) / (ncfo.shift(1) + 85.2653)).pct_change(10)).pct_change(1)) * 0.071162)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc009_10d_base_v009_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc009_10d_base_v009_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc010_10d_base_v010_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(23).std()).rolling(17).std()).rolling(8).std()).rolling(14).max()) * 0.588361)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc010_10d_base_v010_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc010_10d_base_v010_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc011_252d_base_v011_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 92.4558)).diff(1)).rolling(25).std()) * 0.833163)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc011_252d_base_v011_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc011_252d_base_v011_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc012_42d_base_v012_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(15).max()).rolling(7).max()).rolling(18).min()).rolling(19).min()) * 0.965476)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc012_42d_base_v012_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc012_42d_base_v012_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc013_252d_base_v013_signal(revenue, ncfo):
    res = (((((revenue * 45.0596 - ncfo).pct_change(8)).diff(17)).rolling(15).var()) * 0.358201)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc013_252d_base_v013_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc013_252d_base_v013_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc014_63d_base_v014_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 57.6776)).rolling(24).min()).rolling(6).mean()).diff(17)).pct_change(9)) * 0.042793)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc014_63d_base_v014_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc014_63d_base_v014_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc015_42d_base_v015_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(8) / ncfo.pct_change(16)).diff(3)).diff(18)).pct_change(19)).rolling(21).var()) * 0.52289)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc015_42d_base_v015_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc015_42d_base_v015_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc016_5d_base_v016_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(11)).rolling(13).min()).pct_change(10)).rolling(7).var()) * 0.534333)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc016_5d_base_v016_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc016_5d_base_v016_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc017_5d_base_v017_signal(revenue, ncfo):
    res = (((((revenue.pct_change(9) / ncfo.pct_change(2)).rolling(7).max()).rolling(3).max()).diff(10)) * 0.595684)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc017_5d_base_v017_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc017_5d_base_v017_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc018_252d_base_v018_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 73.7643)).rolling(6).var()).rolling(10).max()).rolling(29).var()) * 0.036752)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc018_252d_base_v018_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc018_252d_base_v018_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc019_21d_base_v019_signal(revenue, ncfo):
    res = ((((revenue.diff(6) / (ncfo.shift(10) + 1.5189)).rolling(27).var()).diff(8)) * 0.119318)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc019_21d_base_v019_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc019_21d_base_v019_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc020_42d_base_v020_signal(revenue, ncfo):
    res = ((((revenue * 18.1628 - ncfo).pct_change(16)).pct_change(14)) * 0.526841)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc020_42d_base_v020_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc020_42d_base_v020_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc021_252d_base_v021_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 38.3784)).rolling(26).var()).pct_change(4)).rolling(7).mean()).rolling(14).min()) * 0.657454)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc021_252d_base_v021_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc021_252d_base_v021_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc022_42d_base_v022_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(18).std()).pct_change(14)).rolling(11).mean()) * 0.741228)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc022_42d_base_v022_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc022_42d_base_v022_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc023_252d_base_v023_signal(revenue, ncfo):
    res = (((((revenue.pct_change(4) / ncfo.pct_change(18)).pct_change(14)).rolling(22).max()).pct_change(9)) * 0.674924)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc023_252d_base_v023_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc023_252d_base_v023_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_base_v024_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(13) / ncfo.pct_change(15)).rolling(25).std()).diff(19)).pct_change(7)).rolling(12).max()) * 0.79627)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_base_v024_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc024_21d_base_v024_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc025_126d_base_v025_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 69.0588)).rolling(18).mean()).rolling(23).mean()).rolling(13).min()) * 0.186318)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc025_126d_base_v025_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc025_126d_base_v025_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc026_10d_base_v026_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 72.5525)).diff(7)).rolling(22).max()).rolling(24).mean()).rolling(4).mean()) * 0.256858)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc026_10d_base_v026_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc026_10d_base_v026_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc027_252d_base_v027_signal(revenue, ncfo):
    res = (((((revenue.diff(19) / (ncfo.shift(3) + 60.5081)).rolling(23).min()).rolling(22).mean()).rolling(10).min()) * 0.378439)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc027_252d_base_v027_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc027_252d_base_v027_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc028_252d_base_v028_signal(revenue, ncfo):
    res = ((((revenue.diff(11) / (ncfo.shift(5) + 42.7556)).rolling(14).min()).rolling(3).var()) * 0.895324)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc028_252d_base_v028_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc028_252d_base_v028_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc029_21d_base_v029_signal(revenue, ncfo):
    res = (((((revenue * 95.565 - ncfo).rolling(22).std()).rolling(5).min()).rolling(19).std()) * 0.269372)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc029_21d_base_v029_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc029_21d_base_v029_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_base_v030_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 43.1822)).rolling(20).mean()).diff(9)) * 0.611687)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_base_v030_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc030_252d_base_v030_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc031_252d_base_v031_signal(revenue, ncfo):
    res = ((((revenue.diff(5) / (ncfo.shift(1) + 44.6436)).diff(11)).rolling(20).min()) * 0.888582)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc031_252d_base_v031_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc031_252d_base_v031_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc032_5d_base_v032_signal(revenue, ncfo):
    res = ((((revenue.pct_change(14) / ncfo.pct_change(13)).rolling(9).max()).rolling(14).mean()) * 0.931113)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc032_5d_base_v032_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc032_5d_base_v032_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc033_126d_base_v033_signal(revenue, ncfo):
    res = (((((revenue.pct_change(12) / ncfo.pct_change(11)).rolling(3).min()).diff(3)).rolling(19).var()) * 0.482425)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc033_126d_base_v033_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc033_126d_base_v033_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc034_252d_base_v034_signal(revenue, ncfo):
    res = ((((revenue * 96.0965 - ncfo).rolling(23).min()).rolling(11).std()) * 0.088848)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc034_252d_base_v034_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc034_252d_base_v034_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc035_126d_base_v035_signal(revenue, ncfo):
    res = ((((revenue.pct_change(3) / ncfo.pct_change(15)).rolling(3).std()).rolling(2).std()) * 0.114633)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc035_126d_base_v035_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc035_126d_base_v035_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc036_126d_base_v036_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(15)).rolling(3).mean()).rolling(3).var()).rolling(27).var()) * 0.243715)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc036_126d_base_v036_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc036_126d_base_v036_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_base_v037_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(18) / ncfo.pct_change(5)).rolling(4).std()).rolling(25).mean()).rolling(17).std()).diff(1)) * 0.125823)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_base_v037_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc037_126d_base_v037_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc038_42d_base_v038_signal(revenue, ncfo):
    res = ((((revenue.pct_change(1) / ncfo.pct_change(6)).rolling(28).var()).pct_change(4)) * 0.616005)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc038_42d_base_v038_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc038_42d_base_v038_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc039_42d_base_v039_signal(revenue, ncfo):
    res = ((((((revenue * 61.1615 - ncfo).rolling(4).std()).pct_change(7)).rolling(12).min()).pct_change(13)) * 0.828645)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc039_42d_base_v039_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc039_42d_base_v039_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc040_21d_base_v040_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 12.1682)).rolling(12).std()).rolling(5).mean()).rolling(6).var()).pct_change(14)) * 0.680407)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc040_21d_base_v040_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc040_21d_base_v040_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc041_10d_base_v041_signal(revenue, ncfo):
    res = ((((ncfo / (revenue + 69.6599)).pct_change(20)).rolling(26).min()) * 0.55234)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc041_10d_base_v041_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc041_10d_base_v041_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc042_10d_base_v042_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(6) / ncfo.pct_change(3)).rolling(30).max()).rolling(15).var()).diff(16)).diff(5)) * 0.487228)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc042_10d_base_v042_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc042_10d_base_v042_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc043_10d_base_v043_signal(revenue, ncfo):
    res = ((((((revenue * 14.3945 - ncfo).rolling(21).mean()).rolling(24).std()).rolling(21).min()).rolling(22).mean()) * 0.275531)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc043_10d_base_v043_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc043_10d_base_v043_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc044_252d_base_v044_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 78.28)).rolling(21).mean()).rolling(29).var()).pct_change(18)).rolling(9).max()) * 0.350896)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc044_252d_base_v044_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc044_252d_base_v044_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc045_42d_base_v045_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 77.0561)).pct_change(16)).rolling(7).min()).rolling(23).std()).rolling(3).mean()) * 0.656141)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc045_42d_base_v045_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc045_42d_base_v045_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc046_126d_base_v046_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 36.4829)).diff(2)).rolling(7).max()) * 0.215398)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc046_126d_base_v046_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc046_126d_base_v046_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc047_10d_base_v047_signal(revenue, ncfo):
    res = ((((((revenue * 78.5707 - ncfo).rolling(15).var()).rolling(25).std()).diff(11)).rolling(26).std()) * 0.48536)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc047_10d_base_v047_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc047_10d_base_v047_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc048_5d_base_v048_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 32.6806)).rolling(17).max()).rolling(30).mean()).rolling(6).min()) * 0.106103)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc048_5d_base_v048_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc048_5d_base_v048_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc049_10d_base_v049_signal(revenue, ncfo):
    res = ((((revenue.pct_change(5) / ncfo.pct_change(15)).diff(12)).rolling(8).var()) * 0.455891)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc049_10d_base_v049_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc049_10d_base_v049_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc050_21d_base_v050_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(7).min()).pct_change(11)).rolling(30).std()) * 0.688366)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc050_21d_base_v050_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc050_21d_base_v050_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc051_21d_base_v051_signal(revenue, ncfo):
    res = ((((ncfo / (revenue + 60.4032)).rolling(29).min()).rolling(17).max()) * 0.783756)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc051_21d_base_v051_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc051_21d_base_v051_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc052_252d_base_v052_signal(revenue, ncfo):
    res = ((((revenue.pct_change(1) / ncfo.pct_change(14)).rolling(12).std()).rolling(20).min()) * 0.589749)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc052_252d_base_v052_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc052_252d_base_v052_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc053_10d_base_v053_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 89.1931)).rolling(25).min()).pct_change(17)) * 0.589936)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc053_10d_base_v053_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc053_10d_base_v053_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc054_5d_base_v054_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 42.6272)).pct_change(1)).diff(14)).rolling(6).std()).rolling(11).var()) * 0.396434)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc054_5d_base_v054_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc054_5d_base_v054_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc055_10d_base_v055_signal(revenue, ncfo):
    res = ((((((revenue * 64.7993 - ncfo).rolling(2).max()).rolling(16).min()).pct_change(5)).pct_change(13)) * 0.098915)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc055_10d_base_v055_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc055_10d_base_v055_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc056_10d_base_v056_signal(revenue, ncfo):
    res = (((((revenue.pct_change(3) / ncfo.pct_change(13)).rolling(3).max()).rolling(15).var()).pct_change(9)) * 0.373012)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc056_10d_base_v056_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc056_10d_base_v056_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc057_126d_base_v057_signal(revenue, ncfo):
    res = ((((revenue.pct_change(20) / ncfo.pct_change(11)).rolling(23).max()).rolling(30).var()) * 0.541586)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc057_126d_base_v057_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc057_126d_base_v057_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc058_5d_base_v058_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 11.1856)).rolling(24).max()).rolling(19).mean()).diff(7)).rolling(12).std()) * 0.368279)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc058_5d_base_v058_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc058_5d_base_v058_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_base_v059_signal(revenue, ncfo):
    res = (((((revenue.diff(19) / (ncfo.shift(4) + 54.0094)).rolling(23).max()).rolling(10).min()).rolling(4).mean()) * 0.646058)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_base_v059_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc059_10d_base_v059_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc060_21d_base_v060_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(16) / ncfo.pct_change(18)).rolling(16).var()).rolling(13).max()).pct_change(3)).rolling(30).std()) * 0.486502)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc060_21d_base_v060_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc060_21d_base_v060_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc061_42d_base_v061_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 8.8221)).rolling(24).mean()).rolling(17).std()).rolling(29).std()) * 0.392869)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc061_42d_base_v061_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc061_42d_base_v061_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc062_10d_base_v062_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(16).min()).diff(1)).rolling(8).var()) * 0.624731)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc062_10d_base_v062_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc062_10d_base_v062_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc063_5d_base_v063_signal(revenue, ncfo):
    res = ((((((revenue.diff(17) / (ncfo.shift(6) + 2.3015)).diff(11)).rolling(20).min()).diff(17)).pct_change(18)) * 0.795949)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc063_5d_base_v063_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc063_5d_base_v063_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc064_42d_base_v064_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(26).var()).pct_change(2)).rolling(13).std()) * 0.565907)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc064_42d_base_v064_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc064_42d_base_v064_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc065_21d_base_v065_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 45.6471)).diff(5)).rolling(9).std()).rolling(3).mean()).rolling(20).var()) * 0.173036)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc065_21d_base_v065_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc065_21d_base_v065_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc066_10d_base_v066_signal(revenue, ncfo):
    res = ((((revenue.diff(7) / (ncfo.shift(9) + 44.1448)).rolling(16).var()).rolling(7).max()) * 0.372279)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc066_10d_base_v066_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc066_10d_base_v066_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc067_63d_base_v067_signal(revenue, ncfo):
    res = ((((revenue.diff(13) / (ncfo.shift(8) + 30.2258)).rolling(25).mean()).rolling(18).max()) * 0.912025)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc067_63d_base_v067_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc067_63d_base_v067_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc068_21d_base_v068_signal(revenue, ncfo):
    res = (((((revenue.pct_change(5) / ncfo.pct_change(19)).rolling(24).var()).rolling(25).mean()).rolling(30).min()) * 0.299646)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc068_21d_base_v068_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc068_21d_base_v068_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc069_5d_base_v069_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 14.0284)).rolling(4).var()).rolling(3).var()).rolling(22).max()) * 0.549941)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc069_5d_base_v069_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc069_5d_base_v069_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc070_10d_base_v070_signal(revenue, ncfo):
    res = (((((revenue * 58.3848 - ncfo).diff(3)).rolling(14).max()).rolling(17).std()) * 0.227701)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc070_10d_base_v070_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc070_10d_base_v070_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc071_21d_base_v071_signal(revenue, ncfo):
    res = (((((revenue.pct_change(13) / ncfo.pct_change(5)).rolling(14).var()).rolling(2).var()).rolling(13).var()) * 0.511325)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc071_21d_base_v071_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc071_21d_base_v071_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc072_21d_base_v072_signal(revenue, ncfo):
    res = (((((revenue.pct_change(7) / ncfo.pct_change(15)).pct_change(15)).rolling(7).var()).pct_change(14)) * 0.446665)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc072_21d_base_v072_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc072_21d_base_v072_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc073_126d_base_v073_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 89.6532)).rolling(29).min()).rolling(12).max()).rolling(20).mean()) * 0.146776)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc073_126d_base_v073_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc073_126d_base_v073_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc074_252d_base_v074_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(26).max()).rolling(8).std()).rolling(28).std()).rolling(11).min()) * 0.016486)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc074_252d_base_v074_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc074_252d_base_v074_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc075_63d_base_v075_signal(revenue, ncfo):
    res = ((((((revenue * 49.1095 - ncfo).rolling(9).min()).rolling(27).mean()).rolling(6).mean()).rolling(11).var()) * 0.816343)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc075_63d_base_v075_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc075_63d_base_v075_signal


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
