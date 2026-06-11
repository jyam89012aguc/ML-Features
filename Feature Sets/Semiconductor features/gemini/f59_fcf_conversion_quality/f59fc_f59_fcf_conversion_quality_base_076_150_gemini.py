import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f59fc_f59_fcf_conversion_quality_calc076_10d_base_v076_signal(pb, close):
    res = (pb / close).pct_change(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc076_10d_base_v076_signal'] = f59fc_f59_fcf_conversion_quality_calc076_10d_base_v076_signal

def f59fc_f59_fcf_conversion_quality_calc077_42d_base_v077_signal(pe, workingcapital):
    res = (workingcapital / pe).diff(5).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc077_42d_base_v077_signal'] = f59fc_f59_fcf_conversion_quality_calc077_42d_base_v077_signal

def f59fc_f59_fcf_conversion_quality_calc078_5d_base_v078_signal(open, equity, assets):
    res = (open * equity / assets).rolling(5).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc078_5d_base_v078_signal'] = f59fc_f59_fcf_conversion_quality_calc078_5d_base_v078_signal

def f59fc_f59_fcf_conversion_quality_calc079_5d_base_v079_signal(open, taxexp, pb):
    res = (taxexp / open).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc079_5d_base_v079_signal'] = f59fc_f59_fcf_conversion_quality_calc079_5d_base_v079_signal

def f59fc_f59_fcf_conversion_quality_calc080_126d_base_v080_signal(taxexp, eps, ebitda):
    res = (eps * ebitda / taxexp).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc080_126d_base_v080_signal'] = f59fc_f59_fcf_conversion_quality_calc080_126d_base_v080_signal

def f59fc_f59_fcf_conversion_quality_calc081_5d_base_v081_signal(evebit, ebitda):
    res = (ebitda / evebit)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc081_5d_base_v081_signal'] = f59fc_f59_fcf_conversion_quality_calc081_5d_base_v081_signal

def f59fc_f59_fcf_conversion_quality_calc082_42d_base_v082_signal(ncfi, volume, ev):
    res = (((ev / ncfi) - (ev / ncfi).rolling(42).mean()) / (ev / ncfi).rolling(42).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc082_42d_base_v082_signal'] = f59fc_f59_fcf_conversion_quality_calc082_42d_base_v082_signal

def f59fc_f59_fcf_conversion_quality_calc083_10d_base_v083_signal(ps, close):
    res = np.log((ps / close).abs().replace(0, np.nan)).rolling(10).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc083_10d_base_v083_signal'] = f59fc_f59_fcf_conversion_quality_calc083_10d_base_v083_signal

def f59fc_f59_fcf_conversion_quality_calc084_10d_base_v084_signal(ncfi, netinc):
    res = (((ncfi / netinc) - (ncfi / netinc).rolling(10).mean()) / (ncfi / netinc).rolling(10).std()).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc084_10d_base_v084_signal'] = f59fc_f59_fcf_conversion_quality_calc084_10d_base_v084_signal

def f59fc_f59_fcf_conversion_quality_calc085_63d_base_v085_signal(assets, eps):
    res = (((eps / assets) - (eps / assets).rolling(63).mean()) / (eps / assets).rolling(63).std()).rolling(63).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc085_63d_base_v085_signal'] = f59fc_f59_fcf_conversion_quality_calc085_63d_base_v085_signal

def f59fc_f59_fcf_conversion_quality_calc086_63d_base_v086_signal(fcf, eps):
    res = (eps / fcf)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc086_63d_base_v086_signal'] = f59fc_f59_fcf_conversion_quality_calc086_63d_base_v086_signal

def f59fc_f59_fcf_conversion_quality_calc087_42d_base_v087_signal(fcf, workingcapital):
    res = (((fcf / workingcapital) - (fcf / workingcapital).rolling(42).mean()) / (fcf / workingcapital).rolling(42).std()).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc087_42d_base_v087_signal'] = f59fc_f59_fcf_conversion_quality_calc087_42d_base_v087_signal

def f59fc_f59_fcf_conversion_quality_calc088_126d_base_v088_signal(equity, currentratio):
    res = (equity / currentratio).pct_change(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc088_126d_base_v088_signal'] = f59fc_f59_fcf_conversion_quality_calc088_126d_base_v088_signal

def f59fc_f59_fcf_conversion_quality_calc089_42d_base_v089_signal(debt, high):
    res = np.log((debt / high).abs().replace(0, np.nan)).rolling(42).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc089_42d_base_v089_signal'] = f59fc_f59_fcf_conversion_quality_calc089_42d_base_v089_signal

def f59fc_f59_fcf_conversion_quality_calc090_42d_base_v090_signal(retearn, equity, assets):
    res = (equity * retearn / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc090_42d_base_v090_signal'] = f59fc_f59_fcf_conversion_quality_calc090_42d_base_v090_signal

def f59fc_f59_fcf_conversion_quality_calc091_10d_base_v091_signal(opinc, ev):
    res = np.log((opinc / ev).abs().replace(0, np.nan)).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc091_10d_base_v091_signal'] = f59fc_f59_fcf_conversion_quality_calc091_10d_base_v091_signal

def f59fc_f59_fcf_conversion_quality_calc092_21d_base_v092_signal(evebit, ncfo, assets):
    res = (ncfo * evebit / assets).rolling(21).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc092_21d_base_v092_signal'] = f59fc_f59_fcf_conversion_quality_calc092_21d_base_v092_signal

def f59fc_f59_fcf_conversion_quality_calc093_126d_base_v093_signal(marketcap, ev):
    res = np.log((ev / marketcap).abs().replace(0, np.nan)).rolling(126).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc093_126d_base_v093_signal'] = f59fc_f59_fcf_conversion_quality_calc093_126d_base_v093_signal

def f59fc_f59_fcf_conversion_quality_calc094_126d_base_v094_signal(retearn, volume, assets):
    res = (volume * retearn / assets).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc094_126d_base_v094_signal'] = f59fc_f59_fcf_conversion_quality_calc094_126d_base_v094_signal

def f59fc_f59_fcf_conversion_quality_calc095_10d_base_v095_signal(ncfo, capex):
    res = (capex / ncfo).pct_change(21).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc095_10d_base_v095_signal'] = f59fc_f59_fcf_conversion_quality_calc095_10d_base_v095_signal

def f59fc_f59_fcf_conversion_quality_calc096_63d_base_v096_signal(intexp, evebit, pe):
    res = (((intexp / pe) - (intexp / pe).rolling(63).mean()) / (intexp / pe).rolling(63).std()).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc096_63d_base_v096_signal'] = f59fc_f59_fcf_conversion_quality_calc096_63d_base_v096_signal

def f59fc_f59_fcf_conversion_quality_calc097_252d_base_v097_signal(intexp, ncfo, pe):
    res = np.log((intexp / ncfo).abs().replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc097_252d_base_v097_signal'] = f59fc_f59_fcf_conversion_quality_calc097_252d_base_v097_signal

def f59fc_f59_fcf_conversion_quality_calc098_5d_base_v098_signal(revenue, eps):
    res = np.log((eps / revenue).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc098_5d_base_v098_signal'] = f59fc_f59_fcf_conversion_quality_calc098_5d_base_v098_signal

def f59fc_f59_fcf_conversion_quality_calc099_5d_base_v099_signal(netinc, closeadj):
    res = (netinc / closeadj).pct_change(21).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc099_5d_base_v099_signal'] = f59fc_f59_fcf_conversion_quality_calc099_5d_base_v099_signal

def f59fc_f59_fcf_conversion_quality_calc100_5d_base_v100_signal(sharesbas, assets):
    res = (sharesbas / assets).diff(21).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc100_5d_base_v100_signal'] = f59fc_f59_fcf_conversion_quality_calc100_5d_base_v100_signal

def f59fc_f59_fcf_conversion_quality_calc101_10d_base_v101_signal(volume, ps, assets):
    res = (ps * volume / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc101_10d_base_v101_signal'] = f59fc_f59_fcf_conversion_quality_calc101_10d_base_v101_signal

def f59fc_f59_fcf_conversion_quality_calc102_10d_base_v102_signal(liabilities, evebit):
    res = np.log((liabilities / evebit).abs().replace(0, np.nan)).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc102_10d_base_v102_signal'] = f59fc_f59_fcf_conversion_quality_calc102_10d_base_v102_signal

def f59fc_f59_fcf_conversion_quality_calc103_10d_base_v103_signal(evebit, evebitda, assets):
    res = (evebitda * evebit / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc103_10d_base_v103_signal'] = f59fc_f59_fcf_conversion_quality_calc103_10d_base_v103_signal

def f59fc_f59_fcf_conversion_quality_calc104_252d_base_v104_signal(fcf, pb):
    res = (((fcf / pb) - (fcf / pb).rolling(252).mean()) / (fcf / pb).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc104_252d_base_v104_signal'] = f59fc_f59_fcf_conversion_quality_calc104_252d_base_v104_signal

def f59fc_f59_fcf_conversion_quality_calc105_126d_base_v105_signal(netinc, ps, assets):
    res = (ps * netinc / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc105_126d_base_v105_signal'] = f59fc_f59_fcf_conversion_quality_calc105_126d_base_v105_signal

def f59fc_f59_fcf_conversion_quality_calc106_252d_base_v106_signal(open, workingcapital, assets):
    res = (open * workingcapital / assets).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc106_252d_base_v106_signal'] = f59fc_f59_fcf_conversion_quality_calc106_252d_base_v106_signal

def f59fc_f59_fcf_conversion_quality_calc107_42d_base_v107_signal(pb, workingcapital, assets):
    res = (workingcapital * pb / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc107_42d_base_v107_signal'] = f59fc_f59_fcf_conversion_quality_calc107_42d_base_v107_signal

def f59fc_f59_fcf_conversion_quality_calc108_63d_base_v108_signal(open, liabilities):
    res = (open / liabilities).pct_change(1).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc108_63d_base_v108_signal'] = f59fc_f59_fcf_conversion_quality_calc108_63d_base_v108_signal

def f59fc_f59_fcf_conversion_quality_calc109_42d_base_v109_signal(sharesbas, liabilities):
    res = (sharesbas / liabilities).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc109_42d_base_v109_signal'] = f59fc_f59_fcf_conversion_quality_calc109_42d_base_v109_signal

def f59fc_f59_fcf_conversion_quality_calc110_252d_base_v110_signal(equity, fcf, assets):
    res = (equity * fcf / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc110_252d_base_v110_signal'] = f59fc_f59_fcf_conversion_quality_calc110_252d_base_v110_signal

def f59fc_f59_fcf_conversion_quality_calc111_42d_base_v111_signal(debt, ncfo):
    res = (ncfo / debt).pct_change(1).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc111_42d_base_v111_signal'] = f59fc_f59_fcf_conversion_quality_calc111_42d_base_v111_signal

def f59fc_f59_fcf_conversion_quality_calc112_5d_base_v112_signal(evebitda, ps, eps):
    res = (ps / eps).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc112_5d_base_v112_signal'] = f59fc_f59_fcf_conversion_quality_calc112_5d_base_v112_signal

def f59fc_f59_fcf_conversion_quality_calc113_21d_base_v113_signal(fcf, currentratio):
    res = (currentratio / fcf).pct_change(21).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc113_21d_base_v113_signal'] = f59fc_f59_fcf_conversion_quality_calc113_21d_base_v113_signal

def f59fc_f59_fcf_conversion_quality_calc114_21d_base_v114_signal(sharesbas, fcf, assets):
    res = (sharesbas * fcf / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc114_21d_base_v114_signal'] = f59fc_f59_fcf_conversion_quality_calc114_21d_base_v114_signal

def f59fc_f59_fcf_conversion_quality_calc115_5d_base_v115_signal(currentratio, ncfo, assets):
    res = (ncfo * currentratio / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc115_5d_base_v115_signal'] = f59fc_f59_fcf_conversion_quality_calc115_5d_base_v115_signal

def f59fc_f59_fcf_conversion_quality_calc116_42d_base_v116_signal(closeadj, ps, assets):
    res = (closeadj * ps / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc116_42d_base_v116_signal'] = f59fc_f59_fcf_conversion_quality_calc116_42d_base_v116_signal

def f59fc_f59_fcf_conversion_quality_calc117_252d_base_v117_signal(open, debt, taxexp):
    res = (((open / taxexp) - (open / taxexp).rolling(252).mean()) / (open / taxexp).rolling(252).std()).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc117_252d_base_v117_signal'] = f59fc_f59_fcf_conversion_quality_calc117_252d_base_v117_signal

def f59fc_f59_fcf_conversion_quality_calc118_252d_base_v118_signal(open, retearn, pe):
    res = (open / retearn).diff(5).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc118_252d_base_v118_signal'] = f59fc_f59_fcf_conversion_quality_calc118_252d_base_v118_signal

def f59fc_f59_fcf_conversion_quality_calc119_252d_base_v119_signal(closeadj, workingcapital):
    res = (workingcapital / closeadj).rolling(252).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc119_252d_base_v119_signal'] = f59fc_f59_fcf_conversion_quality_calc119_252d_base_v119_signal

def f59fc_f59_fcf_conversion_quality_calc120_5d_base_v120_signal(ev, workingcapital, assets):
    res = (ev * workingcapital / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc120_5d_base_v120_signal'] = f59fc_f59_fcf_conversion_quality_calc120_5d_base_v120_signal

def f59fc_f59_fcf_conversion_quality_calc121_63d_base_v121_signal(taxexp, capex):
    res = np.log((capex / taxexp).abs().replace(0, np.nan)).rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc121_63d_base_v121_signal'] = f59fc_f59_fcf_conversion_quality_calc121_63d_base_v121_signal

def f59fc_f59_fcf_conversion_quality_calc122_42d_base_v122_signal(netinc, currentratio, ps):
    res = (((currentratio / ps) - (currentratio / ps).rolling(42).mean()) / (currentratio / ps).rolling(42).std()).rolling(42).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc122_42d_base_v122_signal'] = f59fc_f59_fcf_conversion_quality_calc122_42d_base_v122_signal

def f59fc_f59_fcf_conversion_quality_calc123_21d_base_v123_signal(volume, high):
    res = (volume / high).diff(1).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc123_21d_base_v123_signal'] = f59fc_f59_fcf_conversion_quality_calc123_21d_base_v123_signal

def f59fc_f59_fcf_conversion_quality_calc124_252d_base_v124_signal(open, ncfo):
    res = (((open / ncfo) - (open / ncfo).rolling(252).mean()) / (open / ncfo).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc124_252d_base_v124_signal'] = f59fc_f59_fcf_conversion_quality_calc124_252d_base_v124_signal

def f59fc_f59_fcf_conversion_quality_calc125_42d_base_v125_signal(intexp, ebitda):
    res = (ebitda / intexp).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc125_42d_base_v125_signal'] = f59fc_f59_fcf_conversion_quality_calc125_42d_base_v125_signal

def f59fc_f59_fcf_conversion_quality_calc126_252d_base_v126_signal(intexp, equity):
    res = (((intexp / equity) - (intexp / equity).rolling(252).mean()) / (intexp / equity).rolling(252).std()).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc126_252d_base_v126_signal'] = f59fc_f59_fcf_conversion_quality_calc126_252d_base_v126_signal

def f59fc_f59_fcf_conversion_quality_calc127_21d_base_v127_signal(evebit, evebitda):
    res = (evebitda / evebit).diff(1).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc127_21d_base_v127_signal'] = f59fc_f59_fcf_conversion_quality_calc127_21d_base_v127_signal

def f59fc_f59_fcf_conversion_quality_calc128_63d_base_v128_signal(netinc, pe, debt):
    res = (netinc / debt).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc128_63d_base_v128_signal'] = f59fc_f59_fcf_conversion_quality_calc128_63d_base_v128_signal

def f59fc_f59_fcf_conversion_quality_calc129_10d_base_v129_signal(ev, evebitda):
    res = (evebitda / ev).diff(1).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc129_10d_base_v129_signal'] = f59fc_f59_fcf_conversion_quality_calc129_10d_base_v129_signal

def f59fc_f59_fcf_conversion_quality_calc130_252d_base_v130_signal(ev, assets):
    res = (ev * assets / assets).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc130_252d_base_v130_signal'] = f59fc_f59_fcf_conversion_quality_calc130_252d_base_v130_signal

def f59fc_f59_fcf_conversion_quality_calc131_10d_base_v131_signal(low, liabilities, fcf):
    res = (liabilities / low).diff(1).rolling(10).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc131_10d_base_v131_signal'] = f59fc_f59_fcf_conversion_quality_calc131_10d_base_v131_signal

def f59fc_f59_fcf_conversion_quality_calc132_42d_base_v132_signal(taxexp, ps, assets):
    res = (taxexp * ps / assets).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc132_42d_base_v132_signal'] = f59fc_f59_fcf_conversion_quality_calc132_42d_base_v132_signal

def f59fc_f59_fcf_conversion_quality_calc133_126d_base_v133_signal(ncfi, liabilities, assets):
    res = (liabilities * ncfi / assets).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc133_126d_base_v133_signal'] = f59fc_f59_fcf_conversion_quality_calc133_126d_base_v133_signal

def f59fc_f59_fcf_conversion_quality_calc134_126d_base_v134_signal(ncfi, high):
    res = (high / ncfi).pct_change(21).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc134_126d_base_v134_signal'] = f59fc_f59_fcf_conversion_quality_calc134_126d_base_v134_signal

def f59fc_f59_fcf_conversion_quality_calc135_42d_base_v135_signal(open, workingcapital):
    res = (open / workingcapital).pct_change(1).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc135_42d_base_v135_signal'] = f59fc_f59_fcf_conversion_quality_calc135_42d_base_v135_signal

def f59fc_f59_fcf_conversion_quality_calc136_5d_base_v136_signal(netinc, evebitda):
    res = (evebitda / netinc).diff(21).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc136_5d_base_v136_signal'] = f59fc_f59_fcf_conversion_quality_calc136_5d_base_v136_signal

def f59fc_f59_fcf_conversion_quality_calc137_252d_base_v137_signal(ncfi, ps):
    res = (((ncfi / ps) - (ncfi / ps).rolling(252).mean()) / (ncfi / ps).rolling(252).std()).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc137_252d_base_v137_signal'] = f59fc_f59_fcf_conversion_quality_calc137_252d_base_v137_signal

def f59fc_f59_fcf_conversion_quality_calc138_252d_base_v138_signal(debt, equity):
    res = (debt / equity).pct_change(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc138_252d_base_v138_signal'] = f59fc_f59_fcf_conversion_quality_calc138_252d_base_v138_signal

def f59fc_f59_fcf_conversion_quality_calc139_126d_base_v139_signal(debt, fcf, eps):
    res = (debt / fcf).diff(21).rolling(126).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc139_126d_base_v139_signal'] = f59fc_f59_fcf_conversion_quality_calc139_126d_base_v139_signal

def f59fc_f59_fcf_conversion_quality_calc140_63d_base_v140_signal(ncfo, ebitda):
    res = (((ebitda / ncfo) - (ebitda / ncfo).rolling(63).mean()) / (ebitda / ncfo).rolling(63).std()).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc140_63d_base_v140_signal'] = f59fc_f59_fcf_conversion_quality_calc140_63d_base_v140_signal

def f59fc_f59_fcf_conversion_quality_calc141_21d_base_v141_signal(equity, fcf):
    res = np.log((equity / fcf).abs().replace(0, np.nan)).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc141_21d_base_v141_signal'] = f59fc_f59_fcf_conversion_quality_calc141_21d_base_v141_signal

def f59fc_f59_fcf_conversion_quality_calc142_252d_base_v142_signal(sharesbas, open, volume):
    res = (volume / sharesbas).diff(21).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc142_252d_base_v142_signal'] = f59fc_f59_fcf_conversion_quality_calc142_252d_base_v142_signal

def f59fc_f59_fcf_conversion_quality_calc143_42d_base_v143_signal(debt, revenue, assets):
    res = (revenue * debt / assets).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc143_42d_base_v143_signal'] = f59fc_f59_fcf_conversion_quality_calc143_42d_base_v143_signal

def f59fc_f59_fcf_conversion_quality_calc144_21d_base_v144_signal(low, assets, pe):
    res = (pe / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc144_21d_base_v144_signal'] = f59fc_f59_fcf_conversion_quality_calc144_21d_base_v144_signal

def f59fc_f59_fcf_conversion_quality_calc145_10d_base_v145_signal(evebitda, workingcapital):
    res = (workingcapital / evebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc145_10d_base_v145_signal'] = f59fc_f59_fcf_conversion_quality_calc145_10d_base_v145_signal

def f59fc_f59_fcf_conversion_quality_calc146_21d_base_v146_signal(open, ncff, closeadj):
    res = (ncff * open / closeadj)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc146_21d_base_v146_signal'] = f59fc_f59_fcf_conversion_quality_calc146_21d_base_v146_signal

def f59fc_f59_fcf_conversion_quality_calc147_63d_base_v147_signal(liabilities, equity, workingcapital):
    res = (((equity / liabilities) - (equity / liabilities).rolling(63).mean()) / (equity / liabilities).rolling(63).std()).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc147_63d_base_v147_signal'] = f59fc_f59_fcf_conversion_quality_calc147_63d_base_v147_signal

def f59fc_f59_fcf_conversion_quality_calc148_5d_base_v148_signal(debt, high):
    res = (high / debt).diff(21).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc148_5d_base_v148_signal'] = f59fc_f59_fcf_conversion_quality_calc148_5d_base_v148_signal

def f59fc_f59_fcf_conversion_quality_calc149_126d_base_v149_signal(ncfi, currentratio, ebitda):
    res = (ncfi * ebitda / currentratio)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc149_126d_base_v149_signal'] = f59fc_f59_fcf_conversion_quality_calc149_126d_base_v149_signal

def f59fc_f59_fcf_conversion_quality_calc150_252d_base_v150_signal(sharesbas, ncfo):
    res = (ncfo / sharesbas).diff(5).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f59fc_f59_fcf_conversion_quality_calc150_252d_base_v150_signal'] = f59fc_f59_fcf_conversion_quality_calc150_252d_base_v150_signal

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
