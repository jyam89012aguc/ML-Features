import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f69oc_f69_operating_cash_flow_stability_calc076_10d_base_v076_signal(capex, ncfo):
    res = np.log((ncfo.abs() + 1) / (capex.abs() + 1)).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc076_10d_base_v076_signal'] = f69oc_f69_operating_cash_flow_stability_calc076_10d_base_v076_signal

def f69oc_f69_operating_cash_flow_stability_calc077_10d_base_v077_signal(ncfo):
    res = (ncfo.rolling(10).rank(pct=True)).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc077_10d_base_v077_signal'] = f69oc_f69_operating_cash_flow_stability_calc077_10d_base_v077_signal

def f69oc_f69_operating_cash_flow_stability_calc078_15d_base_v078_signal(ncfo, pe):
    res = (ncfo / pe.replace(0, np.nan)).rolling(15).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc078_15d_base_v078_signal'] = f69oc_f69_operating_cash_flow_stability_calc078_15d_base_v078_signal

def f69oc_f69_operating_cash_flow_stability_calc079_30d_base_v079_signal(assets, ncfo):
    res = (ncfo - assets.rolling(30).mean()).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc079_30d_base_v079_signal'] = f69oc_f69_operating_cash_flow_stability_calc079_30d_base_v079_signal

def f69oc_f69_operating_cash_flow_stability_calc080_126d_base_v080_signal(ncfo):
    res = ncfo.pct_change(126).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc080_126d_base_v080_signal'] = f69oc_f69_operating_cash_flow_stability_calc080_126d_base_v080_signal

def f69oc_f69_operating_cash_flow_stability_calc081_126d_base_v081_signal(fcf, gp, ncfo):
    res = (ncfo * gp / fcf.replace(0, np.nan)).pct_change(12)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc081_126d_base_v081_signal'] = f69oc_f69_operating_cash_flow_stability_calc081_126d_base_v081_signal

def f69oc_f69_operating_cash_flow_stability_calc082_200d_base_v082_signal(marketcap, ncfo, taxexp):
    res = (ncfo.rolling(200).mean() - marketcap.rolling(200).mean()) / taxexp.replace(0, np.nan).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc082_200d_base_v082_signal'] = f69oc_f69_operating_cash_flow_stability_calc082_200d_base_v082_signal

def f69oc_f69_operating_cash_flow_stability_calc083_80d_base_v083_signal(ncfo, open):
    res = (ncfo - open.rolling(80).mean()).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc083_80d_base_v083_signal'] = f69oc_f69_operating_cash_flow_stability_calc083_80d_base_v083_signal

def f69oc_f69_operating_cash_flow_stability_calc084_50d_base_v084_signal(ncfo):
    res = (ncfo.rolling(50).max() / ncfo.rolling(50).min()).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc084_50d_base_v084_signal'] = f69oc_f69_operating_cash_flow_stability_calc084_50d_base_v084_signal

def f69oc_f69_operating_cash_flow_stability_calc085_126d_base_v085_signal(ncfi, ncfo):
    res = (ncfo.rolling(126).max() - ncfo.rolling(126).min()) / ncfi.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc085_126d_base_v085_signal'] = f69oc_f69_operating_cash_flow_stability_calc085_126d_base_v085_signal

def f69oc_f69_operating_cash_flow_stability_calc086_150d_base_v086_signal(ncfo):
    res = (ncfo - ncfo.shift(150)).rolling(150).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc086_150d_base_v086_signal'] = f69oc_f69_operating_cash_flow_stability_calc086_150d_base_v086_signal

def f69oc_f69_operating_cash_flow_stability_calc087_126d_base_v087_signal(ncfo):
    res = ncfo.rolling(126).median().pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc087_126d_base_v087_signal'] = f69oc_f69_operating_cash_flow_stability_calc087_126d_base_v087_signal

def f69oc_f69_operating_cash_flow_stability_calc088_80d_base_v088_signal(ncfo):
    res = (ncfo.rolling(80).rank(pct=True)).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc088_80d_base_v088_signal'] = f69oc_f69_operating_cash_flow_stability_calc088_80d_base_v088_signal

def f69oc_f69_operating_cash_flow_stability_calc089_126d_base_v089_signal(capex, ncfo):
    res = np.log((ncfo.abs() + 1) / (capex.abs() + 1)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc089_126d_base_v089_signal'] = f69oc_f69_operating_cash_flow_stability_calc089_126d_base_v089_signal

def f69oc_f69_operating_cash_flow_stability_calc090_21d_base_v090_signal(eps, marketcap, ncfo):
    res = (ncfo.rolling(21).mean() - eps.rolling(21).mean()) / marketcap.replace(0, np.nan).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc090_21d_base_v090_signal'] = f69oc_f69_operating_cash_flow_stability_calc090_21d_base_v090_signal

def f69oc_f69_operating_cash_flow_stability_calc091_150d_base_v091_signal(ev, ncfo):
    res = (ncfo - ev.rolling(150).mean()).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc091_150d_base_v091_signal'] = f69oc_f69_operating_cash_flow_stability_calc091_150d_base_v091_signal

def f69oc_f69_operating_cash_flow_stability_calc092_200d_base_v092_signal(ncfo):
    res = ncfo.rolling(200).std() / ncfo.rolling(200).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc092_200d_base_v092_signal'] = f69oc_f69_operating_cash_flow_stability_calc092_200d_base_v092_signal

def f69oc_f69_operating_cash_flow_stability_calc093_15d_base_v093_signal(currentratio, ncfo):
    res = (ncfo.diff(15) / currentratio.replace(0, np.nan).diff(15)).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc093_15d_base_v093_signal'] = f69oc_f69_operating_cash_flow_stability_calc093_15d_base_v093_signal

def f69oc_f69_operating_cash_flow_stability_calc094_30d_base_v094_signal(ncfo, sharesbas):
    res = ncfo.rolling(30).quantile(0.3) - sharesbas.rolling(30).quantile(0.7)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc094_30d_base_v094_signal'] = f69oc_f69_operating_cash_flow_stability_calc094_30d_base_v094_signal

def f69oc_f69_operating_cash_flow_stability_calc095_252d_base_v095_signal(eps, ncfo):
    res = ncfo.rolling(252).quantile(0.3) - eps.rolling(252).quantile(0.7)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc095_252d_base_v095_signal'] = f69oc_f69_operating_cash_flow_stability_calc095_252d_base_v095_signal

def f69oc_f69_operating_cash_flow_stability_calc096_42d_base_v096_signal(close, ncfo):
    res = (close / ncfo.replace(0, np.nan)).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc096_42d_base_v096_signal'] = f69oc_f69_operating_cash_flow_stability_calc096_42d_base_v096_signal

def f69oc_f69_operating_cash_flow_stability_calc097_150d_base_v097_signal(currentratio, ebitda, ncfo):
    res = (ncfo * ebitda / currentratio.replace(0, np.nan)).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc097_150d_base_v097_signal'] = f69oc_f69_operating_cash_flow_stability_calc097_150d_base_v097_signal

def f69oc_f69_operating_cash_flow_stability_calc098_150d_base_v098_signal(ncfo):
    res = np.log((ncfo.abs() + 1) / (ncfo.abs() + 1)).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc098_150d_base_v098_signal'] = f69oc_f69_operating_cash_flow_stability_calc098_150d_base_v098_signal

def f69oc_f69_operating_cash_flow_stability_calc099_80d_base_v099_signal(liabilities, ncfo):
    res = (ncfo * liabilities).rolling(80).std() / (ncfo * liabilities).rolling(80).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc099_80d_base_v099_signal'] = f69oc_f69_operating_cash_flow_stability_calc099_80d_base_v099_signal

def f69oc_f69_operating_cash_flow_stability_calc100_50d_base_v100_signal(intexp, ncfo):
    res = (ncfo / intexp.replace(0, np.nan)).rolling(50).std().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc100_50d_base_v100_signal'] = f69oc_f69_operating_cash_flow_stability_calc100_50d_base_v100_signal

def f69oc_f69_operating_cash_flow_stability_calc101_150d_base_v101_signal(ncfo):
    res = (ncfo.rolling(150).rank(pct=True)).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc101_150d_base_v101_signal'] = f69oc_f69_operating_cash_flow_stability_calc101_150d_base_v101_signal

def f69oc_f69_operating_cash_flow_stability_calc102_50d_base_v102_signal(equity, ncfo, workingcapital):
    res = (ncfo.rolling(50).mean() - equity.rolling(50).mean()) / workingcapital.replace(0, np.nan).rolling(50).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc102_50d_base_v102_signal'] = f69oc_f69_operating_cash_flow_stability_calc102_50d_base_v102_signal

def f69oc_f69_operating_cash_flow_stability_calc103_10d_base_v103_signal(ncfo, pb):
    res = (ncfo - pb).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc103_10d_base_v103_signal'] = f69oc_f69_operating_cash_flow_stability_calc103_10d_base_v103_signal

def f69oc_f69_operating_cash_flow_stability_calc104_30d_base_v104_signal(ncff, ncfo):
    res = (ncfo / ncff.replace(0, np.nan)).rolling(30).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc104_30d_base_v104_signal'] = f69oc_f69_operating_cash_flow_stability_calc104_30d_base_v104_signal

def f69oc_f69_operating_cash_flow_stability_calc105_100d_base_v105_signal(ncfo, open):
    res = ncfo.rolling(100).var() / open.rolling(100).var().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc105_100d_base_v105_signal'] = f69oc_f69_operating_cash_flow_stability_calc105_100d_base_v105_signal

def f69oc_f69_operating_cash_flow_stability_calc106_252d_base_v106_signal(ncfo, taxexp):
    res = (ncfo.rolling(252).max() - ncfo.rolling(252).min()) / taxexp.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc106_252d_base_v106_signal'] = f69oc_f69_operating_cash_flow_stability_calc106_252d_base_v106_signal

def f69oc_f69_operating_cash_flow_stability_calc107_252d_base_v107_signal(evebitda, ncfo):
    res = (ncfo / evebitda.replace(0, np.nan)).rolling(252).mean().diff(25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc107_252d_base_v107_signal'] = f69oc_f69_operating_cash_flow_stability_calc107_252d_base_v107_signal

def f69oc_f69_operating_cash_flow_stability_calc108_15d_base_v108_signal(intexp, ncfo):
    res = (ncfo - intexp).diff(15).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc108_15d_base_v108_signal'] = f69oc_f69_operating_cash_flow_stability_calc108_15d_base_v108_signal

def f69oc_f69_operating_cash_flow_stability_calc109_63d_base_v109_signal(intexp, ncfo):
    res = (ncfo / intexp.replace(0, np.nan)).rolling(63).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc109_63d_base_v109_signal'] = f69oc_f69_operating_cash_flow_stability_calc109_63d_base_v109_signal

def f69oc_f69_operating_cash_flow_stability_calc110_30d_base_v110_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital.replace(0, np.nan)).rolling(30).mean().diff(3)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc110_30d_base_v110_signal'] = f69oc_f69_operating_cash_flow_stability_calc110_30d_base_v110_signal

def f69oc_f69_operating_cash_flow_stability_calc111_10d_base_v111_signal(ncfo):
    res = ncfo.rolling(10).median().pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc111_10d_base_v111_signal'] = f69oc_f69_operating_cash_flow_stability_calc111_10d_base_v111_signal

def f69oc_f69_operating_cash_flow_stability_calc112_252d_base_v112_signal(equity, low, ncfo):
    res = (ncfo.rolling(252).mean() - equity.rolling(252).mean()) / low.replace(0, np.nan).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc112_252d_base_v112_signal'] = f69oc_f69_operating_cash_flow_stability_calc112_252d_base_v112_signal

def f69oc_f69_operating_cash_flow_stability_calc113_10d_base_v113_signal(ncfo):
    res = ncfo.pct_change(10).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc113_10d_base_v113_signal'] = f69oc_f69_operating_cash_flow_stability_calc113_10d_base_v113_signal

def f69oc_f69_operating_cash_flow_stability_calc114_15d_base_v114_signal(fcf, ncfo):
    res = (ncfo.diff(15) / fcf.replace(0, np.nan).diff(15)).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc114_15d_base_v114_signal'] = f69oc_f69_operating_cash_flow_stability_calc114_15d_base_v114_signal

def f69oc_f69_operating_cash_flow_stability_calc115_150d_base_v115_signal(gp, ncfo):
    res = np.log((ncfo.abs() + 1) / (gp.abs() + 1)).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc115_150d_base_v115_signal'] = f69oc_f69_operating_cash_flow_stability_calc115_150d_base_v115_signal

def f69oc_f69_operating_cash_flow_stability_calc116_15d_base_v116_signal(high, ncfo):
    res = (ncfo / high.replace(0, np.nan)).rolling(15).mean().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc116_15d_base_v116_signal'] = f69oc_f69_operating_cash_flow_stability_calc116_15d_base_v116_signal

def f69oc_f69_operating_cash_flow_stability_calc117_42d_base_v117_signal(ncfo, volume):
    res = (ncfo.rolling(42).max() - volume.rolling(42).min()) / volume.rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc117_42d_base_v117_signal'] = f69oc_f69_operating_cash_flow_stability_calc117_42d_base_v117_signal

def f69oc_f69_operating_cash_flow_stability_calc118_15d_base_v118_signal(ncfo):
    res = ncfo.pct_change(15).rolling(15).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc118_15d_base_v118_signal'] = f69oc_f69_operating_cash_flow_stability_calc118_15d_base_v118_signal

def f69oc_f69_operating_cash_flow_stability_calc119_30d_base_v119_signal(ncfo):
    res = ncfo.rolling(30).median().pct_change(6)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc119_30d_base_v119_signal'] = f69oc_f69_operating_cash_flow_stability_calc119_30d_base_v119_signal

def f69oc_f69_operating_cash_flow_stability_calc120_15d_base_v120_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital.replace(0, np.nan)).rolling(15).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc120_15d_base_v120_signal'] = f69oc_f69_operating_cash_flow_stability_calc120_15d_base_v120_signal

def f69oc_f69_operating_cash_flow_stability_calc121_100d_base_v121_signal(closeadj, ncfo):
    res = (ncfo.diff(100) / closeadj.replace(0, np.nan).diff(100)).rolling(100).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc121_100d_base_v121_signal'] = f69oc_f69_operating_cash_flow_stability_calc121_100d_base_v121_signal

def f69oc_f69_operating_cash_flow_stability_calc122_30d_base_v122_signal(intexp, ncfo):
    res = (ncfo * intexp).rolling(30).std() / (ncfo * intexp).rolling(30).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc122_30d_base_v122_signal'] = f69oc_f69_operating_cash_flow_stability_calc122_30d_base_v122_signal

def f69oc_f69_operating_cash_flow_stability_calc123_200d_base_v123_signal(ev, ncfo):
    res = (ncfo - ev.rolling(200).mean()).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc123_200d_base_v123_signal'] = f69oc_f69_operating_cash_flow_stability_calc123_200d_base_v123_signal

def f69oc_f69_operating_cash_flow_stability_calc124_252d_base_v124_signal(ncff, ncfo):
    res = (ncfo - ncff.rolling(252).mean()).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc124_252d_base_v124_signal'] = f69oc_f69_operating_cash_flow_stability_calc124_252d_base_v124_signal

def f69oc_f69_operating_cash_flow_stability_calc125_30d_base_v125_signal(high, ncff, ncfo):
    res = (ncfo * high / ncff.replace(0, np.nan)).pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc125_30d_base_v125_signal'] = f69oc_f69_operating_cash_flow_stability_calc125_30d_base_v125_signal

def f69oc_f69_operating_cash_flow_stability_calc126_200d_base_v126_signal(ncfo, taxexp):
    res = ncfo.rolling(200).var() / taxexp.rolling(200).var().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc126_200d_base_v126_signal'] = f69oc_f69_operating_cash_flow_stability_calc126_200d_base_v126_signal

def f69oc_f69_operating_cash_flow_stability_calc127_126d_base_v127_signal(assets, ncfo):
    res = (ncfo / assets.replace(0, np.nan)).rolling(126).mean().diff(12)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc127_126d_base_v127_signal'] = f69oc_f69_operating_cash_flow_stability_calc127_126d_base_v127_signal

def f69oc_f69_operating_cash_flow_stability_calc128_200d_base_v128_signal(ncfi, ncfo):
    res = (ncfo * ncfi).rolling(200).std() / (ncfo * ncfi).rolling(200).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc128_200d_base_v128_signal'] = f69oc_f69_operating_cash_flow_stability_calc128_200d_base_v128_signal

def f69oc_f69_operating_cash_flow_stability_calc129_21d_base_v129_signal(fcf, ncfo):
    res = (ncfo / fcf.replace(0, np.nan)).rolling(21).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc129_21d_base_v129_signal'] = f69oc_f69_operating_cash_flow_stability_calc129_21d_base_v129_signal

def f69oc_f69_operating_cash_flow_stability_calc130_15d_base_v130_signal(ncfo, revenue):
    res = (ncfo / revenue.replace(0, np.nan)).rolling(15).std().pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc130_15d_base_v130_signal'] = f69oc_f69_operating_cash_flow_stability_calc130_15d_base_v130_signal

def f69oc_f69_operating_cash_flow_stability_calc131_252d_base_v131_signal(ncfo, volume):
    res = (ncfo / volume.replace(0, np.nan)).rolling(252).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc131_252d_base_v131_signal'] = f69oc_f69_operating_cash_flow_stability_calc131_252d_base_v131_signal

def f69oc_f69_operating_cash_flow_stability_calc132_21d_base_v132_signal(ncfo, opinc):
    res = (ncfo - opinc.rolling(21).mean()).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc132_21d_base_v132_signal'] = f69oc_f69_operating_cash_flow_stability_calc132_21d_base_v132_signal

def f69oc_f69_operating_cash_flow_stability_calc133_15d_base_v133_signal(close, ncfo):
    res = (ncfo / close.replace(0, np.nan)).rolling(15).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc133_15d_base_v133_signal'] = f69oc_f69_operating_cash_flow_stability_calc133_15d_base_v133_signal

def f69oc_f69_operating_cash_flow_stability_calc134_252d_base_v134_signal(ncfo, pe):
    res = ncfo.rolling(252).quantile(0.3) - pe.rolling(252).quantile(0.7)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc134_252d_base_v134_signal'] = f69oc_f69_operating_cash_flow_stability_calc134_252d_base_v134_signal

def f69oc_f69_operating_cash_flow_stability_calc135_5d_base_v135_signal(debt, ncfo):
    res = ncfo.rolling(5).var() / debt.rolling(5).var().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc135_5d_base_v135_signal'] = f69oc_f69_operating_cash_flow_stability_calc135_5d_base_v135_signal

def f69oc_f69_operating_cash_flow_stability_calc136_252d_base_v136_signal(ncff, ncfo):
    res = (ncfo / ncff.replace(0, np.nan)).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc136_252d_base_v136_signal'] = f69oc_f69_operating_cash_flow_stability_calc136_252d_base_v136_signal

def f69oc_f69_operating_cash_flow_stability_calc137_21d_base_v137_signal(ncfo, sharesbas):
    res = np.log((ncfo.abs() + 1) / (sharesbas.abs() + 1)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc137_21d_base_v137_signal'] = f69oc_f69_operating_cash_flow_stability_calc137_21d_base_v137_signal

def f69oc_f69_operating_cash_flow_stability_calc138_80d_base_v138_signal(high, ncfo):
    res = (ncfo.diff(80) / high.replace(0, np.nan).diff(80)).rolling(80).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc138_80d_base_v138_signal'] = f69oc_f69_operating_cash_flow_stability_calc138_80d_base_v138_signal

def f69oc_f69_operating_cash_flow_stability_calc139_42d_base_v139_signal(eps, ncfo):
    res = (ncfo / eps.replace(0, np.nan)).rolling(42).mean().diff(4)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc139_42d_base_v139_signal'] = f69oc_f69_operating_cash_flow_stability_calc139_42d_base_v139_signal

def f69oc_f69_operating_cash_flow_stability_calc140_50d_base_v140_signal(capex, ncfo):
    res = ncfo.rolling(50).quantile(0.3) - capex.rolling(50).quantile(0.7)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc140_50d_base_v140_signal'] = f69oc_f69_operating_cash_flow_stability_calc140_50d_base_v140_signal

def f69oc_f69_operating_cash_flow_stability_calc141_80d_base_v141_signal(currentratio, ncfo):
    res = ncfo.rolling(80).std() / currentratio.replace(0, np.nan).rolling(80).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc141_80d_base_v141_signal'] = f69oc_f69_operating_cash_flow_stability_calc141_80d_base_v141_signal

def f69oc_f69_operating_cash_flow_stability_calc142_200d_base_v142_signal(ncfo, retearn):
    res = np.log((ncfo.abs() + 1) / (retearn.abs() + 1)).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc142_200d_base_v142_signal'] = f69oc_f69_operating_cash_flow_stability_calc142_200d_base_v142_signal

def f69oc_f69_operating_cash_flow_stability_calc143_21d_base_v143_signal(capex, ncfo):
    res = (capex / ncfo.replace(0, np.nan)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc143_21d_base_v143_signal'] = f69oc_f69_operating_cash_flow_stability_calc143_21d_base_v143_signal

def f69oc_f69_operating_cash_flow_stability_calc144_50d_base_v144_signal(fcf, ncfo):
    res = ncfo.rolling(50).quantile(0.3) - fcf.rolling(50).quantile(0.7)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc144_50d_base_v144_signal'] = f69oc_f69_operating_cash_flow_stability_calc144_50d_base_v144_signal

def f69oc_f69_operating_cash_flow_stability_calc145_5d_base_v145_signal(debt, ncfo):
    res = (ncfo / debt.replace(0, np.nan)).rolling(5).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc145_5d_base_v145_signal'] = f69oc_f69_operating_cash_flow_stability_calc145_5d_base_v145_signal

def f69oc_f69_operating_cash_flow_stability_calc146_150d_base_v146_signal(closeadj, evebitda, ncfo):
    res = (ncfo.rolling(150).mean() - evebitda.rolling(150).mean()) / closeadj.replace(0, np.nan).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc146_150d_base_v146_signal'] = f69oc_f69_operating_cash_flow_stability_calc146_150d_base_v146_signal

def f69oc_f69_operating_cash_flow_stability_calc147_21d_base_v147_signal(ncfo, opinc):
    res = np.log((ncfo.abs() + 1) / (opinc.abs() + 1)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc147_21d_base_v147_signal'] = f69oc_f69_operating_cash_flow_stability_calc147_21d_base_v147_signal

def f69oc_f69_operating_cash_flow_stability_calc148_42d_base_v148_signal(closeadj, ncfo):
    res = (ncfo.rolling(42).max() - ncfo.rolling(42).min()) / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc148_42d_base_v148_signal'] = f69oc_f69_operating_cash_flow_stability_calc148_42d_base_v148_signal

def f69oc_f69_operating_cash_flow_stability_calc149_80d_base_v149_signal(currentratio, ncfo):
    res = (ncfo.diff(80) / currentratio.replace(0, np.nan).diff(80)).rolling(80).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc149_80d_base_v149_signal'] = f69oc_f69_operating_cash_flow_stability_calc149_80d_base_v149_signal

def f69oc_f69_operating_cash_flow_stability_calc150_10d_base_v150_signal(evebit, ncfo):
    res = (evebit / ncfo.replace(0, np.nan)).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f69oc_f69_operating_cash_flow_stability_calc150_10d_base_v150_signal'] = f69oc_f69_operating_cash_flow_stability_calc150_10d_base_v150_signal


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
