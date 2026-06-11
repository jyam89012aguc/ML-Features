import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f202e_f202_ebitda_per_share_growth_regime_calc076_42d_base_v076_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 7.2278)).rolling(6).max().pct_change(40).rolling(44).min().rolling(10).min() * 0.292182
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc076_42d_base_v076_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc076_42d_base_v076_signal

def f202e_f202_ebitda_per_share_growth_regime_calc077_126d_base_v077_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 9.8816)).rolling(6).min().diff(49) * 0.684408
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc077_126d_base_v077_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc077_126d_base_v077_signal

def f202e_f202_ebitda_per_share_growth_regime_calc078_84d_base_v078_signal(ebitda, sharesbas):
    res = (ebitda * 9.5324 - sharesbas).rolling(5).std().rolling(33).max().pct_change(39) * 0.998538
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc078_84d_base_v078_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc078_84d_base_v078_signal

def f202e_f202_ebitda_per_share_growth_regime_calc079_10d_base_v079_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(34).rolling(12).mean() * 0.292946
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc079_10d_base_v079_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc079_10d_base_v079_signal

def f202e_f202_ebitda_per_share_growth_regime_calc080_5d_base_v080_signal(ebitda, sharesbas):
    res = (ebitda.diff(8) / (sharesbas.shift(1) + 2.6220)).rolling(42).min().pct_change(16).pct_change(50).rolling(30).var() * 0.643748
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc080_5d_base_v080_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc080_5d_base_v080_signal

def f202e_f202_ebitda_per_share_growth_regime_calc081_5d_base_v081_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 7.6945)).diff(32).diff(22) * 0.642999
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc081_5d_base_v081_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc081_5d_base_v081_signal

def f202e_f202_ebitda_per_share_growth_regime_calc082_252d_base_v082_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(10).min().rolling(9).max().pct_change(13).rolling(46).max() * 0.513071
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc082_252d_base_v082_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc082_252d_base_v082_signal

def f202e_f202_ebitda_per_share_growth_regime_calc083_42d_base_v083_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(2).min().rolling(45).var().rolling(5).mean().rolling(28).var() * 0.457990
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc083_42d_base_v083_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc083_42d_base_v083_signal

def f202e_f202_ebitda_per_share_growth_regime_calc084_252d_base_v084_signal(ebitda, sharesbas):
    res = (ebitda * 0.3435 - sharesbas).diff(8).pct_change(2).rolling(19).max().diff(48) * 0.404262
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc084_252d_base_v084_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc084_252d_base_v084_signal

def f202e_f202_ebitda_per_share_growth_regime_calc085_200d_base_v085_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(8).mean().rolling(14).var().diff(24) * 0.232677
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc085_200d_base_v085_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc085_200d_base_v085_signal

def f202e_f202_ebitda_per_share_growth_regime_calc086_252d_base_v086_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 4.4397)).rolling(6).var().rolling(48).min().rolling(38).min() * 0.312266
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc086_252d_base_v086_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc086_252d_base_v086_signal

def f202e_f202_ebitda_per_share_growth_regime_calc087_150d_base_v087_signal(ebitda, sharesbas):
    res = (ebitda * 7.2989 - sharesbas).pct_change(9).rolling(46).min().rolling(46).min() * 0.266015
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc087_150d_base_v087_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc087_150d_base_v087_signal

def f202e_f202_ebitda_per_share_growth_regime_calc088_105d_base_v088_signal(ebitda, sharesbas):
    res = (ebitda.diff(5) / (sharesbas.shift(5) + 8.8778)).rolling(31).var().rolling(42).var().diff(27) * 0.854739
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc088_105d_base_v088_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc088_105d_base_v088_signal

def f202e_f202_ebitda_per_share_growth_regime_calc089_126d_base_v089_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.5372)).rolling(29).min().diff(41).diff(19).rolling(28).mean() * 0.869334
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc089_126d_base_v089_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc089_126d_base_v089_signal

def f202e_f202_ebitda_per_share_growth_regime_calc090_63d_base_v090_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 4.0662)).pct_change(14).rolling(15).var().pct_change(3) * 0.302708
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc090_63d_base_v090_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc090_63d_base_v090_signal

def f202e_f202_ebitda_per_share_growth_regime_calc091_252d_base_v091_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 1.5661)).rolling(37).mean().pct_change(46).diff(26) * 0.457289
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc091_252d_base_v091_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc091_252d_base_v091_signal

def f202e_f202_ebitda_per_share_growth_regime_calc092_63d_base_v092_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 6.0634)).diff(18).rolling(30).mean() * 0.372365
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc092_63d_base_v092_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc092_63d_base_v092_signal

def f202e_f202_ebitda_per_share_growth_regime_calc093_252d_base_v093_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.1968)).rolling(32).max().rolling(33).std().diff(47).rolling(41).min() * 0.679354
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc093_252d_base_v093_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc093_252d_base_v093_signal

def f202e_f202_ebitda_per_share_growth_regime_calc094_5d_base_v094_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 8.9806)).rolling(27).var().rolling(30).var().rolling(10).max() * 0.462439
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc094_5d_base_v094_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc094_5d_base_v094_signal

def f202e_f202_ebitda_per_share_growth_regime_calc095_150d_base_v095_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 3.4894)).rolling(38).var().rolling(47).min() * 0.087786
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc095_150d_base_v095_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc095_150d_base_v095_signal

def f202e_f202_ebitda_per_share_growth_regime_calc096_84d_base_v096_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(14).mean().rolling(27).var().rolling(18).max().pct_change(16) * 0.198153
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc096_84d_base_v096_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc096_84d_base_v096_signal

def f202e_f202_ebitda_per_share_growth_regime_calc097_5d_base_v097_signal(ebitda, sharesbas):
    res = (ebitda * 7.9768 - sharesbas).diff(2).rolling(11).max().rolling(6).mean() * 0.083546
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc097_5d_base_v097_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc097_5d_base_v097_signal

def f202e_f202_ebitda_per_share_growth_regime_calc098_126d_base_v098_signal(ebitda, sharesbas):
    res = (ebitda.diff(8) / (sharesbas.shift(2) + 4.6764)).diff(10).rolling(20).std() * 0.498394
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc098_126d_base_v098_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc098_126d_base_v098_signal

def f202e_f202_ebitda_per_share_growth_regime_calc099_252d_base_v099_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(19).max().pct_change(43).rolling(14).max().rolling(43).max() * 0.221035
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc099_252d_base_v099_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc099_252d_base_v099_signal

def f202e_f202_ebitda_per_share_growth_regime_calc100_10d_base_v100_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(6).min().diff(46) * 0.758126
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc100_10d_base_v100_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc100_10d_base_v100_signal

def f202e_f202_ebitda_per_share_growth_regime_calc101_150d_base_v101_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(3).max().rolling(49).var() * 0.029334
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc101_150d_base_v101_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc101_150d_base_v101_signal

def f202e_f202_ebitda_per_share_growth_regime_calc102_200d_base_v102_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.2397)).rolling(2).max().rolling(9).max().diff(40).diff(8) * 0.641298
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc102_200d_base_v102_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc102_200d_base_v102_signal

def f202e_f202_ebitda_per_share_growth_regime_calc103_5d_base_v103_signal(ebitda, sharesbas):
    res = (ebitda.diff(7) / (sharesbas.shift(5) + 8.9117)).rolling(48).mean().pct_change(5).rolling(23).min().pct_change(14) * 0.400548
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc103_5d_base_v103_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc103_5d_base_v103_signal

def f202e_f202_ebitda_per_share_growth_regime_calc104_42d_base_v104_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 6.1153)).rolling(11).std().rolling(45).min() * 0.165983
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc104_42d_base_v104_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc104_42d_base_v104_signal

def f202e_f202_ebitda_per_share_growth_regime_calc105_5d_base_v105_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 0.9750)).rolling(48).min().pct_change(26) * 0.098560
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc105_5d_base_v105_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc105_5d_base_v105_signal

def f202e_f202_ebitda_per_share_growth_regime_calc106_63d_base_v106_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 8.6105)).rolling(12).std().diff(10) * 0.347482
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc106_63d_base_v106_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc106_63d_base_v106_signal

def f202e_f202_ebitda_per_share_growth_regime_calc107_252d_base_v107_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 4.4685)).rolling(48).min().pct_change(47).diff(20) * 0.529691
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc107_252d_base_v107_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc107_252d_base_v107_signal

def f202e_f202_ebitda_per_share_growth_regime_calc108_252d_base_v108_signal(ebitda, sharesbas):
    res = (ebitda.diff(4) / (sharesbas.shift(5) + 8.9331)).rolling(6).std().pct_change(3).rolling(45).mean().pct_change(23) * 0.226971
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc108_252d_base_v108_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc108_252d_base_v108_signal

def f202e_f202_ebitda_per_share_growth_regime_calc109_105d_base_v109_signal(ebitda, sharesbas):
    res = (ebitda * 2.5299 - sharesbas).rolling(3).mean().rolling(23).mean().rolling(14).std().pct_change(21) * 0.015344
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc109_105d_base_v109_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc109_105d_base_v109_signal

def f202e_f202_ebitda_per_share_growth_regime_calc110_126d_base_v110_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 0.2280)).pct_change(3).rolling(33).min().pct_change(7).rolling(38).std() * 0.817997
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc110_126d_base_v110_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc110_126d_base_v110_signal

def f202e_f202_ebitda_per_share_growth_regime_calc111_5d_base_v111_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(13).max().rolling(24).var() * 0.239626
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc111_5d_base_v111_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc111_5d_base_v111_signal

def f202e_f202_ebitda_per_share_growth_regime_calc112_84d_base_v112_signal(ebitda, sharesbas):
    res = (ebitda * 4.5025 - sharesbas).diff(47).rolling(9).mean().pct_change(42) * 0.354548
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc112_84d_base_v112_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc112_84d_base_v112_signal

def f202e_f202_ebitda_per_share_growth_regime_calc113_252d_base_v113_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 7.6588)).rolling(33).var().rolling(18).mean().rolling(16).std() * 0.564408
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc113_252d_base_v113_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc113_252d_base_v113_signal

def f202e_f202_ebitda_per_share_growth_regime_calc114_150d_base_v114_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(23).mean().rolling(41).std().rolling(17).std().rolling(45).min() * 0.182160
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc114_150d_base_v114_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc114_150d_base_v114_signal

def f202e_f202_ebitda_per_share_growth_regime_calc115_5d_base_v115_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 0.5141)).pct_change(49).pct_change(43).diff(50).diff(30) * 0.690223
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc115_5d_base_v115_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc115_5d_base_v115_signal

def f202e_f202_ebitda_per_share_growth_regime_calc116_84d_base_v116_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 5.7739)).diff(6).diff(3).rolling(11).std().rolling(35).max() * 0.379858
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc116_84d_base_v116_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc116_84d_base_v116_signal

def f202e_f202_ebitda_per_share_growth_regime_calc117_63d_base_v117_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 3.2959)).rolling(19).max().rolling(47).max().rolling(30).mean() * 0.331781
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc117_63d_base_v117_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc117_63d_base_v117_signal

def f202e_f202_ebitda_per_share_growth_regime_calc118_105d_base_v118_signal(ebitda, sharesbas):
    res = (ebitda.diff(6) / (sharesbas.shift(4) + 4.5463)).rolling(8).min().rolling(50).var().rolling(21).max().rolling(4).mean() * 0.010362
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc118_105d_base_v118_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc118_105d_base_v118_signal

def f202e_f202_ebitda_per_share_growth_regime_calc119_200d_base_v119_signal(ebitda, sharesbas):
    res = (ebitda * 8.9425 - sharesbas).rolling(40).max().rolling(23).max().rolling(11).min() * 0.632488
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc119_200d_base_v119_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc119_200d_base_v119_signal

def f202e_f202_ebitda_per_share_growth_regime_calc120_84d_base_v120_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.6492)).rolling(6).var().rolling(31).mean().diff(40).rolling(14).mean() * 0.973401
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc120_84d_base_v120_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc120_84d_base_v120_signal

def f202e_f202_ebitda_per_share_growth_regime_calc121_5d_base_v121_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 1.6185)).rolling(36).var().rolling(44).var().rolling(31).max() * 0.295616
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc121_5d_base_v121_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc121_5d_base_v121_signal

def f202e_f202_ebitda_per_share_growth_regime_calc122_42d_base_v122_signal(ebitda, sharesbas):
    res = (ebitda * 8.8632 - sharesbas).diff(46).rolling(39).max() * 0.896671
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc122_42d_base_v122_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc122_42d_base_v122_signal

def f202e_f202_ebitda_per_share_growth_regime_calc123_10d_base_v123_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 2.8422)).diff(38).rolling(6).min().rolling(17).min().pct_change(25) * 0.985019
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc123_10d_base_v123_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc123_10d_base_v123_signal

def f202e_f202_ebitda_per_share_growth_regime_calc124_200d_base_v124_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 2.2323)).rolling(30).var().rolling(20).min().diff(27) * 0.783695
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc124_200d_base_v124_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc124_200d_base_v124_signal

def f202e_f202_ebitda_per_share_growth_regime_calc125_126d_base_v125_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(32).var().diff(35).diff(2) * 0.624130
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc125_126d_base_v125_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc125_126d_base_v125_signal

def f202e_f202_ebitda_per_share_growth_regime_calc126_5d_base_v126_signal(ebitda, sharesbas):
    res = (ebitda.diff(5) / (sharesbas.shift(4) + 9.9430)).rolling(49).var().diff(38).rolling(25).var().rolling(15).max() * 0.697639
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc126_5d_base_v126_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc126_5d_base_v126_signal

def f202e_f202_ebitda_per_share_growth_regime_calc127_126d_base_v127_signal(ebitda, sharesbas):
    res = (ebitda.diff(10) / (sharesbas.shift(3) + 7.4737)).rolling(23).mean().rolling(10).var().diff(49) * 0.915411
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc127_126d_base_v127_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc127_126d_base_v127_signal

def f202e_f202_ebitda_per_share_growth_regime_calc128_63d_base_v128_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 3.7942)).rolling(34).mean().rolling(5).max().diff(23) * 0.648583
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc128_63d_base_v128_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc128_63d_base_v128_signal

def f202e_f202_ebitda_per_share_growth_regime_calc129_200d_base_v129_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 5.4241)).diff(42).rolling(15).std().pct_change(11) * 0.598383
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc129_200d_base_v129_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc129_200d_base_v129_signal

def f202e_f202_ebitda_per_share_growth_regime_calc130_105d_base_v130_signal(ebitda, sharesbas):
    res = (ebitda.diff(3) / (sharesbas.shift(5) + 8.6377)).rolling(26).min().diff(19) * 0.922839
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc130_105d_base_v130_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc130_105d_base_v130_signal

def f202e_f202_ebitda_per_share_growth_regime_calc131_150d_base_v131_signal(ebitda, sharesbas):
    res = (ebitda.diff(5) / (sharesbas.shift(1) + 3.0458)).rolling(2).max().diff(19).rolling(38).std() * 0.369794
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc131_150d_base_v131_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc131_150d_base_v131_signal

def f202e_f202_ebitda_per_share_growth_regime_calc132_126d_base_v132_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 5.3225)).pct_change(12).pct_change(14).pct_change(39) * 0.740234
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc132_126d_base_v132_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc132_126d_base_v132_signal

def f202e_f202_ebitda_per_share_growth_regime_calc133_63d_base_v133_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(47).pct_change(16).diff(22) * 0.658780
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc133_63d_base_v133_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc133_63d_base_v133_signal

def f202e_f202_ebitda_per_share_growth_regime_calc134_5d_base_v134_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 9.7564)).pct_change(13).rolling(50).std().pct_change(14).pct_change(50) * 0.025805
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc134_5d_base_v134_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc134_5d_base_v134_signal

def f202e_f202_ebitda_per_share_growth_regime_calc135_10d_base_v135_signal(ebitda, sharesbas):
    res = (ebitda * 0.2178 - sharesbas).rolling(8).std().pct_change(32).diff(24) * 0.300086
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc135_10d_base_v135_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc135_10d_base_v135_signal

def f202e_f202_ebitda_per_share_growth_regime_calc136_21d_base_v136_signal(ebitda, sharesbas):
    res = (ebitda * 6.3763 - sharesbas).rolling(14).min().diff(12).diff(28).rolling(8).var() * 0.476119
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc136_21d_base_v136_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc136_21d_base_v136_signal

def f202e_f202_ebitda_per_share_growth_regime_calc137_63d_base_v137_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(31).max().rolling(15).std() * 0.188258
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc137_63d_base_v137_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc137_63d_base_v137_signal

def f202e_f202_ebitda_per_share_growth_regime_calc138_126d_base_v138_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 1.9879)).rolling(22).mean().rolling(10).var().diff(45) * 0.515763
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc138_126d_base_v138_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc138_126d_base_v138_signal

def f202e_f202_ebitda_per_share_growth_regime_calc139_252d_base_v139_signal(ebitda, sharesbas):
    res = (ebitda.diff(5) / (sharesbas.shift(4) + 8.8944)).rolling(20).min().rolling(36).min() * 0.468460
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc139_252d_base_v139_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc139_252d_base_v139_signal

def f202e_f202_ebitda_per_share_growth_regime_calc140_105d_base_v140_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 1.5155)).rolling(33).min().rolling(40).min().diff(16).pct_change(6) * 0.676287
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc140_105d_base_v140_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc140_105d_base_v140_signal

def f202e_f202_ebitda_per_share_growth_regime_calc141_84d_base_v141_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 7.4952)).rolling(41).min().rolling(33).max().rolling(37).std().rolling(14).std() * 0.081578
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc141_84d_base_v141_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc141_84d_base_v141_signal

def f202e_f202_ebitda_per_share_growth_regime_calc142_105d_base_v142_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 0.9342)).rolling(37).min().rolling(27).max().rolling(46).var().rolling(11).max() * 0.928161
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc142_105d_base_v142_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc142_105d_base_v142_signal

def f202e_f202_ebitda_per_share_growth_regime_calc143_126d_base_v143_signal(ebitda, sharesbas):
    res = (ebitda * 1.5917 - sharesbas).rolling(22).var().rolling(23).std().rolling(13).var() * 0.788423
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc143_126d_base_v143_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc143_126d_base_v143_signal

def f202e_f202_ebitda_per_share_growth_regime_calc144_126d_base_v144_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(27).min().rolling(30).var().rolling(23).min() * 0.841486
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc144_126d_base_v144_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc144_126d_base_v144_signal

def f202e_f202_ebitda_per_share_growth_regime_calc145_42d_base_v145_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 9.9356)).rolling(38).max().pct_change(45).rolling(13).mean() * 0.394654
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc145_42d_base_v145_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc145_42d_base_v145_signal

def f202e_f202_ebitda_per_share_growth_regime_calc146_126d_base_v146_signal(ebitda, sharesbas):
    res = (sharesbas / (ebitda + 0.2214)).rolling(34).std().rolling(20).std().rolling(6).max() * 0.579264
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc146_126d_base_v146_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc146_126d_base_v146_signal

def f202e_f202_ebitda_per_share_growth_regime_calc147_10d_base_v147_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(15).rolling(33).max().rolling(3).var().rolling(6).max() * 0.992200
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc147_10d_base_v147_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc147_10d_base_v147_signal

def f202e_f202_ebitda_per_share_growth_regime_calc148_10d_base_v148_signal(ebitda, sharesbas):
    res = (ebitda / (sharesbas + 7.3381)).rolling(29).mean().rolling(38).mean() * 0.383881
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc148_10d_base_v148_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc148_10d_base_v148_signal

def f202e_f202_ebitda_per_share_growth_regime_calc149_10d_base_v149_signal(ebitda, sharesbas):
    res = (ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(5).max().rolling(3).mean().rolling(16).max() * 0.362138
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc149_10d_base_v149_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc149_10d_base_v149_signal

def f202e_f202_ebitda_per_share_growth_regime_calc150_200d_base_v150_signal(ebitda, sharesbas):
    res = (ebitda.diff(9) / (sharesbas.shift(4) + 8.5328)).rolling(20).std().rolling(2).std().rolling(16).var().pct_change(3) * 0.633862
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc150_200d_base_v150_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc150_200d_base_v150_signal


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
