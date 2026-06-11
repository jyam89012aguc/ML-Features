import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f212r_f212_revenue_to_cash_conversion_momentum_calc076_126d_base_v076_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(6) / ncfo.pct_change(16)).rolling(2).std()).rolling(26).mean()).rolling(17).var()).rolling(21).mean()) * 0.47309)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc076_126d_base_v076_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc076_126d_base_v076_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc077_126d_base_v077_signal(revenue, ncfo):
    res = ((((((revenue.diff(14) / (ncfo.shift(5) + 36.2398)).diff(19)).rolling(29).mean()).rolling(7).var()).rolling(3).max()) * 0.480876)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc077_126d_base_v077_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc077_126d_base_v077_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc078_10d_base_v078_signal(revenue, ncfo):
    res = (((((revenue.diff(5) / (ncfo.shift(6) + 32.0361)).rolling(22).min()).rolling(3).var()).rolling(11).var()) * 0.870751)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc078_10d_base_v078_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc078_10d_base_v078_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc079_63d_base_v079_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 63.9308)).rolling(29).var()).rolling(28).var()).pct_change(10)).rolling(23).var()) * 0.08529)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc079_63d_base_v079_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc079_63d_base_v079_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc080_126d_base_v080_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 68.8658)).rolling(13).var()).pct_change(16)).rolling(12).min()).rolling(5).std()) * 0.103917)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc080_126d_base_v080_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc080_126d_base_v080_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc081_10d_base_v081_signal(revenue, ncfo):
    res = ((((((revenue * 15.54 - ncfo).rolling(24).max()).pct_change(4)).rolling(16).min()).rolling(5).mean()) * 0.226691)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc081_10d_base_v081_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc081_10d_base_v081_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc082_252d_base_v082_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(26).max()).rolling(7).var()).diff(10)).rolling(25).mean()) * 0.027032)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc082_252d_base_v082_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc082_252d_base_v082_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc083_252d_base_v083_signal(revenue, ncfo):
    res = ((((ncfo / (revenue + 11.9478)).rolling(15).mean()).diff(4)) * 0.13614)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc083_252d_base_v083_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc083_252d_base_v083_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc084_5d_base_v084_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 1.9788)).rolling(20).max()).rolling(17).mean()).rolling(10).mean()).rolling(4).mean()) * 0.48457)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc084_5d_base_v084_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc084_5d_base_v084_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc085_21d_base_v085_signal(revenue, ncfo):
    res = ((((ncfo / (revenue + 66.7919)).diff(12)).rolling(4).mean()) * 0.749459)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc085_21d_base_v085_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc085_21d_base_v085_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc086_10d_base_v086_signal(revenue, ncfo):
    res = ((((((revenue * 84.6016 - ncfo).rolling(9).max()).rolling(20).max()).rolling(5).mean()).pct_change(19)) * 0.933008)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc086_10d_base_v086_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc086_10d_base_v086_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc087_252d_base_v087_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 1.497)).rolling(8).mean()).rolling(29).max()).diff(16)).rolling(24).var()) * 0.222658)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc087_252d_base_v087_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc087_252d_base_v087_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc088_63d_base_v088_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(9).max()).rolling(5).min()) * 0.670055)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc088_63d_base_v088_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc088_63d_base_v088_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc089_252d_base_v089_signal(revenue, ncfo):
    res = ((((((revenue.diff(4) / (ncfo.shift(9) + 98.4628)).rolling(19).var()).diff(2)).rolling(12).mean()).rolling(5).min()) * 0.131143)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc089_252d_base_v089_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc089_252d_base_v089_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_base_v090_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).pct_change(14)).rolling(29).std()).rolling(30).mean()) * 0.598382)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_base_v090_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc090_42d_base_v090_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc091_252d_base_v091_signal(revenue, ncfo):
    res = ((((revenue.pct_change(1) / ncfo.pct_change(16)).rolling(16).min()).rolling(23).max()) * 0.9303)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc091_252d_base_v091_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc091_252d_base_v091_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc092_126d_base_v092_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 8.5921)).rolling(12).std()).rolling(21).std()).pct_change(13)) * 0.1505)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc092_126d_base_v092_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc092_126d_base_v092_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc093_5d_base_v093_signal(revenue, ncfo):
    res = ((((((revenue.diff(16) / (ncfo.shift(5) + 23.3637)).rolling(13).min()).rolling(23).min()).rolling(14).max()).rolling(18).min()) * 0.42621)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc093_5d_base_v093_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc093_5d_base_v093_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc094_21d_base_v094_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 14.8227)).rolling(2).std()).rolling(25).mean()).rolling(28).mean()).rolling(17).mean()) * 0.455542)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc094_21d_base_v094_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc094_21d_base_v094_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc095_126d_base_v095_signal(revenue, ncfo):
    res = ((((((revenue * 2.7722 - ncfo).rolling(26).mean()).rolling(23).mean()).pct_change(17)).pct_change(16)) * 0.185514)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc095_126d_base_v095_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc095_126d_base_v095_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc096_252d_base_v096_signal(revenue, ncfo):
    res = (((((revenue * 46.6556 - ncfo).pct_change(18)).rolling(2).max()).pct_change(2)) * 0.297692)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc096_252d_base_v096_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc096_252d_base_v096_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc097_42d_base_v097_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(7).mean()).rolling(23).max()) * 0.126751)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc097_42d_base_v097_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc097_42d_base_v097_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc098_252d_base_v098_signal(revenue, ncfo):
    res = ((((((revenue.diff(6) / (ncfo.shift(8) + 77.9603)).rolling(17).min()).pct_change(4)).rolling(23).max()).rolling(23).min()) * 0.877006)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc098_252d_base_v098_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc098_252d_base_v098_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc099_63d_base_v099_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 68.5689)).rolling(17).var()).rolling(14).max()).rolling(23).max()) * 0.570766)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc099_63d_base_v099_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc099_63d_base_v099_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc100_21d_base_v100_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 76.6704)).rolling(27).var()).diff(19)).rolling(26).mean()) * 0.288749)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc100_21d_base_v100_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc100_21d_base_v100_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc101_126d_base_v101_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 34.1915)).rolling(9).std()).rolling(22).std()).rolling(20).var()).rolling(24).mean()) * 0.105403)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc101_126d_base_v101_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc101_126d_base_v101_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc102_5d_base_v102_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 86.9071)).diff(14)).rolling(18).max()).rolling(10).min()) * 0.122182)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc102_5d_base_v102_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc102_5d_base_v102_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_base_v103_signal(revenue, ncfo):
    res = ((((((revenue.diff(11) / (ncfo.shift(7) + 69.6263)).rolling(27).mean()).rolling(5).min()).diff(7)).rolling(17).var()) * 0.586229)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_base_v103_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc103_5d_base_v103_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc104_63d_base_v104_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(22).min()).pct_change(3)) * 0.66404)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc104_63d_base_v104_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc104_63d_base_v104_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc105_252d_base_v105_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(25).max()).rolling(24).mean()) * 0.219799)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc105_252d_base_v105_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc105_252d_base_v105_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc106_252d_base_v106_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(13).std()).pct_change(3)).diff(10)) * 0.590027)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc106_252d_base_v106_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc106_252d_base_v106_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc107_63d_base_v107_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(18).max()).rolling(23).min()).pct_change(18)) * 0.434252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc107_63d_base_v107_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc107_63d_base_v107_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc108_10d_base_v108_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 88.1016)).pct_change(15)).rolling(22).var()).rolling(27).max()).rolling(29).max()) * 0.625287)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc108_10d_base_v108_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc108_10d_base_v108_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_base_v109_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(6).std()).diff(10)) * 0.925943)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_base_v109_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc109_252d_base_v109_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc110_252d_base_v110_signal(revenue, ncfo):
    res = ((((((revenue.diff(3) / (ncfo.shift(4) + 43.5953)).rolling(10).std()).diff(20)).rolling(14).std()).rolling(5).std()) * 0.32228)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc110_252d_base_v110_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc110_252d_base_v110_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc111_10d_base_v111_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(2)).rolling(7).std()).rolling(6).var()) * 0.250675)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc111_10d_base_v111_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc111_10d_base_v111_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc112_5d_base_v112_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 25.9138)).pct_change(3)).rolling(21).var()) * 0.797467)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc112_5d_base_v112_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc112_5d_base_v112_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc113_21d_base_v113_signal(revenue, ncfo):
    res = ((((revenue.pct_change(3) / ncfo.pct_change(13)).rolling(5).std()).rolling(25).max()) * 0.892563)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc113_21d_base_v113_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc113_21d_base_v113_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc114_63d_base_v114_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 93.3003)).rolling(5).max()).pct_change(11)) * 0.521518)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc114_63d_base_v114_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc114_63d_base_v114_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc115_21d_base_v115_signal(revenue, ncfo):
    res = ((((revenue / (ncfo + 83.2502)).rolling(10).std()).rolling(15).min()) * 0.732492)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc115_21d_base_v115_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc115_21d_base_v115_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc116_21d_base_v116_signal(revenue, ncfo):
    res = (((((revenue * 86.3037 - ncfo).rolling(23).min()).rolling(10).std()).pct_change(5)) * 0.064807)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc116_21d_base_v116_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc116_21d_base_v116_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc117_21d_base_v117_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(20) / ncfo.pct_change(2)).pct_change(2)).diff(8)).rolling(19).var()).rolling(11).min()) * 0.370385)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc117_21d_base_v117_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc117_21d_base_v117_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc118_126d_base_v118_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(10).min()).rolling(4).var()) * 0.365598)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc118_126d_base_v118_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc118_126d_base_v118_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc119_252d_base_v119_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 75.6911)).pct_change(3)).pct_change(16)).rolling(25).min()) * 0.301474)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc119_252d_base_v119_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc119_252d_base_v119_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc120_42d_base_v120_signal(revenue, ncfo):
    res = ((((revenue * 92.6571 - ncfo).rolling(15).var()).rolling(25).max()) * 0.336068)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc120_42d_base_v120_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc120_42d_base_v120_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc121_252d_base_v121_signal(revenue, ncfo):
    res = ((((revenue.pct_change(6) / ncfo.pct_change(15)).rolling(14).mean()).rolling(22).std()) * 0.330233)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc121_252d_base_v121_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc121_252d_base_v121_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc122_21d_base_v122_signal(revenue, ncfo):
    res = ((((((revenue * 31.4408 - ncfo).rolling(27).min()).rolling(16).var()).rolling(29).min()).diff(5)) * 0.090587)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc122_21d_base_v122_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc122_21d_base_v122_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc123_21d_base_v123_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(14).std()).rolling(28).min()).rolling(9).max()) * 0.59116)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc123_21d_base_v123_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc123_21d_base_v123_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc124_5d_base_v124_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 94.8161)).diff(6)).rolling(14).mean()).rolling(15).max()) * 0.91465)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc124_5d_base_v124_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc124_5d_base_v124_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc125_63d_base_v125_signal(revenue, ncfo):
    res = ((((((revenue / (ncfo + 26.0898)).rolling(15).max()).pct_change(15)).pct_change(16)).rolling(9).mean()) * 0.09728)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc125_63d_base_v125_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc125_63d_base_v125_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc126_126d_base_v126_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 20.3942)).pct_change(7)).rolling(8).max()).pct_change(10)) * 0.937131)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc126_126d_base_v126_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc126_126d_base_v126_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc127_126d_base_v127_signal(revenue, ncfo):
    res = ((((revenue.diff(14) / (ncfo.shift(3) + 67.7511)).rolling(16).max()).rolling(13).std()) * 0.419964)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc127_126d_base_v127_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc127_126d_base_v127_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc128_63d_base_v128_signal(revenue, ncfo):
    res = (((((revenue.pct_change(5) / ncfo.pct_change(11)).diff(7)).diff(13)).diff(14)) * 0.459001)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc128_63d_base_v128_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc128_63d_base_v128_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc129_126d_base_v129_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 59.7599)).rolling(21).var()).diff(20)).diff(2)) * 0.081595)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc129_126d_base_v129_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc129_126d_base_v129_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc130_5d_base_v130_signal(revenue, ncfo):
    res = ((((revenue * 25.4403 - ncfo).rolling(7).max()).rolling(7).var()) * 0.617265)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc130_5d_base_v130_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc130_5d_base_v130_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_base_v131_signal(revenue, ncfo):
    res = ((((((revenue.pct_change(3) / ncfo.pct_change(11)).rolling(6).min()).rolling(5).var()).rolling(3).var()).rolling(17).std()) * 0.342393)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_base_v131_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc131_63d_base_v131_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc132_252d_base_v132_signal(revenue, ncfo):
    res = (((((revenue * 97.3398 - ncfo).rolling(12).max()).rolling(30).min()).rolling(12).std()) * 0.285381)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc132_252d_base_v132_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc132_252d_base_v132_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc133_126d_base_v133_signal(revenue, ncfo):
    res = ((((ncfo / (revenue + 99.4571)).rolling(9).mean()).rolling(3).std()) * 0.758402)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc133_126d_base_v133_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc133_126d_base_v133_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc134_42d_base_v134_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(18)).rolling(16).min()).rolling(5).min()) * 0.701844)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc134_42d_base_v134_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc134_42d_base_v134_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc135_252d_base_v135_signal(revenue, ncfo):
    res = ((((ncfo / (revenue + 72.0044)).diff(17)).pct_change(9)) * 0.155093)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc135_252d_base_v135_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc135_252d_base_v135_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc136_63d_base_v136_signal(revenue, ncfo):
    res = (((((ncfo / (revenue + 89.1004)).rolling(9).mean()).pct_change(16)).diff(4)) * 0.583964)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc136_63d_base_v136_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc136_63d_base_v136_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc137_21d_base_v137_signal(revenue, ncfo):
    res = (((((revenue / (ncfo + 2.6936)).rolling(2).std()).rolling(16).mean()).pct_change(16)) * 0.677686)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc137_21d_base_v137_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc137_21d_base_v137_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc138_42d_base_v138_signal(revenue, ncfo):
    res = (((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).diff(19)).rolling(8).std()).pct_change(2)) * 0.273932)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc138_42d_base_v138_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc138_42d_base_v138_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc139_252d_base_v139_signal(revenue, ncfo):
    res = ((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(10).min()).rolling(9).std()) * 0.326707)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc139_252d_base_v139_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc139_252d_base_v139_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc140_252d_base_v140_signal(revenue, ncfo):
    res = ((((((revenue.diff(7) / (ncfo.shift(3) + 86.565)).pct_change(5)).rolling(11).mean()).rolling(27).min()).rolling(25).min()) * 0.097405)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc140_252d_base_v140_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc140_252d_base_v140_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc141_252d_base_v141_signal(revenue, ncfo):
    res = ((((((revenue.diff(20) / (ncfo.shift(3) + 92.1778)).rolling(17).std()).rolling(30).min()).rolling(17).min()).rolling(20).var()) * 0.89566)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc141_252d_base_v141_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc141_252d_base_v141_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc142_63d_base_v142_signal(revenue, ncfo):
    res = (((((revenue.pct_change(6) / ncfo.pct_change(14)).rolling(3).mean()).rolling(12).max()).rolling(23).min()) * 0.751361)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc142_63d_base_v142_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc142_63d_base_v142_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc143_10d_base_v143_signal(revenue, ncfo):
    res = (((((revenue.diff(16) / (ncfo.shift(9) + 64.7963)).rolling(4).min()).pct_change(16)).rolling(6).var()) * 0.709363)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc143_10d_base_v143_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc143_10d_base_v143_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc144_10d_base_v144_signal(revenue, ncfo):
    res = ((((revenue * 68.463 - ncfo).rolling(4).max()).rolling(18).mean()) * 0.3044)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc144_10d_base_v144_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc144_10d_base_v144_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc145_5d_base_v145_signal(revenue, ncfo):
    res = ((((((revenue.diff(15) / (ncfo.shift(10) + 51.1141)).rolling(26).mean()).rolling(2).max()).rolling(25).mean()).diff(15)) * 0.414759)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc145_5d_base_v145_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc145_5d_base_v145_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc146_10d_base_v146_signal(revenue, ncfo):
    res = ((((((revenue.diff(2) / (ncfo.shift(2) + 78.6391)).diff(15)).pct_change(15)).rolling(27).max()).rolling(12).var()) * 0.836052)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc146_10d_base_v146_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc146_10d_base_v146_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc147_252d_base_v147_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(2).mean()).rolling(5).min()).rolling(7).mean()).diff(16)) * 0.216847)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc147_252d_base_v147_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc147_252d_base_v147_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc148_42d_base_v148_signal(revenue, ncfo):
    res = (((((revenue * 69.2114 - ncfo).diff(13)).pct_change(10)).rolling(6).mean()) * 0.861405)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc148_42d_base_v148_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc148_42d_base_v148_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc149_10d_base_v149_signal(revenue, ncfo):
    res = ((((((revenue.replace(0, np.nan) / ncfo.replace(0, np.nan)).rolling(22).std()).rolling(15).std()).pct_change(18)).rolling(4).std()) * 0.119674)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc149_10d_base_v149_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc149_10d_base_v149_signal

def f212r_f212_revenue_to_cash_conversion_momentum_calc150_21d_base_v150_signal(revenue, ncfo):
    res = ((((((ncfo / (revenue + 76.9951)).diff(15)).rolling(17).min()).rolling(29).mean()).rolling(20).min()) * 0.155202)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f212r_f212_revenue_to_cash_conversion_momentum_calc150_21d_base_v150_signal'] = f212r_f212_revenue_to_cash_conversion_momentum_calc150_21d_base_v150_signal


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
