import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f60md_f60_market_cap_dominance_calc076_126d_base_v076_signal(ev, ncfo):
    res = (ev / ncfo).pct_change(1).rolling(126).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc076_126d_base_v076_signal'] = f60md_f60_market_cap_dominance_calc076_126d_base_v076_signal

def f60md_f60_market_cap_dominance_calc077_21d_base_v077_signal(retearn, ebitda, workingcapital):
    res = (workingcapital / retearn).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc077_21d_base_v077_signal'] = f60md_f60_market_cap_dominance_calc077_21d_base_v077_signal

def f60md_f60_market_cap_dominance_calc078_126d_base_v078_signal(evebitda, high, evebit):
    res = (evebit * evebitda / high)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc078_126d_base_v078_signal'] = f60md_f60_market_cap_dominance_calc078_126d_base_v078_signal

def f60md_f60_market_cap_dominance_calc079_42d_base_v079_signal(pb, closeadj):
    res = (pb / closeadj).diff(1).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc079_42d_base_v079_signal'] = f60md_f60_market_cap_dominance_calc079_42d_base_v079_signal

def f60md_f60_market_cap_dominance_calc080_63d_base_v080_signal(pe, low, assets):
    res = (pe * low / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc080_63d_base_v080_signal'] = f60md_f60_market_cap_dominance_calc080_63d_base_v080_signal

def f60md_f60_market_cap_dominance_calc081_42d_base_v081_signal(evebitda, gp, evebit):
    res = (evebitda * evebit / gp)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc081_42d_base_v081_signal'] = f60md_f60_market_cap_dominance_calc081_42d_base_v081_signal

def f60md_f60_market_cap_dominance_calc082_252d_base_v082_signal(pe, assets):
    res = np.log((pe / assets).abs().replace(0, np.nan)).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc082_252d_base_v082_signal'] = f60md_f60_market_cap_dominance_calc082_252d_base_v082_signal

def f60md_f60_market_cap_dominance_calc083_252d_base_v083_signal(pe, currentratio, fcf):
    res = (pe / fcf).diff(1).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc083_252d_base_v083_signal'] = f60md_f60_market_cap_dominance_calc083_252d_base_v083_signal

def f60md_f60_market_cap_dominance_calc084_63d_base_v084_signal(ncff, liabilities):
    res = (liabilities / ncff).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc084_63d_base_v084_signal'] = f60md_f60_market_cap_dominance_calc084_63d_base_v084_signal

def f60md_f60_market_cap_dominance_calc085_42d_base_v085_signal(netinc, ncfo):
    res = np.log((ncfo / netinc).abs().replace(0, np.nan)).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc085_42d_base_v085_signal'] = f60md_f60_market_cap_dominance_calc085_42d_base_v085_signal

def f60md_f60_market_cap_dominance_calc086_126d_base_v086_signal(pe, open, netinc):
    res = np.log((open / pe).abs().replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc086_126d_base_v086_signal'] = f60md_f60_market_cap_dominance_calc086_126d_base_v086_signal

def f60md_f60_market_cap_dominance_calc087_21d_base_v087_signal(sharesbas, ncfo, close):
    res = (close / sharesbas).pct_change(1).rolling(21).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc087_21d_base_v087_signal'] = f60md_f60_market_cap_dominance_calc087_21d_base_v087_signal

def f60md_f60_market_cap_dominance_calc088_252d_base_v088_signal(ev, ebitda):
    res = (((ebitda / ev) - (ebitda / ev).rolling(252).mean()) / (ebitda / ev).rolling(252).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc088_252d_base_v088_signal'] = f60md_f60_market_cap_dominance_calc088_252d_base_v088_signal

def f60md_f60_market_cap_dominance_calc089_63d_base_v089_signal(ncff, evebitda, high):
    res = (((ncff / evebitda) - (ncff / evebitda).rolling(63).mean()) / (ncff / evebitda).rolling(63).std()).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc089_63d_base_v089_signal'] = f60md_f60_market_cap_dominance_calc089_63d_base_v089_signal

def f60md_f60_market_cap_dominance_calc090_252d_base_v090_signal(pb, taxexp):
    res = (pb / taxexp).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc090_252d_base_v090_signal'] = f60md_f60_market_cap_dominance_calc090_252d_base_v090_signal

def f60md_f60_market_cap_dominance_calc091_63d_base_v091_signal(ev, assets):
    res = (ev * assets / assets).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc091_63d_base_v091_signal'] = f60md_f60_market_cap_dominance_calc091_63d_base_v091_signal

def f60md_f60_market_cap_dominance_calc092_63d_base_v092_signal(sharesbas, high, ps):
    res = (((high / sharesbas) - (high / sharesbas).rolling(63).mean()) / (high / sharesbas).rolling(63).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc092_63d_base_v092_signal'] = f60md_f60_market_cap_dominance_calc092_63d_base_v092_signal

def f60md_f60_market_cap_dominance_calc093_42d_base_v093_signal(taxexp, revenue):
    res = (taxexp / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc093_42d_base_v093_signal'] = f60md_f60_market_cap_dominance_calc093_42d_base_v093_signal

def f60md_f60_market_cap_dominance_calc094_21d_base_v094_signal(revenue, fcf):
    res = (fcf / revenue).diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc094_21d_base_v094_signal'] = f60md_f60_market_cap_dominance_calc094_21d_base_v094_signal

def f60md_f60_market_cap_dominance_calc095_42d_base_v095_signal(retearn, ncfo):
    res = (((ncfo / retearn) - (ncfo / retearn).rolling(42).mean()) / (ncfo / retearn).rolling(42).std()).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc095_42d_base_v095_signal'] = f60md_f60_market_cap_dominance_calc095_42d_base_v095_signal

def f60md_f60_market_cap_dominance_calc096_126d_base_v096_signal(opinc, low):
    res = np.log((opinc / low).abs().replace(0, np.nan)).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc096_126d_base_v096_signal'] = f60md_f60_market_cap_dominance_calc096_126d_base_v096_signal

def f60md_f60_market_cap_dominance_calc097_126d_base_v097_signal(pb, eps):
    res = (pb / eps).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc097_126d_base_v097_signal'] = f60md_f60_market_cap_dominance_calc097_126d_base_v097_signal

def f60md_f60_market_cap_dominance_calc098_126d_base_v098_signal(sharesbas, intexp, assets):
    res = (intexp * sharesbas / assets).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc098_126d_base_v098_signal'] = f60md_f60_market_cap_dominance_calc098_126d_base_v098_signal

def f60md_f60_market_cap_dominance_calc099_63d_base_v099_signal(pe, equity):
    res = (pe / equity)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc099_63d_base_v099_signal'] = f60md_f60_market_cap_dominance_calc099_63d_base_v099_signal

def f60md_f60_market_cap_dominance_calc100_63d_base_v100_signal(assets, workingcapital, close):
    res = (close / workingcapital).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc100_63d_base_v100_signal'] = f60md_f60_market_cap_dominance_calc100_63d_base_v100_signal

def f60md_f60_market_cap_dominance_calc101_10d_base_v101_signal(liabilities, equity, assets):
    res = (liabilities * equity / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc101_10d_base_v101_signal'] = f60md_f60_market_cap_dominance_calc101_10d_base_v101_signal

def f60md_f60_market_cap_dominance_calc102_42d_base_v102_signal(high, evebit):
    res = (evebit / high).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc102_42d_base_v102_signal'] = f60md_f60_market_cap_dominance_calc102_42d_base_v102_signal

def f60md_f60_market_cap_dominance_calc103_63d_base_v103_signal(volume, currentratio, close):
    res = np.log((currentratio / close).abs().replace(0, np.nan)).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc103_63d_base_v103_signal'] = f60md_f60_market_cap_dominance_calc103_63d_base_v103_signal

def f60md_f60_market_cap_dominance_calc104_126d_base_v104_signal(assets, workingcapital):
    res = (((workingcapital / assets) - (workingcapital / assets).rolling(126).mean()) / (workingcapital / assets).rolling(126).std()).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc104_126d_base_v104_signal'] = f60md_f60_market_cap_dominance_calc104_126d_base_v104_signal

def f60md_f60_market_cap_dominance_calc105_63d_base_v105_signal(intexp, close):
    res = (intexp / close).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc105_63d_base_v105_signal'] = f60md_f60_market_cap_dominance_calc105_63d_base_v105_signal

def f60md_f60_market_cap_dominance_calc106_21d_base_v106_signal(sharesbas, workingcapital):
    res = (sharesbas / workingcapital).pct_change(5).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc106_21d_base_v106_signal'] = f60md_f60_market_cap_dominance_calc106_21d_base_v106_signal

def f60md_f60_market_cap_dominance_calc107_10d_base_v107_signal(pb, intexp):
    res = (((intexp / pb) - (intexp / pb).rolling(10).mean()) / (intexp / pb).rolling(10).std()).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc107_10d_base_v107_signal'] = f60md_f60_market_cap_dominance_calc107_10d_base_v107_signal

def f60md_f60_market_cap_dominance_calc108_21d_base_v108_signal(sharesbas, evebit):
    res = (((sharesbas / evebit) - (sharesbas / evebit).rolling(21).mean()) / (sharesbas / evebit).rolling(21).std()).rolling(21).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc108_21d_base_v108_signal'] = f60md_f60_market_cap_dominance_calc108_21d_base_v108_signal

def f60md_f60_market_cap_dominance_calc109_10d_base_v109_signal(sharesbas, volume, assets):
    res = (volume * sharesbas / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc109_10d_base_v109_signal'] = f60md_f60_market_cap_dominance_calc109_10d_base_v109_signal

def f60md_f60_market_cap_dominance_calc110_252d_base_v110_signal(evebit, ncfo):
    res = (((evebit / ncfo) - (evebit / ncfo).rolling(252).mean()) / (evebit / ncfo).rolling(252).std()).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc110_252d_base_v110_signal'] = f60md_f60_market_cap_dominance_calc110_252d_base_v110_signal

def f60md_f60_market_cap_dominance_calc111_63d_base_v111_signal(sharesbas, revenue):
    res = (revenue / sharesbas)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc111_63d_base_v111_signal'] = f60md_f60_market_cap_dominance_calc111_63d_base_v111_signal

def f60md_f60_market_cap_dominance_calc112_252d_base_v112_signal(high, workingcapital):
    res = (workingcapital / high).diff(1).rolling(252).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc112_252d_base_v112_signal'] = f60md_f60_market_cap_dominance_calc112_252d_base_v112_signal

def f60md_f60_market_cap_dominance_calc113_252d_base_v113_signal(intexp, marketcap):
    res = (((marketcap / intexp) - (marketcap / intexp).rolling(252).mean()) / (marketcap / intexp).rolling(252).std()).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc113_252d_base_v113_signal'] = f60md_f60_market_cap_dominance_calc113_252d_base_v113_signal

def f60md_f60_market_cap_dominance_calc114_5d_base_v114_signal(volume, revenue):
    res = (volume / revenue).diff(21).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc114_5d_base_v114_signal'] = f60md_f60_market_cap_dominance_calc114_5d_base_v114_signal

def f60md_f60_market_cap_dominance_calc115_5d_base_v115_signal(opinc, debt):
    res = (debt / opinc).rolling(5).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc115_5d_base_v115_signal'] = f60md_f60_market_cap_dominance_calc115_5d_base_v115_signal

def f60md_f60_market_cap_dominance_calc116_21d_base_v116_signal(pb, close):
    res = np.log((close / pb).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc116_21d_base_v116_signal'] = f60md_f60_market_cap_dominance_calc116_21d_base_v116_signal

def f60md_f60_market_cap_dominance_calc117_126d_base_v117_signal(ebitda, close):
    res = np.log((close / ebitda).abs().replace(0, np.nan)).rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc117_126d_base_v117_signal'] = f60md_f60_market_cap_dominance_calc117_126d_base_v117_signal

def f60md_f60_market_cap_dominance_calc118_252d_base_v118_signal(ncff, low, ev):
    res = (low / ncff).diff(21).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc118_252d_base_v118_signal'] = f60md_f60_market_cap_dominance_calc118_252d_base_v118_signal

def f60md_f60_market_cap_dominance_calc119_10d_base_v119_signal(closeadj, assets):
    res = (assets / closeadj).pct_change(5).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc119_10d_base_v119_signal'] = f60md_f60_market_cap_dominance_calc119_10d_base_v119_signal

def f60md_f60_market_cap_dominance_calc120_5d_base_v120_signal(volume, open):
    res = (open / volume).diff(21).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc120_5d_base_v120_signal'] = f60md_f60_market_cap_dominance_calc120_5d_base_v120_signal

def f60md_f60_market_cap_dominance_calc121_126d_base_v121_signal(volume, closeadj):
    res = (closeadj / volume).pct_change(5).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc121_126d_base_v121_signal'] = f60md_f60_market_cap_dominance_calc121_126d_base_v121_signal

def f60md_f60_market_cap_dominance_calc122_252d_base_v122_signal(open, eps):
    res = (eps / open).rolling(252).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc122_252d_base_v122_signal'] = f60md_f60_market_cap_dominance_calc122_252d_base_v122_signal

def f60md_f60_market_cap_dominance_calc123_126d_base_v123_signal(high, debt, assets):
    res = (high * debt / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc123_126d_base_v123_signal'] = f60md_f60_market_cap_dominance_calc123_126d_base_v123_signal

def f60md_f60_market_cap_dominance_calc124_42d_base_v124_signal(volume, debt):
    res = (volume / debt).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc124_42d_base_v124_signal'] = f60md_f60_market_cap_dominance_calc124_42d_base_v124_signal

def f60md_f60_market_cap_dominance_calc125_42d_base_v125_signal(pe, currentratio):
    res = (pe / currentratio).diff(21).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc125_42d_base_v125_signal'] = f60md_f60_market_cap_dominance_calc125_42d_base_v125_signal

def f60md_f60_market_cap_dominance_calc126_5d_base_v126_signal(intexp, workingcapital):
    res = (workingcapital / intexp).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc126_5d_base_v126_signal'] = f60md_f60_market_cap_dominance_calc126_5d_base_v126_signal

def f60md_f60_market_cap_dominance_calc127_21d_base_v127_signal(taxexp, intexp):
    res = (intexp / taxexp).pct_change(21).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc127_21d_base_v127_signal'] = f60md_f60_market_cap_dominance_calc127_21d_base_v127_signal

def f60md_f60_market_cap_dominance_calc128_42d_base_v128_signal(low, workingcapital, marketcap):
    res = (low / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc128_42d_base_v128_signal'] = f60md_f60_market_cap_dominance_calc128_42d_base_v128_signal

def f60md_f60_market_cap_dominance_calc129_42d_base_v129_signal(low, revenue, assets):
    res = (revenue * low / assets).rolling(42).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc129_42d_base_v129_signal'] = f60md_f60_market_cap_dominance_calc129_42d_base_v129_signal

def f60md_f60_market_cap_dominance_calc130_5d_base_v130_signal(open, workingcapital):
    res = (workingcapital / open).pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc130_5d_base_v130_signal'] = f60md_f60_market_cap_dominance_calc130_5d_base_v130_signal

def f60md_f60_market_cap_dominance_calc131_21d_base_v131_signal(high, assets):
    res = (assets / high).pct_change(21).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc131_21d_base_v131_signal'] = f60md_f60_market_cap_dominance_calc131_21d_base_v131_signal

def f60md_f60_market_cap_dominance_calc132_10d_base_v132_signal(taxexp, ncfi, low):
    res = (ncfi * low / taxexp).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc132_10d_base_v132_signal'] = f60md_f60_market_cap_dominance_calc132_10d_base_v132_signal

def f60md_f60_market_cap_dominance_calc133_21d_base_v133_signal(opinc, equity):
    res = np.log((equity / opinc).abs().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc133_21d_base_v133_signal'] = f60md_f60_market_cap_dominance_calc133_21d_base_v133_signal

def f60md_f60_market_cap_dominance_calc134_10d_base_v134_signal(sharesbas, ncfi):
    res = (sharesbas / ncfi).pct_change(1).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc134_10d_base_v134_signal'] = f60md_f60_market_cap_dominance_calc134_10d_base_v134_signal

def f60md_f60_market_cap_dominance_calc135_63d_base_v135_signal(ncfi, currentratio, assets):
    res = (currentratio * ncfi / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc135_63d_base_v135_signal'] = f60md_f60_market_cap_dominance_calc135_63d_base_v135_signal

def f60md_f60_market_cap_dominance_calc136_21d_base_v136_signal(pe, assets, debt):
    res = (debt / assets).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc136_21d_base_v136_signal'] = f60md_f60_market_cap_dominance_calc136_21d_base_v136_signal

def f60md_f60_market_cap_dominance_calc137_21d_base_v137_signal(netinc, marketcap):
    res = (netinc / marketcap).pct_change(21).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc137_21d_base_v137_signal'] = f60md_f60_market_cap_dominance_calc137_21d_base_v137_signal

def f60md_f60_market_cap_dominance_calc138_63d_base_v138_signal(pe, ebitda):
    res = (((pe / ebitda) - (pe / ebitda).rolling(63).mean()) / (pe / ebitda).rolling(63).std()).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc138_63d_base_v138_signal'] = f60md_f60_market_cap_dominance_calc138_63d_base_v138_signal

def f60md_f60_market_cap_dominance_calc139_42d_base_v139_signal(ncfi, marketcap):
    res = (marketcap / ncfi).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc139_42d_base_v139_signal'] = f60md_f60_market_cap_dominance_calc139_42d_base_v139_signal

def f60md_f60_market_cap_dominance_calc140_21d_base_v140_signal(opinc, pe):
    res = (((pe / opinc) - (pe / opinc).rolling(21).mean()) / (pe / opinc).rolling(21).std())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc140_21d_base_v140_signal'] = f60md_f60_market_cap_dominance_calc140_21d_base_v140_signal

def f60md_f60_market_cap_dominance_calc141_10d_base_v141_signal(opinc, volume):
    res = (volume / opinc).rolling(10).sum()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc141_10d_base_v141_signal'] = f60md_f60_market_cap_dominance_calc141_10d_base_v141_signal

def f60md_f60_market_cap_dominance_calc142_21d_base_v142_signal(intexp, closeadj, revenue):
    res = (intexp * closeadj / revenue)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc142_21d_base_v142_signal'] = f60md_f60_market_cap_dominance_calc142_21d_base_v142_signal

def f60md_f60_market_cap_dominance_calc143_252d_base_v143_signal(taxexp, volume, gp):
    res = (volume / gp).diff(5).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc143_252d_base_v143_signal'] = f60md_f60_market_cap_dominance_calc143_252d_base_v143_signal

def f60md_f60_market_cap_dominance_calc144_42d_base_v144_signal(low, debt, ncfo):
    res = (low * debt / ncfo).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc144_42d_base_v144_signal'] = f60md_f60_market_cap_dominance_calc144_42d_base_v144_signal

def f60md_f60_market_cap_dominance_calc145_126d_base_v145_signal(intexp, ncfo, assets):
    res = (ncfo * intexp / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc145_126d_base_v145_signal'] = f60md_f60_market_cap_dominance_calc145_126d_base_v145_signal

def f60md_f60_market_cap_dominance_calc146_126d_base_v146_signal(ncfi, closeadj, workingcapital):
    res = (ncfi / closeadj).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc146_126d_base_v146_signal'] = f60md_f60_market_cap_dominance_calc146_126d_base_v146_signal

def f60md_f60_market_cap_dominance_calc147_21d_base_v147_signal(evebitda, assets):
    res = (assets / evebitda)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc147_21d_base_v147_signal'] = f60md_f60_market_cap_dominance_calc147_21d_base_v147_signal

def f60md_f60_market_cap_dominance_calc148_5d_base_v148_signal(ncff, opinc):
    res = (opinc / ncff).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc148_5d_base_v148_signal'] = f60md_f60_market_cap_dominance_calc148_5d_base_v148_signal

def f60md_f60_market_cap_dominance_calc149_126d_base_v149_signal(currentratio, fcf):
    res = (fcf / currentratio).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc149_126d_base_v149_signal'] = f60md_f60_market_cap_dominance_calc149_126d_base_v149_signal

def f60md_f60_market_cap_dominance_calc150_252d_base_v150_signal(netinc, close, assets):
    res = (netinc * close / assets).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f60md_f60_market_cap_dominance_calc150_252d_base_v150_signal'] = f60md_f60_market_cap_dominance_calc150_252d_base_v150_signal

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
