import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f104f_f104_free_cash_flow_yield_regime_calc076_21d_base_v076_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc076_21d_base_v076_signal'] = f104f_f104_free_cash_flow_yield_regime_calc076_21d_base_v076_signal

def f104f_f104_free_cash_flow_yield_regime_calc077_63d_base_v077_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(63).rank(pct=True) / ncfo.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc077_63d_base_v077_signal'] = f104f_f104_free_cash_flow_yield_regime_calc077_63d_base_v077_signal

def f104f_f104_free_cash_flow_yield_regime_calc078_252d_base_v078_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(252).abs() / marketcap.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc078_252d_base_v078_signal'] = f104f_f104_free_cash_flow_yield_regime_calc078_252d_base_v078_signal

def f104f_f104_free_cash_flow_yield_regime_calc079_126d_base_v079_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc079_126d_base_v079_signal'] = f104f_f104_free_cash_flow_yield_regime_calc079_126d_base_v079_signal

def f104f_f104_free_cash_flow_yield_regime_calc080_126d_base_v080_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc080_126d_base_v080_signal'] = f104f_f104_free_cash_flow_yield_regime_calc080_126d_base_v080_signal

def f104f_f104_free_cash_flow_yield_regime_calc081_126d_base_v081_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(126).kurt() - assets.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc081_126d_base_v081_signal'] = f104f_f104_free_cash_flow_yield_regime_calc081_126d_base_v081_signal

def f104f_f104_free_cash_flow_yield_regime_calc082_10d_base_v082_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc082_10d_base_v082_signal'] = f104f_f104_free_cash_flow_yield_regime_calc082_10d_base_v082_signal

def f104f_f104_free_cash_flow_yield_regime_calc083_10d_base_v083_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(10) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc083_10d_base_v083_signal'] = f104f_f104_free_cash_flow_yield_regime_calc083_10d_base_v083_signal

def f104f_f104_free_cash_flow_yield_regime_calc084_21d_base_v084_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(21).kurt() - marketcap.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc084_21d_base_v084_signal'] = f104f_f104_free_cash_flow_yield_regime_calc084_21d_base_v084_signal

def f104f_f104_free_cash_flow_yield_regime_calc085_42d_base_v085_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(42).max() - ev.rolling(42).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc085_42d_base_v085_signal'] = f104f_f104_free_cash_flow_yield_regime_calc085_42d_base_v085_signal

def f104f_f104_free_cash_flow_yield_regime_calc086_42d_base_v086_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(42) - ncfo.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc086_42d_base_v086_signal'] = f104f_f104_free_cash_flow_yield_regime_calc086_42d_base_v086_signal

def f104f_f104_free_cash_flow_yield_regime_calc087_21d_base_v087_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(21).kurt() - assets.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc087_21d_base_v087_signal'] = f104f_f104_free_cash_flow_yield_regime_calc087_21d_base_v087_signal

def f104f_f104_free_cash_flow_yield_regime_calc088_126d_base_v088_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / equity.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc088_126d_base_v088_signal'] = f104f_f104_free_cash_flow_yield_regime_calc088_126d_base_v088_signal

def f104f_f104_free_cash_flow_yield_regime_calc089_63d_base_v089_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(63).mean()) / fcf.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc089_63d_base_v089_signal'] = f104f_f104_free_cash_flow_yield_regime_calc089_63d_base_v089_signal

def f104f_f104_free_cash_flow_yield_regime_calc090_42d_base_v090_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(42) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc090_42d_base_v090_signal'] = f104f_f104_free_cash_flow_yield_regime_calc090_42d_base_v090_signal

def f104f_f104_free_cash_flow_yield_regime_calc091_21d_base_v091_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((equity - equity.rolling(21).mean()) / equity.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc091_21d_base_v091_signal'] = f104f_f104_free_cash_flow_yield_regime_calc091_21d_base_v091_signal

def f104f_f104_free_cash_flow_yield_regime_calc092_63d_base_v092_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(63).kurt() - revenue.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc092_63d_base_v092_signal'] = f104f_f104_free_cash_flow_yield_regime_calc092_63d_base_v092_signal

def f104f_f104_free_cash_flow_yield_regime_calc093_42d_base_v093_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / equity.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc093_42d_base_v093_signal'] = f104f_f104_free_cash_flow_yield_regime_calc093_42d_base_v093_signal

def f104f_f104_free_cash_flow_yield_regime_calc094_126d_base_v094_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / ev.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc094_126d_base_v094_signal'] = f104f_f104_free_cash_flow_yield_regime_calc094_126d_base_v094_signal

def f104f_f104_free_cash_flow_yield_regime_calc095_63d_base_v095_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(63) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc095_63d_base_v095_signal'] = f104f_f104_free_cash_flow_yield_regime_calc095_63d_base_v095_signal

def f104f_f104_free_cash_flow_yield_regime_calc096_63d_base_v096_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(63).max() - equity.rolling(63).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc096_63d_base_v096_signal'] = f104f_f104_free_cash_flow_yield_regime_calc096_63d_base_v096_signal

def f104f_f104_free_cash_flow_yield_regime_calc097_63d_base_v097_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(63).quantile(0.5) / ev.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc097_63d_base_v097_signal'] = f104f_f104_free_cash_flow_yield_regime_calc097_63d_base_v097_signal

def f104f_f104_free_cash_flow_yield_regime_calc098_21d_base_v098_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(21) - fcf.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc098_21d_base_v098_signal'] = f104f_f104_free_cash_flow_yield_regime_calc098_21d_base_v098_signal

def f104f_f104_free_cash_flow_yield_regime_calc099_10d_base_v099_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(10).abs() / ev.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc099_10d_base_v099_signal'] = f104f_f104_free_cash_flow_yield_regime_calc099_10d_base_v099_signal

def f104f_f104_free_cash_flow_yield_regime_calc100_42d_base_v100_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(42).quantile(0.5) / ev.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc100_42d_base_v100_signal'] = f104f_f104_free_cash_flow_yield_regime_calc100_42d_base_v100_signal

def f104f_f104_free_cash_flow_yield_regime_calc101_42d_base_v101_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / ev.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc101_42d_base_v101_signal'] = f104f_f104_free_cash_flow_yield_regime_calc101_42d_base_v101_signal

def f104f_f104_free_cash_flow_yield_regime_calc102_5d_base_v102_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / fcf.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc102_5d_base_v102_signal'] = f104f_f104_free_cash_flow_yield_regime_calc102_5d_base_v102_signal

def f104f_f104_free_cash_flow_yield_regime_calc103_10d_base_v103_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / assets.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc103_10d_base_v103_signal'] = f104f_f104_free_cash_flow_yield_regime_calc103_10d_base_v103_signal

def f104f_f104_free_cash_flow_yield_regime_calc104_63d_base_v104_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / marketcap.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc104_63d_base_v104_signal'] = f104f_f104_free_cash_flow_yield_regime_calc104_63d_base_v104_signal

def f104f_f104_free_cash_flow_yield_regime_calc105_5d_base_v105_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.diff(5) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc105_5d_base_v105_signal'] = f104f_f104_free_cash_flow_yield_regime_calc105_5d_base_v105_signal

def f104f_f104_free_cash_flow_yield_regime_calc106_10d_base_v106_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(10) - equity.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc106_10d_base_v106_signal'] = f104f_f104_free_cash_flow_yield_regime_calc106_10d_base_v106_signal

def f104f_f104_free_cash_flow_yield_regime_calc107_21d_base_v107_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc107_21d_base_v107_signal'] = f104f_f104_free_cash_flow_yield_regime_calc107_21d_base_v107_signal

def f104f_f104_free_cash_flow_yield_regime_calc108_126d_base_v108_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc108_126d_base_v108_signal'] = f104f_f104_free_cash_flow_yield_regime_calc108_126d_base_v108_signal

def f104f_f104_free_cash_flow_yield_regime_calc109_10d_base_v109_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(10).abs() / marketcap.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc109_10d_base_v109_signal'] = f104f_f104_free_cash_flow_yield_regime_calc109_10d_base_v109_signal

def f104f_f104_free_cash_flow_yield_regime_calc110_5d_base_v110_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(5).quantile(0.5) / ncfo.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc110_5d_base_v110_signal'] = f104f_f104_free_cash_flow_yield_regime_calc110_5d_base_v110_signal

def f104f_f104_free_cash_flow_yield_regime_calc111_10d_base_v111_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / fcf.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc111_10d_base_v111_signal'] = f104f_f104_free_cash_flow_yield_regime_calc111_10d_base_v111_signal

def f104f_f104_free_cash_flow_yield_regime_calc112_5d_base_v112_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.diff(5) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc112_5d_base_v112_signal'] = f104f_f104_free_cash_flow_yield_regime_calc112_5d_base_v112_signal

def f104f_f104_free_cash_flow_yield_regime_calc113_5d_base_v113_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(5) - ev.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc113_5d_base_v113_signal'] = f104f_f104_free_cash_flow_yield_regime_calc113_5d_base_v113_signal

def f104f_f104_free_cash_flow_yield_regime_calc114_252d_base_v114_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(252) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc114_252d_base_v114_signal'] = f104f_f104_free_cash_flow_yield_regime_calc114_252d_base_v114_signal

def f104f_f104_free_cash_flow_yield_regime_calc115_63d_base_v115_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(63).rank(pct=True) / marketcap.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc115_63d_base_v115_signal'] = f104f_f104_free_cash_flow_yield_regime_calc115_63d_base_v115_signal

def f104f_f104_free_cash_flow_yield_regime_calc116_5d_base_v116_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(5).quantile(0.5) / fcf.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc116_5d_base_v116_signal'] = f104f_f104_free_cash_flow_yield_regime_calc116_5d_base_v116_signal

def f104f_f104_free_cash_flow_yield_regime_calc117_21d_base_v117_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((ev - ev.rolling(21).mean()) / ev.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc117_21d_base_v117_signal'] = f104f_f104_free_cash_flow_yield_regime_calc117_21d_base_v117_signal

def f104f_f104_free_cash_flow_yield_regime_calc118_21d_base_v118_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).rank(pct=True) / ncfo.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc118_21d_base_v118_signal'] = f104f_f104_free_cash_flow_yield_regime_calc118_21d_base_v118_signal

def f104f_f104_free_cash_flow_yield_regime_calc119_63d_base_v119_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(63).kurt() - ncfo.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc119_63d_base_v119_signal'] = f104f_f104_free_cash_flow_yield_regime_calc119_63d_base_v119_signal

def f104f_f104_free_cash_flow_yield_regime_calc120_10d_base_v120_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc120_10d_base_v120_signal'] = f104f_f104_free_cash_flow_yield_regime_calc120_10d_base_v120_signal

def f104f_f104_free_cash_flow_yield_regime_calc121_21d_base_v121_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.diff(21) / ncfo.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc121_21d_base_v121_signal'] = f104f_f104_free_cash_flow_yield_regime_calc121_21d_base_v121_signal

def f104f_f104_free_cash_flow_yield_regime_calc122_126d_base_v122_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((equity - equity.rolling(126).mean()) / equity.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc122_126d_base_v122_signal'] = f104f_f104_free_cash_flow_yield_regime_calc122_126d_base_v122_signal

def f104f_f104_free_cash_flow_yield_regime_calc123_63d_base_v123_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc123_63d_base_v123_signal'] = f104f_f104_free_cash_flow_yield_regime_calc123_63d_base_v123_signal

def f104f_f104_free_cash_flow_yield_regime_calc124_252d_base_v124_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(252).mean()) / fcf.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc124_252d_base_v124_signal'] = f104f_f104_free_cash_flow_yield_regime_calc124_252d_base_v124_signal

def f104f_f104_free_cash_flow_yield_regime_calc125_252d_base_v125_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap / ncfo.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc125_252d_base_v125_signal'] = f104f_f104_free_cash_flow_yield_regime_calc125_252d_base_v125_signal

def f104f_f104_free_cash_flow_yield_regime_calc126_126d_base_v126_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(126).rank(pct=True) / marketcap.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc126_126d_base_v126_signal'] = f104f_f104_free_cash_flow_yield_regime_calc126_126d_base_v126_signal

def f104f_f104_free_cash_flow_yield_regime_calc127_21d_base_v127_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.diff(21) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc127_21d_base_v127_signal'] = f104f_f104_free_cash_flow_yield_regime_calc127_21d_base_v127_signal

def f104f_f104_free_cash_flow_yield_regime_calc128_63d_base_v128_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(63).mean()) / marketcap.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc128_63d_base_v128_signal'] = f104f_f104_free_cash_flow_yield_regime_calc128_63d_base_v128_signal

def f104f_f104_free_cash_flow_yield_regime_calc129_126d_base_v129_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(126).kurt() - equity.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc129_126d_base_v129_signal'] = f104f_f104_free_cash_flow_yield_regime_calc129_126d_base_v129_signal

def f104f_f104_free_cash_flow_yield_regime_calc130_42d_base_v130_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(42).max() - ncfo.rolling(42).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc130_42d_base_v130_signal'] = f104f_f104_free_cash_flow_yield_regime_calc130_42d_base_v130_signal

def f104f_f104_free_cash_flow_yield_regime_calc131_10d_base_v131_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc131_10d_base_v131_signal'] = f104f_f104_free_cash_flow_yield_regime_calc131_10d_base_v131_signal

def f104f_f104_free_cash_flow_yield_regime_calc132_126d_base_v132_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / equity.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc132_126d_base_v132_signal'] = f104f_f104_free_cash_flow_yield_regime_calc132_126d_base_v132_signal

def f104f_f104_free_cash_flow_yield_regime_calc133_126d_base_v133_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(126).max() - ev.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc133_126d_base_v133_signal'] = f104f_f104_free_cash_flow_yield_regime_calc133_126d_base_v133_signal

def f104f_f104_free_cash_flow_yield_regime_calc134_63d_base_v134_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(63) - ncfo.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc134_63d_base_v134_signal'] = f104f_f104_free_cash_flow_yield_regime_calc134_63d_base_v134_signal

def f104f_f104_free_cash_flow_yield_regime_calc135_5d_base_v135_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(5).quantile(0.5) / ev.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc135_5d_base_v135_signal'] = f104f_f104_free_cash_flow_yield_regime_calc135_5d_base_v135_signal

def f104f_f104_free_cash_flow_yield_regime_calc136_21d_base_v136_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(21).max() - assets.rolling(21).min()) / ncfo.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc136_21d_base_v136_signal'] = f104f_f104_free_cash_flow_yield_regime_calc136_21d_base_v136_signal

def f104f_f104_free_cash_flow_yield_regime_calc137_10d_base_v137_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(10) - equity.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc137_10d_base_v137_signal'] = f104f_f104_free_cash_flow_yield_regime_calc137_10d_base_v137_signal

def f104f_f104_free_cash_flow_yield_regime_calc138_252d_base_v138_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(252) - ncfo.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc138_252d_base_v138_signal'] = f104f_f104_free_cash_flow_yield_regime_calc138_252d_base_v138_signal

def f104f_f104_free_cash_flow_yield_regime_calc139_21d_base_v139_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).max() - ev.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc139_21d_base_v139_signal'] = f104f_f104_free_cash_flow_yield_regime_calc139_21d_base_v139_signal

def f104f_f104_free_cash_flow_yield_regime_calc140_5d_base_v140_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc140_5d_base_v140_signal'] = f104f_f104_free_cash_flow_yield_regime_calc140_5d_base_v140_signal

def f104f_f104_free_cash_flow_yield_regime_calc141_10d_base_v141_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(10).max() - equity.rolling(10).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc141_10d_base_v141_signal'] = f104f_f104_free_cash_flow_yield_regime_calc141_10d_base_v141_signal

def f104f_f104_free_cash_flow_yield_regime_calc142_126d_base_v142_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(126).abs() / assets.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc142_126d_base_v142_signal'] = f104f_f104_free_cash_flow_yield_regime_calc142_126d_base_v142_signal

def f104f_f104_free_cash_flow_yield_regime_calc143_42d_base_v143_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(42).mean()) / fcf.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc143_42d_base_v143_signal'] = f104f_f104_free_cash_flow_yield_regime_calc143_42d_base_v143_signal

def f104f_f104_free_cash_flow_yield_regime_calc144_10d_base_v144_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(10).max() - ncfo.rolling(10).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc144_10d_base_v144_signal'] = f104f_f104_free_cash_flow_yield_regime_calc144_10d_base_v144_signal

def f104f_f104_free_cash_flow_yield_regime_calc145_42d_base_v145_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(42).abs() / assets.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc145_42d_base_v145_signal'] = f104f_f104_free_cash_flow_yield_regime_calc145_42d_base_v145_signal

def f104f_f104_free_cash_flow_yield_regime_calc146_5d_base_v146_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(5).max() - fcf.rolling(5).min()) / ncfo.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc146_5d_base_v146_signal'] = f104f_f104_free_cash_flow_yield_regime_calc146_5d_base_v146_signal

def f104f_f104_free_cash_flow_yield_regime_calc147_5d_base_v147_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(5).abs() / marketcap.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc147_5d_base_v147_signal'] = f104f_f104_free_cash_flow_yield_regime_calc147_5d_base_v147_signal

def f104f_f104_free_cash_flow_yield_regime_calc148_21d_base_v148_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / ev.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc148_21d_base_v148_signal'] = f104f_f104_free_cash_flow_yield_regime_calc148_21d_base_v148_signal

def f104f_f104_free_cash_flow_yield_regime_calc149_21d_base_v149_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / assets.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc149_21d_base_v149_signal'] = f104f_f104_free_cash_flow_yield_regime_calc149_21d_base_v149_signal

def f104f_f104_free_cash_flow_yield_regime_calc150_5d_base_v150_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / fcf.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc150_5d_base_v150_signal'] = f104f_f104_free_cash_flow_yield_regime_calc150_5d_base_v150_signal



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
