import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f62ds_f62_dividend_sustainability_calc076_504d_base_v076_signal(ebitda, evebitda, intexp):
    res = ((intexp + evebitda) - ebitda).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc076_504d_base_v076_signal'] = f62ds_f62_dividend_sustainability_calc076_504d_base_v076_signal

def f62ds_f62_dividend_sustainability_calc077_504d_base_v077_signal(fcf, intexp, pe):
    res = ((fcf - pe) - intexp).diff(21).rolling(504).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc077_504d_base_v077_signal'] = f62ds_f62_dividend_sustainability_calc077_504d_base_v077_signal

def f62ds_f62_dividend_sustainability_calc078_10d_base_v078_signal(gp, revenue):
    res = (gp + revenue).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc078_10d_base_v078_signal'] = f62ds_f62_dividend_sustainability_calc078_10d_base_v078_signal

def f62ds_f62_dividend_sustainability_calc079_42d_base_v079_signal(assets, liabilities):
    res = (liabilities * assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc079_42d_base_v079_signal'] = f62ds_f62_dividend_sustainability_calc079_42d_base_v079_signal

def f62ds_f62_dividend_sustainability_calc080_5d_base_v080_signal(gp):
    res = gp.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc080_5d_base_v080_signal'] = f62ds_f62_dividend_sustainability_calc080_5d_base_v080_signal

def f62ds_f62_dividend_sustainability_calc081_5d_base_v081_signal(assets, liabilities):
    res = (liabilities * assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc081_5d_base_v081_signal'] = f62ds_f62_dividend_sustainability_calc081_5d_base_v081_signal

def f62ds_f62_dividend_sustainability_calc082_42d_base_v082_signal(evebit, ps):
    res = (ps * evebit).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc082_42d_base_v082_signal'] = f62ds_f62_dividend_sustainability_calc082_42d_base_v082_signal

def f62ds_f62_dividend_sustainability_calc083_10d_base_v083_signal(currentratio, ps):
    res = (currentratio * ps).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc083_10d_base_v083_signal'] = f62ds_f62_dividend_sustainability_calc083_10d_base_v083_signal

def f62ds_f62_dividend_sustainability_calc084_63d_base_v084_signal(ncfo, netinc):
    res = (ncfo - netinc).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc084_63d_base_v084_signal'] = f62ds_f62_dividend_sustainability_calc084_63d_base_v084_signal

def f62ds_f62_dividend_sustainability_calc085_42d_base_v085_signal(assets, workingcapital):
    res = (workingcapital + assets).pct_change(5).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc085_42d_base_v085_signal'] = f62ds_f62_dividend_sustainability_calc085_42d_base_v085_signal

def f62ds_f62_dividend_sustainability_calc086_63d_base_v086_signal(debt, ev, open):
    res = ((open - debt) + ev).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc086_63d_base_v086_signal'] = f62ds_f62_dividend_sustainability_calc086_63d_base_v086_signal

def f62ds_f62_dividend_sustainability_calc087_10d_base_v087_signal(liabilities):
    res = liabilities.pct_change(21).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc087_10d_base_v087_signal'] = f62ds_f62_dividend_sustainability_calc087_10d_base_v087_signal

def f62ds_f62_dividend_sustainability_calc088_42d_base_v088_signal(intexp, liabilities, volume):
    res = ((intexp / liabilities) - volume).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc088_42d_base_v088_signal'] = f62ds_f62_dividend_sustainability_calc088_42d_base_v088_signal

def f62ds_f62_dividend_sustainability_calc089_5d_base_v089_signal(open):
    res = open.pct_change(1).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc089_5d_base_v089_signal'] = f62ds_f62_dividend_sustainability_calc089_5d_base_v089_signal

def f62ds_f62_dividend_sustainability_calc090_252d_base_v090_signal(ev):
    res = ev.rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc090_252d_base_v090_signal'] = f62ds_f62_dividend_sustainability_calc090_252d_base_v090_signal

def f62ds_f62_dividend_sustainability_calc091_504d_base_v091_signal(closeadj, open):
    res = (open / closeadj).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc091_504d_base_v091_signal'] = f62ds_f62_dividend_sustainability_calc091_504d_base_v091_signal

def f62ds_f62_dividend_sustainability_calc092_5d_base_v092_signal(ev, ncfi):
    res = (ev + ncfi).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc092_5d_base_v092_signal'] = f62ds_f62_dividend_sustainability_calc092_5d_base_v092_signal

def f62ds_f62_dividend_sustainability_calc093_504d_base_v093_signal(marketcap):
    res = marketcap.pct_change(21).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc093_504d_base_v093_signal'] = f62ds_f62_dividend_sustainability_calc093_504d_base_v093_signal

def f62ds_f62_dividend_sustainability_calc094_10d_base_v094_signal(debt, evebit):
    res = (debt - evebit).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc094_10d_base_v094_signal'] = f62ds_f62_dividend_sustainability_calc094_10d_base_v094_signal

def f62ds_f62_dividend_sustainability_calc095_63d_base_v095_signal(ps):
    res = ps.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc095_63d_base_v095_signal'] = f62ds_f62_dividend_sustainability_calc095_63d_base_v095_signal

def f62ds_f62_dividend_sustainability_calc096_504d_base_v096_signal(debt, equity):
    res = (debt / equity).rolling(504).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc096_504d_base_v096_signal'] = f62ds_f62_dividend_sustainability_calc096_504d_base_v096_signal

def f62ds_f62_dividend_sustainability_calc097_10d_base_v097_signal(debt, sharesbas):
    res = (sharesbas / debt).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc097_10d_base_v097_signal'] = f62ds_f62_dividend_sustainability_calc097_10d_base_v097_signal

def f62ds_f62_dividend_sustainability_calc098_5d_base_v098_signal(assets, retearn):
    res = (retearn - assets).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc098_5d_base_v098_signal'] = f62ds_f62_dividend_sustainability_calc098_5d_base_v098_signal

def f62ds_f62_dividend_sustainability_calc099_42d_base_v099_signal(ebitda, intexp):
    res = (ebitda - intexp).rolling(42).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc099_42d_base_v099_signal'] = f62ds_f62_dividend_sustainability_calc099_42d_base_v099_signal

def f62ds_f62_dividend_sustainability_calc100_5d_base_v100_signal(currentratio, opinc, sharesbas):
    res = ((currentratio - sharesbas) + opinc).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc100_5d_base_v100_signal'] = f62ds_f62_dividend_sustainability_calc100_5d_base_v100_signal

def f62ds_f62_dividend_sustainability_calc101_10d_base_v101_signal(low):
    res = low.rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc101_10d_base_v101_signal'] = f62ds_f62_dividend_sustainability_calc101_10d_base_v101_signal

def f62ds_f62_dividend_sustainability_calc102_252d_base_v102_signal(debt, marketcap, netinc):
    res = ((debt / netinc) + marketcap).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc102_252d_base_v102_signal'] = f62ds_f62_dividend_sustainability_calc102_252d_base_v102_signal

def f62ds_f62_dividend_sustainability_calc103_63d_base_v103_signal(debt, equity):
    res = (debt / equity).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc103_63d_base_v103_signal'] = f62ds_f62_dividend_sustainability_calc103_63d_base_v103_signal

def f62ds_f62_dividend_sustainability_calc104_5d_base_v104_signal(sharesbas):
    res = sharesbas.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc104_5d_base_v104_signal'] = f62ds_f62_dividend_sustainability_calc104_5d_base_v104_signal

def f62ds_f62_dividend_sustainability_calc105_42d_base_v105_signal(ev, evebitda):
    res = (ev - evebitda).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc105_42d_base_v105_signal'] = f62ds_f62_dividend_sustainability_calc105_42d_base_v105_signal

def f62ds_f62_dividend_sustainability_calc106_126d_base_v106_signal(ev):
    res = ev.rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc106_126d_base_v106_signal'] = f62ds_f62_dividend_sustainability_calc106_126d_base_v106_signal

def f62ds_f62_dividend_sustainability_calc107_252d_base_v107_signal(ncff, open, sharesbas):
    res = ((ncff + open) * sharesbas).diff(5).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc107_252d_base_v107_signal'] = f62ds_f62_dividend_sustainability_calc107_252d_base_v107_signal

def f62ds_f62_dividend_sustainability_calc108_504d_base_v108_signal(debt, equity):
    res = (debt + equity).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc108_504d_base_v108_signal'] = f62ds_f62_dividend_sustainability_calc108_504d_base_v108_signal

def f62ds_f62_dividend_sustainability_calc109_63d_base_v109_signal(ebitda, intexp):
    res = (ebitda / intexp).rolling(63).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc109_63d_base_v109_signal'] = f62ds_f62_dividend_sustainability_calc109_63d_base_v109_signal

def f62ds_f62_dividend_sustainability_calc110_5d_base_v110_signal(capex, ncfo):
    res = (ncfo + capex).rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc110_5d_base_v110_signal'] = f62ds_f62_dividend_sustainability_calc110_5d_base_v110_signal

def f62ds_f62_dividend_sustainability_calc111_5d_base_v111_signal(pe):
    res = pe.rolling(5).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc111_5d_base_v111_signal'] = f62ds_f62_dividend_sustainability_calc111_5d_base_v111_signal

def f62ds_f62_dividend_sustainability_calc112_10d_base_v112_signal(fcf, marketcap):
    res = (fcf + marketcap).pct_change(1).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc112_10d_base_v112_signal'] = f62ds_f62_dividend_sustainability_calc112_10d_base_v112_signal

def f62ds_f62_dividend_sustainability_calc113_42d_base_v113_signal(ev, marketcap, retearn):
    res = ((marketcap * retearn) / ev).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc113_42d_base_v113_signal'] = f62ds_f62_dividend_sustainability_calc113_42d_base_v113_signal

def f62ds_f62_dividend_sustainability_calc114_252d_base_v114_signal(gp, revenue):
    res = (gp * revenue).pct_change(21).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc114_252d_base_v114_signal'] = f62ds_f62_dividend_sustainability_calc114_252d_base_v114_signal

def f62ds_f62_dividend_sustainability_calc115_5d_base_v115_signal(fcf):
    res = fcf.diff(21).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc115_5d_base_v115_signal'] = f62ds_f62_dividend_sustainability_calc115_5d_base_v115_signal

def f62ds_f62_dividend_sustainability_calc116_126d_base_v116_signal(assets, ncfo):
    res = (ncfo - assets).pct_change(1).rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc116_126d_base_v116_signal'] = f62ds_f62_dividend_sustainability_calc116_126d_base_v116_signal

def f62ds_f62_dividend_sustainability_calc117_252d_base_v117_signal(closeadj, currentratio):
    res = (closeadj * currentratio).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc117_252d_base_v117_signal'] = f62ds_f62_dividend_sustainability_calc117_252d_base_v117_signal

def f62ds_f62_dividend_sustainability_calc118_252d_base_v118_signal(low):
    res = low.diff(1).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc118_252d_base_v118_signal'] = f62ds_f62_dividend_sustainability_calc118_252d_base_v118_signal

def f62ds_f62_dividend_sustainability_calc119_10d_base_v119_signal(ncfo, netinc):
    res = (ncfo - netinc).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc119_10d_base_v119_signal'] = f62ds_f62_dividend_sustainability_calc119_10d_base_v119_signal

def f62ds_f62_dividend_sustainability_calc120_252d_base_v120_signal(capex, liabilities):
    res = (liabilities / capex).pct_change(21).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc120_252d_base_v120_signal'] = f62ds_f62_dividend_sustainability_calc120_252d_base_v120_signal

def f62ds_f62_dividend_sustainability_calc121_10d_base_v121_signal(ev, evebitda):
    res = (ev + evebitda).pct_change(10).rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc121_10d_base_v121_signal'] = f62ds_f62_dividend_sustainability_calc121_10d_base_v121_signal

def f62ds_f62_dividend_sustainability_calc122_5d_base_v122_signal(equity, evebitda):
    res = (evebitda - equity).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc122_5d_base_v122_signal'] = f62ds_f62_dividend_sustainability_calc122_5d_base_v122_signal

def f62ds_f62_dividend_sustainability_calc123_10d_base_v123_signal(equity, low, retearn):
    res = ((equity - retearn) - low).rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc123_10d_base_v123_signal'] = f62ds_f62_dividend_sustainability_calc123_10d_base_v123_signal

def f62ds_f62_dividend_sustainability_calc124_5d_base_v124_signal(assets, fcf):
    res = (fcf + assets).diff(10).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc124_5d_base_v124_signal'] = f62ds_f62_dividend_sustainability_calc124_5d_base_v124_signal

def f62ds_f62_dividend_sustainability_calc125_252d_base_v125_signal(assets, liabilities):
    res = (liabilities / assets).rolling(252).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc125_252d_base_v125_signal'] = f62ds_f62_dividend_sustainability_calc125_252d_base_v125_signal

def f62ds_f62_dividend_sustainability_calc126_21d_base_v126_signal(gp):
    res = gp.rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc126_21d_base_v126_signal'] = f62ds_f62_dividend_sustainability_calc126_21d_base_v126_signal

def f62ds_f62_dividend_sustainability_calc127_504d_base_v127_signal(assets, workingcapital):
    res = (workingcapital - assets).pct_change(5).rolling(504).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc127_504d_base_v127_signal'] = f62ds_f62_dividend_sustainability_calc127_504d_base_v127_signal

def f62ds_f62_dividend_sustainability_calc128_21d_base_v128_signal(debt, equity):
    res = (debt / equity).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc128_21d_base_v128_signal'] = f62ds_f62_dividend_sustainability_calc128_21d_base_v128_signal

def f62ds_f62_dividend_sustainability_calc129_10d_base_v129_signal(assets, ncfo):
    res = (ncfo - assets).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc129_10d_base_v129_signal'] = f62ds_f62_dividend_sustainability_calc129_10d_base_v129_signal

def f62ds_f62_dividend_sustainability_calc130_21d_base_v130_signal(debt, ebitda):
    res = (debt + ebitda).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc130_21d_base_v130_signal'] = f62ds_f62_dividend_sustainability_calc130_21d_base_v130_signal

def f62ds_f62_dividend_sustainability_calc131_63d_base_v131_signal(retearn):
    res = retearn.pct_change(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc131_63d_base_v131_signal'] = f62ds_f62_dividend_sustainability_calc131_63d_base_v131_signal

def f62ds_f62_dividend_sustainability_calc132_5d_base_v132_signal(ncfi):
    res = ncfi.rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc132_5d_base_v132_signal'] = f62ds_f62_dividend_sustainability_calc132_5d_base_v132_signal

def f62ds_f62_dividend_sustainability_calc133_5d_base_v133_signal(opinc, revenue):
    res = (opinc * revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc133_5d_base_v133_signal'] = f62ds_f62_dividend_sustainability_calc133_5d_base_v133_signal

def f62ds_f62_dividend_sustainability_calc134_10d_base_v134_signal(closeadj, liabilities):
    res = (liabilities - closeadj).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc134_10d_base_v134_signal'] = f62ds_f62_dividend_sustainability_calc134_10d_base_v134_signal

def f62ds_f62_dividend_sustainability_calc135_5d_base_v135_signal(debt, retearn):
    res = (debt * retearn).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc135_5d_base_v135_signal'] = f62ds_f62_dividend_sustainability_calc135_5d_base_v135_signal

def f62ds_f62_dividend_sustainability_calc136_5d_base_v136_signal(currentratio, ps):
    res = (currentratio / ps).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc136_5d_base_v136_signal'] = f62ds_f62_dividend_sustainability_calc136_5d_base_v136_signal

def f62ds_f62_dividend_sustainability_calc137_504d_base_v137_signal(equity, netinc):
    res = (netinc - equity).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc137_504d_base_v137_signal'] = f62ds_f62_dividend_sustainability_calc137_504d_base_v137_signal

def f62ds_f62_dividend_sustainability_calc138_5d_base_v138_signal(ncfo, revenue):
    res = (ncfo - revenue).diff(1).rolling(5).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc138_5d_base_v138_signal'] = f62ds_f62_dividend_sustainability_calc138_5d_base_v138_signal

def f62ds_f62_dividend_sustainability_calc139_5d_base_v139_signal(netinc, revenue):
    res = (netinc + revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc139_5d_base_v139_signal'] = f62ds_f62_dividend_sustainability_calc139_5d_base_v139_signal

def f62ds_f62_dividend_sustainability_calc140_21d_base_v140_signal(ncfo, netinc):
    res = (ncfo + netinc).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc140_21d_base_v140_signal'] = f62ds_f62_dividend_sustainability_calc140_21d_base_v140_signal

def f62ds_f62_dividend_sustainability_calc141_21d_base_v141_signal(debt, high):
    res = (high - debt).pct_change(21).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc141_21d_base_v141_signal'] = f62ds_f62_dividend_sustainability_calc141_21d_base_v141_signal

def f62ds_f62_dividend_sustainability_calc142_504d_base_v142_signal(ncfo, netinc):
    res = (ncfo / netinc).diff(21).rolling(504).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc142_504d_base_v142_signal'] = f62ds_f62_dividend_sustainability_calc142_504d_base_v142_signal

def f62ds_f62_dividend_sustainability_calc143_42d_base_v143_signal(debt, ebitda):
    res = (debt - ebitda).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc143_42d_base_v143_signal'] = f62ds_f62_dividend_sustainability_calc143_42d_base_v143_signal

def f62ds_f62_dividend_sustainability_calc144_252d_base_v144_signal(liabilities):
    res = liabilities.pct_change(1).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc144_252d_base_v144_signal'] = f62ds_f62_dividend_sustainability_calc144_252d_base_v144_signal

def f62ds_f62_dividend_sustainability_calc145_63d_base_v145_signal(evebitda):
    res = evebitda.rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc145_63d_base_v145_signal'] = f62ds_f62_dividend_sustainability_calc145_63d_base_v145_signal

def f62ds_f62_dividend_sustainability_calc146_504d_base_v146_signal(marketcap, ncff):
    res = (ncff - marketcap).diff(21).rolling(504).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc146_504d_base_v146_signal'] = f62ds_f62_dividend_sustainability_calc146_504d_base_v146_signal

def f62ds_f62_dividend_sustainability_calc147_63d_base_v147_signal(ebitda, volume):
    res = (volume - ebitda).pct_change(5).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc147_63d_base_v147_signal'] = f62ds_f62_dividend_sustainability_calc147_63d_base_v147_signal

def f62ds_f62_dividend_sustainability_calc148_504d_base_v148_signal(debt, equity):
    res = (debt * equity).diff(5).rolling(504).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc148_504d_base_v148_signal'] = f62ds_f62_dividend_sustainability_calc148_504d_base_v148_signal

def f62ds_f62_dividend_sustainability_calc149_252d_base_v149_signal(ncff):
    res = ncff.rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc149_252d_base_v149_signal'] = f62ds_f62_dividend_sustainability_calc149_252d_base_v149_signal

def f62ds_f62_dividend_sustainability_calc150_42d_base_v150_signal(fcf, netinc):
    res = (fcf - netinc).pct_change(21).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f62ds_f62_dividend_sustainability_calc150_42d_base_v150_signal'] = f62ds_f62_dividend_sustainability_calc150_42d_base_v150_signal



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
