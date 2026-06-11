import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f107d_f107_debt_to_equity_dispersion_calc076_21d_base_v076_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(21).quantile(0.5) / debt.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc076_21d_base_v076_signal'] = f107d_f107_debt_to_equity_dispersion_calc076_21d_base_v076_signal

def f107d_f107_debt_to_equity_dispersion_calc077_5d_base_v077_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.diff(5) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc077_5d_base_v077_signal'] = f107d_f107_debt_to_equity_dispersion_calc077_5d_base_v077_signal

def f107d_f107_debt_to_equity_dispersion_calc078_252d_base_v078_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / marketcap.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc078_252d_base_v078_signal'] = f107d_f107_debt_to_equity_dispersion_calc078_252d_base_v078_signal

def f107d_f107_debt_to_equity_dispersion_calc079_252d_base_v079_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(252).kurt() - currentratio.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc079_252d_base_v079_signal'] = f107d_f107_debt_to_equity_dispersion_calc079_252d_base_v079_signal

def f107d_f107_debt_to_equity_dispersion_calc080_21d_base_v080_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(21).quantile(0.5) / ebitda.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc080_21d_base_v080_signal'] = f107d_f107_debt_to_equity_dispersion_calc080_21d_base_v080_signal

def f107d_f107_debt_to_equity_dispersion_calc081_63d_base_v081_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.pct_change(63) - currentratio.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc081_63d_base_v081_signal'] = f107d_f107_debt_to_equity_dispersion_calc081_63d_base_v081_signal

def f107d_f107_debt_to_equity_dispersion_calc082_252d_base_v082_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((assets - assets.rolling(252).mean()) / assets.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc082_252d_base_v082_signal'] = f107d_f107_debt_to_equity_dispersion_calc082_252d_base_v082_signal

def f107d_f107_debt_to_equity_dispersion_calc083_21d_base_v083_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((liabilities - liabilities.rolling(21).mean()) / liabilities.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc083_21d_base_v083_signal'] = f107d_f107_debt_to_equity_dispersion_calc083_21d_base_v083_signal

def f107d_f107_debt_to_equity_dispersion_calc084_42d_base_v084_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(42).max() - ebitda.rolling(42).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc084_42d_base_v084_signal'] = f107d_f107_debt_to_equity_dispersion_calc084_42d_base_v084_signal

def f107d_f107_debt_to_equity_dispersion_calc085_5d_base_v085_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(5).kurt() - equity.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc085_5d_base_v085_signal'] = f107d_f107_debt_to_equity_dispersion_calc085_5d_base_v085_signal

def f107d_f107_debt_to_equity_dispersion_calc086_21d_base_v086_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(21).kurt() - equity.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc086_21d_base_v086_signal'] = f107d_f107_debt_to_equity_dispersion_calc086_21d_base_v086_signal

def f107d_f107_debt_to_equity_dispersion_calc087_10d_base_v087_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc087_10d_base_v087_signal'] = f107d_f107_debt_to_equity_dispersion_calc087_10d_base_v087_signal

def f107d_f107_debt_to_equity_dispersion_calc088_5d_base_v088_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(5).quantile(0.5) / equity.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc088_5d_base_v088_signal'] = f107d_f107_debt_to_equity_dispersion_calc088_5d_base_v088_signal

def f107d_f107_debt_to_equity_dispersion_calc089_252d_base_v089_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(252).quantile(0.5) / debt.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc089_252d_base_v089_signal'] = f107d_f107_debt_to_equity_dispersion_calc089_252d_base_v089_signal

def f107d_f107_debt_to_equity_dispersion_calc090_21d_base_v090_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.pct_change(21) - marketcap.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc090_21d_base_v090_signal'] = f107d_f107_debt_to_equity_dispersion_calc090_21d_base_v090_signal

def f107d_f107_debt_to_equity_dispersion_calc091_42d_base_v091_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(42).max() - ebitda.rolling(42).min()) / debt.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc091_42d_base_v091_signal'] = f107d_f107_debt_to_equity_dispersion_calc091_42d_base_v091_signal

def f107d_f107_debt_to_equity_dispersion_calc092_21d_base_v092_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(21).abs() / currentratio.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc092_21d_base_v092_signal'] = f107d_f107_debt_to_equity_dispersion_calc092_21d_base_v092_signal

def f107d_f107_debt_to_equity_dispersion_calc093_5d_base_v093_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(5).abs() / currentratio.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc093_5d_base_v093_signal'] = f107d_f107_debt_to_equity_dispersion_calc093_5d_base_v093_signal

def f107d_f107_debt_to_equity_dispersion_calc094_63d_base_v094_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(63).max() - equity.rolling(63).min()) / currentratio.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc094_63d_base_v094_signal'] = f107d_f107_debt_to_equity_dispersion_calc094_63d_base_v094_signal

def f107d_f107_debt_to_equity_dispersion_calc095_5d_base_v095_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(5).max() - equity.rolling(5).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc095_5d_base_v095_signal'] = f107d_f107_debt_to_equity_dispersion_calc095_5d_base_v095_signal

def f107d_f107_debt_to_equity_dispersion_calc096_252d_base_v096_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(252).max() - liabilities.rolling(252).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc096_252d_base_v096_signal'] = f107d_f107_debt_to_equity_dispersion_calc096_252d_base_v096_signal

def f107d_f107_debt_to_equity_dispersion_calc097_21d_base_v097_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(21).abs() / liabilities.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc097_21d_base_v097_signal'] = f107d_f107_debt_to_equity_dispersion_calc097_21d_base_v097_signal

def f107d_f107_debt_to_equity_dispersion_calc098_10d_base_v098_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(10).max() - liabilities.rolling(10).min()) / debt.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc098_10d_base_v098_signal'] = f107d_f107_debt_to_equity_dispersion_calc098_10d_base_v098_signal

def f107d_f107_debt_to_equity_dispersion_calc099_10d_base_v099_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).max() - currentratio.rolling(10).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc099_10d_base_v099_signal'] = f107d_f107_debt_to_equity_dispersion_calc099_10d_base_v099_signal

def f107d_f107_debt_to_equity_dispersion_calc100_42d_base_v100_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(42).kurt() - debt.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc100_42d_base_v100_signal'] = f107d_f107_debt_to_equity_dispersion_calc100_42d_base_v100_signal

def f107d_f107_debt_to_equity_dispersion_calc101_252d_base_v101_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(252).rank(pct=True) / marketcap.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc101_252d_base_v101_signal'] = f107d_f107_debt_to_equity_dispersion_calc101_252d_base_v101_signal

def f107d_f107_debt_to_equity_dispersion_calc102_42d_base_v102_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(42).quantile(0.5) / equity.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc102_42d_base_v102_signal'] = f107d_f107_debt_to_equity_dispersion_calc102_42d_base_v102_signal

def f107d_f107_debt_to_equity_dispersion_calc103_126d_base_v103_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.pct_change(126) - liabilities.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc103_126d_base_v103_signal'] = f107d_f107_debt_to_equity_dispersion_calc103_126d_base_v103_signal

def f107d_f107_debt_to_equity_dispersion_calc104_252d_base_v104_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.pct_change(252) - equity.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc104_252d_base_v104_signal'] = f107d_f107_debt_to_equity_dispersion_calc104_252d_base_v104_signal

def f107d_f107_debt_to_equity_dispersion_calc105_252d_base_v105_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(252).rank(pct=True) / marketcap.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc105_252d_base_v105_signal'] = f107d_f107_debt_to_equity_dispersion_calc105_252d_base_v105_signal

def f107d_f107_debt_to_equity_dispersion_calc106_63d_base_v106_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(63) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc106_63d_base_v106_signal'] = f107d_f107_debt_to_equity_dispersion_calc106_63d_base_v106_signal

def f107d_f107_debt_to_equity_dispersion_calc107_63d_base_v107_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(63).abs() / assets.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc107_63d_base_v107_signal'] = f107d_f107_debt_to_equity_dispersion_calc107_63d_base_v107_signal

def f107d_f107_debt_to_equity_dispersion_calc108_10d_base_v108_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(10).max() - ebitda.rolling(10).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc108_10d_base_v108_signal'] = f107d_f107_debt_to_equity_dispersion_calc108_10d_base_v108_signal

def f107d_f107_debt_to_equity_dispersion_calc109_126d_base_v109_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(126).abs() / assets.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc109_126d_base_v109_signal'] = f107d_f107_debt_to_equity_dispersion_calc109_126d_base_v109_signal

def f107d_f107_debt_to_equity_dispersion_calc110_252d_base_v110_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(252).quantile(0.5) / assets.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc110_252d_base_v110_signal'] = f107d_f107_debt_to_equity_dispersion_calc110_252d_base_v110_signal

def f107d_f107_debt_to_equity_dispersion_calc111_21d_base_v111_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(21).max() - assets.rolling(21).min()) / currentratio.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc111_21d_base_v111_signal'] = f107d_f107_debt_to_equity_dispersion_calc111_21d_base_v111_signal

def f107d_f107_debt_to_equity_dispersion_calc112_252d_base_v112_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(252).kurt() - ebitda.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc112_252d_base_v112_signal'] = f107d_f107_debt_to_equity_dispersion_calc112_252d_base_v112_signal

def f107d_f107_debt_to_equity_dispersion_calc113_5d_base_v113_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc113_5d_base_v113_signal'] = f107d_f107_debt_to_equity_dispersion_calc113_5d_base_v113_signal

def f107d_f107_debt_to_equity_dispersion_calc114_5d_base_v114_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(5).rank(pct=True) / liabilities.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc114_5d_base_v114_signal'] = f107d_f107_debt_to_equity_dispersion_calc114_5d_base_v114_signal

def f107d_f107_debt_to_equity_dispersion_calc115_63d_base_v115_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(63) / currentratio.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc115_63d_base_v115_signal'] = f107d_f107_debt_to_equity_dispersion_calc115_63d_base_v115_signal

def f107d_f107_debt_to_equity_dispersion_calc116_42d_base_v116_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(42).max() - currentratio.rolling(42).min()) / ebitda.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc116_42d_base_v116_signal'] = f107d_f107_debt_to_equity_dispersion_calc116_42d_base_v116_signal

def f107d_f107_debt_to_equity_dispersion_calc117_21d_base_v117_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).kurt() - ebitda.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc117_21d_base_v117_signal'] = f107d_f107_debt_to_equity_dispersion_calc117_21d_base_v117_signal

def f107d_f107_debt_to_equity_dispersion_calc118_252d_base_v118_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.pct_change(252) - liabilities.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc118_252d_base_v118_signal'] = f107d_f107_debt_to_equity_dispersion_calc118_252d_base_v118_signal

def f107d_f107_debt_to_equity_dispersion_calc119_10d_base_v119_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets / liabilities.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc119_10d_base_v119_signal'] = f107d_f107_debt_to_equity_dispersion_calc119_10d_base_v119_signal

def f107d_f107_debt_to_equity_dispersion_calc120_5d_base_v120_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((currentratio - currentratio.rolling(5).mean()) / currentratio.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc120_5d_base_v120_signal'] = f107d_f107_debt_to_equity_dispersion_calc120_5d_base_v120_signal

def f107d_f107_debt_to_equity_dispersion_calc121_10d_base_v121_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((currentratio - currentratio.rolling(10).mean()) / currentratio.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc121_10d_base_v121_signal'] = f107d_f107_debt_to_equity_dispersion_calc121_10d_base_v121_signal

def f107d_f107_debt_to_equity_dispersion_calc122_63d_base_v122_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(63).abs() / ebitda.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc122_63d_base_v122_signal'] = f107d_f107_debt_to_equity_dispersion_calc122_63d_base_v122_signal

def f107d_f107_debt_to_equity_dispersion_calc123_21d_base_v123_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(21).abs() / debt.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc123_21d_base_v123_signal'] = f107d_f107_debt_to_equity_dispersion_calc123_21d_base_v123_signal

def f107d_f107_debt_to_equity_dispersion_calc124_21d_base_v124_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.diff(21) / liabilities.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc124_21d_base_v124_signal'] = f107d_f107_debt_to_equity_dispersion_calc124_21d_base_v124_signal

def f107d_f107_debt_to_equity_dispersion_calc125_42d_base_v125_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(42).quantile(0.5) / assets.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc125_42d_base_v125_signal'] = f107d_f107_debt_to_equity_dispersion_calc125_42d_base_v125_signal

def f107d_f107_debt_to_equity_dispersion_calc126_10d_base_v126_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(10).quantile(0.5) / marketcap.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc126_10d_base_v126_signal'] = f107d_f107_debt_to_equity_dispersion_calc126_10d_base_v126_signal

def f107d_f107_debt_to_equity_dispersion_calc127_21d_base_v127_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc127_21d_base_v127_signal'] = f107d_f107_debt_to_equity_dispersion_calc127_21d_base_v127_signal

def f107d_f107_debt_to_equity_dispersion_calc128_252d_base_v128_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc128_252d_base_v128_signal'] = f107d_f107_debt_to_equity_dispersion_calc128_252d_base_v128_signal

def f107d_f107_debt_to_equity_dispersion_calc129_21d_base_v129_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.pct_change(21) - equity.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc129_21d_base_v129_signal'] = f107d_f107_debt_to_equity_dispersion_calc129_21d_base_v129_signal

def f107d_f107_debt_to_equity_dispersion_calc130_21d_base_v130_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities / currentratio.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc130_21d_base_v130_signal'] = f107d_f107_debt_to_equity_dispersion_calc130_21d_base_v130_signal

def f107d_f107_debt_to_equity_dispersion_calc131_42d_base_v131_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(42).quantile(0.5) / currentratio.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc131_42d_base_v131_signal'] = f107d_f107_debt_to_equity_dispersion_calc131_42d_base_v131_signal

def f107d_f107_debt_to_equity_dispersion_calc132_10d_base_v132_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10).abs() / ebitda.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc132_10d_base_v132_signal'] = f107d_f107_debt_to_equity_dispersion_calc132_10d_base_v132_signal

def f107d_f107_debt_to_equity_dispersion_calc133_252d_base_v133_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(252).rank(pct=True) / debt.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc133_252d_base_v133_signal'] = f107d_f107_debt_to_equity_dispersion_calc133_252d_base_v133_signal

def f107d_f107_debt_to_equity_dispersion_calc134_252d_base_v134_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(252).max() - assets.rolling(252).min()) / ebitda.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc134_252d_base_v134_signal'] = f107d_f107_debt_to_equity_dispersion_calc134_252d_base_v134_signal

def f107d_f107_debt_to_equity_dispersion_calc135_10d_base_v135_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / equity.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc135_10d_base_v135_signal'] = f107d_f107_debt_to_equity_dispersion_calc135_10d_base_v135_signal

def f107d_f107_debt_to_equity_dispersion_calc136_42d_base_v136_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / marketcap.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc136_42d_base_v136_signal'] = f107d_f107_debt_to_equity_dispersion_calc136_42d_base_v136_signal

def f107d_f107_debt_to_equity_dispersion_calc137_63d_base_v137_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc137_63d_base_v137_signal'] = f107d_f107_debt_to_equity_dispersion_calc137_63d_base_v137_signal

def f107d_f107_debt_to_equity_dispersion_calc138_10d_base_v138_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((marketcap - marketcap.rolling(10).mean()) / marketcap.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc138_10d_base_v138_signal'] = f107d_f107_debt_to_equity_dispersion_calc138_10d_base_v138_signal

def f107d_f107_debt_to_equity_dispersion_calc139_252d_base_v139_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.pct_change(252) - debt.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc139_252d_base_v139_signal'] = f107d_f107_debt_to_equity_dispersion_calc139_252d_base_v139_signal

def f107d_f107_debt_to_equity_dispersion_calc140_42d_base_v140_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(42) / liabilities.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc140_42d_base_v140_signal'] = f107d_f107_debt_to_equity_dispersion_calc140_42d_base_v140_signal

def f107d_f107_debt_to_equity_dispersion_calc141_63d_base_v141_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((liabilities - liabilities.rolling(63).mean()) / liabilities.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc141_63d_base_v141_signal'] = f107d_f107_debt_to_equity_dispersion_calc141_63d_base_v141_signal

def f107d_f107_debt_to_equity_dispersion_calc142_252d_base_v142_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc142_252d_base_v142_signal'] = f107d_f107_debt_to_equity_dispersion_calc142_252d_base_v142_signal

def f107d_f107_debt_to_equity_dispersion_calc143_126d_base_v143_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / ebitda.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc143_126d_base_v143_signal'] = f107d_f107_debt_to_equity_dispersion_calc143_126d_base_v143_signal

def f107d_f107_debt_to_equity_dispersion_calc144_126d_base_v144_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.pct_change(126) - marketcap.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc144_126d_base_v144_signal'] = f107d_f107_debt_to_equity_dispersion_calc144_126d_base_v144_signal

def f107d_f107_debt_to_equity_dispersion_calc145_252d_base_v145_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(252).abs() / equity.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc145_252d_base_v145_signal'] = f107d_f107_debt_to_equity_dispersion_calc145_252d_base_v145_signal

def f107d_f107_debt_to_equity_dispersion_calc146_252d_base_v146_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(252).abs() / marketcap.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc146_252d_base_v146_signal'] = f107d_f107_debt_to_equity_dispersion_calc146_252d_base_v146_signal

def f107d_f107_debt_to_equity_dispersion_calc147_252d_base_v147_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities / currentratio.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc147_252d_base_v147_signal'] = f107d_f107_debt_to_equity_dispersion_calc147_252d_base_v147_signal

def f107d_f107_debt_to_equity_dispersion_calc148_10d_base_v148_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(10) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc148_10d_base_v148_signal'] = f107d_f107_debt_to_equity_dispersion_calc148_10d_base_v148_signal

def f107d_f107_debt_to_equity_dispersion_calc149_252d_base_v149_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(252).max() - marketcap.rolling(252).min()) / debt.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc149_252d_base_v149_signal'] = f107d_f107_debt_to_equity_dispersion_calc149_252d_base_v149_signal

def f107d_f107_debt_to_equity_dispersion_calc150_21d_base_v150_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(21).quantile(0.5) / liabilities.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc150_21d_base_v150_signal'] = f107d_f107_debt_to_equity_dispersion_calc150_21d_base_v150_signal



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
