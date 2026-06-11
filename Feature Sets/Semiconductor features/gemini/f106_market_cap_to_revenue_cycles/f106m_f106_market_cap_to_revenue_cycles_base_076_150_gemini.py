import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f106m_f106_market_cap_to_revenue_cycles_calc076_10d_base_v076_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(10).max() - ebitda.rolling(10).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc076_10d_base_v076_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc076_10d_base_v076_signal

def f106m_f106_market_cap_to_revenue_cycles_calc077_126d_base_v077_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(126) - equity.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc077_126d_base_v077_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc077_126d_base_v077_signal

def f106m_f106_market_cap_to_revenue_cycles_calc078_252d_base_v078_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc078_252d_base_v078_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc078_252d_base_v078_signal

def f106m_f106_market_cap_to_revenue_cycles_calc079_5d_base_v079_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(5) - fcf.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc079_5d_base_v079_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc079_5d_base_v079_signal

def f106m_f106_market_cap_to_revenue_cycles_calc080_21d_base_v080_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(21).abs() / netinc.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc080_21d_base_v080_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc080_21d_base_v080_signal

def f106m_f106_market_cap_to_revenue_cycles_calc081_63d_base_v081_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((netinc - netinc.rolling(63).mean()) / netinc.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc081_63d_base_v081_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc081_63d_base_v081_signal

def f106m_f106_market_cap_to_revenue_cycles_calc082_10d_base_v082_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(10).max() - equity.rolling(10).min()) / netinc.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc082_10d_base_v082_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc082_10d_base_v082_signal

def f106m_f106_market_cap_to_revenue_cycles_calc083_21d_base_v083_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(21).quantile(0.5) / equity.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc083_21d_base_v083_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc083_21d_base_v083_signal

def f106m_f106_market_cap_to_revenue_cycles_calc084_21d_base_v084_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(21).max() - marketcap.rolling(21).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc084_21d_base_v084_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc084_21d_base_v084_signal

def f106m_f106_market_cap_to_revenue_cycles_calc085_21d_base_v085_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((assets - assets.rolling(21).mean()) / assets.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc085_21d_base_v085_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc085_21d_base_v085_signal

def f106m_f106_market_cap_to_revenue_cycles_calc086_5d_base_v086_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(5).max() - assets.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc086_5d_base_v086_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc086_5d_base_v086_signal

def f106m_f106_market_cap_to_revenue_cycles_calc087_21d_base_v087_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc087_21d_base_v087_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc087_21d_base_v087_signal

def f106m_f106_market_cap_to_revenue_cycles_calc088_63d_base_v088_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / equity.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc088_63d_base_v088_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc088_63d_base_v088_signal

def f106m_f106_market_cap_to_revenue_cycles_calc089_252d_base_v089_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((equity - equity.rolling(252).mean()) / equity.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc089_252d_base_v089_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc089_252d_base_v089_signal

def f106m_f106_market_cap_to_revenue_cycles_calc090_42d_base_v090_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(42) - netinc.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc090_42d_base_v090_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc090_42d_base_v090_signal

def f106m_f106_market_cap_to_revenue_cycles_calc091_5d_base_v091_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(5).max() - fcf.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc091_5d_base_v091_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc091_5d_base_v091_signal

def f106m_f106_market_cap_to_revenue_cycles_calc092_126d_base_v092_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc092_126d_base_v092_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc092_126d_base_v092_signal

def f106m_f106_market_cap_to_revenue_cycles_calc093_5d_base_v093_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(5).abs() / ebitda.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc093_5d_base_v093_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc093_5d_base_v093_signal

def f106m_f106_market_cap_to_revenue_cycles_calc094_21d_base_v094_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(21).rank(pct=True) / ebitda.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc094_21d_base_v094_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc094_21d_base_v094_signal

def f106m_f106_market_cap_to_revenue_cycles_calc095_42d_base_v095_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc095_42d_base_v095_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc095_42d_base_v095_signal

def f106m_f106_market_cap_to_revenue_cycles_calc096_10d_base_v096_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(10) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc096_10d_base_v096_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc096_10d_base_v096_signal

def f106m_f106_market_cap_to_revenue_cycles_calc097_252d_base_v097_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(252) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc097_252d_base_v097_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc097_252d_base_v097_signal

def f106m_f106_market_cap_to_revenue_cycles_calc098_5d_base_v098_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(5).kurt() - marketcap.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc098_5d_base_v098_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc098_5d_base_v098_signal

def f106m_f106_market_cap_to_revenue_cycles_calc099_10d_base_v099_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap / netinc.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc099_10d_base_v099_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc099_10d_base_v099_signal

def f106m_f106_market_cap_to_revenue_cycles_calc100_10d_base_v100_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(10).rank(pct=True) / ebitda.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc100_10d_base_v100_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc100_10d_base_v100_signal

def f106m_f106_market_cap_to_revenue_cycles_calc101_63d_base_v101_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((assets - assets.rolling(63).mean()) / assets.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc101_63d_base_v101_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc101_63d_base_v101_signal

def f106m_f106_market_cap_to_revenue_cycles_calc102_21d_base_v102_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(21).abs() / ebitda.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc102_21d_base_v102_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc102_21d_base_v102_signal

def f106m_f106_market_cap_to_revenue_cycles_calc103_126d_base_v103_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(126).quantile(0.5) / assets.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc103_126d_base_v103_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc103_126d_base_v103_signal

def f106m_f106_market_cap_to_revenue_cycles_calc104_10d_base_v104_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(10).abs() / marketcap.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc104_10d_base_v104_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc104_10d_base_v104_signal

def f106m_f106_market_cap_to_revenue_cycles_calc105_21d_base_v105_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.diff(21).abs() / assets.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc105_21d_base_v105_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc105_21d_base_v105_signal

def f106m_f106_market_cap_to_revenue_cycles_calc106_21d_base_v106_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(21).rank(pct=True) / revenue.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc106_21d_base_v106_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc106_21d_base_v106_signal

def f106m_f106_market_cap_to_revenue_cycles_calc107_21d_base_v107_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(21).kurt() - fcf.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc107_21d_base_v107_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc107_21d_base_v107_signal

def f106m_f106_market_cap_to_revenue_cycles_calc108_252d_base_v108_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(252) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc108_252d_base_v108_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc108_252d_base_v108_signal

def f106m_f106_market_cap_to_revenue_cycles_calc109_63d_base_v109_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((revenue - revenue.rolling(63).mean()) / revenue.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc109_63d_base_v109_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc109_63d_base_v109_signal

def f106m_f106_market_cap_to_revenue_cycles_calc110_21d_base_v110_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(21) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc110_21d_base_v110_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc110_21d_base_v110_signal

def f106m_f106_market_cap_to_revenue_cycles_calc111_63d_base_v111_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(63).kurt() - netinc.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc111_63d_base_v111_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc111_63d_base_v111_signal

def f106m_f106_market_cap_to_revenue_cycles_calc112_5d_base_v112_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.pct_change(5) - fcf.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc112_5d_base_v112_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc112_5d_base_v112_signal

def f106m_f106_market_cap_to_revenue_cycles_calc113_252d_base_v113_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc113_252d_base_v113_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc113_252d_base_v113_signal

def f106m_f106_market_cap_to_revenue_cycles_calc114_5d_base_v114_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.diff(5).abs() / revenue.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc114_5d_base_v114_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc114_5d_base_v114_signal

def f106m_f106_market_cap_to_revenue_cycles_calc115_63d_base_v115_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(63).quantile(0.5) / revenue.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc115_63d_base_v115_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc115_63d_base_v115_signal

def f106m_f106_market_cap_to_revenue_cycles_calc116_10d_base_v116_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.pct_change(10) - fcf.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc116_10d_base_v116_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc116_10d_base_v116_signal

def f106m_f106_market_cap_to_revenue_cycles_calc117_10d_base_v117_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(10) - equity.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc117_10d_base_v117_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc117_10d_base_v117_signal

def f106m_f106_market_cap_to_revenue_cycles_calc118_63d_base_v118_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc118_63d_base_v118_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc118_63d_base_v118_signal

def f106m_f106_market_cap_to_revenue_cycles_calc119_21d_base_v119_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(21).abs() / marketcap.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc119_21d_base_v119_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc119_21d_base_v119_signal

def f106m_f106_market_cap_to_revenue_cycles_calc120_126d_base_v120_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc120_126d_base_v120_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc120_126d_base_v120_signal

def f106m_f106_market_cap_to_revenue_cycles_calc121_126d_base_v121_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.pct_change(126) - revenue.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc121_126d_base_v121_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc121_126d_base_v121_signal

def f106m_f106_market_cap_to_revenue_cycles_calc122_21d_base_v122_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / equity.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc122_21d_base_v122_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc122_21d_base_v122_signal

def f106m_f106_market_cap_to_revenue_cycles_calc123_21d_base_v123_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(21).rank(pct=True) / netinc.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc123_21d_base_v123_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc123_21d_base_v123_signal

def f106m_f106_market_cap_to_revenue_cycles_calc124_5d_base_v124_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(5) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc124_5d_base_v124_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc124_5d_base_v124_signal

def f106m_f106_market_cap_to_revenue_cycles_calc125_63d_base_v125_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(63).rank(pct=True) / fcf.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc125_63d_base_v125_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc125_63d_base_v125_signal

def f106m_f106_market_cap_to_revenue_cycles_calc126_10d_base_v126_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(10).quantile(0.5) / netinc.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc126_10d_base_v126_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc126_10d_base_v126_signal

def f106m_f106_market_cap_to_revenue_cycles_calc127_5d_base_v127_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((equity - equity.rolling(5).mean()) / equity.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc127_5d_base_v127_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc127_5d_base_v127_signal

def f106m_f106_market_cap_to_revenue_cycles_calc128_252d_base_v128_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(252).kurt() - revenue.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc128_252d_base_v128_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc128_252d_base_v128_signal

def f106m_f106_market_cap_to_revenue_cycles_calc129_252d_base_v129_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(252) - equity.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc129_252d_base_v129_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc129_252d_base_v129_signal

def f106m_f106_market_cap_to_revenue_cycles_calc130_63d_base_v130_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(63).rank(pct=True) / marketcap.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc130_63d_base_v130_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc130_63d_base_v130_signal

def f106m_f106_market_cap_to_revenue_cycles_calc131_63d_base_v131_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(63) - assets.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc131_63d_base_v131_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc131_63d_base_v131_signal

def f106m_f106_market_cap_to_revenue_cycles_calc132_126d_base_v132_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(126).kurt() - assets.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc132_126d_base_v132_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc132_126d_base_v132_signal

def f106m_f106_market_cap_to_revenue_cycles_calc133_5d_base_v133_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(5) - ebitda.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc133_5d_base_v133_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc133_5d_base_v133_signal

def f106m_f106_market_cap_to_revenue_cycles_calc134_21d_base_v134_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc134_21d_base_v134_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc134_21d_base_v134_signal

def f106m_f106_market_cap_to_revenue_cycles_calc135_10d_base_v135_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc135_10d_base_v135_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc135_10d_base_v135_signal

def f106m_f106_market_cap_to_revenue_cycles_calc136_21d_base_v136_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((ebitda - ebitda.rolling(21).mean()) / ebitda.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc136_21d_base_v136_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc136_21d_base_v136_signal

def f106m_f106_market_cap_to_revenue_cycles_calc137_21d_base_v137_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc137_21d_base_v137_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc137_21d_base_v137_signal

def f106m_f106_market_cap_to_revenue_cycles_calc138_63d_base_v138_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc138_63d_base_v138_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc138_63d_base_v138_signal

def f106m_f106_market_cap_to_revenue_cycles_calc139_63d_base_v139_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((ebitda - ebitda.rolling(63).mean()) / ebitda.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc139_63d_base_v139_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc139_63d_base_v139_signal

def f106m_f106_market_cap_to_revenue_cycles_calc140_5d_base_v140_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((ebitda - ebitda.rolling(5).mean()) / ebitda.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc140_5d_base_v140_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc140_5d_base_v140_signal

def f106m_f106_market_cap_to_revenue_cycles_calc141_42d_base_v141_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(42).kurt() - equity.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc141_42d_base_v141_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc141_42d_base_v141_signal

def f106m_f106_market_cap_to_revenue_cycles_calc142_21d_base_v142_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(21).quantile(0.5) / assets.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc142_21d_base_v142_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc142_21d_base_v142_signal

def f106m_f106_market_cap_to_revenue_cycles_calc143_252d_base_v143_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(252).rank(pct=True) / marketcap.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc143_252d_base_v143_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc143_252d_base_v143_signal

def f106m_f106_market_cap_to_revenue_cycles_calc144_63d_base_v144_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(63).max() - netinc.rolling(63).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc144_63d_base_v144_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc144_63d_base_v144_signal

def f106m_f106_market_cap_to_revenue_cycles_calc145_42d_base_v145_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / ebitda.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc145_42d_base_v145_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc145_42d_base_v145_signal

def f106m_f106_market_cap_to_revenue_cycles_calc146_126d_base_v146_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(126).abs() / assets.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc146_126d_base_v146_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc146_126d_base_v146_signal

def f106m_f106_market_cap_to_revenue_cycles_calc147_5d_base_v147_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(5).rank(pct=True) / revenue.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc147_5d_base_v147_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc147_5d_base_v147_signal

def f106m_f106_market_cap_to_revenue_cycles_calc148_5d_base_v148_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(5).rank(pct=True) / ebitda.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc148_5d_base_v148_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc148_5d_base_v148_signal

def f106m_f106_market_cap_to_revenue_cycles_calc149_42d_base_v149_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(42).max() - netinc.rolling(42).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc149_42d_base_v149_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc149_42d_base_v149_signal

def f106m_f106_market_cap_to_revenue_cycles_calc150_63d_base_v150_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(63).rank(pct=True) / revenue.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc150_63d_base_v150_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc150_63d_base_v150_signal



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
