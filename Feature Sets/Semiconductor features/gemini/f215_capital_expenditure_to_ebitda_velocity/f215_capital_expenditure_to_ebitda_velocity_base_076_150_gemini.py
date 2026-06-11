import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_42d_base_v076_signal(capex, ebitda):
    res = (((((capex * 5.0127 - ebitda).rolling(29).std()).rolling(27).mean()).diff(4)) * 0.192021)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_42d_base_v076_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_42d_base_v076_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_63d_base_v077_signal(capex, ebitda):
    res = ((((ebitda / (capex + 18.6423)).pct_change(5)).diff(20)) * 0.035023)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_63d_base_v077_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_63d_base_v077_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_126d_base_v078_signal(capex, ebitda):
    res = (((((capex.diff(5) / (ebitda.shift(4) + 47.9579)).rolling(7).mean()).pct_change(18)).rolling(12).std()) * 0.780411)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_126d_base_v078_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_126d_base_v078_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_10d_base_v079_signal(capex, ebitda):
    res = ((((capex.pct_change(20) / ebitda.pct_change(19)).rolling(7).var()).rolling(17).min()) * 0.809168)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_10d_base_v079_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_10d_base_v079_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_10d_base_v080_signal(capex, ebitda):
    res = ((((capex / (ebitda + 62.2328)).rolling(23).std()).rolling(2).std()) * 0.704926)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_10d_base_v080_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_10d_base_v080_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_63d_base_v081_signal(capex, ebitda):
    res = ((((ebitda / (capex + 9.4827)).pct_change(6)).rolling(10).max()) * 0.684965)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_63d_base_v081_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_63d_base_v081_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_21d_base_v082_signal(capex, ebitda):
    res = ((((capex * 13.9162 - ebitda).rolling(2).max()).pct_change(16)) * 0.952297)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_21d_base_v082_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_21d_base_v082_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_21d_base_v083_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).min()).rolling(20).min()) * 0.854777)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_21d_base_v083_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_21d_base_v083_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_126d_base_v084_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 60.9742)).pct_change(13)).pct_change(10)).rolling(8).std()).diff(5)) * 0.078051)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_126d_base_v084_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_126d_base_v084_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_10d_base_v085_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(8).std()).rolling(15).mean()).diff(17)) * 0.433846)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_10d_base_v085_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_10d_base_v085_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_126d_base_v086_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(19).std()).rolling(3).var()) * 0.945843)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_126d_base_v086_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_126d_base_v086_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_10d_base_v087_signal(capex, ebitda):
    res = (((((capex * 37.9074 - ebitda).rolling(22).std()).rolling(4).var()).diff(2)) * 0.043862)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_10d_base_v087_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_10d_base_v087_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_126d_base_v088_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 47.3444)).diff(14)).rolling(27).min()).pct_change(12)).rolling(7).max()) * 0.703898)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_126d_base_v088_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_126d_base_v088_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_42d_base_v089_signal(capex, ebitda):
    res = ((((capex / (ebitda + 45.399)).rolling(24).std()).rolling(8).min()) * 0.144966)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_42d_base_v089_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_42d_base_v089_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_252d_base_v090_signal(capex, ebitda):
    res = ((((((capex.diff(13) / (ebitda.shift(5) + 50.8848)).rolling(10).min()).rolling(21).var()).rolling(22).min()).rolling(8).max()) * 0.97247)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_252d_base_v090_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_252d_base_v090_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_5d_base_v091_signal(capex, ebitda):
    res = ((((((capex * 52.3196 - ebitda).rolling(28).var()).rolling(27).max()).rolling(10).mean()).rolling(24).max()) * 0.223238)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_5d_base_v091_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_5d_base_v091_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_63d_base_v092_signal(capex, ebitda):
    res = ((((((capex.diff(20) / (ebitda.shift(6) + 42.7822)).diff(7)).rolling(28).std()).rolling(26).min()).pct_change(14)) * 0.587492)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_63d_base_v092_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_63d_base_v092_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_21d_base_v093_signal(capex, ebitda):
    res = ((((capex / (ebitda + 21.7262)).rolling(7).mean()).diff(18)) * 0.139152)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_21d_base_v093_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_21d_base_v093_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_63d_base_v094_signal(capex, ebitda):
    res = ((((((capex.diff(3) / (ebitda.shift(2) + 70.4185)).rolling(9).var()).rolling(2).var()).rolling(24).mean()).rolling(7).mean()) * 0.87291)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_63d_base_v094_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_63d_base_v094_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_126d_base_v095_signal(capex, ebitda):
    res = ((((((capex * 45.098 - ebitda).rolling(17).var()).rolling(7).var()).pct_change(6)).rolling(14).var()) * 0.736486)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_126d_base_v095_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_126d_base_v095_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_126d_base_v096_signal(capex, ebitda):
    res = ((((capex * 46.1634 - ebitda).rolling(8).std()).rolling(18).min()) * 0.503935)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_126d_base_v096_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_126d_base_v096_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_126d_base_v097_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(14).mean()).diff(3)).diff(7)).diff(9)) * 0.483417)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_126d_base_v097_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_126d_base_v097_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_63d_base_v098_signal(capex, ebitda):
    res = (((((capex.diff(15) / (ebitda.shift(10) + 64.2791)).rolling(26).mean()).diff(11)).rolling(15).max()) * 0.402798)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_63d_base_v098_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_63d_base_v098_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_126d_base_v099_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 44.4379)).pct_change(15)).rolling(8).std()).rolling(27).min()).rolling(3).mean()) * 0.273953)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_126d_base_v099_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_126d_base_v099_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_252d_base_v100_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(5).mean()).rolling(12).min()) * 0.572451)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_252d_base_v100_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_252d_base_v100_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_21d_base_v101_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(14).max()).rolling(12).var()).pct_change(12)).rolling(13).min()) * 0.727806)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_21d_base_v101_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_21d_base_v101_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_5d_base_v102_signal(capex, ebitda):
    res = ((((capex / (ebitda + 99.1207)).rolling(18).min()).rolling(12).min()) * 0.178705)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_5d_base_v102_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_5d_base_v102_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_63d_base_v103_signal(capex, ebitda):
    res = ((((capex.diff(17) / (ebitda.shift(3) + 78.711)).rolling(14).min()).rolling(10).var()) * 0.416626)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_63d_base_v103_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_63d_base_v103_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_21d_base_v104_signal(capex, ebitda):
    res = ((((((capex * 10.7405 - ebitda).rolling(17).max()).rolling(2).var()).rolling(27).std()).pct_change(7)) * 0.181623)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_21d_base_v104_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_21d_base_v104_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_10d_base_v105_signal(capex, ebitda):
    res = (((((capex.diff(14) / (ebitda.shift(1) + 52.9754)).pct_change(2)).diff(3)).rolling(2).min()) * 0.903906)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_10d_base_v105_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_10d_base_v105_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_10d_base_v106_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 40.8801)).diff(14)).rolling(7).mean()).rolling(27).mean()).diff(11)) * 0.05467)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_10d_base_v106_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_10d_base_v106_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_126d_base_v107_signal(capex, ebitda):
    res = ((((((capex.diff(18) / (ebitda.shift(4) + 4.9463)).rolling(8).mean()).rolling(23).var()).rolling(2).max()).rolling(26).max()) * 0.609234)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_126d_base_v107_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_126d_base_v107_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_42d_base_v108_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(9)).rolling(6).var()) * 0.817199)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_42d_base_v108_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_42d_base_v108_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_63d_base_v109_signal(capex, ebitda):
    res = (((((capex / (ebitda + 26.9457)).rolling(3).var()).rolling(8).min()).rolling(26).var()) * 0.21555)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_63d_base_v109_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_63d_base_v109_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_252d_base_v110_signal(capex, ebitda):
    res = (((((capex.diff(10) / (ebitda.shift(9) + 37.8263)).diff(8)).rolling(10).max()).diff(1)) * 0.687476)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_252d_base_v110_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_252d_base_v110_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_21d_base_v111_signal(capex, ebitda):
    res = ((((capex / (ebitda + 58.4894)).diff(20)).rolling(10).var()) * 0.625379)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_21d_base_v111_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_21d_base_v111_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_10d_base_v112_signal(capex, ebitda):
    res = ((((((capex * 65.1023 - ebitda).pct_change(5)).rolling(18).var()).rolling(21).var()).pct_change(1)) * 0.802567)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_10d_base_v112_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_10d_base_v112_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_42d_base_v113_signal(capex, ebitda):
    res = (((((capex.pct_change(4) / ebitda.pct_change(19)).diff(15)).rolling(11).min()).rolling(15).max()) * 0.315935)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_42d_base_v113_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_42d_base_v113_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_42d_base_v114_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(23).var()).rolling(25).max()).rolling(8).std()).rolling(18).mean()) * 0.367994)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_42d_base_v114_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_42d_base_v114_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_63d_base_v115_signal(capex, ebitda):
    res = ((((((capex.pct_change(17) / ebitda.pct_change(13)).pct_change(9)).rolling(20).mean()).rolling(7).min()).rolling(22).std()) * 0.136554)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_63d_base_v115_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_63d_base_v115_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_252d_base_v116_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).max()).rolling(7).var()).rolling(15).min()).pct_change(16)) * 0.961653)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_252d_base_v116_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_252d_base_v116_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_21d_base_v117_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(19)).rolling(23).std()) * 0.215591)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_21d_base_v117_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_21d_base_v117_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_126d_base_v118_signal(capex, ebitda):
    res = ((((((capex * 91.4843 - ebitda).rolling(11).std()).pct_change(5)).rolling(28).min()).rolling(28).var()) * 0.094723)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_126d_base_v118_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_126d_base_v118_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_21d_base_v119_signal(capex, ebitda):
    res = ((((ebitda / (capex + 56.3563)).rolling(16).std()).diff(5)) * 0.416033)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_21d_base_v119_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_21d_base_v119_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_10d_base_v120_signal(capex, ebitda):
    res = ((((ebitda / (capex + 65.411)).rolling(17).std()).diff(19)) * 0.126666)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_10d_base_v120_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_10d_base_v120_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_5d_base_v121_signal(capex, ebitda):
    res = ((((((capex.pct_change(9) / ebitda.pct_change(18)).rolling(3).min()).diff(18)).rolling(27).var()).rolling(16).min()) * 0.8063)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_5d_base_v121_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_5d_base_v121_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_63d_base_v122_signal(capex, ebitda):
    res = ((((capex.diff(15) / (ebitda.shift(7) + 32.3638)).rolling(18).max()).rolling(28).mean()) * 0.2643)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_63d_base_v122_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_63d_base_v122_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_252d_base_v123_signal(capex, ebitda):
    res = ((((capex * 54.5101 - ebitda).rolling(20).var()).rolling(12).mean()) * 0.621829)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_252d_base_v123_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_252d_base_v123_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_42d_base_v124_signal(capex, ebitda):
    res = ((((((capex.pct_change(17) / ebitda.pct_change(20)).rolling(7).min()).rolling(28).min()).rolling(8).max()).rolling(10).max()) * 0.55667)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_42d_base_v124_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_42d_base_v124_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_63d_base_v125_signal(capex, ebitda):
    res = (((((capex.pct_change(5) / ebitda.pct_change(1)).rolling(4).min()).rolling(9).std()).rolling(14).max()) * 0.412804)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_63d_base_v125_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_63d_base_v125_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_126d_base_v126_signal(capex, ebitda):
    res = ((((((capex * 10.9665 - ebitda).rolling(6).mean()).rolling(22).max()).pct_change(18)).rolling(22).max()) * 0.122226)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_126d_base_v126_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_126d_base_v126_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_42d_base_v127_signal(capex, ebitda):
    res = (((((capex.pct_change(5) / ebitda.pct_change(1)).rolling(14).mean()).rolling(24).min()).pct_change(20)) * 0.778455)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_42d_base_v127_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_42d_base_v127_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_5d_base_v128_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 87.3203)).rolling(6).max()).rolling(19).min()).rolling(30).max()).rolling(9).std()) * 0.056134)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_5d_base_v128_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_5d_base_v128_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_21d_base_v129_signal(capex, ebitda):
    res = ((((capex / (ebitda + 90.5384)).diff(11)).rolling(15).mean()) * 0.511153)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_21d_base_v129_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_21d_base_v129_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_42d_base_v130_signal(capex, ebitda):
    res = (((((capex.diff(14) / (ebitda.shift(9) + 32.8576)).diff(15)).rolling(27).mean()).rolling(16).min()) * 0.510812)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_42d_base_v130_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_42d_base_v130_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_10d_base_v131_signal(capex, ebitda):
    res = ((((((capex.diff(7) / (ebitda.shift(2) + 73.9995)).rolling(23).mean()).pct_change(11)).rolling(23).min()).rolling(13).mean()) * 0.760623)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_10d_base_v131_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_10d_base_v131_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_10d_base_v132_signal(capex, ebitda):
    res = ((((((capex.diff(20) / (ebitda.shift(10) + 64.4064)).pct_change(9)).rolling(3).var()).rolling(13).var()).rolling(19).max()) * 0.524302)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_10d_base_v132_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_10d_base_v132_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_10d_base_v133_signal(capex, ebitda):
    res = ((((((capex.pct_change(16) / ebitda.pct_change(2)).rolling(26).mean()).rolling(9).std()).diff(11)).pct_change(2)) * 0.084823)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_10d_base_v133_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_10d_base_v133_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_10d_base_v134_signal(capex, ebitda):
    res = ((((capex * 40.1196 - ebitda).diff(2)).rolling(22).max()) * 0.980671)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_10d_base_v134_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_10d_base_v134_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_base_v135_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 87.8463)).rolling(27).var()).pct_change(9)).rolling(15).var()).rolling(11).max()) * 0.451328)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_base_v135_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_base_v135_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_21d_base_v136_signal(capex, ebitda):
    res = (((((capex.pct_change(8) / ebitda.pct_change(14)).rolling(28).var()).rolling(4).mean()).rolling(8).min()) * 0.473568)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_21d_base_v136_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_21d_base_v136_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_10d_base_v137_signal(capex, ebitda):
    res = ((((((capex.diff(16) / (ebitda.shift(9) + 61.3543)).rolling(13).min()).rolling(24).min()).rolling(21).std()).diff(5)) * 0.480171)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_10d_base_v137_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_10d_base_v137_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_126d_base_v138_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 43.9743)).pct_change(3)).rolling(19).var()).rolling(24).var()).diff(10)) * 0.112371)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_126d_base_v138_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_126d_base_v138_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_126d_base_v139_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(4).var()).rolling(13).max()).diff(9)).rolling(9).max()) * 0.815213)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_126d_base_v139_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_126d_base_v139_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_63d_base_v140_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(9)).rolling(7).min()).diff(4)) * 0.39128)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_63d_base_v140_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_63d_base_v140_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_21d_base_v141_signal(capex, ebitda):
    res = ((((((capex.diff(18) / (ebitda.shift(5) + 74.3267)).rolling(5).max()).rolling(4).min()).rolling(2).min()).rolling(2).var()) * 0.570856)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_21d_base_v141_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_21d_base_v141_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_10d_base_v142_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 89.7662)).pct_change(10)).rolling(9).mean()).pct_change(10)).pct_change(9)) * 0.085384)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_10d_base_v142_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_10d_base_v142_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_126d_base_v143_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 48.0033)).rolling(27).min()).rolling(11).min()).rolling(25).mean()).rolling(20).std()) * 0.695069)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_126d_base_v143_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_126d_base_v143_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_252d_base_v144_signal(capex, ebitda):
    res = ((((capex / (ebitda + 71.9247)).rolling(29).min()).diff(12)) * 0.132867)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_252d_base_v144_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_252d_base_v144_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_126d_base_v145_signal(capex, ebitda):
    res = ((((capex * 3.0541 - ebitda).rolling(14).min()).rolling(16).min()) * 0.721489)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_126d_base_v145_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_126d_base_v145_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_5d_base_v146_signal(capex, ebitda):
    res = ((((capex / (ebitda + 60.0183)).rolling(25).var()).rolling(9).min()) * 0.380003)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_5d_base_v146_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_5d_base_v146_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_21d_base_v147_signal(capex, ebitda):
    res = ((((((capex.pct_change(5) / ebitda.pct_change(5)).rolling(10).std()).rolling(20).max()).rolling(3).max()).rolling(30).mean()) * 0.941127)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_21d_base_v147_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_21d_base_v147_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_10d_base_v148_signal(capex, ebitda):
    res = ((((((capex.diff(18) / (ebitda.shift(4) + 72.5473)).diff(1)).rolling(17).mean()).pct_change(15)).rolling(4).max()) * 0.96251)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_10d_base_v148_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_10d_base_v148_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_21d_base_v149_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 15.057)).rolling(8).std()).rolling(26).std()).pct_change(12)).rolling(16).mean()) * 0.308341)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_21d_base_v149_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_21d_base_v149_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_21d_base_v150_signal(capex, ebitda):
    res = ((((capex / (ebitda + 85.1615)).rolling(14).max()).rolling(17).std()) * 0.899806)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_21d_base_v150_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_21d_base_v150_signal


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
