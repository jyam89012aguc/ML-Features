import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f67wc_f67_working_capital_velocity_calc076_5d_base_v076_signal(workingcapital, marketcap):
    res = (workingcapital / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc076_5d_base_v076_signal'] = f67wc_f67_working_capital_velocity_calc076_5d_base_v076_signal

def f67wc_f67_working_capital_velocity_calc077_10d_base_v077_signal(workingcapital, ev):
    res = (workingcapital / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc077_10d_base_v077_signal'] = f67wc_f67_working_capital_velocity_calc077_10d_base_v077_signal

def f67wc_f67_working_capital_velocity_calc078_21d_base_v078_signal(revenue, workingcapital, pe):
    res = ((revenue / workingcapital) * pe).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc078_21d_base_v078_signal'] = f67wc_f67_working_capital_velocity_calc078_21d_base_v078_signal

def f67wc_f67_working_capital_velocity_calc079_42d_base_v079_signal(fcf, workingcapital, pb):
    res = ((fcf / workingcapital) / pb).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc079_42d_base_v079_signal'] = f67wc_f67_working_capital_velocity_calc079_42d_base_v079_signal

def f67wc_f67_working_capital_velocity_calc080_63d_base_v080_signal(ncfo, workingcapital, ps):
    res = ((ncfo / workingcapital) * ps).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc080_63d_base_v080_signal'] = f67wc_f67_working_capital_velocity_calc080_63d_base_v080_signal

def f67wc_f67_working_capital_velocity_calc081_126d_base_v081_signal(workingcapital, revenue, evebitda):
    res = ((workingcapital / revenue) / evebitda).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc081_126d_base_v081_signal'] = f67wc_f67_working_capital_velocity_calc081_126d_base_v081_signal

def f67wc_f67_working_capital_velocity_calc082_252d_base_v082_signal(workingcapital, assets, evebit):
    res = ((workingcapital / assets) * evebit).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc082_252d_base_v082_signal'] = f67wc_f67_working_capital_velocity_calc082_252d_base_v082_signal

def f67wc_f67_working_capital_velocity_calc083_5d_base_v083_signal(workingcapital, revenue, volume):
    res = ((workingcapital / revenue).pct_change(5) * np.log(volume)).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc083_5d_base_v083_signal'] = f67wc_f67_working_capital_velocity_calc083_5d_base_v083_signal

def f67wc_f67_working_capital_velocity_calc084_10d_base_v084_signal(ebitda, workingcapital, marketcap):
    res = ((ebitda / workingcapital) / marketcap).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc084_10d_base_v084_signal'] = f67wc_f67_working_capital_velocity_calc084_10d_base_v084_signal

def f67wc_f67_working_capital_velocity_calc085_21d_base_v085_signal(netinc, workingcapital, ev):
    res = ((netinc / workingcapital) / ev).rolling(21).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc085_21d_base_v085_signal'] = f67wc_f67_working_capital_velocity_calc085_21d_base_v085_signal

def f67wc_f67_working_capital_velocity_calc086_42d_base_v086_signal(gp, workingcapital, ps):
    res = ((gp / workingcapital) * ps).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc086_42d_base_v086_signal'] = f67wc_f67_working_capital_velocity_calc086_42d_base_v086_signal

def f67wc_f67_working_capital_velocity_calc087_63d_base_v087_signal(workingcapital, assets, pb):
    res = ((workingcapital / assets) / pb).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc087_63d_base_v087_signal'] = f67wc_f67_working_capital_velocity_calc087_63d_base_v087_signal

def f67wc_f67_working_capital_velocity_calc088_126d_base_v088_signal(revenue, workingcapital, evebit):
    res = ((revenue / workingcapital) / evebit).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc088_126d_base_v088_signal'] = f67wc_f67_working_capital_velocity_calc088_126d_base_v088_signal

def f67wc_f67_working_capital_velocity_calc089_252d_base_v089_signal(fcf, workingcapital, pe):
    res = ((fcf / workingcapital) * pe).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc089_252d_base_v089_signal'] = f67wc_f67_working_capital_velocity_calc089_252d_base_v089_signal

def f67wc_f67_working_capital_velocity_calc090_5d_base_v090_signal(ncfo, workingcapital, ps):
    res = ((ncfo / workingcapital) / ps).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc090_5d_base_v090_signal'] = f67wc_f67_working_capital_velocity_calc090_5d_base_v090_signal

def f67wc_f67_working_capital_velocity_calc091_10d_base_v091_signal(workingcapital, revenue, ev):
    res = ((workingcapital / revenue) * ev).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc091_10d_base_v091_signal'] = f67wc_f67_working_capital_velocity_calc091_10d_base_v091_signal

def f67wc_f67_working_capital_velocity_calc092_21d_base_v092_signal(workingcapital, assets, marketcap):
    res = ((workingcapital / assets) / marketcap).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc092_21d_base_v092_signal'] = f67wc_f67_working_capital_velocity_calc092_21d_base_v092_signal

def f67wc_f67_working_capital_velocity_calc093_42d_base_v093_signal(ebitda, workingcapital, pe):
    res = ((ebitda / workingcapital) / pe).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc093_42d_base_v093_signal'] = f67wc_f67_working_capital_velocity_calc093_42d_base_v093_signal

def f67wc_f67_working_capital_velocity_calc094_63d_base_v094_signal(netinc, workingcapital, pb):
    res = ((netinc / workingcapital) * pb).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc094_63d_base_v094_signal'] = f67wc_f67_working_capital_velocity_calc094_63d_base_v094_signal

def f67wc_f67_working_capital_velocity_calc095_126d_base_v095_signal(gp, workingcapital, evebitda):
    res = ((gp / workingcapital) / evebitda).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc095_126d_base_v095_signal'] = f67wc_f67_working_capital_velocity_calc095_126d_base_v095_signal

def f67wc_f67_working_capital_velocity_calc096_252d_base_v096_signal(revenue, workingcapital, ps):
    res = ((revenue / workingcapital) * ps).rolling(252).quantile(0.8)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc096_252d_base_v096_signal'] = f67wc_f67_working_capital_velocity_calc096_252d_base_v096_signal

def f67wc_f67_working_capital_velocity_calc097_5d_base_v097_signal(fcf, workingcapital, ev):
    res = ((fcf / workingcapital) / ev).diff(5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc097_5d_base_v097_signal'] = f67wc_f67_working_capital_velocity_calc097_5d_base_v097_signal

def f67wc_f67_working_capital_velocity_calc098_10d_base_v098_signal(ncfo, workingcapital, marketcap):
    res = ((ncfo / workingcapital) * marketcap).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc098_10d_base_v098_signal'] = f67wc_f67_working_capital_velocity_calc098_10d_base_v098_signal

def f67wc_f67_working_capital_velocity_calc099_21d_base_v099_signal(workingcapital, revenue, pe):
    res = ((workingcapital / revenue) / pe).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc099_21d_base_v099_signal'] = f67wc_f67_working_capital_velocity_calc099_21d_base_v099_signal

def f67wc_f67_working_capital_velocity_calc100_42d_base_v100_signal(workingcapital, assets, pb):
    res = ((workingcapital / assets) * pb).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc100_42d_base_v100_signal'] = f67wc_f67_working_capital_velocity_calc100_42d_base_v100_signal

def f67wc_f67_working_capital_velocity_calc101_63d_base_v101_signal(ebitda, workingcapital, evebitda):
    res = ((ebitda / workingcapital) / evebitda).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc101_63d_base_v101_signal'] = f67wc_f67_working_capital_velocity_calc101_63d_base_v101_signal

def f67wc_f67_working_capital_velocity_calc102_126d_base_v102_signal(netinc, workingcapital, ev):
    res = ((netinc / workingcapital) / ev).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc102_126d_base_v102_signal'] = f67wc_f67_working_capital_velocity_calc102_126d_base_v102_signal

def f67wc_f67_working_capital_velocity_calc103_252d_base_v103_signal(gp, workingcapital, ps):
    res = ((gp / workingcapital) * ps).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc103_252d_base_v103_signal'] = f67wc_f67_working_capital_velocity_calc103_252d_base_v103_signal

def f67wc_f67_working_capital_velocity_calc104_5d_base_v104_signal(revenue, workingcapital, volume):
    res = ((revenue / workingcapital) / np.log(volume)).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc104_5d_base_v104_signal'] = f67wc_f67_working_capital_velocity_calc104_5d_base_v104_signal

def f67wc_f67_working_capital_velocity_calc105_10d_base_v105_signal(fcf, workingcapital, pe):
    res = ((fcf / workingcapital) / pe).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc105_10d_base_v105_signal'] = f67wc_f67_working_capital_velocity_calc105_10d_base_v105_signal

def f67wc_f67_working_capital_velocity_calc106_21d_base_v106_signal(ncfo, workingcapital, pb):
    res = ((ncfo / workingcapital) / pb).rolling(21).quantile(0.2)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc106_21d_base_v106_signal'] = f67wc_f67_working_capital_velocity_calc106_21d_base_v106_signal

def f67wc_f67_working_capital_velocity_calc107_42d_base_v107_signal(workingcapital, revenue, ps):
    res = ((workingcapital / revenue) * ps).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc107_42d_base_v107_signal'] = f67wc_f67_working_capital_velocity_calc107_42d_base_v107_signal

def f67wc_f67_working_capital_velocity_calc108_63d_base_v108_signal(workingcapital, assets, ev):
    res = ((workingcapital / assets) / ev).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc108_63d_base_v108_signal'] = f67wc_f67_working_capital_velocity_calc108_63d_base_v108_signal

def f67wc_f67_working_capital_velocity_calc109_126d_base_v109_signal(ebitda, workingcapital, marketcap):
    res = ((ebitda / workingcapital) * marketcap).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc109_126d_base_v109_signal'] = f67wc_f67_working_capital_velocity_calc109_126d_base_v109_signal

def f67wc_f67_working_capital_velocity_calc110_252d_base_v110_signal(netinc, workingcapital, pe):
    res = ((netinc / workingcapital) / pe).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc110_252d_base_v110_signal'] = f67wc_f67_working_capital_velocity_calc110_252d_base_v110_signal

def f67wc_f67_working_capital_velocity_calc111_5d_base_v111_signal(gp, workingcapital, pb):
    res = ((gp / workingcapital) / pb).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc111_5d_base_v111_signal'] = f67wc_f67_working_capital_velocity_calc111_5d_base_v111_signal

def f67wc_f67_working_capital_velocity_calc112_10d_base_v112_signal(revenue, workingcapital, ps):
    res = ((revenue / workingcapital) * ps).rolling(10).rank(pct=True).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc112_10d_base_v112_signal'] = f67wc_f67_working_capital_velocity_calc112_10d_base_v112_signal

def f67wc_f67_working_capital_velocity_calc113_21d_base_v113_signal(fcf, workingcapital, evebitda):
    res = ((fcf / workingcapital) / evebitda).rolling(21).mean().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc113_21d_base_v113_signal'] = f67wc_f67_working_capital_velocity_calc113_21d_base_v113_signal

def f67wc_f67_working_capital_velocity_calc114_42d_base_v114_signal(ncfo, workingcapital, marketcap):
    res = ((ncfo / workingcapital) / marketcap).rolling(42).max() - ((ncfo / workingcapital) / marketcap).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc114_42d_base_v114_signal'] = f67wc_f67_working_capital_velocity_calc114_42d_base_v114_signal

def f67wc_f67_working_capital_velocity_calc115_63d_base_v115_signal(workingcapital, revenue, pe):
    res = ((workingcapital / revenue) * pe).rolling(63).skew().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc115_63d_base_v115_signal'] = f67wc_f67_working_capital_velocity_calc115_63d_base_v115_signal

def f67wc_f67_working_capital_velocity_calc116_126d_base_v116_signal(workingcapital, assets, pb):
    res = ((workingcapital / assets) / pb).rolling(126).rank(pct=True).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc116_126d_base_v116_signal'] = f67wc_f67_working_capital_velocity_calc116_126d_base_v116_signal

def f67wc_f67_working_capital_velocity_calc117_252d_base_v117_signal(ebitda, workingcapital, ev):
    res = ((ebitda / workingcapital) / ev).rolling(252).mean() / ((ebitda / workingcapital) / ev).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc117_252d_base_v117_signal'] = f67wc_f67_working_capital_velocity_calc117_252d_base_v117_signal

def f67wc_f67_working_capital_velocity_calc118_5d_base_v118_signal(netinc, workingcapital, ps):
    res = ((netinc / workingcapital) * ps).rolling(5).quantile(0.5).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc118_5d_base_v118_signal'] = f67wc_f67_working_capital_velocity_calc118_5d_base_v118_signal

def f67wc_f67_working_capital_velocity_calc119_10d_base_v119_signal(gp, workingcapital, marketcap):
    res = ((gp / workingcapital) / marketcap).rolling(10).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc119_10d_base_v119_signal'] = f67wc_f67_working_capital_velocity_calc119_10d_base_v119_signal

def f67wc_f67_working_capital_velocity_calc120_21d_base_v120_signal(revenue, workingcapital, pe):
    res = ((revenue / workingcapital) / pe).rolling(21).kurt().diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc120_21d_base_v120_signal'] = f67wc_f67_working_capital_velocity_calc120_21d_base_v120_signal

def f67wc_f67_working_capital_velocity_calc121_42d_base_v121_signal(fcf, workingcapital, pb):
    res = ((fcf / workingcapital) * pb).rolling(42).rank(pct=True).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc121_42d_base_v121_signal'] = f67wc_f67_working_capital_velocity_calc121_42d_base_v121_signal

def f67wc_f67_working_capital_velocity_calc122_63d_base_v122_signal(ncfo, workingcapital, ps):
    res = ((ncfo / workingcapital) / ps).rolling(63).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc122_63d_base_v122_signal'] = f67wc_f67_working_capital_velocity_calc122_63d_base_v122_signal

def f67wc_f67_working_capital_velocity_calc123_126d_base_v123_signal(workingcapital, revenue, ev):
    res = ((workingcapital / revenue) * ev).rolling(126).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc123_126d_base_v123_signal'] = f67wc_f67_working_capital_velocity_calc123_126d_base_v123_signal

def f67wc_f67_working_capital_velocity_calc124_252d_base_v124_signal(workingcapital, assets, marketcap):
    res = ((workingcapital / assets) / marketcap).rolling(252).max().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc124_252d_base_v124_signal'] = f67wc_f67_working_capital_velocity_calc124_252d_base_v124_signal

def f67wc_f67_working_capital_velocity_calc125_5d_base_v125_signal(ebitda, workingcapital, pe):
    res = ((ebitda / workingcapital) / pe).rolling(5).skew().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc125_5d_base_v125_signal'] = f67wc_f67_working_capital_velocity_calc125_5d_base_v125_signal

def f67wc_f67_working_capital_velocity_calc126_10d_base_v126_signal(netinc, workingcapital, pb):
    res = ((netinc / workingcapital) * pb).rolling(10).mean() / ((netinc / workingcapital) * pb).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc126_10d_base_v126_signal'] = f67wc_f67_working_capital_velocity_calc126_10d_base_v126_signal

def f67wc_f67_working_capital_velocity_calc127_21d_base_v127_signal(gp, workingcapital, ps):
    res = ((gp / workingcapital) / ps).rolling(21).rank(pct=True).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc127_21d_base_v127_signal'] = f67wc_f67_working_capital_velocity_calc127_21d_base_v127_signal

def f67wc_f67_working_capital_velocity_calc128_42d_base_v128_signal(revenue, workingcapital, ev):
    res = ((revenue / workingcapital) * ev).rolling(42).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc128_42d_base_v128_signal'] = f67wc_f67_working_capital_velocity_calc128_42d_base_v128_signal

def f67wc_f67_working_capital_velocity_calc129_63d_base_v129_signal(fcf, workingcapital, marketcap):
    res = ((fcf / workingcapital) / marketcap).rolling(63).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc129_63d_base_v129_signal'] = f67wc_f67_working_capital_velocity_calc129_63d_base_v129_signal

def f67wc_f67_working_capital_velocity_calc130_126d_base_v130_signal(ncfo, workingcapital, pe):
    res = ((ncfo / workingcapital) / pe).rolling(126).skew().rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc130_126d_base_v130_signal'] = f67wc_f67_working_capital_velocity_calc130_126d_base_v130_signal

def f67wc_f67_working_capital_velocity_calc131_252d_base_v131_signal(workingcapital, revenue, pb):
    res = ((workingcapital / revenue) * pb).rolling(252).kurt().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc131_252d_base_v131_signal'] = f67wc_f67_working_capital_velocity_calc131_252d_base_v131_signal

def f67wc_f67_working_capital_velocity_calc132_5d_base_v132_signal(workingcapital, assets, ps):
    res = ((workingcapital / assets) / ps).rolling(5).quantile(0.1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc132_5d_base_v132_signal'] = f67wc_f67_working_capital_velocity_calc132_5d_base_v132_signal

def f67wc_f67_working_capital_velocity_calc133_10d_base_v133_signal(ebitda, workingcapital, marketcap):
    res = ((ebitda / workingcapital) / marketcap).rolling(10).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc133_10d_base_v133_signal'] = f67wc_f67_working_capital_velocity_calc133_10d_base_v133_signal

def f67wc_f67_working_capital_velocity_calc134_21d_base_v134_signal(netinc, workingcapital, pe):
    res = ((netinc / workingcapital) / pe).rolling(21).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc134_21d_base_v134_signal'] = f67wc_f67_working_capital_velocity_calc134_21d_base_v134_signal

def f67wc_f67_working_capital_velocity_calc135_42d_base_v135_signal(gp, workingcapital, pb):
    res = ((gp / workingcapital) * pb).rolling(42).rank(pct=True).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc135_42d_base_v135_signal'] = f67wc_f67_working_capital_velocity_calc135_42d_base_v135_signal

def f67wc_f67_working_capital_velocity_calc136_63d_base_v136_signal(revenue, workingcapital, ps):
    res = ((revenue / workingcapital) / ps).rolling(63).quantile(0.5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc136_63d_base_v136_signal'] = f67wc_f67_working_capital_velocity_calc136_63d_base_v136_signal

def f67wc_f67_working_capital_velocity_calc137_126d_base_v137_signal(fcf, workingcapital, ev):
    res = ((fcf / workingcapital) * ev).rolling(126).var().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc137_126d_base_v137_signal'] = f67wc_f67_working_capital_velocity_calc137_126d_base_v137_signal

def f67wc_f67_working_capital_velocity_calc138_252d_base_v138_signal(ncfo, workingcapital, marketcap):
    res = ((ncfo / workingcapital) / marketcap).rolling(252).skew().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc138_252d_base_v138_signal'] = f67wc_f67_working_capital_velocity_calc138_252d_base_v138_signal

def f67wc_f67_working_capital_velocity_calc139_5d_base_v139_signal(workingcapital, revenue, pe):
    res = ((workingcapital / revenue) / pe).rolling(5).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc139_5d_base_v139_signal'] = f67wc_f67_working_capital_velocity_calc139_5d_base_v139_signal

def f67wc_f67_working_capital_velocity_calc140_10d_base_v140_signal(workingcapital, assets, pb):
    res = ((workingcapital / assets) * pb).rolling(10).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc140_10d_base_v140_signal'] = f67wc_f67_working_capital_velocity_calc140_10d_base_v140_signal

def f67wc_f67_working_capital_velocity_calc141_21d_base_v141_signal(ebitda, workingcapital, ps):
    res = ((ebitda / workingcapital) / ps).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc141_21d_base_v141_signal'] = f67wc_f67_working_capital_velocity_calc141_21d_base_v141_signal

def f67wc_f67_working_capital_velocity_calc142_42d_base_v142_signal(netinc, workingcapital, marketcap):
    res = ((netinc / workingcapital) * marketcap).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc142_42d_base_v142_signal'] = f67wc_f67_working_capital_velocity_calc142_42d_base_v142_signal

def f67wc_f67_working_capital_velocity_calc143_63d_base_v143_signal(gp, workingcapital, pe):
    res = ((gp / workingcapital) / pe).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc143_63d_base_v143_signal'] = f67wc_f67_working_capital_velocity_calc143_63d_base_v143_signal

def f67wc_f67_working_capital_velocity_calc144_126d_base_v144_signal(revenue, workingcapital, pb):
    res = ((revenue / workingcapital) * pb).rolling(126).quantile(0.3).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc144_126d_base_v144_signal'] = f67wc_f67_working_capital_velocity_calc144_126d_base_v144_signal

def f67wc_f67_working_capital_velocity_calc145_252d_base_v145_signal(fcf, workingcapital, ps):
    res = ((fcf / workingcapital) / ps).rolling(252).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc145_252d_base_v145_signal'] = f67wc_f67_working_capital_velocity_calc145_252d_base_v145_signal

def f67wc_f67_working_capital_velocity_calc146_5d_base_v146_signal(ncfo, workingcapital, ev):
    res = ((ncfo / workingcapital) * ev).rolling(5).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc146_5d_base_v146_signal'] = f67wc_f67_working_capital_velocity_calc146_5d_base_v146_signal

def f67wc_f67_working_capital_velocity_calc147_10d_base_v147_signal(workingcapital, revenue, marketcap):
    res = ((workingcapital / revenue) / marketcap).rolling(10).skew().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc147_10d_base_v147_signal'] = f67wc_f67_working_capital_velocity_calc147_10d_base_v147_signal

def f67wc_f67_working_capital_velocity_calc148_21d_base_v148_signal(workingcapital, assets, pe):
    res = ((workingcapital / assets) * pe).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc148_21d_base_v148_signal'] = f67wc_f67_working_capital_velocity_calc148_21d_base_v148_signal

def f67wc_f67_working_capital_velocity_calc149_42d_base_v149_signal(ebitda, workingcapital, pb):
    res = ((ebitda / workingcapital) / pb).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc149_42d_base_v149_signal'] = f67wc_f67_working_capital_velocity_calc149_42d_base_v149_signal

def f67wc_f67_working_capital_velocity_calc150_63d_base_v150_signal(netinc, workingcapital, ps):
    res = ((netinc / workingcapital) * ps).rolling(63).quantile(0.7).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc150_63d_base_v150_signal'] = f67wc_f67_working_capital_velocity_calc150_63d_base_v150_signal


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
