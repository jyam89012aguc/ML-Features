import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f197n_f197_net_income_to_capex_efficiency_regime_calc076_126d_base_v076_signal(assets, netinc):
    res = (netinc / (assets + 4.7730)).rolling(105).min().rolling(42).mean() * 0.732126
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc076_126d_base_v076_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc076_126d_base_v076_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc077_5d_base_v077_signal(capex, netinc):
    res = (netinc / (capex + 0.7374)).rolling(10).std().rolling(10).mean().rolling(126).std().pct_change(5) * 0.146431
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc077_5d_base_v077_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc077_5d_base_v077_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc078_200d_base_v078_signal(netinc, revenue):
    res = (netinc.diff(18) / (revenue.shift(7) + 9.3809)).rolling(5).mean().rolling(126).skew() * 0.462395
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc078_200d_base_v078_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc078_200d_base_v078_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc079_105d_base_v079_signal(assets, netinc):
    res = (netinc.diff(9) / (assets.shift(3) + 6.5092)).rolling(84).min().rolling(252).min() * 0.847241
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc079_105d_base_v079_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc079_105d_base_v079_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc080_150d_base_v080_signal(netinc, revenue):
    res = (netinc.diff(13) / (revenue.shift(7) + 3.8914)).rolling(10).kurt().rolling(42).std().rolling(5).kurt() * 0.830752
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc080_150d_base_v080_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc080_150d_base_v080_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc081_42d_base_v081_signal(assets, netinc):
    res = (((netinc.diff(11) / (assets.shift(4) + 5.4009)).rolling(126).max().rolling(21).std().rolling(150).skew() - (netinc.diff(11) / (assets.shift(4) + 5.4009)).rolling(126).max().rolling(21).std().rolling(150).skew().rolling(5).mean()) / (netinc.diff(11) / (assets.shift(4) + 5.4009)).rolling(126).max().rolling(21).std().rolling(150).skew().rolling(5).std()) * 0.295594
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc081_42d_base_v081_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc081_42d_base_v081_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc082_200d_base_v082_signal(assets, fcf):
    res = ((assets / (fcf + 3.4037)).rolling(21).max().pct_change(10) / (assets / (fcf + 3.4037)).rolling(21).max().pct_change(10).rolling(5).max()) * 0.569192
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc082_200d_base_v082_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc082_200d_base_v082_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc083_200d_base_v083_signal(assets, fcf):
    res = (fcf.diff(20) / (assets.shift(4) + 8.8666)).rolling(105).skew().pct_change(84).rolling(10).skew() * 0.069250
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc083_200d_base_v083_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc083_200d_base_v083_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc084_21d_base_v084_signal(capex, netinc):
    res = ((netinc / (capex + 3.9259)) / (netinc / (capex + 3.9259)).rolling(126).max()).rolling(10).min().rolling(126).kurt() * 0.820719
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc084_21d_base_v084_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc084_21d_base_v084_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc085_10d_base_v085_signal(capex, netinc):
    res = (netinc.diff(9) / (capex.shift(8) + 8.1498)).rolling(21).mean().pct_change(5) * 0.689457
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc085_10d_base_v085_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc085_10d_base_v085_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc086_10d_base_v086_signal(capex, fcf):
    res = (fcf.diff(13) / (capex.shift(7) + 8.0253)).rolling(42).min().rolling(252).min().rolling(10).var().rolling(252).min() * 0.600156
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc086_10d_base_v086_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc086_10d_base_v086_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc087_105d_base_v087_signal(netinc, revenue):
    res = (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(105).max().rolling(105).var().rolling(63).std() * 0.254153
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc087_105d_base_v087_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc087_105d_base_v087_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc088_5d_base_v088_signal(assets, netinc):
    res = (netinc.diff(7) / (assets.shift(1) + 1.8947)).pct_change(105).rolling(5).std().rolling(42).max() * 0.466596
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc088_5d_base_v088_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc088_5d_base_v088_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc089_150d_base_v089_signal(capex, netinc):
    res = ((netinc / (capex + 2.4658)).rolling(126).max() / (netinc / (capex + 2.4658)).rolling(126).max().rolling(84).max()) * 0.459917
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc089_150d_base_v089_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc089_150d_base_v089_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc090_63d_base_v090_signal(capex, netinc):
    res = (((capex / (netinc + 3.4242)).rolling(150).kurt() - (capex / (netinc + 3.4242)).rolling(150).kurt().rolling(200).mean()) / (capex / (netinc + 3.4242)).rolling(150).kurt().rolling(200).std()).rolling(84).mean().rolling(200).min() * 0.049511
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc090_63d_base_v090_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc090_63d_base_v090_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc091_84d_base_v091_signal(assets, netinc):
    res = (assets / (netinc + 0.9773)).rolling(10).mean().rolling(252).max().rolling(150).mean() * 0.978221
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc091_84d_base_v091_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc091_84d_base_v091_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc092_10d_base_v092_signal(netinc, revenue):
    res = ((((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max().rolling(10).max()).rolling(5).kurt() - ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max().rolling(10).max()).rolling(5).kurt().rolling(63).mean()) / ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max().rolling(10).max()).rolling(5).kurt().rolling(63).std()) * 0.976821
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc092_10d_base_v092_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc092_10d_base_v092_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc093_84d_base_v093_signal(netinc, revenue):
    res = (netinc / (revenue + 3.0361)).rolling(126).max().rolling(63).min().rolling(42).skew() * 0.213977
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc093_84d_base_v093_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc093_84d_base_v093_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc094_84d_base_v094_signal(equity, netinc):
    res = ((netinc.diff(3) / (equity.shift(5) + 3.1710)).rolling(42).max().diff(21) / (netinc.diff(3) / (equity.shift(5) + 3.1710)).rolling(42).max().diff(21).rolling(105).max()) * 0.914013
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc094_84d_base_v094_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc094_84d_base_v094_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc095_84d_base_v095_signal(assets, fcf):
    res = (((fcf / (assets + 8.6720)) - (fcf / (assets + 8.6720)).rolling(105).mean()) / (fcf / (assets + 8.6720)).rolling(105).std()).rolling(105).skew().rolling(200).kurt() * 0.904991
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc095_84d_base_v095_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc095_84d_base_v095_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc096_10d_base_v096_signal(capex, fcf):
    res = (((fcf / (capex + 8.6534)).rolling(252).var().rolling(105).min() - (fcf / (capex + 8.6534)).rolling(252).var().rolling(105).min().rolling(10).mean()) / (fcf / (capex + 8.6534)).rolling(252).var().rolling(105).min().rolling(10).std()) * 0.682674
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc096_10d_base_v096_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc096_10d_base_v096_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc097_5d_base_v097_signal(capex, netinc):
    res = (capex / (netinc + 7.9435)).rolling(84).min().rolling(200).var().rolling(5).skew() * 0.479569
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc097_5d_base_v097_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc097_5d_base_v097_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc098_21d_base_v098_signal(assets, netinc):
    res = (netinc.diff(11) / (assets.shift(7) + 8.5853)).diff(63).rolling(21).mean().diff(42).rolling(200).std() * 0.788808
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc098_21d_base_v098_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc098_21d_base_v098_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc099_42d_base_v099_signal(equity, netinc):
    res = (netinc / (equity + 8.6245)).rolling(21).kurt().rolling(42).kurt().rolling(150).std() * 0.725028
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc099_42d_base_v099_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc099_42d_base_v099_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc100_105d_base_v100_signal(netinc, revenue):
    res = (((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).kurt() - (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).kurt().rolling(21).mean()) / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).kurt().rolling(21).std()).rolling(126).mean().rolling(5).mean() * 0.220534
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc100_105d_base_v100_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc100_105d_base_v100_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc101_84d_base_v101_signal(equity, netinc):
    res = ((((((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min() - ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).mean()) / ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).std()) - ((((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min() - ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).mean()) / ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).std()).rolling(150).mean()) / ((((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min() - ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).mean()) / ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)) / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).max()).rolling(5).min().rolling(10).std()).rolling(150).std()) * 0.762855
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc101_84d_base_v101_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc101_84d_base_v101_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc102_126d_base_v102_signal(assets, fcf):
    res = ((fcf.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(105) / (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(105).rolling(10).max()) * 0.502283
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc102_126d_base_v102_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc102_126d_base_v102_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc103_84d_base_v103_signal(capex, netinc):
    res = (((netinc.diff(18) / (capex.shift(4) + 0.1513)) - (netinc.diff(18) / (capex.shift(4) + 0.1513)).rolling(252).mean()) / (netinc.diff(18) / (capex.shift(4) + 0.1513)).rolling(252).std()).rolling(126).kurt() * 0.947949
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc103_84d_base_v103_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc103_84d_base_v103_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc104_42d_base_v104_signal(netinc, revenue):
    res = ((netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(200).min() / (netinc.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(200).min().rolling(63).max()) * 0.569774
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc104_42d_base_v104_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc104_42d_base_v104_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc105_63d_base_v105_signal(assets, fcf):
    res = (fcf / (assets + 6.7824)).pct_change(200).rolling(42).skew().pct_change(63).rolling(84).skew() * 0.310764
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc105_63d_base_v105_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc105_63d_base_v105_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc106_10d_base_v106_signal(equity, netinc):
    res = ((netinc.diff(4) / (equity.shift(9) + 0.5342)).rolling(21).mean() / (netinc.diff(4) / (equity.shift(9) + 0.5342)).rolling(21).mean().rolling(252).max()) * 0.510001
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc106_10d_base_v106_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc106_10d_base_v106_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc107_200d_base_v107_signal(capex, netinc):
    res = ((((netinc.replace(0, np.nan) / capex.replace(0, np.nan)) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).max()) - ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).max()).rolling(126).mean()) / ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).max()).rolling(126).std()).diff(150).rolling(200).kurt() * 0.185516
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc107_200d_base_v107_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc107_200d_base_v107_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc108_10d_base_v108_signal(capex, fcf):
    res = (fcf.diff(15) / (capex.shift(3) + 1.6561)).rolling(126).skew().rolling(126).var().rolling(10).mean().rolling(252).std() * 0.136573
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc108_10d_base_v108_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc108_10d_base_v108_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc109_63d_base_v109_signal(capex, netinc):
    res = (((netinc.diff(15) / (capex.shift(6) + 3.6347)).diff(200) - (netinc.diff(15) / (capex.shift(6) + 3.6347)).diff(200).rolling(105).mean()) / (netinc.diff(15) / (capex.shift(6) + 3.6347)).diff(200).rolling(105).std()) * 0.916250
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc109_63d_base_v109_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc109_63d_base_v109_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc110_42d_base_v110_signal(assets, netinc):
    res = (((netinc.diff(11) / (assets.shift(2) + 2.1393)).pct_change(21).rolling(42).std() - (netinc.diff(11) / (assets.shift(2) + 2.1393)).pct_change(21).rolling(42).std().rolling(5).mean()) / (netinc.diff(11) / (assets.shift(2) + 2.1393)).pct_change(21).rolling(42).std().rolling(5).std()).diff(5) * 0.555256
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc110_42d_base_v110_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc110_42d_base_v110_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc111_105d_base_v111_signal(capex, fcf):
    res = (fcf.diff(11) / (capex.shift(5) + 6.4423)).pct_change(21).rolling(150).min().diff(150) * 0.647963
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc111_105d_base_v111_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc111_105d_base_v111_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc112_5d_base_v112_signal(netinc, revenue):
    res = (netinc.diff(20) / (revenue.shift(1) + 5.5662)).rolling(150).kurt().rolling(105).mean().pct_change(63) * 0.450177
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc112_5d_base_v112_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc112_5d_base_v112_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc113_5d_base_v113_signal(assets, netinc):
    res = (netinc.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).kurt().rolling(150).std().rolling(252).min().rolling(21).max() * 0.366162
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc113_5d_base_v113_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc113_5d_base_v113_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc114_10d_base_v114_signal(assets, fcf):
    res = (((fcf.diff(4) / (assets.shift(9) + 3.0419)).rolling(200).min().rolling(21).var() - (fcf.diff(4) / (assets.shift(9) + 3.0419)).rolling(200).min().rolling(21).var().rolling(63).mean()) / (fcf.diff(4) / (assets.shift(9) + 3.0419)).rolling(200).min().rolling(21).var().rolling(63).std()).rolling(5).min() * 0.323035
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc114_10d_base_v114_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc114_10d_base_v114_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc115_105d_base_v115_signal(assets, netinc):
    res = (assets / (netinc + 6.9262)).pct_change(21).rolling(84).kurt().rolling(63).std() * 0.386910
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc115_105d_base_v115_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc115_105d_base_v115_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc116_105d_base_v116_signal(netinc, revenue):
    res = ((netinc / (revenue + 8.8968)).rolling(63).std().diff(200) / (netinc / (revenue + 8.8968)).rolling(63).std().diff(200).rolling(84).max()).rolling(150).max() * 0.597587
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc116_105d_base_v116_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc116_105d_base_v116_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc117_200d_base_v117_signal(capex, fcf):
    res = (fcf.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(5).skew().rolling(21).kurt() * 0.785057
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc117_200d_base_v117_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc117_200d_base_v117_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc118_63d_base_v118_signal(equity, netinc):
    res = (netinc.diff(2) / (equity.shift(4) + 8.0130)).rolling(21).skew().rolling(200).max().rolling(5).var().rolling(126).min() * 0.817033
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc118_63d_base_v118_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc118_63d_base_v118_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc119_252d_base_v119_signal(capex, netinc):
    res = (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(126).max().rolling(126).max().pct_change(63).rolling(126).mean() * 0.193043
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc119_252d_base_v119_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc119_252d_base_v119_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc120_84d_base_v120_signal(capex, netinc):
    res = (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(84).rolling(126).skew() * 0.685345
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc120_84d_base_v120_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc120_84d_base_v120_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc121_252d_base_v121_signal(assets, fcf):
    res = (((fcf.diff(13) / (assets.shift(2) + 4.7238)).rolling(42).mean().rolling(150).kurt() - (fcf.diff(13) / (assets.shift(2) + 4.7238)).rolling(42).mean().rolling(150).kurt().rolling(63).mean()) / (fcf.diff(13) / (assets.shift(2) + 4.7238)).rolling(42).mean().rolling(150).kurt().rolling(63).std()).pct_change(42) * 0.153637
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc121_252d_base_v121_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc121_252d_base_v121_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc122_252d_base_v122_signal(capex, netinc):
    res = (netinc / (capex + 9.4101)).pct_change(42).rolling(63).std() * 0.642776
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc122_252d_base_v122_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc122_252d_base_v122_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc123_105d_base_v123_signal(netinc, revenue):
    res = (revenue / (netinc + 9.5502)).rolling(105).kurt().rolling(63).max().pct_change(5) * 0.592332
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc123_105d_base_v123_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc123_105d_base_v123_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc124_252d_base_v124_signal(netinc, revenue):
    res = (revenue / (netinc + 3.0676)).rolling(105).kurt().rolling(84).skew() * 0.102345
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc124_252d_base_v124_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc124_252d_base_v124_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc125_252d_base_v125_signal(capex, fcf):
    res = (fcf.diff(2) / (capex.shift(4) + 6.2115)).rolling(63).mean().diff(63) * 0.580018
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc125_252d_base_v125_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc125_252d_base_v125_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc126_105d_base_v126_signal(assets, fcf):
    res = (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).min().rolling(21).kurt() * 0.733531
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc126_105d_base_v126_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc126_105d_base_v126_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc127_200d_base_v127_signal(netinc, revenue):
    res = (netinc.diff(6) / (revenue.shift(2) + 3.0594)).rolling(105).var().rolling(63).skew() * 0.310645
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc127_200d_base_v127_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc127_200d_base_v127_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc128_21d_base_v128_signal(capex, netinc):
    res = (capex / (netinc + 1.5371)).diff(63).rolling(105).mean().rolling(105).min() * 0.461165
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc128_21d_base_v128_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc128_21d_base_v128_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc129_21d_base_v129_signal(equity, netinc):
    res = ((netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).var().rolling(150).max() / (netinc.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).var().rolling(150).max().rolling(63).max()) * 0.504683
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc129_21d_base_v129_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc129_21d_base_v129_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc130_63d_base_v130_signal(capex, fcf):
    res = (((((fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew() - (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).mean()) / (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).std()) - (((fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew() - (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).mean()) / (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).std()).rolling(63).mean()) / (((fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew() - (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).mean()) / (fcf.diff(14) / (capex.shift(7) + 3.0062)).rolling(10).mean().rolling(42).skew().rolling(10).std()).rolling(63).std()) * 0.524889
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc130_63d_base_v130_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc130_63d_base_v130_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc131_84d_base_v131_signal(capex, netinc):
    res = (capex / (netinc + 4.3435)).rolling(10).mean().rolling(126).var().rolling(21).min().rolling(126).skew() * 0.932171
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc131_84d_base_v131_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc131_84d_base_v131_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc132_105d_base_v132_signal(assets, fcf):
    res = (fcf.diff(20) / (assets.shift(5) + 5.8420)).diff(63).pct_change(42) * 0.590621
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc132_105d_base_v132_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc132_105d_base_v132_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc133_21d_base_v133_signal(assets, fcf):
    res = ((assets / (fcf + 2.4659)).rolling(252).min().rolling(200).kurt().rolling(84).std() / (assets / (fcf + 2.4659)).rolling(252).min().rolling(200).kurt().rolling(84).std().rolling(200).max()) * 0.199438
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc133_21d_base_v133_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc133_21d_base_v133_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc134_5d_base_v134_signal(assets, netinc):
    res = (netinc.diff(16) / (assets.shift(10) + 3.5239)).rolling(21).kurt().rolling(200).skew() * 0.419334
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc134_5d_base_v134_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc134_5d_base_v134_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc135_5d_base_v135_signal(assets, netinc):
    res = (netinc / (assets + 7.8601)).rolling(84).min().pct_change(105).pct_change(21) * 0.527036
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc135_5d_base_v135_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc135_5d_base_v135_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc136_84d_base_v136_signal(equity, netinc):
    res = ((netinc / (equity + 4.9327)).rolling(21).skew().diff(42).rolling(63).var() / (netinc / (equity + 4.9327)).rolling(21).skew().diff(42).rolling(63).var().rolling(63).max()) * 0.917847
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc136_84d_base_v136_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc136_84d_base_v136_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc137_63d_base_v137_signal(assets, netinc):
    res = (assets / (netinc + 8.5824)).rolling(63).max().rolling(105).min().rolling(10).skew().rolling(21).skew() * 0.156009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc137_63d_base_v137_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc137_63d_base_v137_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc138_42d_base_v138_signal(assets, fcf):
    res = (fcf.diff(16) / (assets.shift(7) + 9.8435)).rolling(252).kurt().diff(10).rolling(5).min().rolling(5).kurt() * 0.341082
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc138_42d_base_v138_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc138_42d_base_v138_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc139_5d_base_v139_signal(assets, fcf):
    res = ((fcf / (assets + 9.6460)).rolling(10).max().pct_change(150) / (fcf / (assets + 9.6460)).rolling(10).max().pct_change(150).rolling(150).max()) * 0.312081
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc139_5d_base_v139_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc139_5d_base_v139_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc140_42d_base_v140_signal(capex, netinc):
    res = (((netinc / (capex + 4.4955)).rolling(10).min().diff(21) - (netinc / (capex + 4.4955)).rolling(10).min().diff(21).rolling(42).mean()) / (netinc / (capex + 4.4955)).rolling(10).min().diff(21).rolling(42).std()).rolling(63).skew() * 0.807438
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc140_42d_base_v140_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc140_42d_base_v140_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc141_150d_base_v141_signal(capex, netinc):
    res = ((netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126) / (netinc.replace(0, np.nan) / capex.replace(0, np.nan)).diff(126).rolling(42).max()).pct_change(63).rolling(200).kurt() * 0.980844
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc141_150d_base_v141_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc141_150d_base_v141_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc142_200d_base_v142_signal(netinc, revenue):
    res = (((revenue / (netinc + 1.0836)).rolling(21).kurt().rolling(84).kurt().diff(150) - (revenue / (netinc + 1.0836)).rolling(21).kurt().rolling(84).kurt().diff(150).rolling(21).mean()) / (revenue / (netinc + 1.0836)).rolling(21).kurt().rolling(84).kurt().diff(150).rolling(21).std()) * 0.102390
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc142_200d_base_v142_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc142_200d_base_v142_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc143_10d_base_v143_signal(equity, netinc):
    res = ((netinc / (equity + 9.4292)).rolling(42).mean() / (netinc / (equity + 9.4292)).rolling(42).mean().rolling(42).max()) * 0.793236
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc143_10d_base_v143_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc143_10d_base_v143_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc144_84d_base_v144_signal(netinc, revenue):
    res = (netinc / (revenue + 0.5397)).rolling(63).var().rolling(252).std().diff(126) * 0.272528
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc144_84d_base_v144_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc144_84d_base_v144_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc145_252d_base_v145_signal(capex, netinc):
    res = (capex / (netinc + 9.3753)).rolling(126).min().rolling(105).std() * 0.984115
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc145_252d_base_v145_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc145_252d_base_v145_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc146_200d_base_v146_signal(assets, netinc):
    res = (netinc / (assets + 1.1772)).rolling(84).skew().rolling(42).var() * 0.435040
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc146_200d_base_v146_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc146_200d_base_v146_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc147_200d_base_v147_signal(capex, fcf):
    res = ((((fcf.diff(14) / (capex.shift(2) + 6.4991)) / (fcf.diff(14) / (capex.shift(2) + 6.4991)).rolling(5).max()).diff(126).rolling(200).kurt() - ((fcf.diff(14) / (capex.shift(2) + 6.4991)) / (fcf.diff(14) / (capex.shift(2) + 6.4991)).rolling(5).max()).diff(126).rolling(200).kurt().rolling(200).mean()) / ((fcf.diff(14) / (capex.shift(2) + 6.4991)) / (fcf.diff(14) / (capex.shift(2) + 6.4991)).rolling(5).max()).diff(126).rolling(200).kurt().rolling(200).std()) * 0.431490
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc147_200d_base_v147_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc147_200d_base_v147_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc148_21d_base_v148_signal(netinc, revenue):
    res = (netinc.diff(4) / (revenue.shift(4) + 3.4211)).diff(42).rolling(42).skew() * 0.261206
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc148_21d_base_v148_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc148_21d_base_v148_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc149_21d_base_v149_signal(assets, fcf):
    res = (fcf.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(126).min().rolling(21).kurt().rolling(21).max().rolling(63).kurt() * 0.788069
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc149_21d_base_v149_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc149_21d_base_v149_signal

def f197n_f197_net_income_to_capex_efficiency_regime_calc150_84d_base_v150_signal(netinc, revenue):
    res = (netinc.diff(11) / (revenue.shift(6) + 6.6418)).rolling(126).skew().rolling(126).min() * 0.725247
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f197n_f197_net_income_to_capex_efficiency_regime_calc150_84d_base_v150_signal'] = f197n_f197_net_income_to_capex_efficiency_regime_calc150_84d_base_v150_signal


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
