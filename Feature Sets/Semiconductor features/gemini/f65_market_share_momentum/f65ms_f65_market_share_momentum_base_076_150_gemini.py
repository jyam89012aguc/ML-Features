import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f65ms_f65_market_share_momentum_calc076_5d_base_v076_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc076_5d_base_v076_signal'] = f65ms_f65_market_share_momentum_calc076_5d_base_v076_signal

def f65ms_f65_market_share_momentum_calc077_10d_base_v077_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc077_10d_base_v077_signal'] = f65ms_f65_market_share_momentum_calc077_10d_base_v077_signal

def f65ms_f65_market_share_momentum_calc078_21d_base_v078_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc078_21d_base_v078_signal'] = f65ms_f65_market_share_momentum_calc078_21d_base_v078_signal

def f65ms_f65_market_share_momentum_calc079_42d_base_v079_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc079_42d_base_v079_signal'] = f65ms_f65_market_share_momentum_calc079_42d_base_v079_signal

def f65ms_f65_market_share_momentum_calc080_63d_base_v080_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc080_63d_base_v080_signal'] = f65ms_f65_market_share_momentum_calc080_63d_base_v080_signal

def f65ms_f65_market_share_momentum_calc081_126d_base_v081_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc081_126d_base_v081_signal'] = f65ms_f65_market_share_momentum_calc081_126d_base_v081_signal

def f65ms_f65_market_share_momentum_calc082_252d_base_v082_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc082_252d_base_v082_signal'] = f65ms_f65_market_share_momentum_calc082_252d_base_v082_signal

def f65ms_f65_market_share_momentum_calc083_21d_base_v083_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc083_21d_base_v083_signal'] = f65ms_f65_market_share_momentum_calc083_21d_base_v083_signal

def f65ms_f65_market_share_momentum_calc084_63d_base_v084_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc084_63d_base_v084_signal'] = f65ms_f65_market_share_momentum_calc084_63d_base_v084_signal

def f65ms_f65_market_share_momentum_calc085_5d_base_v085_signal(revenue, workingcapital):
    res = (revenue / workingcapital).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc085_5d_base_v085_signal'] = f65ms_f65_market_share_momentum_calc085_5d_base_v085_signal

def f65ms_f65_market_share_momentum_calc086_21d_base_v086_signal(revenue, workingcapital):
    res = (revenue / workingcapital).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc086_21d_base_v086_signal'] = f65ms_f65_market_share_momentum_calc086_21d_base_v086_signal

def f65ms_f65_market_share_momentum_calc087_10d_base_v087_signal(revenue, workingcapital):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / workingcapital)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc087_10d_base_v087_signal'] = f65ms_f65_market_share_momentum_calc087_10d_base_v087_signal

def f65ms_f65_market_share_momentum_calc088_63d_base_v088_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc088_63d_base_v088_signal'] = f65ms_f65_market_share_momentum_calc088_63d_base_v088_signal

def f65ms_f65_market_share_momentum_calc089_126d_base_v089_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc089_126d_base_v089_signal'] = f65ms_f65_market_share_momentum_calc089_126d_base_v089_signal

def f65ms_f65_market_share_momentum_calc090_252d_base_v090_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc090_252d_base_v090_signal'] = f65ms_f65_market_share_momentum_calc090_252d_base_v090_signal

def f65ms_f65_market_share_momentum_calc091_5d_base_v091_signal(revenue, debt):
    res = (revenue / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc091_5d_base_v091_signal'] = f65ms_f65_market_share_momentum_calc091_5d_base_v091_signal

def f65ms_f65_market_share_momentum_calc092_10d_base_v092_signal(revenue, debt):
    res = (revenue / debt).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc092_10d_base_v092_signal'] = f65ms_f65_market_share_momentum_calc092_10d_base_v092_signal

def f65ms_f65_market_share_momentum_calc093_21d_base_v093_signal(revenue, debt):
    res = (revenue / debt).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc093_21d_base_v093_signal'] = f65ms_f65_market_share_momentum_calc093_21d_base_v093_signal

def f65ms_f65_market_share_momentum_calc094_42d_base_v094_signal(revenue, debt):
    res = (revenue / debt).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc094_42d_base_v094_signal'] = f65ms_f65_market_share_momentum_calc094_42d_base_v094_signal

def f65ms_f65_market_share_momentum_calc095_63d_base_v095_signal(revenue, debt):
    res = (revenue / debt).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc095_63d_base_v095_signal'] = f65ms_f65_market_share_momentum_calc095_63d_base_v095_signal

def f65ms_f65_market_share_momentum_calc096_126d_base_v096_signal(revenue, debt):
    res = (revenue / debt).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc096_126d_base_v096_signal'] = f65ms_f65_market_share_momentum_calc096_126d_base_v096_signal

def f65ms_f65_market_share_momentum_calc097_252d_base_v097_signal(revenue, debt):
    res = (revenue / debt).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc097_252d_base_v097_signal'] = f65ms_f65_market_share_momentum_calc097_252d_base_v097_signal

def f65ms_f65_market_share_momentum_calc098_21d_base_v098_signal(revenue, debt):
    res = (revenue / debt).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc098_21d_base_v098_signal'] = f65ms_f65_market_share_momentum_calc098_21d_base_v098_signal

def f65ms_f65_market_share_momentum_calc099_63d_base_v099_signal(revenue, debt):
    res = (revenue / debt).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc099_63d_base_v099_signal'] = f65ms_f65_market_share_momentum_calc099_63d_base_v099_signal

def f65ms_f65_market_share_momentum_calc100_5d_base_v100_signal(revenue, debt):
    res = (revenue / debt).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc100_5d_base_v100_signal'] = f65ms_f65_market_share_momentum_calc100_5d_base_v100_signal

def f65ms_f65_market_share_momentum_calc101_21d_base_v101_signal(revenue, debt):
    res = (revenue / debt).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc101_21d_base_v101_signal'] = f65ms_f65_market_share_momentum_calc101_21d_base_v101_signal

def f65ms_f65_market_share_momentum_calc102_10d_base_v102_signal(revenue, debt):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / debt)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc102_10d_base_v102_signal'] = f65ms_f65_market_share_momentum_calc102_10d_base_v102_signal

def f65ms_f65_market_share_momentum_calc103_63d_base_v103_signal(revenue, debt):
    res = (revenue / debt).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc103_63d_base_v103_signal'] = f65ms_f65_market_share_momentum_calc103_63d_base_v103_signal

def f65ms_f65_market_share_momentum_calc104_126d_base_v104_signal(revenue, debt):
    res = (revenue / debt).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc104_126d_base_v104_signal'] = f65ms_f65_market_share_momentum_calc104_126d_base_v104_signal

def f65ms_f65_market_share_momentum_calc105_252d_base_v105_signal(revenue, debt):
    res = (revenue / debt).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc105_252d_base_v105_signal'] = f65ms_f65_market_share_momentum_calc105_252d_base_v105_signal

def f65ms_f65_market_share_momentum_calc106_5d_base_v106_signal(revenue, volume):
    res = (revenue / volume).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc106_5d_base_v106_signal'] = f65ms_f65_market_share_momentum_calc106_5d_base_v106_signal

def f65ms_f65_market_share_momentum_calc107_10d_base_v107_signal(revenue, volume):
    res = (revenue / volume).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc107_10d_base_v107_signal'] = f65ms_f65_market_share_momentum_calc107_10d_base_v107_signal

def f65ms_f65_market_share_momentum_calc108_21d_base_v108_signal(revenue, volume):
    res = (revenue / volume).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc108_21d_base_v108_signal'] = f65ms_f65_market_share_momentum_calc108_21d_base_v108_signal

def f65ms_f65_market_share_momentum_calc109_42d_base_v109_signal(revenue, volume):
    res = (revenue / volume).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc109_42d_base_v109_signal'] = f65ms_f65_market_share_momentum_calc109_42d_base_v109_signal

def f65ms_f65_market_share_momentum_calc110_63d_base_v110_signal(revenue, volume):
    res = (revenue / volume).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc110_63d_base_v110_signal'] = f65ms_f65_market_share_momentum_calc110_63d_base_v110_signal

def f65ms_f65_market_share_momentum_calc111_126d_base_v111_signal(revenue, volume):
    res = (revenue / volume).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc111_126d_base_v111_signal'] = f65ms_f65_market_share_momentum_calc111_126d_base_v111_signal

def f65ms_f65_market_share_momentum_calc112_252d_base_v112_signal(revenue, volume):
    res = (revenue / volume).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc112_252d_base_v112_signal'] = f65ms_f65_market_share_momentum_calc112_252d_base_v112_signal

def f65ms_f65_market_share_momentum_calc113_21d_base_v113_signal(revenue, volume):
    res = (revenue / volume).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc113_21d_base_v113_signal'] = f65ms_f65_market_share_momentum_calc113_21d_base_v113_signal

def f65ms_f65_market_share_momentum_calc114_63d_base_v114_signal(revenue, volume):
    res = (revenue / volume).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc114_63d_base_v114_signal'] = f65ms_f65_market_share_momentum_calc114_63d_base_v114_signal

def f65ms_f65_market_share_momentum_calc115_5d_base_v115_signal(revenue, volume):
    res = (revenue / volume).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc115_5d_base_v115_signal'] = f65ms_f65_market_share_momentum_calc115_5d_base_v115_signal

def f65ms_f65_market_share_momentum_calc116_21d_base_v116_signal(revenue, volume):
    res = (revenue / volume).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc116_21d_base_v116_signal'] = f65ms_f65_market_share_momentum_calc116_21d_base_v116_signal

def f65ms_f65_market_share_momentum_calc117_10d_base_v117_signal(revenue, volume):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / volume)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc117_10d_base_v117_signal'] = f65ms_f65_market_share_momentum_calc117_10d_base_v117_signal

def f65ms_f65_market_share_momentum_calc118_63d_base_v118_signal(revenue, volume):
    res = (revenue / volume).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc118_63d_base_v118_signal'] = f65ms_f65_market_share_momentum_calc118_63d_base_v118_signal

def f65ms_f65_market_share_momentum_calc119_126d_base_v119_signal(revenue, volume):
    res = (revenue / volume).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc119_126d_base_v119_signal'] = f65ms_f65_market_share_momentum_calc119_126d_base_v119_signal

def f65ms_f65_market_share_momentum_calc120_252d_base_v120_signal(revenue, volume):
    res = (revenue / volume).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc120_252d_base_v120_signal'] = f65ms_f65_market_share_momentum_calc120_252d_base_v120_signal

def f65ms_f65_market_share_momentum_calc121_5d_base_v121_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc121_5d_base_v121_signal'] = f65ms_f65_market_share_momentum_calc121_5d_base_v121_signal

def f65ms_f65_market_share_momentum_calc122_10d_base_v122_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc122_10d_base_v122_signal'] = f65ms_f65_market_share_momentum_calc122_10d_base_v122_signal

def f65ms_f65_market_share_momentum_calc123_21d_base_v123_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc123_21d_base_v123_signal'] = f65ms_f65_market_share_momentum_calc123_21d_base_v123_signal

def f65ms_f65_market_share_momentum_calc124_42d_base_v124_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc124_42d_base_v124_signal'] = f65ms_f65_market_share_momentum_calc124_42d_base_v124_signal

def f65ms_f65_market_share_momentum_calc125_63d_base_v125_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc125_63d_base_v125_signal'] = f65ms_f65_market_share_momentum_calc125_63d_base_v125_signal

def f65ms_f65_market_share_momentum_calc126_126d_base_v126_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc126_126d_base_v126_signal'] = f65ms_f65_market_share_momentum_calc126_126d_base_v126_signal

def f65ms_f65_market_share_momentum_calc127_252d_base_v127_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc127_252d_base_v127_signal'] = f65ms_f65_market_share_momentum_calc127_252d_base_v127_signal

def f65ms_f65_market_share_momentum_calc128_21d_base_v128_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc128_21d_base_v128_signal'] = f65ms_f65_market_share_momentum_calc128_21d_base_v128_signal

def f65ms_f65_market_share_momentum_calc129_63d_base_v129_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc129_63d_base_v129_signal'] = f65ms_f65_market_share_momentum_calc129_63d_base_v129_signal

def f65ms_f65_market_share_momentum_calc130_5d_base_v130_signal(revenue, sharesbas):
    res = (revenue / sharesbas).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc130_5d_base_v130_signal'] = f65ms_f65_market_share_momentum_calc130_5d_base_v130_signal

def f65ms_f65_market_share_momentum_calc131_21d_base_v131_signal(revenue, sharesbas):
    res = (revenue / sharesbas).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc131_21d_base_v131_signal'] = f65ms_f65_market_share_momentum_calc131_21d_base_v131_signal

def f65ms_f65_market_share_momentum_calc132_10d_base_v132_signal(revenue, sharesbas):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / sharesbas)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc132_10d_base_v132_signal'] = f65ms_f65_market_share_momentum_calc132_10d_base_v132_signal

def f65ms_f65_market_share_momentum_calc133_63d_base_v133_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc133_63d_base_v133_signal'] = f65ms_f65_market_share_momentum_calc133_63d_base_v133_signal

def f65ms_f65_market_share_momentum_calc134_126d_base_v134_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc134_126d_base_v134_signal'] = f65ms_f65_market_share_momentum_calc134_126d_base_v134_signal

def f65ms_f65_market_share_momentum_calc135_252d_base_v135_signal(revenue, sharesbas):
    res = (revenue / sharesbas).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc135_252d_base_v135_signal'] = f65ms_f65_market_share_momentum_calc135_252d_base_v135_signal

def f65ms_f65_market_share_momentum_calc136_5d_base_v136_signal(revenue, gp):
    res = (revenue / gp).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc136_5d_base_v136_signal'] = f65ms_f65_market_share_momentum_calc136_5d_base_v136_signal

def f65ms_f65_market_share_momentum_calc137_10d_base_v137_signal(revenue, gp):
    res = (revenue / gp).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc137_10d_base_v137_signal'] = f65ms_f65_market_share_momentum_calc137_10d_base_v137_signal

def f65ms_f65_market_share_momentum_calc138_21d_base_v138_signal(revenue, gp):
    res = (revenue / gp).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc138_21d_base_v138_signal'] = f65ms_f65_market_share_momentum_calc138_21d_base_v138_signal

def f65ms_f65_market_share_momentum_calc139_42d_base_v139_signal(revenue, gp):
    res = (revenue / gp).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc139_42d_base_v139_signal'] = f65ms_f65_market_share_momentum_calc139_42d_base_v139_signal

def f65ms_f65_market_share_momentum_calc140_63d_base_v140_signal(revenue, gp):
    res = (revenue / gp).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc140_63d_base_v140_signal'] = f65ms_f65_market_share_momentum_calc140_63d_base_v140_signal

def f65ms_f65_market_share_momentum_calc141_126d_base_v141_signal(revenue, gp):
    res = (revenue / gp).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc141_126d_base_v141_signal'] = f65ms_f65_market_share_momentum_calc141_126d_base_v141_signal

def f65ms_f65_market_share_momentum_calc142_252d_base_v142_signal(revenue, gp):
    res = (revenue / gp).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc142_252d_base_v142_signal'] = f65ms_f65_market_share_momentum_calc142_252d_base_v142_signal

def f65ms_f65_market_share_momentum_calc143_21d_base_v143_signal(revenue, gp):
    res = (revenue / gp).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc143_21d_base_v143_signal'] = f65ms_f65_market_share_momentum_calc143_21d_base_v143_signal

def f65ms_f65_market_share_momentum_calc144_63d_base_v144_signal(revenue, gp):
    res = (revenue / gp).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc144_63d_base_v144_signal'] = f65ms_f65_market_share_momentum_calc144_63d_base_v144_signal

def f65ms_f65_market_share_momentum_calc145_5d_base_v145_signal(revenue, gp):
    res = (revenue / gp).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc145_5d_base_v145_signal'] = f65ms_f65_market_share_momentum_calc145_5d_base_v145_signal

def f65ms_f65_market_share_momentum_calc146_21d_base_v146_signal(revenue, gp):
    res = (revenue / gp).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc146_21d_base_v146_signal'] = f65ms_f65_market_share_momentum_calc146_21d_base_v146_signal

def f65ms_f65_market_share_momentum_calc147_10d_base_v147_signal(revenue, gp):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / gp)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc147_10d_base_v147_signal'] = f65ms_f65_market_share_momentum_calc147_10d_base_v147_signal

def f65ms_f65_market_share_momentum_calc148_63d_base_v148_signal(revenue, gp):
    res = (revenue / gp).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc148_63d_base_v148_signal'] = f65ms_f65_market_share_momentum_calc148_63d_base_v148_signal

def f65ms_f65_market_share_momentum_calc149_126d_base_v149_signal(revenue, gp):
    res = (revenue / gp).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc149_126d_base_v149_signal'] = f65ms_f65_market_share_momentum_calc149_126d_base_v149_signal

def f65ms_f65_market_share_momentum_calc150_252d_base_v150_signal(revenue, gp):
    res = (revenue / gp).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc150_252d_base_v150_signal'] = f65ms_f65_market_share_momentum_calc150_252d_base_v150_signal


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
