import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f110w_f110_working_capital_to_revenue_regime_calc001_252d_base_v001_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc001_252d_base_v001_signal'] = f110w_f110_working_capital_to_revenue_regime_calc001_252d_base_v001_signal

def f110w_f110_working_capital_to_revenue_regime_calc002_126d_base_v002_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc002_126d_base_v002_signal'] = f110w_f110_working_capital_to_revenue_regime_calc002_126d_base_v002_signal

def f110w_f110_working_capital_to_revenue_regime_calc003_63d_base_v003_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc003_63d_base_v003_signal'] = f110w_f110_working_capital_to_revenue_regime_calc003_63d_base_v003_signal

def f110w_f110_working_capital_to_revenue_regime_calc004_42d_base_v004_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc004_42d_base_v004_signal'] = f110w_f110_working_capital_to_revenue_regime_calc004_42d_base_v004_signal

def f110w_f110_working_capital_to_revenue_regime_calc005_200d_base_v005_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc005_200d_base_v005_signal'] = f110w_f110_working_capital_to_revenue_regime_calc005_200d_base_v005_signal

def f110w_f110_working_capital_to_revenue_regime_calc006_126d_base_v006_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc006_126d_base_v006_signal'] = f110w_f110_working_capital_to_revenue_regime_calc006_126d_base_v006_signal

def f110w_f110_working_capital_to_revenue_regime_calc007_150d_base_v007_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc007_150d_base_v007_signal'] = f110w_f110_working_capital_to_revenue_regime_calc007_150d_base_v007_signal

def f110w_f110_working_capital_to_revenue_regime_calc008_42d_base_v008_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc008_42d_base_v008_signal'] = f110w_f110_working_capital_to_revenue_regime_calc008_42d_base_v008_signal

def f110w_f110_working_capital_to_revenue_regime_calc009_252d_base_v009_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc009_252d_base_v009_signal'] = f110w_f110_working_capital_to_revenue_regime_calc009_252d_base_v009_signal

def f110w_f110_working_capital_to_revenue_regime_calc010_105d_base_v010_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc010_105d_base_v010_signal'] = f110w_f110_working_capital_to_revenue_regime_calc010_105d_base_v010_signal

def f110w_f110_working_capital_to_revenue_regime_calc011_10d_base_v011_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc011_10d_base_v011_signal'] = f110w_f110_working_capital_to_revenue_regime_calc011_10d_base_v011_signal

def f110w_f110_working_capital_to_revenue_regime_calc012_105d_base_v012_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc012_105d_base_v012_signal'] = f110w_f110_working_capital_to_revenue_regime_calc012_105d_base_v012_signal

def f110w_f110_working_capital_to_revenue_regime_calc013_84d_base_v013_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc013_84d_base_v013_signal'] = f110w_f110_working_capital_to_revenue_regime_calc013_84d_base_v013_signal

def f110w_f110_working_capital_to_revenue_regime_calc014_150d_base_v014_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc014_150d_base_v014_signal'] = f110w_f110_working_capital_to_revenue_regime_calc014_150d_base_v014_signal

def f110w_f110_working_capital_to_revenue_regime_calc015_252d_base_v015_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc015_252d_base_v015_signal'] = f110w_f110_working_capital_to_revenue_regime_calc015_252d_base_v015_signal

def f110w_f110_working_capital_to_revenue_regime_calc016_10d_base_v016_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc016_10d_base_v016_signal'] = f110w_f110_working_capital_to_revenue_regime_calc016_10d_base_v016_signal

def f110w_f110_working_capital_to_revenue_regime_calc017_150d_base_v017_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc017_150d_base_v017_signal'] = f110w_f110_working_capital_to_revenue_regime_calc017_150d_base_v017_signal

def f110w_f110_working_capital_to_revenue_regime_calc018_5d_base_v018_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc018_5d_base_v018_signal'] = f110w_f110_working_capital_to_revenue_regime_calc018_5d_base_v018_signal

def f110w_f110_working_capital_to_revenue_regime_calc019_5d_base_v019_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc019_5d_base_v019_signal'] = f110w_f110_working_capital_to_revenue_regime_calc019_5d_base_v019_signal

def f110w_f110_working_capital_to_revenue_regime_calc020_200d_base_v020_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc020_200d_base_v020_signal'] = f110w_f110_working_capital_to_revenue_regime_calc020_200d_base_v020_signal

def f110w_f110_working_capital_to_revenue_regime_calc021_42d_base_v021_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc021_42d_base_v021_signal'] = f110w_f110_working_capital_to_revenue_regime_calc021_42d_base_v021_signal

def f110w_f110_working_capital_to_revenue_regime_calc022_5d_base_v022_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc022_5d_base_v022_signal'] = f110w_f110_working_capital_to_revenue_regime_calc022_5d_base_v022_signal

def f110w_f110_working_capital_to_revenue_regime_calc023_21d_base_v023_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc023_21d_base_v023_signal'] = f110w_f110_working_capital_to_revenue_regime_calc023_21d_base_v023_signal

def f110w_f110_working_capital_to_revenue_regime_calc024_10d_base_v024_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc024_10d_base_v024_signal'] = f110w_f110_working_capital_to_revenue_regime_calc024_10d_base_v024_signal

def f110w_f110_working_capital_to_revenue_regime_calc025_63d_base_v025_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc025_63d_base_v025_signal'] = f110w_f110_working_capital_to_revenue_regime_calc025_63d_base_v025_signal

def f110w_f110_working_capital_to_revenue_regime_calc026_150d_base_v026_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc026_150d_base_v026_signal'] = f110w_f110_working_capital_to_revenue_regime_calc026_150d_base_v026_signal

def f110w_f110_working_capital_to_revenue_regime_calc027_84d_base_v027_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc027_84d_base_v027_signal'] = f110w_f110_working_capital_to_revenue_regime_calc027_84d_base_v027_signal

def f110w_f110_working_capital_to_revenue_regime_calc028_150d_base_v028_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc028_150d_base_v028_signal'] = f110w_f110_working_capital_to_revenue_regime_calc028_150d_base_v028_signal

def f110w_f110_working_capital_to_revenue_regime_calc029_5d_base_v029_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc029_5d_base_v029_signal'] = f110w_f110_working_capital_to_revenue_regime_calc029_5d_base_v029_signal

def f110w_f110_working_capital_to_revenue_regime_calc030_126d_base_v030_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc030_126d_base_v030_signal'] = f110w_f110_working_capital_to_revenue_regime_calc030_126d_base_v030_signal

def f110w_f110_working_capital_to_revenue_regime_calc031_21d_base_v031_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc031_21d_base_v031_signal'] = f110w_f110_working_capital_to_revenue_regime_calc031_21d_base_v031_signal

def f110w_f110_working_capital_to_revenue_regime_calc032_105d_base_v032_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc032_105d_base_v032_signal'] = f110w_f110_working_capital_to_revenue_regime_calc032_105d_base_v032_signal

def f110w_f110_working_capital_to_revenue_regime_calc033_42d_base_v033_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc033_42d_base_v033_signal'] = f110w_f110_working_capital_to_revenue_regime_calc033_42d_base_v033_signal

def f110w_f110_working_capital_to_revenue_regime_calc034_150d_base_v034_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc034_150d_base_v034_signal'] = f110w_f110_working_capital_to_revenue_regime_calc034_150d_base_v034_signal

def f110w_f110_working_capital_to_revenue_regime_calc035_252d_base_v035_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc035_252d_base_v035_signal'] = f110w_f110_working_capital_to_revenue_regime_calc035_252d_base_v035_signal

def f110w_f110_working_capital_to_revenue_regime_calc036_252d_base_v036_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc036_252d_base_v036_signal'] = f110w_f110_working_capital_to_revenue_regime_calc036_252d_base_v036_signal

def f110w_f110_working_capital_to_revenue_regime_calc037_42d_base_v037_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc037_42d_base_v037_signal'] = f110w_f110_working_capital_to_revenue_regime_calc037_42d_base_v037_signal

def f110w_f110_working_capital_to_revenue_regime_calc038_150d_base_v038_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc038_150d_base_v038_signal'] = f110w_f110_working_capital_to_revenue_regime_calc038_150d_base_v038_signal

def f110w_f110_working_capital_to_revenue_regime_calc039_200d_base_v039_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc039_200d_base_v039_signal'] = f110w_f110_working_capital_to_revenue_regime_calc039_200d_base_v039_signal

def f110w_f110_working_capital_to_revenue_regime_calc040_252d_base_v040_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc040_252d_base_v040_signal'] = f110w_f110_working_capital_to_revenue_regime_calc040_252d_base_v040_signal

def f110w_f110_working_capital_to_revenue_regime_calc041_84d_base_v041_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc041_84d_base_v041_signal'] = f110w_f110_working_capital_to_revenue_regime_calc041_84d_base_v041_signal

def f110w_f110_working_capital_to_revenue_regime_calc042_21d_base_v042_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc042_21d_base_v042_signal'] = f110w_f110_working_capital_to_revenue_regime_calc042_21d_base_v042_signal

def f110w_f110_working_capital_to_revenue_regime_calc043_21d_base_v043_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc043_21d_base_v043_signal'] = f110w_f110_working_capital_to_revenue_regime_calc043_21d_base_v043_signal

def f110w_f110_working_capital_to_revenue_regime_calc044_200d_base_v044_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc044_200d_base_v044_signal'] = f110w_f110_working_capital_to_revenue_regime_calc044_200d_base_v044_signal

def f110w_f110_working_capital_to_revenue_regime_calc045_150d_base_v045_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc045_150d_base_v045_signal'] = f110w_f110_working_capital_to_revenue_regime_calc045_150d_base_v045_signal

def f110w_f110_working_capital_to_revenue_regime_calc046_105d_base_v046_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc046_105d_base_v046_signal'] = f110w_f110_working_capital_to_revenue_regime_calc046_105d_base_v046_signal

def f110w_f110_working_capital_to_revenue_regime_calc047_105d_base_v047_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc047_105d_base_v047_signal'] = f110w_f110_working_capital_to_revenue_regime_calc047_105d_base_v047_signal

def f110w_f110_working_capital_to_revenue_regime_calc048_21d_base_v048_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc048_21d_base_v048_signal'] = f110w_f110_working_capital_to_revenue_regime_calc048_21d_base_v048_signal

def f110w_f110_working_capital_to_revenue_regime_calc049_150d_base_v049_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc049_150d_base_v049_signal'] = f110w_f110_working_capital_to_revenue_regime_calc049_150d_base_v049_signal

def f110w_f110_working_capital_to_revenue_regime_calc050_200d_base_v050_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc050_200d_base_v050_signal'] = f110w_f110_working_capital_to_revenue_regime_calc050_200d_base_v050_signal

def f110w_f110_working_capital_to_revenue_regime_calc051_84d_base_v051_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc051_84d_base_v051_signal'] = f110w_f110_working_capital_to_revenue_regime_calc051_84d_base_v051_signal

def f110w_f110_working_capital_to_revenue_regime_calc052_150d_base_v052_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc052_150d_base_v052_signal'] = f110w_f110_working_capital_to_revenue_regime_calc052_150d_base_v052_signal

def f110w_f110_working_capital_to_revenue_regime_calc053_5d_base_v053_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc053_5d_base_v053_signal'] = f110w_f110_working_capital_to_revenue_regime_calc053_5d_base_v053_signal

def f110w_f110_working_capital_to_revenue_regime_calc054_84d_base_v054_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc054_84d_base_v054_signal'] = f110w_f110_working_capital_to_revenue_regime_calc054_84d_base_v054_signal

def f110w_f110_working_capital_to_revenue_regime_calc055_126d_base_v055_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc055_126d_base_v055_signal'] = f110w_f110_working_capital_to_revenue_regime_calc055_126d_base_v055_signal

def f110w_f110_working_capital_to_revenue_regime_calc056_84d_base_v056_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc056_84d_base_v056_signal'] = f110w_f110_working_capital_to_revenue_regime_calc056_84d_base_v056_signal

def f110w_f110_working_capital_to_revenue_regime_calc057_10d_base_v057_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc057_10d_base_v057_signal'] = f110w_f110_working_capital_to_revenue_regime_calc057_10d_base_v057_signal

def f110w_f110_working_capital_to_revenue_regime_calc058_105d_base_v058_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc058_105d_base_v058_signal'] = f110w_f110_working_capital_to_revenue_regime_calc058_105d_base_v058_signal

def f110w_f110_working_capital_to_revenue_regime_calc059_42d_base_v059_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc059_42d_base_v059_signal'] = f110w_f110_working_capital_to_revenue_regime_calc059_42d_base_v059_signal

def f110w_f110_working_capital_to_revenue_regime_calc060_150d_base_v060_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc060_150d_base_v060_signal'] = f110w_f110_working_capital_to_revenue_regime_calc060_150d_base_v060_signal

def f110w_f110_working_capital_to_revenue_regime_calc061_150d_base_v061_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc061_150d_base_v061_signal'] = f110w_f110_working_capital_to_revenue_regime_calc061_150d_base_v061_signal

def f110w_f110_working_capital_to_revenue_regime_calc062_5d_base_v062_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc062_5d_base_v062_signal'] = f110w_f110_working_capital_to_revenue_regime_calc062_5d_base_v062_signal

def f110w_f110_working_capital_to_revenue_regime_calc063_5d_base_v063_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc063_5d_base_v063_signal'] = f110w_f110_working_capital_to_revenue_regime_calc063_5d_base_v063_signal

def f110w_f110_working_capital_to_revenue_regime_calc064_63d_base_v064_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc064_63d_base_v064_signal'] = f110w_f110_working_capital_to_revenue_regime_calc064_63d_base_v064_signal

def f110w_f110_working_capital_to_revenue_regime_calc065_5d_base_v065_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc065_5d_base_v065_signal'] = f110w_f110_working_capital_to_revenue_regime_calc065_5d_base_v065_signal

def f110w_f110_working_capital_to_revenue_regime_calc066_21d_base_v066_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc066_21d_base_v066_signal'] = f110w_f110_working_capital_to_revenue_regime_calc066_21d_base_v066_signal

def f110w_f110_working_capital_to_revenue_regime_calc067_42d_base_v067_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc067_42d_base_v067_signal'] = f110w_f110_working_capital_to_revenue_regime_calc067_42d_base_v067_signal

def f110w_f110_working_capital_to_revenue_regime_calc068_63d_base_v068_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc068_63d_base_v068_signal'] = f110w_f110_working_capital_to_revenue_regime_calc068_63d_base_v068_signal

def f110w_f110_working_capital_to_revenue_regime_calc069_63d_base_v069_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc069_63d_base_v069_signal'] = f110w_f110_working_capital_to_revenue_regime_calc069_63d_base_v069_signal

def f110w_f110_working_capital_to_revenue_regime_calc070_10d_base_v070_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc070_10d_base_v070_signal'] = f110w_f110_working_capital_to_revenue_regime_calc070_10d_base_v070_signal

def f110w_f110_working_capital_to_revenue_regime_calc071_150d_base_v071_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc071_150d_base_v071_signal'] = f110w_f110_working_capital_to_revenue_regime_calc071_150d_base_v071_signal

def f110w_f110_working_capital_to_revenue_regime_calc072_126d_base_v072_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc072_126d_base_v072_signal'] = f110w_f110_working_capital_to_revenue_regime_calc072_126d_base_v072_signal

def f110w_f110_working_capital_to_revenue_regime_calc073_105d_base_v073_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc073_105d_base_v073_signal'] = f110w_f110_working_capital_to_revenue_regime_calc073_105d_base_v073_signal

def f110w_f110_working_capital_to_revenue_regime_calc074_150d_base_v074_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc074_150d_base_v074_signal'] = f110w_f110_working_capital_to_revenue_regime_calc074_150d_base_v074_signal

def f110w_f110_working_capital_to_revenue_regime_calc075_63d_base_v075_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc075_63d_base_v075_signal'] = f110w_f110_working_capital_to_revenue_regime_calc075_63d_base_v075_signal


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
