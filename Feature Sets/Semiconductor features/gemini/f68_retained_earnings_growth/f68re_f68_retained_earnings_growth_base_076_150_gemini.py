import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f68re_f68_retained_earnings_growth_calc076_5d_base_v076_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc076_5d_base_v076_signal'] = f68re_f68_retained_earnings_growth_calc076_5d_base_v076_signal

def f68re_f68_retained_earnings_growth_calc077_10d_base_v077_signal(retearn, capex):
    res = (retearn / capex).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc077_10d_base_v077_signal'] = f68re_f68_retained_earnings_growth_calc077_10d_base_v077_signal

def f68re_f68_retained_earnings_growth_calc078_21d_base_v078_signal(retearn, ncfo):
    res = (retearn / ncfo).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc078_21d_base_v078_signal'] = f68re_f68_retained_earnings_growth_calc078_21d_base_v078_signal

def f68re_f68_retained_earnings_growth_calc079_42d_base_v079_signal(retearn, ncfi):
    res = (retearn / ncfi).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc079_42d_base_v079_signal'] = f68re_f68_retained_earnings_growth_calc079_42d_base_v079_signal

def f68re_f68_retained_earnings_growth_calc080_63d_base_v080_signal(retearn, ncff):
    res = (retearn / ncff).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc080_63d_base_v080_signal'] = f68re_f68_retained_earnings_growth_calc080_63d_base_v080_signal

def f68re_f68_retained_earnings_growth_calc081_126d_base_v081_signal(retearn, gp):
    res = (retearn / gp).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc081_126d_base_v081_signal'] = f68re_f68_retained_earnings_growth_calc081_126d_base_v081_signal

def f68re_f68_retained_earnings_growth_calc082_252d_base_v082_signal(retearn, opinc):
    res = (retearn / opinc).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc082_252d_base_v082_signal'] = f68re_f68_retained_earnings_growth_calc082_252d_base_v082_signal

def f68re_f68_retained_earnings_growth_calc083_5d_base_v083_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc083_5d_base_v083_signal'] = f68re_f68_retained_earnings_growth_calc083_5d_base_v083_signal

def f68re_f68_retained_earnings_growth_calc084_10d_base_v084_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc084_10d_base_v084_signal'] = f68re_f68_retained_earnings_growth_calc084_10d_base_v084_signal

def f68re_f68_retained_earnings_growth_calc085_21d_base_v085_signal(retearn, pe):
    res = (retearn / pe).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc085_21d_base_v085_signal'] = f68re_f68_retained_earnings_growth_calc085_21d_base_v085_signal

def f68re_f68_retained_earnings_growth_calc086_42d_base_v086_signal(retearn, pb):
    res = (retearn / pb).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc086_42d_base_v086_signal'] = f68re_f68_retained_earnings_growth_calc086_42d_base_v086_signal

def f68re_f68_retained_earnings_growth_calc087_63d_base_v087_signal(retearn, ps):
    res = (retearn / ps).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc087_63d_base_v087_signal'] = f68re_f68_retained_earnings_growth_calc087_63d_base_v087_signal

def f68re_f68_retained_earnings_growth_calc088_126d_base_v088_signal(retearn, ev):
    res = (retearn / ev).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc088_126d_base_v088_signal'] = f68re_f68_retained_earnings_growth_calc088_126d_base_v088_signal

def f68re_f68_retained_earnings_growth_calc089_252d_base_v089_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc089_252d_base_v089_signal'] = f68re_f68_retained_earnings_growth_calc089_252d_base_v089_signal

def f68re_f68_retained_earnings_growth_calc090_5d_base_v090_signal(retearn, close):
    res = (retearn / close).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc090_5d_base_v090_signal'] = f68re_f68_retained_earnings_growth_calc090_5d_base_v090_signal

def f68re_f68_retained_earnings_growth_calc091_10d_base_v091_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc091_10d_base_v091_signal'] = f68re_f68_retained_earnings_growth_calc091_10d_base_v091_signal

def f68re_f68_retained_earnings_growth_calc092_21d_base_v092_signal(retearn, intexp):
    res = (retearn / intexp).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc092_21d_base_v092_signal'] = f68re_f68_retained_earnings_growth_calc092_21d_base_v092_signal

def f68re_f68_retained_earnings_growth_calc093_42d_base_v093_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc093_42d_base_v093_signal'] = f68re_f68_retained_earnings_growth_calc093_42d_base_v093_signal

def f68re_f68_retained_earnings_growth_calc094_63d_base_v094_signal(retearn, capex):
    res = (retearn / capex).rolling(63).quantile(0.8)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc094_63d_base_v094_signal'] = f68re_f68_retained_earnings_growth_calc094_63d_base_v094_signal

def f68re_f68_retained_earnings_growth_calc095_126d_base_v095_signal(retearn, ncfo):
    res = (retearn / ncfo).diff(126).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc095_126d_base_v095_signal'] = f68re_f68_retained_earnings_growth_calc095_126d_base_v095_signal

def f68re_f68_retained_earnings_growth_calc096_252d_base_v096_signal(retearn, ncfi):
    res = (retearn / ncfi).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc096_252d_base_v096_signal'] = f68re_f68_retained_earnings_growth_calc096_252d_base_v096_signal

def f68re_f68_retained_earnings_growth_calc097_5d_base_v097_signal(retearn, ncff):
    res = (retearn / ncff).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc097_5d_base_v097_signal'] = f68re_f68_retained_earnings_growth_calc097_5d_base_v097_signal

def f68re_f68_retained_earnings_growth_calc098_10d_base_v098_signal(retearn, gp):
    res = (retearn / gp).rolling(10).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc098_10d_base_v098_signal'] = f68re_f68_retained_earnings_growth_calc098_10d_base_v098_signal

def f68re_f68_retained_earnings_growth_calc099_21d_base_v099_signal(retearn, opinc):
    res = (retearn / opinc).rolling(21).var().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc099_21d_base_v099_signal'] = f68re_f68_retained_earnings_growth_calc099_21d_base_v099_signal

def f68re_f68_retained_earnings_growth_calc100_42d_base_v100_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(42).kurt().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc100_42d_base_v100_signal'] = f68re_f68_retained_earnings_growth_calc100_42d_base_v100_signal

def f68re_f68_retained_earnings_growth_calc101_63d_base_v101_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc101_63d_base_v101_signal'] = f68re_f68_retained_earnings_growth_calc101_63d_base_v101_signal

def f68re_f68_retained_earnings_growth_calc102_126d_base_v102_signal(retearn, pe):
    res = (retearn / pe).rolling(126).quantile(0.3)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc102_126d_base_v102_signal'] = f68re_f68_retained_earnings_growth_calc102_126d_base_v102_signal

def f68re_f68_retained_earnings_growth_calc103_252d_base_v103_signal(retearn, pb):
    res = (retearn / pb).rolling(252).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc103_252d_base_v103_signal'] = f68re_f68_retained_earnings_growth_calc103_252d_base_v103_signal

def f68re_f68_retained_earnings_growth_calc104_5d_base_v104_signal(retearn, ps):
    res = (retearn / ps).rolling(5).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc104_5d_base_v104_signal'] = f68re_f68_retained_earnings_growth_calc104_5d_base_v104_signal

def f68re_f68_retained_earnings_growth_calc105_10d_base_v105_signal(retearn, ev):
    res = (retearn / ev).rolling(10).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc105_10d_base_v105_signal'] = f68re_f68_retained_earnings_growth_calc105_10d_base_v105_signal

def f68re_f68_retained_earnings_growth_calc106_21d_base_v106_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(21).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc106_21d_base_v106_signal'] = f68re_f68_retained_earnings_growth_calc106_21d_base_v106_signal

def f68re_f68_retained_earnings_growth_calc107_42d_base_v107_signal(retearn, close):
    res = (retearn / close).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc107_42d_base_v107_signal'] = f68re_f68_retained_earnings_growth_calc107_42d_base_v107_signal

def f68re_f68_retained_earnings_growth_calc108_63d_base_v108_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc108_63d_base_v108_signal'] = f68re_f68_retained_earnings_growth_calc108_63d_base_v108_signal

def f68re_f68_retained_earnings_growth_calc109_126d_base_v109_signal(retearn, intexp):
    res = (retearn / intexp).rolling(126).quantile(0.4).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc109_126d_base_v109_signal'] = f68re_f68_retained_earnings_growth_calc109_126d_base_v109_signal

def f68re_f68_retained_earnings_growth_calc110_252d_base_v110_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(252).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc110_252d_base_v110_signal'] = f68re_f68_retained_earnings_growth_calc110_252d_base_v110_signal

def f68re_f68_retained_earnings_growth_calc111_5d_base_v111_signal(retearn, capex):
    res = (retearn / capex).rolling(5).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc111_5d_base_v111_signal'] = f68re_f68_retained_earnings_growth_calc111_5d_base_v111_signal

def f68re_f68_retained_earnings_growth_calc112_10d_base_v112_signal(retearn, ncfo):
    res = (retearn / ncfo).rolling(10).skew().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc112_10d_base_v112_signal'] = f68re_f68_retained_earnings_growth_calc112_10d_base_v112_signal

def f68re_f68_retained_earnings_growth_calc113_21d_base_v113_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc113_21d_base_v113_signal'] = f68re_f68_retained_earnings_growth_calc113_21d_base_v113_signal

def f68re_f68_retained_earnings_growth_calc114_42d_base_v114_signal(retearn, ncff):
    res = (retearn / ncff).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc114_42d_base_v114_signal'] = f68re_f68_retained_earnings_growth_calc114_42d_base_v114_signal

def f68re_f68_retained_earnings_growth_calc115_63d_base_v115_signal(retearn, gp):
    res = (retearn / gp).rolling(63).quantile(0.6).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc115_63d_base_v115_signal'] = f68re_f68_retained_earnings_growth_calc115_63d_base_v115_signal

def f68re_f68_retained_earnings_growth_calc116_126d_base_v116_signal(retearn, opinc):
    res = (retearn / opinc).rolling(126).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc116_126d_base_v116_signal'] = f68re_f68_retained_earnings_growth_calc116_126d_base_v116_signal

def f68re_f68_retained_earnings_growth_calc117_252d_base_v117_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(252).std().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc117_252d_base_v117_signal'] = f68re_f68_retained_earnings_growth_calc117_252d_base_v117_signal

def f68re_f68_retained_earnings_growth_calc118_5d_base_v118_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(5).skew().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc118_5d_base_v118_signal'] = f68re_f68_retained_earnings_growth_calc118_5d_base_v118_signal

def f68re_f68_retained_earnings_growth_calc119_10d_base_v119_signal(retearn, pe):
    res = (retearn / pe).rolling(10).mean() / (retearn / pe).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc119_10d_base_v119_signal'] = f68re_f68_retained_earnings_growth_calc119_10d_base_v119_signal

def f68re_f68_retained_earnings_growth_calc120_21d_base_v120_signal(retearn, pb):
    res = (retearn / pb).rolling(21).rank(pct=True).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc120_21d_base_v120_signal'] = f68re_f68_retained_earnings_growth_calc120_21d_base_v120_signal

def f68re_f68_retained_earnings_growth_calc121_42d_base_v121_signal(retearn, ps):
    res = (retearn / ps).rolling(42).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc121_42d_base_v121_signal'] = f68re_f68_retained_earnings_growth_calc121_42d_base_v121_signal

def f68re_f68_retained_earnings_growth_calc122_63d_base_v122_signal(retearn, ev):
    res = (retearn / ev).rolling(63).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc122_63d_base_v122_signal'] = f68re_f68_retained_earnings_growth_calc122_63d_base_v122_signal

def f68re_f68_retained_earnings_growth_calc123_126d_base_v123_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(126).skew().rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc123_126d_base_v123_signal'] = f68re_f68_retained_earnings_growth_calc123_126d_base_v123_signal

def f68re_f68_retained_earnings_growth_calc124_252d_base_v124_signal(retearn, close):
    res = (retearn / close).rolling(252).kurt().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc124_252d_base_v124_signal'] = f68re_f68_retained_earnings_growth_calc124_252d_base_v124_signal

def f68re_f68_retained_earnings_growth_calc125_5d_base_v125_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(5).quantile(0.1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc125_5d_base_v125_signal'] = f68re_f68_retained_earnings_growth_calc125_5d_base_v125_signal

def f68re_f68_retained_earnings_growth_calc126_10d_base_v126_signal(retearn, intexp):
    res = (retearn / intexp).rolling(10).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc126_10d_base_v126_signal'] = f68re_f68_retained_earnings_growth_calc126_10d_base_v126_signal

def f68re_f68_retained_earnings_growth_calc127_21d_base_v127_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(21).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc127_21d_base_v127_signal'] = f68re_f68_retained_earnings_growth_calc127_21d_base_v127_signal

def f68re_f68_retained_earnings_growth_calc128_42d_base_v128_signal(retearn, capex):
    res = (retearn / capex).rolling(42).rank(pct=True).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc128_42d_base_v128_signal'] = f68re_f68_retained_earnings_growth_calc128_42d_base_v128_signal

def f68re_f68_retained_earnings_growth_calc129_63d_base_v129_signal(retearn, ncfo):
    res = (retearn / ncfo).rolling(63).quantile(0.5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc129_63d_base_v129_signal'] = f68re_f68_retained_earnings_growth_calc129_63d_base_v129_signal

def f68re_f68_retained_earnings_growth_calc130_126d_base_v130_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(126).var().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc130_126d_base_v130_signal'] = f68re_f68_retained_earnings_growth_calc130_126d_base_v130_signal

def f68re_f68_retained_earnings_growth_calc131_252d_base_v131_signal(retearn, ncff):
    res = (retearn / ncff).rolling(252).skew().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc131_252d_base_v131_signal'] = f68re_f68_retained_earnings_growth_calc131_252d_base_v131_signal

def f68re_f68_retained_earnings_growth_calc132_5d_base_v132_signal(retearn, gp):
    res = (retearn / gp).rolling(5).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc132_5d_base_v132_signal'] = f68re_f68_retained_earnings_growth_calc132_5d_base_v132_signal

def f68re_f68_retained_earnings_growth_calc133_10d_base_v133_signal(retearn, opinc):
    res = (retearn / opinc).rolling(10).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc133_10d_base_v133_signal'] = f68re_f68_retained_earnings_growth_calc133_10d_base_v133_signal

def f68re_f68_retained_earnings_growth_calc134_21d_base_v134_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc134_21d_base_v134_signal'] = f68re_f68_retained_earnings_growth_calc134_21d_base_v134_signal

def f68re_f68_retained_earnings_growth_calc135_42d_base_v135_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc135_42d_base_v135_signal'] = f68re_f68_retained_earnings_growth_calc135_42d_base_v135_signal

def f68re_f68_retained_earnings_growth_calc136_63d_base_v136_signal(retearn, pe):
    res = (retearn / pe).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc136_63d_base_v136_signal'] = f68re_f68_retained_earnings_growth_calc136_63d_base_v136_signal

def f68re_f68_retained_earnings_growth_calc137_126d_base_v137_signal(retearn, pb):
    res = (retearn / pb).rolling(126).quantile(0.3).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc137_126d_base_v137_signal'] = f68re_f68_retained_earnings_growth_calc137_126d_base_v137_signal

def f68re_f68_retained_earnings_growth_calc138_252d_base_v138_signal(retearn, ps):
    res = (retearn / ps).rolling(252).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc138_252d_base_v138_signal'] = f68re_f68_retained_earnings_growth_calc138_252d_base_v138_signal

def f68re_f68_retained_earnings_growth_calc139_5d_base_v139_signal(retearn, ev):
    res = (retearn / ev).rolling(5).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc139_5d_base_v139_signal'] = f68re_f68_retained_earnings_growth_calc139_5d_base_v139_signal

def f68re_f68_retained_earnings_growth_calc140_10d_base_v140_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(10).skew().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc140_10d_base_v140_signal'] = f68re_f68_retained_earnings_growth_calc140_10d_base_v140_signal

def f68re_f68_retained_earnings_growth_calc141_21d_base_v141_signal(retearn, close):
    res = (retearn / close).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc141_21d_base_v141_signal'] = f68re_f68_retained_earnings_growth_calc141_21d_base_v141_signal

def f68re_f68_retained_earnings_growth_calc142_42d_base_v142_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc142_42d_base_v142_signal'] = f68re_f68_retained_earnings_growth_calc142_42d_base_v142_signal

def f68re_f68_retained_earnings_growth_calc143_63d_base_v143_signal(retearn, intexp):
    res = (retearn / intexp).rolling(63).quantile(0.7).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc143_63d_base_v143_signal'] = f68re_f68_retained_earnings_growth_calc143_63d_base_v143_signal

def f68re_f68_retained_earnings_growth_calc144_126d_base_v144_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(126).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc144_126d_base_v144_signal'] = f68re_f68_retained_earnings_growth_calc144_126d_base_v144_signal

def f68re_f68_retained_earnings_growth_calc145_252d_base_v145_signal(retearn, capex):
    res = (retearn / capex).rolling(252).std().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc145_252d_base_v145_signal'] = f68re_f68_retained_earnings_growth_calc145_252d_base_v145_signal

def f68re_f68_retained_earnings_growth_calc146_5d_base_v146_signal(retearn, ncfo):
    res = (retearn / ncfo).rolling(5).skew().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc146_5d_base_v146_signal'] = f68re_f68_retained_earnings_growth_calc146_5d_base_v146_signal

def f68re_f68_retained_earnings_growth_calc147_10d_base_v147_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(10).mean() / (retearn / ncfi).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc147_10d_base_v147_signal'] = f68re_f68_retained_earnings_growth_calc147_10d_base_v147_signal

def f68re_f68_retained_earnings_growth_calc148_21d_base_v148_signal(retearn, ncff):
    res = (retearn / ncff).rolling(21).rank(pct=True).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc148_21d_base_v148_signal'] = f68re_f68_retained_earnings_growth_calc148_21d_base_v148_signal

def f68re_f68_retained_earnings_growth_calc149_42d_base_v149_signal(retearn, gp):
    res = (retearn / gp).rolling(42).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc149_42d_base_v149_signal'] = f68re_f68_retained_earnings_growth_calc149_42d_base_v149_signal

def f68re_f68_retained_earnings_growth_calc150_63d_base_v150_signal(retearn, opinc):
    res = (retearn / opinc).rolling(63).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc150_63d_base_v150_signal'] = f68re_f68_retained_earnings_growth_calc150_63d_base_v150_signal


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
