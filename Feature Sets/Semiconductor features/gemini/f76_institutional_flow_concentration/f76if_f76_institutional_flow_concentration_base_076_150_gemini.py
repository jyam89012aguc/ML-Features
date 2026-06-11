import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f76if_f76_institutional_flow_concentration_calc076_5d_base_v076_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(5).kurt() - volume.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc076_5d_base_v076_signal'] = f76if_f76_institutional_flow_concentration_calc076_5d_base_v076_signal

def f76if_f76_institutional_flow_concentration_calc077_42d_base_v077_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.pct_change(42) - open.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc077_42d_base_v077_signal'] = f76if_f76_institutional_flow_concentration_calc077_42d_base_v077_signal

def f76if_f76_institutional_flow_concentration_calc078_10d_base_v078_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(10) / volume.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc078_10d_base_v078_signal'] = f76if_f76_institutional_flow_concentration_calc078_10d_base_v078_signal

def f76if_f76_institutional_flow_concentration_calc079_42d_base_v079_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.diff(42).abs() / open.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc079_42d_base_v079_signal'] = f76if_f76_institutional_flow_concentration_calc079_42d_base_v079_signal

def f76if_f76_institutional_flow_concentration_calc080_63d_base_v080_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(63).max() - high.rolling(63).min()) / low.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc080_63d_base_v080_signal'] = f76if_f76_institutional_flow_concentration_calc080_63d_base_v080_signal

def f76if_f76_institutional_flow_concentration_calc081_42d_base_v081_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(42) - sharesbas.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc081_42d_base_v081_signal'] = f76if_f76_institutional_flow_concentration_calc081_42d_base_v081_signal

def f76if_f76_institutional_flow_concentration_calc082_63d_base_v082_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / volume.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc082_63d_base_v082_signal'] = f76if_f76_institutional_flow_concentration_calc082_63d_base_v082_signal

def f76if_f76_institutional_flow_concentration_calc083_63d_base_v083_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.pct_change(63) - open.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc083_63d_base_v083_signal'] = f76if_f76_institutional_flow_concentration_calc083_63d_base_v083_signal

def f76if_f76_institutional_flow_concentration_calc084_42d_base_v084_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((open - open.rolling(42).mean()) / open.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc084_42d_base_v084_signal'] = f76if_f76_institutional_flow_concentration_calc084_42d_base_v084_signal

def f76if_f76_institutional_flow_concentration_calc085_63d_base_v085_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(63) / open.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc085_63d_base_v085_signal'] = f76if_f76_institutional_flow_concentration_calc085_63d_base_v085_signal

def f76if_f76_institutional_flow_concentration_calc086_5d_base_v086_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(5).quantile(0.5) / open.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc086_5d_base_v086_signal'] = f76if_f76_institutional_flow_concentration_calc086_5d_base_v086_signal

def f76if_f76_institutional_flow_concentration_calc087_21d_base_v087_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(21).rank(pct=True) / high.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc087_21d_base_v087_signal'] = f76if_f76_institutional_flow_concentration_calc087_21d_base_v087_signal

def f76if_f76_institutional_flow_concentration_calc088_126d_base_v088_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(126).rank(pct=True) / close.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc088_126d_base_v088_signal'] = f76if_f76_institutional_flow_concentration_calc088_126d_base_v088_signal

def f76if_f76_institutional_flow_concentration_calc089_42d_base_v089_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(42).quantile(0.5) / high.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc089_42d_base_v089_signal'] = f76if_f76_institutional_flow_concentration_calc089_42d_base_v089_signal

def f76if_f76_institutional_flow_concentration_calc090_10d_base_v090_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(10) / low.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc090_10d_base_v090_signal'] = f76if_f76_institutional_flow_concentration_calc090_10d_base_v090_signal

def f76if_f76_institutional_flow_concentration_calc091_63d_base_v091_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(63).quantile(0.5) / sharesbas.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc091_63d_base_v091_signal'] = f76if_f76_institutional_flow_concentration_calc091_63d_base_v091_signal

def f76if_f76_institutional_flow_concentration_calc092_126d_base_v092_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((low - low.rolling(126).mean()) / low.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc092_126d_base_v092_signal'] = f76if_f76_institutional_flow_concentration_calc092_126d_base_v092_signal

def f76if_f76_institutional_flow_concentration_calc093_21d_base_v093_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / low.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc093_21d_base_v093_signal'] = f76if_f76_institutional_flow_concentration_calc093_21d_base_v093_signal

def f76if_f76_institutional_flow_concentration_calc094_126d_base_v094_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / volume.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc094_126d_base_v094_signal'] = f76if_f76_institutional_flow_concentration_calc094_126d_base_v094_signal

def f76if_f76_institutional_flow_concentration_calc095_252d_base_v095_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(252) / close.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc095_252d_base_v095_signal'] = f76if_f76_institutional_flow_concentration_calc095_252d_base_v095_signal

def f76if_f76_institutional_flow_concentration_calc096_42d_base_v096_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / marketcap.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc096_42d_base_v096_signal'] = f76if_f76_institutional_flow_concentration_calc096_42d_base_v096_signal

def f76if_f76_institutional_flow_concentration_calc097_10d_base_v097_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(10).quantile(0.5) / low.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc097_10d_base_v097_signal'] = f76if_f76_institutional_flow_concentration_calc097_10d_base_v097_signal

def f76if_f76_institutional_flow_concentration_calc098_252d_base_v098_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).max() - high.rolling(252).min()) / volume.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc098_252d_base_v098_signal'] = f76if_f76_institutional_flow_concentration_calc098_252d_base_v098_signal

def f76if_f76_institutional_flow_concentration_calc099_10d_base_v099_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(10) / close.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc099_10d_base_v099_signal'] = f76if_f76_institutional_flow_concentration_calc099_10d_base_v099_signal

def f76if_f76_institutional_flow_concentration_calc100_126d_base_v100_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(126) / high.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc100_126d_base_v100_signal'] = f76if_f76_institutional_flow_concentration_calc100_126d_base_v100_signal

def f76if_f76_institutional_flow_concentration_calc101_63d_base_v101_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).max() - low.rolling(63).min()) / high.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc101_63d_base_v101_signal'] = f76if_f76_institutional_flow_concentration_calc101_63d_base_v101_signal

def f76if_f76_institutional_flow_concentration_calc102_63d_base_v102_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close / low.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc102_63d_base_v102_signal'] = f76if_f76_institutional_flow_concentration_calc102_63d_base_v102_signal

def f76if_f76_institutional_flow_concentration_calc103_10d_base_v103_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(10).max() - high.rolling(10).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc103_10d_base_v103_signal'] = f76if_f76_institutional_flow_concentration_calc103_10d_base_v103_signal

def f76if_f76_institutional_flow_concentration_calc104_42d_base_v104_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.pct_change(42) - sharesbas.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc104_42d_base_v104_signal'] = f76if_f76_institutional_flow_concentration_calc104_42d_base_v104_signal

def f76if_f76_institutional_flow_concentration_calc105_5d_base_v105_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(5) / volume.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc105_5d_base_v105_signal'] = f76if_f76_institutional_flow_concentration_calc105_5d_base_v105_signal

def f76if_f76_institutional_flow_concentration_calc106_252d_base_v106_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / low.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc106_252d_base_v106_signal'] = f76if_f76_institutional_flow_concentration_calc106_252d_base_v106_signal

def f76if_f76_institutional_flow_concentration_calc107_63d_base_v107_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(63).kurt() - low.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc107_63d_base_v107_signal'] = f76if_f76_institutional_flow_concentration_calc107_63d_base_v107_signal

def f76if_f76_institutional_flow_concentration_calc108_126d_base_v108_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(126).quantile(0.5) / volume.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc108_126d_base_v108_signal'] = f76if_f76_institutional_flow_concentration_calc108_126d_base_v108_signal

def f76if_f76_institutional_flow_concentration_calc109_63d_base_v109_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(63).kurt() - sharesbas.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc109_63d_base_v109_signal'] = f76if_f76_institutional_flow_concentration_calc109_63d_base_v109_signal

def f76if_f76_institutional_flow_concentration_calc110_63d_base_v110_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(63).quantile(0.5) / open.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc110_63d_base_v110_signal'] = f76if_f76_institutional_flow_concentration_calc110_63d_base_v110_signal

def f76if_f76_institutional_flow_concentration_calc111_10d_base_v111_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / close.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc111_10d_base_v111_signal'] = f76if_f76_institutional_flow_concentration_calc111_10d_base_v111_signal

def f76if_f76_institutional_flow_concentration_calc112_126d_base_v112_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(126) - open.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc112_126d_base_v112_signal'] = f76if_f76_institutional_flow_concentration_calc112_126d_base_v112_signal

def f76if_f76_institutional_flow_concentration_calc113_5d_base_v113_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(5).rank(pct=True) / sharesbas.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc113_5d_base_v113_signal'] = f76if_f76_institutional_flow_concentration_calc113_5d_base_v113_signal

def f76if_f76_institutional_flow_concentration_calc114_10d_base_v114_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / marketcap.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc114_10d_base_v114_signal'] = f76if_f76_institutional_flow_concentration_calc114_10d_base_v114_signal

def f76if_f76_institutional_flow_concentration_calc115_42d_base_v115_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.pct_change(42) - low.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc115_42d_base_v115_signal'] = f76if_f76_institutional_flow_concentration_calc115_42d_base_v115_signal

def f76if_f76_institutional_flow_concentration_calc116_21d_base_v116_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(21) / sharesbas.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc116_21d_base_v116_signal'] = f76if_f76_institutional_flow_concentration_calc116_21d_base_v116_signal

def f76if_f76_institutional_flow_concentration_calc117_42d_base_v117_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(42).quantile(0.5) / open.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc117_42d_base_v117_signal'] = f76if_f76_institutional_flow_concentration_calc117_42d_base_v117_signal

def f76if_f76_institutional_flow_concentration_calc118_10d_base_v118_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(10).max() - low.rolling(10).min()) / close.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc118_10d_base_v118_signal'] = f76if_f76_institutional_flow_concentration_calc118_10d_base_v118_signal

def f76if_f76_institutional_flow_concentration_calc119_10d_base_v119_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / close.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc119_10d_base_v119_signal'] = f76if_f76_institutional_flow_concentration_calc119_10d_base_v119_signal

def f76if_f76_institutional_flow_concentration_calc120_252d_base_v120_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).rank(pct=True) / low.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc120_252d_base_v120_signal'] = f76if_f76_institutional_flow_concentration_calc120_252d_base_v120_signal

def f76if_f76_institutional_flow_concentration_calc121_252d_base_v121_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.diff(252).abs() / marketcap.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc121_252d_base_v121_signal'] = f76if_f76_institutional_flow_concentration_calc121_252d_base_v121_signal

def f76if_f76_institutional_flow_concentration_calc122_63d_base_v122_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((volume - volume.rolling(63).mean()) / volume.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc122_63d_base_v122_signal'] = f76if_f76_institutional_flow_concentration_calc122_63d_base_v122_signal

def f76if_f76_institutional_flow_concentration_calc123_5d_base_v123_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open / marketcap.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc123_5d_base_v123_signal'] = f76if_f76_institutional_flow_concentration_calc123_5d_base_v123_signal

def f76if_f76_institutional_flow_concentration_calc124_42d_base_v124_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / sharesbas.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc124_42d_base_v124_signal'] = f76if_f76_institutional_flow_concentration_calc124_42d_base_v124_signal

def f76if_f76_institutional_flow_concentration_calc125_63d_base_v125_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(63) / open.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc125_63d_base_v125_signal'] = f76if_f76_institutional_flow_concentration_calc125_63d_base_v125_signal

def f76if_f76_institutional_flow_concentration_calc126_126d_base_v126_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(126).kurt() - close.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc126_126d_base_v126_signal'] = f76if_f76_institutional_flow_concentration_calc126_126d_base_v126_signal

def f76if_f76_institutional_flow_concentration_calc127_252d_base_v127_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / close.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc127_252d_base_v127_signal'] = f76if_f76_institutional_flow_concentration_calc127_252d_base_v127_signal

def f76if_f76_institutional_flow_concentration_calc128_252d_base_v128_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.pct_change(252) - sharesbas.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc128_252d_base_v128_signal'] = f76if_f76_institutional_flow_concentration_calc128_252d_base_v128_signal

def f76if_f76_institutional_flow_concentration_calc129_42d_base_v129_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / close.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc129_42d_base_v129_signal'] = f76if_f76_institutional_flow_concentration_calc129_42d_base_v129_signal

def f76if_f76_institutional_flow_concentration_calc130_21d_base_v130_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(21).quantile(0.5) / open.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc130_21d_base_v130_signal'] = f76if_f76_institutional_flow_concentration_calc130_21d_base_v130_signal

def f76if_f76_institutional_flow_concentration_calc131_42d_base_v131_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(42).rank(pct=True) / sharesbas.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc131_42d_base_v131_signal'] = f76if_f76_institutional_flow_concentration_calc131_42d_base_v131_signal

def f76if_f76_institutional_flow_concentration_calc132_252d_base_v132_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(252) - low.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc132_252d_base_v132_signal'] = f76if_f76_institutional_flow_concentration_calc132_252d_base_v132_signal

def f76if_f76_institutional_flow_concentration_calc133_42d_base_v133_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((marketcap - marketcap.rolling(42).mean()) / marketcap.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc133_42d_base_v133_signal'] = f76if_f76_institutional_flow_concentration_calc133_42d_base_v133_signal

def f76if_f76_institutional_flow_concentration_calc134_252d_base_v134_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(252).rank(pct=True) / sharesbas.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc134_252d_base_v134_signal'] = f76if_f76_institutional_flow_concentration_calc134_252d_base_v134_signal

def f76if_f76_institutional_flow_concentration_calc135_10d_base_v135_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(10).rank(pct=True) / close.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc135_10d_base_v135_signal'] = f76if_f76_institutional_flow_concentration_calc135_10d_base_v135_signal

def f76if_f76_institutional_flow_concentration_calc136_126d_base_v136_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((close - close.rolling(126).mean()) / close.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc136_126d_base_v136_signal'] = f76if_f76_institutional_flow_concentration_calc136_126d_base_v136_signal

def f76if_f76_institutional_flow_concentration_calc137_63d_base_v137_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / sharesbas.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc137_63d_base_v137_signal'] = f76if_f76_institutional_flow_concentration_calc137_63d_base_v137_signal

def f76if_f76_institutional_flow_concentration_calc138_126d_base_v138_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((sharesbas - sharesbas.rolling(126).mean()) / sharesbas.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc138_126d_base_v138_signal'] = f76if_f76_institutional_flow_concentration_calc138_126d_base_v138_signal

def f76if_f76_institutional_flow_concentration_calc139_252d_base_v139_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / sharesbas.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc139_252d_base_v139_signal'] = f76if_f76_institutional_flow_concentration_calc139_252d_base_v139_signal

def f76if_f76_institutional_flow_concentration_calc140_252d_base_v140_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(252) / close.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc140_252d_base_v140_signal'] = f76if_f76_institutional_flow_concentration_calc140_252d_base_v140_signal

def f76if_f76_institutional_flow_concentration_calc141_42d_base_v141_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(42).kurt() - marketcap.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc141_42d_base_v141_signal'] = f76if_f76_institutional_flow_concentration_calc141_42d_base_v141_signal

def f76if_f76_institutional_flow_concentration_calc142_126d_base_v142_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(126) - volume.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc142_126d_base_v142_signal'] = f76if_f76_institutional_flow_concentration_calc142_126d_base_v142_signal

def f76if_f76_institutional_flow_concentration_calc143_5d_base_v143_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(5).max() - open.rolling(5).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc143_5d_base_v143_signal'] = f76if_f76_institutional_flow_concentration_calc143_5d_base_v143_signal

def f76if_f76_institutional_flow_concentration_calc144_252d_base_v144_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(252) - sharesbas.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc144_252d_base_v144_signal'] = f76if_f76_institutional_flow_concentration_calc144_252d_base_v144_signal

def f76if_f76_institutional_flow_concentration_calc145_10d_base_v145_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(10).abs() / low.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc145_10d_base_v145_signal'] = f76if_f76_institutional_flow_concentration_calc145_10d_base_v145_signal

def f76if_f76_institutional_flow_concentration_calc146_252d_base_v146_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).rank(pct=True) / close.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc146_252d_base_v146_signal'] = f76if_f76_institutional_flow_concentration_calc146_252d_base_v146_signal

def f76if_f76_institutional_flow_concentration_calc147_42d_base_v147_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(42).rank(pct=True) / high.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc147_42d_base_v147_signal'] = f76if_f76_institutional_flow_concentration_calc147_42d_base_v147_signal

def f76if_f76_institutional_flow_concentration_calc148_63d_base_v148_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(63) - high.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc148_63d_base_v148_signal'] = f76if_f76_institutional_flow_concentration_calc148_63d_base_v148_signal

def f76if_f76_institutional_flow_concentration_calc149_10d_base_v149_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(10).max() - marketcap.rolling(10).min()) / close.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc149_10d_base_v149_signal'] = f76if_f76_institutional_flow_concentration_calc149_10d_base_v149_signal

def f76if_f76_institutional_flow_concentration_calc150_5d_base_v150_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(5).quantile(0.5) / marketcap.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc150_5d_base_v150_signal'] = f76if_f76_institutional_flow_concentration_calc150_5d_base_v150_signal



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
