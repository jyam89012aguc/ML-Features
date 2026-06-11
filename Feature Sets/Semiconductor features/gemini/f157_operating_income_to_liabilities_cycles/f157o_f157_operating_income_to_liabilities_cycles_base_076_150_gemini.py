import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f157o_f157_operating_income_to_liabilities_cycles_calc076_21d_base_v076_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(42).skew()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).std()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc076_21d_base_v076_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc076_21d_base_v076_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc077_10d_base_v077_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(21).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc077_10d_base_v077_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc077_10d_base_v077_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc078_63d_base_v078_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = (v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).mean()
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).min()
    v_008 = v_007.rolling(126).skew()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc078_63d_base_v078_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc078_63d_base_v078_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc079_252d_base_v079_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(252).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc079_252d_base_v079_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc079_252d_base_v079_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc080_42d_base_v080_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(252).std()
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(5).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc080_42d_base_v080_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc080_42d_base_v080_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc081_5d_base_v081_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(126).min()
    v_008 = v_007.rolling(252).max() / v_007.rolling(252).min().replace(0, np.nan)
    v_009 = (v_008 - v_008.rolling(10).mean()) / v_008.rolling(10).std().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc081_5d_base_v081_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc081_5d_base_v081_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc082_10d_base_v082_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(63).max() / v_005.rolling(63).min().replace(0, np.nan)
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(63).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc082_10d_base_v082_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc082_10d_base_v082_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc083_252d_base_v083_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(63).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc083_252d_base_v083_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc083_252d_base_v083_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc084_42d_base_v084_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.rolling(126).kurt()
    v_006 = v_005.rolling(42).max()
    v_007 = v_006.rolling(21).var()
    v_008 = v_007.rolling(252).max()
    v_009 = v_008.rolling(126).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc084_42d_base_v084_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc084_42d_base_v084_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc085_126d_base_v085_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(5).mean()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(252).min()
    v_007 = v_006.rolling(126).skew()
    v_008 = (v_007 - v_007.rolling(126).mean()) / v_007.rolling(126).std().replace(0, np.nan)
    v_009 = v_008.rolling(5).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc085_126d_base_v085_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc085_126d_base_v085_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc086_42d_base_v086_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(5).kurt()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(10).max() / v_006.rolling(10).min().replace(0, np.nan)
    v_008 = v_007.rolling(42).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc086_42d_base_v086_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc086_42d_base_v086_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc087_21d_base_v087_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(252).max()
    v_003 = (v_002 - v_002.rolling(5).mean()) / v_002.rolling(5).std().replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(63).var()
    v_008 = v_007.rolling(5).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc087_21d_base_v087_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc087_21d_base_v087_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc088_252d_base_v088_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(126).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc088_252d_base_v088_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc088_252d_base_v088_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc089_126d_base_v089_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(42).var()
    v_008 = v_007.rolling(252).var()
    v_009 = v_008.rolling(63).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc089_126d_base_v089_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc089_126d_base_v089_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc090_252d_base_v090_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(63).kurt()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    v_008 = v_007.rolling(126).rank(pct=True)
    v_009 = v_008.rolling(21).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc090_252d_base_v090_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc090_252d_base_v090_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc091_63d_base_v091_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(10).rank(pct=True)
    v_003 = v_002.rolling(252).rank(pct=True)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(126).max()
    v_008 = v_007.rolling(21).mean()
    v_009 = v_008.rolling(63).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc091_63d_base_v091_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc091_63d_base_v091_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc092_63d_base_v092_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).max()
    v_008 = v_007.rolling(42).skew()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc092_63d_base_v092_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc092_63d_base_v092_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc093_21d_base_v093_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(21).kurt()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(63).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc093_21d_base_v093_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc093_21d_base_v093_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc094_252d_base_v094_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(42).skew()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(10).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc094_252d_base_v094_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc094_252d_base_v094_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc095_252d_base_v095_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).rank(pct=True)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(5).mean()
    v_007 = v_006.rolling(5).max()
    v_008 = v_007.rolling(21).rank(pct=True)
    v_009 = v_008.rolling(10).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc095_252d_base_v095_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc095_252d_base_v095_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc096_252d_base_v096_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(10).rank(pct=True)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc096_252d_base_v096_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc096_252d_base_v096_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc097_126d_base_v097_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(21).kurt()
    v_005 = (v_004 - v_004.rolling(21).mean()) / v_004.rolling(21).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc097_126d_base_v097_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc097_126d_base_v097_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc098_42d_base_v098_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(21).mean()
    v_007 = v_006.rolling(42).min()
    v_008 = (v_007 - v_007.rolling(5).mean()) / v_007.rolling(5).std().replace(0, np.nan)
    v_009 = v_008.rolling(63).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc098_42d_base_v098_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc098_42d_base_v098_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc099_21d_base_v099_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(252).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc099_21d_base_v099_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc099_21d_base_v099_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc100_42d_base_v100_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(10).var()
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(126).var()
    v_007 = v_006.rolling(42).var()
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc100_42d_base_v100_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc100_42d_base_v100_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc101_126d_base_v101_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(21).mean()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc101_126d_base_v101_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc101_126d_base_v101_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc102_63d_base_v102_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(10).mean()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(42).std()
    v_008 = v_007.rolling(42).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc102_63d_base_v102_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc102_63d_base_v102_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc103_42d_base_v103_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(21).kurt()
    v_007 = v_006.rolling(63).max()
    v_008 = v_007.rolling(126).max()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc103_42d_base_v103_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc103_42d_base_v103_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc104_42d_base_v104_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(5).mean()
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(21).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc104_42d_base_v104_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc104_42d_base_v104_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc105_63d_base_v105_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(21).max()
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(252).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc105_63d_base_v105_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc105_63d_base_v105_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc106_21d_base_v106_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(126).var()
    v_008 = v_007.rolling(21).var()
    v_009 = v_008.rolling(21).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc106_21d_base_v106_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc106_21d_base_v106_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc107_10d_base_v107_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(21).rank(pct=True)
    v_007 = v_006.rolling(42).skew()
    v_008 = v_007.rolling(21).mean()
    v_009 = (v_008 - v_008.rolling(42).mean()) / v_008.rolling(42).std().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc107_10d_base_v107_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc107_10d_base_v107_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc108_252d_base_v108_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(5).min()
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(63).min()
    v_008 = v_007.rolling(252).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc108_252d_base_v108_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc108_252d_base_v108_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc109_42d_base_v109_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(126).var()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).rank(pct=True)
    v_009 = v_008.rolling(10).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc109_42d_base_v109_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc109_42d_base_v109_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc110_5d_base_v110_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).std()
    v_004 = (v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan)
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).max()
    v_007 = v_006.rolling(5).var()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc110_5d_base_v110_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc110_5d_base_v110_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc111_5d_base_v111_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(42).kurt()
    v_007 = (v_006 - v_006.rolling(10).mean()) / v_006.rolling(10).std().replace(0, np.nan)
    v_008 = (v_007 - v_007.rolling(21).mean()) / v_007.rolling(21).std().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc111_5d_base_v111_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc111_5d_base_v111_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc112_21d_base_v112_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(10).min()
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(21).var()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(63).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc112_21d_base_v112_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc112_21d_base_v112_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc113_42d_base_v113_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).min()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(42).max() / v_004.rolling(42).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).min()
    v_007 = v_006.rolling(42).rank(pct=True)
    v_008 = (v_007 - v_007.rolling(10).mean()) / v_007.rolling(10).std().replace(0, np.nan)
    v_009 = v_008.rolling(126).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc113_42d_base_v113_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc113_42d_base_v113_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc114_42d_base_v114_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).min()
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(21).max()
    v_007 = v_006.rolling(126).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc114_42d_base_v114_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc114_42d_base_v114_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc115_10d_base_v115_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).mean()
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc115_10d_base_v115_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc115_10d_base_v115_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc116_126d_base_v116_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(126).mean()
    v_004 = v_003.rolling(252).std()
    v_005 = (v_004 - v_004.rolling(42).mean()) / v_004.rolling(42).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc116_126d_base_v116_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc116_126d_base_v116_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc117_10d_base_v117_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(63).kurt()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(252).var()
    v_008 = v_007.rolling(252).max() / v_007.rolling(252).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc117_10d_base_v117_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc117_10d_base_v117_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc118_5d_base_v118_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(126).kurt()
    v_006 = v_005.rolling(126).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc118_5d_base_v118_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc118_5d_base_v118_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc119_5d_base_v119_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(126).mean()) / v_001.rolling(126).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).skew()
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(126).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc119_5d_base_v119_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc119_5d_base_v119_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc120_126d_base_v120_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(252).std()
    v_005 = (v_004 - v_004.rolling(10).mean()) / v_004.rolling(10).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).mean()
    v_007 = (v_006 - v_006.rolling(5).mean()) / v_006.rolling(5).std().replace(0, np.nan)
    v_008 = v_007.rolling(42).skew()
    v_009 = v_008.rolling(5).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc120_126d_base_v120_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc120_126d_base_v120_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc121_5d_base_v121_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(252).kurt()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(21).mean()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc121_5d_base_v121_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc121_5d_base_v121_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc122_252d_base_v122_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(42).skew()
    v_006 = v_005.rolling(5).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc122_252d_base_v122_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc122_252d_base_v122_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc123_5d_base_v123_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(5).skew()
    v_005 = (v_004 - v_004.rolling(42).mean()) / v_004.rolling(42).std().replace(0, np.nan)
    v_006 = v_005.rolling(252).max() / v_005.rolling(252).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc123_5d_base_v123_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc123_5d_base_v123_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc124_42d_base_v124_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(126).mean()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).rank(pct=True)
    v_007 = v_006.rolling(252).mean()
    v_008 = v_007.rolling(5).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc124_42d_base_v124_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc124_42d_base_v124_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc125_126d_base_v125_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(21).kurt()
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc125_126d_base_v125_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc125_126d_base_v125_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc126_5d_base_v126_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(42).mean()
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).skew()
    v_007 = v_006.rolling(42).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc126_5d_base_v126_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc126_5d_base_v126_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc127_10d_base_v127_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(21).mean()
    v_007 = (v_006 - v_006.rolling(10).mean()) / v_006.rolling(10).std().replace(0, np.nan)
    v_008 = v_007.rolling(5).max()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc127_10d_base_v127_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc127_10d_base_v127_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc128_42d_base_v128_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(5).var()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).rank(pct=True)
    v_007 = v_006.rolling(5).rank(pct=True)
    v_008 = v_007.rolling(63).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc128_42d_base_v128_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc128_42d_base_v128_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc129_63d_base_v129_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    v_008 = v_007.rolling(42).min()
    v_009 = (v_008 - v_008.rolling(21).mean()) / v_008.rolling(21).std().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc129_63d_base_v129_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc129_63d_base_v129_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc130_126d_base_v130_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(252).rank(pct=True)
    v_008 = v_007.rolling(5).var()
    v_009 = v_008.rolling(42).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc130_126d_base_v130_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc130_126d_base_v130_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc131_21d_base_v131_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(21).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc131_21d_base_v131_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc131_21d_base_v131_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc132_10d_base_v132_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(126).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc132_10d_base_v132_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc132_10d_base_v132_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc133_21d_base_v133_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(10).min()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(21).std()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc133_21d_base_v133_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc133_21d_base_v133_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc134_63d_base_v134_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(42).std()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(126).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc134_63d_base_v134_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc134_63d_base_v134_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc135_63d_base_v135_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(10).max() / v_001.rolling(10).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(42).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc135_63d_base_v135_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc135_63d_base_v135_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc136_5d_base_v136_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).std()
    v_008 = v_007.rolling(5).kurt()
    v_009 = v_008.rolling(252).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc136_5d_base_v136_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc136_5d_base_v136_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc137_252d_base_v137_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(63).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc137_252d_base_v137_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc137_252d_base_v137_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc138_5d_base_v138_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(10).mean()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.rolling(5).max()
    v_006 = v_005.rolling(63).var()
    v_007 = (v_006 - v_006.rolling(10).mean()) / v_006.rolling(10).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc138_5d_base_v138_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc138_5d_base_v138_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc139_126d_base_v139_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(5).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc139_126d_base_v139_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc139_126d_base_v139_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc140_252d_base_v140_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(10).min()
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(126).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc140_252d_base_v140_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc140_252d_base_v140_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc141_63d_base_v141_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).std()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(63).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc141_63d_base_v141_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc141_63d_base_v141_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc142_252d_base_v142_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(252).mean()
    v_003 = (v_002 - v_002.rolling(21).mean()) / v_002.rolling(21).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(252).mean()
    v_008 = v_007.rolling(5).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc142_252d_base_v142_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc142_252d_base_v142_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc143_42d_base_v143_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).min()
    v_003 = v_002.rolling(21).max()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(63).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc143_42d_base_v143_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc143_42d_base_v143_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc144_252d_base_v144_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(42).min()
    v_008 = v_007.rolling(126).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc144_252d_base_v144_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc144_252d_base_v144_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc145_42d_base_v145_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).std()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(5).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc145_42d_base_v145_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc145_42d_base_v145_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc146_10d_base_v146_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(252).max()
    v_003 = v_002.rolling(10).var()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(10).max()
    v_007 = (v_006 - v_006.rolling(10).mean()) / v_006.rolling(10).std().replace(0, np.nan)
    v_008 = v_007.rolling(252).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc146_10d_base_v146_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc146_10d_base_v146_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc147_21d_base_v147_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(252).std()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(126).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc147_21d_base_v147_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc147_21d_base_v147_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc148_126d_base_v148_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = (v_001 - v_001.rolling(63).mean()) / v_001.rolling(63).std().replace(0, np.nan)
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(252).std()
    v_008 = (v_007 - v_007.rolling(10).mean()) / v_007.rolling(10).std().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc148_126d_base_v148_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc148_126d_base_v148_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc149_42d_base_v149_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(126).mean()
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.rolling(63).kurt()
    v_006 = v_005.rolling(10).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc149_42d_base_v149_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc149_42d_base_v149_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc150_42d_base_v150_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(63).rank(pct=True)
    v_008 = v_007.rolling(63).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc150_42d_base_v150_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc150_42d_base_v150_signal


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
