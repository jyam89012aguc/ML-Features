import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f70le_f70_liabilities_to_equity_momentum_calc076_252d_base_v076_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(252).std() / (equity / marketcap.replace(0, np.nan)).rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc076_252d_base_v076_signal'] = f70le_f70_liabilities_to_equity_momentum_calc076_252d_base_v076_signal

def f70le_f70_liabilities_to_equity_momentum_calc077_5d_base_v077_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(5).std() / (equity / marketcap.replace(0, np.nan)).rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc077_5d_base_v077_signal'] = f70le_f70_liabilities_to_equity_momentum_calc077_5d_base_v077_signal

def f70le_f70_liabilities_to_equity_momentum_calc078_10d_base_v078_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(10).std() / (equity / marketcap.replace(0, np.nan)).rolling(10).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc078_10d_base_v078_signal'] = f70le_f70_liabilities_to_equity_momentum_calc078_10d_base_v078_signal

def f70le_f70_liabilities_to_equity_momentum_calc079_21d_base_v079_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(21).std() / (equity / marketcap.replace(0, np.nan)).rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc079_21d_base_v079_signal'] = f70le_f70_liabilities_to_equity_momentum_calc079_21d_base_v079_signal

def f70le_f70_liabilities_to_equity_momentum_calc080_42d_base_v080_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(42).std() / (equity / marketcap.replace(0, np.nan)).rolling(42).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc080_42d_base_v080_signal'] = f70le_f70_liabilities_to_equity_momentum_calc080_42d_base_v080_signal

def f70le_f70_liabilities_to_equity_momentum_calc081_63d_base_v081_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(63).mean().diff(100).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc081_63d_base_v081_signal'] = f70le_f70_liabilities_to_equity_momentum_calc081_63d_base_v081_signal

def f70le_f70_liabilities_to_equity_momentum_calc082_126d_base_v082_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(126).mean().diff(150).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc082_126d_base_v082_signal'] = f70le_f70_liabilities_to_equity_momentum_calc082_126d_base_v082_signal

def f70le_f70_liabilities_to_equity_momentum_calc083_252d_base_v083_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(252).mean().diff(200).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc083_252d_base_v083_signal'] = f70le_f70_liabilities_to_equity_momentum_calc083_252d_base_v083_signal

def f70le_f70_liabilities_to_equity_momentum_calc084_5d_base_v084_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(5).mean().diff(15).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc084_5d_base_v084_signal'] = f70le_f70_liabilities_to_equity_momentum_calc084_5d_base_v084_signal

def f70le_f70_liabilities_to_equity_momentum_calc085_10d_base_v085_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(10).mean().diff(30).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc085_10d_base_v085_signal'] = f70le_f70_liabilities_to_equity_momentum_calc085_10d_base_v085_signal

def f70le_f70_liabilities_to_equity_momentum_calc086_21d_base_v086_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(21).mean().diff(50).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc086_21d_base_v086_signal'] = f70le_f70_liabilities_to_equity_momentum_calc086_21d_base_v086_signal

def f70le_f70_liabilities_to_equity_momentum_calc087_42d_base_v087_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(42).mean().diff(80).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc087_42d_base_v087_signal'] = f70le_f70_liabilities_to_equity_momentum_calc087_42d_base_v087_signal

def f70le_f70_liabilities_to_equity_momentum_calc088_63d_base_v088_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(63).mean().diff(100).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc088_63d_base_v088_signal'] = f70le_f70_liabilities_to_equity_momentum_calc088_63d_base_v088_signal

def f70le_f70_liabilities_to_equity_momentum_calc089_126d_base_v089_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(126).mean().diff(150).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc089_126d_base_v089_signal'] = f70le_f70_liabilities_to_equity_momentum_calc089_126d_base_v089_signal

def f70le_f70_liabilities_to_equity_momentum_calc090_252d_base_v090_signal(liabilities, equity, debt):
    res = ((liabilities + debt) / equity.replace(0, np.nan)).rolling(252).mean().diff(200).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc090_252d_base_v090_signal'] = f70le_f70_liabilities_to_equity_momentum_calc090_252d_base_v090_signal

def f70le_f70_liabilities_to_equity_momentum_calc091_5d_base_v091_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(5).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc091_5d_base_v091_signal'] = f70le_f70_liabilities_to_equity_momentum_calc091_5d_base_v091_signal

def f70le_f70_liabilities_to_equity_momentum_calc092_10d_base_v092_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(10).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc092_10d_base_v092_signal'] = f70le_f70_liabilities_to_equity_momentum_calc092_10d_base_v092_signal

def f70le_f70_liabilities_to_equity_momentum_calc093_21d_base_v093_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(21).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc093_21d_base_v093_signal'] = f70le_f70_liabilities_to_equity_momentum_calc093_21d_base_v093_signal

def f70le_f70_liabilities_to_equity_momentum_calc094_42d_base_v094_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(42).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc094_42d_base_v094_signal'] = f70le_f70_liabilities_to_equity_momentum_calc094_42d_base_v094_signal

def f70le_f70_liabilities_to_equity_momentum_calc095_63d_base_v095_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(63).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc095_63d_base_v095_signal'] = f70le_f70_liabilities_to_equity_momentum_calc095_63d_base_v095_signal

def f70le_f70_liabilities_to_equity_momentum_calc096_126d_base_v096_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(126).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc096_126d_base_v096_signal'] = f70le_f70_liabilities_to_equity_momentum_calc096_126d_base_v096_signal

def f70le_f70_liabilities_to_equity_momentum_calc097_252d_base_v097_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(252).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc097_252d_base_v097_signal'] = f70le_f70_liabilities_to_equity_momentum_calc097_252d_base_v097_signal

def f70le_f70_liabilities_to_equity_momentum_calc098_5d_base_v098_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(5).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc098_5d_base_v098_signal'] = f70le_f70_liabilities_to_equity_momentum_calc098_5d_base_v098_signal

def f70le_f70_liabilities_to_equity_momentum_calc099_10d_base_v099_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(10).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc099_10d_base_v099_signal'] = f70le_f70_liabilities_to_equity_momentum_calc099_10d_base_v099_signal

def f70le_f70_liabilities_to_equity_momentum_calc100_21d_base_v100_signal(liabilities, assets):
    res = (liabilities / (assets - liabilities).replace(0, np.nan)).rolling(21).quantile(0.5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc100_21d_base_v100_signal'] = f70le_f70_liabilities_to_equity_momentum_calc100_21d_base_v100_signal

def f70le_f70_liabilities_to_equity_momentum_calc101_42d_base_v101_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(42) - (equity / revenue.replace(0, np.nan)).pct_change(42).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc101_42d_base_v101_signal'] = f70le_f70_liabilities_to_equity_momentum_calc101_42d_base_v101_signal

def f70le_f70_liabilities_to_equity_momentum_calc102_63d_base_v102_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(63) - (equity / revenue.replace(0, np.nan)).pct_change(63).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc102_63d_base_v102_signal'] = f70le_f70_liabilities_to_equity_momentum_calc102_63d_base_v102_signal

def f70le_f70_liabilities_to_equity_momentum_calc103_126d_base_v103_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(126) - (equity / revenue.replace(0, np.nan)).pct_change(126).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc103_126d_base_v103_signal'] = f70le_f70_liabilities_to_equity_momentum_calc103_126d_base_v103_signal

def f70le_f70_liabilities_to_equity_momentum_calc104_252d_base_v104_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(252) - (equity / revenue.replace(0, np.nan)).pct_change(252).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc104_252d_base_v104_signal'] = f70le_f70_liabilities_to_equity_momentum_calc104_252d_base_v104_signal

def f70le_f70_liabilities_to_equity_momentum_calc105_5d_base_v105_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(5) - (equity / revenue.replace(0, np.nan)).pct_change(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc105_5d_base_v105_signal'] = f70le_f70_liabilities_to_equity_momentum_calc105_5d_base_v105_signal

def f70le_f70_liabilities_to_equity_momentum_calc106_10d_base_v106_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(10) - (equity / revenue.replace(0, np.nan)).pct_change(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc106_10d_base_v106_signal'] = f70le_f70_liabilities_to_equity_momentum_calc106_10d_base_v106_signal

def f70le_f70_liabilities_to_equity_momentum_calc107_21d_base_v107_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(21) - (equity / revenue.replace(0, np.nan)).pct_change(21).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc107_21d_base_v107_signal'] = f70le_f70_liabilities_to_equity_momentum_calc107_21d_base_v107_signal

def f70le_f70_liabilities_to_equity_momentum_calc108_42d_base_v108_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(42) - (equity / revenue.replace(0, np.nan)).pct_change(42).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc108_42d_base_v108_signal'] = f70le_f70_liabilities_to_equity_momentum_calc108_42d_base_v108_signal

def f70le_f70_liabilities_to_equity_momentum_calc109_63d_base_v109_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(63) - (equity / revenue.replace(0, np.nan)).pct_change(63).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc109_63d_base_v109_signal'] = f70le_f70_liabilities_to_equity_momentum_calc109_63d_base_v109_signal

def f70le_f70_liabilities_to_equity_momentum_calc110_126d_base_v110_signal(liabilities, equity, revenue):
    res = (liabilities / revenue.replace(0, np.nan)).pct_change(126) - (equity / revenue.replace(0, np.nan)).pct_change(126).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc110_126d_base_v110_signal'] = f70le_f70_liabilities_to_equity_momentum_calc110_126d_base_v110_signal

def f70le_f70_liabilities_to_equity_momentum_calc111_252d_base_v111_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(252).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc111_252d_base_v111_signal'] = f70le_f70_liabilities_to_equity_momentum_calc111_252d_base_v111_signal

def f70le_f70_liabilities_to_equity_momentum_calc112_5d_base_v112_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(5).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(5).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc112_5d_base_v112_signal'] = f70le_f70_liabilities_to_equity_momentum_calc112_5d_base_v112_signal

def f70le_f70_liabilities_to_equity_momentum_calc113_10d_base_v113_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(10).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(10).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc113_10d_base_v113_signal'] = f70le_f70_liabilities_to_equity_momentum_calc113_10d_base_v113_signal

def f70le_f70_liabilities_to_equity_momentum_calc114_21d_base_v114_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(21).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc114_21d_base_v114_signal'] = f70le_f70_liabilities_to_equity_momentum_calc114_21d_base_v114_signal

def f70le_f70_liabilities_to_equity_momentum_calc115_42d_base_v115_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(42).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(42).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc115_42d_base_v115_signal'] = f70le_f70_liabilities_to_equity_momentum_calc115_42d_base_v115_signal

def f70le_f70_liabilities_to_equity_momentum_calc116_63d_base_v116_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(63).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(63).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc116_63d_base_v116_signal'] = f70le_f70_liabilities_to_equity_momentum_calc116_63d_base_v116_signal

def f70le_f70_liabilities_to_equity_momentum_calc117_126d_base_v117_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(126).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(126).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc117_126d_base_v117_signal'] = f70le_f70_liabilities_to_equity_momentum_calc117_126d_base_v117_signal

def f70le_f70_liabilities_to_equity_momentum_calc118_252d_base_v118_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(252).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc118_252d_base_v118_signal'] = f70le_f70_liabilities_to_equity_momentum_calc118_252d_base_v118_signal

def f70le_f70_liabilities_to_equity_momentum_calc119_5d_base_v119_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(5).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(5).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc119_5d_base_v119_signal'] = f70le_f70_liabilities_to_equity_momentum_calc119_5d_base_v119_signal

def f70le_f70_liabilities_to_equity_momentum_calc120_10d_base_v120_signal(liabilities, equity, netinc):
    res = (liabilities / netinc.replace(0, np.nan).abs()).rolling(10).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(10).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc120_10d_base_v120_signal'] = f70le_f70_liabilities_to_equity_momentum_calc120_10d_base_v120_signal

def f70le_f70_liabilities_to_equity_momentum_calc121_21d_base_v121_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(21).std().pct_change(50).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc121_21d_base_v121_signal'] = f70le_f70_liabilities_to_equity_momentum_calc121_21d_base_v121_signal

def f70le_f70_liabilities_to_equity_momentum_calc122_42d_base_v122_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(42).std().pct_change(80).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc122_42d_base_v122_signal'] = f70le_f70_liabilities_to_equity_momentum_calc122_42d_base_v122_signal

def f70le_f70_liabilities_to_equity_momentum_calc123_63d_base_v123_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(63).std().pct_change(100).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc123_63d_base_v123_signal'] = f70le_f70_liabilities_to_equity_momentum_calc123_63d_base_v123_signal

def f70le_f70_liabilities_to_equity_momentum_calc124_126d_base_v124_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(126).std().pct_change(150).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc124_126d_base_v124_signal'] = f70le_f70_liabilities_to_equity_momentum_calc124_126d_base_v124_signal

def f70le_f70_liabilities_to_equity_momentum_calc125_252d_base_v125_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(252).std().pct_change(200).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc125_252d_base_v125_signal'] = f70le_f70_liabilities_to_equity_momentum_calc125_252d_base_v125_signal

def f70le_f70_liabilities_to_equity_momentum_calc126_5d_base_v126_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(5).std().pct_change(15).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc126_5d_base_v126_signal'] = f70le_f70_liabilities_to_equity_momentum_calc126_5d_base_v126_signal

def f70le_f70_liabilities_to_equity_momentum_calc127_10d_base_v127_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(10).std().pct_change(30).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc127_10d_base_v127_signal'] = f70le_f70_liabilities_to_equity_momentum_calc127_10d_base_v127_signal

def f70le_f70_liabilities_to_equity_momentum_calc128_21d_base_v128_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(21).std().pct_change(50).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc128_21d_base_v128_signal'] = f70le_f70_liabilities_to_equity_momentum_calc128_21d_base_v128_signal

def f70le_f70_liabilities_to_equity_momentum_calc129_42d_base_v129_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(42).std().pct_change(80).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc129_42d_base_v129_signal'] = f70le_f70_liabilities_to_equity_momentum_calc129_42d_base_v129_signal

def f70le_f70_liabilities_to_equity_momentum_calc130_63d_base_v130_signal(liabilities, ebitda):
    res = (liabilities / ebitda.replace(0, np.nan).abs()).rolling(63).std().pct_change(100).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc130_63d_base_v130_signal'] = f70le_f70_liabilities_to_equity_momentum_calc130_63d_base_v130_signal

def f70le_f70_liabilities_to_equity_momentum_calc131_126d_base_v131_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(126).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(126).mean().rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc131_126d_base_v131_signal'] = f70le_f70_liabilities_to_equity_momentum_calc131_126d_base_v131_signal

def f70le_f70_liabilities_to_equity_momentum_calc132_252d_base_v132_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(252).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(252).mean().rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc132_252d_base_v132_signal'] = f70le_f70_liabilities_to_equity_momentum_calc132_252d_base_v132_signal

def f70le_f70_liabilities_to_equity_momentum_calc133_5d_base_v133_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(5).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(5).mean().rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc133_5d_base_v133_signal'] = f70le_f70_liabilities_to_equity_momentum_calc133_5d_base_v133_signal

def f70le_f70_liabilities_to_equity_momentum_calc134_10d_base_v134_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(10).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(10).mean().rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc134_10d_base_v134_signal'] = f70le_f70_liabilities_to_equity_momentum_calc134_10d_base_v134_signal

def f70le_f70_liabilities_to_equity_momentum_calc135_21d_base_v135_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(21).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(21).mean().rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc135_21d_base_v135_signal'] = f70le_f70_liabilities_to_equity_momentum_calc135_21d_base_v135_signal

def f70le_f70_liabilities_to_equity_momentum_calc136_42d_base_v136_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(42).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(42).mean().rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc136_42d_base_v136_signal'] = f70le_f70_liabilities_to_equity_momentum_calc136_42d_base_v136_signal

def f70le_f70_liabilities_to_equity_momentum_calc137_63d_base_v137_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(63).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(63).mean().rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc137_63d_base_v137_signal'] = f70le_f70_liabilities_to_equity_momentum_calc137_63d_base_v137_signal

def f70le_f70_liabilities_to_equity_momentum_calc138_126d_base_v138_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(126).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(126).mean().rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc138_126d_base_v138_signal'] = f70le_f70_liabilities_to_equity_momentum_calc138_126d_base_v138_signal

def f70le_f70_liabilities_to_equity_momentum_calc139_252d_base_v139_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(252).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(252).mean().rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc139_252d_base_v139_signal'] = f70le_f70_liabilities_to_equity_momentum_calc139_252d_base_v139_signal

def f70le_f70_liabilities_to_equity_momentum_calc140_5d_base_v140_signal(liabilities, equity, workingcapital):
    res = (liabilities / workingcapital.replace(0, np.nan)).rolling(5).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(5).mean().rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc140_5d_base_v140_signal'] = f70le_f70_liabilities_to_equity_momentum_calc140_5d_base_v140_signal

def f70le_f70_liabilities_to_equity_momentum_calc141_10d_base_v141_signal(liabilities, equity):
    res = (liabilities.pct_change(10) / equity.pct_change(10).replace(0, np.nan)).rolling(30).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc141_10d_base_v141_signal'] = f70le_f70_liabilities_to_equity_momentum_calc141_10d_base_v141_signal

def f70le_f70_liabilities_to_equity_momentum_calc142_21d_base_v142_signal(liabilities, equity):
    res = (liabilities.pct_change(21) / equity.pct_change(21).replace(0, np.nan)).rolling(50).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc142_21d_base_v142_signal'] = f70le_f70_liabilities_to_equity_momentum_calc142_21d_base_v142_signal

def f70le_f70_liabilities_to_equity_momentum_calc143_42d_base_v143_signal(liabilities, equity):
    res = (liabilities.pct_change(42) / equity.pct_change(42).replace(0, np.nan)).rolling(80).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc143_42d_base_v143_signal'] = f70le_f70_liabilities_to_equity_momentum_calc143_42d_base_v143_signal

def f70le_f70_liabilities_to_equity_momentum_calc144_63d_base_v144_signal(liabilities, equity):
    res = (liabilities.pct_change(63) / equity.pct_change(63).replace(0, np.nan)).rolling(100).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc144_63d_base_v144_signal'] = f70le_f70_liabilities_to_equity_momentum_calc144_63d_base_v144_signal

def f70le_f70_liabilities_to_equity_momentum_calc145_126d_base_v145_signal(liabilities, equity):
    res = (liabilities.pct_change(126) / equity.pct_change(126).replace(0, np.nan)).rolling(150).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc145_126d_base_v145_signal'] = f70le_f70_liabilities_to_equity_momentum_calc145_126d_base_v145_signal

def f70le_f70_liabilities_to_equity_momentum_calc146_252d_base_v146_signal(liabilities, equity):
    res = (liabilities.pct_change(252) / equity.pct_change(252).replace(0, np.nan)).rolling(200).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc146_252d_base_v146_signal'] = f70le_f70_liabilities_to_equity_momentum_calc146_252d_base_v146_signal

def f70le_f70_liabilities_to_equity_momentum_calc147_5d_base_v147_signal(liabilities, equity):
    res = (liabilities.pct_change(5) / equity.pct_change(5).replace(0, np.nan)).rolling(15).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc147_5d_base_v147_signal'] = f70le_f70_liabilities_to_equity_momentum_calc147_5d_base_v147_signal

def f70le_f70_liabilities_to_equity_momentum_calc148_10d_base_v148_signal(liabilities, equity):
    res = (liabilities.pct_change(10) / equity.pct_change(10).replace(0, np.nan)).rolling(30).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc148_10d_base_v148_signal'] = f70le_f70_liabilities_to_equity_momentum_calc148_10d_base_v148_signal

def f70le_f70_liabilities_to_equity_momentum_calc149_21d_base_v149_signal(liabilities, equity):
    res = (liabilities.pct_change(21) / equity.pct_change(21).replace(0, np.nan)).rolling(50).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc149_21d_base_v149_signal'] = f70le_f70_liabilities_to_equity_momentum_calc149_21d_base_v149_signal

def f70le_f70_liabilities_to_equity_momentum_calc150_42d_base_v150_signal(liabilities, equity):
    res = (liabilities.pct_change(42) / equity.pct_change(42).replace(0, np.nan)).rolling(80).mean().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc150_42d_base_v150_signal'] = f70le_f70_liabilities_to_equity_momentum_calc150_42d_base_v150_signal

