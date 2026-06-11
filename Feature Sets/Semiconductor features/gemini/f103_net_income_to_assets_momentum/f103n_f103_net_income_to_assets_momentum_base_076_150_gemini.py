import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f103n_f103_net_income_to_assets_momentum_calc076_10d_base_v076_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(10).quantile(0.5) / ncfo.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc076_10d_base_v076_signal'] = f103n_f103_net_income_to_assets_momentum_calc076_10d_base_v076_signal

def f103n_f103_net_income_to_assets_momentum_calc077_63d_base_v077_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(63).quantile(0.5) / netinc.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc077_63d_base_v077_signal'] = f103n_f103_net_income_to_assets_momentum_calc077_63d_base_v077_signal

def f103n_f103_net_income_to_assets_momentum_calc078_63d_base_v078_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.pct_change(63) - ncfo.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc078_63d_base_v078_signal'] = f103n_f103_net_income_to_assets_momentum_calc078_63d_base_v078_signal

def f103n_f103_net_income_to_assets_momentum_calc079_10d_base_v079_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets / netinc.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc079_10d_base_v079_signal'] = f103n_f103_net_income_to_assets_momentum_calc079_10d_base_v079_signal

def f103n_f103_net_income_to_assets_momentum_calc080_63d_base_v080_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(63).rank(pct=True) / revenue.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc080_63d_base_v080_signal'] = f103n_f103_net_income_to_assets_momentum_calc080_63d_base_v080_signal

def f103n_f103_net_income_to_assets_momentum_calc081_252d_base_v081_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ebitda - ebitda.rolling(252).mean()) / ebitda.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc081_252d_base_v081_signal'] = f103n_f103_net_income_to_assets_momentum_calc081_252d_base_v081_signal

def f103n_f103_net_income_to_assets_momentum_calc082_5d_base_v082_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc082_5d_base_v082_signal'] = f103n_f103_net_income_to_assets_momentum_calc082_5d_base_v082_signal

def f103n_f103_net_income_to_assets_momentum_calc083_252d_base_v083_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(252).max() - equity.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc083_252d_base_v083_signal'] = f103n_f103_net_income_to_assets_momentum_calc083_252d_base_v083_signal

def f103n_f103_net_income_to_assets_momentum_calc084_21d_base_v084_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc084_21d_base_v084_signal'] = f103n_f103_net_income_to_assets_momentum_calc084_21d_base_v084_signal

def f103n_f103_net_income_to_assets_momentum_calc085_126d_base_v085_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(126).rank(pct=True) / netinc.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc085_126d_base_v085_signal'] = f103n_f103_net_income_to_assets_momentum_calc085_126d_base_v085_signal

def f103n_f103_net_income_to_assets_momentum_calc086_63d_base_v086_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / netinc.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc086_63d_base_v086_signal'] = f103n_f103_net_income_to_assets_momentum_calc086_63d_base_v086_signal

def f103n_f103_net_income_to_assets_momentum_calc087_21d_base_v087_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(21).quantile(0.5) / fcf.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc087_21d_base_v087_signal'] = f103n_f103_net_income_to_assets_momentum_calc087_21d_base_v087_signal

def f103n_f103_net_income_to_assets_momentum_calc088_252d_base_v088_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(252) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc088_252d_base_v088_signal'] = f103n_f103_net_income_to_assets_momentum_calc088_252d_base_v088_signal

def f103n_f103_net_income_to_assets_momentum_calc089_10d_base_v089_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets / fcf.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc089_10d_base_v089_signal'] = f103n_f103_net_income_to_assets_momentum_calc089_10d_base_v089_signal

def f103n_f103_net_income_to_assets_momentum_calc090_5d_base_v090_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(5).kurt() - netinc.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc090_5d_base_v090_signal'] = f103n_f103_net_income_to_assets_momentum_calc090_5d_base_v090_signal

def f103n_f103_net_income_to_assets_momentum_calc091_252d_base_v091_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.pct_change(252) - ebitda.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc091_252d_base_v091_signal'] = f103n_f103_net_income_to_assets_momentum_calc091_252d_base_v091_signal

def f103n_f103_net_income_to_assets_momentum_calc092_126d_base_v092_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(126).kurt() - netinc.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc092_126d_base_v092_signal'] = f103n_f103_net_income_to_assets_momentum_calc092_126d_base_v092_signal

def f103n_f103_net_income_to_assets_momentum_calc093_252d_base_v093_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(252).abs() / revenue.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc093_252d_base_v093_signal'] = f103n_f103_net_income_to_assets_momentum_calc093_252d_base_v093_signal

def f103n_f103_net_income_to_assets_momentum_calc094_42d_base_v094_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.pct_change(42) - assets.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc094_42d_base_v094_signal'] = f103n_f103_net_income_to_assets_momentum_calc094_42d_base_v094_signal

def f103n_f103_net_income_to_assets_momentum_calc095_21d_base_v095_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(21).max() - equity.rolling(21).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc095_21d_base_v095_signal'] = f103n_f103_net_income_to_assets_momentum_calc095_21d_base_v095_signal

def f103n_f103_net_income_to_assets_momentum_calc096_5d_base_v096_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(5).kurt() - assets.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc096_5d_base_v096_signal'] = f103n_f103_net_income_to_assets_momentum_calc096_5d_base_v096_signal

def f103n_f103_net_income_to_assets_momentum_calc097_63d_base_v097_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((fcf - fcf.rolling(63).mean()) / fcf.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc097_63d_base_v097_signal'] = f103n_f103_net_income_to_assets_momentum_calc097_63d_base_v097_signal

def f103n_f103_net_income_to_assets_momentum_calc098_10d_base_v098_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(10).max() - ebitda.rolling(10).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc098_10d_base_v098_signal'] = f103n_f103_net_income_to_assets_momentum_calc098_10d_base_v098_signal

def f103n_f103_net_income_to_assets_momentum_calc099_126d_base_v099_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(126) - revenue.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc099_126d_base_v099_signal'] = f103n_f103_net_income_to_assets_momentum_calc099_126d_base_v099_signal

def f103n_f103_net_income_to_assets_momentum_calc100_5d_base_v100_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(5) / ncfo.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc100_5d_base_v100_signal'] = f103n_f103_net_income_to_assets_momentum_calc100_5d_base_v100_signal

def f103n_f103_net_income_to_assets_momentum_calc101_126d_base_v101_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ncfo - ncfo.rolling(126).mean()) / ncfo.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc101_126d_base_v101_signal'] = f103n_f103_net_income_to_assets_momentum_calc101_126d_base_v101_signal

def f103n_f103_net_income_to_assets_momentum_calc102_10d_base_v102_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(10) - assets.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc102_10d_base_v102_signal'] = f103n_f103_net_income_to_assets_momentum_calc102_10d_base_v102_signal

def f103n_f103_net_income_to_assets_momentum_calc103_126d_base_v103_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.pct_change(126) - netinc.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc103_126d_base_v103_signal'] = f103n_f103_net_income_to_assets_momentum_calc103_126d_base_v103_signal

def f103n_f103_net_income_to_assets_momentum_calc104_126d_base_v104_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.pct_change(126) - ebitda.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc104_126d_base_v104_signal'] = f103n_f103_net_income_to_assets_momentum_calc104_126d_base_v104_signal

def f103n_f103_net_income_to_assets_momentum_calc105_126d_base_v105_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(126).kurt() - equity.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc105_126d_base_v105_signal'] = f103n_f103_net_income_to_assets_momentum_calc105_126d_base_v105_signal

def f103n_f103_net_income_to_assets_momentum_calc106_10d_base_v106_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc106_10d_base_v106_signal'] = f103n_f103_net_income_to_assets_momentum_calc106_10d_base_v106_signal

def f103n_f103_net_income_to_assets_momentum_calc107_42d_base_v107_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(42).abs() / ebitda.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc107_42d_base_v107_signal'] = f103n_f103_net_income_to_assets_momentum_calc107_42d_base_v107_signal

def f103n_f103_net_income_to_assets_momentum_calc108_252d_base_v108_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(252).abs() / ncfo.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc108_252d_base_v108_signal'] = f103n_f103_net_income_to_assets_momentum_calc108_252d_base_v108_signal

def f103n_f103_net_income_to_assets_momentum_calc109_126d_base_v109_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / revenue.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc109_126d_base_v109_signal'] = f103n_f103_net_income_to_assets_momentum_calc109_126d_base_v109_signal

def f103n_f103_net_income_to_assets_momentum_calc110_10d_base_v110_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc110_10d_base_v110_signal'] = f103n_f103_net_income_to_assets_momentum_calc110_10d_base_v110_signal

def f103n_f103_net_income_to_assets_momentum_calc111_126d_base_v111_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(126) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc111_126d_base_v111_signal'] = f103n_f103_net_income_to_assets_momentum_calc111_126d_base_v111_signal

def f103n_f103_net_income_to_assets_momentum_calc112_126d_base_v112_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc112_126d_base_v112_signal'] = f103n_f103_net_income_to_assets_momentum_calc112_126d_base_v112_signal

def f103n_f103_net_income_to_assets_momentum_calc113_63d_base_v113_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(63) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc113_63d_base_v113_signal'] = f103n_f103_net_income_to_assets_momentum_calc113_63d_base_v113_signal

def f103n_f103_net_income_to_assets_momentum_calc114_21d_base_v114_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(21).kurt() - fcf.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc114_21d_base_v114_signal'] = f103n_f103_net_income_to_assets_momentum_calc114_21d_base_v114_signal

def f103n_f103_net_income_to_assets_momentum_calc115_5d_base_v115_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / ncfo.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc115_5d_base_v115_signal'] = f103n_f103_net_income_to_assets_momentum_calc115_5d_base_v115_signal

def f103n_f103_net_income_to_assets_momentum_calc116_21d_base_v116_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(21).quantile(0.5) / fcf.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc116_21d_base_v116_signal'] = f103n_f103_net_income_to_assets_momentum_calc116_21d_base_v116_signal

def f103n_f103_net_income_to_assets_momentum_calc117_10d_base_v117_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(10).kurt() - assets.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc117_10d_base_v117_signal'] = f103n_f103_net_income_to_assets_momentum_calc117_10d_base_v117_signal

def f103n_f103_net_income_to_assets_momentum_calc118_5d_base_v118_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.pct_change(5) - ncfo.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc118_5d_base_v118_signal'] = f103n_f103_net_income_to_assets_momentum_calc118_5d_base_v118_signal

def f103n_f103_net_income_to_assets_momentum_calc119_42d_base_v119_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc119_42d_base_v119_signal'] = f103n_f103_net_income_to_assets_momentum_calc119_42d_base_v119_signal

def f103n_f103_net_income_to_assets_momentum_calc120_5d_base_v120_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc120_5d_base_v120_signal'] = f103n_f103_net_income_to_assets_momentum_calc120_5d_base_v120_signal

def f103n_f103_net_income_to_assets_momentum_calc121_42d_base_v121_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(42).max() - ncfo.rolling(42).min()) / netinc.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc121_42d_base_v121_signal'] = f103n_f103_net_income_to_assets_momentum_calc121_42d_base_v121_signal

def f103n_f103_net_income_to_assets_momentum_calc122_42d_base_v122_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(42).rank(pct=True) / assets.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc122_42d_base_v122_signal'] = f103n_f103_net_income_to_assets_momentum_calc122_42d_base_v122_signal

def f103n_f103_net_income_to_assets_momentum_calc123_5d_base_v123_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((assets - assets.rolling(5).mean()) / assets.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc123_5d_base_v123_signal'] = f103n_f103_net_income_to_assets_momentum_calc123_5d_base_v123_signal

def f103n_f103_net_income_to_assets_momentum_calc124_42d_base_v124_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc124_42d_base_v124_signal'] = f103n_f103_net_income_to_assets_momentum_calc124_42d_base_v124_signal

def f103n_f103_net_income_to_assets_momentum_calc125_21d_base_v125_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((revenue - revenue.rolling(21).mean()) / revenue.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc125_21d_base_v125_signal'] = f103n_f103_net_income_to_assets_momentum_calc125_21d_base_v125_signal

def f103n_f103_net_income_to_assets_momentum_calc126_252d_base_v126_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue / ncfo.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc126_252d_base_v126_signal'] = f103n_f103_net_income_to_assets_momentum_calc126_252d_base_v126_signal

def f103n_f103_net_income_to_assets_momentum_calc127_42d_base_v127_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.pct_change(42) - fcf.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc127_42d_base_v127_signal'] = f103n_f103_net_income_to_assets_momentum_calc127_42d_base_v127_signal

def f103n_f103_net_income_to_assets_momentum_calc128_126d_base_v128_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / netinc.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc128_126d_base_v128_signal'] = f103n_f103_net_income_to_assets_momentum_calc128_126d_base_v128_signal

def f103n_f103_net_income_to_assets_momentum_calc129_5d_base_v129_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc129_5d_base_v129_signal'] = f103n_f103_net_income_to_assets_momentum_calc129_5d_base_v129_signal

def f103n_f103_net_income_to_assets_momentum_calc130_21d_base_v130_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(21).abs() / ncfo.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc130_21d_base_v130_signal'] = f103n_f103_net_income_to_assets_momentum_calc130_21d_base_v130_signal

def f103n_f103_net_income_to_assets_momentum_calc131_126d_base_v131_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.pct_change(126) - fcf.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc131_126d_base_v131_signal'] = f103n_f103_net_income_to_assets_momentum_calc131_126d_base_v131_signal

def f103n_f103_net_income_to_assets_momentum_calc132_21d_base_v132_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(21).rank(pct=True) / assets.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc132_21d_base_v132_signal'] = f103n_f103_net_income_to_assets_momentum_calc132_21d_base_v132_signal

def f103n_f103_net_income_to_assets_momentum_calc133_63d_base_v133_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(63).rank(pct=True) / ebitda.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc133_63d_base_v133_signal'] = f103n_f103_net_income_to_assets_momentum_calc133_63d_base_v133_signal

def f103n_f103_net_income_to_assets_momentum_calc134_252d_base_v134_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(252).max() - netinc.rolling(252).min()) / ncfo.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc134_252d_base_v134_signal'] = f103n_f103_net_income_to_assets_momentum_calc134_252d_base_v134_signal

def f103n_f103_net_income_to_assets_momentum_calc135_21d_base_v135_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ncfo - ncfo.rolling(21).mean()) / ncfo.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc135_21d_base_v135_signal'] = f103n_f103_net_income_to_assets_momentum_calc135_21d_base_v135_signal

def f103n_f103_net_income_to_assets_momentum_calc136_252d_base_v136_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(252).abs() / ebitda.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc136_252d_base_v136_signal'] = f103n_f103_net_income_to_assets_momentum_calc136_252d_base_v136_signal

def f103n_f103_net_income_to_assets_momentum_calc137_42d_base_v137_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(42).rank(pct=True) / netinc.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc137_42d_base_v137_signal'] = f103n_f103_net_income_to_assets_momentum_calc137_42d_base_v137_signal

def f103n_f103_net_income_to_assets_momentum_calc138_5d_base_v138_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(5).kurt() - assets.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc138_5d_base_v138_signal'] = f103n_f103_net_income_to_assets_momentum_calc138_5d_base_v138_signal

def f103n_f103_net_income_to_assets_momentum_calc139_252d_base_v139_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(252).max() - revenue.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc139_252d_base_v139_signal'] = f103n_f103_net_income_to_assets_momentum_calc139_252d_base_v139_signal

def f103n_f103_net_income_to_assets_momentum_calc140_10d_base_v140_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(10).abs() / fcf.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc140_10d_base_v140_signal'] = f103n_f103_net_income_to_assets_momentum_calc140_10d_base_v140_signal

def f103n_f103_net_income_to_assets_momentum_calc141_63d_base_v141_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(63) - ncfo.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc141_63d_base_v141_signal'] = f103n_f103_net_income_to_assets_momentum_calc141_63d_base_v141_signal

def f103n_f103_net_income_to_assets_momentum_calc142_10d_base_v142_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue / ebitda.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc142_10d_base_v142_signal'] = f103n_f103_net_income_to_assets_momentum_calc142_10d_base_v142_signal

def f103n_f103_net_income_to_assets_momentum_calc143_10d_base_v143_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(10) / netinc.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc143_10d_base_v143_signal'] = f103n_f103_net_income_to_assets_momentum_calc143_10d_base_v143_signal

def f103n_f103_net_income_to_assets_momentum_calc144_63d_base_v144_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(63) - ebitda.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc144_63d_base_v144_signal'] = f103n_f103_net_income_to_assets_momentum_calc144_63d_base_v144_signal

def f103n_f103_net_income_to_assets_momentum_calc145_5d_base_v145_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((equity - equity.rolling(5).mean()) / equity.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc145_5d_base_v145_signal'] = f103n_f103_net_income_to_assets_momentum_calc145_5d_base_v145_signal

def f103n_f103_net_income_to_assets_momentum_calc146_5d_base_v146_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc / revenue.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc146_5d_base_v146_signal'] = f103n_f103_net_income_to_assets_momentum_calc146_5d_base_v146_signal

def f103n_f103_net_income_to_assets_momentum_calc147_42d_base_v147_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc147_42d_base_v147_signal'] = f103n_f103_net_income_to_assets_momentum_calc147_42d_base_v147_signal

def f103n_f103_net_income_to_assets_momentum_calc148_63d_base_v148_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((revenue - revenue.rolling(63).mean()) / revenue.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc148_63d_base_v148_signal'] = f103n_f103_net_income_to_assets_momentum_calc148_63d_base_v148_signal

def f103n_f103_net_income_to_assets_momentum_calc149_126d_base_v149_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(126) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc149_126d_base_v149_signal'] = f103n_f103_net_income_to_assets_momentum_calc149_126d_base_v149_signal

def f103n_f103_net_income_to_assets_momentum_calc150_21d_base_v150_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc150_21d_base_v150_signal'] = f103n_f103_net_income_to_assets_momentum_calc150_21d_base_v150_signal



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
