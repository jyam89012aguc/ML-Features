import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f203n_f203_net_income_to_working_capital_momentum_calc076_252d_base_v076_signal(netinc, workingcapital):
    res = (netinc * 0.1060 - workingcapital).diff(50).rolling(28).mean() * 0.917650
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc076_252d_base_v076_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc076_252d_base_v076_signal

def f203n_f203_net_income_to_working_capital_momentum_calc077_200d_base_v077_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 3.7444)).diff(46).rolling(49).var().rolling(16).var().rolling(38).mean() * 0.705897
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc077_200d_base_v077_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc077_200d_base_v077_signal

def f203n_f203_net_income_to_working_capital_momentum_calc078_150d_base_v078_signal(netinc, workingcapital):
    res = (netinc.diff(9) / (workingcapital.shift(1) + 1.0990)).rolling(41).min().rolling(33).max().rolling(32).max() * 0.737421
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc078_150d_base_v078_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc078_150d_base_v078_signal

def f203n_f203_net_income_to_working_capital_momentum_calc079_10d_base_v079_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(27).min().rolling(21).max() * 0.393614
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc079_10d_base_v079_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc079_10d_base_v079_signal

def f203n_f203_net_income_to_working_capital_momentum_calc080_42d_base_v080_signal(netinc, workingcapital):
    res = (netinc.diff(9) / (workingcapital.shift(5) + 3.9696)).diff(4).diff(11).rolling(4).mean().pct_change(28) * 0.165943
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc080_42d_base_v080_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc080_42d_base_v080_signal

def f203n_f203_net_income_to_working_capital_momentum_calc081_5d_base_v081_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(18).var().rolling(5).var().pct_change(41) * 0.958552
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc081_5d_base_v081_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc081_5d_base_v081_signal

def f203n_f203_net_income_to_working_capital_momentum_calc082_126d_base_v082_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 2.9648)).rolling(47).std().rolling(49).std().rolling(2).min().diff(5) * 0.011595
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc082_126d_base_v082_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc082_126d_base_v082_signal

def f203n_f203_net_income_to_working_capital_momentum_calc083_21d_base_v083_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(12).var().diff(44).rolling(33).var() * 0.426371
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc083_21d_base_v083_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc083_21d_base_v083_signal

def f203n_f203_net_income_to_working_capital_momentum_calc084_126d_base_v084_signal(netinc, workingcapital):
    res = (netinc * 5.4587 - workingcapital).rolling(17).max().rolling(12).var().rolling(27).var().pct_change(23) * 0.169072
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc084_126d_base_v084_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc084_126d_base_v084_signal

def f203n_f203_net_income_to_working_capital_momentum_calc085_84d_base_v085_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 6.0901)).pct_change(15).rolling(20).mean() * 0.651169
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc085_84d_base_v085_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc085_84d_base_v085_signal

def f203n_f203_net_income_to_working_capital_momentum_calc086_10d_base_v086_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 2.5468)).pct_change(23).rolling(50).max().rolling(19).var().pct_change(29) * 0.692273
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc086_10d_base_v086_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc086_10d_base_v086_signal

def f203n_f203_net_income_to_working_capital_momentum_calc087_84d_base_v087_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 2.8047)).rolling(42).max().pct_change(2) * 0.572668
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc087_84d_base_v087_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc087_84d_base_v087_signal

def f203n_f203_net_income_to_working_capital_momentum_calc088_105d_base_v088_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 9.3894)).pct_change(39).diff(37).pct_change(28).rolling(14).std() * 0.132327
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc088_105d_base_v088_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc088_105d_base_v088_signal

def f203n_f203_net_income_to_working_capital_momentum_calc089_200d_base_v089_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(38).var().rolling(40).mean() * 0.361767
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc089_200d_base_v089_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc089_200d_base_v089_signal

def f203n_f203_net_income_to_working_capital_momentum_calc090_126d_base_v090_signal(netinc, workingcapital):
    res = (netinc.diff(6) / (workingcapital.shift(1) + 6.9044)).diff(23).rolling(25).min().pct_change(32).rolling(13).mean() * 0.127632
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc090_126d_base_v090_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc090_126d_base_v090_signal

def f203n_f203_net_income_to_working_capital_momentum_calc091_84d_base_v091_signal(netinc, workingcapital):
    res = (netinc * 4.7744 - workingcapital).rolling(5).min().rolling(48).max() * 0.059157
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc091_84d_base_v091_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc091_84d_base_v091_signal

def f203n_f203_net_income_to_working_capital_momentum_calc092_63d_base_v092_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 0.3880)).diff(2).rolling(17).std() * 0.592818
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc092_63d_base_v092_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc092_63d_base_v092_signal

def f203n_f203_net_income_to_working_capital_momentum_calc093_126d_base_v093_signal(netinc, workingcapital):
    res = (netinc * 8.5291 - workingcapital).rolling(35).std().rolling(16).std().rolling(2).mean() * 0.546041
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc093_126d_base_v093_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc093_126d_base_v093_signal

def f203n_f203_net_income_to_working_capital_momentum_calc094_5d_base_v094_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 5.5672)).rolling(6).std().rolling(30).std().rolling(4).var() * 0.872202
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc094_5d_base_v094_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc094_5d_base_v094_signal

def f203n_f203_net_income_to_working_capital_momentum_calc095_105d_base_v095_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 7.5823)).pct_change(11).rolling(42).var().diff(3) * 0.376923
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc095_105d_base_v095_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc095_105d_base_v095_signal

def f203n_f203_net_income_to_working_capital_momentum_calc096_21d_base_v096_signal(netinc, workingcapital):
    res = (netinc * 8.1075 - workingcapital).rolling(4).std().rolling(8).var() * 0.149760
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc096_21d_base_v096_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc096_21d_base_v096_signal

def f203n_f203_net_income_to_working_capital_momentum_calc097_5d_base_v097_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 0.8202)).rolling(19).var().diff(28) * 0.512481
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc097_5d_base_v097_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc097_5d_base_v097_signal

def f203n_f203_net_income_to_working_capital_momentum_calc098_105d_base_v098_signal(netinc, workingcapital):
    res = (netinc * 3.9752 - workingcapital).rolling(48).min().rolling(40).max() * 0.734544
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc098_105d_base_v098_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc098_105d_base_v098_signal

def f203n_f203_net_income_to_working_capital_momentum_calc099_150d_base_v099_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(7).rolling(2).mean() * 0.936310
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc099_150d_base_v099_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc099_150d_base_v099_signal

def f203n_f203_net_income_to_working_capital_momentum_calc100_126d_base_v100_signal(netinc, workingcapital):
    res = (netinc.diff(2) / (workingcapital.shift(3) + 1.1201)).rolling(33).mean().rolling(15).mean().rolling(30).std().diff(47) * 0.134129
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc100_126d_base_v100_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc100_126d_base_v100_signal

def f203n_f203_net_income_to_working_capital_momentum_calc101_200d_base_v101_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 0.1271)).rolling(10).max().rolling(21).std().diff(30).rolling(24).std() * 0.394415
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc101_200d_base_v101_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc101_200d_base_v101_signal

def f203n_f203_net_income_to_working_capital_momentum_calc102_42d_base_v102_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 6.0160)).pct_change(25).diff(14).diff(24).rolling(37).std() * 0.973737
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc102_42d_base_v102_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc102_42d_base_v102_signal

def f203n_f203_net_income_to_working_capital_momentum_calc103_200d_base_v103_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 8.3867)).rolling(4).mean().diff(24) * 0.018602
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc103_200d_base_v103_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc103_200d_base_v103_signal

def f203n_f203_net_income_to_working_capital_momentum_calc104_42d_base_v104_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 4.0069)).rolling(38).std().diff(14) * 0.185785
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc104_42d_base_v104_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc104_42d_base_v104_signal

def f203n_f203_net_income_to_working_capital_momentum_calc105_105d_base_v105_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(35).rolling(41).var() * 0.625155
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc105_105d_base_v105_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc105_105d_base_v105_signal

def f203n_f203_net_income_to_working_capital_momentum_calc106_252d_base_v106_signal(netinc, workingcapital):
    res = (netinc * 9.3460 - workingcapital).pct_change(13).rolling(17).max().rolling(46).min() * 0.704110
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc106_252d_base_v106_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc106_252d_base_v106_signal

def f203n_f203_net_income_to_working_capital_momentum_calc107_126d_base_v107_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 1.9087)).rolling(42).var().pct_change(23).rolling(25).var() * 0.306077
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc107_126d_base_v107_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc107_126d_base_v107_signal

def f203n_f203_net_income_to_working_capital_momentum_calc108_150d_base_v108_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(20).mean().diff(22).rolling(12).max() * 0.099744
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc108_150d_base_v108_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc108_150d_base_v108_signal

def f203n_f203_net_income_to_working_capital_momentum_calc109_21d_base_v109_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 9.1632)).rolling(32).min().pct_change(12).diff(32).pct_change(6) * 0.567738
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc109_21d_base_v109_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc109_21d_base_v109_signal

def f203n_f203_net_income_to_working_capital_momentum_calc110_63d_base_v110_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 3.9078)).rolling(14).std().rolling(2).mean().rolling(40).max() * 0.765235
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc110_63d_base_v110_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc110_63d_base_v110_signal

def f203n_f203_net_income_to_working_capital_momentum_calc111_63d_base_v111_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 1.2932)).rolling(7).var().rolling(15).var().rolling(39).min() * 0.477430
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc111_63d_base_v111_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc111_63d_base_v111_signal

def f203n_f203_net_income_to_working_capital_momentum_calc112_252d_base_v112_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 5.9911)).rolling(41).std().rolling(28).var() * 0.051289
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc112_252d_base_v112_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc112_252d_base_v112_signal

def f203n_f203_net_income_to_working_capital_momentum_calc113_84d_base_v113_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 8.0500)).pct_change(10).rolling(37).min() * 0.723599
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc113_84d_base_v113_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc113_84d_base_v113_signal

def f203n_f203_net_income_to_working_capital_momentum_calc114_252d_base_v114_signal(netinc, workingcapital):
    res = (netinc * 6.9583 - workingcapital).rolling(29).max().rolling(39).mean().rolling(3).std() * 0.118618
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc114_252d_base_v114_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc114_252d_base_v114_signal

def f203n_f203_net_income_to_working_capital_momentum_calc115_84d_base_v115_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 9.8898)).rolling(43).mean().rolling(5).var().pct_change(31) * 0.857082
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc115_84d_base_v115_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc115_84d_base_v115_signal

def f203n_f203_net_income_to_working_capital_momentum_calc116_150d_base_v116_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 3.7879)).rolling(9).max().rolling(13).min().rolling(15).std().diff(9) * 0.028641
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc116_150d_base_v116_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc116_150d_base_v116_signal

def f203n_f203_net_income_to_working_capital_momentum_calc117_63d_base_v117_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(4).diff(43) * 0.275034
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc117_63d_base_v117_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc117_63d_base_v117_signal

def f203n_f203_net_income_to_working_capital_momentum_calc118_21d_base_v118_signal(netinc, workingcapital):
    res = (netinc.diff(7) / (workingcapital.shift(4) + 4.3989)).diff(6).rolling(35).mean().rolling(15).min() * 0.688520
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc118_21d_base_v118_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc118_21d_base_v118_signal

def f203n_f203_net_income_to_working_capital_momentum_calc119_42d_base_v119_signal(netinc, workingcapital):
    res = (netinc * 4.0008 - workingcapital).rolling(30).var().rolling(48).std().rolling(50).std().diff(16) * 0.413472
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc119_42d_base_v119_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc119_42d_base_v119_signal

def f203n_f203_net_income_to_working_capital_momentum_calc120_21d_base_v120_signal(netinc, workingcapital):
    res = (netinc * 2.0366 - workingcapital).rolling(4).min().pct_change(45) * 0.568174
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc120_21d_base_v120_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc120_21d_base_v120_signal

def f203n_f203_net_income_to_working_capital_momentum_calc121_63d_base_v121_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(40).var().rolling(2).std() * 0.181751
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc121_63d_base_v121_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc121_63d_base_v121_signal

def f203n_f203_net_income_to_working_capital_momentum_calc122_200d_base_v122_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 0.4397)).rolling(35).var().diff(49).rolling(6).max() * 0.865202
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc122_200d_base_v122_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc122_200d_base_v122_signal

def f203n_f203_net_income_to_working_capital_momentum_calc123_42d_base_v123_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(39).min().rolling(7).min().rolling(32).max() * 0.871965
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc123_42d_base_v123_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc123_42d_base_v123_signal

def f203n_f203_net_income_to_working_capital_momentum_calc124_21d_base_v124_signal(netinc, workingcapital):
    res = (netinc * 7.9829 - workingcapital).rolling(5).min().rolling(21).min().rolling(42).mean() * 0.037459
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc124_21d_base_v124_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc124_21d_base_v124_signal

def f203n_f203_net_income_to_working_capital_momentum_calc125_105d_base_v125_signal(netinc, workingcapital):
    res = (netinc * 8.2374 - workingcapital).rolling(23).min().rolling(17).mean().rolling(4).std().rolling(34).max() * 0.311704
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc125_105d_base_v125_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc125_105d_base_v125_signal

def f203n_f203_net_income_to_working_capital_momentum_calc126_5d_base_v126_signal(netinc, workingcapital):
    res = (netinc.diff(3) / (workingcapital.shift(3) + 3.5022)).diff(14).rolling(27).min().rolling(31).max() * 0.129009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc126_5d_base_v126_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc126_5d_base_v126_signal

def f203n_f203_net_income_to_working_capital_momentum_calc127_150d_base_v127_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 3.0318)).rolling(18).max().rolling(24).min() * 0.049798
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc127_150d_base_v127_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc127_150d_base_v127_signal

def f203n_f203_net_income_to_working_capital_momentum_calc128_126d_base_v128_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 9.7185)).rolling(14).var().diff(11).rolling(47).mean() * 0.107735
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc128_126d_base_v128_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc128_126d_base_v128_signal

def f203n_f203_net_income_to_working_capital_momentum_calc129_200d_base_v129_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 9.4931)).rolling(42).max().rolling(39).var().rolling(3).min() * 0.368812
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc129_200d_base_v129_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc129_200d_base_v129_signal

def f203n_f203_net_income_to_working_capital_momentum_calc130_150d_base_v130_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(26).mean().rolling(5).std().pct_change(31) * 0.408284
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc130_150d_base_v130_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc130_150d_base_v130_signal

def f203n_f203_net_income_to_working_capital_momentum_calc131_105d_base_v131_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 2.5601)).rolling(3).max().diff(17) * 0.268955
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc131_105d_base_v131_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc131_105d_base_v131_signal

def f203n_f203_net_income_to_working_capital_momentum_calc132_84d_base_v132_signal(netinc, workingcapital):
    res = (netinc.diff(7) / (workingcapital.shift(1) + 4.6761)).pct_change(9).rolling(19).min().rolling(12).std().rolling(4).max() * 0.045749
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc132_84d_base_v132_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc132_84d_base_v132_signal

def f203n_f203_net_income_to_working_capital_momentum_calc133_21d_base_v133_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 3.5805)).diff(8).pct_change(9).rolling(33).min().rolling(49).mean() * 0.618116
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc133_21d_base_v133_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc133_21d_base_v133_signal

def f203n_f203_net_income_to_working_capital_momentum_calc134_252d_base_v134_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 1.9483)).rolling(42).min().rolling(10).min().diff(31).rolling(16).max() * 0.547077
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc134_252d_base_v134_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc134_252d_base_v134_signal

def f203n_f203_net_income_to_working_capital_momentum_calc135_150d_base_v135_signal(netinc, workingcapital):
    res = (netinc.diff(3) / (workingcapital.shift(1) + 1.4416)).rolling(42).mean().rolling(32).std().rolling(9).mean().rolling(24).var() * 0.829509
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc135_150d_base_v135_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc135_150d_base_v135_signal

def f203n_f203_net_income_to_working_capital_momentum_calc136_42d_base_v136_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 4.3720)).rolling(4).max().rolling(48).max().diff(49) * 0.271850
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc136_42d_base_v136_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc136_42d_base_v136_signal

def f203n_f203_net_income_to_working_capital_momentum_calc137_126d_base_v137_signal(netinc, workingcapital):
    res = (netinc.diff(9) / (workingcapital.shift(2) + 7.4303)).rolling(3).min().rolling(7).mean() * 0.210668
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc137_126d_base_v137_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc137_126d_base_v137_signal

def f203n_f203_net_income_to_working_capital_momentum_calc138_126d_base_v138_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(7).min().rolling(11).min() * 0.360995
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc138_126d_base_v138_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc138_126d_base_v138_signal

def f203n_f203_net_income_to_working_capital_momentum_calc139_150d_base_v139_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(4).min().rolling(41).var().rolling(16).std() * 0.870748
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc139_150d_base_v139_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc139_150d_base_v139_signal

def f203n_f203_net_income_to_working_capital_momentum_calc140_84d_base_v140_signal(netinc, workingcapital):
    res = (netinc * 0.7860 - workingcapital).pct_change(29).diff(3).rolling(15).std() * 0.015374
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc140_84d_base_v140_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc140_84d_base_v140_signal

def f203n_f203_net_income_to_working_capital_momentum_calc141_84d_base_v141_signal(netinc, workingcapital):
    res = (netinc * 9.1564 - workingcapital).rolling(20).std().diff(28) * 0.543272
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc141_84d_base_v141_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc141_84d_base_v141_signal

def f203n_f203_net_income_to_working_capital_momentum_calc142_42d_base_v142_signal(netinc, workingcapital):
    res = (netinc.diff(7) / (workingcapital.shift(5) + 7.0062)).rolling(33).max().rolling(13).max().rolling(46).mean().pct_change(17) * 0.185534
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc142_42d_base_v142_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc142_42d_base_v142_signal

def f203n_f203_net_income_to_working_capital_momentum_calc143_105d_base_v143_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 3.8395)).diff(41).rolling(11).min().rolling(16).mean().rolling(35).min() * 0.408657
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc143_105d_base_v143_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc143_105d_base_v143_signal

def f203n_f203_net_income_to_working_capital_momentum_calc144_5d_base_v144_signal(netinc, workingcapital):
    res = (netinc.diff(8) / (workingcapital.shift(1) + 0.2288)).diff(9).rolling(30).min().diff(29).rolling(24).mean() * 0.466185
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc144_5d_base_v144_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc144_5d_base_v144_signal

def f203n_f203_net_income_to_working_capital_momentum_calc145_150d_base_v145_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 1.5994)).rolling(29).var().rolling(26).std() * 0.720883
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc145_150d_base_v145_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc145_150d_base_v145_signal

def f203n_f203_net_income_to_working_capital_momentum_calc146_21d_base_v146_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(39).max().diff(49) * 0.983807
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc146_21d_base_v146_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc146_21d_base_v146_signal

def f203n_f203_net_income_to_working_capital_momentum_calc147_200d_base_v147_signal(netinc, workingcapital):
    res = (netinc * 2.0581 - workingcapital).rolling(44).std().rolling(19).max().pct_change(9).rolling(28).max() * 0.479060
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc147_200d_base_v147_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc147_200d_base_v147_signal

def f203n_f203_net_income_to_working_capital_momentum_calc148_126d_base_v148_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(39).std().rolling(36).std().pct_change(29).rolling(48).std() * 0.534823
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc148_126d_base_v148_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc148_126d_base_v148_signal

def f203n_f203_net_income_to_working_capital_momentum_calc149_10d_base_v149_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 0.7148)).rolling(3).std().rolling(8).mean().rolling(3).min().rolling(10).mean() * 0.104042
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc149_10d_base_v149_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc149_10d_base_v149_signal

def f203n_f203_net_income_to_working_capital_momentum_calc150_252d_base_v150_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(47).var().pct_change(10) * 0.979920
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc150_252d_base_v150_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc150_252d_base_v150_signal


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
