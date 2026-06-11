import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc076_84d_base_v076_signal(assets, capex):
    res = (capex.diff(12) / (assets.shift(7) + 6.2394)).rolling(150).kurt().pct_change(84) * 0.923371
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc076_84d_base_v076_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc076_84d_base_v076_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc077_42d_base_v077_signal(capex, ebitda):
    res = (ebitda / (capex + 9.9071)).rolling(84).kurt().rolling(150).kurt().rolling(63).skew() * 0.516607
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc077_42d_base_v077_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc077_42d_base_v077_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc078_200d_base_v078_signal(capex, revenue):
    res = ((capex / (revenue + 4.9528)) / (capex / (revenue + 4.9528)).rolling(21).max()).rolling(105).var() * 0.591189
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc078_200d_base_v078_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc078_200d_base_v078_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc079_105d_base_v079_signal(ebitda, revenue):
    res = ((((ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew() / (ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew().rolling(63).max()) - ((ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew() / (ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew().rolling(63).max()).rolling(84).mean()) / ((ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew() / (ebitda.diff(5) / (revenue.shift(10) + 7.4170)).rolling(150).std().rolling(200).skew().rolling(63).max()).rolling(84).std()) * 0.913350
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc079_105d_base_v079_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc079_105d_base_v079_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc080_42d_base_v080_signal(ebitda, revenue):
    res = (ebitda.diff(6) / (revenue.shift(4) + 1.9631)).rolling(252).std().rolling(5).skew().diff(252).rolling(105).var() * 0.260506
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc080_42d_base_v080_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc080_42d_base_v080_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc081_10d_base_v081_signal(assets, ebitda):
    res = (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(42).diff(84).pct_change(150) * 0.402329
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc081_10d_base_v081_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc081_10d_base_v081_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc082_252d_base_v082_signal(assets, capex):
    res = (capex.diff(8) / (assets.shift(10) + 9.9627)).rolling(126).std().rolling(42).skew().pct_change(10) * 0.600091
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc082_252d_base_v082_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc082_252d_base_v082_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc083_84d_base_v083_signal(ebitda, revenue):
    res = (((ebitda.diff(2) / (revenue.shift(9) + 0.6557)) - (ebitda.diff(2) / (revenue.shift(9) + 0.6557)).rolling(5).mean()) / (ebitda.diff(2) / (revenue.shift(9) + 0.6557)).rolling(5).std()).rolling(42).kurt() * 0.507662
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc083_84d_base_v083_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc083_84d_base_v083_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc084_105d_base_v084_signal(capex, ebitda):
    res = ((ebitda / (capex + 9.3518)).rolling(21).kurt().rolling(5).std() / (ebitda / (capex + 9.3518)).rolling(21).kurt().rolling(5).std().rolling(10).max()).rolling(5).var() * 0.985757
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc084_105d_base_v084_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc084_105d_base_v084_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc085_5d_base_v085_signal(capex, ebitda):
    res = (((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(63).rolling(105).skew().rolling(150).mean() - (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(63).rolling(105).skew().rolling(150).mean().rolling(150).mean()) / (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(63).rolling(105).skew().rolling(150).mean().rolling(150).std()) * 0.587545
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc085_5d_base_v085_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc085_5d_base_v085_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc086_5d_base_v086_signal(capex, ebitda):
    res = (ebitda.diff(2) / (capex.shift(7) + 0.4442)).rolling(105).mean().diff(200) * 0.897664
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc086_5d_base_v086_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc086_5d_base_v086_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc087_10d_base_v087_signal(capex, ebitda):
    res = (capex / (ebitda + 7.5143)).rolling(10).min().rolling(200).mean() * 0.090459
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc087_10d_base_v087_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc087_10d_base_v087_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc088_5d_base_v088_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(252).std().pct_change(5).rolling(5).skew() * 0.487779
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc088_5d_base_v088_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc088_5d_base_v088_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc089_105d_base_v089_signal(ebitda, equity):
    res = (equity / (ebitda + 2.1153)).rolling(252).mean().rolling(21).min().rolling(150).mean() * 0.418822
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc089_105d_base_v089_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc089_105d_base_v089_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc090_10d_base_v090_signal(assets, ebitda):
    res = (((ebitda / (assets + 5.8032)).rolling(42).var().rolling(84).std().rolling(150).std() - (ebitda / (assets + 5.8032)).rolling(42).var().rolling(84).std().rolling(150).std().rolling(200).mean()) / (ebitda / (assets + 5.8032)).rolling(42).var().rolling(84).std().rolling(150).std().rolling(200).std()) * 0.392835
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc090_10d_base_v090_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc090_10d_base_v090_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc091_84d_base_v091_signal(assets, ebitda):
    res = (ebitda.diff(18) / (assets.shift(2) + 5.5322)).diff(10).rolling(126).skew().rolling(105).std().rolling(105).skew() * 0.890463
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc091_84d_base_v091_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc091_84d_base_v091_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc092_252d_base_v092_signal(assets, ebitda):
    res = (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(10).kurt().rolling(21).skew() * 0.513115
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc092_252d_base_v092_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc092_252d_base_v092_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc093_252d_base_v093_signal(ebitda, revenue):
    res = (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).max().pct_change(126) * 0.606085
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc093_252d_base_v093_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc093_252d_base_v093_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc094_10d_base_v094_signal(assets, ebitda):
    res = (ebitda.diff(10) / (assets.shift(3) + 4.3857)).rolling(10).skew().rolling(63).max().rolling(150).kurt() * 0.617554
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc094_10d_base_v094_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc094_10d_base_v094_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc095_252d_base_v095_signal(ebitda, revenue):
    res = (revenue / (ebitda + 7.2218)).rolling(10).skew().diff(105) * 0.889859
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc095_252d_base_v095_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc095_252d_base_v095_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc096_84d_base_v096_signal(capex, ebitda):
    res = (capex / (ebitda + 2.3352)).rolling(63).kurt().rolling(21).var().rolling(63).var() * 0.277582
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc096_84d_base_v096_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc096_84d_base_v096_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc097_5d_base_v097_signal(ebitda, revenue):
    res = (((ebitda.diff(8) / (revenue.shift(8) + 0.4417)).rolling(150).std() - (ebitda.diff(8) / (revenue.shift(8) + 0.4417)).rolling(150).std().rolling(5).mean()) / (ebitda.diff(8) / (revenue.shift(8) + 0.4417)).rolling(150).std().rolling(5).std()) * 0.929915
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc097_5d_base_v097_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc097_5d_base_v097_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc098_150d_base_v098_signal(ebitda, equity):
    res = (ebitda / (equity + 6.3007)).rolling(42).var().rolling(126).mean().rolling(10).var().pct_change(84) * 0.393435
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc098_150d_base_v098_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc098_150d_base_v098_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc099_200d_base_v099_signal(capex, ebitda):
    res = (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(63).var().rolling(42).min().rolling(5).mean().diff(21) * 0.252059
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc099_200d_base_v099_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc099_200d_base_v099_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc100_42d_base_v100_signal(ebitda, equity):
    res = ((equity / (ebitda + 6.1921)).rolling(21).skew() / (equity / (ebitda + 6.1921)).rolling(21).skew().rolling(84).max()).rolling(105).var().rolling(105).max() * 0.962743
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc100_42d_base_v100_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc100_42d_base_v100_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc101_150d_base_v101_signal(capex, revenue):
    res = ((revenue / (capex + 8.0185)).rolling(10).var().rolling(5).min() / (revenue / (capex + 8.0185)).rolling(10).var().rolling(5).min().rolling(42).max()) * 0.110869
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc101_150d_base_v101_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc101_150d_base_v101_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc102_150d_base_v102_signal(ebitda, equity):
    res = (ebitda.diff(10) / (equity.shift(7) + 8.8892)).rolling(150).kurt().rolling(126).kurt() * 0.671986
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc102_150d_base_v102_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc102_150d_base_v102_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc103_252d_base_v103_signal(capex, ebitda):
    res = (capex / (ebitda + 3.1580)).diff(252).pct_change(126) * 0.577531
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc103_252d_base_v103_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc103_252d_base_v103_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc104_252d_base_v104_signal(assets, ebitda):
    res = (assets / (ebitda + 7.4265)).diff(21).diff(63) * 0.720452
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc104_252d_base_v104_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc104_252d_base_v104_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc105_84d_base_v105_signal(capex, ebitda):
    res = (ebitda / (capex + 5.7244)).rolling(63).skew().rolling(84).kurt().rolling(42).var() * 0.746235
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc105_84d_base_v105_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc105_84d_base_v105_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc106_252d_base_v106_signal(capex, revenue):
    res = (capex / (revenue + 8.9945)).rolling(63).skew().rolling(63).var() * 0.064339
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc106_252d_base_v106_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc106_252d_base_v106_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc107_21d_base_v107_signal(capex, ebitda):
    res = (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).std().pct_change(21) * 0.715730
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc107_21d_base_v107_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc107_21d_base_v107_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc108_252d_base_v108_signal(capex, revenue):
    res = (((((revenue / (capex + 7.5081)) - (revenue / (capex + 7.5081)).rolling(5).mean()) / (revenue / (capex + 7.5081)).rolling(5).std()) - (((revenue / (capex + 7.5081)) - (revenue / (capex + 7.5081)).rolling(5).mean()) / (revenue / (capex + 7.5081)).rolling(5).std()).rolling(200).mean()) / (((revenue / (capex + 7.5081)) - (revenue / (capex + 7.5081)).rolling(5).mean()) / (revenue / (capex + 7.5081)).rolling(5).std()).rolling(200).std()).diff(200) * 0.173233
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc108_252d_base_v108_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc108_252d_base_v108_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc109_150d_base_v109_signal(assets, ebitda):
    res = ((((assets / (ebitda + 3.0884)) / (assets / (ebitda + 3.0884)).rolling(63).max()).rolling(105).mean() - ((assets / (ebitda + 3.0884)) / (assets / (ebitda + 3.0884)).rolling(63).max()).rolling(105).mean().rolling(84).mean()) / ((assets / (ebitda + 3.0884)) / (assets / (ebitda + 3.0884)).rolling(63).max()).rolling(105).mean().rolling(84).std()) * 0.967906
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc109_150d_base_v109_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc109_150d_base_v109_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc110_10d_base_v110_signal(capex, ebitda):
    res = ((ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).kurt() / (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).rolling(10).kurt().rolling(5).max()).rolling(200).kurt().rolling(10).skew() * 0.355045
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc110_10d_base_v110_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc110_10d_base_v110_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc111_5d_base_v111_signal(assets, capex):
    res = (capex.diff(9) / (assets.shift(4) + 8.7051)).rolling(200).std().pct_change(200).pct_change(42).rolling(105).skew() * 0.330329
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc111_5d_base_v111_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc111_5d_base_v111_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc112_200d_base_v112_signal(capex, revenue):
    res = (capex.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(252).var().diff(200) * 0.562451
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc112_200d_base_v112_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc112_200d_base_v112_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc113_10d_base_v113_signal(assets, ebitda):
    res = (ebitda.diff(17) / (assets.shift(8) + 8.4936)).rolling(200).skew().rolling(42).std() * 0.309893
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc113_10d_base_v113_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc113_10d_base_v113_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc114_105d_base_v114_signal(ebitda, revenue):
    res = ((ebitda / (revenue + 9.5823)).rolling(42).skew().rolling(21).skew() / (ebitda / (revenue + 9.5823)).rolling(42).skew().rolling(21).skew().rolling(10).max()) * 0.022423
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc114_105d_base_v114_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc114_105d_base_v114_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc115_84d_base_v115_signal(capex, ebitda):
    res = (capex / (ebitda + 3.6195)).rolling(126).var().rolling(5).kurt() * 0.402111
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc115_84d_base_v115_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc115_84d_base_v115_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc116_5d_base_v116_signal(ebitda, equity):
    res = (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).var().rolling(5).max() * 0.938118
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc116_5d_base_v116_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc116_5d_base_v116_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc117_252d_base_v117_signal(capex, revenue):
    res = (((capex / (revenue + 2.8352)) - (capex / (revenue + 2.8352)).rolling(150).mean()) / (capex / (revenue + 2.8352)).rolling(150).std()).rolling(5).min().rolling(150).max() * 0.902025
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc117_252d_base_v117_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc117_252d_base_v117_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc118_150d_base_v118_signal(ebitda, revenue):
    res = (((ebitda.diff(20) / (revenue.shift(1) + 5.2998)).diff(252).rolling(84).max() - (ebitda.diff(20) / (revenue.shift(1) + 5.2998)).diff(252).rolling(84).max().rolling(150).mean()) / (ebitda.diff(20) / (revenue.shift(1) + 5.2998)).diff(252).rolling(84).max().rolling(150).std()) * 0.901535
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc118_150d_base_v118_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc118_150d_base_v118_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc119_200d_base_v119_signal(capex, ebitda):
    res = ((ebitda / (capex + 7.6284)) / (ebitda / (capex + 7.6284)).rolling(252).max()).rolling(10).std().rolling(105).min() * 0.634717
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc119_200d_base_v119_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc119_200d_base_v119_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc120_150d_base_v120_signal(ebitda, equity):
    res = (equity / (ebitda + 9.2208)).rolling(42).min().pct_change(200).diff(150) * 0.359558
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc120_150d_base_v120_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc120_150d_base_v120_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc121_105d_base_v121_signal(assets, ebitda):
    res = (((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).skew() - (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).skew().rolling(21).mean()) / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).skew().rolling(21).std()) * 0.799494
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc121_105d_base_v121_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc121_105d_base_v121_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc122_252d_base_v122_signal(capex, ebitda):
    res = (ebitda.replace(0, np.nan) / capex.replace(0, np.nan)).pct_change(5).rolling(126).mean().diff(10).pct_change(200) * 0.078428
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc122_252d_base_v122_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc122_252d_base_v122_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc123_105d_base_v123_signal(assets, capex):
    res = (assets / (capex + 2.2010)).pct_change(126).pct_change(105) * 0.095197
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc123_105d_base_v123_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc123_105d_base_v123_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc124_200d_base_v124_signal(ebitda, revenue):
    res = (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).mean().rolling(42).skew().rolling(252).skew().rolling(200).kurt() * 0.127785
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc124_200d_base_v124_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc124_200d_base_v124_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc125_84d_base_v125_signal(capex, revenue):
    res = (revenue / (capex + 4.3919)).rolling(105).mean().rolling(200).min().rolling(252).min() * 0.201913
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc125_84d_base_v125_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc125_84d_base_v125_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc126_42d_base_v126_signal(ebitda, equity):
    res = (((equity / (ebitda + 4.7894)) / (equity / (ebitda + 4.7894)).rolling(200).max()).rolling(200).mean().rolling(63).kurt() / ((equity / (ebitda + 4.7894)) / (equity / (ebitda + 4.7894)).rolling(200).max()).rolling(200).mean().rolling(63).kurt().rolling(21).max()) * 0.308888
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc126_42d_base_v126_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc126_42d_base_v126_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc127_150d_base_v127_signal(capex, revenue):
    res = (capex.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(252).rolling(84).mean() * 0.972021
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc127_150d_base_v127_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc127_150d_base_v127_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc128_10d_base_v128_signal(assets, ebitda):
    res = ((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84) / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).pct_change(84).rolling(10).max()).rolling(5).var().diff(63) * 0.667974
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc128_10d_base_v128_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc128_10d_base_v128_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc129_5d_base_v129_signal(assets, ebitda):
    res = (assets / (ebitda + 2.2248)).rolling(105).min().rolling(42).max().rolling(105).kurt().diff(42) * 0.626632
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc129_5d_base_v129_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc129_5d_base_v129_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc130_21d_base_v130_signal(capex, revenue):
    res = (capex.diff(12) / (revenue.shift(4) + 6.4102)).rolling(105).kurt().rolling(10).skew().rolling(150).mean() * 0.139018
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc130_21d_base_v130_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc130_21d_base_v130_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc131_21d_base_v131_signal(assets, ebitda):
    res = (assets / (ebitda + 0.1573)).rolling(105).min().rolling(5).var() * 0.226510
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc131_21d_base_v131_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc131_21d_base_v131_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc132_84d_base_v132_signal(ebitda, revenue):
    res = ((ebitda.diff(5) / (revenue.shift(2) + 3.0213)).rolling(105).std().rolling(63).kurt() / (ebitda.diff(5) / (revenue.shift(2) + 3.0213)).rolling(105).std().rolling(63).kurt().rolling(21).max()).rolling(200).min() * 0.737445
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc132_84d_base_v132_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc132_84d_base_v132_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc133_10d_base_v133_signal(capex, revenue):
    res = (revenue / (capex + 6.4916)).rolling(252).skew().rolling(63).kurt() * 0.659672
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc133_10d_base_v133_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc133_10d_base_v133_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc134_126d_base_v134_signal(assets, capex):
    res = (capex.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(42).kurt().rolling(200).min().rolling(21).std() * 0.511956
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc134_126d_base_v134_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc134_126d_base_v134_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc135_150d_base_v135_signal(assets, capex):
    res = (capex / (assets + 7.2799)).rolling(126).mean().rolling(150).min().diff(10).rolling(105).min() * 0.646241
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc135_150d_base_v135_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc135_150d_base_v135_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc136_105d_base_v136_signal(ebitda, equity):
    res = (ebitda.diff(19) / (equity.shift(6) + 9.6002)).rolling(200).max().rolling(150).std().rolling(84).skew().diff(200) * 0.827966
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc136_105d_base_v136_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc136_105d_base_v136_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc137_21d_base_v137_signal(assets, capex):
    res = (assets / (capex + 3.7175)).rolling(63).var().rolling(21).std().rolling(252).mean().rolling(150).min() * 0.793852
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc137_21d_base_v137_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc137_21d_base_v137_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc138_105d_base_v138_signal(capex, revenue):
    res = (revenue / (capex + 7.0482)).rolling(105).kurt().pct_change(21).rolling(21).max() * 0.007207
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc138_105d_base_v138_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc138_105d_base_v138_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc139_42d_base_v139_signal(assets, ebitda):
    res = (assets / (ebitda + 1.0393)).rolling(5).max().rolling(10).max() * 0.603379
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc139_42d_base_v139_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc139_42d_base_v139_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc140_252d_base_v140_signal(ebitda, equity):
    res = ((ebitda.replace(0, np.nan) / equity.replace(0, np.nan)) / (ebitda.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(126).max()).rolling(105).kurt() * 0.427952
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc140_252d_base_v140_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc140_252d_base_v140_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc141_126d_base_v141_signal(ebitda, revenue):
    res = (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(200).diff(42) * 0.084271
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc141_126d_base_v141_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc141_126d_base_v141_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc142_63d_base_v142_signal(ebitda, equity):
    res = (ebitda / (equity + 8.5415)).diff(200).diff(10) * 0.610009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc142_63d_base_v142_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc142_63d_base_v142_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc143_150d_base_v143_signal(capex, ebitda):
    res = (ebitda / (capex + 2.8613)).rolling(200).var().rolling(200).std().rolling(42).std() * 0.586546
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc143_150d_base_v143_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc143_150d_base_v143_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc144_150d_base_v144_signal(capex, revenue):
    res = (((capex.diff(15) / (revenue.shift(2) + 9.4811)).rolling(42).std() - (capex.diff(15) / (revenue.shift(2) + 9.4811)).rolling(42).std().rolling(21).mean()) / (capex.diff(15) / (revenue.shift(2) + 9.4811)).rolling(42).std().rolling(21).std()) * 0.232542
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc144_150d_base_v144_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc144_150d_base_v144_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc145_5d_base_v145_signal(ebitda, revenue):
    res = (ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).max().rolling(21).skew().diff(150).diff(84) * 0.413187
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc145_5d_base_v145_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc145_5d_base_v145_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc146_5d_base_v146_signal(ebitda, equity):
    res = ((ebitda / (equity + 8.2773)) / (ebitda / (equity + 8.2773)).rolling(21).max()).rolling(252).var() * 0.765635
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc146_5d_base_v146_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc146_5d_base_v146_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc147_21d_base_v147_signal(ebitda, revenue):
    res = (((ebitda / (revenue + 6.1541)).rolling(21).kurt() - (ebitda / (revenue + 6.1541)).rolling(21).kurt().rolling(105).mean()) / (ebitda / (revenue + 6.1541)).rolling(21).kurt().rolling(105).std()) * 0.994372
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc147_21d_base_v147_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc147_21d_base_v147_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc148_200d_base_v148_signal(ebitda, equity):
    res = (equity / (ebitda + 0.3393)).rolling(5).max().rolling(105).kurt().rolling(252).kurt() * 0.502462
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc148_200d_base_v148_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc148_200d_base_v148_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc149_200d_base_v149_signal(assets, ebitda):
    res = (((ebitda.replace(0, np.nan) / assets.replace(0, np.nan)) - (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).mean()) / (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).std()).rolling(10).max() * 0.600844
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc149_200d_base_v149_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc149_200d_base_v149_signal

def f194e_f194_ebitda_to_assets_efficiency_velocity_calc150_150d_base_v150_signal(assets, ebitda):
    res = (ebitda.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(150).kurt().rolling(150).max() * 0.856302
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f194e_f194_ebitda_to_assets_efficiency_velocity_calc150_150d_base_v150_signal'] = f194e_f194_ebitda_to_assets_efficiency_velocity_calc150_150d_base_v150_signal


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
