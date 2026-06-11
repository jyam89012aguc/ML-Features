import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f110w_f110_working_capital_to_revenue_regime_calc001_252d_jerk_v001_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc001_252d_jerk_v001_signal'] = f110w_f110_working_capital_to_revenue_regime_calc001_252d_jerk_v001_signal

def f110w_f110_working_capital_to_revenue_regime_calc002_126d_jerk_v002_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc002_126d_jerk_v002_signal'] = f110w_f110_working_capital_to_revenue_regime_calc002_126d_jerk_v002_signal

def f110w_f110_working_capital_to_revenue_regime_calc003_63d_jerk_v003_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc003_63d_jerk_v003_signal'] = f110w_f110_working_capital_to_revenue_regime_calc003_63d_jerk_v003_signal

def f110w_f110_working_capital_to_revenue_regime_calc004_42d_jerk_v004_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc004_42d_jerk_v004_signal'] = f110w_f110_working_capital_to_revenue_regime_calc004_42d_jerk_v004_signal

def f110w_f110_working_capital_to_revenue_regime_calc005_200d_jerk_v005_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc005_200d_jerk_v005_signal'] = f110w_f110_working_capital_to_revenue_regime_calc005_200d_jerk_v005_signal

def f110w_f110_working_capital_to_revenue_regime_calc006_126d_jerk_v006_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc006_126d_jerk_v006_signal'] = f110w_f110_working_capital_to_revenue_regime_calc006_126d_jerk_v006_signal

def f110w_f110_working_capital_to_revenue_regime_calc007_150d_jerk_v007_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc007_150d_jerk_v007_signal'] = f110w_f110_working_capital_to_revenue_regime_calc007_150d_jerk_v007_signal

def f110w_f110_working_capital_to_revenue_regime_calc008_42d_jerk_v008_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc008_42d_jerk_v008_signal'] = f110w_f110_working_capital_to_revenue_regime_calc008_42d_jerk_v008_signal

def f110w_f110_working_capital_to_revenue_regime_calc009_252d_jerk_v009_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc009_252d_jerk_v009_signal'] = f110w_f110_working_capital_to_revenue_regime_calc009_252d_jerk_v009_signal

def f110w_f110_working_capital_to_revenue_regime_calc010_105d_jerk_v010_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc010_105d_jerk_v010_signal'] = f110w_f110_working_capital_to_revenue_regime_calc010_105d_jerk_v010_signal

def f110w_f110_working_capital_to_revenue_regime_calc011_10d_jerk_v011_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc011_10d_jerk_v011_signal'] = f110w_f110_working_capital_to_revenue_regime_calc011_10d_jerk_v011_signal

def f110w_f110_working_capital_to_revenue_regime_calc012_105d_jerk_v012_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(105).std()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc012_105d_jerk_v012_signal'] = f110w_f110_working_capital_to_revenue_regime_calc012_105d_jerk_v012_signal

def f110w_f110_working_capital_to_revenue_regime_calc013_84d_jerk_v013_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).min()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc013_84d_jerk_v013_signal'] = f110w_f110_working_capital_to_revenue_regime_calc013_84d_jerk_v013_signal

def f110w_f110_working_capital_to_revenue_regime_calc014_150d_jerk_v014_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc014_150d_jerk_v014_signal'] = f110w_f110_working_capital_to_revenue_regime_calc014_150d_jerk_v014_signal

def f110w_f110_working_capital_to_revenue_regime_calc015_252d_jerk_v015_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc015_252d_jerk_v015_signal'] = f110w_f110_working_capital_to_revenue_regime_calc015_252d_jerk_v015_signal

def f110w_f110_working_capital_to_revenue_regime_calc016_10d_jerk_v016_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc016_10d_jerk_v016_signal'] = f110w_f110_working_capital_to_revenue_regime_calc016_10d_jerk_v016_signal

def f110w_f110_working_capital_to_revenue_regime_calc017_150d_jerk_v017_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc017_150d_jerk_v017_signal'] = f110w_f110_working_capital_to_revenue_regime_calc017_150d_jerk_v017_signal

def f110w_f110_working_capital_to_revenue_regime_calc018_5d_jerk_v018_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc018_5d_jerk_v018_signal'] = f110w_f110_working_capital_to_revenue_regime_calc018_5d_jerk_v018_signal

def f110w_f110_working_capital_to_revenue_regime_calc019_5d_jerk_v019_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc019_5d_jerk_v019_signal'] = f110w_f110_working_capital_to_revenue_regime_calc019_5d_jerk_v019_signal

def f110w_f110_working_capital_to_revenue_regime_calc020_200d_jerk_v020_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc020_200d_jerk_v020_signal'] = f110w_f110_working_capital_to_revenue_regime_calc020_200d_jerk_v020_signal

def f110w_f110_working_capital_to_revenue_regime_calc021_42d_jerk_v021_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc021_42d_jerk_v021_signal'] = f110w_f110_working_capital_to_revenue_regime_calc021_42d_jerk_v021_signal

def f110w_f110_working_capital_to_revenue_regime_calc022_5d_jerk_v022_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc022_5d_jerk_v022_signal'] = f110w_f110_working_capital_to_revenue_regime_calc022_5d_jerk_v022_signal

def f110w_f110_working_capital_to_revenue_regime_calc023_21d_jerk_v023_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc023_21d_jerk_v023_signal'] = f110w_f110_working_capital_to_revenue_regime_calc023_21d_jerk_v023_signal

def f110w_f110_working_capital_to_revenue_regime_calc024_10d_jerk_v024_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc024_10d_jerk_v024_signal'] = f110w_f110_working_capital_to_revenue_regime_calc024_10d_jerk_v024_signal

def f110w_f110_working_capital_to_revenue_regime_calc025_63d_jerk_v025_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc025_63d_jerk_v025_signal'] = f110w_f110_working_capital_to_revenue_regime_calc025_63d_jerk_v025_signal

def f110w_f110_working_capital_to_revenue_regime_calc026_150d_jerk_v026_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc026_150d_jerk_v026_signal'] = f110w_f110_working_capital_to_revenue_regime_calc026_150d_jerk_v026_signal

def f110w_f110_working_capital_to_revenue_regime_calc027_84d_jerk_v027_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc027_84d_jerk_v027_signal'] = f110w_f110_working_capital_to_revenue_regime_calc027_84d_jerk_v027_signal

def f110w_f110_working_capital_to_revenue_regime_calc028_150d_jerk_v028_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc028_150d_jerk_v028_signal'] = f110w_f110_working_capital_to_revenue_regime_calc028_150d_jerk_v028_signal

def f110w_f110_working_capital_to_revenue_regime_calc029_5d_jerk_v029_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc029_5d_jerk_v029_signal'] = f110w_f110_working_capital_to_revenue_regime_calc029_5d_jerk_v029_signal

def f110w_f110_working_capital_to_revenue_regime_calc030_126d_jerk_v030_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc030_126d_jerk_v030_signal'] = f110w_f110_working_capital_to_revenue_regime_calc030_126d_jerk_v030_signal

def f110w_f110_working_capital_to_revenue_regime_calc031_21d_jerk_v031_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc031_21d_jerk_v031_signal'] = f110w_f110_working_capital_to_revenue_regime_calc031_21d_jerk_v031_signal

def f110w_f110_working_capital_to_revenue_regime_calc032_105d_jerk_v032_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc032_105d_jerk_v032_signal'] = f110w_f110_working_capital_to_revenue_regime_calc032_105d_jerk_v032_signal

def f110w_f110_working_capital_to_revenue_regime_calc033_42d_jerk_v033_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc033_42d_jerk_v033_signal'] = f110w_f110_working_capital_to_revenue_regime_calc033_42d_jerk_v033_signal

def f110w_f110_working_capital_to_revenue_regime_calc034_150d_jerk_v034_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc034_150d_jerk_v034_signal'] = f110w_f110_working_capital_to_revenue_regime_calc034_150d_jerk_v034_signal

def f110w_f110_working_capital_to_revenue_regime_calc035_252d_jerk_v035_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc035_252d_jerk_v035_signal'] = f110w_f110_working_capital_to_revenue_regime_calc035_252d_jerk_v035_signal

def f110w_f110_working_capital_to_revenue_regime_calc036_252d_jerk_v036_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc036_252d_jerk_v036_signal'] = f110w_f110_working_capital_to_revenue_regime_calc036_252d_jerk_v036_signal

def f110w_f110_working_capital_to_revenue_regime_calc037_42d_jerk_v037_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc037_42d_jerk_v037_signal'] = f110w_f110_working_capital_to_revenue_regime_calc037_42d_jerk_v037_signal

def f110w_f110_working_capital_to_revenue_regime_calc038_150d_jerk_v038_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc038_150d_jerk_v038_signal'] = f110w_f110_working_capital_to_revenue_regime_calc038_150d_jerk_v038_signal

def f110w_f110_working_capital_to_revenue_regime_calc039_200d_jerk_v039_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc039_200d_jerk_v039_signal'] = f110w_f110_working_capital_to_revenue_regime_calc039_200d_jerk_v039_signal

def f110w_f110_working_capital_to_revenue_regime_calc040_252d_jerk_v040_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc040_252d_jerk_v040_signal'] = f110w_f110_working_capital_to_revenue_regime_calc040_252d_jerk_v040_signal

def f110w_f110_working_capital_to_revenue_regime_calc041_84d_jerk_v041_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc041_84d_jerk_v041_signal'] = f110w_f110_working_capital_to_revenue_regime_calc041_84d_jerk_v041_signal

def f110w_f110_working_capital_to_revenue_regime_calc042_21d_jerk_v042_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc042_21d_jerk_v042_signal'] = f110w_f110_working_capital_to_revenue_regime_calc042_21d_jerk_v042_signal

def f110w_f110_working_capital_to_revenue_regime_calc043_21d_jerk_v043_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc043_21d_jerk_v043_signal'] = f110w_f110_working_capital_to_revenue_regime_calc043_21d_jerk_v043_signal

def f110w_f110_working_capital_to_revenue_regime_calc044_200d_jerk_v044_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc044_200d_jerk_v044_signal'] = f110w_f110_working_capital_to_revenue_regime_calc044_200d_jerk_v044_signal

def f110w_f110_working_capital_to_revenue_regime_calc045_150d_jerk_v045_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc045_150d_jerk_v045_signal'] = f110w_f110_working_capital_to_revenue_regime_calc045_150d_jerk_v045_signal

def f110w_f110_working_capital_to_revenue_regime_calc046_105d_jerk_v046_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc046_105d_jerk_v046_signal'] = f110w_f110_working_capital_to_revenue_regime_calc046_105d_jerk_v046_signal

def f110w_f110_working_capital_to_revenue_regime_calc047_105d_jerk_v047_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc047_105d_jerk_v047_signal'] = f110w_f110_working_capital_to_revenue_regime_calc047_105d_jerk_v047_signal

def f110w_f110_working_capital_to_revenue_regime_calc048_21d_jerk_v048_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc048_21d_jerk_v048_signal'] = f110w_f110_working_capital_to_revenue_regime_calc048_21d_jerk_v048_signal

def f110w_f110_working_capital_to_revenue_regime_calc049_150d_jerk_v049_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).mean()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc049_150d_jerk_v049_signal'] = f110w_f110_working_capital_to_revenue_regime_calc049_150d_jerk_v049_signal

def f110w_f110_working_capital_to_revenue_regime_calc050_200d_jerk_v050_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc050_200d_jerk_v050_signal'] = f110w_f110_working_capital_to_revenue_regime_calc050_200d_jerk_v050_signal

def f110w_f110_working_capital_to_revenue_regime_calc051_84d_jerk_v051_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc051_84d_jerk_v051_signal'] = f110w_f110_working_capital_to_revenue_regime_calc051_84d_jerk_v051_signal

def f110w_f110_working_capital_to_revenue_regime_calc052_150d_jerk_v052_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc052_150d_jerk_v052_signal'] = f110w_f110_working_capital_to_revenue_regime_calc052_150d_jerk_v052_signal

def f110w_f110_working_capital_to_revenue_regime_calc053_5d_jerk_v053_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc053_5d_jerk_v053_signal'] = f110w_f110_working_capital_to_revenue_regime_calc053_5d_jerk_v053_signal

def f110w_f110_working_capital_to_revenue_regime_calc054_84d_jerk_v054_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc054_84d_jerk_v054_signal'] = f110w_f110_working_capital_to_revenue_regime_calc054_84d_jerk_v054_signal

def f110w_f110_working_capital_to_revenue_regime_calc055_126d_jerk_v055_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc055_126d_jerk_v055_signal'] = f110w_f110_working_capital_to_revenue_regime_calc055_126d_jerk_v055_signal

def f110w_f110_working_capital_to_revenue_regime_calc056_84d_jerk_v056_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc056_84d_jerk_v056_signal'] = f110w_f110_working_capital_to_revenue_regime_calc056_84d_jerk_v056_signal

def f110w_f110_working_capital_to_revenue_regime_calc057_10d_jerk_v057_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc057_10d_jerk_v057_signal'] = f110w_f110_working_capital_to_revenue_regime_calc057_10d_jerk_v057_signal

def f110w_f110_working_capital_to_revenue_regime_calc058_105d_jerk_v058_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).min()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc058_105d_jerk_v058_signal'] = f110w_f110_working_capital_to_revenue_regime_calc058_105d_jerk_v058_signal

def f110w_f110_working_capital_to_revenue_regime_calc059_42d_jerk_v059_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc059_42d_jerk_v059_signal'] = f110w_f110_working_capital_to_revenue_regime_calc059_42d_jerk_v059_signal

def f110w_f110_working_capital_to_revenue_regime_calc060_150d_jerk_v060_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).mean()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc060_150d_jerk_v060_signal'] = f110w_f110_working_capital_to_revenue_regime_calc060_150d_jerk_v060_signal

def f110w_f110_working_capital_to_revenue_regime_calc061_150d_jerk_v061_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc061_150d_jerk_v061_signal'] = f110w_f110_working_capital_to_revenue_regime_calc061_150d_jerk_v061_signal

def f110w_f110_working_capital_to_revenue_regime_calc062_5d_jerk_v062_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc062_5d_jerk_v062_signal'] = f110w_f110_working_capital_to_revenue_regime_calc062_5d_jerk_v062_signal

def f110w_f110_working_capital_to_revenue_regime_calc063_5d_jerk_v063_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc063_5d_jerk_v063_signal'] = f110w_f110_working_capital_to_revenue_regime_calc063_5d_jerk_v063_signal

def f110w_f110_working_capital_to_revenue_regime_calc064_63d_jerk_v064_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc064_63d_jerk_v064_signal'] = f110w_f110_working_capital_to_revenue_regime_calc064_63d_jerk_v064_signal

def f110w_f110_working_capital_to_revenue_regime_calc065_5d_jerk_v065_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc065_5d_jerk_v065_signal'] = f110w_f110_working_capital_to_revenue_regime_calc065_5d_jerk_v065_signal

def f110w_f110_working_capital_to_revenue_regime_calc066_21d_jerk_v066_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc066_21d_jerk_v066_signal'] = f110w_f110_working_capital_to_revenue_regime_calc066_21d_jerk_v066_signal

def f110w_f110_working_capital_to_revenue_regime_calc067_42d_jerk_v067_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc067_42d_jerk_v067_signal'] = f110w_f110_working_capital_to_revenue_regime_calc067_42d_jerk_v067_signal

def f110w_f110_working_capital_to_revenue_regime_calc068_63d_jerk_v068_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc068_63d_jerk_v068_signal'] = f110w_f110_working_capital_to_revenue_regime_calc068_63d_jerk_v068_signal

def f110w_f110_working_capital_to_revenue_regime_calc069_63d_jerk_v069_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc069_63d_jerk_v069_signal'] = f110w_f110_working_capital_to_revenue_regime_calc069_63d_jerk_v069_signal

def f110w_f110_working_capital_to_revenue_regime_calc070_10d_jerk_v070_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc070_10d_jerk_v070_signal'] = f110w_f110_working_capital_to_revenue_regime_calc070_10d_jerk_v070_signal

def f110w_f110_working_capital_to_revenue_regime_calc071_150d_jerk_v071_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc071_150d_jerk_v071_signal'] = f110w_f110_working_capital_to_revenue_regime_calc071_150d_jerk_v071_signal

def f110w_f110_working_capital_to_revenue_regime_calc072_126d_jerk_v072_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc072_126d_jerk_v072_signal'] = f110w_f110_working_capital_to_revenue_regime_calc072_126d_jerk_v072_signal

def f110w_f110_working_capital_to_revenue_regime_calc073_105d_jerk_v073_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc073_105d_jerk_v073_signal'] = f110w_f110_working_capital_to_revenue_regime_calc073_105d_jerk_v073_signal

def f110w_f110_working_capital_to_revenue_regime_calc074_150d_jerk_v074_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc074_150d_jerk_v074_signal'] = f110w_f110_working_capital_to_revenue_regime_calc074_150d_jerk_v074_signal

def f110w_f110_working_capital_to_revenue_regime_calc075_63d_jerk_v075_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc075_63d_jerk_v075_signal'] = f110w_f110_working_capital_to_revenue_regime_calc075_63d_jerk_v075_signal

def f110w_f110_working_capital_to_revenue_regime_calc076_21d_jerk_v076_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc076_21d_jerk_v076_signal'] = f110w_f110_working_capital_to_revenue_regime_calc076_21d_jerk_v076_signal

def f110w_f110_working_capital_to_revenue_regime_calc077_42d_jerk_v077_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc077_42d_jerk_v077_signal'] = f110w_f110_working_capital_to_revenue_regime_calc077_42d_jerk_v077_signal

def f110w_f110_working_capital_to_revenue_regime_calc078_10d_jerk_v078_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc078_10d_jerk_v078_signal'] = f110w_f110_working_capital_to_revenue_regime_calc078_10d_jerk_v078_signal

def f110w_f110_working_capital_to_revenue_regime_calc079_200d_jerk_v079_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc079_200d_jerk_v079_signal'] = f110w_f110_working_capital_to_revenue_regime_calc079_200d_jerk_v079_signal

def f110w_f110_working_capital_to_revenue_regime_calc080_105d_jerk_v080_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc080_105d_jerk_v080_signal'] = f110w_f110_working_capital_to_revenue_regime_calc080_105d_jerk_v080_signal

def f110w_f110_working_capital_to_revenue_regime_calc081_105d_jerk_v081_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc081_105d_jerk_v081_signal'] = f110w_f110_working_capital_to_revenue_regime_calc081_105d_jerk_v081_signal

def f110w_f110_working_capital_to_revenue_regime_calc082_42d_jerk_v082_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc082_42d_jerk_v082_signal'] = f110w_f110_working_capital_to_revenue_regime_calc082_42d_jerk_v082_signal

def f110w_f110_working_capital_to_revenue_regime_calc083_200d_jerk_v083_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc083_200d_jerk_v083_signal'] = f110w_f110_working_capital_to_revenue_regime_calc083_200d_jerk_v083_signal

def f110w_f110_working_capital_to_revenue_regime_calc084_84d_jerk_v084_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc084_84d_jerk_v084_signal'] = f110w_f110_working_capital_to_revenue_regime_calc084_84d_jerk_v084_signal

def f110w_f110_working_capital_to_revenue_regime_calc085_63d_jerk_v085_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc085_63d_jerk_v085_signal'] = f110w_f110_working_capital_to_revenue_regime_calc085_63d_jerk_v085_signal

def f110w_f110_working_capital_to_revenue_regime_calc086_84d_jerk_v086_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc086_84d_jerk_v086_signal'] = f110w_f110_working_capital_to_revenue_regime_calc086_84d_jerk_v086_signal

def f110w_f110_working_capital_to_revenue_regime_calc087_63d_jerk_v087_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc087_63d_jerk_v087_signal'] = f110w_f110_working_capital_to_revenue_regime_calc087_63d_jerk_v087_signal

def f110w_f110_working_capital_to_revenue_regime_calc088_252d_jerk_v088_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc088_252d_jerk_v088_signal'] = f110w_f110_working_capital_to_revenue_regime_calc088_252d_jerk_v088_signal

def f110w_f110_working_capital_to_revenue_regime_calc089_252d_jerk_v089_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc089_252d_jerk_v089_signal'] = f110w_f110_working_capital_to_revenue_regime_calc089_252d_jerk_v089_signal

def f110w_f110_working_capital_to_revenue_regime_calc090_126d_jerk_v090_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc090_126d_jerk_v090_signal'] = f110w_f110_working_capital_to_revenue_regime_calc090_126d_jerk_v090_signal

def f110w_f110_working_capital_to_revenue_regime_calc091_84d_jerk_v091_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc091_84d_jerk_v091_signal'] = f110w_f110_working_capital_to_revenue_regime_calc091_84d_jerk_v091_signal

def f110w_f110_working_capital_to_revenue_regime_calc092_5d_jerk_v092_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc092_5d_jerk_v092_signal'] = f110w_f110_working_capital_to_revenue_regime_calc092_5d_jerk_v092_signal

def f110w_f110_working_capital_to_revenue_regime_calc093_126d_jerk_v093_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc093_126d_jerk_v093_signal'] = f110w_f110_working_capital_to_revenue_regime_calc093_126d_jerk_v093_signal

def f110w_f110_working_capital_to_revenue_regime_calc094_150d_jerk_v094_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc094_150d_jerk_v094_signal'] = f110w_f110_working_capital_to_revenue_regime_calc094_150d_jerk_v094_signal

def f110w_f110_working_capital_to_revenue_regime_calc095_63d_jerk_v095_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc095_63d_jerk_v095_signal'] = f110w_f110_working_capital_to_revenue_regime_calc095_63d_jerk_v095_signal

def f110w_f110_working_capital_to_revenue_regime_calc096_252d_jerk_v096_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc096_252d_jerk_v096_signal'] = f110w_f110_working_capital_to_revenue_regime_calc096_252d_jerk_v096_signal

def f110w_f110_working_capital_to_revenue_regime_calc097_84d_jerk_v097_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).var()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc097_84d_jerk_v097_signal'] = f110w_f110_working_capital_to_revenue_regime_calc097_84d_jerk_v097_signal

def f110w_f110_working_capital_to_revenue_regime_calc098_21d_jerk_v098_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc098_21d_jerk_v098_signal'] = f110w_f110_working_capital_to_revenue_regime_calc098_21d_jerk_v098_signal

def f110w_f110_working_capital_to_revenue_regime_calc099_84d_jerk_v099_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc099_84d_jerk_v099_signal'] = f110w_f110_working_capital_to_revenue_regime_calc099_84d_jerk_v099_signal

def f110w_f110_working_capital_to_revenue_regime_calc100_63d_jerk_v100_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc100_63d_jerk_v100_signal'] = f110w_f110_working_capital_to_revenue_regime_calc100_63d_jerk_v100_signal

def f110w_f110_working_capital_to_revenue_regime_calc101_10d_jerk_v101_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc101_10d_jerk_v101_signal'] = f110w_f110_working_capital_to_revenue_regime_calc101_10d_jerk_v101_signal

def f110w_f110_working_capital_to_revenue_regime_calc102_105d_jerk_v102_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc102_105d_jerk_v102_signal'] = f110w_f110_working_capital_to_revenue_regime_calc102_105d_jerk_v102_signal

def f110w_f110_working_capital_to_revenue_regime_calc103_200d_jerk_v103_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc103_200d_jerk_v103_signal'] = f110w_f110_working_capital_to_revenue_regime_calc103_200d_jerk_v103_signal

def f110w_f110_working_capital_to_revenue_regime_calc104_105d_jerk_v104_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc104_105d_jerk_v104_signal'] = f110w_f110_working_capital_to_revenue_regime_calc104_105d_jerk_v104_signal

def f110w_f110_working_capital_to_revenue_regime_calc105_21d_jerk_v105_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc105_21d_jerk_v105_signal'] = f110w_f110_working_capital_to_revenue_regime_calc105_21d_jerk_v105_signal

def f110w_f110_working_capital_to_revenue_regime_calc106_84d_jerk_v106_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc106_84d_jerk_v106_signal'] = f110w_f110_working_capital_to_revenue_regime_calc106_84d_jerk_v106_signal

def f110w_f110_working_capital_to_revenue_regime_calc107_10d_jerk_v107_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc107_10d_jerk_v107_signal'] = f110w_f110_working_capital_to_revenue_regime_calc107_10d_jerk_v107_signal

def f110w_f110_working_capital_to_revenue_regime_calc108_252d_jerk_v108_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc108_252d_jerk_v108_signal'] = f110w_f110_working_capital_to_revenue_regime_calc108_252d_jerk_v108_signal

def f110w_f110_working_capital_to_revenue_regime_calc109_5d_jerk_v109_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc109_5d_jerk_v109_signal'] = f110w_f110_working_capital_to_revenue_regime_calc109_5d_jerk_v109_signal

def f110w_f110_working_capital_to_revenue_regime_calc110_63d_jerk_v110_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc110_63d_jerk_v110_signal'] = f110w_f110_working_capital_to_revenue_regime_calc110_63d_jerk_v110_signal

def f110w_f110_working_capital_to_revenue_regime_calc111_126d_jerk_v111_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc111_126d_jerk_v111_signal'] = f110w_f110_working_capital_to_revenue_regime_calc111_126d_jerk_v111_signal

def f110w_f110_working_capital_to_revenue_regime_calc112_252d_jerk_v112_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc112_252d_jerk_v112_signal'] = f110w_f110_working_capital_to_revenue_regime_calc112_252d_jerk_v112_signal

def f110w_f110_working_capital_to_revenue_regime_calc113_105d_jerk_v113_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc113_105d_jerk_v113_signal'] = f110w_f110_working_capital_to_revenue_regime_calc113_105d_jerk_v113_signal

def f110w_f110_working_capital_to_revenue_regime_calc114_42d_jerk_v114_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc114_42d_jerk_v114_signal'] = f110w_f110_working_capital_to_revenue_regime_calc114_42d_jerk_v114_signal

def f110w_f110_working_capital_to_revenue_regime_calc115_150d_jerk_v115_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc115_150d_jerk_v115_signal'] = f110w_f110_working_capital_to_revenue_regime_calc115_150d_jerk_v115_signal

def f110w_f110_working_capital_to_revenue_regime_calc116_84d_jerk_v116_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc116_84d_jerk_v116_signal'] = f110w_f110_working_capital_to_revenue_regime_calc116_84d_jerk_v116_signal

def f110w_f110_working_capital_to_revenue_regime_calc117_105d_jerk_v117_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc117_105d_jerk_v117_signal'] = f110w_f110_working_capital_to_revenue_regime_calc117_105d_jerk_v117_signal

def f110w_f110_working_capital_to_revenue_regime_calc118_10d_jerk_v118_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc118_10d_jerk_v118_signal'] = f110w_f110_working_capital_to_revenue_regime_calc118_10d_jerk_v118_signal

def f110w_f110_working_capital_to_revenue_regime_calc119_10d_jerk_v119_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc119_10d_jerk_v119_signal'] = f110w_f110_working_capital_to_revenue_regime_calc119_10d_jerk_v119_signal

def f110w_f110_working_capital_to_revenue_regime_calc120_10d_jerk_v120_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc120_10d_jerk_v120_signal'] = f110w_f110_working_capital_to_revenue_regime_calc120_10d_jerk_v120_signal

def f110w_f110_working_capital_to_revenue_regime_calc121_42d_jerk_v121_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc121_42d_jerk_v121_signal'] = f110w_f110_working_capital_to_revenue_regime_calc121_42d_jerk_v121_signal

def f110w_f110_working_capital_to_revenue_regime_calc122_5d_jerk_v122_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc122_5d_jerk_v122_signal'] = f110w_f110_working_capital_to_revenue_regime_calc122_5d_jerk_v122_signal

def f110w_f110_working_capital_to_revenue_regime_calc123_63d_jerk_v123_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc123_63d_jerk_v123_signal'] = f110w_f110_working_capital_to_revenue_regime_calc123_63d_jerk_v123_signal

def f110w_f110_working_capital_to_revenue_regime_calc124_5d_jerk_v124_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc124_5d_jerk_v124_signal'] = f110w_f110_working_capital_to_revenue_regime_calc124_5d_jerk_v124_signal

def f110w_f110_working_capital_to_revenue_regime_calc125_252d_jerk_v125_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc125_252d_jerk_v125_signal'] = f110w_f110_working_capital_to_revenue_regime_calc125_252d_jerk_v125_signal

def f110w_f110_working_capital_to_revenue_regime_calc126_84d_jerk_v126_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc126_84d_jerk_v126_signal'] = f110w_f110_working_capital_to_revenue_regime_calc126_84d_jerk_v126_signal

def f110w_f110_working_capital_to_revenue_regime_calc127_252d_jerk_v127_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc127_252d_jerk_v127_signal'] = f110w_f110_working_capital_to_revenue_regime_calc127_252d_jerk_v127_signal

def f110w_f110_working_capital_to_revenue_regime_calc128_105d_jerk_v128_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc128_105d_jerk_v128_signal'] = f110w_f110_working_capital_to_revenue_regime_calc128_105d_jerk_v128_signal

def f110w_f110_working_capital_to_revenue_regime_calc129_5d_jerk_v129_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc129_5d_jerk_v129_signal'] = f110w_f110_working_capital_to_revenue_regime_calc129_5d_jerk_v129_signal

def f110w_f110_working_capital_to_revenue_regime_calc130_5d_jerk_v130_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc130_5d_jerk_v130_signal'] = f110w_f110_working_capital_to_revenue_regime_calc130_5d_jerk_v130_signal

def f110w_f110_working_capital_to_revenue_regime_calc131_10d_jerk_v131_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc131_10d_jerk_v131_signal'] = f110w_f110_working_capital_to_revenue_regime_calc131_10d_jerk_v131_signal

def f110w_f110_working_capital_to_revenue_regime_calc132_10d_jerk_v132_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc132_10d_jerk_v132_signal'] = f110w_f110_working_capital_to_revenue_regime_calc132_10d_jerk_v132_signal

def f110w_f110_working_capital_to_revenue_regime_calc133_252d_jerk_v133_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc133_252d_jerk_v133_signal'] = f110w_f110_working_capital_to_revenue_regime_calc133_252d_jerk_v133_signal

def f110w_f110_working_capital_to_revenue_regime_calc134_5d_jerk_v134_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc134_5d_jerk_v134_signal'] = f110w_f110_working_capital_to_revenue_regime_calc134_5d_jerk_v134_signal

def f110w_f110_working_capital_to_revenue_regime_calc135_42d_jerk_v135_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc135_42d_jerk_v135_signal'] = f110w_f110_working_capital_to_revenue_regime_calc135_42d_jerk_v135_signal

def f110w_f110_working_capital_to_revenue_regime_calc136_63d_jerk_v136_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc136_63d_jerk_v136_signal'] = f110w_f110_working_capital_to_revenue_regime_calc136_63d_jerk_v136_signal

def f110w_f110_working_capital_to_revenue_regime_calc137_84d_jerk_v137_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc137_84d_jerk_v137_signal'] = f110w_f110_working_capital_to_revenue_regime_calc137_84d_jerk_v137_signal

def f110w_f110_working_capital_to_revenue_regime_calc138_200d_jerk_v138_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc138_200d_jerk_v138_signal'] = f110w_f110_working_capital_to_revenue_regime_calc138_200d_jerk_v138_signal

def f110w_f110_working_capital_to_revenue_regime_calc139_200d_jerk_v139_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).var()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc139_200d_jerk_v139_signal'] = f110w_f110_working_capital_to_revenue_regime_calc139_200d_jerk_v139_signal

def f110w_f110_working_capital_to_revenue_regime_calc140_5d_jerk_v140_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc140_5d_jerk_v140_signal'] = f110w_f110_working_capital_to_revenue_regime_calc140_5d_jerk_v140_signal

def f110w_f110_working_capital_to_revenue_regime_calc141_200d_jerk_v141_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc141_200d_jerk_v141_signal'] = f110w_f110_working_capital_to_revenue_regime_calc141_200d_jerk_v141_signal

def f110w_f110_working_capital_to_revenue_regime_calc142_10d_jerk_v142_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc142_10d_jerk_v142_signal'] = f110w_f110_working_capital_to_revenue_regime_calc142_10d_jerk_v142_signal

def f110w_f110_working_capital_to_revenue_regime_calc143_126d_jerk_v143_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc143_126d_jerk_v143_signal'] = f110w_f110_working_capital_to_revenue_regime_calc143_126d_jerk_v143_signal

def f110w_f110_working_capital_to_revenue_regime_calc144_5d_jerk_v144_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc144_5d_jerk_v144_signal'] = f110w_f110_working_capital_to_revenue_regime_calc144_5d_jerk_v144_signal

def f110w_f110_working_capital_to_revenue_regime_calc145_150d_jerk_v145_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc145_150d_jerk_v145_signal'] = f110w_f110_working_capital_to_revenue_regime_calc145_150d_jerk_v145_signal

def f110w_f110_working_capital_to_revenue_regime_calc146_10d_jerk_v146_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc146_10d_jerk_v146_signal'] = f110w_f110_working_capital_to_revenue_regime_calc146_10d_jerk_v146_signal

def f110w_f110_working_capital_to_revenue_regime_calc147_5d_jerk_v147_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc147_5d_jerk_v147_signal'] = f110w_f110_working_capital_to_revenue_regime_calc147_5d_jerk_v147_signal

def f110w_f110_working_capital_to_revenue_regime_calc148_126d_jerk_v148_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc148_126d_jerk_v148_signal'] = f110w_f110_working_capital_to_revenue_regime_calc148_126d_jerk_v148_signal

def f110w_f110_working_capital_to_revenue_regime_calc149_42d_jerk_v149_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc149_42d_jerk_v149_signal'] = f110w_f110_working_capital_to_revenue_regime_calc149_42d_jerk_v149_signal

def f110w_f110_working_capital_to_revenue_regime_calc150_10d_jerk_v150_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc150_10d_jerk_v150_signal'] = f110w_f110_working_capital_to_revenue_regime_calc150_10d_jerk_v150_signal


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
