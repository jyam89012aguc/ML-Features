import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f205f_f205_fcf_per_share_dispersion_cycles_calc076_5d_base_v076_signal(fcf, sharesbas):
    res = (fcf * 2.2918 - sharesbas).rolling(20).std().rolling(36).max().rolling(34).mean() * 0.420264
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc076_5d_base_v076_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc076_5d_base_v076_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc077_42d_base_v077_signal(fcf, sharesbas):
    res = (fcf * 9.7614 - sharesbas).diff(5).pct_change(8).diff(12) * 0.589813
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc077_42d_base_v077_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc077_42d_base_v077_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc078_105d_base_v078_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 0.9852)).rolling(26).mean().rolling(49).mean().rolling(25).max().rolling(11).var() * 0.878682
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc078_105d_base_v078_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc078_105d_base_v078_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc079_5d_base_v079_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 7.3763)).pct_change(42).rolling(12).max().rolling(22).var().pct_change(29) * 0.072054
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc079_5d_base_v079_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc079_5d_base_v079_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc080_84d_base_v080_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 6.8231)).rolling(40).mean().rolling(38).min().rolling(2).mean() * 0.916645
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc080_84d_base_v080_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc080_84d_base_v080_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc081_63d_base_v081_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 3.6409)).rolling(37).var().rolling(4).mean().rolling(6).std() * 0.116152
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc081_63d_base_v081_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc081_63d_base_v081_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc082_252d_base_v082_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(12).rolling(37).max().rolling(43).max() * 0.057016
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc082_252d_base_v082_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc082_252d_base_v082_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc083_63d_base_v083_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 6.8918)).rolling(9).max().rolling(28).var() * 0.150008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc083_63d_base_v083_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc083_63d_base_v083_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc084_21d_base_v084_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 3.5646)).rolling(32).max().pct_change(37).diff(8).rolling(25).std() * 0.997785
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc084_21d_base_v084_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc084_21d_base_v084_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc085_200d_base_v085_signal(fcf, sharesbas):
    res = (fcf * 8.4199 - sharesbas).rolling(34).var().diff(20) * 0.605050
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc085_200d_base_v085_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc085_200d_base_v085_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc086_150d_base_v086_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(29).mean().rolling(43).var().pct_change(12) * 0.897460
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc086_150d_base_v086_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc086_150d_base_v086_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc087_63d_base_v087_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 7.1054)).rolling(16).var().rolling(26).var().rolling(21).std().rolling(26).min() * 0.176742
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc087_63d_base_v087_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc087_63d_base_v087_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc088_63d_base_v088_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 3.9662)).rolling(38).min().rolling(16).min().rolling(5).max() * 0.557115
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc088_63d_base_v088_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc088_63d_base_v088_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc089_126d_base_v089_signal(fcf, sharesbas):
    res = (fcf * 3.5097 - sharesbas).rolling(2).var().rolling(13).mean() * 0.017329
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc089_126d_base_v089_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc089_126d_base_v089_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc090_105d_base_v090_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(20).std().rolling(42).max() * 0.682639
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc090_105d_base_v090_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc090_105d_base_v090_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc091_5d_base_v091_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(14).max().rolling(48).max().rolling(20).min() * 0.359540
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc091_5d_base_v091_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc091_5d_base_v091_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc092_63d_base_v092_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(50).rolling(46).max() * 0.987147
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc092_63d_base_v092_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc092_63d_base_v092_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc093_126d_base_v093_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 2.4377)).rolling(48).min().rolling(25).mean().pct_change(32).rolling(47).std() * 0.672005
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc093_126d_base_v093_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc093_126d_base_v093_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc094_5d_base_v094_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 1.0670)).rolling(16).mean().rolling(25).max() * 0.860760
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc094_5d_base_v094_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc094_5d_base_v094_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc095_105d_base_v095_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 2.8728)).rolling(23).std().rolling(44).max().rolling(39).min() * 0.289242
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc095_105d_base_v095_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc095_105d_base_v095_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc096_252d_base_v096_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 7.9268)).rolling(4).mean().diff(35) * 0.457793
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc096_252d_base_v096_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc096_252d_base_v096_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc097_42d_base_v097_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 7.8616)).rolling(44).mean().rolling(43).mean().pct_change(32).rolling(36).max() * 0.938549
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc097_42d_base_v097_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc097_42d_base_v097_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc098_63d_base_v098_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 9.1336)).rolling(26).var().rolling(10).std() * 0.075217
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc098_63d_base_v098_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc098_63d_base_v098_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc099_10d_base_v099_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 1.4072)).pct_change(49).rolling(48).min().rolling(26).mean() * 0.805655
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc099_10d_base_v099_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc099_10d_base_v099_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc100_42d_base_v100_signal(fcf, sharesbas):
    res = (fcf.diff(8) / (sharesbas.shift(1) + 2.8932)).diff(28).rolling(19).mean().diff(35).rolling(15).mean() * 0.142296
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc100_42d_base_v100_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc100_42d_base_v100_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc101_84d_base_v101_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 0.7885)).pct_change(28).diff(8).rolling(45).var().diff(8) * 0.800450
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc101_84d_base_v101_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc101_84d_base_v101_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc102_126d_base_v102_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 8.3610)).pct_change(35).rolling(9).var().pct_change(19).rolling(41).max() * 0.271034
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc102_126d_base_v102_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc102_126d_base_v102_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc103_42d_base_v103_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 7.9145)).rolling(41).var().rolling(6).mean() * 0.900843
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc103_42d_base_v103_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc103_42d_base_v103_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc104_63d_base_v104_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 9.4126)).rolling(17).std().rolling(33).std().rolling(4).mean().rolling(40).mean() * 0.156393
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc104_63d_base_v104_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc104_63d_base_v104_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc105_126d_base_v105_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 2.7610)).rolling(29).max().rolling(6).std().rolling(4).min() * 0.882361
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc105_126d_base_v105_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc105_126d_base_v105_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc106_84d_base_v106_signal(fcf, sharesbas):
    res = (fcf * 1.4924 - sharesbas).rolling(25).max().diff(13) * 0.914428
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc106_84d_base_v106_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc106_84d_base_v106_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc107_42d_base_v107_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 9.7327)).rolling(49).max().diff(50).rolling(4).min() * 0.745282
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc107_42d_base_v107_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc107_42d_base_v107_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc108_150d_base_v108_signal(fcf, sharesbas):
    res = (fcf.diff(6) / (sharesbas.shift(2) + 7.3885)).rolling(3).min().pct_change(22).diff(29).rolling(43).var() * 0.379553
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc108_150d_base_v108_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc108_150d_base_v108_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc109_42d_base_v109_signal(fcf, sharesbas):
    res = (fcf.diff(5) / (sharesbas.shift(5) + 8.0334)).rolling(23).var().rolling(7).mean() * 0.978176
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc109_42d_base_v109_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc109_42d_base_v109_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc110_10d_base_v110_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 9.1044)).diff(42).rolling(23).mean() * 0.182837
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc110_10d_base_v110_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc110_10d_base_v110_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc111_63d_base_v111_signal(fcf, sharesbas):
    res = (fcf.diff(4) / (sharesbas.shift(4) + 4.2083)).rolling(12).max().rolling(32).mean() * 0.608647
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc111_63d_base_v111_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc111_63d_base_v111_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc112_200d_base_v112_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(22).mean().rolling(46).std().rolling(22).max().rolling(11).mean() * 0.359904
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc112_200d_base_v112_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc112_200d_base_v112_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc113_42d_base_v113_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(33).min().rolling(13).max().rolling(11).var() * 0.439619
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc113_42d_base_v113_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc113_42d_base_v113_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc114_105d_base_v114_signal(fcf, sharesbas):
    res = (fcf.diff(9) / (sharesbas.shift(2) + 5.8981)).rolling(49).var().rolling(30).std() * 0.208751
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc114_105d_base_v114_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc114_105d_base_v114_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc115_21d_base_v115_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 3.2747)).rolling(40).mean().pct_change(40).rolling(11).mean().rolling(22).var() * 0.789723
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc115_21d_base_v115_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc115_21d_base_v115_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc116_84d_base_v116_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 4.3896)).rolling(46).var().diff(6).rolling(15).mean().diff(29) * 0.100012
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc116_84d_base_v116_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc116_84d_base_v116_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc117_42d_base_v117_signal(fcf, sharesbas):
    res = (fcf * 6.5507 - sharesbas).rolling(9).min().rolling(39).var().rolling(37).max() * 0.869023
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc117_42d_base_v117_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc117_42d_base_v117_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc118_63d_base_v118_signal(fcf, sharesbas):
    res = (fcf.diff(9) / (sharesbas.shift(1) + 7.2099)).rolling(2).min().pct_change(2) * 0.617685
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc118_63d_base_v118_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc118_63d_base_v118_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc119_10d_base_v119_signal(fcf, sharesbas):
    res = (fcf * 3.2062 - sharesbas).rolling(14).min().diff(13).rolling(14).mean() * 0.313782
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc119_10d_base_v119_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc119_10d_base_v119_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc120_105d_base_v120_signal(fcf, sharesbas):
    res = (fcf.diff(10) / (sharesbas.shift(3) + 4.5746)).diff(47).rolling(28).var().rolling(45).std().rolling(25).var() * 0.713370
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc120_105d_base_v120_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc120_105d_base_v120_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc121_252d_base_v121_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 9.4723)).diff(32).rolling(8).min().rolling(4).std() * 0.577133
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc121_252d_base_v121_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc121_252d_base_v121_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc122_84d_base_v122_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 3.5873)).rolling(21).min().rolling(8).var() * 0.959214
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc122_84d_base_v122_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc122_84d_base_v122_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc123_105d_base_v123_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 0.4432)).diff(32).rolling(27).std() * 0.885375
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc123_105d_base_v123_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc123_105d_base_v123_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc124_252d_base_v124_signal(fcf, sharesbas):
    res = (fcf * 3.2580 - sharesbas).pct_change(8).rolling(20).min().rolling(10).var().pct_change(25) * 0.503797
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc124_252d_base_v124_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc124_252d_base_v124_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc125_252d_base_v125_signal(fcf, sharesbas):
    res = (fcf.diff(4) / (sharesbas.shift(1) + 1.5941)).rolling(7).max().rolling(22).mean().rolling(23).max() * 0.197106
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc125_252d_base_v125_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc125_252d_base_v125_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc126_5d_base_v126_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(45).var().rolling(12).mean().rolling(23).std() * 0.626652
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc126_5d_base_v126_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc126_5d_base_v126_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc127_200d_base_v127_signal(fcf, sharesbas):
    res = (fcf * 9.9270 - sharesbas).diff(29).diff(47) * 0.773779
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc127_200d_base_v127_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc127_200d_base_v127_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc128_126d_base_v128_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 9.8653)).rolling(32).max().rolling(11).min().rolling(48).mean().pct_change(30) * 0.715207
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc128_126d_base_v128_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc128_126d_base_v128_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc129_10d_base_v129_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(28).std().rolling(21).var() * 0.042915
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc129_10d_base_v129_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc129_10d_base_v129_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc130_21d_base_v130_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(26).min().diff(26).rolling(24).min() * 0.394497
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc130_21d_base_v130_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc130_21d_base_v130_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_base_v131_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(7).mean().rolling(11).max() * 0.144750
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_base_v131_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_base_v131_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc132_21d_base_v132_signal(fcf, sharesbas):
    res = (fcf.diff(3) / (sharesbas.shift(2) + 1.6265)).diff(46).rolling(28).var() * 0.841392
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc132_21d_base_v132_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc132_21d_base_v132_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc133_84d_base_v133_signal(fcf, sharesbas):
    res = (fcf.diff(5) / (sharesbas.shift(2) + 7.9687)).rolling(24).min().rolling(24).max().diff(2) * 0.559606
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc133_84d_base_v133_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc133_84d_base_v133_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc134_10d_base_v134_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 3.9296)).pct_change(49).rolling(46).max().rolling(5).min().rolling(10).min() * 0.392713
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc134_10d_base_v134_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc134_10d_base_v134_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc135_105d_base_v135_signal(fcf, sharesbas):
    res = (fcf.diff(8) / (sharesbas.shift(3) + 8.9618)).rolling(45).min().pct_change(45).pct_change(20).rolling(27).mean() * 0.262466
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc135_105d_base_v135_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc135_105d_base_v135_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc136_200d_base_v136_signal(fcf, sharesbas):
    res = (fcf.diff(4) / (sharesbas.shift(5) + 7.6394)).pct_change(7).pct_change(25).rolling(46).max().pct_change(9) * 0.408390
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc136_200d_base_v136_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc136_200d_base_v136_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc137_10d_base_v137_signal(fcf, sharesbas):
    res = (fcf * 5.9020 - sharesbas).rolling(11).max().rolling(33).std().rolling(38).max() * 0.124270
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc137_10d_base_v137_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc137_10d_base_v137_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc138_10d_base_v138_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(24).pct_change(2).rolling(37).var().rolling(28).var() * 0.546789
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc138_10d_base_v138_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc138_10d_base_v138_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc139_126d_base_v139_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(26).rolling(10).var().rolling(35).mean() * 0.255386
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc139_126d_base_v139_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc139_126d_base_v139_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc140_10d_base_v140_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(44).pct_change(50) * 0.965961
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc140_10d_base_v140_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc140_10d_base_v140_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc141_63d_base_v141_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 0.1390)).rolling(24).min().rolling(45).min().rolling(14).max().rolling(21).mean() * 0.495170
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc141_63d_base_v141_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc141_63d_base_v141_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc142_63d_base_v142_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(27).rolling(44).std() * 0.156121
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc142_63d_base_v142_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc142_63d_base_v142_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc143_252d_base_v143_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(7).diff(2) * 0.743145
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc143_252d_base_v143_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc143_252d_base_v143_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc144_126d_base_v144_signal(fcf, sharesbas):
    res = (fcf * 5.6126 - sharesbas).rolling(19).min().rolling(20).std() * 0.636190
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc144_126d_base_v144_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc144_126d_base_v144_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc145_10d_base_v145_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 2.6437)).rolling(9).var().rolling(23).mean() * 0.118542
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc145_10d_base_v145_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc145_10d_base_v145_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc146_63d_base_v146_signal(fcf, sharesbas):
    res = (fcf.diff(6) / (sharesbas.shift(2) + 2.1844)).rolling(12).var().rolling(30).std().rolling(50).min().pct_change(4) * 0.237631
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc146_63d_base_v146_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc146_63d_base_v146_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc147_150d_base_v147_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(41).var().pct_change(6).rolling(10).min().pct_change(24) * 0.521737
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc147_150d_base_v147_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc147_150d_base_v147_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc148_5d_base_v148_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(12).min().pct_change(31).rolling(27).var() * 0.360962
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc148_5d_base_v148_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc148_5d_base_v148_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc149_150d_base_v149_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(47).var().pct_change(14).rolling(12).var().pct_change(6) * 0.790687
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc149_150d_base_v149_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc149_150d_base_v149_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc150_252d_base_v150_signal(fcf, sharesbas):
    res = (fcf * 1.2484 - sharesbas).rolling(27).max().diff(47) * 0.526038
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc150_252d_base_v150_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc150_252d_base_v150_signal


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
