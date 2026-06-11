import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f58ds_f58_debt_servicing_capacity_calc076_21d_base_v076_signal(debt, equity):
    res = (debt / equity).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc076_21d_base_v076_signal'] = f58ds_f58_debt_servicing_capacity_calc076_21d_base_v076_signal

def f58ds_f58_debt_servicing_capacity_calc077_21d_base_v077_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc077_21d_base_v077_signal'] = f58ds_f58_debt_servicing_capacity_calc077_21d_base_v077_signal

def f58ds_f58_debt_servicing_capacity_calc078_63d_base_v078_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(63).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc078_63d_base_v078_signal'] = f58ds_f58_debt_servicing_capacity_calc078_63d_base_v078_signal

def f58ds_f58_debt_servicing_capacity_calc079_5d_base_v079_signal(liabilities, revenue):
    res = (liabilities / revenue).rolling(5).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc079_5d_base_v079_signal'] = f58ds_f58_debt_servicing_capacity_calc079_5d_base_v079_signal

def f58ds_f58_debt_servicing_capacity_calc080_63d_base_v080_signal(ebitda, liabilities):
    res = (((ebitda / liabilities)) / ((ebitda / liabilities)).rolling(63).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc080_63d_base_v080_signal'] = f58ds_f58_debt_servicing_capacity_calc080_63d_base_v080_signal

def f58ds_f58_debt_servicing_capacity_calc081_252d_base_v081_signal(liabilities, revenue):
    res = np.log(((liabilities / revenue)).abs().replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc081_252d_base_v081_signal'] = f58ds_f58_debt_servicing_capacity_calc081_252d_base_v081_signal

def f58ds_f58_debt_servicing_capacity_calc082_10d_base_v082_signal(intexp, netinc):
    res = (netinc / intexp).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc082_10d_base_v082_signal'] = f58ds_f58_debt_servicing_capacity_calc082_10d_base_v082_signal

def f58ds_f58_debt_servicing_capacity_calc083_5d_base_v083_signal(ebitda, liabilities):
    res = (liabilities / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc083_5d_base_v083_signal'] = f58ds_f58_debt_servicing_capacity_calc083_5d_base_v083_signal

def f58ds_f58_debt_servicing_capacity_calc084_10d_base_v084_signal(intexp, netinc):
    res = (netinc / intexp).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc084_10d_base_v084_signal'] = f58ds_f58_debt_servicing_capacity_calc084_10d_base_v084_signal

def f58ds_f58_debt_servicing_capacity_calc085_63d_base_v085_signal(debt, ncfo):
    res = (ncfo / debt).rolling(63).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc085_63d_base_v085_signal'] = f58ds_f58_debt_servicing_capacity_calc085_63d_base_v085_signal

def f58ds_f58_debt_servicing_capacity_calc086_252d_base_v086_signal(debt, fcf):
    res = (((fcf / debt)) / ((fcf / debt)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc086_252d_base_v086_signal'] = f58ds_f58_debt_servicing_capacity_calc086_252d_base_v086_signal

def f58ds_f58_debt_servicing_capacity_calc087_63d_base_v087_signal(liabilities, revenue):
    res = (liabilities / revenue).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc087_63d_base_v087_signal'] = f58ds_f58_debt_servicing_capacity_calc087_63d_base_v087_signal

def f58ds_f58_debt_servicing_capacity_calc088_10d_base_v088_signal(currentratio, debt):
    res = (((currentratio / debt)) / ((currentratio / debt)).rolling(10).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc088_10d_base_v088_signal'] = f58ds_f58_debt_servicing_capacity_calc088_10d_base_v088_signal

def f58ds_f58_debt_servicing_capacity_calc089_5d_base_v089_signal(ebitda, intexp):
    res = (ebitda / intexp).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc089_5d_base_v089_signal'] = f58ds_f58_debt_servicing_capacity_calc089_5d_base_v089_signal

def f58ds_f58_debt_servicing_capacity_calc090_5d_base_v090_signal(debt, ncfo):
    res = (ncfo / debt).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc090_5d_base_v090_signal'] = f58ds_f58_debt_servicing_capacity_calc090_5d_base_v090_signal

def f58ds_f58_debt_servicing_capacity_calc091_21d_base_v091_signal(equity, liabilities):
    res = (liabilities / equity).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc091_21d_base_v091_signal'] = f58ds_f58_debt_servicing_capacity_calc091_21d_base_v091_signal

def f58ds_f58_debt_servicing_capacity_calc092_63d_base_v092_signal(intexp, revenue):
    res = (intexp / revenue).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc092_63d_base_v092_signal'] = f58ds_f58_debt_servicing_capacity_calc092_63d_base_v092_signal

def f58ds_f58_debt_servicing_capacity_calc093_252d_base_v093_signal(ebitda, liabilities):
    res = (liabilities / ebitda).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc093_252d_base_v093_signal'] = f58ds_f58_debt_servicing_capacity_calc093_252d_base_v093_signal

def f58ds_f58_debt_servicing_capacity_calc094_252d_base_v094_signal(intexp, opinc):
    res = (opinc / intexp).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc094_252d_base_v094_signal'] = f58ds_f58_debt_servicing_capacity_calc094_252d_base_v094_signal

def f58ds_f58_debt_servicing_capacity_calc095_126d_base_v095_signal(debt, workingcapital):
    res = (((debt / workingcapital)) - ((debt / workingcapital)).rolling(126).mean()) / ((debt / workingcapital)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc095_126d_base_v095_signal'] = f58ds_f58_debt_servicing_capacity_calc095_126d_base_v095_signal

def f58ds_f58_debt_servicing_capacity_calc096_63d_base_v096_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(63).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc096_63d_base_v096_signal'] = f58ds_f58_debt_servicing_capacity_calc096_63d_base_v096_signal

def f58ds_f58_debt_servicing_capacity_calc097_10d_base_v097_signal(debt, ncfo):
    res = (ncfo / debt).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc097_10d_base_v097_signal'] = f58ds_f58_debt_servicing_capacity_calc097_10d_base_v097_signal

def f58ds_f58_debt_servicing_capacity_calc098_21d_base_v098_signal(liabilities, netinc):
    res = (netinc / liabilities).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc098_21d_base_v098_signal'] = f58ds_f58_debt_servicing_capacity_calc098_21d_base_v098_signal

def f58ds_f58_debt_servicing_capacity_calc099_63d_base_v099_signal(assets, netinc):
    res = (netinc / assets).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc099_63d_base_v099_signal'] = f58ds_f58_debt_servicing_capacity_calc099_63d_base_v099_signal

def f58ds_f58_debt_servicing_capacity_calc100_126d_base_v100_signal(fcf, intexp):
    res = (fcf / intexp).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc100_126d_base_v100_signal'] = f58ds_f58_debt_servicing_capacity_calc100_126d_base_v100_signal

def f58ds_f58_debt_servicing_capacity_calc101_63d_base_v101_signal(assets, fcf):
    res = (fcf / assets).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc101_63d_base_v101_signal'] = f58ds_f58_debt_servicing_capacity_calc101_63d_base_v101_signal

def f58ds_f58_debt_servicing_capacity_calc102_126d_base_v102_signal(debt, gp):
    res = (debt / gp).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc102_126d_base_v102_signal'] = f58ds_f58_debt_servicing_capacity_calc102_126d_base_v102_signal

def f58ds_f58_debt_servicing_capacity_calc103_42d_base_v103_signal(equity, liabilities):
    res = (((liabilities / equity)) / ((liabilities / equity)).rolling(42).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc103_42d_base_v103_signal'] = f58ds_f58_debt_servicing_capacity_calc103_42d_base_v103_signal

def f58ds_f58_debt_servicing_capacity_calc104_42d_base_v104_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc104_42d_base_v104_signal'] = f58ds_f58_debt_servicing_capacity_calc104_42d_base_v104_signal

def f58ds_f58_debt_servicing_capacity_calc105_42d_base_v105_signal(debt, revenue):
    res = (debt / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc105_42d_base_v105_signal'] = f58ds_f58_debt_servicing_capacity_calc105_42d_base_v105_signal

def f58ds_f58_debt_servicing_capacity_calc106_10d_base_v106_signal(fcf, intexp):
    res = (fcf / intexp).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc106_10d_base_v106_signal'] = f58ds_f58_debt_servicing_capacity_calc106_10d_base_v106_signal

def f58ds_f58_debt_servicing_capacity_calc107_126d_base_v107_signal(ebitda, liabilities):
    res = (liabilities / ebitda).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc107_126d_base_v107_signal'] = f58ds_f58_debt_servicing_capacity_calc107_126d_base_v107_signal

def f58ds_f58_debt_servicing_capacity_calc108_252d_base_v108_signal(currentratio, debt):
    res = (currentratio / debt).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc108_252d_base_v108_signal'] = f58ds_f58_debt_servicing_capacity_calc108_252d_base_v108_signal

def f58ds_f58_debt_servicing_capacity_calc109_126d_base_v109_signal(intexp, opinc):
    res = np.log(((opinc / intexp)).abs().replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc109_126d_base_v109_signal'] = f58ds_f58_debt_servicing_capacity_calc109_126d_base_v109_signal

def f58ds_f58_debt_servicing_capacity_calc110_63d_base_v110_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc110_63d_base_v110_signal'] = f58ds_f58_debt_servicing_capacity_calc110_63d_base_v110_signal

def f58ds_f58_debt_servicing_capacity_calc111_5d_base_v111_signal(debt, fcf):
    res = (fcf / debt).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc111_5d_base_v111_signal'] = f58ds_f58_debt_servicing_capacity_calc111_5d_base_v111_signal

def f58ds_f58_debt_servicing_capacity_calc112_252d_base_v112_signal(assets, netinc):
    res = (netinc / assets).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc112_252d_base_v112_signal'] = f58ds_f58_debt_servicing_capacity_calc112_252d_base_v112_signal

def f58ds_f58_debt_servicing_capacity_calc113_126d_base_v113_signal(debt, fcf):
    res = (fcf / debt).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc113_126d_base_v113_signal'] = f58ds_f58_debt_servicing_capacity_calc113_126d_base_v113_signal

def f58ds_f58_debt_servicing_capacity_calc114_252d_base_v114_signal(liabilities, netinc):
    res = (((netinc / liabilities)) - ((netinc / liabilities)).rolling(252).mean()) / ((netinc / liabilities)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc114_252d_base_v114_signal'] = f58ds_f58_debt_servicing_capacity_calc114_252d_base_v114_signal

def f58ds_f58_debt_servicing_capacity_calc115_126d_base_v115_signal(intexp, opinc):
    res = (opinc / intexp).rolling(126).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc115_126d_base_v115_signal'] = f58ds_f58_debt_servicing_capacity_calc115_126d_base_v115_signal

def f58ds_f58_debt_servicing_capacity_calc116_252d_base_v116_signal(ebitda, ev):
    res = (ev / ebitda).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc116_252d_base_v116_signal'] = f58ds_f58_debt_servicing_capacity_calc116_252d_base_v116_signal

def f58ds_f58_debt_servicing_capacity_calc117_21d_base_v117_signal(intexp, opinc):
    res = (((intexp / opinc)) / ((intexp / opinc)).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc117_21d_base_v117_signal'] = f58ds_f58_debt_servicing_capacity_calc117_21d_base_v117_signal

def f58ds_f58_debt_servicing_capacity_calc118_126d_base_v118_signal(ebitda, intexp):
    res = (ebitda / intexp).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc118_126d_base_v118_signal'] = f58ds_f58_debt_servicing_capacity_calc118_126d_base_v118_signal

def f58ds_f58_debt_servicing_capacity_calc119_126d_base_v119_signal(ebitda, intexp):
    res = (ebitda / intexp).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc119_126d_base_v119_signal'] = f58ds_f58_debt_servicing_capacity_calc119_126d_base_v119_signal

def f58ds_f58_debt_servicing_capacity_calc120_126d_base_v120_signal(ebitda, liabilities):
    res = (((liabilities / ebitda)) / ((liabilities / ebitda)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc120_126d_base_v120_signal'] = f58ds_f58_debt_servicing_capacity_calc120_126d_base_v120_signal

def f58ds_f58_debt_servicing_capacity_calc121_126d_base_v121_signal(assets, debt):
    res = (((debt / assets)) / ((debt / assets)).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc121_126d_base_v121_signal'] = f58ds_f58_debt_servicing_capacity_calc121_126d_base_v121_signal

def f58ds_f58_debt_servicing_capacity_calc122_63d_base_v122_signal(ebitda, ev):
    res = np.log(((ev / ebitda)).abs().replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc122_63d_base_v122_signal'] = f58ds_f58_debt_servicing_capacity_calc122_63d_base_v122_signal

def f58ds_f58_debt_servicing_capacity_calc123_252d_base_v123_signal(debt, gp):
    res = (((gp / debt)) - ((gp / debt)).rolling(252).mean()) / ((gp / debt)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc123_252d_base_v123_signal'] = f58ds_f58_debt_servicing_capacity_calc123_252d_base_v123_signal

def f58ds_f58_debt_servicing_capacity_calc124_21d_base_v124_signal(intexp, netinc):
    res = (netinc / intexp).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc124_21d_base_v124_signal'] = f58ds_f58_debt_servicing_capacity_calc124_21d_base_v124_signal

def f58ds_f58_debt_servicing_capacity_calc125_63d_base_v125_signal(debt, ncfo):
    res = (ncfo / debt).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc125_63d_base_v125_signal'] = f58ds_f58_debt_servicing_capacity_calc125_63d_base_v125_signal

def f58ds_f58_debt_servicing_capacity_calc126_252d_base_v126_signal(debt, workingcapital):
    res = (debt / workingcapital).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc126_252d_base_v126_signal'] = f58ds_f58_debt_servicing_capacity_calc126_252d_base_v126_signal

def f58ds_f58_debt_servicing_capacity_calc127_126d_base_v127_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc127_126d_base_v127_signal'] = f58ds_f58_debt_servicing_capacity_calc127_126d_base_v127_signal

def f58ds_f58_debt_servicing_capacity_calc128_10d_base_v128_signal(assets, fcf):
    res = (fcf / assets).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc128_10d_base_v128_signal'] = f58ds_f58_debt_servicing_capacity_calc128_10d_base_v128_signal

def f58ds_f58_debt_servicing_capacity_calc129_21d_base_v129_signal(debt, marketcap):
    res = (debt / marketcap).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc129_21d_base_v129_signal'] = f58ds_f58_debt_servicing_capacity_calc129_21d_base_v129_signal

def f58ds_f58_debt_servicing_capacity_calc130_10d_base_v130_signal(liabilities, netinc):
    res = (((netinc / liabilities)) / ((netinc / liabilities)).rolling(10).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc130_10d_base_v130_signal'] = f58ds_f58_debt_servicing_capacity_calc130_10d_base_v130_signal

def f58ds_f58_debt_servicing_capacity_calc131_42d_base_v131_signal(intexp, opinc):
    res = (intexp / opinc).rolling(42).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc131_42d_base_v131_signal'] = f58ds_f58_debt_servicing_capacity_calc131_42d_base_v131_signal

def f58ds_f58_debt_servicing_capacity_calc132_42d_base_v132_signal(debt, equity):
    res = (debt / equity).rolling(42).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc132_42d_base_v132_signal'] = f58ds_f58_debt_servicing_capacity_calc132_42d_base_v132_signal

def f58ds_f58_debt_servicing_capacity_calc133_5d_base_v133_signal(debt, equity):
    res = (debt / equity).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc133_5d_base_v133_signal'] = f58ds_f58_debt_servicing_capacity_calc133_5d_base_v133_signal

def f58ds_f58_debt_servicing_capacity_calc134_63d_base_v134_signal(debt, ebitda):
    res = (debt / ebitda).rolling(63).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc134_63d_base_v134_signal'] = f58ds_f58_debt_servicing_capacity_calc134_63d_base_v134_signal

def f58ds_f58_debt_servicing_capacity_calc135_63d_base_v135_signal(assets, netinc):
    res = (netinc / assets).rolling(63).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc135_63d_base_v135_signal'] = f58ds_f58_debt_servicing_capacity_calc135_63d_base_v135_signal

def f58ds_f58_debt_servicing_capacity_calc136_63d_base_v136_signal(intexp, opinc):
    res = (((opinc / intexp)) / ((opinc / intexp)).rolling(63).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc136_63d_base_v136_signal'] = f58ds_f58_debt_servicing_capacity_calc136_63d_base_v136_signal

def f58ds_f58_debt_servicing_capacity_calc137_10d_base_v137_signal(ebitda, ev):
    res = (ev / ebitda).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc137_10d_base_v137_signal'] = f58ds_f58_debt_servicing_capacity_calc137_10d_base_v137_signal

def f58ds_f58_debt_servicing_capacity_calc138_252d_base_v138_signal(fcf, liabilities):
    res = (((fcf / liabilities)) / ((fcf / liabilities)).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc138_252d_base_v138_signal'] = f58ds_f58_debt_servicing_capacity_calc138_252d_base_v138_signal

def f58ds_f58_debt_servicing_capacity_calc139_10d_base_v139_signal(debt, fcf):
    res = (fcf / debt).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc139_10d_base_v139_signal'] = f58ds_f58_debt_servicing_capacity_calc139_10d_base_v139_signal

def f58ds_f58_debt_servicing_capacity_calc140_126d_base_v140_signal(intexp, opinc):
    res = (opinc / intexp).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc140_126d_base_v140_signal'] = f58ds_f58_debt_servicing_capacity_calc140_126d_base_v140_signal

def f58ds_f58_debt_servicing_capacity_calc141_63d_base_v141_signal(intexp, opinc):
    res = np.log(((opinc / intexp)).abs().replace(0, np.nan)).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc141_63d_base_v141_signal'] = f58ds_f58_debt_servicing_capacity_calc141_63d_base_v141_signal

def f58ds_f58_debt_servicing_capacity_calc142_42d_base_v142_signal(assets, debt):
    res = np.log(((debt / assets)).abs().replace(0, np.nan)).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc142_42d_base_v142_signal'] = f58ds_f58_debt_servicing_capacity_calc142_42d_base_v142_signal

def f58ds_f58_debt_servicing_capacity_calc143_5d_base_v143_signal(intexp, opinc):
    res = (opinc / intexp).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc143_5d_base_v143_signal'] = f58ds_f58_debt_servicing_capacity_calc143_5d_base_v143_signal

def f58ds_f58_debt_servicing_capacity_calc144_5d_base_v144_signal(intexp, netinc):
    res = (((netinc / intexp)) - ((netinc / intexp)).rolling(5).mean()) / ((netinc / intexp)).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc144_5d_base_v144_signal'] = f58ds_f58_debt_servicing_capacity_calc144_5d_base_v144_signal

def f58ds_f58_debt_servicing_capacity_calc145_21d_base_v145_signal(debt, workingcapital):
    res = (workingcapital / debt).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc145_21d_base_v145_signal'] = f58ds_f58_debt_servicing_capacity_calc145_21d_base_v145_signal

def f58ds_f58_debt_servicing_capacity_calc146_63d_base_v146_signal(debt, gp):
    res = (debt / gp).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc146_63d_base_v146_signal'] = f58ds_f58_debt_servicing_capacity_calc146_63d_base_v146_signal

def f58ds_f58_debt_servicing_capacity_calc147_10d_base_v147_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc147_10d_base_v147_signal'] = f58ds_f58_debt_servicing_capacity_calc147_10d_base_v147_signal

def f58ds_f58_debt_servicing_capacity_calc148_5d_base_v148_signal(debt, marketcap):
    res = (debt / marketcap).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc148_5d_base_v148_signal'] = f58ds_f58_debt_servicing_capacity_calc148_5d_base_v148_signal

def f58ds_f58_debt_servicing_capacity_calc149_42d_base_v149_signal(ebitda, ev):
    res = (ev / ebitda).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc149_42d_base_v149_signal'] = f58ds_f58_debt_servicing_capacity_calc149_42d_base_v149_signal

def f58ds_f58_debt_servicing_capacity_calc150_126d_base_v150_signal(intexp, opinc):
    res = (intexp / opinc).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f58ds_f58_debt_servicing_capacity_calc150_126d_base_v150_signal'] = f58ds_f58_debt_servicing_capacity_calc150_126d_base_v150_signal



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
