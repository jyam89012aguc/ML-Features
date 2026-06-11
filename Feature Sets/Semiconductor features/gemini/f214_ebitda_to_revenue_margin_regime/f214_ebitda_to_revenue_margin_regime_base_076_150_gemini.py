import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f214e_f214_ebitda_to_revenue_margin_regime_calc076_5d_base_v076_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(2).mean()).rolling(22).max()) * 0.264707)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc076_5d_base_v076_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc076_5d_base_v076_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc077_126d_base_v077_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 57.2827)).rolling(14).var()).rolling(23).min()) * 0.800854)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc077_126d_base_v077_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc077_126d_base_v077_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc078_252d_base_v078_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(12).mean()).pct_change(14)).rolling(7).var()) * 0.894969)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc078_252d_base_v078_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc078_252d_base_v078_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc079_5d_base_v079_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(30).max()).rolling(20).mean()).rolling(27).min()) * 0.922765)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc079_5d_base_v079_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc079_5d_base_v079_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc080_21d_base_v080_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(29).std()).pct_change(12)) * 0.955463)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc080_21d_base_v080_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc080_21d_base_v080_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc081_21d_base_v081_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(14) / revenue.pct_change(11)).rolling(5).mean()).rolling(22).min()).rolling(21).var()) * 0.868368)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc081_21d_base_v081_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc081_21d_base_v081_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc082_63d_base_v082_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 34.7676)).rolling(11).std()).rolling(26).std()) * 0.916845)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc082_63d_base_v082_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc082_63d_base_v082_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc083_252d_base_v083_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 45.2474)).rolling(4).max()).rolling(2).min()).rolling(4).mean()) * 0.955047)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc083_252d_base_v083_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc083_252d_base_v083_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc084_10d_base_v084_signal(ebitda, revenue):
    res = ((((((ebitda * 28.165 - revenue).diff(13)).rolling(2).mean()).pct_change(18)).rolling(5).mean()) * 0.973824)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc084_10d_base_v084_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc084_10d_base_v084_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc085_42d_base_v085_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 58.9221)).rolling(20).std()).rolling(30).max()) * 0.972339)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc085_42d_base_v085_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc085_42d_base_v085_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc086_21d_base_v086_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(15) / revenue.pct_change(5)).pct_change(9)).pct_change(6)).diff(14)) * 0.779882)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc086_21d_base_v086_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc086_21d_base_v086_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc087_5d_base_v087_signal(ebitda, revenue):
    res = ((((ebitda.diff(6) / (revenue.shift(1) + 14.8127)).diff(16)).rolling(9).var()) * 0.11869)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc087_5d_base_v087_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc087_5d_base_v087_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc088_42d_base_v088_signal(ebitda, revenue):
    res = (((((ebitda * 34.6374 - revenue).pct_change(6)).rolling(10).var()).rolling(7).max()) * 0.586967)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc088_42d_base_v088_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc088_42d_base_v088_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc089_21d_base_v089_signal(ebitda, revenue):
    res = (((((ebitda.diff(8) / (revenue.shift(9) + 12.8789)).rolling(3).mean()).diff(14)).rolling(11).var()) * 0.668314)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc089_21d_base_v089_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc089_21d_base_v089_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc090_126d_base_v090_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 36.806)).rolling(6).std()).diff(15)) * 0.649163)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc090_126d_base_v090_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc090_126d_base_v090_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc091_21d_base_v091_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(7)).rolling(23).std()).rolling(22).var()) * 0.612481)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc091_21d_base_v091_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc091_21d_base_v091_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc092_126d_base_v092_signal(ebitda, revenue):
    res = (((((ebitda * 67.884 - revenue).diff(6)).pct_change(3)).rolling(13).min()) * 0.17303)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc092_126d_base_v092_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc092_126d_base_v092_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc093_126d_base_v093_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 1.3603)).rolling(24).var()).diff(7)).rolling(14).mean()) * 0.542044)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc093_126d_base_v093_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc093_126d_base_v093_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc094_63d_base_v094_signal(ebitda, revenue):
    res = ((((((ebitda.diff(11) / (revenue.shift(9) + 99.4336)).rolling(12).std()).pct_change(8)).rolling(2).var()).rolling(29).mean()) * 0.969284)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc094_63d_base_v094_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc094_63d_base_v094_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc095_252d_base_v095_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(11).max()).rolling(30).max()).rolling(28).mean()) * 0.631682)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc095_252d_base_v095_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc095_252d_base_v095_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc096_42d_base_v096_signal(ebitda, revenue):
    res = (((((ebitda.diff(9) / (revenue.shift(5) + 34.5995)).rolling(28).mean()).rolling(8).max()).pct_change(18)) * 0.178805)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc096_42d_base_v096_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc096_42d_base_v096_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc097_21d_base_v097_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 68.8746)).diff(11)).rolling(22).std()) * 0.475609)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc097_21d_base_v097_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc097_21d_base_v097_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc098_63d_base_v098_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(9) / revenue.pct_change(18)).pct_change(20)).rolling(20).max()).rolling(20).min()) * 0.535898)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc098_63d_base_v098_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc098_63d_base_v098_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc099_63d_base_v099_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(5)).pct_change(16)).rolling(10).mean()).pct_change(15)) * 0.161903)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc099_63d_base_v099_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc099_63d_base_v099_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc100_126d_base_v100_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(20) / revenue.pct_change(18)).diff(9)).rolling(10).std()).rolling(30).std()) * 0.379305)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc100_126d_base_v100_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc100_126d_base_v100_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc101_10d_base_v101_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 83.181)).rolling(27).max()).rolling(6).mean()) * 0.645724)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc101_10d_base_v101_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc101_10d_base_v101_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc102_5d_base_v102_signal(ebitda, revenue):
    res = ((((ebitda * 98.5345 - revenue).rolling(18).std()).pct_change(17)) * 0.65634)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc102_5d_base_v102_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc102_5d_base_v102_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc103_5d_base_v103_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 71.1979)).rolling(7).mean()).rolling(7).std()) * 0.555905)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc103_5d_base_v103_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc103_5d_base_v103_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc104_5d_base_v104_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 1.7261)).rolling(18).mean()).pct_change(20)) * 0.687832)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc104_5d_base_v104_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc104_5d_base_v104_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc105_126d_base_v105_signal(ebitda, revenue):
    res = ((((ebitda * 86.7968 - revenue).pct_change(10)).rolling(13).std()) * 0.911159)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc105_126d_base_v105_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc105_126d_base_v105_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc106_42d_base_v106_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(10) / revenue.pct_change(11)).diff(3)).rolling(18).max()) * 0.292989)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc106_42d_base_v106_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc106_42d_base_v106_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc107_252d_base_v107_signal(ebitda, revenue):
    res = (((((ebitda.diff(14) / (revenue.shift(9) + 4.8317)).rolling(29).min()).rolling(12).max()).pct_change(4)) * 0.482936)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc107_252d_base_v107_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc107_252d_base_v107_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc108_5d_base_v108_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 0.4646)).pct_change(9)).rolling(25).var()).rolling(14).max()) * 0.728669)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc108_5d_base_v108_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc108_5d_base_v108_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc109_42d_base_v109_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(4).mean()).rolling(30).mean()).diff(13)) * 0.334779)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc109_42d_base_v109_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc109_42d_base_v109_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc110_21d_base_v110_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).var()).rolling(21).min()).pct_change(19)).rolling(26).var()) * 0.094811)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc110_21d_base_v110_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc110_21d_base_v110_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc111_63d_base_v111_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(8).max()).rolling(19).var()).rolling(14).std()) * 0.522337)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc111_63d_base_v111_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc111_63d_base_v111_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc112_63d_base_v112_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(9).max()).rolling(15).max()) * 0.56331)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc112_63d_base_v112_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc112_63d_base_v112_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc113_63d_base_v113_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(16) / revenue.pct_change(17)).diff(16)).pct_change(20)).rolling(13).mean()).rolling(13).mean()) * 0.889752)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc113_63d_base_v113_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc113_63d_base_v113_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc114_252d_base_v114_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(20)).rolling(6).std()) * 0.186998)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc114_252d_base_v114_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc114_252d_base_v114_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc115_5d_base_v115_signal(ebitda, revenue):
    res = ((((ebitda * 94.3325 - revenue).rolling(2).min()).rolling(4).var()) * 0.140047)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc115_5d_base_v115_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc115_5d_base_v115_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc116_63d_base_v116_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(18).var()).rolling(5).var()).rolling(17).min()) * 0.755831)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc116_63d_base_v116_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc116_63d_base_v116_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc117_42d_base_v117_signal(ebitda, revenue):
    res = ((((ebitda * 29.1497 - revenue).pct_change(3)).rolling(19).mean()) * 0.098408)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc117_42d_base_v117_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc117_42d_base_v117_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc118_126d_base_v118_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(3) / revenue.pct_change(20)).rolling(6).min()).rolling(10).min()).rolling(7).std()).rolling(21).std()) * 0.642081)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc118_126d_base_v118_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc118_126d_base_v118_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc119_42d_base_v119_signal(ebitda, revenue):
    res = ((((ebitda.diff(15) / (revenue.shift(1) + 33.4933)).rolling(28).mean()).rolling(13).max()) * 0.585882)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc119_42d_base_v119_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc119_42d_base_v119_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc120_126d_base_v120_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 29.4355)).pct_change(19)).rolling(6).std()) * 0.486384)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc120_126d_base_v120_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc120_126d_base_v120_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc121_252d_base_v121_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 86.9774)).rolling(9).min()).diff(11)).rolling(10).min()).rolling(16).mean()) * 0.497006)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc121_252d_base_v121_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc121_252d_base_v121_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc122_10d_base_v122_signal(ebitda, revenue):
    res = ((((((ebitda * 21.2061 - revenue).rolling(30).var()).diff(9)).rolling(3).mean()).rolling(17).mean()) * 0.143292)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc122_10d_base_v122_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc122_10d_base_v122_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc123_63d_base_v123_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(6) / revenue.pct_change(9)).rolling(4).std()).rolling(15).std()).rolling(14).mean()) * 0.904166)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc123_63d_base_v123_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc123_63d_base_v123_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc124_63d_base_v124_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 92.4272)).rolling(22).max()).diff(2)).rolling(5).mean()) * 0.788944)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc124_63d_base_v124_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc124_63d_base_v124_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc125_63d_base_v125_signal(ebitda, revenue):
    res = ((((ebitda.diff(6) / (revenue.shift(8) + 37.243)).rolling(4).min()).diff(2)) * 0.011005)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc125_63d_base_v125_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc125_63d_base_v125_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc126_126d_base_v126_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 36.3365)).rolling(16).mean()).rolling(27).mean()) * 0.938064)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc126_126d_base_v126_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc126_126d_base_v126_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc127_42d_base_v127_signal(ebitda, revenue):
    res = ((((((ebitda * 59.4055 - revenue).pct_change(10)).rolling(24).max()).rolling(24).var()).rolling(9).var()) * 0.676876)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc127_42d_base_v127_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc127_42d_base_v127_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc128_252d_base_v128_signal(ebitda, revenue):
    res = ((((((ebitda * 64.6214 - revenue).rolling(29).std()).pct_change(14)).rolling(6).var()).rolling(10).max()) * 0.7915)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc128_252d_base_v128_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc128_252d_base_v128_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc129_21d_base_v129_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 95.6593)).rolling(27).std()).rolling(27).var()).rolling(4).max()) * 0.760671)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc129_21d_base_v129_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc129_21d_base_v129_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc130_10d_base_v130_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 90.1795)).rolling(26).var()).rolling(23).max()) * 0.720846)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc130_10d_base_v130_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc130_10d_base_v130_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc131_63d_base_v131_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(10) / revenue.pct_change(7)).rolling(10).min()).rolling(26).max()).pct_change(8)) * 0.68091)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc131_63d_base_v131_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc131_63d_base_v131_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc132_21d_base_v132_signal(ebitda, revenue):
    res = (((((ebitda * 87.1486 - revenue).rolling(25).mean()).rolling(16).min()).rolling(20).std()) * 0.158356)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc132_21d_base_v132_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc132_21d_base_v132_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc133_63d_base_v133_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 21.981)).rolling(7).var()).rolling(27).var()).rolling(14).std()).pct_change(10)) * 0.713393)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc133_63d_base_v133_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc133_63d_base_v133_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc134_42d_base_v134_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(2)).rolling(13).min()).rolling(21).min()) * 0.539388)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc134_42d_base_v134_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc134_42d_base_v134_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc135_21d_base_v135_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 35.3087)).pct_change(1)).rolling(3).max()).rolling(12).max()).pct_change(11)) * 0.366938)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc135_21d_base_v135_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc135_21d_base_v135_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc136_5d_base_v136_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 4.3463)).rolling(5).mean()).rolling(26).min()) * 0.626365)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc136_5d_base_v136_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc136_5d_base_v136_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc137_63d_base_v137_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(11) / revenue.pct_change(10)).diff(13)).rolling(23).mean()).diff(6)) * 0.10286)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc137_63d_base_v137_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc137_63d_base_v137_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc138_10d_base_v138_signal(ebitda, revenue):
    res = ((((((ebitda.diff(20) / (revenue.shift(6) + 63.4212)).rolling(23).mean()).rolling(2).std()).rolling(23).mean()).rolling(7).std()) * 0.408)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc138_10d_base_v138_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc138_10d_base_v138_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc139_42d_base_v139_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 90.1216)).pct_change(2)).rolling(12).mean()).rolling(12).mean()) * 0.779235)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc139_42d_base_v139_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc139_42d_base_v139_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc140_10d_base_v140_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(9) / revenue.pct_change(15)).rolling(3).var()).rolling(11).min()).rolling(28).mean()).rolling(5).min()) * 0.921891)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc140_10d_base_v140_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc140_10d_base_v140_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc141_252d_base_v141_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 44.3499)).diff(19)).diff(12)).diff(1)) * 0.197438)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc141_252d_base_v141_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc141_252d_base_v141_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc142_10d_base_v142_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(13) / revenue.pct_change(10)).rolling(11).std()).pct_change(1)).rolling(24).std()).rolling(5).max()) * 0.822649)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc142_10d_base_v142_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc142_10d_base_v142_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc143_5d_base_v143_signal(ebitda, revenue):
    res = ((((((ebitda * 27.8157 - revenue).diff(10)).rolling(4).mean()).rolling(11).max()).diff(20)) * 0.133535)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc143_5d_base_v143_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc143_5d_base_v143_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc144_5d_base_v144_signal(ebitda, revenue):
    res = (((((ebitda * 95.5456 - revenue).rolling(26).var()).pct_change(8)).rolling(23).var()) * 0.980676)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc144_5d_base_v144_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc144_5d_base_v144_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc145_63d_base_v145_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(20).max()).rolling(22).mean()).rolling(14).mean()) * 0.054791)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc145_63d_base_v145_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc145_63d_base_v145_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc146_63d_base_v146_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).min()).rolling(3).var()).pct_change(8)).rolling(18).min()) * 0.905727)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc146_63d_base_v146_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc146_63d_base_v146_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc147_21d_base_v147_signal(ebitda, revenue):
    res = ((((((ebitda.diff(7) / (revenue.shift(4) + 69.4694)).diff(12)).pct_change(8)).rolling(2).mean()).rolling(17).min()) * 0.1328)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc147_21d_base_v147_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc147_21d_base_v147_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc148_42d_base_v148_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 37.76)).diff(12)).pct_change(1)) * 0.841105)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc148_42d_base_v148_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc148_42d_base_v148_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc149_5d_base_v149_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 49.3737)).rolling(16).mean()).rolling(10).max()).rolling(20).std()) * 0.975661)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc149_5d_base_v149_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc149_5d_base_v149_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc150_5d_base_v150_signal(ebitda, revenue):
    res = (((((ebitda.diff(19) / (revenue.shift(3) + 62.8109)).pct_change(4)).rolling(2).mean()).diff(2)) * 0.658262)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc150_5d_base_v150_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc150_5d_base_v150_signal


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
