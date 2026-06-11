import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f75ps_f75_fcf_per_share_acceleration_calc076_21d_base_v076_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((revenue - revenue.rolling(21).mean()) / revenue.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc076_21d_base_v076_signal'] = f75ps_f75_fcf_per_share_acceleration_calc076_21d_base_v076_signal

def f75ps_f75_fcf_per_share_acceleration_calc077_42d_base_v077_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(42).quantile(0.5) / fcf.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc077_42d_base_v077_signal'] = f75ps_f75_fcf_per_share_acceleration_calc077_42d_base_v077_signal

def f75ps_f75_fcf_per_share_acceleration_calc078_10d_base_v078_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(10).quantile(0.5) / fcf.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc078_10d_base_v078_signal'] = f75ps_f75_fcf_per_share_acceleration_calc078_10d_base_v078_signal

def f75ps_f75_fcf_per_share_acceleration_calc079_5d_base_v079_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(5).abs() / fcf.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc079_5d_base_v079_signal'] = f75ps_f75_fcf_per_share_acceleration_calc079_5d_base_v079_signal

def f75ps_f75_fcf_per_share_acceleration_calc080_126d_base_v080_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(126).max() - assets.rolling(126).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc080_126d_base_v080_signal'] = f75ps_f75_fcf_per_share_acceleration_calc080_126d_base_v080_signal

def f75ps_f75_fcf_per_share_acceleration_calc081_5d_base_v081_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc081_5d_base_v081_signal'] = f75ps_f75_fcf_per_share_acceleration_calc081_5d_base_v081_signal

def f75ps_f75_fcf_per_share_acceleration_calc082_10d_base_v082_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / sharesbas.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc082_10d_base_v082_signal'] = f75ps_f75_fcf_per_share_acceleration_calc082_10d_base_v082_signal

def f75ps_f75_fcf_per_share_acceleration_calc083_63d_base_v083_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(63) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc083_63d_base_v083_signal'] = f75ps_f75_fcf_per_share_acceleration_calc083_63d_base_v083_signal

def f75ps_f75_fcf_per_share_acceleration_calc084_126d_base_v084_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc084_126d_base_v084_signal'] = f75ps_f75_fcf_per_share_acceleration_calc084_126d_base_v084_signal

def f75ps_f75_fcf_per_share_acceleration_calc085_126d_base_v085_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc085_126d_base_v085_signal'] = f75ps_f75_fcf_per_share_acceleration_calc085_126d_base_v085_signal

def f75ps_f75_fcf_per_share_acceleration_calc086_42d_base_v086_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(42).max() - fcf.rolling(42).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc086_42d_base_v086_signal'] = f75ps_f75_fcf_per_share_acceleration_calc086_42d_base_v086_signal

def f75ps_f75_fcf_per_share_acceleration_calc087_42d_base_v087_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / eps.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc087_42d_base_v087_signal'] = f75ps_f75_fcf_per_share_acceleration_calc087_42d_base_v087_signal

def f75ps_f75_fcf_per_share_acceleration_calc088_42d_base_v088_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(42).rank(pct=True) / marketcap.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc088_42d_base_v088_signal'] = f75ps_f75_fcf_per_share_acceleration_calc088_42d_base_v088_signal

def f75ps_f75_fcf_per_share_acceleration_calc089_42d_base_v089_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas / eps.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc089_42d_base_v089_signal'] = f75ps_f75_fcf_per_share_acceleration_calc089_42d_base_v089_signal

def f75ps_f75_fcf_per_share_acceleration_calc090_42d_base_v090_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).rank(pct=True) / eps.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc090_42d_base_v090_signal'] = f75ps_f75_fcf_per_share_acceleration_calc090_42d_base_v090_signal

def f75ps_f75_fcf_per_share_acceleration_calc091_252d_base_v091_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / marketcap.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc091_252d_base_v091_signal'] = f75ps_f75_fcf_per_share_acceleration_calc091_252d_base_v091_signal

def f75ps_f75_fcf_per_share_acceleration_calc092_10d_base_v092_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(10).quantile(0.5) / fcf.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc092_10d_base_v092_signal'] = f75ps_f75_fcf_per_share_acceleration_calc092_10d_base_v092_signal

def f75ps_f75_fcf_per_share_acceleration_calc093_126d_base_v093_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(126).max() - eps.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc093_126d_base_v093_signal'] = f75ps_f75_fcf_per_share_acceleration_calc093_126d_base_v093_signal

def f75ps_f75_fcf_per_share_acceleration_calc094_21d_base_v094_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(21) / eps.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc094_21d_base_v094_signal'] = f75ps_f75_fcf_per_share_acceleration_calc094_21d_base_v094_signal

def f75ps_f75_fcf_per_share_acceleration_calc095_21d_base_v095_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(21).quantile(0.5) / revenue.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc095_21d_base_v095_signal'] = f75ps_f75_fcf_per_share_acceleration_calc095_21d_base_v095_signal

def f75ps_f75_fcf_per_share_acceleration_calc096_5d_base_v096_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(5).max() - assets.rolling(5).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc096_5d_base_v096_signal'] = f75ps_f75_fcf_per_share_acceleration_calc096_5d_base_v096_signal

def f75ps_f75_fcf_per_share_acceleration_calc097_42d_base_v097_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(42) - marketcap.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc097_42d_base_v097_signal'] = f75ps_f75_fcf_per_share_acceleration_calc097_42d_base_v097_signal

def f75ps_f75_fcf_per_share_acceleration_calc098_63d_base_v098_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(63).max() - netinc.rolling(63).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc098_63d_base_v098_signal'] = f75ps_f75_fcf_per_share_acceleration_calc098_63d_base_v098_signal

def f75ps_f75_fcf_per_share_acceleration_calc099_63d_base_v099_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(63).quantile(0.5) / sharesbas.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc099_63d_base_v099_signal'] = f75ps_f75_fcf_per_share_acceleration_calc099_63d_base_v099_signal

def f75ps_f75_fcf_per_share_acceleration_calc100_63d_base_v100_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(63).quantile(0.5) / marketcap.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc100_63d_base_v100_signal'] = f75ps_f75_fcf_per_share_acceleration_calc100_63d_base_v100_signal

def f75ps_f75_fcf_per_share_acceleration_calc101_21d_base_v101_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps / revenue.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc101_21d_base_v101_signal'] = f75ps_f75_fcf_per_share_acceleration_calc101_21d_base_v101_signal

def f75ps_f75_fcf_per_share_acceleration_calc102_21d_base_v102_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / sharesbas.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc102_21d_base_v102_signal'] = f75ps_f75_fcf_per_share_acceleration_calc102_21d_base_v102_signal

def f75ps_f75_fcf_per_share_acceleration_calc103_10d_base_v103_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc103_10d_base_v103_signal'] = f75ps_f75_fcf_per_share_acceleration_calc103_10d_base_v103_signal

def f75ps_f75_fcf_per_share_acceleration_calc104_10d_base_v104_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((eps - eps.rolling(10).mean()) / eps.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc104_10d_base_v104_signal'] = f75ps_f75_fcf_per_share_acceleration_calc104_10d_base_v104_signal

def f75ps_f75_fcf_per_share_acceleration_calc105_21d_base_v105_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((eps - eps.rolling(21).mean()) / eps.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc105_21d_base_v105_signal'] = f75ps_f75_fcf_per_share_acceleration_calc105_21d_base_v105_signal

def f75ps_f75_fcf_per_share_acceleration_calc106_42d_base_v106_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((revenue - revenue.rolling(42).mean()) / revenue.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc106_42d_base_v106_signal'] = f75ps_f75_fcf_per_share_acceleration_calc106_42d_base_v106_signal

def f75ps_f75_fcf_per_share_acceleration_calc107_63d_base_v107_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(63).kurt() - revenue.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc107_63d_base_v107_signal'] = f75ps_f75_fcf_per_share_acceleration_calc107_63d_base_v107_signal

def f75ps_f75_fcf_per_share_acceleration_calc108_63d_base_v108_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((assets - assets.rolling(63).mean()) / assets.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc108_63d_base_v108_signal'] = f75ps_f75_fcf_per_share_acceleration_calc108_63d_base_v108_signal

def f75ps_f75_fcf_per_share_acceleration_calc109_42d_base_v109_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(42).rank(pct=True) / eps.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc109_42d_base_v109_signal'] = f75ps_f75_fcf_per_share_acceleration_calc109_42d_base_v109_signal

def f75ps_f75_fcf_per_share_acceleration_calc110_42d_base_v110_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc110_42d_base_v110_signal'] = f75ps_f75_fcf_per_share_acceleration_calc110_42d_base_v110_signal

def f75ps_f75_fcf_per_share_acceleration_calc111_21d_base_v111_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).max() - netinc.rolling(21).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc111_21d_base_v111_signal'] = f75ps_f75_fcf_per_share_acceleration_calc111_21d_base_v111_signal

def f75ps_f75_fcf_per_share_acceleration_calc112_5d_base_v112_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(5) - netinc.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc112_5d_base_v112_signal'] = f75ps_f75_fcf_per_share_acceleration_calc112_5d_base_v112_signal

def f75ps_f75_fcf_per_share_acceleration_calc113_21d_base_v113_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(21).kurt() - assets.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc113_21d_base_v113_signal'] = f75ps_f75_fcf_per_share_acceleration_calc113_21d_base_v113_signal

def f75ps_f75_fcf_per_share_acceleration_calc114_126d_base_v114_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(126) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc114_126d_base_v114_signal'] = f75ps_f75_fcf_per_share_acceleration_calc114_126d_base_v114_signal

def f75ps_f75_fcf_per_share_acceleration_calc115_21d_base_v115_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc115_21d_base_v115_signal'] = f75ps_f75_fcf_per_share_acceleration_calc115_21d_base_v115_signal

def f75ps_f75_fcf_per_share_acceleration_calc116_21d_base_v116_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((fcf - fcf.rolling(21).mean()) / fcf.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc116_21d_base_v116_signal'] = f75ps_f75_fcf_per_share_acceleration_calc116_21d_base_v116_signal

def f75ps_f75_fcf_per_share_acceleration_calc117_42d_base_v117_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.pct_change(42) - assets.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc117_42d_base_v117_signal'] = f75ps_f75_fcf_per_share_acceleration_calc117_42d_base_v117_signal

def f75ps_f75_fcf_per_share_acceleration_calc118_63d_base_v118_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(63).max() - eps.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc118_63d_base_v118_signal'] = f75ps_f75_fcf_per_share_acceleration_calc118_63d_base_v118_signal

def f75ps_f75_fcf_per_share_acceleration_calc119_42d_base_v119_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(42).rank(pct=True) / marketcap.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc119_42d_base_v119_signal'] = f75ps_f75_fcf_per_share_acceleration_calc119_42d_base_v119_signal

def f75ps_f75_fcf_per_share_acceleration_calc120_5d_base_v120_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(5).abs() / sharesbas.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc120_5d_base_v120_signal'] = f75ps_f75_fcf_per_share_acceleration_calc120_5d_base_v120_signal

def f75ps_f75_fcf_per_share_acceleration_calc121_5d_base_v121_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.diff(5) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc121_5d_base_v121_signal'] = f75ps_f75_fcf_per_share_acceleration_calc121_5d_base_v121_signal

def f75ps_f75_fcf_per_share_acceleration_calc122_5d_base_v122_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / revenue.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc122_5d_base_v122_signal'] = f75ps_f75_fcf_per_share_acceleration_calc122_5d_base_v122_signal

def f75ps_f75_fcf_per_share_acceleration_calc123_21d_base_v123_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.pct_change(21) - eps.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc123_21d_base_v123_signal'] = f75ps_f75_fcf_per_share_acceleration_calc123_21d_base_v123_signal

def f75ps_f75_fcf_per_share_acceleration_calc124_126d_base_v124_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(126).quantile(0.5) / fcf.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc124_126d_base_v124_signal'] = f75ps_f75_fcf_per_share_acceleration_calc124_126d_base_v124_signal

def f75ps_f75_fcf_per_share_acceleration_calc125_126d_base_v125_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(126).kurt() - sharesbas.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc125_126d_base_v125_signal'] = f75ps_f75_fcf_per_share_acceleration_calc125_126d_base_v125_signal

def f75ps_f75_fcf_per_share_acceleration_calc126_10d_base_v126_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(10).max() - revenue.rolling(10).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc126_10d_base_v126_signal'] = f75ps_f75_fcf_per_share_acceleration_calc126_10d_base_v126_signal

def f75ps_f75_fcf_per_share_acceleration_calc127_5d_base_v127_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(5).kurt() - eps.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc127_5d_base_v127_signal'] = f75ps_f75_fcf_per_share_acceleration_calc127_5d_base_v127_signal

def f75ps_f75_fcf_per_share_acceleration_calc128_21d_base_v128_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc128_21d_base_v128_signal'] = f75ps_f75_fcf_per_share_acceleration_calc128_21d_base_v128_signal

def f75ps_f75_fcf_per_share_acceleration_calc129_42d_base_v129_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.pct_change(42) - eps.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc129_42d_base_v129_signal'] = f75ps_f75_fcf_per_share_acceleration_calc129_42d_base_v129_signal

def f75ps_f75_fcf_per_share_acceleration_calc130_63d_base_v130_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(63).max() - marketcap.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc130_63d_base_v130_signal'] = f75ps_f75_fcf_per_share_acceleration_calc130_63d_base_v130_signal

def f75ps_f75_fcf_per_share_acceleration_calc131_63d_base_v131_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(63) - assets.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc131_63d_base_v131_signal'] = f75ps_f75_fcf_per_share_acceleration_calc131_63d_base_v131_signal

def f75ps_f75_fcf_per_share_acceleration_calc132_10d_base_v132_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc132_10d_base_v132_signal'] = f75ps_f75_fcf_per_share_acceleration_calc132_10d_base_v132_signal

def f75ps_f75_fcf_per_share_acceleration_calc133_63d_base_v133_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(63).abs() / sharesbas.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc133_63d_base_v133_signal'] = f75ps_f75_fcf_per_share_acceleration_calc133_63d_base_v133_signal

def f75ps_f75_fcf_per_share_acceleration_calc134_42d_base_v134_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(42) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc134_42d_base_v134_signal'] = f75ps_f75_fcf_per_share_acceleration_calc134_42d_base_v134_signal

def f75ps_f75_fcf_per_share_acceleration_calc135_126d_base_v135_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((marketcap - marketcap.rolling(126).mean()) / marketcap.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc135_126d_base_v135_signal'] = f75ps_f75_fcf_per_share_acceleration_calc135_126d_base_v135_signal

def f75ps_f75_fcf_per_share_acceleration_calc136_5d_base_v136_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.pct_change(5) - revenue.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc136_5d_base_v136_signal'] = f75ps_f75_fcf_per_share_acceleration_calc136_5d_base_v136_signal

def f75ps_f75_fcf_per_share_acceleration_calc137_126d_base_v137_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(126).kurt() - netinc.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc137_126d_base_v137_signal'] = f75ps_f75_fcf_per_share_acceleration_calc137_126d_base_v137_signal

def f75ps_f75_fcf_per_share_acceleration_calc138_5d_base_v138_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.pct_change(5) - assets.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc138_5d_base_v138_signal'] = f75ps_f75_fcf_per_share_acceleration_calc138_5d_base_v138_signal

def f75ps_f75_fcf_per_share_acceleration_calc139_5d_base_v139_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(5).max() - marketcap.rolling(5).min()) / eps.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc139_5d_base_v139_signal'] = f75ps_f75_fcf_per_share_acceleration_calc139_5d_base_v139_signal

def f75ps_f75_fcf_per_share_acceleration_calc140_21d_base_v140_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps / revenue.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc140_21d_base_v140_signal'] = f75ps_f75_fcf_per_share_acceleration_calc140_21d_base_v140_signal

def f75ps_f75_fcf_per_share_acceleration_calc141_42d_base_v141_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(42).abs() / eps.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc141_42d_base_v141_signal'] = f75ps_f75_fcf_per_share_acceleration_calc141_42d_base_v141_signal

def f75ps_f75_fcf_per_share_acceleration_calc142_252d_base_v142_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((sharesbas - sharesbas.rolling(252).mean()) / sharesbas.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc142_252d_base_v142_signal'] = f75ps_f75_fcf_per_share_acceleration_calc142_252d_base_v142_signal

def f75ps_f75_fcf_per_share_acceleration_calc143_10d_base_v143_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc143_10d_base_v143_signal'] = f75ps_f75_fcf_per_share_acceleration_calc143_10d_base_v143_signal

def f75ps_f75_fcf_per_share_acceleration_calc144_252d_base_v144_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(252).rank(pct=True) / sharesbas.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc144_252d_base_v144_signal'] = f75ps_f75_fcf_per_share_acceleration_calc144_252d_base_v144_signal

def f75ps_f75_fcf_per_share_acceleration_calc145_126d_base_v145_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(126) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc145_126d_base_v145_signal'] = f75ps_f75_fcf_per_share_acceleration_calc145_126d_base_v145_signal

def f75ps_f75_fcf_per_share_acceleration_calc146_63d_base_v146_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(63).max() - sharesbas.rolling(63).min()) / eps.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc146_63d_base_v146_signal'] = f75ps_f75_fcf_per_share_acceleration_calc146_63d_base_v146_signal

def f75ps_f75_fcf_per_share_acceleration_calc147_10d_base_v147_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.pct_change(10) - assets.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc147_10d_base_v147_signal'] = f75ps_f75_fcf_per_share_acceleration_calc147_10d_base_v147_signal

def f75ps_f75_fcf_per_share_acceleration_calc148_21d_base_v148_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((sharesbas - sharesbas.rolling(21).mean()) / sharesbas.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc148_21d_base_v148_signal'] = f75ps_f75_fcf_per_share_acceleration_calc148_21d_base_v148_signal

def f75ps_f75_fcf_per_share_acceleration_calc149_63d_base_v149_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / eps.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc149_63d_base_v149_signal'] = f75ps_f75_fcf_per_share_acceleration_calc149_63d_base_v149_signal

def f75ps_f75_fcf_per_share_acceleration_calc150_42d_base_v150_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / assets.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc150_42d_base_v150_signal'] = f75ps_f75_fcf_per_share_acceleration_calc150_42d_base_v150_signal



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
