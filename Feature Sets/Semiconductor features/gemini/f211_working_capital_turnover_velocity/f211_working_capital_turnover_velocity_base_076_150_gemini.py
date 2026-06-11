import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f211w_f211_working_capital_turnover_velocity_calc076_63d_base_v076_signal(workingcapital, revenue):
    res = (((((workingcapital * 50.8733 - revenue).pct_change(1)).rolling(25).var()).rolling(28).var()) * 0.87174)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc076_63d_base_v076_signal'] = f211w_f211_working_capital_turnover_velocity_calc076_63d_base_v076_signal

def f211w_f211_working_capital_turnover_velocity_calc077_63d_base_v077_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(5) / (revenue.shift(8) + 58.0343)).rolling(26).max()).rolling(14).max()).rolling(12).min()) * 0.656742)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc077_63d_base_v077_signal'] = f211w_f211_working_capital_turnover_velocity_calc077_63d_base_v077_signal

def f211w_f211_working_capital_turnover_velocity_calc078_252d_base_v078_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 18.9464)).diff(16)).diff(13)).rolling(23).min()) * 0.693548)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc078_252d_base_v078_signal'] = f211w_f211_working_capital_turnover_velocity_calc078_252d_base_v078_signal

def f211w_f211_working_capital_turnover_velocity_calc079_252d_base_v079_signal(workingcapital, revenue):
    res = (((((workingcapital * 82.0927 - revenue).pct_change(4)).pct_change(15)).rolling(18).mean()) * 0.971202)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc079_252d_base_v079_signal'] = f211w_f211_working_capital_turnover_velocity_calc079_252d_base_v079_signal

def f211w_f211_working_capital_turnover_velocity_calc080_42d_base_v080_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(5) / (revenue.shift(2) + 1.6332)).diff(13)).diff(3)).pct_change(11)).pct_change(18)) * 0.151272)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc080_42d_base_v080_signal'] = f211w_f211_working_capital_turnover_velocity_calc080_42d_base_v080_signal

def f211w_f211_working_capital_turnover_velocity_calc081_42d_base_v081_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 95.4185)).diff(10)).rolling(25).std()) * 0.624263)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc081_42d_base_v081_signal'] = f211w_f211_working_capital_turnover_velocity_calc081_42d_base_v081_signal

def f211w_f211_working_capital_turnover_velocity_calc082_5d_base_v082_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 43.4538)).rolling(27).var()).rolling(11).mean()) * 0.106474)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc082_5d_base_v082_signal'] = f211w_f211_working_capital_turnover_velocity_calc082_5d_base_v082_signal

def f211w_f211_working_capital_turnover_velocity_calc083_21d_base_v083_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 37.5466)).rolling(21).mean()).pct_change(13)) * 0.152658)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc083_21d_base_v083_signal'] = f211w_f211_working_capital_turnover_velocity_calc083_21d_base_v083_signal

def f211w_f211_working_capital_turnover_velocity_calc084_63d_base_v084_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(15)).rolling(10).min()).diff(1)).pct_change(15)) * 0.497714)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc084_63d_base_v084_signal'] = f211w_f211_working_capital_turnover_velocity_calc084_63d_base_v084_signal

def f211w_f211_working_capital_turnover_velocity_calc085_21d_base_v085_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(19) / revenue.pct_change(10)).diff(9)).rolling(29).min()).rolling(8).var()) * 0.164816)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc085_21d_base_v085_signal'] = f211w_f211_working_capital_turnover_velocity_calc085_21d_base_v085_signal

def f211w_f211_working_capital_turnover_velocity_calc086_42d_base_v086_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(13) / (revenue.shift(10) + 85.3482)).rolling(2).var()).pct_change(13)).rolling(2).var()).rolling(29).max()) * 0.11452)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc086_42d_base_v086_signal'] = f211w_f211_working_capital_turnover_velocity_calc086_42d_base_v086_signal

def f211w_f211_working_capital_turnover_velocity_calc087_126d_base_v087_signal(workingcapital, revenue):
    res = (((((workingcapital * 77.8533 - revenue).rolling(22).std()).rolling(21).std()).rolling(23).var()) * 0.964131)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc087_126d_base_v087_signal'] = f211w_f211_working_capital_turnover_velocity_calc087_126d_base_v087_signal

def f211w_f211_working_capital_turnover_velocity_calc088_252d_base_v088_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).max()).diff(5)) * 0.655998)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc088_252d_base_v088_signal'] = f211w_f211_working_capital_turnover_velocity_calc088_252d_base_v088_signal

def f211w_f211_working_capital_turnover_velocity_calc089_5d_base_v089_signal(workingcapital, revenue):
    res = (((((workingcapital * 90.9718 - revenue).rolling(18).max()).rolling(28).var()).rolling(10).std()) * 0.330185)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc089_5d_base_v089_signal'] = f211w_f211_working_capital_turnover_velocity_calc089_5d_base_v089_signal

def f211w_f211_working_capital_turnover_velocity_calc090_252d_base_v090_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 94.4244)).pct_change(8)).pct_change(13)) * 0.958036)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc090_252d_base_v090_signal'] = f211w_f211_working_capital_turnover_velocity_calc090_252d_base_v090_signal

def f211w_f211_working_capital_turnover_velocity_calc091_252d_base_v091_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 80.4783)).rolling(23).var()).diff(9)).rolling(14).max()) * 0.36846)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc091_252d_base_v091_signal'] = f211w_f211_working_capital_turnover_velocity_calc091_252d_base_v091_signal

def f211w_f211_working_capital_turnover_velocity_calc092_252d_base_v092_signal(workingcapital, revenue):
    res = (((((workingcapital * 63.8911 - revenue).rolling(9).max()).diff(3)).diff(15)) * 0.374044)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc092_252d_base_v092_signal'] = f211w_f211_working_capital_turnover_velocity_calc092_252d_base_v092_signal

def f211w_f211_working_capital_turnover_velocity_calc093_126d_base_v093_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(9).mean()).rolling(6).max()) * 0.41013)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc093_126d_base_v093_signal'] = f211w_f211_working_capital_turnover_velocity_calc093_126d_base_v093_signal

def f211w_f211_working_capital_turnover_velocity_calc094_42d_base_v094_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(28).mean()).rolling(21).min()).rolling(10).min()).rolling(24).mean()) * 0.667076)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc094_42d_base_v094_signal'] = f211w_f211_working_capital_turnover_velocity_calc094_42d_base_v094_signal

def f211w_f211_working_capital_turnover_velocity_calc095_21d_base_v095_signal(workingcapital, revenue):
    res = ((((((workingcapital * 21.8052 - revenue).rolling(3).var()).rolling(10).min()).rolling(5).std()).pct_change(15)) * 0.445802)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc095_21d_base_v095_signal'] = f211w_f211_working_capital_turnover_velocity_calc095_21d_base_v095_signal

def f211w_f211_working_capital_turnover_velocity_calc096_5d_base_v096_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 66.3106)).pct_change(19)).rolling(4).std()) * 0.63887)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc096_5d_base_v096_signal'] = f211w_f211_working_capital_turnover_velocity_calc096_5d_base_v096_signal

def f211w_f211_working_capital_turnover_velocity_calc097_252d_base_v097_signal(workingcapital, revenue):
    res = ((((workingcapital * 76.5392 - revenue).rolling(29).var()).rolling(6).std()) * 0.213014)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc097_252d_base_v097_signal'] = f211w_f211_working_capital_turnover_velocity_calc097_252d_base_v097_signal

def f211w_f211_working_capital_turnover_velocity_calc098_63d_base_v098_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 25.1404)).rolling(2).var()).rolling(10).std()).rolling(6).mean()).diff(14)) * 0.181007)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc098_63d_base_v098_signal'] = f211w_f211_working_capital_turnover_velocity_calc098_63d_base_v098_signal

def f211w_f211_working_capital_turnover_velocity_calc099_63d_base_v099_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 11.4536)).rolling(9).max()).rolling(3).max()).diff(17)) * 0.072287)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc099_63d_base_v099_signal'] = f211w_f211_working_capital_turnover_velocity_calc099_63d_base_v099_signal

def f211w_f211_working_capital_turnover_velocity_calc100_21d_base_v100_signal(workingcapital, revenue):
    res = ((((workingcapital.pct_change(13) / revenue.pct_change(14)).rolling(24).min()).rolling(4).min()) * 0.954746)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc100_21d_base_v100_signal'] = f211w_f211_working_capital_turnover_velocity_calc100_21d_base_v100_signal

def f211w_f211_working_capital_turnover_velocity_calc101_5d_base_v101_signal(workingcapital, revenue):
    res = ((((((workingcapital * 32.279 - revenue).rolling(14).var()).rolling(18).max()).rolling(16).var()).rolling(21).max()) * 0.155367)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc101_5d_base_v101_signal'] = f211w_f211_working_capital_turnover_velocity_calc101_5d_base_v101_signal

def f211w_f211_working_capital_turnover_velocity_calc102_42d_base_v102_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 10.0079)).rolling(28).var()).rolling(14).min()).rolling(25).min()) * 0.697744)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc102_42d_base_v102_signal'] = f211w_f211_working_capital_turnover_velocity_calc102_42d_base_v102_signal

def f211w_f211_working_capital_turnover_velocity_calc103_5d_base_v103_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 31.3236)).pct_change(3)).rolling(15).mean()) * 0.316273)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc103_5d_base_v103_signal'] = f211w_f211_working_capital_turnover_velocity_calc103_5d_base_v103_signal

def f211w_f211_working_capital_turnover_velocity_calc104_5d_base_v104_signal(workingcapital, revenue):
    res = ((((((workingcapital * 74.4844 - revenue).rolling(23).var()).rolling(15).mean()).rolling(29).var()).diff(14)) * 0.375194)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc104_5d_base_v104_signal'] = f211w_f211_working_capital_turnover_velocity_calc104_5d_base_v104_signal

def f211w_f211_working_capital_turnover_velocity_calc105_252d_base_v105_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 91.5928)).rolling(8).max()).rolling(23).std()).rolling(9).min()).pct_change(4)) * 0.060417)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc105_252d_base_v105_signal'] = f211w_f211_working_capital_turnover_velocity_calc105_252d_base_v105_signal

def f211w_f211_working_capital_turnover_velocity_calc106_21d_base_v106_signal(workingcapital, revenue):
    res = ((((((workingcapital * 84.5528 - revenue).rolling(23).max()).diff(18)).rolling(21).mean()).diff(9)) * 0.37021)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc106_21d_base_v106_signal'] = f211w_f211_working_capital_turnover_velocity_calc106_21d_base_v106_signal

def f211w_f211_working_capital_turnover_velocity_calc107_5d_base_v107_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 18.1236)).rolling(23).max()).rolling(4).min()) * 0.698645)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc107_5d_base_v107_signal'] = f211w_f211_working_capital_turnover_velocity_calc107_5d_base_v107_signal

def f211w_f211_working_capital_turnover_velocity_calc108_10d_base_v108_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(7).var()).rolling(11).var()).diff(11)) * 0.962374)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc108_10d_base_v108_signal'] = f211w_f211_working_capital_turnover_velocity_calc108_10d_base_v108_signal

def f211w_f211_working_capital_turnover_velocity_calc109_252d_base_v109_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 94.1466)).rolling(10).mean()).rolling(23).min()).rolling(17).min()).rolling(16).max()) * 0.594299)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc109_252d_base_v109_signal'] = f211w_f211_working_capital_turnover_velocity_calc109_252d_base_v109_signal

def f211w_f211_working_capital_turnover_velocity_calc110_42d_base_v110_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(4) / (revenue.shift(6) + 27.3894)).diff(19)).rolling(18).min()).diff(10)).rolling(9).mean()) * 0.749844)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc110_42d_base_v110_signal'] = f211w_f211_working_capital_turnover_velocity_calc110_42d_base_v110_signal

def f211w_f211_working_capital_turnover_velocity_calc111_42d_base_v111_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(7) / (revenue.shift(5) + 98.4461)).rolling(5).var()).rolling(17).mean()).diff(14)) * 0.063686)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc111_42d_base_v111_signal'] = f211w_f211_working_capital_turnover_velocity_calc111_42d_base_v111_signal

def f211w_f211_working_capital_turnover_velocity_calc112_10d_base_v112_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 13.0057)).pct_change(2)).rolling(2).min()).rolling(4).min()) * 0.531931)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc112_10d_base_v112_signal'] = f211w_f211_working_capital_turnover_velocity_calc112_10d_base_v112_signal

def f211w_f211_working_capital_turnover_velocity_calc113_252d_base_v113_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(7).var()).pct_change(20)) * 0.430699)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc113_252d_base_v113_signal'] = f211w_f211_working_capital_turnover_velocity_calc113_252d_base_v113_signal

def f211w_f211_working_capital_turnover_velocity_calc114_42d_base_v114_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(18).min()).rolling(14).mean()).pct_change(10)).diff(11)) * 0.911374)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc114_42d_base_v114_signal'] = f211w_f211_working_capital_turnover_velocity_calc114_42d_base_v114_signal

def f211w_f211_working_capital_turnover_velocity_calc115_10d_base_v115_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 33.3736)).rolling(25).var()).pct_change(5)).rolling(5).std()) * 0.17477)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc115_10d_base_v115_signal'] = f211w_f211_working_capital_turnover_velocity_calc115_10d_base_v115_signal

def f211w_f211_working_capital_turnover_velocity_calc116_10d_base_v116_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(19)).rolling(23).min()).rolling(22).max()).diff(20)) * 0.180029)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc116_10d_base_v116_signal'] = f211w_f211_working_capital_turnover_velocity_calc116_10d_base_v116_signal

def f211w_f211_working_capital_turnover_velocity_calc117_21d_base_v117_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(27).var()).rolling(20).var()).rolling(13).mean()).rolling(4).max()) * 0.624673)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc117_21d_base_v117_signal'] = f211w_f211_working_capital_turnover_velocity_calc117_21d_base_v117_signal

def f211w_f211_working_capital_turnover_velocity_calc118_21d_base_v118_signal(workingcapital, revenue):
    res = ((((((workingcapital * 46.2281 - revenue).rolling(14).max()).rolling(20).min()).rolling(27).max()).diff(2)) * 0.046855)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc118_21d_base_v118_signal'] = f211w_f211_working_capital_turnover_velocity_calc118_21d_base_v118_signal

def f211w_f211_working_capital_turnover_velocity_calc119_42d_base_v119_signal(workingcapital, revenue):
    res = ((((workingcapital * 90.9141 - revenue).rolling(16).mean()).rolling(27).mean()) * 0.570224)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc119_42d_base_v119_signal'] = f211w_f211_working_capital_turnover_velocity_calc119_42d_base_v119_signal

def f211w_f211_working_capital_turnover_velocity_calc120_252d_base_v120_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(2) / revenue.pct_change(8)).rolling(18).min()).rolling(21).max()).rolling(13).std()) * 0.710029)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc120_252d_base_v120_signal'] = f211w_f211_working_capital_turnover_velocity_calc120_252d_base_v120_signal

def f211w_f211_working_capital_turnover_velocity_calc121_21d_base_v121_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 91.8019)).rolling(19).mean()).diff(13)).rolling(10).var()) * 0.389668)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc121_21d_base_v121_signal'] = f211w_f211_working_capital_turnover_velocity_calc121_21d_base_v121_signal

def f211w_f211_working_capital_turnover_velocity_calc122_126d_base_v122_signal(workingcapital, revenue):
    res = ((((((workingcapital * 85.1715 - revenue).rolling(13).std()).rolling(22).var()).diff(13)).rolling(21).std()) * 0.955122)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc122_126d_base_v122_signal'] = f211w_f211_working_capital_turnover_velocity_calc122_126d_base_v122_signal

def f211w_f211_working_capital_turnover_velocity_calc123_126d_base_v123_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 93.8064)).diff(14)).rolling(13).max()).rolling(13).mean()).rolling(7).var()) * 0.31339)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc123_126d_base_v123_signal'] = f211w_f211_working_capital_turnover_velocity_calc123_126d_base_v123_signal

def f211w_f211_working_capital_turnover_velocity_calc124_10d_base_v124_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 34.2391)).pct_change(4)).rolling(26).max()).rolling(28).max()) * 0.760833)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc124_10d_base_v124_signal'] = f211w_f211_working_capital_turnover_velocity_calc124_10d_base_v124_signal

def f211w_f211_working_capital_turnover_velocity_calc125_126d_base_v125_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(7).std()).pct_change(20)) * 0.046993)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc125_126d_base_v125_signal'] = f211w_f211_working_capital_turnover_velocity_calc125_126d_base_v125_signal

def f211w_f211_working_capital_turnover_velocity_calc126_252d_base_v126_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).var()).diff(15)).rolling(19).std()).rolling(11).std()) * 0.716759)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc126_252d_base_v126_signal'] = f211w_f211_working_capital_turnover_velocity_calc126_252d_base_v126_signal

def f211w_f211_working_capital_turnover_velocity_calc127_252d_base_v127_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(13)).rolling(18).max()).rolling(7).min()) * 0.895895)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc127_252d_base_v127_signal'] = f211w_f211_working_capital_turnover_velocity_calc127_252d_base_v127_signal

def f211w_f211_working_capital_turnover_velocity_calc128_252d_base_v128_signal(workingcapital, revenue):
    res = ((((workingcapital * 20.0498 - revenue).diff(17)).pct_change(4)) * 0.60257)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc128_252d_base_v128_signal'] = f211w_f211_working_capital_turnover_velocity_calc128_252d_base_v128_signal

def f211w_f211_working_capital_turnover_velocity_calc129_21d_base_v129_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 8.4791)).pct_change(15)).rolling(2).var()) * 0.167106)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc129_21d_base_v129_signal'] = f211w_f211_working_capital_turnover_velocity_calc129_21d_base_v129_signal

def f211w_f211_working_capital_turnover_velocity_calc130_42d_base_v130_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 5.4204)).rolling(5).var()).pct_change(11)) * 0.501967)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc130_42d_base_v130_signal'] = f211w_f211_working_capital_turnover_velocity_calc130_42d_base_v130_signal

def f211w_f211_working_capital_turnover_velocity_calc131_252d_base_v131_signal(workingcapital, revenue):
    res = ((((workingcapital * 14.6903 - revenue).rolling(2).mean()).rolling(8).var()) * 0.047537)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc131_252d_base_v131_signal'] = f211w_f211_working_capital_turnover_velocity_calc131_252d_base_v131_signal

def f211w_f211_working_capital_turnover_velocity_calc132_252d_base_v132_signal(workingcapital, revenue):
    res = ((((workingcapital.diff(20) / (revenue.shift(9) + 15.037)).rolling(5).var()).rolling(9).mean()) * 0.931421)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc132_252d_base_v132_signal'] = f211w_f211_working_capital_turnover_velocity_calc132_252d_base_v132_signal

def f211w_f211_working_capital_turnover_velocity_calc133_42d_base_v133_signal(workingcapital, revenue):
    res = ((((workingcapital * 63.9313 - revenue).diff(17)).rolling(9).max()) * 0.620354)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc133_42d_base_v133_signal'] = f211w_f211_working_capital_turnover_velocity_calc133_42d_base_v133_signal

def f211w_f211_working_capital_turnover_velocity_calc134_126d_base_v134_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(3)).rolling(13).max()) * 0.430654)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc134_126d_base_v134_signal'] = f211w_f211_working_capital_turnover_velocity_calc134_126d_base_v134_signal

def f211w_f211_working_capital_turnover_velocity_calc135_5d_base_v135_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(13)).rolling(10).var()) * 0.5432)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc135_5d_base_v135_signal'] = f211w_f211_working_capital_turnover_velocity_calc135_5d_base_v135_signal

def f211w_f211_working_capital_turnover_velocity_calc136_126d_base_v136_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(4) / revenue.pct_change(19)).rolling(3).std()).rolling(19).var()).rolling(28).var()) * 0.78275)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc136_126d_base_v136_signal'] = f211w_f211_working_capital_turnover_velocity_calc136_126d_base_v136_signal

def f211w_f211_working_capital_turnover_velocity_calc137_126d_base_v137_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 17.5914)).pct_change(15)).rolling(11).mean()).rolling(3).std()).pct_change(7)) * 0.77356)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc137_126d_base_v137_signal'] = f211w_f211_working_capital_turnover_velocity_calc137_126d_base_v137_signal

def f211w_f211_working_capital_turnover_velocity_calc138_5d_base_v138_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 31.628)).rolling(11).std()).rolling(29).var()).pct_change(2)).pct_change(11)) * 0.313874)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc138_5d_base_v138_signal'] = f211w_f211_working_capital_turnover_velocity_calc138_5d_base_v138_signal

def f211w_f211_working_capital_turnover_velocity_calc139_21d_base_v139_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 12.5351)).diff(16)).rolling(27).var()).rolling(10).max()) * 0.370659)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc139_21d_base_v139_signal'] = f211w_f211_working_capital_turnover_velocity_calc139_21d_base_v139_signal

def f211w_f211_working_capital_turnover_velocity_calc140_252d_base_v140_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(14) / (revenue.shift(10) + 8.3529)).rolling(4).mean()).rolling(23).var()).rolling(11).var()) * 0.42601)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc140_252d_base_v140_signal'] = f211w_f211_working_capital_turnover_velocity_calc140_252d_base_v140_signal

def f211w_f211_working_capital_turnover_velocity_calc141_42d_base_v141_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(15) / revenue.pct_change(2)).rolling(15).max()).rolling(22).var()).pct_change(2)) * 0.427594)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc141_42d_base_v141_signal'] = f211w_f211_working_capital_turnover_velocity_calc141_42d_base_v141_signal

def f211w_f211_working_capital_turnover_velocity_calc142_5d_base_v142_signal(workingcapital, revenue):
    res = ((((((workingcapital * 67.1513 - revenue).pct_change(15)).rolling(6).mean()).rolling(9).mean()).pct_change(12)) * 0.408086)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc142_5d_base_v142_signal'] = f211w_f211_working_capital_turnover_velocity_calc142_5d_base_v142_signal

def f211w_f211_working_capital_turnover_velocity_calc143_21d_base_v143_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(20) / (revenue.shift(3) + 38.3472)).pct_change(3)).rolling(6).max()).rolling(13).max()) * 0.5659)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc143_21d_base_v143_signal'] = f211w_f211_working_capital_turnover_velocity_calc143_21d_base_v143_signal

def f211w_f211_working_capital_turnover_velocity_calc144_42d_base_v144_signal(workingcapital, revenue):
    res = (((((workingcapital * 31.5071 - revenue).rolling(5).max()).rolling(26).var()).rolling(24).var()) * 0.283116)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc144_42d_base_v144_signal'] = f211w_f211_working_capital_turnover_velocity_calc144_42d_base_v144_signal

def f211w_f211_working_capital_turnover_velocity_calc145_42d_base_v145_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 21.5356)).rolling(30).std()).diff(15)).rolling(27).mean()) * 0.60964)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc145_42d_base_v145_signal'] = f211w_f211_working_capital_turnover_velocity_calc145_42d_base_v145_signal

def f211w_f211_working_capital_turnover_velocity_calc146_126d_base_v146_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(12) / (revenue.shift(2) + 96.7594)).pct_change(6)).diff(6)).pct_change(12)) * 0.976843)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc146_126d_base_v146_signal'] = f211w_f211_working_capital_turnover_velocity_calc146_126d_base_v146_signal

def f211w_f211_working_capital_turnover_velocity_calc147_63d_base_v147_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(5) / (revenue.shift(4) + 22.5017)).rolling(13).max()).rolling(27).min()).rolling(6).max()).rolling(30).max()) * 0.97543)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc147_63d_base_v147_signal'] = f211w_f211_working_capital_turnover_velocity_calc147_63d_base_v147_signal

def f211w_f211_working_capital_turnover_velocity_calc148_5d_base_v148_signal(workingcapital, revenue):
    res = ((((workingcapital * 6.6682 - revenue).rolling(12).std()).diff(3)) * 0.400197)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc148_5d_base_v148_signal'] = f211w_f211_working_capital_turnover_velocity_calc148_5d_base_v148_signal

def f211w_f211_working_capital_turnover_velocity_calc149_42d_base_v149_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 46.6367)).rolling(29).max()).rolling(28).mean()).rolling(18).mean()) * 0.517013)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc149_42d_base_v149_signal'] = f211w_f211_working_capital_turnover_velocity_calc149_42d_base_v149_signal

def f211w_f211_working_capital_turnover_velocity_calc150_10d_base_v150_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 30.482)).rolling(22).std()).rolling(10).max()).rolling(22).std()) * 0.168728)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc150_10d_base_v150_signal'] = f211w_f211_working_capital_turnover_velocity_calc150_10d_base_v150_signal


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
