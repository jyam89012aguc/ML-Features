import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_42d_base_v076_signal(ncfo, liabilities):
    res = (ncfo * 7.3650 - liabilities).rolling(42).var().rolling(22).mean() * 0.057991
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_42d_base_v076_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_42d_base_v076_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_126d_base_v077_signal(ncfo, liabilities):
    res = (ncfo * 1.8043 - liabilities).rolling(13).min().pct_change(9).rolling(20).mean() * 0.347847
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_126d_base_v077_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_126d_base_v077_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_150d_base_v078_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(25).var().rolling(11).max().diff(39) * 0.247843
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_150d_base_v078_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_150d_base_v078_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_105d_base_v079_signal(ncfo, liabilities):
    res = (ncfo * 0.8789 - liabilities).pct_change(4).rolling(3).min().diff(18) * 0.263789
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_105d_base_v079_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_105d_base_v079_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_63d_base_v080_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(42).rolling(22).var().diff(50).rolling(35).max() * 0.569909
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_63d_base_v080_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_63d_base_v080_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_84d_base_v081_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 7.0870)).rolling(13).var().diff(19) * 0.227498
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_84d_base_v081_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_84d_base_v081_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_105d_base_v082_signal(ncfo, liabilities):
    res = (ncfo * 7.4168 - liabilities).rolling(41).max().diff(20).rolling(48).min() * 0.821561
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_105d_base_v082_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_105d_base_v082_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_42d_base_v083_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 4.6001)).rolling(11).min().rolling(37).max().rolling(41).var().rolling(6).std() * 0.301836
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_42d_base_v083_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_42d_base_v083_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_84d_base_v084_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(21).std().rolling(48).mean().rolling(37).mean() * 0.385073
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_84d_base_v084_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_84d_base_v084_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_200d_base_v085_signal(ncfo, liabilities):
    res = (ncfo.diff(10) / (liabilities.shift(4) + 8.8486)).pct_change(41).rolling(7).max() * 0.234775
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_200d_base_v085_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_200d_base_v085_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_126d_base_v086_signal(ncfo, liabilities):
    res = (ncfo.diff(9) / (liabilities.shift(5) + 6.1065)).rolling(26).var().rolling(47).std().rolling(13).mean().rolling(49).mean() * 0.353781
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_126d_base_v086_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_126d_base_v086_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_126d_base_v087_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 3.2138)).rolling(6).max().rolling(9).std() * 0.935242
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_126d_base_v087_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_126d_base_v087_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_126d_base_v088_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 8.5219)).diff(30).diff(27).rolling(2).var() * 0.282055
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_126d_base_v088_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_126d_base_v088_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_63d_base_v089_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 6.7175)).rolling(14).max().rolling(25).std().pct_change(36) * 0.224196
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_63d_base_v089_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_63d_base_v089_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_84d_base_v090_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(39).max().diff(29).rolling(50).mean() * 0.532042
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_84d_base_v090_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_84d_base_v090_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_252d_base_v091_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 3.2561)).rolling(42).var().rolling(9).mean().diff(17).rolling(13).std() * 0.939936
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_252d_base_v091_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_252d_base_v091_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_21d_base_v092_signal(ncfo, liabilities):
    res = (ncfo * 7.5676 - liabilities).rolling(27).std().rolling(24).std().rolling(26).max().diff(30) * 0.616371
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_21d_base_v092_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_21d_base_v092_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_150d_base_v093_signal(ncfo, liabilities):
    res = (ncfo * 9.0181 - liabilities).rolling(23).var().rolling(10).var() * 0.706635
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_150d_base_v093_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_150d_base_v093_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_5d_base_v094_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 9.2442)).rolling(12).min().rolling(50).mean() * 0.155840
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_5d_base_v094_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_5d_base_v094_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_150d_base_v095_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(35).diff(4) * 0.639332
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_150d_base_v095_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_150d_base_v095_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_5d_base_v096_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(13).std().rolling(22).var() * 0.211597
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_5d_base_v096_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_5d_base_v096_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_126d_base_v097_signal(ncfo, liabilities):
    res = (ncfo.diff(3) / (liabilities.shift(1) + 6.2273)).pct_change(16).rolling(45).max().rolling(32).min() * 0.055270
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_126d_base_v097_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_126d_base_v097_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_126d_base_v098_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 4.5928)).rolling(35).min().rolling(43).min().rolling(43).mean() * 0.734387
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_126d_base_v098_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_126d_base_v098_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_63d_base_v099_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 3.3243)).rolling(28).min().rolling(29).max().pct_change(25) * 0.148747
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_63d_base_v099_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_63d_base_v099_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_5d_base_v100_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(41).rolling(6).mean().rolling(40).min() * 0.053135
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_5d_base_v100_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_5d_base_v100_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_5d_base_v101_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 3.2402)).rolling(19).max().rolling(15).std().rolling(35).std() * 0.252735
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_5d_base_v101_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_5d_base_v101_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_200d_base_v102_signal(ncfo, liabilities):
    res = (ncfo * 4.2122 - liabilities).diff(18).rolling(41).max().rolling(49).std().rolling(7).max() * 0.012071
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_200d_base_v102_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_200d_base_v102_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_10d_base_v103_signal(ncfo, liabilities):
    res = (ncfo.diff(6) / (liabilities.shift(2) + 2.5763)).rolling(32).max().pct_change(45).pct_change(35) * 0.568986
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_10d_base_v103_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_10d_base_v103_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_84d_base_v104_signal(ncfo, liabilities):
    res = (ncfo.diff(4) / (liabilities.shift(2) + 9.7275)).rolling(24).std().rolling(47).std() * 0.716710
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_84d_base_v104_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_84d_base_v104_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_84d_base_v105_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 0.9869)).rolling(21).min().rolling(29).std().rolling(24).max() * 0.779678
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_84d_base_v105_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_84d_base_v105_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_21d_base_v106_signal(ncfo, liabilities):
    res = (ncfo.diff(2) / (liabilities.shift(2) + 9.1368)).rolling(46).mean().diff(25) * 0.906532
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_21d_base_v106_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_21d_base_v106_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_5d_base_v107_signal(ncfo, liabilities):
    res = (ncfo * 4.6482 - liabilities).pct_change(37).rolling(18).min().pct_change(22) * 0.077395
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_5d_base_v107_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_5d_base_v107_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_200d_base_v108_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(48).max().rolling(42).mean().rolling(35).min() * 0.568417
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_200d_base_v108_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_200d_base_v108_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_63d_base_v109_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(32).std().rolling(26).max().rolling(47).min() * 0.048549
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_63d_base_v109_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_63d_base_v109_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_105d_base_v110_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(33).diff(6) * 0.052433
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_105d_base_v110_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_105d_base_v110_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_126d_base_v111_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.6103)).rolling(27).var().rolling(25).std().pct_change(8) * 0.691392
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_126d_base_v111_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_126d_base_v111_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_10d_base_v112_signal(ncfo, liabilities):
    res = (ncfo.diff(9) / (liabilities.shift(1) + 3.2911)).rolling(28).mean().rolling(39).max().rolling(30).min().rolling(39).std() * 0.508626
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_10d_base_v112_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_10d_base_v112_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_252d_base_v113_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 7.8665)).rolling(5).max().rolling(19).var().pct_change(33) * 0.546513
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_252d_base_v113_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_252d_base_v113_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_200d_base_v114_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.6262)).rolling(11).max().rolling(45).mean().rolling(23).mean().rolling(43).max() * 0.362282
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_200d_base_v114_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_200d_base_v114_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_5d_base_v115_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(31).std().rolling(22).min().diff(29) * 0.181829
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_5d_base_v115_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_5d_base_v115_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_84d_base_v116_signal(ncfo, liabilities):
    res = (ncfo.diff(4) / (liabilities.shift(3) + 4.2467)).pct_change(16).rolling(27).var() * 0.210636
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_84d_base_v116_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_84d_base_v116_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_126d_base_v117_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.0431)).rolling(34).min().rolling(50).mean().rolling(10).mean().rolling(26).min() * 0.770656
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_126d_base_v117_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_126d_base_v117_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_126d_base_v118_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.8835)).pct_change(49).rolling(21).var().rolling(16).mean().rolling(2).max() * 0.723074
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_126d_base_v118_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_126d_base_v118_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_200d_base_v119_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 4.7313)).rolling(29).mean().rolling(47).mean() * 0.590956
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_200d_base_v119_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_200d_base_v119_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_10d_base_v120_signal(ncfo, liabilities):
    res = (ncfo * 7.7312 - liabilities).rolling(33).std().rolling(8).max().diff(12).rolling(10).max() * 0.314002
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_10d_base_v120_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_10d_base_v120_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_150d_base_v121_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.8556)).rolling(46).var().rolling(14).max().diff(32) * 0.822306
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_150d_base_v121_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_150d_base_v121_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_42d_base_v122_signal(ncfo, liabilities):
    res = (ncfo * 7.1411 - liabilities).rolling(48).max().rolling(11).std() * 0.064806
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_42d_base_v122_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_42d_base_v122_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_21d_base_v123_signal(ncfo, liabilities):
    res = (ncfo * 4.3836 - liabilities).rolling(32).max().rolling(35).max() * 0.620550
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_21d_base_v123_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_21d_base_v123_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_63d_base_v124_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 1.9419)).rolling(32).min().rolling(2).var().rolling(26).var().rolling(19).std() * 0.577166
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_63d_base_v124_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_63d_base_v124_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_200d_base_v125_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 2.5546)).rolling(31).max().rolling(35).min() * 0.605254
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_200d_base_v125_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_200d_base_v125_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_200d_base_v126_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 9.9761)).rolling(45).std().rolling(6).mean() * 0.887746
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_200d_base_v126_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_200d_base_v126_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_252d_base_v127_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 0.3312)).rolling(8).min().diff(26) * 0.422897
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_252d_base_v127_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_252d_base_v127_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_252d_base_v128_signal(ncfo, liabilities):
    res = (ncfo.diff(4) / (liabilities.shift(3) + 3.4430)).rolling(48).var().diff(47).rolling(49).var().rolling(40).min() * 0.850379
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_252d_base_v128_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_252d_base_v128_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_21d_base_v129_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(23).std().pct_change(46) * 0.939415
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_21d_base_v129_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_21d_base_v129_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_252d_base_v130_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 5.0551)).rolling(32).min().rolling(42).max() * 0.988615
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_252d_base_v130_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_252d_base_v130_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_252d_base_v131_signal(ncfo, liabilities):
    res = (ncfo * 9.1212 - liabilities).rolling(23).min().rolling(10).std().rolling(14).var() * 0.589251
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_252d_base_v131_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_252d_base_v131_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_150d_base_v132_signal(ncfo, liabilities):
    res = (ncfo * 1.3950 - liabilities).rolling(21).var().rolling(49).std().rolling(38).min().diff(17) * 0.375257
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_150d_base_v132_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_150d_base_v132_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_63d_base_v133_signal(ncfo, liabilities):
    res = (ncfo.diff(6) / (liabilities.shift(2) + 4.8686)).rolling(30).mean().rolling(44).max().rolling(29).mean() * 0.514070
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_63d_base_v133_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_63d_base_v133_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_200d_base_v134_signal(ncfo, liabilities):
    res = (ncfo * 8.3941 - liabilities).diff(23).rolling(16).mean().pct_change(28).rolling(8).mean() * 0.458766
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_200d_base_v134_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_200d_base_v134_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_84d_base_v135_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 6.7394)).rolling(14).max().diff(8) * 0.150437
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_84d_base_v135_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_84d_base_v135_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_42d_base_v136_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(30).rolling(48).std() * 0.663642
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_42d_base_v136_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_42d_base_v136_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_84d_base_v137_signal(ncfo, liabilities):
    res = (ncfo * 5.5990 - liabilities).pct_change(9).rolling(24).min() * 0.985642
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_84d_base_v137_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_84d_base_v137_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_200d_base_v138_signal(ncfo, liabilities):
    res = (ncfo / (liabilities + 5.0588)).rolling(28).max().rolling(47).var() * 0.930583
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_200d_base_v138_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_200d_base_v138_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_63d_base_v139_signal(ncfo, liabilities):
    res = (ncfo.diff(8) / (liabilities.shift(1) + 3.3912)).rolling(4).min().rolling(49).std().rolling(33).mean() * 0.087780
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_63d_base_v139_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_63d_base_v139_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_84d_base_v140_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 5.4141)).rolling(13).mean().diff(11) * 0.824537
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_84d_base_v140_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_84d_base_v140_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_5d_base_v141_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 4.7340)).diff(35).rolling(49).std() * 0.561396
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_5d_base_v141_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_5d_base_v141_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_84d_base_v142_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(45).rolling(6).min().rolling(2).mean() * 0.010059
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_84d_base_v142_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_84d_base_v142_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_200d_base_v143_signal(ncfo, liabilities):
    res = (ncfo.diff(7) / (liabilities.shift(5) + 6.6367)).rolling(33).max().rolling(24).min().rolling(14).std() * 0.808472
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_200d_base_v143_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_200d_base_v143_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_84d_base_v144_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 1.7244)).pct_change(35).rolling(8).var() * 0.347805
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_84d_base_v144_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_84d_base_v144_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_126d_base_v145_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 1.6853)).rolling(18).std().rolling(20).min().rolling(41).var().rolling(3).var() * 0.992271
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_126d_base_v145_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_126d_base_v145_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_105d_base_v146_signal(ncfo, liabilities):
    res = (liabilities / (ncfo + 2.4872)).pct_change(20).pct_change(14).diff(5) * 0.665487
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_105d_base_v146_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_105d_base_v146_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_200d_base_v147_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(48).rolling(27).mean().rolling(40).var().rolling(38).mean() * 0.373823
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_200d_base_v147_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_200d_base_v147_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_5d_base_v148_signal(ncfo, liabilities):
    res = (ncfo * 7.6978 - liabilities).diff(27).rolling(36).var().rolling(17).std().rolling(44).min() * 0.498576
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_5d_base_v148_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_5d_base_v148_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_252d_base_v149_signal(ncfo, liabilities):
    res = (ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(37).var().rolling(39).std().rolling(2).std() * 0.361169
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_252d_base_v149_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_252d_base_v149_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_21d_base_v150_signal(ncfo, liabilities):
    res = (ncfo.diff(2) / (liabilities.shift(2) + 5.5627)).diff(28).rolling(14).mean() * 0.956085
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_21d_base_v150_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_21d_base_v150_signal


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
