import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f156g_f156_gross_profit_to_fcf_quality_calc001_126d_slope_v001_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(10).std()
    v_007 = v_006.rolling(10).max() / v_006.rolling(10).min().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc001_126d_slope_v001_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc001_126d_slope_v001_signal

def f156g_f156_gross_profit_to_fcf_quality_calc002_5d_slope_v002_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(126).max()
    v_003 = (v_002 - v_002.rolling(5).mean()) / v_002.rolling(5).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(252).skew()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc002_5d_slope_v002_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc002_5d_slope_v002_signal

def f156g_f156_gross_profit_to_fcf_quality_calc003_5d_slope_v003_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(10).skew()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(10).var()
    v_008 = v_007.rolling(126).min()
    v_009 = (v_008 - v_008.rolling(42).mean()) / v_008.rolling(42).std().replace(0, np.nan)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc003_5d_slope_v003_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc003_5d_slope_v003_signal

def f156g_f156_gross_profit_to_fcf_quality_calc004_126d_slope_v004_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(10).mean()
    v_008 = v_007.rolling(21).mean()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc004_126d_slope_v004_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc004_126d_slope_v004_signal

def f156g_f156_gross_profit_to_fcf_quality_calc005_21d_slope_v005_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(10).rank(pct=True)
    v_007 = v_006.rolling(10).mean()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc005_21d_slope_v005_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc005_21d_slope_v005_signal

def f156g_f156_gross_profit_to_fcf_quality_calc006_10d_slope_v006_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + revenue)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(126).rank(pct=True)
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(63).rank(pct=True)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc006_10d_slope_v006_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc006_10d_slope_v006_signal

def f156g_f156_gross_profit_to_fcf_quality_calc007_10d_slope_v007_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(42).skew()
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).rank(pct=True)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc007_10d_slope_v007_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc007_10d_slope_v007_signal

def f156g_f156_gross_profit_to_fcf_quality_calc008_10d_slope_v008_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    v_009 = v_008.rolling(252).max()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc008_10d_slope_v008_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc008_10d_slope_v008_signal

def f156g_f156_gross_profit_to_fcf_quality_calc009_126d_slope_v009_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(10).max()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.rolling(252).max() / v_004.rolling(252).min().replace(0, np.nan)
    v_006 = v_005.rolling(21).mean()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc009_126d_slope_v009_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc009_126d_slope_v009_signal

def f156g_f156_gross_profit_to_fcf_quality_calc010_5d_slope_v010_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).kurt()
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(63).std()
    v_007 = v_006.rolling(5).var()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc010_5d_slope_v010_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc010_5d_slope_v010_signal

def f156g_f156_gross_profit_to_fcf_quality_calc011_126d_slope_v011_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.rolling(63).kurt()
    v_006 = v_005.rolling(10).skew()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc011_126d_slope_v011_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc011_126d_slope_v011_signal

def f156g_f156_gross_profit_to_fcf_quality_calc012_126d_slope_v012_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(5).mean()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc012_126d_slope_v012_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc012_126d_slope_v012_signal

def f156g_f156_gross_profit_to_fcf_quality_calc013_63d_slope_v013_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = v_001.rolling(10).min()
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(252).rank(pct=True)
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc013_63d_slope_v013_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc013_63d_slope_v013_signal

def f156g_f156_gross_profit_to_fcf_quality_calc014_5d_slope_v014_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + ncfo)
    v_002 = v_001.rolling(42).kurt()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(63).min()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc014_5d_slope_v014_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc014_5d_slope_v014_signal

def f156g_f156_gross_profit_to_fcf_quality_calc015_63d_slope_v015_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + gross_profit)
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(5).std()
    v_008 = v_007.rolling(21).min()
    v_009 = (v_008 - v_008.rolling(126).mean()) / v_008.rolling(126).std().replace(0, np.nan)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc015_63d_slope_v015_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc015_63d_slope_v015_signal

def f156g_f156_gross_profit_to_fcf_quality_calc016_42d_slope_v016_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(5).kurt()
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).mean()
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    v_009 = v_008.rolling(5).rank(pct=True)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc016_42d_slope_v016_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc016_42d_slope_v016_signal

def f156g_f156_gross_profit_to_fcf_quality_calc017_5d_slope_v017_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(21).kurt()
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(5).std()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc017_5d_slope_v017_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc017_5d_slope_v017_signal

def f156g_f156_gross_profit_to_fcf_quality_calc018_5d_slope_v018_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(63).min()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    v_007 = v_006.rolling(10).var()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc018_5d_slope_v018_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc018_5d_slope_v018_signal

def f156g_f156_gross_profit_to_fcf_quality_calc019_5d_slope_v019_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + revenue)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(5).var()
    v_008 = v_007.rolling(21).rank(pct=True)
    v_009 = v_008.rolling(42).skew()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc019_5d_slope_v019_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc019_5d_slope_v019_signal

def f156g_f156_gross_profit_to_fcf_quality_calc020_10d_slope_v020_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(10).min()
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = (v_004 - v_004.rolling(42).mean()) / v_004.rolling(42).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(126).max() / v_007.rolling(126).min().replace(0, np.nan)
    v_009 = v_008.rolling(63).var()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc020_10d_slope_v020_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc020_10d_slope_v020_signal

def f156g_f156_gross_profit_to_fcf_quality_calc021_10d_slope_v021_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(5).mean()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(5).max()
    v_007 = v_006.rolling(126).var()
    v_008 = (v_007 - v_007.rolling(42).mean()) / v_007.rolling(42).std().replace(0, np.nan)
    v_009 = v_008.rolling(252).max() / v_008.rolling(252).min().replace(0, np.nan)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc021_10d_slope_v021_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc021_10d_slope_v021_signal

def f156g_f156_gross_profit_to_fcf_quality_calc022_63d_slope_v022_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(1)
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(63).var()
    v_007 = v_006.rolling(63).var()
    v_008 = v_007.rolling(63).std()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc022_63d_slope_v022_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc022_63d_slope_v022_signal

def f156g_f156_gross_profit_to_fcf_quality_calc023_63d_slope_v023_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(5).kurt()
    v_004 = (v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(126).min()
    v_008 = v_007.rolling(252).std()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc023_63d_slope_v023_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc023_63d_slope_v023_signal

def f156g_f156_gross_profit_to_fcf_quality_calc024_5d_slope_v024_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(10).max() / v_001.rolling(10).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(10).min()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc024_5d_slope_v024_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc024_5d_slope_v024_signal

def f156g_f156_gross_profit_to_fcf_quality_calc025_63d_slope_v025_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).mean()
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).kurt()
    v_006 = v_005.rolling(21).rank(pct=True)
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc025_63d_slope_v025_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc025_63d_slope_v025_signal

def f156g_f156_gross_profit_to_fcf_quality_calc026_10d_slope_v026_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(126).kurt()
    v_009 = v_008.rolling(126).rank(pct=True)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc026_10d_slope_v026_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc026_10d_slope_v026_signal

def f156g_f156_gross_profit_to_fcf_quality_calc027_126d_slope_v027_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(10).var()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(126).skew()
    v_008 = v_007.rolling(10).min()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc027_126d_slope_v027_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc027_126d_slope_v027_signal

def f156g_f156_gross_profit_to_fcf_quality_calc028_126d_slope_v028_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(21).mean()
    v_007 = (v_006 - v_006.rolling(42).mean()) / v_006.rolling(42).std().replace(0, np.nan)
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc028_126d_slope_v028_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc028_126d_slope_v028_signal

def f156g_f156_gross_profit_to_fcf_quality_calc029_126d_slope_v029_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(21).mean()
    v_006 = v_005.rolling(63).var()
    v_007 = v_006.rolling(252).rank(pct=True)
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc029_126d_slope_v029_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc029_126d_slope_v029_signal

def f156g_f156_gross_profit_to_fcf_quality_calc030_63d_slope_v030_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(10).min()
    v_008 = v_007.rolling(42).min()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc030_63d_slope_v030_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc030_63d_slope_v030_signal

def f156g_f156_gross_profit_to_fcf_quality_calc031_42d_slope_v031_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - revenue)
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(5).mean()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc031_42d_slope_v031_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc031_42d_slope_v031_signal

def f156g_f156_gross_profit_to_fcf_quality_calc032_10d_slope_v032_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = v_005.rolling(5).min()
    v_007 = (v_006 - v_006.rolling(21).mean()) / v_006.rolling(21).std().replace(0, np.nan)
    v_008 = v_007.rolling(21).skew()
    v_009 = (v_008 - v_008.rolling(63).mean()) / v_008.rolling(63).std().replace(0, np.nan)
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc032_10d_slope_v032_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc032_10d_slope_v032_signal

def f156g_f156_gross_profit_to_fcf_quality_calc033_42d_slope_v033_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).min()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(252).skew()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc033_42d_slope_v033_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc033_42d_slope_v033_signal

def f156g_f156_gross_profit_to_fcf_quality_calc034_63d_slope_v034_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - ncfo)
    v_002 = v_001.rolling(126).kurt()
    v_003 = (v_002 - v_002.rolling(21).mean()) / v_002.rolling(21).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(21).max() / v_004.rolling(21).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(252).kurt()
    v_008 = (v_007 - v_007.rolling(10).mean()) / v_007.rolling(10).std().replace(0, np.nan)
    v_009 = v_008.rolling(126).min()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc034_63d_slope_v034_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc034_63d_slope_v034_signal

def f156g_f156_gross_profit_to_fcf_quality_calc035_21d_slope_v035_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - gross_profit)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(126).mean()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc035_21d_slope_v035_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc035_21d_slope_v035_signal

def f156g_f156_gross_profit_to_fcf_quality_calc036_252d_slope_v036_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + revenue)
    v_002 = v_001.rolling(252).rank(pct=True)
    v_003 = v_002.rolling(5).std()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(10).rank(pct=True)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc036_252d_slope_v036_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc036_252d_slope_v036_signal

def f156g_f156_gross_profit_to_fcf_quality_calc037_252d_slope_v037_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(126).max() / v_002.rolling(126).min().replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(126).max()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc037_252d_slope_v037_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc037_252d_slope_v037_signal

def f156g_f156_gross_profit_to_fcf_quality_calc038_5d_slope_v038_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).kurt()
    v_003 = v_002.rolling(126).var()
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(42).max()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc038_5d_slope_v038_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc038_5d_slope_v038_signal

def f156g_f156_gross_profit_to_fcf_quality_calc039_252d_slope_v039_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(126).mean()
    v_007 = v_006.rolling(5).skew()
    v_008 = v_007.rolling(126).kurt()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc039_252d_slope_v039_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc039_252d_slope_v039_signal

def f156g_f156_gross_profit_to_fcf_quality_calc040_252d_slope_v040_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - revenue)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).mean()
    v_008 = v_007.rolling(21).kurt()
    v_009 = v_008.rolling(5).rank(pct=True)
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc040_252d_slope_v040_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc040_252d_slope_v040_signal

def f156g_f156_gross_profit_to_fcf_quality_calc041_10d_slope_v041_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - revenue)
    v_002 = v_001.rolling(126).kurt()
    v_003 = v_002.rolling(5).kurt()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(126).max()
    v_008 = v_007.rolling(5).var()
    v_009 = v_008.rolling(126).skew()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc041_10d_slope_v041_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc041_10d_slope_v041_signal

def f156g_f156_gross_profit_to_fcf_quality_calc042_126d_slope_v042_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(5).std()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(21).mean()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).std()
    v_008 = v_007.rolling(126).rank(pct=True)
    v_009 = v_008.rolling(5).rank(pct=True)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc042_126d_slope_v042_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc042_126d_slope_v042_signal

def f156g_f156_gross_profit_to_fcf_quality_calc043_42d_slope_v043_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(126).mean()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(252).var()
    v_007 = (v_006 - v_006.rolling(5).mean()) / v_006.rolling(5).std().replace(0, np.nan)
    v_008 = v_007.rolling(10).kurt()
    v_009 = v_008.rolling(63).kurt()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc043_42d_slope_v043_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc043_42d_slope_v043_signal

def f156g_f156_gross_profit_to_fcf_quality_calc044_21d_slope_v044_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(252).skew()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc044_21d_slope_v044_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc044_21d_slope_v044_signal

def f156g_f156_gross_profit_to_fcf_quality_calc045_21d_slope_v045_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - gross_profit)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).skew()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(5).std()
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).min()
    v_008 = v_007.rolling(5).max()
    v_009 = v_008.rolling(21).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc045_21d_slope_v045_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc045_21d_slope_v045_signal

def f156g_f156_gross_profit_to_fcf_quality_calc046_10d_slope_v046_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(5).kurt()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(21).skew()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).skew()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc046_10d_slope_v046_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc046_10d_slope_v046_signal

def f156g_f156_gross_profit_to_fcf_quality_calc047_10d_slope_v047_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).kurt()
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.rolling(5).max() / v_004.rolling(5).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(10).max()
    v_008 = v_007.rolling(63).rank(pct=True)
    v_009 = v_008.rolling(42).mean()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc047_10d_slope_v047_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc047_10d_slope_v047_signal

def f156g_f156_gross_profit_to_fcf_quality_calc048_252d_slope_v048_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(5).rank(pct=True)
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc048_252d_slope_v048_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc048_252d_slope_v048_signal

def f156g_f156_gross_profit_to_fcf_quality_calc049_21d_slope_v049_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).kurt()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc049_21d_slope_v049_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc049_21d_slope_v049_signal

def f156g_f156_gross_profit_to_fcf_quality_calc050_5d_slope_v050_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(5).mean()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc050_5d_slope_v050_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc050_5d_slope_v050_signal

def f156g_f156_gross_profit_to_fcf_quality_calc051_5d_slope_v051_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - revenue)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(10).skew()
    v_007 = v_006.rolling(42).skew()
    v_008 = v_007.rolling(42).mean()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc051_5d_slope_v051_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc051_5d_slope_v051_signal

def f156g_f156_gross_profit_to_fcf_quality_calc052_42d_slope_v052_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(10).skew()
    v_008 = (v_007 - v_007.rolling(252).mean()) / v_007.rolling(252).std().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc052_42d_slope_v052_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc052_42d_slope_v052_signal

def f156g_f156_gross_profit_to_fcf_quality_calc053_5d_slope_v053_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(126).max() / v_007.rolling(126).min().replace(0, np.nan)
    v_009 = v_008.rolling(10).min()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc053_5d_slope_v053_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc053_5d_slope_v053_signal

def f156g_f156_gross_profit_to_fcf_quality_calc054_21d_slope_v054_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(5).std()
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(252).skew()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc054_21d_slope_v054_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc054_21d_slope_v054_signal

def f156g_f156_gross_profit_to_fcf_quality_calc055_252d_slope_v055_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = (v_001 - v_001.rolling(63).mean()) / v_001.rolling(63).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc055_252d_slope_v055_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc055_252d_slope_v055_signal

def f156g_f156_gross_profit_to_fcf_quality_calc056_21d_slope_v056_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(5).std()
    v_007 = v_006.rolling(63).min()
    v_008 = v_007.rolling(42).skew()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc056_21d_slope_v056_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc056_21d_slope_v056_signal

def f156g_f156_gross_profit_to_fcf_quality_calc057_63d_slope_v057_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.rolling(21).var()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(10).mean()) / v_006.rolling(10).std().replace(0, np.nan)
    v_008 = v_007.rolling(5).min()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc057_63d_slope_v057_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc057_63d_slope_v057_signal

def f156g_f156_gross_profit_to_fcf_quality_calc058_21d_slope_v058_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(21).max()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).max() / v_004.rolling(42).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).max() / v_005.rolling(252).min().replace(0, np.nan)
    v_007 = v_006.rolling(5).kurt()
    v_008 = v_007.rolling(252).rank(pct=True)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc058_21d_slope_v058_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc058_21d_slope_v058_signal

def f156g_f156_gross_profit_to_fcf_quality_calc059_252d_slope_v059_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(10).mean()
    v_003 = v_002.rolling(126).kurt()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc059_252d_slope_v059_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc059_252d_slope_v059_signal

def f156g_f156_gross_profit_to_fcf_quality_calc060_5d_slope_v060_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(5).skew()
    v_006 = (v_005 - v_005.rolling(10).mean()) / v_005.rolling(10).std().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(252).mean()) / v_006.rolling(252).std().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc060_5d_slope_v060_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc060_5d_slope_v060_signal

def f156g_f156_gross_profit_to_fcf_quality_calc061_126d_slope_v061_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = v_005.rolling(5).mean()
    v_007 = v_006.rolling(42).skew()
    v_008 = v_007.rolling(10).skew()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc061_126d_slope_v061_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc061_126d_slope_v061_signal

def f156g_f156_gross_profit_to_fcf_quality_calc062_42d_slope_v062_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc062_42d_slope_v062_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc062_42d_slope_v062_signal

def f156g_f156_gross_profit_to_fcf_quality_calc063_63d_slope_v063_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(42).max() / v_004.rolling(42).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(10).max()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc063_63d_slope_v063_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc063_63d_slope_v063_signal

def f156g_f156_gross_profit_to_fcf_quality_calc064_5d_slope_v064_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(252).max()
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).skew()
    v_008 = v_007.rolling(10).min()
    v_009 = v_008.rolling(252).skew()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc064_5d_slope_v064_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc064_5d_slope_v064_signal

def f156g_f156_gross_profit_to_fcf_quality_calc065_42d_slope_v065_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(252).skew()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc065_42d_slope_v065_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc065_42d_slope_v065_signal

def f156g_f156_gross_profit_to_fcf_quality_calc066_5d_slope_v066_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - gross_profit)
    v_002 = v_001.rolling(21).min()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(10).min()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc066_5d_slope_v066_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc066_5d_slope_v066_signal

def f156g_f156_gross_profit_to_fcf_quality_calc067_63d_slope_v067_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(63).mean()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc067_63d_slope_v067_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc067_63d_slope_v067_signal

def f156g_f156_gross_profit_to_fcf_quality_calc068_21d_slope_v068_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - revenue)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(126).mean()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc068_21d_slope_v068_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc068_21d_slope_v068_signal

def f156g_f156_gross_profit_to_fcf_quality_calc069_252d_slope_v069_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(126).max()
    v_008 = v_007.rolling(252).min()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc069_252d_slope_v069_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc069_252d_slope_v069_signal

def f156g_f156_gross_profit_to_fcf_quality_calc070_126d_slope_v070_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(5).min()
    v_008 = v_007.rolling(63).rank(pct=True)
    v_009 = v_008.rolling(252).mean()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc070_126d_slope_v070_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc070_126d_slope_v070_signal

def f156g_f156_gross_profit_to_fcf_quality_calc071_63d_slope_v071_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(42).mean()
    v_008 = v_007.rolling(21).skew()
    v_009 = (v_008 - v_008.rolling(10).mean()) / v_008.rolling(10).std().replace(0, np.nan)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc071_63d_slope_v071_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc071_63d_slope_v071_signal

def f156g_f156_gross_profit_to_fcf_quality_calc072_252d_slope_v072_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(21).std()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc072_252d_slope_v072_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc072_252d_slope_v072_signal

def f156g_f156_gross_profit_to_fcf_quality_calc073_21d_slope_v073_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).kurt()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc073_21d_slope_v073_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc073_21d_slope_v073_signal

def f156g_f156_gross_profit_to_fcf_quality_calc074_63d_slope_v074_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = v_005.rolling(10).std()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc074_63d_slope_v074_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc074_63d_slope_v074_signal

def f156g_f156_gross_profit_to_fcf_quality_calc075_10d_slope_v075_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.rolling(21).max() / v_004.rolling(21).min().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = v_006.rolling(42).skew()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc075_10d_slope_v075_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc075_10d_slope_v075_signal

def f156g_f156_gross_profit_to_fcf_quality_calc076_126d_slope_v076_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(42).skew()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(42).min()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).skew()
    v_007 = v_006.rolling(126).rank(pct=True)
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc076_126d_slope_v076_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc076_126d_slope_v076_signal

def f156g_f156_gross_profit_to_fcf_quality_calc077_5d_slope_v077_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = v_006.rolling(21).skew()
    v_008 = v_007.rolling(42).var()
    v_009 = v_008.rolling(10).max() / v_008.rolling(10).min().replace(0, np.nan)
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc077_5d_slope_v077_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc077_5d_slope_v077_signal

def f156g_f156_gross_profit_to_fcf_quality_calc078_5d_slope_v078_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.rolling(5).max()
    v_006 = v_005.rolling(252).std()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc078_5d_slope_v078_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc078_5d_slope_v078_signal

def f156g_f156_gross_profit_to_fcf_quality_calc079_126d_slope_v079_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(10).min()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc079_126d_slope_v079_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc079_126d_slope_v079_signal

def f156g_f156_gross_profit_to_fcf_quality_calc080_10d_slope_v080_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - gross_profit)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(42).skew()
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(21).min()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc080_10d_slope_v080_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc080_10d_slope_v080_signal

def f156g_f156_gross_profit_to_fcf_quality_calc081_252d_slope_v081_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(63).min()
    v_007 = v_006.rolling(252).max()
    v_008 = v_007.rolling(5).std()
    v_009 = v_008.rolling(10).std()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc081_252d_slope_v081_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc081_252d_slope_v081_signal

def f156g_f156_gross_profit_to_fcf_quality_calc082_21d_slope_v082_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(10).skew()
    v_008 = v_007.rolling(42).max() / v_007.rolling(42).min().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc082_21d_slope_v082_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc082_21d_slope_v082_signal

def f156g_f156_gross_profit_to_fcf_quality_calc083_5d_slope_v083_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc083_5d_slope_v083_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc083_5d_slope_v083_signal

def f156g_f156_gross_profit_to_fcf_quality_calc084_252d_slope_v084_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - revenue)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(126).std()
    v_008 = v_007.rolling(252).var()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc084_252d_slope_v084_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc084_252d_slope_v084_signal

def f156g_f156_gross_profit_to_fcf_quality_calc085_10d_slope_v085_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - gross_profit)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(10).skew()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc085_10d_slope_v085_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc085_10d_slope_v085_signal

def f156g_f156_gross_profit_to_fcf_quality_calc086_252d_slope_v086_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - gross_profit)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(126).mean()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(63).var()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc086_252d_slope_v086_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc086_252d_slope_v086_signal

def f156g_f156_gross_profit_to_fcf_quality_calc087_5d_slope_v087_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(42).mean()
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(21).max()
    v_007 = v_006.rolling(10).mean()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc087_5d_slope_v087_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc087_5d_slope_v087_signal

def f156g_f156_gross_profit_to_fcf_quality_calc088_42d_slope_v088_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(252).min()
    v_004 = (v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(21).mean()) / v_006.rolling(21).std().replace(0, np.nan)
    v_008 = v_007.rolling(63).std()
    v_009 = v_008.rolling(252).skew()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc088_42d_slope_v088_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc088_42d_slope_v088_signal

def f156g_f156_gross_profit_to_fcf_quality_calc089_21d_slope_v089_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(252).min()
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).std()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc089_21d_slope_v089_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc089_21d_slope_v089_signal

def f156g_f156_gross_profit_to_fcf_quality_calc090_42d_slope_v090_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - free_cash_flow)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(63).skew()
    v_007 = v_006.rolling(63).mean()
    v_008 = v_007.rolling(63).min()
    v_009 = v_008.rolling(21).max() / v_008.rolling(21).min().replace(0, np.nan)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc090_42d_slope_v090_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc090_42d_slope_v090_signal

def f156g_f156_gross_profit_to_fcf_quality_calc091_126d_slope_v091_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = (v_006 - v_006.rolling(5).mean()) / v_006.rolling(5).std().replace(0, np.nan)
    v_008 = v_007.rolling(42).min()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc091_126d_slope_v091_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc091_126d_slope_v091_signal

def f156g_f156_gross_profit_to_fcf_quality_calc092_252d_slope_v092_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - revenue)
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(42).max() / v_002.rolling(42).min().replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(252).min()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc092_252d_slope_v092_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc092_252d_slope_v092_signal

def f156g_f156_gross_profit_to_fcf_quality_calc093_21d_slope_v093_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - revenue)
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(10).var()
    v_008 = v_007.rolling(126).max() / v_007.rolling(126).min().replace(0, np.nan)
    v_009 = v_008.rolling(252).max()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc093_21d_slope_v093_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc093_21d_slope_v093_signal

def f156g_f156_gross_profit_to_fcf_quality_calc094_10d_slope_v094_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(10).mean()
    v_003 = v_002.rolling(42).max() / v_002.rolling(42).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(42).kurt()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc094_10d_slope_v094_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc094_10d_slope_v094_signal

def f156g_f156_gross_profit_to_fcf_quality_calc095_21d_slope_v095_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(63).std()
    v_003 = v_002.rolling(42).max() / v_002.rolling(42).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc095_21d_slope_v095_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc095_21d_slope_v095_signal

def f156g_f156_gross_profit_to_fcf_quality_calc096_21d_slope_v096_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(126).mean()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(21).var()
    v_007 = (v_006 - v_006.rolling(252).mean()) / v_006.rolling(252).std().replace(0, np.nan)
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc096_21d_slope_v096_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc096_21d_slope_v096_signal

def f156g_f156_gross_profit_to_fcf_quality_calc097_10d_slope_v097_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(63).skew()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc097_10d_slope_v097_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc097_10d_slope_v097_signal

def f156g_f156_gross_profit_to_fcf_quality_calc098_126d_slope_v098_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(126).skew()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = v_005.rolling(63).std()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc098_126d_slope_v098_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc098_126d_slope_v098_signal

def f156g_f156_gross_profit_to_fcf_quality_calc099_21d_slope_v099_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).var()
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(126).std()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc099_21d_slope_v099_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc099_21d_slope_v099_signal

def f156g_f156_gross_profit_to_fcf_quality_calc100_126d_slope_v100_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(252).rank(pct=True)
    v_003 = v_002.rolling(5).std()
    v_004 = (v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = v_005.rolling(63).skew()
    v_007 = v_006.rolling(10).max()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc100_126d_slope_v100_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc100_126d_slope_v100_signal

def f156g_f156_gross_profit_to_fcf_quality_calc101_126d_slope_v101_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(5).skew()
    v_008 = v_007.rolling(42).kurt()
    v_009 = v_008.rolling(42).var()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc101_126d_slope_v101_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc101_126d_slope_v101_signal

def f156g_f156_gross_profit_to_fcf_quality_calc102_126d_slope_v102_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - free_cash_flow)
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(63).min()
    v_007 = v_006.rolling(42).rank(pct=True)
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc102_126d_slope_v102_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc102_126d_slope_v102_signal

def f156g_f156_gross_profit_to_fcf_quality_calc103_5d_slope_v103_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(126).mean()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc103_5d_slope_v103_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc103_5d_slope_v103_signal

def f156g_f156_gross_profit_to_fcf_quality_calc104_63d_slope_v104_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(126).min()
    v_008 = v_007.rolling(10).var()
    v_009 = v_008.rolling(252).kurt()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc104_63d_slope_v104_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc104_63d_slope_v104_signal

def f156g_f156_gross_profit_to_fcf_quality_calc105_126d_slope_v105_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(252).skew()
    v_008 = v_007.rolling(21).max() / v_007.rolling(21).min().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc105_126d_slope_v105_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc105_126d_slope_v105_signal

def f156g_f156_gross_profit_to_fcf_quality_calc106_10d_slope_v106_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(21).min()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc106_10d_slope_v106_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc106_10d_slope_v106_signal

def f156g_f156_gross_profit_to_fcf_quality_calc107_63d_slope_v107_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(126).std()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc107_63d_slope_v107_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc107_63d_slope_v107_signal

def f156g_f156_gross_profit_to_fcf_quality_calc108_126d_slope_v108_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(63).mean()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc108_126d_slope_v108_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc108_126d_slope_v108_signal

def f156g_f156_gross_profit_to_fcf_quality_calc109_10d_slope_v109_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(10).min()
    v_008 = v_007.rolling(63).mean()
    v_009 = v_008.rolling(126).max()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc109_10d_slope_v109_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc109_10d_slope_v109_signal

def f156g_f156_gross_profit_to_fcf_quality_calc110_10d_slope_v110_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = v_006.rolling(252).var()
    v_008 = v_007.rolling(252).var()
    v_009 = v_008.rolling(5).rank(pct=True)
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc110_10d_slope_v110_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc110_10d_slope_v110_signal

def f156g_f156_gross_profit_to_fcf_quality_calc111_42d_slope_v111_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + gross_profit)
    v_002 = v_001.rolling(63).skew()
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).var()
    v_007 = v_006.rolling(42).min()
    v_008 = v_007.rolling(252).kurt()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc111_42d_slope_v111_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc111_42d_slope_v111_signal

def f156g_f156_gross_profit_to_fcf_quality_calc112_42d_slope_v112_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(5).max()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(63).min()
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    v_009 = v_008.rolling(10).max()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc112_42d_slope_v112_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc112_42d_slope_v112_signal

def f156g_f156_gross_profit_to_fcf_quality_calc113_21d_slope_v113_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + free_cash_flow)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(126).var()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc113_21d_slope_v113_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc113_21d_slope_v113_signal

def f156g_f156_gross_profit_to_fcf_quality_calc114_126d_slope_v114_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(5).kurt()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc114_126d_slope_v114_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc114_126d_slope_v114_signal

def f156g_f156_gross_profit_to_fcf_quality_calc115_126d_slope_v115_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(10).min()
    v_003 = (v_002 - v_002.rolling(5).mean()) / v_002.rolling(5).std().replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(252).var()
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(5).std()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc115_126d_slope_v115_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc115_126d_slope_v115_signal

def f156g_f156_gross_profit_to_fcf_quality_calc116_63d_slope_v116_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(252).std()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(252).max()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc116_63d_slope_v116_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc116_63d_slope_v116_signal

def f156g_f156_gross_profit_to_fcf_quality_calc117_10d_slope_v117_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(126).min()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc117_10d_slope_v117_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc117_10d_slope_v117_signal

def f156g_f156_gross_profit_to_fcf_quality_calc118_126d_slope_v118_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(126).max()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc118_126d_slope_v118_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc118_126d_slope_v118_signal

def f156g_f156_gross_profit_to_fcf_quality_calc119_21d_slope_v119_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(63).mean()
    v_008 = v_007.rolling(63).var()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc119_21d_slope_v119_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc119_21d_slope_v119_signal

def f156g_f156_gross_profit_to_fcf_quality_calc120_252d_slope_v120_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(5).kurt()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(10).skew()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(21).rank(pct=True)
    v_009 = v_008.rolling(10).max() / v_008.rolling(10).min().replace(0, np.nan)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc120_252d_slope_v120_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc120_252d_slope_v120_signal

def f156g_f156_gross_profit_to_fcf_quality_calc121_252d_slope_v121_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(252).max()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).max()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    v_008 = v_007.rolling(126).max() / v_007.rolling(126).min().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc121_252d_slope_v121_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc121_252d_slope_v121_signal

def f156g_f156_gross_profit_to_fcf_quality_calc122_252d_slope_v122_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(126).skew()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(252).var()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(252).mean()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc122_252d_slope_v122_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc122_252d_slope_v122_signal

def f156g_f156_gross_profit_to_fcf_quality_calc123_5d_slope_v123_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(5).max()
    v_006 = v_005.rolling(5).std()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(21).max()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc123_5d_slope_v123_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc123_5d_slope_v123_signal

def f156g_f156_gross_profit_to_fcf_quality_calc124_10d_slope_v124_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = v_001.rolling(42).mean()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(252).min()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc124_10d_slope_v124_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc124_10d_slope_v124_signal

def f156g_f156_gross_profit_to_fcf_quality_calc125_252d_slope_v125_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + free_cash_flow)
    v_002 = v_001.rolling(63).mean()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(63).std()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc125_252d_slope_v125_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc125_252d_slope_v125_signal

def f156g_f156_gross_profit_to_fcf_quality_calc126_5d_slope_v126_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(21).mean()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(63).min()
    v_007 = v_006.rolling(63).var()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc126_5d_slope_v126_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc126_5d_slope_v126_signal

def f156g_f156_gross_profit_to_fcf_quality_calc127_252d_slope_v127_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + revenue)
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).min()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    v_009 = v_008.rolling(252).max()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc127_252d_slope_v127_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc127_252d_slope_v127_signal

def f156g_f156_gross_profit_to_fcf_quality_calc128_21d_slope_v128_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(10).kurt()
    v_008 = (v_007 - v_007.rolling(252).mean()) / v_007.rolling(252).std().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc128_21d_slope_v128_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc128_21d_slope_v128_signal

def f156g_f156_gross_profit_to_fcf_quality_calc129_42d_slope_v129_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - gross_profit)
    v_002 = v_001.rolling(126).kurt()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(10).skew()
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    v_009 = v_008.rolling(63).kurt()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc129_42d_slope_v129_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc129_42d_slope_v129_signal

def f156g_f156_gross_profit_to_fcf_quality_calc130_21d_slope_v130_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).std()
    v_003 = v_002.rolling(42).skew()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(5).min()
    v_008 = v_007.rolling(21).kurt()
    v_009 = v_008.rolling(5).max()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc130_21d_slope_v130_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc130_21d_slope_v130_signal

def f156g_f156_gross_profit_to_fcf_quality_calc131_5d_slope_v131_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(252).std()
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(10).mean()) / v_005.rolling(10).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).std()
    v_008 = v_007.rolling(21).max()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc131_5d_slope_v131_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc131_5d_slope_v131_signal

def f156g_f156_gross_profit_to_fcf_quality_calc132_10d_slope_v132_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + revenue)
    v_002 = v_001.rolling(252).max()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(42).min()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc132_10d_slope_v132_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc132_10d_slope_v132_signal

def f156g_f156_gross_profit_to_fcf_quality_calc133_63d_slope_v133_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(10).kurt()
    v_008 = v_007.rolling(252).min()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc133_63d_slope_v133_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc133_63d_slope_v133_signal

def f156g_f156_gross_profit_to_fcf_quality_calc134_126d_slope_v134_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(21).kurt()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.rolling(21).mean()
    v_006 = v_005.rolling(126).rank(pct=True)
    v_007 = (v_006 - v_006.rolling(5).mean()) / v_006.rolling(5).std().replace(0, np.nan)
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc134_126d_slope_v134_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc134_126d_slope_v134_signal

def f156g_f156_gross_profit_to_fcf_quality_calc135_21d_slope_v135_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(126).max() / v_002.rolling(126).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(42).mean()
    v_008 = v_007.rolling(5).rank(pct=True)
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc135_21d_slope_v135_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc135_21d_slope_v135_signal

def f156g_f156_gross_profit_to_fcf_quality_calc136_10d_slope_v136_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(5).max()
    v_008 = v_007.rolling(126).rank(pct=True)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc136_10d_slope_v136_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc136_10d_slope_v136_signal

def f156g_f156_gross_profit_to_fcf_quality_calc137_126d_slope_v137_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).kurt()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(126).max()
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(63).min()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc137_126d_slope_v137_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc137_126d_slope_v137_signal

def f156g_f156_gross_profit_to_fcf_quality_calc138_42d_slope_v138_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(63).var()
    v_007 = v_006.rolling(5).max()
    v_008 = v_007.rolling(21).std()
    v_009 = v_008.rolling(5).max()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc138_42d_slope_v138_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc138_42d_slope_v138_signal

def f156g_f156_gross_profit_to_fcf_quality_calc139_42d_slope_v139_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - ncfo)
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(21).var()
    v_007 = v_006.rolling(10).skew()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc139_42d_slope_v139_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc139_42d_slope_v139_signal

def f156g_f156_gross_profit_to_fcf_quality_calc140_126d_slope_v140_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(42).var()
    v_006 = v_005.rolling(5).skew()
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(126).max()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc140_126d_slope_v140_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc140_126d_slope_v140_signal

def f156g_f156_gross_profit_to_fcf_quality_calc141_42d_slope_v141_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - revenue)
    v_002 = v_001.rolling(21).std()
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(42).max() / v_004.rolling(42).min().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(42).mean()
    v_009 = v_008.rolling(63).var()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc141_42d_slope_v141_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc141_42d_slope_v141_signal

def f156g_f156_gross_profit_to_fcf_quality_calc142_10d_slope_v142_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow - revenue)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(126).kurt()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc142_10d_slope_v142_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc142_10d_slope_v142_signal

def f156g_f156_gross_profit_to_fcf_quality_calc143_21d_slope_v143_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(42).var()
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(5).std()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = v_006.rolling(63).rank(pct=True)
    v_008 = v_007.rolling(10).min()
    v_009 = v_008.rolling(126).rank(pct=True)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc143_21d_slope_v143_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc143_21d_slope_v143_signal

def f156g_f156_gross_profit_to_fcf_quality_calc144_10d_slope_v144_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(126).skew()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc144_10d_slope_v144_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc144_10d_slope_v144_signal

def f156g_f156_gross_profit_to_fcf_quality_calc145_10d_slope_v145_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - gross_profit)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(10).var()
    v_004 = (v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(252).min()
    v_008 = v_007.rolling(63).rank(pct=True)
    v_009 = v_008.rolling(21).max()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc145_10d_slope_v145_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc145_10d_slope_v145_signal

def f156g_f156_gross_profit_to_fcf_quality_calc146_126d_slope_v146_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(252).std()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc146_126d_slope_v146_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc146_126d_slope_v146_signal

def f156g_f156_gross_profit_to_fcf_quality_calc147_63d_slope_v147_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(5).kurt()
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = v_005.rolling(252).max()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc147_63d_slope_v147_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc147_63d_slope_v147_signal

def f156g_f156_gross_profit_to_fcf_quality_calc148_63d_slope_v148_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(42).max()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(252).min()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc148_63d_slope_v148_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc148_63d_slope_v148_signal

def f156g_f156_gross_profit_to_fcf_quality_calc149_21d_slope_v149_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(252).var()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(21).std()
    v_007 = (v_006 - v_006.rolling(5).mean()) / v_006.rolling(5).std().replace(0, np.nan)
    v_008 = v_007.rolling(63).skew()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc149_21d_slope_v149_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc149_21d_slope_v149_signal

def f156g_f156_gross_profit_to_fcf_quality_calc150_126d_slope_v150_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(42).rank(pct=True)
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(42).max()
    v_009 = v_008.rolling(21).min()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc150_126d_slope_v150_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc150_126d_slope_v150_signal


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
