import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f156g_f156_gross_profit_to_fcf_quality_calc001_126d_base_v001_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).rank(pct=True)
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(63).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc001_126d_base_v001_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc001_126d_base_v001_signal

def f156g_f156_gross_profit_to_fcf_quality_calc002_5d_base_v002_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(126).kurt()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).mean()
    v_009 = v_008.rolling(42).max() / v_008.rolling(42).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc002_5d_base_v002_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc002_5d_base_v002_signal

def f156g_f156_gross_profit_to_fcf_quality_calc003_5d_base_v003_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(252).max()
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(252).max() / v_004.rolling(252).min().replace(0, np.nan)
    v_006 = v_005.rolling(63).max()
    v_007 = (v_006 - v_006.rolling(10).mean()) / v_006.rolling(10).std().replace(0, np.nan)
    v_008 = v_007.rolling(252).mean()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc003_5d_base_v003_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc003_5d_base_v003_signal

def f156g_f156_gross_profit_to_fcf_quality_calc004_126d_base_v004_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(126).kurt()
    v_008 = v_007.rolling(252).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc004_126d_base_v004_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc004_126d_base_v004_signal

def f156g_f156_gross_profit_to_fcf_quality_calc005_21d_base_v005_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(21).rank(pct=True)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(42).min()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc005_21d_base_v005_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc005_21d_base_v005_signal

def f156g_f156_gross_profit_to_fcf_quality_calc006_10d_base_v006_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(10).kurt()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(63).min()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    v_008 = (v_007 - v_007.rolling(5).mean()) / v_007.rolling(5).std().replace(0, np.nan)
    v_009 = v_008.rolling(126).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc006_10d_base_v006_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc006_10d_base_v006_signal

def f156g_f156_gross_profit_to_fcf_quality_calc007_10d_base_v007_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(5).mean()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(10).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc007_10d_base_v007_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc007_10d_base_v007_signal

def f156g_f156_gross_profit_to_fcf_quality_calc008_10d_base_v008_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(5).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc008_10d_base_v008_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc008_10d_base_v008_signal

def f156g_f156_gross_profit_to_fcf_quality_calc009_126d_base_v009_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc009_126d_base_v009_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc009_126d_base_v009_signal

def f156g_f156_gross_profit_to_fcf_quality_calc010_5d_base_v010_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(5).skew()
    v_005 = (v_004 - v_004.rolling(10).mean()) / v_004.rolling(10).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc010_5d_base_v010_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc010_5d_base_v010_signal

def f156g_f156_gross_profit_to_fcf_quality_calc011_126d_base_v011_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(10).var()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc011_126d_base_v011_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc011_126d_base_v011_signal

def f156g_f156_gross_profit_to_fcf_quality_calc012_126d_base_v012_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - revenue)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(63).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc012_126d_base_v012_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc012_126d_base_v012_signal

def f156g_f156_gross_profit_to_fcf_quality_calc013_63d_base_v013_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(126).kurt()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).kurt()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc013_63d_base_v013_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc013_63d_base_v013_signal

def f156g_f156_gross_profit_to_fcf_quality_calc014_5d_base_v014_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).mean()
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).mean()
    v_008 = v_007.rolling(5).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc014_5d_base_v014_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc014_5d_base_v014_signal

def f156g_f156_gross_profit_to_fcf_quality_calc015_63d_base_v015_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(21).max()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(21).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc015_63d_base_v015_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc015_63d_base_v015_signal

def f156g_f156_gross_profit_to_fcf_quality_calc016_42d_base_v016_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + revenue)
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).kurt()
    v_006 = v_005.rolling(10).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc016_42d_base_v016_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc016_42d_base_v016_signal

def f156g_f156_gross_profit_to_fcf_quality_calc017_5d_base_v017_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - free_cash_flow)
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(21).skew()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc017_5d_base_v017_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc017_5d_base_v017_signal

def f156g_f156_gross_profit_to_fcf_quality_calc018_5d_base_v018_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(63).std()
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(126).kurt()
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = v_006.rolling(252).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc018_5d_base_v018_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc018_5d_base_v018_signal

def f156g_f156_gross_profit_to_fcf_quality_calc019_5d_base_v019_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - revenue)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(252).max()
    v_009 = v_008.rolling(63).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc019_5d_base_v019_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc019_5d_base_v019_signal

def f156g_f156_gross_profit_to_fcf_quality_calc020_10d_base_v020_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - gross_profit)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(252).std()
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc020_10d_base_v020_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc020_10d_base_v020_signal

def f156g_f156_gross_profit_to_fcf_quality_calc021_10d_base_v021_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(10).mean()) / v_004.rolling(10).std().replace(0, np.nan)
    v_006 = v_005.rolling(126).skew()
    v_007 = (v_006 - v_006.rolling(42).mean()) / v_006.rolling(42).std().replace(0, np.nan)
    v_008 = v_007.rolling(21).mean()
    v_009 = v_008.rolling(252).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc021_10d_base_v021_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc021_10d_base_v021_signal

def f156g_f156_gross_profit_to_fcf_quality_calc022_63d_base_v022_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(42).mean()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc022_63d_base_v022_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc022_63d_base_v022_signal

def f156g_f156_gross_profit_to_fcf_quality_calc023_63d_base_v023_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(5).std()
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(126).max()
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).std()
    v_008 = v_007.rolling(63).mean()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc023_63d_base_v023_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc023_63d_base_v023_signal

def f156g_f156_gross_profit_to_fcf_quality_calc024_5d_base_v024_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).rank(pct=True)
    v_007 = v_006.rolling(126).std()
    v_008 = v_007.rolling(126).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc024_5d_base_v024_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc024_5d_base_v024_signal

def f156g_f156_gross_profit_to_fcf_quality_calc025_63d_base_v025_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = v_001.rolling(252).max()
    v_003 = v_002.rolling(21).skew()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).std()
    v_006 = v_005.rolling(63).min()
    v_007 = v_006.rolling(42).mean()
    v_008 = v_007.rolling(42).var()
    v_009 = (v_008 - v_008.rolling(63).mean()) / v_008.rolling(63).std().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc025_63d_base_v025_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc025_63d_base_v025_signal

def f156g_f156_gross_profit_to_fcf_quality_calc026_10d_base_v026_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - ncfo)
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(252).kurt()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc026_10d_base_v026_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc026_10d_base_v026_signal

def f156g_f156_gross_profit_to_fcf_quality_calc027_126d_base_v027_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(10).min()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc027_126d_base_v027_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc027_126d_base_v027_signal

def f156g_f156_gross_profit_to_fcf_quality_calc028_126d_base_v028_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(252).rank(pct=True)
    v_006 = v_005.rolling(42).max()
    v_007 = v_006.rolling(63).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc028_126d_base_v028_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc028_126d_base_v028_signal

def f156g_f156_gross_profit_to_fcf_quality_calc029_126d_base_v029_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(42).max()
    v_007 = v_006.rolling(126).rank(pct=True)
    v_008 = v_007.rolling(42).var()
    v_009 = v_008.rolling(252).max() / v_008.rolling(252).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc029_126d_base_v029_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc029_126d_base_v029_signal

def f156g_f156_gross_profit_to_fcf_quality_calc030_63d_base_v030_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).max() / v_004.rolling(21).min().replace(0, np.nan)
    v_006 = v_005.rolling(63).mean()
    v_007 = v_006.rolling(10).kurt()
    v_008 = v_007.rolling(10).rank(pct=True)
    v_009 = v_008.rolling(126).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc030_63d_base_v030_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc030_63d_base_v030_signal

def f156g_f156_gross_profit_to_fcf_quality_calc031_42d_base_v031_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(42).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc031_42d_base_v031_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc031_42d_base_v031_signal

def f156g_f156_gross_profit_to_fcf_quality_calc032_10d_base_v032_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).mean()
    v_003 = v_002.rolling(252).std()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(10).min()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc032_10d_base_v032_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc032_10d_base_v032_signal

def f156g_f156_gross_profit_to_fcf_quality_calc033_42d_base_v033_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(252).rank(pct=True)
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(63).min()
    v_008 = v_007.rolling(42).skew()
    v_009 = v_008.rolling(63).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc033_42d_base_v033_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc033_42d_base_v033_signal

def f156g_f156_gross_profit_to_fcf_quality_calc034_63d_base_v034_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(42).max() / v_002.rolling(42).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(21).var()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(21).std()
    v_009 = v_008.rolling(42).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc034_63d_base_v034_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc034_63d_base_v034_signal

def f156g_f156_gross_profit_to_fcf_quality_calc035_21d_base_v035_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.rolling(10).skew()
    v_006 = (v_005 - v_005.rolling(252).mean()) / v_005.rolling(252).std().replace(0, np.nan)
    v_007 = v_006.rolling(63).skew()
    v_008 = v_007.rolling(10).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc035_21d_base_v035_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc035_21d_base_v035_signal

def f156g_f156_gross_profit_to_fcf_quality_calc036_252d_base_v036_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(21).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc036_252d_base_v036_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc036_252d_base_v036_signal

def f156g_f156_gross_profit_to_fcf_quality_calc037_252d_base_v037_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(42).std()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(126).min()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(252).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc037_252d_base_v037_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc037_252d_base_v037_signal

def f156g_f156_gross_profit_to_fcf_quality_calc038_5d_base_v038_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(5).mean()
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(5).var()
    v_008 = v_007.rolling(21).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc038_5d_base_v038_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc038_5d_base_v038_signal

def f156g_f156_gross_profit_to_fcf_quality_calc039_252d_base_v039_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - ncfo)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(42).var()
    v_007 = v_006.rolling(252).std()
    v_008 = v_007.rolling(21).min()
    v_009 = v_008.rolling(252).mean()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc039_252d_base_v039_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc039_252d_base_v039_signal

def f156g_f156_gross_profit_to_fcf_quality_calc040_252d_base_v040_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).var()
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(42).skew()
    v_007 = v_006.rolling(10).mean()
    v_008 = v_007.rolling(10).var()
    v_009 = v_008.rolling(252).mean()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc040_252d_base_v040_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc040_252d_base_v040_signal

def f156g_f156_gross_profit_to_fcf_quality_calc041_10d_base_v041_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(252).max()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(126).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc041_10d_base_v041_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc041_10d_base_v041_signal

def f156g_f156_gross_profit_to_fcf_quality_calc042_126d_base_v042_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(10).max() / v_001.rolling(10).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).std()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).min()
    v_006 = v_005.rolling(63).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc042_126d_base_v042_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc042_126d_base_v042_signal

def f156g_f156_gross_profit_to_fcf_quality_calc043_42d_base_v043_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(21).mean()) / v_004.rolling(21).std().replace(0, np.nan)
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(252).max()
    v_008 = v_007.rolling(10).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc043_42d_base_v043_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc043_42d_base_v043_signal

def f156g_f156_gross_profit_to_fcf_quality_calc044_21d_base_v044_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(252).kurt()
    v_003 = (v_002 - v_002.rolling(21).mean()) / v_002.rolling(21).std().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(10).max()
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc044_21d_base_v044_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc044_21d_base_v044_signal

def f156g_f156_gross_profit_to_fcf_quality_calc045_21d_base_v045_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + ncfo)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(42).var()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(21).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc045_21d_base_v045_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc045_21d_base_v045_signal

def f156g_f156_gross_profit_to_fcf_quality_calc046_10d_base_v046_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(252).rank(pct=True)
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(10).kurt()
    v_008 = v_007.rolling(63).kurt()
    v_009 = v_008.rolling(63).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc046_10d_base_v046_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc046_10d_base_v046_signal

def f156g_f156_gross_profit_to_fcf_quality_calc047_10d_base_v047_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(252).kurt()
    v_008 = (v_007 - v_007.rolling(126).mean()) / v_007.rolling(126).std().replace(0, np.nan)
    v_009 = (v_008 - v_008.rolling(21).mean()) / v_008.rolling(21).std().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc047_10d_base_v047_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc047_10d_base_v047_signal

def f156g_f156_gross_profit_to_fcf_quality_calc048_252d_base_v048_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - revenue)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(42).min()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(21).mean()) / v_006.rolling(21).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc048_252d_base_v048_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc048_252d_base_v048_signal

def f156g_f156_gross_profit_to_fcf_quality_calc049_21d_base_v049_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).min()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).kurt()
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc049_21d_base_v049_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc049_21d_base_v049_signal

def f156g_f156_gross_profit_to_fcf_quality_calc050_5d_base_v050_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc050_5d_base_v050_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc050_5d_base_v050_signal

def f156g_f156_gross_profit_to_fcf_quality_calc051_5d_base_v051_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(63).min()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc051_5d_base_v051_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc051_5d_base_v051_signal

def f156g_f156_gross_profit_to_fcf_quality_calc052_42d_base_v052_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + ncfo)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = v_005.rolling(126).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc052_42d_base_v052_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc052_42d_base_v052_signal

def f156g_f156_gross_profit_to_fcf_quality_calc053_5d_base_v053_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).mean()
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(21).var()
    v_007 = v_006.rolling(252).std()
    v_008 = v_007.rolling(5).max()
    v_009 = v_008.rolling(5).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc053_5d_base_v053_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc053_5d_base_v053_signal

def f156g_f156_gross_profit_to_fcf_quality_calc054_21d_base_v054_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(5).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc054_21d_base_v054_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc054_21d_base_v054_signal

def f156g_f156_gross_profit_to_fcf_quality_calc055_252d_base_v055_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).var()
    v_007 = v_006.rolling(5).var()
    v_008 = v_007.rolling(126).skew()
    v_009 = v_008.rolling(252).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc055_252d_base_v055_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc055_252d_base_v055_signal

def f156g_f156_gross_profit_to_fcf_quality_calc056_21d_base_v056_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.rolling(42).kurt()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(42).rank(pct=True)
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc056_21d_base_v056_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc056_21d_base_v056_signal

def f156g_f156_gross_profit_to_fcf_quality_calc057_63d_base_v057_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(126).max()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(21).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc057_63d_base_v057_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc057_63d_base_v057_signal

def f156g_f156_gross_profit_to_fcf_quality_calc058_21d_base_v058_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + free_cash_flow)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(42).rank(pct=True)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc058_21d_base_v058_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc058_21d_base_v058_signal

def f156g_f156_gross_profit_to_fcf_quality_calc059_252d_base_v059_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + free_cash_flow)
    v_002 = v_001.rolling(21).var()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(5).std()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(126).var()
    v_009 = v_008.rolling(42).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc059_252d_base_v059_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc059_252d_base_v059_signal

def f156g_f156_gross_profit_to_fcf_quality_calc060_5d_base_v060_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(42).max()
    v_007 = v_006.rolling(126).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc060_5d_base_v060_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc060_5d_base_v060_signal

def f156g_f156_gross_profit_to_fcf_quality_calc061_126d_base_v061_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - revenue)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(252).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc061_126d_base_v061_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc061_126d_base_v061_signal

def f156g_f156_gross_profit_to_fcf_quality_calc062_42d_base_v062_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(5).min()
    v_004 = (v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(42).kurt()
    v_009 = v_008.rolling(126).rank(pct=True)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc062_42d_base_v062_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc062_42d_base_v062_signal

def f156g_f156_gross_profit_to_fcf_quality_calc063_63d_base_v063_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(10).std()
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(63).std()
    v_007 = v_006.rolling(10).rank(pct=True)
    v_008 = v_007.rolling(5).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc063_63d_base_v063_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc063_63d_base_v063_signal

def f156g_f156_gross_profit_to_fcf_quality_calc064_5d_base_v064_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - ncfo)
    v_002 = v_001.rolling(10).min()
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(21).var()
    v_008 = v_007.rolling(10).max()
    v_009 = v_008.rolling(42).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc064_5d_base_v064_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc064_5d_base_v064_signal

def f156g_f156_gross_profit_to_fcf_quality_calc065_42d_base_v065_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + revenue)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(5).var()
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).min()
    v_008 = v_007.rolling(21).min()
    v_009 = v_008.rolling(5).max() / v_008.rolling(5).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc065_42d_base_v065_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc065_42d_base_v065_signal

def f156g_f156_gross_profit_to_fcf_quality_calc066_5d_base_v066_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc066_5d_base_v066_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc066_5d_base_v066_signal

def f156g_f156_gross_profit_to_fcf_quality_calc067_63d_base_v067_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = v_001.rolling(126).kurt()
    v_003 = v_002.rolling(21).skew()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(21).min()
    v_006 = v_005.rolling(5).rank(pct=True)
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc067_63d_base_v067_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc067_63d_base_v067_signal

def f156g_f156_gross_profit_to_fcf_quality_calc068_21d_base_v068_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - gross_profit)
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(126).max() / v_006.rolling(126).min().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc068_21d_base_v068_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc068_21d_base_v068_signal

def f156g_f156_gross_profit_to_fcf_quality_calc069_252d_base_v069_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).std()
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(5).std()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc069_252d_base_v069_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc069_252d_base_v069_signal

def f156g_f156_gross_profit_to_fcf_quality_calc070_126d_base_v070_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(5).mean()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(21).max()
    v_007 = v_006.rolling(10).min()
    v_008 = v_007.rolling(126).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc070_126d_base_v070_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc070_126d_base_v070_signal

def f156g_f156_gross_profit_to_fcf_quality_calc071_63d_base_v071_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).kurt()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(42).rank(pct=True)
    v_008 = v_007.rolling(21).var()
    v_009 = v_008.rolling(42).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc071_63d_base_v071_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc071_63d_base_v071_signal

def f156g_f156_gross_profit_to_fcf_quality_calc072_252d_base_v072_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(42).var()
    v_006 = (v_005 - v_005.rolling(252).mean()) / v_005.rolling(252).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(63).mean()
    v_009 = v_008.rolling(5).mean()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc072_252d_base_v072_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc072_252d_base_v072_signal

def f156g_f156_gross_profit_to_fcf_quality_calc073_21d_base_v073_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - free_cash_flow)
    v_002 = v_001.rolling(5).var()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(10).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc073_21d_base_v073_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc073_21d_base_v073_signal

def f156g_f156_gross_profit_to_fcf_quality_calc074_63d_base_v074_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(10).min()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(252).rank(pct=True)
    v_006 = v_005.rolling(5).min()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc074_63d_base_v074_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc074_63d_base_v074_signal

def f156g_f156_gross_profit_to_fcf_quality_calc075_10d_base_v075_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - gross_profit)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(21).skew()
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).mean()
    v_007 = v_006.rolling(21).rank(pct=True)
    v_008 = v_007.rolling(10).skew()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc075_10d_base_v075_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc075_10d_base_v075_signal


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
