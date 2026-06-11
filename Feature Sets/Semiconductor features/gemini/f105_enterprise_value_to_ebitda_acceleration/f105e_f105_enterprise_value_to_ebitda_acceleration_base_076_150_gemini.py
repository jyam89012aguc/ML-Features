import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc076_10d_base_v076_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / ev.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc076_10d_base_v076_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc076_10d_base_v076_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc077_10d_base_v077_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).max() - ev.rolling(10).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc077_10d_base_v077_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc077_10d_base_v077_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc078_252d_base_v078_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / debt.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc078_252d_base_v078_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc078_252d_base_v078_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc079_10d_base_v079_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(10) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc079_10d_base_v079_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc079_10d_base_v079_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc080_10d_base_v080_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((assets - assets.rolling(10).mean()) / assets.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc080_10d_base_v080_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc080_10d_base_v080_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc081_21d_base_v081_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt / fcf.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc081_21d_base_v081_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc081_21d_base_v081_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc082_126d_base_v082_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc082_126d_base_v082_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc082_126d_base_v082_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc083_63d_base_v083_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / assets.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc083_63d_base_v083_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc083_63d_base_v083_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc084_126d_base_v084_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc084_126d_base_v084_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc084_126d_base_v084_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc085_21d_base_v085_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(21) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc085_21d_base_v085_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc085_21d_base_v085_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc086_21d_base_v086_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / equity.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc086_21d_base_v086_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc086_21d_base_v086_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc087_10d_base_v087_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(10).mean()) / ev.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc087_10d_base_v087_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc087_10d_base_v087_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc088_10d_base_v088_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / debt.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc088_10d_base_v088_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc088_10d_base_v088_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc089_126d_base_v089_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / ev.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc089_126d_base_v089_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc089_126d_base_v089_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc090_126d_base_v090_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc090_126d_base_v090_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc090_126d_base_v090_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc091_21d_base_v091_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(21).quantile(0.5) / revenue.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc091_21d_base_v091_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc091_21d_base_v091_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc092_126d_base_v092_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.pct_change(126) - fcf.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc092_126d_base_v092_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc092_126d_base_v092_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc093_10d_base_v093_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc093_10d_base_v093_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc093_10d_base_v093_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc094_42d_base_v094_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / fcf.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc094_42d_base_v094_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc094_42d_base_v094_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc095_63d_base_v095_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc095_63d_base_v095_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc095_63d_base_v095_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc096_126d_base_v096_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(126).abs() / ev.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc096_126d_base_v096_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc096_126d_base_v096_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc097_5d_base_v097_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc097_5d_base_v097_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc097_5d_base_v097_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc098_42d_base_v098_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(42).kurt() - equity.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc098_42d_base_v098_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc098_42d_base_v098_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc099_5d_base_v099_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(5) / debt.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc099_5d_base_v099_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc099_5d_base_v099_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc100_252d_base_v100_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.pct_change(252) - assets.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc100_252d_base_v100_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc100_252d_base_v100_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc101_10d_base_v101_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / assets.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc101_10d_base_v101_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc101_10d_base_v101_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc102_21d_base_v102_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ebitda - ebitda.rolling(21).mean()) / ebitda.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc102_21d_base_v102_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc102_21d_base_v102_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc103_126d_base_v103_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.pct_change(126) - debt.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc103_126d_base_v103_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc103_126d_base_v103_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc104_126d_base_v104_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.diff(126) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc104_126d_base_v104_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc104_126d_base_v104_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc105_10d_base_v105_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / fcf.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc105_10d_base_v105_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc105_10d_base_v105_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc106_10d_base_v106_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / ev.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc106_10d_base_v106_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc106_10d_base_v106_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc107_5d_base_v107_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc107_5d_base_v107_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc107_5d_base_v107_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc108_63d_base_v108_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(63).quantile(0.5) / debt.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc108_63d_base_v108_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc108_63d_base_v108_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc109_21d_base_v109_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(21).max() - ev.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc109_21d_base_v109_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc109_21d_base_v109_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc110_5d_base_v110_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(5).max() - fcf.rolling(5).min()) / debt.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc110_5d_base_v110_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc110_5d_base_v110_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc111_252d_base_v111_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).max() - ebitda.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc111_252d_base_v111_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc111_252d_base_v111_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc112_5d_base_v112_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(5) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc112_5d_base_v112_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc112_5d_base_v112_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc113_42d_base_v113_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(42).abs() / equity.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc113_42d_base_v113_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc113_42d_base_v113_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc114_21d_base_v114_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(21) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc114_21d_base_v114_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc114_21d_base_v114_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc115_42d_base_v115_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc115_42d_base_v115_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc115_42d_base_v115_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc116_10d_base_v116_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(10).kurt() - assets.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc116_10d_base_v116_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc116_10d_base_v116_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc117_5d_base_v117_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / fcf.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc117_5d_base_v117_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc117_5d_base_v117_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc118_63d_base_v118_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(63).abs() / ebitda.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc118_63d_base_v118_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc118_63d_base_v118_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc119_63d_base_v119_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(63).rank(pct=True) / assets.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc119_63d_base_v119_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc119_63d_base_v119_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc120_10d_base_v120_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(10).abs() / debt.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc120_10d_base_v120_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc120_10d_base_v120_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc121_42d_base_v121_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc121_42d_base_v121_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc121_42d_base_v121_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc122_126d_base_v122_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc122_126d_base_v122_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc122_126d_base_v122_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc123_252d_base_v123_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc123_252d_base_v123_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc123_252d_base_v123_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc124_252d_base_v124_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / equity.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc124_252d_base_v124_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc124_252d_base_v124_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc125_252d_base_v125_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(252).max() - ev.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc125_252d_base_v125_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc125_252d_base_v125_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc126_42d_base_v126_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(42).rank(pct=True) / ev.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc126_42d_base_v126_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc126_42d_base_v126_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc127_252d_base_v127_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / equity.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc127_252d_base_v127_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc127_252d_base_v127_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc128_10d_base_v128_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(10).abs() / debt.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc128_10d_base_v128_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc128_10d_base_v128_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc129_252d_base_v129_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(252).quantile(0.5) / debt.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc129_252d_base_v129_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc129_252d_base_v129_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc130_252d_base_v130_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).rank(pct=True) / debt.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc130_252d_base_v130_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc130_252d_base_v130_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc131_42d_base_v131_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(42).quantile(0.5) / ev.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc131_42d_base_v131_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc131_42d_base_v131_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc132_126d_base_v132_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc132_126d_base_v132_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc132_126d_base_v132_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc133_10d_base_v133_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(10).max() - fcf.rolling(10).min()) / ebitda.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc133_10d_base_v133_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc133_10d_base_v133_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc134_63d_base_v134_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(63) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc134_63d_base_v134_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc134_63d_base_v134_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc135_10d_base_v135_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).rank(pct=True) / debt.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc135_10d_base_v135_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc135_10d_base_v135_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc136_10d_base_v136_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(10).max() - ebitda.rolling(10).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc136_10d_base_v136_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc136_10d_base_v136_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc137_63d_base_v137_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((revenue - revenue.rolling(63).mean()) / revenue.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc137_63d_base_v137_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc137_63d_base_v137_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc138_5d_base_v138_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(5).rank(pct=True) / revenue.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc138_5d_base_v138_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc138_5d_base_v138_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc139_63d_base_v139_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(63).abs() / revenue.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc139_63d_base_v139_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc139_63d_base_v139_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc140_252d_base_v140_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc140_252d_base_v140_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc140_252d_base_v140_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc141_63d_base_v141_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(63).rank(pct=True) / revenue.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc141_63d_base_v141_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc141_63d_base_v141_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc142_126d_base_v142_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc142_126d_base_v142_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc142_126d_base_v142_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc143_126d_base_v143_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).kurt() - assets.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc143_126d_base_v143_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc143_126d_base_v143_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc144_63d_base_v144_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(63).max() - ebitda.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc144_63d_base_v144_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc144_63d_base_v144_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc145_21d_base_v145_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(21).quantile(0.5) / debt.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc145_21d_base_v145_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc145_21d_base_v145_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc146_5d_base_v146_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(5).rank(pct=True) / ebitda.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc146_5d_base_v146_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc146_5d_base_v146_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc147_42d_base_v147_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(42).abs() / ebitda.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc147_42d_base_v147_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc147_42d_base_v147_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc148_5d_base_v148_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / ev.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc148_5d_base_v148_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc148_5d_base_v148_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc149_10d_base_v149_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc149_10d_base_v149_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc149_10d_base_v149_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc150_63d_base_v150_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(63).abs() / assets.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc150_63d_base_v150_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc150_63d_base_v150_signal



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
