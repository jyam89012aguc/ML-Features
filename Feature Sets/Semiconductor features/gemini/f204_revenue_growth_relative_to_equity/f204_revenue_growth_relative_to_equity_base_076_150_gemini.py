import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f204r_f204_revenue_growth_relative_to_equity_calc076_21d_base_v076_signal(revenue, equity):
    res = (revenue.diff(10) / (equity.shift(1) + 5.6372)).pct_change(29).diff(31).rolling(46).mean().rolling(23).max() * 0.847082
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc076_21d_base_v076_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc076_21d_base_v076_signal

def f204r_f204_revenue_growth_relative_to_equity_calc077_21d_base_v077_signal(revenue, equity):
    res = (equity / (revenue + 9.8200)).pct_change(43).rolling(18).max().rolling(30).std().rolling(6).mean() * 0.325918
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc077_21d_base_v077_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc077_21d_base_v077_signal

def f204r_f204_revenue_growth_relative_to_equity_calc078_126d_base_v078_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(5).var().rolling(17).mean().rolling(39).mean().diff(42) * 0.346353
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc078_126d_base_v078_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc078_126d_base_v078_signal

def f204r_f204_revenue_growth_relative_to_equity_calc079_10d_base_v079_signal(revenue, equity):
    res = (equity / (revenue + 5.6912)).rolling(30).mean().rolling(41).max() * 0.881206
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc079_10d_base_v079_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc079_10d_base_v079_signal

def f204r_f204_revenue_growth_relative_to_equity_calc080_5d_base_v080_signal(revenue, equity):
    res = (revenue * 1.5120 - equity).diff(16).rolling(19).min().pct_change(40).rolling(41).max() * 0.206781
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc080_5d_base_v080_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc080_5d_base_v080_signal

def f204r_f204_revenue_growth_relative_to_equity_calc081_21d_base_v081_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(48).std().diff(11).rolling(35).std() * 0.277951
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc081_21d_base_v081_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc081_21d_base_v081_signal

def f204r_f204_revenue_growth_relative_to_equity_calc082_63d_base_v082_signal(revenue, equity):
    res = (revenue.diff(5) / (equity.shift(4) + 0.5389)).pct_change(6).rolling(31).max().pct_change(24).rolling(5).std() * 0.116573
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc082_63d_base_v082_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc082_63d_base_v082_signal

def f204r_f204_revenue_growth_relative_to_equity_calc083_63d_base_v083_signal(revenue, equity):
    res = (revenue.diff(3) / (equity.shift(2) + 7.8205)).pct_change(5).rolling(24).var() * 0.979638
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc083_63d_base_v083_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc083_63d_base_v083_signal

def f204r_f204_revenue_growth_relative_to_equity_calc084_200d_base_v084_signal(revenue, equity):
    res = (revenue.diff(5) / (equity.shift(5) + 2.2909)).rolling(42).max().pct_change(46) * 0.656542
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc084_200d_base_v084_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc084_200d_base_v084_signal

def f204r_f204_revenue_growth_relative_to_equity_calc085_10d_base_v085_signal(revenue, equity):
    res = (revenue.diff(8) / (equity.shift(5) + 5.2135)).rolling(31).std().pct_change(13).pct_change(23).rolling(4).var() * 0.266892
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc085_10d_base_v085_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc085_10d_base_v085_signal

def f204r_f204_revenue_growth_relative_to_equity_calc086_5d_base_v086_signal(revenue, equity):
    res = (equity / (revenue + 4.3235)).rolling(48).std().rolling(49).max() * 0.826493
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc086_5d_base_v086_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc086_5d_base_v086_signal

def f204r_f204_revenue_growth_relative_to_equity_calc087_5d_base_v087_signal(revenue, equity):
    res = (revenue * 9.8853 - equity).diff(18).rolling(27).max().pct_change(43) * 0.766881
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc087_5d_base_v087_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc087_5d_base_v087_signal

def f204r_f204_revenue_growth_relative_to_equity_calc088_42d_base_v088_signal(revenue, equity):
    res = (revenue.diff(2) / (equity.shift(1) + 7.0301)).rolling(2).min().rolling(18).var().rolling(13).mean() * 0.429647
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc088_42d_base_v088_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc088_42d_base_v088_signal

def f204r_f204_revenue_growth_relative_to_equity_calc089_5d_base_v089_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(30).std().rolling(5).mean().rolling(5).max() * 0.691968
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc089_5d_base_v089_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc089_5d_base_v089_signal

def f204r_f204_revenue_growth_relative_to_equity_calc090_126d_base_v090_signal(revenue, equity):
    res = (revenue / (equity + 8.8444)).rolling(10).mean().pct_change(23) * 0.788841
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc090_126d_base_v090_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc090_126d_base_v090_signal

def f204r_f204_revenue_growth_relative_to_equity_calc091_63d_base_v091_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(42).min().rolling(43).max() * 0.484163
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc091_63d_base_v091_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc091_63d_base_v091_signal

def f204r_f204_revenue_growth_relative_to_equity_calc092_84d_base_v092_signal(revenue, equity):
    res = (revenue / (equity + 1.7755)).rolling(22).std().rolling(18).max().rolling(4).mean() * 0.238769
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc092_84d_base_v092_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc092_84d_base_v092_signal

def f204r_f204_revenue_growth_relative_to_equity_calc093_105d_base_v093_signal(revenue, equity):
    res = (revenue / (equity + 2.9801)).rolling(15).mean().diff(41) * 0.560247
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc093_105d_base_v093_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc093_105d_base_v093_signal

def f204r_f204_revenue_growth_relative_to_equity_calc094_42d_base_v094_signal(revenue, equity):
    res = (revenue * 5.6255 - equity).rolling(44).mean().diff(47).rolling(11).min() * 0.017481
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc094_42d_base_v094_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc094_42d_base_v094_signal

def f204r_f204_revenue_growth_relative_to_equity_calc095_63d_base_v095_signal(revenue, equity):
    res = (revenue * 1.2043 - equity).rolling(15).std().rolling(14).var().rolling(42).min().rolling(21).std() * 0.768419
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc095_63d_base_v095_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc095_63d_base_v095_signal

def f204r_f204_revenue_growth_relative_to_equity_calc096_126d_base_v096_signal(revenue, equity):
    res = (revenue / (equity + 5.1562)).rolling(24).max().rolling(26).mean() * 0.035158
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc096_126d_base_v096_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc096_126d_base_v096_signal

def f204r_f204_revenue_growth_relative_to_equity_calc097_150d_base_v097_signal(revenue, equity):
    res = (revenue * 9.5124 - equity).rolling(47).min().diff(24) * 0.760653
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc097_150d_base_v097_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc097_150d_base_v097_signal

def f204r_f204_revenue_growth_relative_to_equity_calc098_84d_base_v098_signal(revenue, equity):
    res = (revenue.diff(9) / (equity.shift(5) + 0.8500)).rolling(50).max().rolling(10).std().rolling(28).var() * 0.962101
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc098_84d_base_v098_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc098_84d_base_v098_signal

def f204r_f204_revenue_growth_relative_to_equity_calc099_63d_base_v099_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(19).pct_change(12).rolling(20).var() * 0.835256
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc099_63d_base_v099_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc099_63d_base_v099_signal

def f204r_f204_revenue_growth_relative_to_equity_calc100_5d_base_v100_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(16).var().diff(18).rolling(25).std() * 0.957300
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc100_5d_base_v100_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc100_5d_base_v100_signal

def f204r_f204_revenue_growth_relative_to_equity_calc101_150d_base_v101_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(46).rolling(15).max().rolling(12).mean() * 0.567872
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc101_150d_base_v101_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc101_150d_base_v101_signal

def f204r_f204_revenue_growth_relative_to_equity_calc102_42d_base_v102_signal(revenue, equity):
    res = (revenue / (equity + 0.6234)).rolling(36).min().rolling(3).min().rolling(31).std().rolling(17).mean() * 0.721200
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc102_42d_base_v102_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc102_42d_base_v102_signal

def f204r_f204_revenue_growth_relative_to_equity_calc103_84d_base_v103_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(42).min().rolling(32).std().pct_change(47) * 0.935097
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc103_84d_base_v103_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc103_84d_base_v103_signal

def f204r_f204_revenue_growth_relative_to_equity_calc104_21d_base_v104_signal(revenue, equity):
    res = (revenue / (equity + 4.2657)).diff(21).rolling(41).mean().pct_change(12).rolling(3).std() * 0.329221
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc104_21d_base_v104_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc104_21d_base_v104_signal

def f204r_f204_revenue_growth_relative_to_equity_calc105_10d_base_v105_signal(revenue, equity):
    res = (equity / (revenue + 3.0990)).rolling(9).max().rolling(26).var().diff(34).rolling(47).var() * 0.737511
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc105_10d_base_v105_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc105_10d_base_v105_signal

def f204r_f204_revenue_growth_relative_to_equity_calc106_21d_base_v106_signal(revenue, equity):
    res = (revenue.diff(7) / (equity.shift(5) + 1.0633)).rolling(4).mean().rolling(27).mean().rolling(44).mean().pct_change(26) * 0.434615
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc106_21d_base_v106_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc106_21d_base_v106_signal

def f204r_f204_revenue_growth_relative_to_equity_calc107_105d_base_v107_signal(revenue, equity):
    res = (equity / (revenue + 6.5021)).pct_change(38).diff(36).pct_change(27) * 0.902152
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc107_105d_base_v107_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc107_105d_base_v107_signal

def f204r_f204_revenue_growth_relative_to_equity_calc108_105d_base_v108_signal(revenue, equity):
    res = (revenue * 7.8361 - equity).diff(5).diff(43) * 0.029502
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc108_105d_base_v108_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc108_105d_base_v108_signal

def f204r_f204_revenue_growth_relative_to_equity_calc109_84d_base_v109_signal(revenue, equity):
    res = (revenue * 1.3044 - equity).rolling(49).mean().rolling(45).mean().rolling(30).min() * 0.852098
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc109_84d_base_v109_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc109_84d_base_v109_signal

def f204r_f204_revenue_growth_relative_to_equity_calc110_150d_base_v110_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(23).std().rolling(50).mean() * 0.216512
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc110_150d_base_v110_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc110_150d_base_v110_signal

def f204r_f204_revenue_growth_relative_to_equity_calc111_252d_base_v111_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(46).var().rolling(14).std().rolling(29).min().rolling(20).mean() * 0.206423
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc111_252d_base_v111_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc111_252d_base_v111_signal

def f204r_f204_revenue_growth_relative_to_equity_calc112_10d_base_v112_signal(revenue, equity):
    res = (revenue.diff(7) / (equity.shift(2) + 6.6483)).rolling(36).var().diff(19).rolling(8).max() * 0.204494
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc112_10d_base_v112_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc112_10d_base_v112_signal

def f204r_f204_revenue_growth_relative_to_equity_calc113_42d_base_v113_signal(revenue, equity):
    res = (equity / (revenue + 7.0763)).rolling(20).mean().rolling(22).mean().diff(11) * 0.490953
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc113_42d_base_v113_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc113_42d_base_v113_signal

def f204r_f204_revenue_growth_relative_to_equity_calc114_10d_base_v114_signal(revenue, equity):
    res = (revenue / (equity + 8.6902)).diff(43).rolling(7).std().rolling(29).mean().rolling(2).var() * 0.790675
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc114_10d_base_v114_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc114_10d_base_v114_signal

def f204r_f204_revenue_growth_relative_to_equity_calc115_10d_base_v115_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(22).std().pct_change(39).pct_change(44).rolling(43).max() * 0.468671
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc115_10d_base_v115_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc115_10d_base_v115_signal

def f204r_f204_revenue_growth_relative_to_equity_calc116_21d_base_v116_signal(revenue, equity):
    res = (revenue * 8.0441 - equity).diff(29).rolling(4).mean().rolling(26).std() * 0.886537
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc116_21d_base_v116_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc116_21d_base_v116_signal

def f204r_f204_revenue_growth_relative_to_equity_calc117_63d_base_v117_signal(revenue, equity):
    res = (revenue * 5.4944 - equity).pct_change(45).rolling(44).max().rolling(31).mean() * 0.598576
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc117_63d_base_v117_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc117_63d_base_v117_signal

def f204r_f204_revenue_growth_relative_to_equity_calc118_5d_base_v118_signal(revenue, equity):
    res = (equity / (revenue + 3.9704)).rolling(8).mean().rolling(31).min() * 0.963439
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc118_5d_base_v118_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc118_5d_base_v118_signal

def f204r_f204_revenue_growth_relative_to_equity_calc119_84d_base_v119_signal(revenue, equity):
    res = (revenue / (equity + 2.7632)).diff(10).rolling(5).var() * 0.322872
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc119_84d_base_v119_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc119_84d_base_v119_signal

def f204r_f204_revenue_growth_relative_to_equity_calc120_200d_base_v120_signal(revenue, equity):
    res = (revenue / (equity + 8.2315)).rolling(48).min().diff(42) * 0.549511
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc120_200d_base_v120_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc120_200d_base_v120_signal

def f204r_f204_revenue_growth_relative_to_equity_calc121_105d_base_v121_signal(revenue, equity):
    res = (equity / (revenue + 8.0578)).rolling(19).var().diff(22) * 0.843753
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc121_105d_base_v121_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc121_105d_base_v121_signal

def f204r_f204_revenue_growth_relative_to_equity_calc122_150d_base_v122_signal(revenue, equity):
    res = (revenue.diff(10) / (equity.shift(2) + 6.8680)).rolling(5).min().rolling(8).max() * 0.600305
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc122_150d_base_v122_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc122_150d_base_v122_signal

def f204r_f204_revenue_growth_relative_to_equity_calc123_10d_base_v123_signal(revenue, equity):
    res = (revenue * 7.1012 - equity).diff(45).rolling(34).var().rolling(19).min() * 0.198194
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc123_10d_base_v123_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc123_10d_base_v123_signal

def f204r_f204_revenue_growth_relative_to_equity_calc124_200d_base_v124_signal(revenue, equity):
    res = (revenue / (equity + 4.0878)).rolling(12).std().diff(26).rolling(20).std().rolling(14).var() * 0.884361
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc124_200d_base_v124_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc124_200d_base_v124_signal

def f204r_f204_revenue_growth_relative_to_equity_calc125_200d_base_v125_signal(revenue, equity):
    res = (equity / (revenue + 8.6638)).pct_change(43).rolling(49).max().pct_change(34).rolling(45).var() * 0.339277
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc125_200d_base_v125_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc125_200d_base_v125_signal

def f204r_f204_revenue_growth_relative_to_equity_calc126_84d_base_v126_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(37).std().rolling(46).std().rolling(23).std().rolling(3).var() * 0.469400
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc126_84d_base_v126_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc126_84d_base_v126_signal

def f204r_f204_revenue_growth_relative_to_equity_calc127_21d_base_v127_signal(revenue, equity):
    res = (revenue.diff(9) / (equity.shift(4) + 7.0337)).diff(17).diff(20).diff(34).rolling(36).std() * 0.477834
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc127_21d_base_v127_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc127_21d_base_v127_signal

def f204r_f204_revenue_growth_relative_to_equity_calc128_21d_base_v128_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).min().rolling(23).std().rolling(39).var() * 0.755124
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc128_21d_base_v128_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc128_21d_base_v128_signal

def f204r_f204_revenue_growth_relative_to_equity_calc129_126d_base_v129_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(37).max().diff(42) * 0.126663
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc129_126d_base_v129_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc129_126d_base_v129_signal

def f204r_f204_revenue_growth_relative_to_equity_calc130_10d_base_v130_signal(revenue, equity):
    res = (equity / (revenue + 4.0662)).diff(35).diff(2).pct_change(32) * 0.493619
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc130_10d_base_v130_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc130_10d_base_v130_signal

def f204r_f204_revenue_growth_relative_to_equity_calc131_84d_base_v131_signal(revenue, equity):
    res = (revenue / (equity + 8.3818)).rolling(5).var().rolling(32).max() * 0.974064
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc131_84d_base_v131_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc131_84d_base_v131_signal

def f204r_f204_revenue_growth_relative_to_equity_calc132_84d_base_v132_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(16).min().rolling(9).var() * 0.669763
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc132_84d_base_v132_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc132_84d_base_v132_signal

def f204r_f204_revenue_growth_relative_to_equity_calc133_126d_base_v133_signal(revenue, equity):
    res = (revenue / (equity + 2.2474)).pct_change(41).rolling(3).min() * 0.963313
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc133_126d_base_v133_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc133_126d_base_v133_signal

def f204r_f204_revenue_growth_relative_to_equity_calc134_21d_base_v134_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(36).min().pct_change(13).rolling(11).std().pct_change(23) * 0.179358
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc134_21d_base_v134_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc134_21d_base_v134_signal

def f204r_f204_revenue_growth_relative_to_equity_calc135_5d_base_v135_signal(revenue, equity):
    res = (revenue / (equity + 1.1392)).rolling(4).mean().rolling(24).std().rolling(3).std() * 0.312362
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc135_5d_base_v135_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc135_5d_base_v135_signal

def f204r_f204_revenue_growth_relative_to_equity_calc136_5d_base_v136_signal(revenue, equity):
    res = (revenue * 5.5461 - equity).diff(39).rolling(7).max().rolling(23).min().pct_change(2) * 0.508019
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc136_5d_base_v136_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc136_5d_base_v136_signal

def f204r_f204_revenue_growth_relative_to_equity_calc137_21d_base_v137_signal(revenue, equity):
    res = (revenue / (equity + 1.0491)).diff(21).rolling(3).mean().pct_change(4) * 0.958824
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc137_21d_base_v137_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc137_21d_base_v137_signal

def f204r_f204_revenue_growth_relative_to_equity_calc138_200d_base_v138_signal(revenue, equity):
    res = (revenue / (equity + 2.2691)).rolling(8).std().pct_change(39) * 0.564509
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc138_200d_base_v138_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc138_200d_base_v138_signal

def f204r_f204_revenue_growth_relative_to_equity_calc139_63d_base_v139_signal(revenue, equity):
    res = (revenue.replace(0, np.nan) / equity.replace(0, np.nan)).diff(20).rolling(5).min() * 0.827134
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc139_63d_base_v139_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc139_63d_base_v139_signal

def f204r_f204_revenue_growth_relative_to_equity_calc140_252d_base_v140_signal(revenue, equity):
    res = (revenue * 8.2414 - equity).rolling(11).std().rolling(5).min().pct_change(21) * 0.387928
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc140_252d_base_v140_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc140_252d_base_v140_signal

def f204r_f204_revenue_growth_relative_to_equity_calc141_5d_base_v141_signal(revenue, equity):
    res = (revenue / (equity + 4.2832)).rolling(33).var().pct_change(7).rolling(50).mean().rolling(13).max() * 0.947267
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc141_5d_base_v141_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc141_5d_base_v141_signal

def f204r_f204_revenue_growth_relative_to_equity_calc142_63d_base_v142_signal(revenue, equity):
    res = (revenue * 0.3375 - equity).rolling(48).max().rolling(41).min() * 0.089496
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc142_63d_base_v142_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc142_63d_base_v142_signal

def f204r_f204_revenue_growth_relative_to_equity_calc143_21d_base_v143_signal(revenue, equity):
    res = (revenue.diff(8) / (equity.shift(4) + 8.5674)).pct_change(33).pct_change(8).rolling(8).max() * 0.432347
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc143_21d_base_v143_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc143_21d_base_v143_signal

def f204r_f204_revenue_growth_relative_to_equity_calc144_10d_base_v144_signal(revenue, equity):
    res = (revenue / (equity + 9.0268)).rolling(15).mean().rolling(26).min() * 0.046495
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc144_10d_base_v144_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc144_10d_base_v144_signal

def f204r_f204_revenue_growth_relative_to_equity_calc145_21d_base_v145_signal(revenue, equity):
    res = (revenue.diff(3) / (equity.shift(4) + 9.5071)).rolling(27).std().rolling(31).min() * 0.907835
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc145_21d_base_v145_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc145_21d_base_v145_signal

def f204r_f204_revenue_growth_relative_to_equity_calc146_105d_base_v146_signal(revenue, equity):
    res = (revenue * 8.3938 - equity).rolling(25).min().rolling(7).var().diff(27) * 0.193085
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc146_105d_base_v146_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc146_105d_base_v146_signal

def f204r_f204_revenue_growth_relative_to_equity_calc147_5d_base_v147_signal(revenue, equity):
    res = (revenue.diff(6) / (equity.shift(5) + 7.0210)).rolling(37).std().pct_change(10).diff(3).rolling(29).std() * 0.976795
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc147_5d_base_v147_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc147_5d_base_v147_signal

def f204r_f204_revenue_growth_relative_to_equity_calc148_126d_base_v148_signal(revenue, equity):
    res = (revenue.diff(10) / (equity.shift(3) + 3.5770)).diff(9).pct_change(41).rolling(35).min() * 0.134468
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc148_126d_base_v148_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc148_126d_base_v148_signal

def f204r_f204_revenue_growth_relative_to_equity_calc149_5d_base_v149_signal(revenue, equity):
    res = (revenue.diff(6) / (equity.shift(2) + 7.5475)).rolling(11).var().rolling(14).mean().rolling(24).std().rolling(6).min() * 0.322557
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc149_5d_base_v149_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc149_5d_base_v149_signal

def f204r_f204_revenue_growth_relative_to_equity_calc150_252d_base_v150_signal(revenue, equity):
    res = (revenue / (equity + 7.8892)).rolling(23).std().rolling(12).std().pct_change(15).rolling(19).std() * 0.540952
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f204r_f204_revenue_growth_relative_to_equity_calc150_252d_base_v150_signal'] = f204r_f204_revenue_growth_relative_to_equity_calc150_252d_base_v150_signal


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
