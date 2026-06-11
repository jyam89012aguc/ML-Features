import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f213n_f213_net_income_stability_cycles_calc076_42d_base_v076_signal(netinc, ebitda):
    res = (((((netinc.diff(7) / (ebitda.shift(9) + 56.1764)).rolling(23).min()).rolling(2).min()).rolling(21).std()) * 0.348393)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc076_42d_base_v076_signal'] = f213n_f213_net_income_stability_cycles_calc076_42d_base_v076_signal

def f213n_f213_net_income_stability_cycles_calc077_63d_base_v077_signal(netinc, ebitda):
    res = ((((((netinc * 16.7568 - ebitda).rolling(9).min()).rolling(19).min()).rolling(14).std()).rolling(29).max()) * 0.354594)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc077_63d_base_v077_signal'] = f213n_f213_net_income_stability_cycles_calc077_63d_base_v077_signal

def f213n_f213_net_income_stability_cycles_calc078_5d_base_v078_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 9.7883)).rolling(19).min()).rolling(13).min()).pct_change(7)).rolling(30).min()) * 0.223939)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc078_5d_base_v078_signal'] = f213n_f213_net_income_stability_cycles_calc078_5d_base_v078_signal

def f213n_f213_net_income_stability_cycles_calc079_63d_base_v079_signal(netinc, ebitda):
    res = (((((netinc * 27.9601 - ebitda).rolling(29).std()).rolling(17).min()).pct_change(15)) * 0.76509)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc079_63d_base_v079_signal'] = f213n_f213_net_income_stability_cycles_calc079_63d_base_v079_signal

def f213n_f213_net_income_stability_cycles_calc080_21d_base_v080_signal(netinc, ebitda):
    res = (((((netinc * 82.6312 - ebitda).pct_change(15)).diff(6)).diff(4)) * 0.450467)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc080_21d_base_v080_signal'] = f213n_f213_net_income_stability_cycles_calc080_21d_base_v080_signal

def f213n_f213_net_income_stability_cycles_calc081_42d_base_v081_signal(netinc, ebitda):
    res = ((((netinc * 58.0578 - ebitda).rolling(21).std()).rolling(18).max()) * 0.419738)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc081_42d_base_v081_signal'] = f213n_f213_net_income_stability_cycles_calc081_42d_base_v081_signal

def f213n_f213_net_income_stability_cycles_calc082_5d_base_v082_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 59.9969)).diff(16)).diff(3)).rolling(2).var()).diff(20)) * 0.727505)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc082_5d_base_v082_signal'] = f213n_f213_net_income_stability_cycles_calc082_5d_base_v082_signal

def f213n_f213_net_income_stability_cycles_calc083_252d_base_v083_signal(netinc, ebitda):
    res = ((((netinc.pct_change(15) / ebitda.pct_change(12)).rolling(17).std()).diff(7)) * 0.551016)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc083_252d_base_v083_signal'] = f213n_f213_net_income_stability_cycles_calc083_252d_base_v083_signal

def f213n_f213_net_income_stability_cycles_calc084_21d_base_v084_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(20)).rolling(9).min()) * 0.073517)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc084_21d_base_v084_signal'] = f213n_f213_net_income_stability_cycles_calc084_21d_base_v084_signal

def f213n_f213_net_income_stability_cycles_calc085_252d_base_v085_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 17.7701)).diff(3)).rolling(25).mean()).rolling(23).mean()) * 0.462178)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc085_252d_base_v085_signal'] = f213n_f213_net_income_stability_cycles_calc085_252d_base_v085_signal

def f213n_f213_net_income_stability_cycles_calc086_126d_base_v086_signal(netinc, ebitda):
    res = ((((((netinc.diff(16) / (ebitda.shift(7) + 40.694)).rolling(5).max()).diff(20)).diff(18)).diff(1)) * 0.519372)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc086_126d_base_v086_signal'] = f213n_f213_net_income_stability_cycles_calc086_126d_base_v086_signal

def f213n_f213_net_income_stability_cycles_calc087_42d_base_v087_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(22).max()).diff(15)).rolling(27).min()).rolling(5).mean()) * 0.721511)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc087_42d_base_v087_signal'] = f213n_f213_net_income_stability_cycles_calc087_42d_base_v087_signal

def f213n_f213_net_income_stability_cycles_calc088_10d_base_v088_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(6).var()).rolling(27).std()).rolling(8).min()).rolling(5).var()) * 0.752782)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc088_10d_base_v088_signal'] = f213n_f213_net_income_stability_cycles_calc088_10d_base_v088_signal

def f213n_f213_net_income_stability_cycles_calc089_21d_base_v089_signal(netinc, ebitda):
    res = ((((((netinc.diff(16) / (ebitda.shift(4) + 64.2394)).rolling(12).min()).pct_change(15)).diff(9)).rolling(10).max()) * 0.082588)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc089_21d_base_v089_signal'] = f213n_f213_net_income_stability_cycles_calc089_21d_base_v089_signal

def f213n_f213_net_income_stability_cycles_calc090_63d_base_v090_signal(netinc, ebitda):
    res = ((((((netinc.diff(17) / (ebitda.shift(5) + 3.6709)).rolling(24).var()).rolling(11).var()).diff(6)).rolling(22).max()) * 0.147221)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc090_63d_base_v090_signal'] = f213n_f213_net_income_stability_cycles_calc090_63d_base_v090_signal

def f213n_f213_net_income_stability_cycles_calc091_21d_base_v091_signal(netinc, ebitda):
    res = (((((netinc * 47.581 - ebitda).pct_change(13)).rolling(22).var()).rolling(2).std()) * 0.441065)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc091_21d_base_v091_signal'] = f213n_f213_net_income_stability_cycles_calc091_21d_base_v091_signal

def f213n_f213_net_income_stability_cycles_calc092_252d_base_v092_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(9) / ebitda.pct_change(12)).diff(17)).rolling(17).min()).rolling(30).max()).rolling(13).std()) * 0.306897)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc092_252d_base_v092_signal'] = f213n_f213_net_income_stability_cycles_calc092_252d_base_v092_signal

def f213n_f213_net_income_stability_cycles_calc093_126d_base_v093_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(29).std()).rolling(17).max()).rolling(17).std()).rolling(2).min()) * 0.845558)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc093_126d_base_v093_signal'] = f213n_f213_net_income_stability_cycles_calc093_126d_base_v093_signal

def f213n_f213_net_income_stability_cycles_calc094_126d_base_v094_signal(netinc, ebitda):
    res = ((((((netinc.diff(10) / (ebitda.shift(4) + 94.7001)).pct_change(4)).diff(7)).rolling(17).var()).rolling(20).min()) * 0.34552)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc094_126d_base_v094_signal'] = f213n_f213_net_income_stability_cycles_calc094_126d_base_v094_signal

def f213n_f213_net_income_stability_cycles_calc095_126d_base_v095_signal(netinc, ebitda):
    res = ((((netinc.pct_change(7) / ebitda.pct_change(12)).rolling(22).min()).rolling(12).mean()) * 0.833178)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc095_126d_base_v095_signal'] = f213n_f213_net_income_stability_cycles_calc095_126d_base_v095_signal

def f213n_f213_net_income_stability_cycles_calc096_63d_base_v096_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(9).max()).rolling(10).std()).pct_change(6)).diff(8)) * 0.552219)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc096_63d_base_v096_signal'] = f213n_f213_net_income_stability_cycles_calc096_63d_base_v096_signal

def f213n_f213_net_income_stability_cycles_calc097_10d_base_v097_signal(netinc, ebitda):
    res = ((((netinc.diff(2) / (ebitda.shift(10) + 68.9948)).diff(7)).diff(3)) * 0.456945)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc097_10d_base_v097_signal'] = f213n_f213_net_income_stability_cycles_calc097_10d_base_v097_signal

def f213n_f213_net_income_stability_cycles_calc098_10d_base_v098_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(19).mean()).pct_change(2)).rolling(27).var()) * 0.069648)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc098_10d_base_v098_signal'] = f213n_f213_net_income_stability_cycles_calc098_10d_base_v098_signal

def f213n_f213_net_income_stability_cycles_calc099_126d_base_v099_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 7.3981)).rolling(8).max()).rolling(17).max()).rolling(20).var()).rolling(20).mean()) * 0.478733)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc099_126d_base_v099_signal'] = f213n_f213_net_income_stability_cycles_calc099_126d_base_v099_signal

def f213n_f213_net_income_stability_cycles_calc100_42d_base_v100_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).var()).rolling(21).min()) * 0.119293)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc100_42d_base_v100_signal'] = f213n_f213_net_income_stability_cycles_calc100_42d_base_v100_signal

def f213n_f213_net_income_stability_cycles_calc101_21d_base_v101_signal(netinc, ebitda):
    res = (((((netinc.pct_change(17) / ebitda.pct_change(10)).rolling(29).var()).rolling(9).max()).rolling(10).var()) * 0.183001)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc101_21d_base_v101_signal'] = f213n_f213_net_income_stability_cycles_calc101_21d_base_v101_signal

def f213n_f213_net_income_stability_cycles_calc102_126d_base_v102_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 56.1703)).rolling(17).max()).rolling(7).min()).rolling(4).std()) * 0.312628)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc102_126d_base_v102_signal'] = f213n_f213_net_income_stability_cycles_calc102_126d_base_v102_signal

def f213n_f213_net_income_stability_cycles_calc103_252d_base_v103_signal(netinc, ebitda):
    res = ((((ebitda / (netinc + 43.2583)).pct_change(8)).rolling(11).std()) * 0.308548)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc103_252d_base_v103_signal'] = f213n_f213_net_income_stability_cycles_calc103_252d_base_v103_signal

def f213n_f213_net_income_stability_cycles_calc104_63d_base_v104_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 30.6078)).diff(5)).rolling(7).var()).rolling(26).std()).rolling(27).min()) * 0.761092)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc104_63d_base_v104_signal'] = f213n_f213_net_income_stability_cycles_calc104_63d_base_v104_signal

def f213n_f213_net_income_stability_cycles_calc105_10d_base_v105_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(17) / ebitda.pct_change(16)).pct_change(14)).pct_change(9)).rolling(10).std()).rolling(29).min()) * 0.607921)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc105_10d_base_v105_signal'] = f213n_f213_net_income_stability_cycles_calc105_10d_base_v105_signal

def f213n_f213_net_income_stability_cycles_calc106_252d_base_v106_signal(netinc, ebitda):
    res = (((((netinc.diff(11) / (ebitda.shift(6) + 30.4315)).rolling(14).max()).pct_change(14)).rolling(26).mean()) * 0.152087)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc106_252d_base_v106_signal'] = f213n_f213_net_income_stability_cycles_calc106_252d_base_v106_signal

def f213n_f213_net_income_stability_cycles_calc107_42d_base_v107_signal(netinc, ebitda):
    res = ((((netinc.pct_change(9) / ebitda.pct_change(1)).rolling(23).std()).diff(9)) * 0.410612)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc107_42d_base_v107_signal'] = f213n_f213_net_income_stability_cycles_calc107_42d_base_v107_signal

def f213n_f213_net_income_stability_cycles_calc108_21d_base_v108_signal(netinc, ebitda):
    res = ((((((netinc * 83.2719 - ebitda).rolling(27).std()).rolling(21).std()).rolling(16).max()).pct_change(9)) * 0.033205)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc108_21d_base_v108_signal'] = f213n_f213_net_income_stability_cycles_calc108_21d_base_v108_signal

def f213n_f213_net_income_stability_cycles_calc109_5d_base_v109_signal(netinc, ebitda):
    res = (((((netinc.pct_change(16) / ebitda.pct_change(2)).diff(16)).rolling(10).std()).rolling(20).max()) * 0.16721)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc109_5d_base_v109_signal'] = f213n_f213_net_income_stability_cycles_calc109_5d_base_v109_signal

def f213n_f213_net_income_stability_cycles_calc110_42d_base_v110_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(17).mean()).rolling(30).std()).diff(3)) * 0.064992)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc110_42d_base_v110_signal'] = f213n_f213_net_income_stability_cycles_calc110_42d_base_v110_signal

def f213n_f213_net_income_stability_cycles_calc111_21d_base_v111_signal(netinc, ebitda):
    res = ((((netinc * 97.7202 - ebitda).rolling(4).max()).rolling(9).min()) * 0.7278)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc111_21d_base_v111_signal'] = f213n_f213_net_income_stability_cycles_calc111_21d_base_v111_signal

def f213n_f213_net_income_stability_cycles_calc112_21d_base_v112_signal(netinc, ebitda):
    res = ((((netinc.pct_change(17) / ebitda.pct_change(10)).rolling(26).std()).pct_change(3)) * 0.757531)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc112_21d_base_v112_signal'] = f213n_f213_net_income_stability_cycles_calc112_21d_base_v112_signal

def f213n_f213_net_income_stability_cycles_calc113_252d_base_v113_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 78.6115)).rolling(9).min()).rolling(13).min()).rolling(8).var()) * 0.707175)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc113_252d_base_v113_signal'] = f213n_f213_net_income_stability_cycles_calc113_252d_base_v113_signal

def f213n_f213_net_income_stability_cycles_calc114_126d_base_v114_signal(netinc, ebitda):
    res = (((((netinc.pct_change(5) / ebitda.pct_change(4)).rolling(14).min()).pct_change(16)).pct_change(2)) * 0.263845)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc114_126d_base_v114_signal'] = f213n_f213_net_income_stability_cycles_calc114_126d_base_v114_signal

def f213n_f213_net_income_stability_cycles_calc115_252d_base_v115_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(29).max()).pct_change(11)) * 0.904723)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc115_252d_base_v115_signal'] = f213n_f213_net_income_stability_cycles_calc115_252d_base_v115_signal

def f213n_f213_net_income_stability_cycles_calc116_252d_base_v116_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 53.9271)).pct_change(4)).rolling(7).max()).pct_change(17)).pct_change(3)) * 0.286993)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc116_252d_base_v116_signal'] = f213n_f213_net_income_stability_cycles_calc116_252d_base_v116_signal

def f213n_f213_net_income_stability_cycles_calc117_63d_base_v117_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(5)).diff(11)).rolling(7).mean()) * 0.607831)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc117_63d_base_v117_signal'] = f213n_f213_net_income_stability_cycles_calc117_63d_base_v117_signal

def f213n_f213_net_income_stability_cycles_calc118_126d_base_v118_signal(netinc, ebitda):
    res = ((((netinc.diff(14) / (ebitda.shift(1) + 57.5649)).rolling(28).max()).rolling(2).min()) * 0.454966)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc118_126d_base_v118_signal'] = f213n_f213_net_income_stability_cycles_calc118_126d_base_v118_signal

def f213n_f213_net_income_stability_cycles_calc119_5d_base_v119_signal(netinc, ebitda):
    res = (((((netinc * 22.6005 - ebitda).diff(7)).pct_change(19)).rolling(30).var()) * 0.428607)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc119_5d_base_v119_signal'] = f213n_f213_net_income_stability_cycles_calc119_5d_base_v119_signal

def f213n_f213_net_income_stability_cycles_calc120_126d_base_v120_signal(netinc, ebitda):
    res = ((((netinc / (ebitda + 86.7376)).rolling(21).max()).pct_change(2)) * 0.159553)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc120_126d_base_v120_signal'] = f213n_f213_net_income_stability_cycles_calc120_126d_base_v120_signal

def f213n_f213_net_income_stability_cycles_calc121_252d_base_v121_signal(netinc, ebitda):
    res = ((((netinc.pct_change(11) / ebitda.pct_change(8)).rolling(11).std()).rolling(15).std()) * 0.351549)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc121_252d_base_v121_signal'] = f213n_f213_net_income_stability_cycles_calc121_252d_base_v121_signal

def f213n_f213_net_income_stability_cycles_calc122_21d_base_v122_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 23.3746)).rolling(16).mean()).pct_change(7)).rolling(3).min()) * 0.911481)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc122_21d_base_v122_signal'] = f213n_f213_net_income_stability_cycles_calc122_21d_base_v122_signal

def f213n_f213_net_income_stability_cycles_calc123_42d_base_v123_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 43.9108)).rolling(25).max()).rolling(5).max()).rolling(26).std()).rolling(5).std()) * 0.204665)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc123_42d_base_v123_signal'] = f213n_f213_net_income_stability_cycles_calc123_42d_base_v123_signal

def f213n_f213_net_income_stability_cycles_calc124_42d_base_v124_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 74.0901)).rolling(17).var()).rolling(18).var()).rolling(16).mean()).rolling(2).mean()) * 0.361223)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc124_42d_base_v124_signal'] = f213n_f213_net_income_stability_cycles_calc124_42d_base_v124_signal

def f213n_f213_net_income_stability_cycles_calc125_42d_base_v125_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 80.3608)).pct_change(10)).rolling(24).std()).rolling(22).mean()) * 0.402302)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc125_42d_base_v125_signal'] = f213n_f213_net_income_stability_cycles_calc125_42d_base_v125_signal

def f213n_f213_net_income_stability_cycles_calc126_126d_base_v126_signal(netinc, ebitda):
    res = ((((ebitda / (netinc + 81.0359)).rolling(20).std()).rolling(6).mean()) * 0.868423)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc126_126d_base_v126_signal'] = f213n_f213_net_income_stability_cycles_calc126_126d_base_v126_signal

def f213n_f213_net_income_stability_cycles_calc127_63d_base_v127_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(20) / ebitda.pct_change(7)).rolling(13).var()).rolling(15).max()).pct_change(6)).rolling(7).min()) * 0.691169)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc127_63d_base_v127_signal'] = f213n_f213_net_income_stability_cycles_calc127_63d_base_v127_signal

def f213n_f213_net_income_stability_cycles_calc128_10d_base_v128_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 93.6355)).rolling(11).std()).rolling(22).min()).rolling(28).var()) * 0.955994)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc128_10d_base_v128_signal'] = f213n_f213_net_income_stability_cycles_calc128_10d_base_v128_signal

def f213n_f213_net_income_stability_cycles_calc129_21d_base_v129_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 62.2292)).pct_change(5)).rolling(3).min()).rolling(14).max()).pct_change(20)) * 0.037909)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc129_21d_base_v129_signal'] = f213n_f213_net_income_stability_cycles_calc129_21d_base_v129_signal

def f213n_f213_net_income_stability_cycles_calc130_126d_base_v130_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(17).mean()).rolling(15).min()) * 0.165009)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc130_126d_base_v130_signal'] = f213n_f213_net_income_stability_cycles_calc130_126d_base_v130_signal

def f213n_f213_net_income_stability_cycles_calc131_252d_base_v131_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).std()).diff(18)).rolling(21).var()) * 0.441608)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc131_252d_base_v131_signal'] = f213n_f213_net_income_stability_cycles_calc131_252d_base_v131_signal

def f213n_f213_net_income_stability_cycles_calc132_126d_base_v132_signal(netinc, ebitda):
    res = ((((netinc * 71.6599 - ebitda).pct_change(5)).rolling(23).std()) * 0.478234)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc132_126d_base_v132_signal'] = f213n_f213_net_income_stability_cycles_calc132_126d_base_v132_signal

def f213n_f213_net_income_stability_cycles_calc133_5d_base_v133_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 74.3442)).rolling(25).std()).diff(10)).rolling(24).var()) * 0.712923)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc133_5d_base_v133_signal'] = f213n_f213_net_income_stability_cycles_calc133_5d_base_v133_signal

def f213n_f213_net_income_stability_cycles_calc134_42d_base_v134_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(5)).rolling(25).max()).pct_change(2)) * 0.519519)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc134_42d_base_v134_signal'] = f213n_f213_net_income_stability_cycles_calc134_42d_base_v134_signal

def f213n_f213_net_income_stability_cycles_calc135_126d_base_v135_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 90.6109)).rolling(28).mean()).pct_change(8)).rolling(14).std()).rolling(2).var()) * 0.387329)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc135_126d_base_v135_signal'] = f213n_f213_net_income_stability_cycles_calc135_126d_base_v135_signal

def f213n_f213_net_income_stability_cycles_calc136_63d_base_v136_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 48.1296)).rolling(10).max()).rolling(16).max()).rolling(25).mean()) * 0.850527)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc136_63d_base_v136_signal'] = f213n_f213_net_income_stability_cycles_calc136_63d_base_v136_signal

def f213n_f213_net_income_stability_cycles_calc137_21d_base_v137_signal(netinc, ebitda):
    res = (((((netinc.diff(11) / (ebitda.shift(6) + 65.5805)).pct_change(18)).rolling(23).min()).rolling(23).mean()) * 0.514201)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc137_21d_base_v137_signal'] = f213n_f213_net_income_stability_cycles_calc137_21d_base_v137_signal

def f213n_f213_net_income_stability_cycles_calc138_252d_base_v138_signal(netinc, ebitda):
    res = ((((netinc * 34.3033 - ebitda).rolling(9).mean()).rolling(28).min()) * 0.518691)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc138_252d_base_v138_signal'] = f213n_f213_net_income_stability_cycles_calc138_252d_base_v138_signal

def f213n_f213_net_income_stability_cycles_calc139_5d_base_v139_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(29).mean()).rolling(7).max()).rolling(28).min()).rolling(8).max()) * 0.708441)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc139_5d_base_v139_signal'] = f213n_f213_net_income_stability_cycles_calc139_5d_base_v139_signal

def f213n_f213_net_income_stability_cycles_calc140_10d_base_v140_signal(netinc, ebitda):
    res = ((((netinc * 84.0173 - ebitda).rolling(29).max()).rolling(18).max()) * 0.22742)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc140_10d_base_v140_signal'] = f213n_f213_net_income_stability_cycles_calc140_10d_base_v140_signal

def f213n_f213_net_income_stability_cycles_calc141_5d_base_v141_signal(netinc, ebitda):
    res = ((((ebitda / (netinc + 80.046)).diff(6)).diff(20)) * 0.365403)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc141_5d_base_v141_signal'] = f213n_f213_net_income_stability_cycles_calc141_5d_base_v141_signal

def f213n_f213_net_income_stability_cycles_calc142_10d_base_v142_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 84.3396)).rolling(14).mean()).rolling(14).var()).rolling(15).max()) * 0.746082)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc142_10d_base_v142_signal'] = f213n_f213_net_income_stability_cycles_calc142_10d_base_v142_signal

def f213n_f213_net_income_stability_cycles_calc143_42d_base_v143_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(3) / ebitda.pct_change(9)).diff(10)).rolling(25).std()).rolling(21).max()).rolling(3).mean()) * 0.143397)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc143_42d_base_v143_signal'] = f213n_f213_net_income_stability_cycles_calc143_42d_base_v143_signal

def f213n_f213_net_income_stability_cycles_calc144_252d_base_v144_signal(netinc, ebitda):
    res = (((((netinc.pct_change(13) / ebitda.pct_change(6)).rolling(20).min()).rolling(9).std()).pct_change(12)) * 0.150916)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc144_252d_base_v144_signal'] = f213n_f213_net_income_stability_cycles_calc144_252d_base_v144_signal

def f213n_f213_net_income_stability_cycles_calc145_5d_base_v145_signal(netinc, ebitda):
    res = ((((netinc.pct_change(4) / ebitda.pct_change(19)).rolling(16).std()).rolling(23).std()) * 0.940069)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc145_5d_base_v145_signal'] = f213n_f213_net_income_stability_cycles_calc145_5d_base_v145_signal

def f213n_f213_net_income_stability_cycles_calc146_21d_base_v146_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 76.0824)).rolling(17).max()).rolling(23).std()).rolling(11).min()).pct_change(4)) * 0.020554)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc146_21d_base_v146_signal'] = f213n_f213_net_income_stability_cycles_calc146_21d_base_v146_signal

def f213n_f213_net_income_stability_cycles_calc147_63d_base_v147_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(22).mean()).rolling(15).min()).rolling(7).max()) * 0.45528)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc147_63d_base_v147_signal'] = f213n_f213_net_income_stability_cycles_calc147_63d_base_v147_signal

def f213n_f213_net_income_stability_cycles_calc148_126d_base_v148_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 69.1745)).rolling(21).max()).pct_change(12)).rolling(29).std()).pct_change(16)) * 0.788567)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc148_126d_base_v148_signal'] = f213n_f213_net_income_stability_cycles_calc148_126d_base_v148_signal

def f213n_f213_net_income_stability_cycles_calc149_252d_base_v149_signal(netinc, ebitda):
    res = ((((((netinc.diff(2) / (ebitda.shift(2) + 70.1897)).rolling(12).max()).rolling(23).min()).pct_change(9)).rolling(4).var()) * 0.433828)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc149_252d_base_v149_signal'] = f213n_f213_net_income_stability_cycles_calc149_252d_base_v149_signal

def f213n_f213_net_income_stability_cycles_calc150_5d_base_v150_signal(netinc, ebitda):
    res = (((((netinc * 10.203 - ebitda).diff(9)).rolling(26).mean()).pct_change(16)) * 0.799872)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc150_5d_base_v150_signal'] = f213n_f213_net_income_stability_cycles_calc150_5d_base_v150_signal


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
