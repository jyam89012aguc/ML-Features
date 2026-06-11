import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f156g_f156_gross_profit_to_fcf_quality_calc076_126d_base_v076_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(63).var()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc076_126d_base_v076_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc076_126d_base_v076_signal

def f156g_f156_gross_profit_to_fcf_quality_calc077_5d_base_v077_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + ncfo)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(42).kurt()
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(10).min()
    v_009 = v_008.rolling(10).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc077_5d_base_v077_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc077_5d_base_v077_signal

def f156g_f156_gross_profit_to_fcf_quality_calc078_5d_base_v078_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + revenue)
    v_002 = v_001.rolling(63).min()
    v_003 = v_002.rolling(42).max() / v_002.rolling(42).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(126).max()
    v_008 = (v_007 - v_007.rolling(42).mean()) / v_007.rolling(42).std().replace(0, np.nan)
    v_009 = v_008.rolling(10).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc078_5d_base_v078_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc078_5d_base_v078_signal

def f156g_f156_gross_profit_to_fcf_quality_calc079_126d_base_v079_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).kurt()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(5).kurt()
    v_009 = v_008.rolling(5).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc079_126d_base_v079_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc079_126d_base_v079_signal

def f156g_f156_gross_profit_to_fcf_quality_calc080_10d_base_v080_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(63).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc080_10d_base_v080_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc080_10d_base_v080_signal

def f156g_f156_gross_profit_to_fcf_quality_calc081_252d_base_v081_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(21).max()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(252).mean()) / v_005.rolling(252).std().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc081_252d_base_v081_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc081_252d_base_v081_signal

def f156g_f156_gross_profit_to_fcf_quality_calc082_21d_base_v082_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(126).max() / v_002.rolling(126).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(63).rank(pct=True)
    v_008 = v_007.rolling(5).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc082_21d_base_v082_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc082_21d_base_v082_signal

def f156g_f156_gross_profit_to_fcf_quality_calc083_5d_base_v083_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc083_5d_base_v083_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc083_5d_base_v083_signal

def f156g_f156_gross_profit_to_fcf_quality_calc084_252d_base_v084_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(10).rank(pct=True)
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(42).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc084_252d_base_v084_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc084_252d_base_v084_signal

def f156g_f156_gross_profit_to_fcf_quality_calc085_10d_base_v085_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + free_cash_flow)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(42).min()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc085_10d_base_v085_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc085_10d_base_v085_signal

def f156g_f156_gross_profit_to_fcf_quality_calc086_252d_base_v086_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(21).max() / v_004.rolling(21).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc086_252d_base_v086_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc086_252d_base_v086_signal

def f156g_f156_gross_profit_to_fcf_quality_calc087_5d_base_v087_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).std()
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(42).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc087_5d_base_v087_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc087_5d_base_v087_signal

def f156g_f156_gross_profit_to_fcf_quality_calc088_42d_base_v088_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.rolling(42).kurt()
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(252).rank(pct=True)
    v_008 = v_007.rolling(42).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc088_42d_base_v088_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc088_42d_base_v088_signal

def f156g_f156_gross_profit_to_fcf_quality_calc089_21d_base_v089_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).std()
    v_003 = v_002.rolling(63).std()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(252).mean()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc089_21d_base_v089_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc089_21d_base_v089_signal

def f156g_f156_gross_profit_to_fcf_quality_calc090_42d_base_v090_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(21).mean()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = v_006.rolling(252).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc090_42d_base_v090_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc090_42d_base_v090_signal

def f156g_f156_gross_profit_to_fcf_quality_calc091_126d_base_v091_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(42).var()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    v_009 = v_008.rolling(21).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc091_126d_base_v091_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc091_126d_base_v091_signal

def f156g_f156_gross_profit_to_fcf_quality_calc092_252d_base_v092_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(42).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc092_252d_base_v092_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc092_252d_base_v092_signal

def f156g_f156_gross_profit_to_fcf_quality_calc093_21d_base_v093_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(126).mean()
    v_007 = v_006.rolling(63).kurt()
    v_008 = v_007.rolling(5).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc093_21d_base_v093_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc093_21d_base_v093_signal

def f156g_f156_gross_profit_to_fcf_quality_calc094_10d_base_v094_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).mean()
    v_003 = v_002.rolling(42).max() / v_002.rolling(42).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(5).mean()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc094_10d_base_v094_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc094_10d_base_v094_signal

def f156g_f156_gross_profit_to_fcf_quality_calc095_21d_base_v095_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(252).min()
    v_003 = v_002.rolling(21).rank(pct=True)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = v_006.rolling(10).std()
    v_008 = v_007.rolling(126).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc095_21d_base_v095_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc095_21d_base_v095_signal

def f156g_f156_gross_profit_to_fcf_quality_calc096_21d_base_v096_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(21).mean()
    v_007 = v_006.rolling(10).rank(pct=True)
    v_008 = v_007.rolling(252).mean()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc096_21d_base_v096_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc096_21d_base_v096_signal

def f156g_f156_gross_profit_to_fcf_quality_calc097_10d_base_v097_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - gross_profit)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(5).max()
    v_007 = v_006.rolling(252).mean()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc097_10d_base_v097_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc097_10d_base_v097_signal

def f156g_f156_gross_profit_to_fcf_quality_calc098_126d_base_v098_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).rank(pct=True)
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(21).std()
    v_007 = (v_006 - v_006.rolling(42).mean()) / v_006.rolling(42).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc098_126d_base_v098_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc098_126d_base_v098_signal

def f156g_f156_gross_profit_to_fcf_quality_calc099_21d_base_v099_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).var()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).min()
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc099_21d_base_v099_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc099_21d_base_v099_signal

def f156g_f156_gross_profit_to_fcf_quality_calc100_126d_base_v100_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(10).min()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(252).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc100_126d_base_v100_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc100_126d_base_v100_signal

def f156g_f156_gross_profit_to_fcf_quality_calc101_126d_base_v101_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(5).std()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(21).var()
    v_007 = v_006.rolling(42).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc101_126d_base_v101_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc101_126d_base_v101_signal

def f156g_f156_gross_profit_to_fcf_quality_calc102_126d_base_v102_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(10).mean()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(10).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc102_126d_base_v102_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc102_126d_base_v102_signal

def f156g_f156_gross_profit_to_fcf_quality_calc103_5d_base_v103_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = v_006.rolling(63).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc103_5d_base_v103_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc103_5d_base_v103_signal

def f156g_f156_gross_profit_to_fcf_quality_calc104_63d_base_v104_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(42).min()
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(63).var()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc104_63d_base_v104_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc104_63d_base_v104_signal

def f156g_f156_gross_profit_to_fcf_quality_calc105_126d_base_v105_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(42).min()
    v_006 = v_005.rolling(126).rank(pct=True)
    v_007 = v_006.rolling(63).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc105_126d_base_v105_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc105_126d_base_v105_signal

def f156g_f156_gross_profit_to_fcf_quality_calc106_10d_base_v106_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(21).kurt()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(252).kurt()
    v_009 = v_008.rolling(126).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc106_10d_base_v106_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc106_10d_base_v106_signal

def f156g_f156_gross_profit_to_fcf_quality_calc107_63d_base_v107_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(252).rank(pct=True)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(5).rank(pct=True)
    v_008 = v_007.rolling(5).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc107_63d_base_v107_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc107_63d_base_v107_signal

def f156g_f156_gross_profit_to_fcf_quality_calc108_126d_base_v108_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(21).mean()) / v_006.rolling(21).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc108_126d_base_v108_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc108_126d_base_v108_signal

def f156g_f156_gross_profit_to_fcf_quality_calc109_10d_base_v109_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + gross_profit)
    v_002 = v_001.rolling(252).kurt()
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(42).var()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(126).var()
    v_008 = v_007.rolling(21).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc109_10d_base_v109_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc109_10d_base_v109_signal

def f156g_f156_gross_profit_to_fcf_quality_calc110_10d_base_v110_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).min()
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).kurt()
    v_006 = v_005.rolling(126).mean()
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    v_008 = v_007.rolling(63).var()
    v_009 = v_008.rolling(10).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc110_10d_base_v110_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc110_10d_base_v110_signal

def f156g_f156_gross_profit_to_fcf_quality_calc111_42d_base_v111_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(126).max() / v_002.rolling(126).min().replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(5).rank(pct=True)
    v_008 = v_007.rolling(252).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc111_42d_base_v111_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc111_42d_base_v111_signal

def f156g_f156_gross_profit_to_fcf_quality_calc112_42d_base_v112_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue - gross_profit)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(126).rank(pct=True)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc112_42d_base_v112_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc112_42d_base_v112_signal

def f156g_f156_gross_profit_to_fcf_quality_calc113_21d_base_v113_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + free_cash_flow)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(5).kurt()
    v_008 = v_007.rolling(42).rank(pct=True)
    v_009 = v_008.rolling(42).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc113_21d_base_v113_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc113_21d_base_v113_signal

def f156g_f156_gross_profit_to_fcf_quality_calc114_126d_base_v114_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = (v_001 - v_001.rolling(63).mean()) / v_001.rolling(63).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).max() / v_002.rolling(126).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(126).rank(pct=True)
    v_008 = v_007.rolling(5).var()
    v_009 = v_008.rolling(126).mean()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc114_126d_base_v114_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc114_126d_base_v114_signal

def f156g_f156_gross_profit_to_fcf_quality_calc115_126d_base_v115_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan))
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(63).mean()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(252).mean()) / v_006.rolling(252).std().replace(0, np.nan)
    v_008 = v_007.rolling(10).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc115_126d_base_v115_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc115_126d_base_v115_signal

def f156g_f156_gross_profit_to_fcf_quality_calc116_63d_base_v116_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(126).std()
    v_007 = v_006.rolling(63).var()
    v_008 = v_007.rolling(252).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc116_63d_base_v116_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc116_63d_base_v116_signal

def f156g_f156_gross_profit_to_fcf_quality_calc117_10d_base_v117_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(126).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc117_10d_base_v117_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc117_10d_base_v117_signal

def f156g_f156_gross_profit_to_fcf_quality_calc118_126d_base_v118_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(21).rank(pct=True)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.rolling(126).mean()
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc118_126d_base_v118_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc118_126d_base_v118_signal

def f156g_f156_gross_profit_to_fcf_quality_calc119_21d_base_v119_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + gross_profit)
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).max()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(63).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc119_21d_base_v119_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc119_21d_base_v119_signal

def f156g_f156_gross_profit_to_fcf_quality_calc120_252d_base_v120_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + gross_profit)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(126).skew()
    v_004 = v_003.rolling(21).min()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).min()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc120_252d_base_v120_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc120_252d_base_v120_signal

def f156g_f156_gross_profit_to_fcf_quality_calc121_252d_base_v121_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + free_cash_flow)
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(42).var()
    v_007 = v_006.rolling(42).var()
    v_008 = (v_007 - v_007.rolling(21).mean()) / v_007.rolling(21).std().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc121_252d_base_v121_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc121_252d_base_v121_signal

def f156g_f156_gross_profit_to_fcf_quality_calc122_252d_base_v122_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + revenue)
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(42).max() / v_006.rolling(42).min().replace(0, np.nan)
    v_008 = (v_007 - v_007.rolling(10).mean()) / v_007.rolling(10).std().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc122_252d_base_v122_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc122_252d_base_v122_signal

def f156g_f156_gross_profit_to_fcf_quality_calc123_5d_base_v123_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + revenue)
    v_002 = v_001.rolling(42).min()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(42).rank(pct=True)
    v_008 = v_007.rolling(42).max()
    v_009 = v_008.rolling(21).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc123_5d_base_v123_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc123_5d_base_v123_signal

def f156g_f156_gross_profit_to_fcf_quality_calc124_10d_base_v124_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(42).max()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).min()
    v_008 = v_007.rolling(21).var()
    v_009 = v_008.rolling(5).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc124_10d_base_v124_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc124_10d_base_v124_signal

def f156g_f156_gross_profit_to_fcf_quality_calc125_252d_base_v125_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - free_cash_flow)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(63).mean()
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc125_252d_base_v125_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc125_252d_base_v125_signal

def f156g_f156_gross_profit_to_fcf_quality_calc126_5d_base_v126_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(63).mean()
    v_007 = v_006.rolling(252).mean()
    v_008 = v_007.rolling(10).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc126_5d_base_v126_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc126_5d_base_v126_signal

def f156g_f156_gross_profit_to_fcf_quality_calc127_252d_base_v127_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(63).min()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc127_252d_base_v127_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc127_252d_base_v127_signal

def f156g_f156_gross_profit_to_fcf_quality_calc128_21d_base_v128_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + revenue)
    v_002 = v_001.rolling(63).std()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(126).var()
    v_007 = v_006.rolling(21).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc128_21d_base_v128_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc128_21d_base_v128_signal

def f156g_f156_gross_profit_to_fcf_quality_calc129_42d_base_v129_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + gross_profit)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(21).var()
    v_006 = v_005.rolling(63).min()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(63).skew()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc129_42d_base_v129_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc129_42d_base_v129_signal

def f156g_f156_gross_profit_to_fcf_quality_calc130_21d_base_v130_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = (v_006 - v_006.rolling(42).mean()) / v_006.rolling(42).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc130_21d_base_v130_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc130_21d_base_v130_signal

def f156g_f156_gross_profit_to_fcf_quality_calc131_5d_base_v131_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / ncfo.replace(0, np.nan))
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(21).max()
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = v_006.rolling(21).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc131_5d_base_v131_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc131_5d_base_v131_signal

def f156g_f156_gross_profit_to_fcf_quality_calc132_10d_base_v132_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo + revenue)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).max() / v_004.rolling(252).min().replace(0, np.nan)
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(21).var()
    v_009 = v_008.rolling(21).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc132_10d_base_v132_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc132_10d_base_v132_signal

def f156g_f156_gross_profit_to_fcf_quality_calc133_63d_base_v133_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(21).kurt()
    v_007 = v_006.rolling(126).var()
    v_008 = v_007.rolling(126).max() / v_007.rolling(126).min().replace(0, np.nan)
    v_009 = v_008.rolling(10).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc133_63d_base_v133_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc133_63d_base_v133_signal

def f156g_f156_gross_profit_to_fcf_quality_calc134_126d_base_v134_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow + ncfo)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(10).min()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).max()
    v_007 = (v_006 - v_006.rolling(5).mean()) / v_006.rolling(5).std().replace(0, np.nan)
    v_008 = v_007.rolling(42).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc134_126d_base_v134_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc134_126d_base_v134_signal

def f156g_f156_gross_profit_to_fcf_quality_calc135_21d_base_v135_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(42).var()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    v_007 = v_006.rolling(126).max() / v_006.rolling(126).min().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc135_21d_base_v135_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc135_21d_base_v135_signal

def f156g_f156_gross_profit_to_fcf_quality_calc136_10d_base_v136_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - revenue)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc136_10d_base_v136_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc136_10d_base_v136_signal

def f156g_f156_gross_profit_to_fcf_quality_calc137_126d_base_v137_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan))
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(126).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc137_126d_base_v137_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc137_126d_base_v137_signal

def f156g_f156_gross_profit_to_fcf_quality_calc138_42d_base_v138_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(10).mean()) / v_004.rolling(10).std().replace(0, np.nan)
    v_006 = v_005.rolling(252).min()
    v_007 = v_006.rolling(252).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc138_42d_base_v138_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc138_42d_base_v138_signal

def f156g_f156_gross_profit_to_fcf_quality_calc139_42d_base_v139_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(21).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc139_42d_base_v139_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc139_42d_base_v139_signal

def f156g_f156_gross_profit_to_fcf_quality_calc140_126d_base_v140_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).mean()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = v_006.rolling(42).kurt()
    v_008 = v_007.rolling(10).max() / v_007.rolling(10).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc140_126d_base_v140_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc140_126d_base_v140_signal

def f156g_f156_gross_profit_to_fcf_quality_calc141_42d_base_v141_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue + ncfo)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).min()
    v_004 = (v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(126).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc141_42d_base_v141_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc141_42d_base_v141_signal

def f156g_f156_gross_profit_to_fcf_quality_calc142_10d_base_v142_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(5).mean()
    v_007 = v_006.rolling(5).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc142_10d_base_v142_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc142_10d_base_v142_signal

def f156g_f156_gross_profit_to_fcf_quality_calc143_21d_base_v143_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit - ncfo)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(126).kurt()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(63).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc143_21d_base_v143_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc143_21d_base_v143_signal

def f156g_f156_gross_profit_to_fcf_quality_calc144_10d_base_v144_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / gross_profit.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).skew()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(126).skew()
    v_009 = (v_008 - v_008.rolling(63).mean()) / v_008.rolling(63).std().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc144_10d_base_v144_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc144_10d_base_v144_signal

def f156g_f156_gross_profit_to_fcf_quality_calc145_10d_base_v145_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(252).rank(pct=True)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc145_10d_base_v145_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc145_10d_base_v145_signal

def f156g_f156_gross_profit_to_fcf_quality_calc146_126d_base_v146_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (revenue.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = v_005.rolling(63).std()
    v_007 = v_006.rolling(126).rank(pct=True)
    v_008 = (v_007 - v_007.rolling(252).mean()) / v_007.rolling(252).std().replace(0, np.nan)
    v_009 = v_008.rolling(252).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc146_126d_base_v146_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc146_126d_base_v146_signal

def f156g_f156_gross_profit_to_fcf_quality_calc147_63d_base_v147_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit.replace(0, np.nan) / free_cash_flow.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).max()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).kurt()
    v_008 = v_007.rolling(63).std()
    v_009 = v_008.rolling(10).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc147_63d_base_v147_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc147_63d_base_v147_signal

def f156g_f156_gross_profit_to_fcf_quality_calc148_63d_base_v148_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (free_cash_flow.replace(0, np.nan) / gross_profit.replace(0, np.nan))
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(10).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc148_63d_base_v148_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc148_63d_base_v148_signal

def f156g_f156_gross_profit_to_fcf_quality_calc149_21d_base_v149_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (gross_profit + revenue)
    v_002 = v_001.rolling(21).min()
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(21).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc149_21d_base_v149_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc149_21d_base_v149_signal

def f156g_f156_gross_profit_to_fcf_quality_calc150_126d_base_v150_signal(free_cash_flow, gross_profit, ncfo, revenue):
    v_001 = (ncfo - gross_profit)
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(21).skew()
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(21).rank(pct=True)
    v_008 = v_007.rolling(10).std()
    v_009 = v_008.rolling(42).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f156g_f156_gross_profit_to_fcf_quality_calc150_126d_base_v150_signal'] = f156g_f156_gross_profit_to_fcf_quality_calc150_126d_base_v150_signal


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
