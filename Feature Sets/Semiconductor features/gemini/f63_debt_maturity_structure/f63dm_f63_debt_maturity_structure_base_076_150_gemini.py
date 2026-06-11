import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f63dm_f63_debt_maturity_structure_calc076_60d_base_v076_signal(assets, debt):
    res = (debt / assets).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc076_60d_base_v076_signal'] = f63dm_f63_debt_maturity_structure_calc076_60d_base_v076_signal

def f63dm_f63_debt_maturity_structure_calc077_60d_base_v077_signal(debt, equity):
    res = (debt / equity).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc077_60d_base_v077_signal'] = f63dm_f63_debt_maturity_structure_calc077_60d_base_v077_signal

def f63dm_f63_debt_maturity_structure_calc078_60d_base_v078_signal(debt, ebitda):
    res = (debt / ebitda).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc078_60d_base_v078_signal'] = f63dm_f63_debt_maturity_structure_calc078_60d_base_v078_signal

def f63dm_f63_debt_maturity_structure_calc079_60d_base_v079_signal(debt, marketcap):
    res = (debt / marketcap).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc079_60d_base_v079_signal'] = f63dm_f63_debt_maturity_structure_calc079_60d_base_v079_signal

def f63dm_f63_debt_maturity_structure_calc080_60d_base_v080_signal(assets, liabilities):
    res = (liabilities / assets).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc080_60d_base_v080_signal'] = f63dm_f63_debt_maturity_structure_calc080_60d_base_v080_signal

def f63dm_f63_debt_maturity_structure_calc081_60d_base_v081_signal(debt, workingcapital):
    res = (workingcapital / debt).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc081_60d_base_v081_signal'] = f63dm_f63_debt_maturity_structure_calc081_60d_base_v081_signal

def f63dm_f63_debt_maturity_structure_calc082_60d_base_v082_signal(currentratio):
    res = currentratio.diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc082_60d_base_v082_signal'] = f63dm_f63_debt_maturity_structure_calc082_60d_base_v082_signal

def f63dm_f63_debt_maturity_structure_calc083_60d_base_v083_signal(intexp, revenue):
    res = (intexp / revenue).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc083_60d_base_v083_signal'] = f63dm_f63_debt_maturity_structure_calc083_60d_base_v083_signal

def f63dm_f63_debt_maturity_structure_calc084_60d_base_v084_signal(debt, intexp):
    res = (intexp / debt).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc084_60d_base_v084_signal'] = f63dm_f63_debt_maturity_structure_calc084_60d_base_v084_signal

def f63dm_f63_debt_maturity_structure_calc085_60d_base_v085_signal(debt, fcf):
    res = (fcf / debt).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc085_60d_base_v085_signal'] = f63dm_f63_debt_maturity_structure_calc085_60d_base_v085_signal

def f63dm_f63_debt_maturity_structure_calc086_60d_base_v086_signal(debt, ncfo):
    res = (ncfo / debt).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc086_60d_base_v086_signal'] = f63dm_f63_debt_maturity_structure_calc086_60d_base_v086_signal

def f63dm_f63_debt_maturity_structure_calc087_60d_base_v087_signal(debt, revenue):
    res = (debt / revenue).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc087_60d_base_v087_signal'] = f63dm_f63_debt_maturity_structure_calc087_60d_base_v087_signal

def f63dm_f63_debt_maturity_structure_calc088_60d_base_v088_signal(debt, opinc):
    res = (debt / opinc).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc088_60d_base_v088_signal'] = f63dm_f63_debt_maturity_structure_calc088_60d_base_v088_signal

def f63dm_f63_debt_maturity_structure_calc089_60d_base_v089_signal(debt, ev):
    res = (debt / ev).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc089_60d_base_v089_signal'] = f63dm_f63_debt_maturity_structure_calc089_60d_base_v089_signal

def f63dm_f63_debt_maturity_structure_calc090_60d_base_v090_signal(assets, equity):
    res = (equity / assets).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc090_60d_base_v090_signal'] = f63dm_f63_debt_maturity_structure_calc090_60d_base_v090_signal

def f63dm_f63_debt_maturity_structure_calc091_120d_base_v091_signal(assets, debt):
    res = (debt / assets).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc091_120d_base_v091_signal'] = f63dm_f63_debt_maturity_structure_calc091_120d_base_v091_signal

def f63dm_f63_debt_maturity_structure_calc092_120d_base_v092_signal(debt, equity):
    res = (debt / equity).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc092_120d_base_v092_signal'] = f63dm_f63_debt_maturity_structure_calc092_120d_base_v092_signal

def f63dm_f63_debt_maturity_structure_calc093_120d_base_v093_signal(debt, ebitda):
    res = (debt / ebitda).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc093_120d_base_v093_signal'] = f63dm_f63_debt_maturity_structure_calc093_120d_base_v093_signal

def f63dm_f63_debt_maturity_structure_calc094_120d_base_v094_signal(debt, marketcap):
    res = (debt / marketcap).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc094_120d_base_v094_signal'] = f63dm_f63_debt_maturity_structure_calc094_120d_base_v094_signal

def f63dm_f63_debt_maturity_structure_calc095_120d_base_v095_signal(assets, liabilities):
    res = (liabilities / assets).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc095_120d_base_v095_signal'] = f63dm_f63_debt_maturity_structure_calc095_120d_base_v095_signal

def f63dm_f63_debt_maturity_structure_calc096_120d_base_v096_signal(debt, workingcapital):
    res = (workingcapital / debt).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc096_120d_base_v096_signal'] = f63dm_f63_debt_maturity_structure_calc096_120d_base_v096_signal

def f63dm_f63_debt_maturity_structure_calc097_120d_base_v097_signal(currentratio):
    res = currentratio.diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc097_120d_base_v097_signal'] = f63dm_f63_debt_maturity_structure_calc097_120d_base_v097_signal

def f63dm_f63_debt_maturity_structure_calc098_120d_base_v098_signal(intexp, revenue):
    res = (intexp / revenue).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc098_120d_base_v098_signal'] = f63dm_f63_debt_maturity_structure_calc098_120d_base_v098_signal

def f63dm_f63_debt_maturity_structure_calc099_120d_base_v099_signal(debt, intexp):
    res = (intexp / debt).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc099_120d_base_v099_signal'] = f63dm_f63_debt_maturity_structure_calc099_120d_base_v099_signal

def f63dm_f63_debt_maturity_structure_calc100_120d_base_v100_signal(debt, fcf):
    res = (fcf / debt).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc100_120d_base_v100_signal'] = f63dm_f63_debt_maturity_structure_calc100_120d_base_v100_signal

def f63dm_f63_debt_maturity_structure_calc101_120d_base_v101_signal(debt, ncfo):
    res = (ncfo / debt).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc101_120d_base_v101_signal'] = f63dm_f63_debt_maturity_structure_calc101_120d_base_v101_signal

def f63dm_f63_debt_maturity_structure_calc102_120d_base_v102_signal(debt, revenue):
    res = (debt / revenue).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc102_120d_base_v102_signal'] = f63dm_f63_debt_maturity_structure_calc102_120d_base_v102_signal

def f63dm_f63_debt_maturity_structure_calc103_120d_base_v103_signal(debt, opinc):
    res = (debt / opinc).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc103_120d_base_v103_signal'] = f63dm_f63_debt_maturity_structure_calc103_120d_base_v103_signal

def f63dm_f63_debt_maturity_structure_calc104_120d_base_v104_signal(debt, ev):
    res = (debt / ev).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc104_120d_base_v104_signal'] = f63dm_f63_debt_maturity_structure_calc104_120d_base_v104_signal

def f63dm_f63_debt_maturity_structure_calc105_120d_base_v105_signal(assets, equity):
    res = (equity / assets).diff(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc105_120d_base_v105_signal'] = f63dm_f63_debt_maturity_structure_calc105_120d_base_v105_signal

def f63dm_f63_debt_maturity_structure_calc106_30d_base_v106_signal(assets, debt):
    res = (debt / assets).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc106_30d_base_v106_signal'] = f63dm_f63_debt_maturity_structure_calc106_30d_base_v106_signal

def f63dm_f63_debt_maturity_structure_calc107_30d_base_v107_signal(debt, equity):
    res = (debt / equity).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc107_30d_base_v107_signal'] = f63dm_f63_debt_maturity_structure_calc107_30d_base_v107_signal

def f63dm_f63_debt_maturity_structure_calc108_30d_base_v108_signal(debt, ebitda):
    res = (debt / ebitda).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc108_30d_base_v108_signal'] = f63dm_f63_debt_maturity_structure_calc108_30d_base_v108_signal

def f63dm_f63_debt_maturity_structure_calc109_30d_base_v109_signal(debt, marketcap):
    res = (debt / marketcap).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc109_30d_base_v109_signal'] = f63dm_f63_debt_maturity_structure_calc109_30d_base_v109_signal

def f63dm_f63_debt_maturity_structure_calc110_30d_base_v110_signal(assets, liabilities):
    res = (liabilities / assets).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc110_30d_base_v110_signal'] = f63dm_f63_debt_maturity_structure_calc110_30d_base_v110_signal

def f63dm_f63_debt_maturity_structure_calc111_30d_base_v111_signal(debt, workingcapital):
    res = (workingcapital / debt).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc111_30d_base_v111_signal'] = f63dm_f63_debt_maturity_structure_calc111_30d_base_v111_signal

def f63dm_f63_debt_maturity_structure_calc112_30d_base_v112_signal(currentratio):
    res = currentratio.diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc112_30d_base_v112_signal'] = f63dm_f63_debt_maturity_structure_calc112_30d_base_v112_signal

def f63dm_f63_debt_maturity_structure_calc113_30d_base_v113_signal(intexp, revenue):
    res = (intexp / revenue).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc113_30d_base_v113_signal'] = f63dm_f63_debt_maturity_structure_calc113_30d_base_v113_signal

def f63dm_f63_debt_maturity_structure_calc114_30d_base_v114_signal(debt, intexp):
    res = (intexp / debt).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc114_30d_base_v114_signal'] = f63dm_f63_debt_maturity_structure_calc114_30d_base_v114_signal

def f63dm_f63_debt_maturity_structure_calc115_30d_base_v115_signal(debt, fcf):
    res = (fcf / debt).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc115_30d_base_v115_signal'] = f63dm_f63_debt_maturity_structure_calc115_30d_base_v115_signal

def f63dm_f63_debt_maturity_structure_calc116_30d_base_v116_signal(debt, ncfo):
    res = (ncfo / debt).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc116_30d_base_v116_signal'] = f63dm_f63_debt_maturity_structure_calc116_30d_base_v116_signal

def f63dm_f63_debt_maturity_structure_calc117_30d_base_v117_signal(debt, revenue):
    res = (debt / revenue).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc117_30d_base_v117_signal'] = f63dm_f63_debt_maturity_structure_calc117_30d_base_v117_signal

def f63dm_f63_debt_maturity_structure_calc118_30d_base_v118_signal(debt, opinc):
    res = (debt / opinc).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc118_30d_base_v118_signal'] = f63dm_f63_debt_maturity_structure_calc118_30d_base_v118_signal

def f63dm_f63_debt_maturity_structure_calc119_30d_base_v119_signal(debt, ev):
    res = (debt / ev).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc119_30d_base_v119_signal'] = f63dm_f63_debt_maturity_structure_calc119_30d_base_v119_signal

def f63dm_f63_debt_maturity_structure_calc120_30d_base_v120_signal(assets, equity):
    res = (equity / assets).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc120_30d_base_v120_signal'] = f63dm_f63_debt_maturity_structure_calc120_30d_base_v120_signal

def f63dm_f63_debt_maturity_structure_calc121_90d_base_v121_signal(assets, debt):
    res = (debt / assets).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc121_90d_base_v121_signal'] = f63dm_f63_debt_maturity_structure_calc121_90d_base_v121_signal

def f63dm_f63_debt_maturity_structure_calc122_90d_base_v122_signal(debt, equity):
    res = (debt / equity).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc122_90d_base_v122_signal'] = f63dm_f63_debt_maturity_structure_calc122_90d_base_v122_signal

def f63dm_f63_debt_maturity_structure_calc123_90d_base_v123_signal(debt, ebitda):
    res = (debt / ebitda).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc123_90d_base_v123_signal'] = f63dm_f63_debt_maturity_structure_calc123_90d_base_v123_signal

def f63dm_f63_debt_maturity_structure_calc124_90d_base_v124_signal(debt, marketcap):
    res = (debt / marketcap).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc124_90d_base_v124_signal'] = f63dm_f63_debt_maturity_structure_calc124_90d_base_v124_signal

def f63dm_f63_debt_maturity_structure_calc125_90d_base_v125_signal(assets, liabilities):
    res = (liabilities / assets).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc125_90d_base_v125_signal'] = f63dm_f63_debt_maturity_structure_calc125_90d_base_v125_signal

def f63dm_f63_debt_maturity_structure_calc126_90d_base_v126_signal(debt, workingcapital):
    res = (workingcapital / debt).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc126_90d_base_v126_signal'] = f63dm_f63_debt_maturity_structure_calc126_90d_base_v126_signal

def f63dm_f63_debt_maturity_structure_calc127_90d_base_v127_signal(currentratio):
    res = currentratio.diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc127_90d_base_v127_signal'] = f63dm_f63_debt_maturity_structure_calc127_90d_base_v127_signal

def f63dm_f63_debt_maturity_structure_calc128_90d_base_v128_signal(intexp, revenue):
    res = (intexp / revenue).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc128_90d_base_v128_signal'] = f63dm_f63_debt_maturity_structure_calc128_90d_base_v128_signal

def f63dm_f63_debt_maturity_structure_calc129_90d_base_v129_signal(debt, intexp):
    res = (intexp / debt).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc129_90d_base_v129_signal'] = f63dm_f63_debt_maturity_structure_calc129_90d_base_v129_signal

def f63dm_f63_debt_maturity_structure_calc130_90d_base_v130_signal(debt, fcf):
    res = (fcf / debt).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc130_90d_base_v130_signal'] = f63dm_f63_debt_maturity_structure_calc130_90d_base_v130_signal

def f63dm_f63_debt_maturity_structure_calc131_90d_base_v131_signal(debt, ncfo):
    res = (ncfo / debt).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc131_90d_base_v131_signal'] = f63dm_f63_debt_maturity_structure_calc131_90d_base_v131_signal

def f63dm_f63_debt_maturity_structure_calc132_90d_base_v132_signal(debt, revenue):
    res = (debt / revenue).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc132_90d_base_v132_signal'] = f63dm_f63_debt_maturity_structure_calc132_90d_base_v132_signal

def f63dm_f63_debt_maturity_structure_calc133_90d_base_v133_signal(debt, opinc):
    res = (debt / opinc).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc133_90d_base_v133_signal'] = f63dm_f63_debt_maturity_structure_calc133_90d_base_v133_signal

def f63dm_f63_debt_maturity_structure_calc134_90d_base_v134_signal(debt, ev):
    res = (debt / ev).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc134_90d_base_v134_signal'] = f63dm_f63_debt_maturity_structure_calc134_90d_base_v134_signal

def f63dm_f63_debt_maturity_structure_calc135_90d_base_v135_signal(assets, equity):
    res = (equity / assets).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc135_90d_base_v135_signal'] = f63dm_f63_debt_maturity_structure_calc135_90d_base_v135_signal

def f63dm_f63_debt_maturity_structure_calc136_150d_base_v136_signal(assets, debt):
    res = (debt / assets).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc136_150d_base_v136_signal'] = f63dm_f63_debt_maturity_structure_calc136_150d_base_v136_signal

def f63dm_f63_debt_maturity_structure_calc137_150d_base_v137_signal(debt, equity):
    res = (debt / equity).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc137_150d_base_v137_signal'] = f63dm_f63_debt_maturity_structure_calc137_150d_base_v137_signal

def f63dm_f63_debt_maturity_structure_calc138_150d_base_v138_signal(debt, ebitda):
    res = (debt / ebitda).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc138_150d_base_v138_signal'] = f63dm_f63_debt_maturity_structure_calc138_150d_base_v138_signal

def f63dm_f63_debt_maturity_structure_calc139_150d_base_v139_signal(debt, marketcap):
    res = (debt / marketcap).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc139_150d_base_v139_signal'] = f63dm_f63_debt_maturity_structure_calc139_150d_base_v139_signal

def f63dm_f63_debt_maturity_structure_calc140_150d_base_v140_signal(assets, liabilities):
    res = (liabilities / assets).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc140_150d_base_v140_signal'] = f63dm_f63_debt_maturity_structure_calc140_150d_base_v140_signal

def f63dm_f63_debt_maturity_structure_calc141_150d_base_v141_signal(debt, workingcapital):
    res = (workingcapital / debt).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc141_150d_base_v141_signal'] = f63dm_f63_debt_maturity_structure_calc141_150d_base_v141_signal

def f63dm_f63_debt_maturity_structure_calc142_150d_base_v142_signal(currentratio):
    res = currentratio.diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc142_150d_base_v142_signal'] = f63dm_f63_debt_maturity_structure_calc142_150d_base_v142_signal

def f63dm_f63_debt_maturity_structure_calc143_150d_base_v143_signal(intexp, revenue):
    res = (intexp / revenue).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc143_150d_base_v143_signal'] = f63dm_f63_debt_maturity_structure_calc143_150d_base_v143_signal

def f63dm_f63_debt_maturity_structure_calc144_150d_base_v144_signal(debt, intexp):
    res = (intexp / debt).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc144_150d_base_v144_signal'] = f63dm_f63_debt_maturity_structure_calc144_150d_base_v144_signal

def f63dm_f63_debt_maturity_structure_calc145_150d_base_v145_signal(debt, fcf):
    res = (fcf / debt).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc145_150d_base_v145_signal'] = f63dm_f63_debt_maturity_structure_calc145_150d_base_v145_signal

def f63dm_f63_debt_maturity_structure_calc146_150d_base_v146_signal(debt, ncfo):
    res = (ncfo / debt).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc146_150d_base_v146_signal'] = f63dm_f63_debt_maturity_structure_calc146_150d_base_v146_signal

def f63dm_f63_debt_maturity_structure_calc147_150d_base_v147_signal(debt, revenue):
    res = (debt / revenue).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc147_150d_base_v147_signal'] = f63dm_f63_debt_maturity_structure_calc147_150d_base_v147_signal

def f63dm_f63_debt_maturity_structure_calc148_150d_base_v148_signal(debt, opinc):
    res = (debt / opinc).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc148_150d_base_v148_signal'] = f63dm_f63_debt_maturity_structure_calc148_150d_base_v148_signal

def f63dm_f63_debt_maturity_structure_calc149_150d_base_v149_signal(debt, ev):
    res = (debt / ev).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc149_150d_base_v149_signal'] = f63dm_f63_debt_maturity_structure_calc149_150d_base_v149_signal

def f63dm_f63_debt_maturity_structure_calc150_150d_base_v150_signal(assets, equity):
    res = (equity / assets).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f63dm_f63_debt_maturity_structure_calc150_150d_base_v150_signal'] = f63dm_f63_debt_maturity_structure_calc150_150d_base_v150_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "debt": np.random.uniform(100, 1000, n),
        "assets": np.random.uniform(1000, 5000, n),
        "equity": np.random.uniform(500, 3000, n),
        "ebitda": np.random.uniform(50, 500, n),
        "marketcap": np.random.uniform(1000, 10000, n),
        "liabilities": np.random.uniform(500, 4000, n),
        "workingcapital": np.random.uniform(50, 1000, n),
        "currentratio": np.random.uniform(0.5, 3.0, n),
        "intexp": np.random.uniform(5, 100, n),
        "revenue": np.random.uniform(500, 5000, n),
        "fcf": np.random.uniform(10, 500, n),
        "ncfo": np.random.uniform(20, 600, n),
        "opinc": np.random.uniform(30, 700, n),
        "ev": np.random.uniform(1000, 15000, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        max_corr = 0
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                c = corr_matrix.iloc[i, j]
                if c > max_corr: max_corr = c
        print(f"Max correlation: {max_corr}")
        assert max_corr <= 0.95, f"Max correlation {max_corr} > 0.95"
    print("Self-test passed")

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
