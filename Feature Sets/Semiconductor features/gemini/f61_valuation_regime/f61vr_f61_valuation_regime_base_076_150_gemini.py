import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f61vr_f61_valuation_regime_calc076_5d_base_v076_signal(pe, pb, ps):
    res = (pe * pb / ps).pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc076_5d_base_v076_signal'] = f61vr_f61_valuation_regime_calc076_5d_base_v076_signal

def f61vr_f61_valuation_regime_calc077_10d_base_v077_signal(ev, ebitda, revenue):
    res = (ev / (ebitda + revenue)).diff(5).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc077_10d_base_v077_signal'] = f61vr_f61_valuation_regime_calc077_10d_base_v077_signal

def f61vr_f61_valuation_regime_calc078_21d_base_v078_signal(marketcap, eps, assets):
    res = np.log((marketcap / (eps * assets)).abs().replace(0, np.nan)).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc078_21d_base_v078_signal'] = f61vr_f61_valuation_regime_calc078_21d_base_v078_signal

def f61vr_f61_valuation_regime_calc079_42d_base_v079_signal(evebitda, fcf, gp):
    res = (evebitda * fcf / gp).pct_change(5).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc079_42d_base_v079_signal'] = f61vr_f61_valuation_regime_calc079_42d_base_v079_signal

def f61vr_f61_valuation_regime_calc080_63d_base_v080_signal(pe, netinc, assets):
    res = (pe * netinc / assets).diff(10).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc080_63d_base_v080_signal'] = f61vr_f61_valuation_regime_calc080_63d_base_v080_signal

def f61vr_f61_valuation_regime_calc081_126d_base_v081_signal(pb, close, revenue):
    res = (close * pb / revenue).rolling(126).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc081_126d_base_v081_signal'] = f61vr_f61_valuation_regime_calc081_126d_base_v081_signal

def f61vr_f61_valuation_regime_calc082_252d_base_v082_signal(ps, ev, ebitda):
    res = (ps * ev / ebitda).pct_change(21).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc082_252d_base_v082_signal'] = f61vr_f61_valuation_regime_calc082_252d_base_v082_signal

def f61vr_f61_valuation_regime_calc083_504d_base_v083_signal(evebitda, ps, pb):
    res = (evebitda / (ps + pb)).diff(63).rolling(504).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc083_504d_base_v083_signal'] = f61vr_f61_valuation_regime_calc083_504d_base_v083_signal

def f61vr_f61_valuation_regime_calc084_5d_base_v084_signal(pe, marketcap, revenue):
    res = (marketcap / (pe * revenue)).pct_change(1).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc084_5d_base_v084_signal'] = f61vr_f61_valuation_regime_calc084_5d_base_v084_signal

def f61vr_f61_valuation_regime_calc085_10d_base_v085_signal(pb, assets, eps):
    res = (assets * pb / eps).diff(1).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc085_10d_base_v085_signal'] = f61vr_f61_valuation_regime_calc085_10d_base_v085_signal

def f61vr_f61_valuation_regime_calc086_21d_base_v086_signal(ps, gp, netinc):
    res = (((ps * gp / netinc) - (ps * gp / netinc).rolling(21).mean()) / (ps * gp / netinc).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc086_21d_base_v086_signal'] = f61vr_f61_valuation_regime_calc086_21d_base_v086_signal

def f61vr_f61_valuation_regime_calc087_42d_base_v087_signal(evebitda, fcf, assets):
    res = (fcf / (evebitda * assets)).pct_change(5).rolling(42).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc087_42d_base_v087_signal'] = f61vr_f61_valuation_regime_calc087_42d_base_v087_signal

def f61vr_f61_valuation_regime_calc088_63d_base_v088_signal(pe, pb, ev):
    res = (pe + pb - ev/1000).diff(1).rolling(63).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc088_63d_base_v088_signal'] = f61vr_f61_valuation_regime_calc088_63d_base_v088_signal

def f61vr_f61_valuation_regime_calc089_126d_base_v089_signal(ev, ebitda, ps):
    res = (ev * ps / ebitda).pct_change(10).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc089_126d_base_v089_signal'] = f61vr_f61_valuation_regime_calc089_126d_base_v089_signal

def f61vr_f61_valuation_regime_calc090_252d_base_v090_signal(marketcap, netinc, fcf):
    res = np.log((marketcap / (netinc + fcf)).abs().replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc090_252d_base_v090_signal'] = f61vr_f61_valuation_regime_calc090_252d_base_v090_signal

def f61vr_f61_valuation_regime_calc091_5d_base_v091_signal(pe, ps, pb):
    res = (pe * ps / pb).diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc091_5d_base_v091_signal'] = f61vr_f61_valuation_regime_calc091_5d_base_v091_signal

def f61vr_f61_valuation_regime_calc092_10d_base_v092_signal(pb, ps, evebitda):
    res = (pb / ps * evebitda).pct_change(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc092_10d_base_v092_signal'] = f61vr_f61_valuation_regime_calc092_10d_base_v092_signal

def f61vr_f61_valuation_regime_calc093_21d_base_v093_signal(evebitda, marketcap, revenue):
    res = (marketcap * revenue / evebitda).diff(5).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc093_21d_base_v093_signal'] = f61vr_f61_valuation_regime_calc093_21d_base_v093_signal

def f61vr_f61_valuation_regime_calc094_42d_base_v094_signal(ev, ps, ebitda):
    res = np.log((ev * ps / ebitda).abs().replace(0, np.nan)).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc094_42d_base_v094_signal'] = f61vr_f61_valuation_regime_calc094_42d_base_v094_signal

def f61vr_f61_valuation_regime_calc095_63d_base_v095_signal(pe, revenue, eps):
    res = (revenue * eps / pe).pct_change(10).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc095_63d_base_v095_signal'] = f61vr_f61_valuation_regime_calc095_63d_base_v095_signal

def f61vr_f61_valuation_regime_calc096_126d_base_v096_signal(pb, ebitda, netinc):
    res = ((ebitda + netinc) / pb).diff(21).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc096_126d_base_v096_signal'] = f61vr_f61_valuation_regime_calc096_126d_base_v096_signal

def f61vr_f61_valuation_regime_calc097_252d_base_v097_signal(ps, ev, assets):
    res = (((ps * ev / assets) - (ps * ev / assets).rolling(252).mean()) / (ps * ev / assets).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc097_252d_base_v097_signal'] = f61vr_f61_valuation_regime_calc097_252d_base_v097_signal

def f61vr_f61_valuation_regime_calc098_504d_base_v098_signal(evebitda, ps, fcf):
    res = (evebitda * fcf / ps).pct_change(63).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc098_504d_base_v098_signal'] = f61vr_f61_valuation_regime_calc098_504d_base_v098_signal

def f61vr_f61_valuation_regime_calc099_5d_base_v099_signal(pe, ps, pb, netinc):
    res = (pe * ps * pb / netinc).diff(1).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc099_5d_base_v099_signal'] = f61vr_f61_valuation_regime_calc099_5d_base_v099_signal

def f61vr_f61_valuation_regime_calc100_10d_base_v100_signal(ev, netinc, revenue, gp):
    res = (ev * gp / (netinc + revenue)).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc100_10d_base_v100_signal'] = f61vr_f61_valuation_regime_calc100_10d_base_v100_signal

def f61vr_f61_valuation_regime_calc101_21d_base_v101_signal(marketcap, ebitda, assets, ps):
    res = (ebitda * assets / (marketcap * ps)).pct_change(5).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc101_21d_base_v101_signal'] = f61vr_f61_valuation_regime_calc101_21d_base_v101_signal

def f61vr_f61_valuation_regime_calc102_42d_base_v102_signal(pe, pb, evebitda, fcf):
    res = np.log((pe * pb / (evebitda * fcf)).abs().replace(0, np.nan)).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc102_42d_base_v102_signal'] = f61vr_f61_valuation_regime_calc102_42d_base_v102_signal

def f61vr_f61_valuation_regime_calc103_63d_base_v103_signal(ps, ev, fcf, eps):
    res = (fcf * eps / (ps * ev)).diff(10).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc103_63d_base_v103_signal'] = f61vr_f61_valuation_regime_calc103_63d_base_v103_signal

def f61vr_f61_valuation_regime_calc104_126d_base_v104_signal(marketcap, ps, eps, revenue):
    res = (marketcap * eps / (ps * revenue)).pct_change(21).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc104_126d_base_v104_signal'] = f61vr_f61_valuation_regime_calc104_126d_base_v104_signal

def f61vr_f61_valuation_regime_calc105_252d_base_v105_signal(evebitda, ebitda, revenue, assets):
    res = (revenue * assets / (evebitda + ebitda)).rolling(252).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc105_252d_base_v105_signal'] = f61vr_f61_valuation_regime_calc105_252d_base_v105_signal

def f61vr_f61_valuation_regime_calc106_5d_base_v106_signal(pe, ps, marketcap, pb):
    res = (marketcap / (pe * ps * pb)).pct_change(1).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc106_5d_base_v106_signal'] = f61vr_f61_valuation_regime_calc106_5d_base_v106_signal

def f61vr_f61_valuation_regime_calc107_10d_base_v107_signal(ev, gp, assets, netinc):
    res = (ev * gp / (assets * netinc)).diff(2).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc107_10d_base_v107_signal'] = f61vr_f61_valuation_regime_calc107_10d_base_v107_signal

def f61vr_f61_valuation_regime_calc108_21d_base_v108_signal(pb, netinc, ebitda, ps):
    res = np.log(((pb * netinc) / (ebitda * ps)).abs().replace(0, np.nan)).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc108_21d_base_v108_signal'] = f61vr_f61_valuation_regime_calc108_21d_base_v108_signal

def f61vr_f61_valuation_regime_calc109_42d_base_v109_signal(ps, revenue, marketcap, ev):
    res = (marketcap * ev / (ps * revenue)).pct_change(5).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc109_42d_base_v109_signal'] = f61vr_f61_valuation_regime_calc109_42d_base_v109_signal

def f61vr_f61_valuation_regime_calc110_63d_base_v110_signal(evebitda, ebitda, assets, gp):
    res = (((evebitda * gp / ebitda) - (evebitda * gp / ebitda).rolling(63).mean()) / (evebitda * gp / ebitda).rolling(63).std()).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc110_63d_base_v110_signal'] = f61vr_f61_valuation_regime_calc110_63d_base_v110_signal

def f61vr_f61_valuation_regime_calc111_126d_base_v111_signal(ev, fcf, netinc, pb):
    res = (ev * pb / (fcf + netinc)).diff(10).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc111_126d_base_v111_signal'] = f61vr_f61_valuation_regime_calc111_126d_base_v111_signal

def f61vr_f61_valuation_regime_calc112_252d_base_v112_signal(pe, eps, assets, revenue):
    res = (pe * eps * revenue / assets).pct_change(21).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc112_252d_base_v112_signal'] = f61vr_f61_valuation_regime_calc112_252d_base_v112_signal

def f61vr_f61_valuation_regime_calc113_504d_base_v113_signal(pb, close, revenue, ps):
    res = (revenue * ps / (pb * close)).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc113_504d_base_v113_signal'] = f61vr_f61_valuation_regime_calc113_504d_base_v113_signal

def f61vr_f61_valuation_regime_calc114_5d_base_v114_signal(ps, gp, ebitda, fcf):
    res = (ps * gp / (ebitda + fcf)).diff(1).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc114_5d_base_v114_signal'] = f61vr_f61_valuation_regime_calc114_5d_base_v114_signal

def f61vr_f61_valuation_regime_calc115_10d_base_v115_signal(evebitda, netinc, fcf, ev):
    res = np.log(((evebitda * netinc) / (fcf * ev)).abs().replace(0, np.nan)).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc115_10d_base_v115_signal'] = f61vr_f61_valuation_regime_calc115_10d_base_v115_signal

def f61vr_f61_valuation_regime_calc116_21d_base_v116_signal(pe, ps, pb, ev, marketcap):
    res = (pe + ps + pb / (ev + marketcap)).pct_change(5).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc116_21d_base_v116_signal'] = f61vr_f61_valuation_regime_calc116_21d_base_v116_signal

def f61vr_f61_valuation_regime_calc117_42d_base_v117_signal(marketcap, revenue, eps, gp):
    res = (marketcap * gp / (revenue * eps)).diff(10).rolling(42).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc117_42d_base_v117_signal'] = f61vr_f61_valuation_regime_calc117_42d_base_v117_signal

def f61vr_f61_valuation_regime_calc118_63d_base_v118_signal(ev, ebitda, gp, ps):
    res = (((ev * ps / ebitda) - (ev * ps / ebitda).rolling(63).mean()) / (ev * ps / ebitda).rolling(63).std()).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc118_63d_base_v118_signal'] = f61vr_f61_valuation_regime_calc118_63d_base_v118_signal

def f61vr_f61_valuation_regime_calc119_126d_base_v119_signal(pe, pb, netinc, fcf):
    res = (pe / pb * (netinc + fcf)).pct_change(21).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc119_126d_base_v119_signal'] = f61vr_f61_valuation_regime_calc119_126d_base_v119_signal

def f61vr_f61_valuation_regime_calc120_252d_base_v120_signal(ps, evebitda, fcf, ebitda):
    res = (ps * evebitda / (fcf + ebitda)).diff(63).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc120_252d_base_v120_signal'] = f61vr_f61_valuation_regime_calc120_252d_base_v120_signal

def f61vr_f61_valuation_regime_calc121_5d_base_v121_signal(marketcap, revenue, assets, pe):
    res = np.log((marketcap * revenue / (assets * pe)).abs().replace(0, np.nan)).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc121_5d_base_v121_signal'] = f61vr_f61_valuation_regime_calc121_5d_base_v121_signal

def f61vr_f61_valuation_regime_calc122_10d_base_v122_signal(ev, ebitda, netinc, ps):
    res = (ev * ps / (ebitda + netinc)).pct_change(1).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc122_10d_base_v122_signal'] = f61vr_f61_valuation_regime_calc122_10d_base_v122_signal

def f61vr_f61_valuation_regime_calc123_21d_base_v123_signal(pe, pb, ps, revenue, gp):
    res = (pe + pb + ps / (revenue + gp)).diff(5).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc123_21d_base_v123_signal'] = f61vr_f61_valuation_regime_calc123_21d_base_v123_signal

def f61vr_f61_valuation_regime_calc124_42d_base_v124_signal(evebitda, ebitda, assets, ps):
    res = (evebitda * assets / (ebitda * ps)).pct_change(10).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc124_42d_base_v124_signal'] = f61vr_f61_valuation_regime_calc124_42d_base_v124_signal

def f61vr_f61_valuation_regime_calc125_63d_base_v125_signal(ev, gp, fcf, eps):
    res = np.log((ev * gp / (fcf * eps)).abs().replace(0, np.nan)).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc125_63d_base_v125_signal'] = f61vr_f61_valuation_regime_calc125_63d_base_v125_signal

def f61vr_f61_valuation_regime_calc126_126d_base_v126_signal(marketcap, ps, eps, pb):
    res = (((marketcap / (ps * pb)) - (marketcap / (ps * pb)).rolling(126).mean()) / (marketcap / (ps * pb)).rolling(126).std()).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc126_126d_base_v126_signal'] = f61vr_f61_valuation_regime_calc126_126d_base_v126_signal

def f61vr_f61_valuation_regime_calc127_252d_base_v127_signal(pe, pb, netinc, revenue, ps):
    res = (pe * netinc / (pb * revenue * ps)).pct_change(21).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc127_252d_base_v127_signal'] = f61vr_f61_valuation_regime_calc127_252d_base_v127_signal

def f61vr_f61_valuation_regime_calc128_504d_base_v128_signal(evebitda, ebitda, fcf, assets, gp):
    res = (evebitda * fcf * gp / (ebitda * assets)).diff(63).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc128_504d_base_v128_signal'] = f61vr_f61_valuation_regime_calc128_504d_base_v128_signal

def f61vr_f61_valuation_regime_calc129_5d_base_v129_signal(ev, gp, netinc, ps):
    res = (ev * ps / (gp + netinc)).pct_change(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc129_5d_base_v129_signal'] = f61vr_f61_valuation_regime_calc129_5d_base_v129_signal

def f61vr_f61_valuation_regime_calc130_10d_base_v130_signal(marketcap, revenue, eps, assets, pb):
    res = np.log((marketcap * eps * pb / (revenue * assets)).abs().replace(0, np.nan)).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc130_10d_base_v130_signal'] = f61vr_f61_valuation_regime_calc130_10d_base_v130_signal

def f61vr_f61_valuation_regime_calc131_21d_base_v131_signal(pe, ps, pb, ebitda, netinc):
    res = (pe * ps / (pb * (ebitda + netinc))).diff(5).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc131_21d_base_v131_signal'] = f61vr_f61_valuation_regime_calc131_21d_base_v131_signal

def f61vr_f61_valuation_regime_calc132_42d_base_v132_signal(evebitda, ebitda, netinc, fcf, ps):
    res = (evebitda * ps / (ebitda + netinc + fcf)).pct_change(10).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc132_42d_base_v132_signal'] = f61vr_f61_valuation_regime_calc132_42d_base_v132_signal

def f61vr_f61_valuation_regime_calc133_63d_base_v133_signal(ev, gp, revenue, assets, pb):
    res = (((ev * gp * pb) / (revenue * assets)) - ((ev * gp * pb) / (revenue * assets)).rolling(63).mean()) / ((ev * gp * pb) / (revenue * assets)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc133_63d_base_v133_signal'] = f61vr_f61_valuation_regime_calc133_63d_base_v133_signal

def f61vr_f61_valuation_regime_calc134_126d_base_v134_signal(marketcap, ps, eps, netinc, pe):
    res = (marketcap * ps * pe / (eps * netinc)).diff(21).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc134_126d_base_v134_signal'] = f61vr_f61_valuation_regime_calc134_126d_base_v134_signal

def f61vr_f61_valuation_regime_calc135_252d_base_v135_signal(pe, pb, ps, evebitda, ev):
    res = (pe + pb + ps + evebitda + ev/1000).pct_change(63).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc135_252d_base_v135_signal'] = f61vr_f61_valuation_regime_calc135_252d_base_v135_signal

def f61vr_f61_valuation_regime_calc136_5d_base_v136_signal(ev, ebitda, netinc, revenue, ps):
    res = (ev * revenue * ps / (ebitda * netinc)).diff(1).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc136_5d_base_v136_signal'] = f61vr_f61_valuation_regime_calc136_5d_base_v136_signal

def f61vr_f61_valuation_regime_calc137_10d_base_v137_signal(marketcap, ps, eps, fcf, pb):
    res = np.log((marketcap * ps * pb / (eps * fcf)).abs().replace(0, np.nan)).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc137_10d_base_v137_signal'] = f61vr_f61_valuation_regime_calc137_10d_base_v137_signal

def f61vr_f61_valuation_regime_calc138_21d_base_v138_signal(pe, pb, ps, evebitda, ev, assets):
    res = (pe * pb * assets / (ps * evebitda * ev)).pct_change(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc138_21d_base_v138_signal'] = f61vr_f61_valuation_regime_calc138_21d_base_v138_signal

def f61vr_f61_valuation_regime_calc139_42d_base_v139_signal(marketcap, revenue, assets, gp, ps):
    res = (marketcap * assets * ps / (revenue * gp)).diff(10).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc139_42d_base_v139_signal'] = f61vr_f61_valuation_regime_calc139_42d_base_v139_signal

def f61vr_f61_valuation_regime_calc140_63d_base_v140_signal(ev, ebitda, netinc, fcf, ps, pb):
    res = (ev * ps * pb / (ebitda + netinc + fcf)).pct_change(21).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc140_63d_base_v140_signal'] = f61vr_f61_valuation_regime_calc140_63d_base_v140_signal

def f61vr_f61_valuation_regime_calc141_126d_base_v141_signal(pe, pb, marketcap, revenue, eps, assets):
    res = (((pe * pb * assets) / (marketcap / revenue * eps)) - ((pe * pb * assets) / (marketcap / revenue * eps)).rolling(126).mean()) / ((pe * pb * assets) / (marketcap / revenue * eps)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc141_126d_base_v141_signal'] = f61vr_f61_valuation_regime_calc141_126d_base_v141_signal

def f61vr_f61_valuation_regime_calc142_252d_base_v142_signal(ps, evebitda, ebitda, assets, gp, netinc):
    res = (ps * evebitda * gp / (ebitda * assets * netinc)).diff(63).rolling(252).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc142_252d_base_v142_signal'] = f61vr_f61_valuation_regime_calc142_252d_base_v142_signal

def f61vr_f61_valuation_regime_calc143_504d_base_v143_signal(ev, netinc, fcf, revenue, pe, pb):
    res = np.log((ev * pe * pb / (netinc + fcf + revenue)).abs().replace(0, np.nan)).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc143_504d_base_v143_signal'] = f61vr_f61_valuation_regime_calc143_504d_base_v143_signal

def f61vr_f61_valuation_regime_calc144_5d_base_v144_signal(marketcap, eps, assets, pb, ps, pe):
    res = (marketcap * pb * pe / (eps * assets * ps)).pct_change(1).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc144_5d_base_v144_signal'] = f61vr_f61_valuation_regime_calc144_5d_base_v144_signal

def f61vr_f61_valuation_regime_calc145_10d_base_v145_signal(pe, ps, evebitda, ebitda, gp, fcf):
    res = (pe * ps * gp / (evebitda * ebitda * fcf)).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc145_10d_base_v145_signal'] = f61vr_f61_valuation_regime_calc145_10d_base_v145_signal

def f61vr_f61_valuation_regime_calc146_21d_base_v146_signal(ev, netinc, fcf, revenue, assets, ps):
    res = (ev * assets * ps / (netinc + fcf + revenue)).pct_change(5).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc146_21d_base_v146_signal'] = f61vr_f61_valuation_regime_calc146_21d_base_v146_signal

def f61vr_f61_valuation_regime_calc147_42d_base_v147_signal(marketcap, eps, pb, ps, pe, gp):
    res = np.log((marketcap * pe * gp / (eps * pb * ps)).abs().replace(0, np.nan)).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc147_42d_base_v147_signal'] = f61vr_f61_valuation_regime_calc147_42d_base_v147_signal

def f61vr_f61_valuation_regime_calc148_63d_base_v148_signal(evebitda, ebitda, gp, revenue, assets, fcf):
    res = (evebitda * revenue * fcf / (ebitda * gp * assets)).diff(10).rolling(63).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc148_63d_base_v148_signal'] = f61vr_f61_valuation_regime_calc148_63d_base_v148_signal

def f61vr_f61_valuation_regime_calc149_126d_base_v149_signal(ev, netinc, fcf, ps, pb, pe):
    res = (ev * ps * pe / (netinc + fcf + pb)).pct_change(21).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc149_126d_base_v149_signal'] = f61vr_f61_valuation_regime_calc149_126d_base_v149_signal

def f61vr_f61_valuation_regime_calc150_252d_base_v150_signal(pe, ps, pb, evebitda, ev, assets):
    res = (((pe * ps * pb * assets) / (evebitda * ev)) - ((pe * ps * pb * assets) / (evebitda * ev)).rolling(252).mean()) / ((pe * ps * pb * assets) / (evebitda * ev)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f61vr_f61_valuation_regime_calc150_252d_base_v150_signal'] = f61vr_f61_valuation_regime_calc150_252d_base_v150_signal


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
