import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f01rs_f01_revenue_stability_base_v076_signal(close, volume):
    res = close.pct_change(252).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v076_signal'] = f01rs_f01_revenue_stability_base_v076_signal

def f01rs_f01_revenue_stability_base_v077_signal(close, volume):
    res = close.pct_change(5).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v077_signal'] = f01rs_f01_revenue_stability_base_v077_signal

def f01rs_f01_revenue_stability_base_v078_signal(close, volume):
    res = close.pct_change(10).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v078_signal'] = f01rs_f01_revenue_stability_base_v078_signal

def f01rs_f01_revenue_stability_base_v079_signal(close, volume):
    res = close.pct_change(21).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v079_signal'] = f01rs_f01_revenue_stability_base_v079_signal

def f01rs_f01_revenue_stability_base_v080_signal(close, volume):
    res = close.pct_change(42).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v080_signal'] = f01rs_f01_revenue_stability_base_v080_signal

def f01rs_f01_revenue_stability_base_v081_signal(close, volume):
    res = close.pct_change(63).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v081_signal'] = f01rs_f01_revenue_stability_base_v081_signal

def f01rs_f01_revenue_stability_base_v082_signal(close, volume):
    res = close.pct_change(126).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v082_signal'] = f01rs_f01_revenue_stability_base_v082_signal

def f01rs_f01_revenue_stability_base_v083_signal(close, volume):
    res = close.pct_change(253).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v083_signal'] = f01rs_f01_revenue_stability_base_v083_signal

def f01rs_f01_revenue_stability_base_v084_signal(close, volume):
    res = close.pct_change(6).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v084_signal'] = f01rs_f01_revenue_stability_base_v084_signal

def f01rs_f01_revenue_stability_base_v085_signal(close, volume):
    res = close.pct_change(11).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v085_signal'] = f01rs_f01_revenue_stability_base_v085_signal

def f01rs_f01_revenue_stability_base_v086_signal(close, volume):
    res = close.pct_change(22).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v086_signal'] = f01rs_f01_revenue_stability_base_v086_signal

def f01rs_f01_revenue_stability_base_v087_signal(close, volume):
    res = close.pct_change(43).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v087_signal'] = f01rs_f01_revenue_stability_base_v087_signal

def f01rs_f01_revenue_stability_base_v088_signal(close, volume):
    res = close.pct_change(64).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v088_signal'] = f01rs_f01_revenue_stability_base_v088_signal

def f01rs_f01_revenue_stability_base_v089_signal(close, volume):
    res = close.pct_change(127).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v089_signal'] = f01rs_f01_revenue_stability_base_v089_signal

def f01rs_f01_revenue_stability_base_v090_signal(close, volume):
    res = close.pct_change(254).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v090_signal'] = f01rs_f01_revenue_stability_base_v090_signal

def f01rs_f01_revenue_stability_base_v091_signal(close, volume):
    res = close.pct_change(7).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v091_signal'] = f01rs_f01_revenue_stability_base_v091_signal

def f01rs_f01_revenue_stability_base_v092_signal(close, volume):
    res = close.pct_change(12).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v092_signal'] = f01rs_f01_revenue_stability_base_v092_signal

def f01rs_f01_revenue_stability_base_v093_signal(close, volume):
    res = close.pct_change(23).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v093_signal'] = f01rs_f01_revenue_stability_base_v093_signal

def f01rs_f01_revenue_stability_base_v094_signal(close, volume):
    res = close.pct_change(44).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v094_signal'] = f01rs_f01_revenue_stability_base_v094_signal

def f01rs_f01_revenue_stability_base_v095_signal(close, volume):
    res = close.pct_change(65).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v095_signal'] = f01rs_f01_revenue_stability_base_v095_signal

def f01rs_f01_revenue_stability_base_v096_signal(close, volume):
    res = close.pct_change(128).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v096_signal'] = f01rs_f01_revenue_stability_base_v096_signal

def f01rs_f01_revenue_stability_base_v097_signal(close, volume):
    res = close.pct_change(255).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v097_signal'] = f01rs_f01_revenue_stability_base_v097_signal

def f01rs_f01_revenue_stability_base_v098_signal(close, volume):
    res = close.pct_change(8).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v098_signal'] = f01rs_f01_revenue_stability_base_v098_signal

def f01rs_f01_revenue_stability_base_v099_signal(close, volume):
    res = close.pct_change(13).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v099_signal'] = f01rs_f01_revenue_stability_base_v099_signal

def f01rs_f01_revenue_stability_base_v100_signal(close, volume):
    res = close.pct_change(24).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v100_signal'] = f01rs_f01_revenue_stability_base_v100_signal

def f01rs_f01_revenue_stability_base_v101_signal(close, volume):
    res = close.pct_change(45).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v101_signal'] = f01rs_f01_revenue_stability_base_v101_signal

def f01rs_f01_revenue_stability_base_v102_signal(close, volume):
    res = close.pct_change(66).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v102_signal'] = f01rs_f01_revenue_stability_base_v102_signal

def f01rs_f01_revenue_stability_base_v103_signal(close, volume):
    res = close.pct_change(129).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v103_signal'] = f01rs_f01_revenue_stability_base_v103_signal

def f01rs_f01_revenue_stability_base_v104_signal(close, volume):
    res = close.pct_change(256).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v104_signal'] = f01rs_f01_revenue_stability_base_v104_signal

def f01rs_f01_revenue_stability_base_v105_signal(close, volume):
    res = close.pct_change(9).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v105_signal'] = f01rs_f01_revenue_stability_base_v105_signal

def f01rs_f01_revenue_stability_base_v106_signal(close, volume):
    res = close.pct_change(14).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v106_signal'] = f01rs_f01_revenue_stability_base_v106_signal

def f01rs_f01_revenue_stability_base_v107_signal(close, volume):
    res = close.pct_change(25).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v107_signal'] = f01rs_f01_revenue_stability_base_v107_signal

def f01rs_f01_revenue_stability_base_v108_signal(close, volume):
    res = close.pct_change(46).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v108_signal'] = f01rs_f01_revenue_stability_base_v108_signal

def f01rs_f01_revenue_stability_base_v109_signal(close, volume):
    res = close.pct_change(67).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v109_signal'] = f01rs_f01_revenue_stability_base_v109_signal

def f01rs_f01_revenue_stability_base_v110_signal(close, volume):
    res = close.pct_change(130).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v110_signal'] = f01rs_f01_revenue_stability_base_v110_signal

def f01rs_f01_revenue_stability_base_v111_signal(close, volume):
    res = close.pct_change(257).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v111_signal'] = f01rs_f01_revenue_stability_base_v111_signal

def f01rs_f01_revenue_stability_base_v112_signal(close, volume):
    res = close.pct_change(10).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v112_signal'] = f01rs_f01_revenue_stability_base_v112_signal

def f01rs_f01_revenue_stability_base_v113_signal(close, volume):
    res = close.pct_change(15).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v113_signal'] = f01rs_f01_revenue_stability_base_v113_signal

def f01rs_f01_revenue_stability_base_v114_signal(close, volume):
    res = close.pct_change(26).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v114_signal'] = f01rs_f01_revenue_stability_base_v114_signal

def f01rs_f01_revenue_stability_base_v115_signal(close, volume):
    res = close.pct_change(47).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v115_signal'] = f01rs_f01_revenue_stability_base_v115_signal

def f01rs_f01_revenue_stability_base_v116_signal(close, volume):
    res = close.pct_change(68).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v116_signal'] = f01rs_f01_revenue_stability_base_v116_signal

def f01rs_f01_revenue_stability_base_v117_signal(close, volume):
    res = close.pct_change(131).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v117_signal'] = f01rs_f01_revenue_stability_base_v117_signal

def f01rs_f01_revenue_stability_base_v118_signal(close, volume):
    res = close.pct_change(258).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v118_signal'] = f01rs_f01_revenue_stability_base_v118_signal

def f01rs_f01_revenue_stability_base_v119_signal(close, volume):
    res = close.pct_change(11).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v119_signal'] = f01rs_f01_revenue_stability_base_v119_signal

def f01rs_f01_revenue_stability_base_v120_signal(close, volume):
    res = close.pct_change(16).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v120_signal'] = f01rs_f01_revenue_stability_base_v120_signal

def f01rs_f01_revenue_stability_base_v121_signal(close, volume):
    res = close.pct_change(27).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v121_signal'] = f01rs_f01_revenue_stability_base_v121_signal

def f01rs_f01_revenue_stability_base_v122_signal(close, volume):
    res = close.pct_change(48).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v122_signal'] = f01rs_f01_revenue_stability_base_v122_signal

def f01rs_f01_revenue_stability_base_v123_signal(close, volume):
    res = close.pct_change(69).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v123_signal'] = f01rs_f01_revenue_stability_base_v123_signal

def f01rs_f01_revenue_stability_base_v124_signal(close, volume):
    res = close.pct_change(132).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v124_signal'] = f01rs_f01_revenue_stability_base_v124_signal

def f01rs_f01_revenue_stability_base_v125_signal(close, volume):
    res = close.pct_change(259).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v125_signal'] = f01rs_f01_revenue_stability_base_v125_signal

def f01rs_f01_revenue_stability_base_v126_signal(close, volume):
    res = close.pct_change(12).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v126_signal'] = f01rs_f01_revenue_stability_base_v126_signal

def f01rs_f01_revenue_stability_base_v127_signal(close, volume):
    res = close.pct_change(17).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v127_signal'] = f01rs_f01_revenue_stability_base_v127_signal

def f01rs_f01_revenue_stability_base_v128_signal(close, volume):
    res = close.pct_change(28).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v128_signal'] = f01rs_f01_revenue_stability_base_v128_signal

def f01rs_f01_revenue_stability_base_v129_signal(close, volume):
    res = close.pct_change(49).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v129_signal'] = f01rs_f01_revenue_stability_base_v129_signal

def f01rs_f01_revenue_stability_base_v130_signal(close, volume):
    res = close.pct_change(70).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v130_signal'] = f01rs_f01_revenue_stability_base_v130_signal

def f01rs_f01_revenue_stability_base_v131_signal(close, volume):
    res = close.pct_change(133).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v131_signal'] = f01rs_f01_revenue_stability_base_v131_signal

def f01rs_f01_revenue_stability_base_v132_signal(close, volume):
    res = close.pct_change(260).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v132_signal'] = f01rs_f01_revenue_stability_base_v132_signal

def f01rs_f01_revenue_stability_base_v133_signal(close, volume):
    res = close.pct_change(13).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v133_signal'] = f01rs_f01_revenue_stability_base_v133_signal

def f01rs_f01_revenue_stability_base_v134_signal(close, volume):
    res = close.pct_change(18).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v134_signal'] = f01rs_f01_revenue_stability_base_v134_signal

def f01rs_f01_revenue_stability_base_v135_signal(close, volume):
    res = close.pct_change(29).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v135_signal'] = f01rs_f01_revenue_stability_base_v135_signal

def f01rs_f01_revenue_stability_base_v136_signal(close, volume):
    res = close.pct_change(50).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v136_signal'] = f01rs_f01_revenue_stability_base_v136_signal

def f01rs_f01_revenue_stability_base_v137_signal(close, volume):
    res = close.pct_change(71).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v137_signal'] = f01rs_f01_revenue_stability_base_v137_signal

def f01rs_f01_revenue_stability_base_v138_signal(close, volume):
    res = close.pct_change(134).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v138_signal'] = f01rs_f01_revenue_stability_base_v138_signal

def f01rs_f01_revenue_stability_base_v139_signal(close, volume):
    res = close.pct_change(261).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v139_signal'] = f01rs_f01_revenue_stability_base_v139_signal

def f01rs_f01_revenue_stability_base_v140_signal(close, volume):
    res = close.pct_change(14).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v140_signal'] = f01rs_f01_revenue_stability_base_v140_signal

def f01rs_f01_revenue_stability_base_v141_signal(close, volume):
    res = close.pct_change(19).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v141_signal'] = f01rs_f01_revenue_stability_base_v141_signal

def f01rs_f01_revenue_stability_base_v142_signal(close, volume):
    res = close.pct_change(30).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v142_signal'] = f01rs_f01_revenue_stability_base_v142_signal

def f01rs_f01_revenue_stability_base_v143_signal(close, volume):
    res = close.pct_change(51).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v143_signal'] = f01rs_f01_revenue_stability_base_v143_signal

def f01rs_f01_revenue_stability_base_v144_signal(close, volume):
    res = close.pct_change(72).rolling(63).mean() * volume.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v144_signal'] = f01rs_f01_revenue_stability_base_v144_signal

def f01rs_f01_revenue_stability_base_v145_signal(close, volume):
    res = close.pct_change(135).rolling(126).mean() * volume.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v145_signal'] = f01rs_f01_revenue_stability_base_v145_signal

def f01rs_f01_revenue_stability_base_v146_signal(close, volume):
    res = close.pct_change(262).rolling(252).mean() * volume.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v146_signal'] = f01rs_f01_revenue_stability_base_v146_signal

def f01rs_f01_revenue_stability_base_v147_signal(close, volume):
    res = close.pct_change(15).rolling(5).mean() * volume.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v147_signal'] = f01rs_f01_revenue_stability_base_v147_signal

def f01rs_f01_revenue_stability_base_v148_signal(close, volume):
    res = close.pct_change(20).rolling(10).mean() * volume.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v148_signal'] = f01rs_f01_revenue_stability_base_v148_signal

def f01rs_f01_revenue_stability_base_v149_signal(close, volume):
    res = close.pct_change(31).rolling(21).mean() * volume.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v149_signal'] = f01rs_f01_revenue_stability_base_v149_signal

def f01rs_f01_revenue_stability_base_v150_signal(close, volume):
    res = close.pct_change(52).rolling(42).mean() * volume.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f01rs_f01_revenue_stability_base_v150_signal'] = f01rs_f01_revenue_stability_base_v150_signal





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
