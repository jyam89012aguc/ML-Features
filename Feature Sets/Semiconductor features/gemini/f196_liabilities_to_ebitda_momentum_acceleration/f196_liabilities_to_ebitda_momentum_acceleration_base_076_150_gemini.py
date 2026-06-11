import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc076_21d_base_v076_signal(ebitda, liabilities):
    res = ((liabilities / (ebitda + 7.4201)) / (liabilities / (ebitda + 7.4201)).rolling(10).max()).pct_change(150).rolling(5).mean() * 0.742833
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc076_21d_base_v076_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc076_21d_base_v076_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc077_10d_base_v077_signal(debt, ebitda):
    res = (debt.diff(8) / (ebitda.shift(3) + 1.5170)).rolling(84).var().diff(5) * 0.727933
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc077_10d_base_v077_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc077_10d_base_v077_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc078_42d_base_v078_signal(debt, ebitda):
    res = (ebitda / (debt + 8.7738)).rolling(42).mean().rolling(84).kurt().pct_change(10) * 0.462655
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc078_42d_base_v078_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc078_42d_base_v078_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc079_10d_base_v079_signal(ebitda, liabilities):
    res = (ebitda / (liabilities + 8.5366)).diff(10).rolling(105).max().rolling(252).std().rolling(21).min() * 0.187151
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc079_10d_base_v079_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc079_10d_base_v079_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc080_252d_base_v080_signal(debt, revenue):
    res = (debt.diff(15) / (revenue.shift(9) + 2.6615)).rolling(84).kurt().pct_change(5) * 0.530839
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc080_252d_base_v080_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc080_252d_base_v080_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc081_42d_base_v081_signal(debt, revenue):
    res = (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(84).skew().rolling(105).kurt() * 0.891718
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc081_42d_base_v081_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc081_42d_base_v081_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc082_126d_base_v082_signal(assets, liabilities):
    res = ((liabilities / (assets + 8.1130)).diff(42).rolling(105).max() / (liabilities / (assets + 8.1130)).diff(42).rolling(105).max().rolling(105).max()).pct_change(5) * 0.751155
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc082_126d_base_v082_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc082_126d_base_v082_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc083_84d_base_v083_signal(ebitda, liabilities):
    res = (((liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(84) - (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(84).rolling(42).mean()) / (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(84).rolling(42).std()).rolling(5).var() * 0.792834
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc083_84d_base_v083_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc083_84d_base_v083_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc084_252d_base_v084_signal(equity, liabilities):
    res = (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(10).skew().pct_change(150) * 0.897746
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc084_252d_base_v084_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc084_252d_base_v084_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc085_150d_base_v085_signal(debt, ebitda):
    res = (ebitda / (debt + 9.3708)).pct_change(252).rolling(84).var() * 0.928231
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc085_150d_base_v085_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc085_150d_base_v085_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc086_42d_base_v086_signal(debt, ebitda):
    res = (ebitda / (debt + 3.5564)).rolling(150).var().rolling(42).std() * 0.897260
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc086_42d_base_v086_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc086_42d_base_v086_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc087_84d_base_v087_signal(debt, revenue):
    res = (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).std().pct_change(10) * 0.762009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc087_84d_base_v087_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc087_84d_base_v087_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc088_150d_base_v088_signal(ebitda, liabilities):
    res = (liabilities / (ebitda + 4.0725)).diff(63).pct_change(252) * 0.475624
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc088_150d_base_v088_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc088_150d_base_v088_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc089_252d_base_v089_signal(liabilities, revenue):
    res = (liabilities / (revenue + 8.2231)).rolling(10).var().rolling(126).std() * 0.310104
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc089_252d_base_v089_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc089_252d_base_v089_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc090_63d_base_v090_signal(ebitda, liabilities):
    res = (((((liabilities / (ebitda + 4.3629)) - (liabilities / (ebitda + 4.3629)).rolling(252).mean()) / (liabilities / (ebitda + 4.3629)).rolling(252).std()) - (((liabilities / (ebitda + 4.3629)) - (liabilities / (ebitda + 4.3629)).rolling(252).mean()) / (liabilities / (ebitda + 4.3629)).rolling(252).std()).rolling(63).mean()) / (((liabilities / (ebitda + 4.3629)) - (liabilities / (ebitda + 4.3629)).rolling(252).mean()) / (liabilities / (ebitda + 4.3629)).rolling(252).std()).rolling(63).std()) * 0.629719
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc090_63d_base_v090_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc090_63d_base_v090_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc091_105d_base_v091_signal(debt, ebitda):
    res = (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).std().pct_change(105).rolling(105).kurt() - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).std().pct_change(105).rolling(105).kurt().rolling(252).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).std().pct_change(105).rolling(105).kurt().rolling(252).std()) * 0.226447
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc091_105d_base_v091_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc091_105d_base_v091_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc092_63d_base_v092_signal(debt, revenue):
    res = (((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) - (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).mean()) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).std()).rolling(42).std() * 0.840482
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc092_63d_base_v092_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc092_63d_base_v092_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc093_105d_base_v093_signal(equity, liabilities):
    res = (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(42).min().rolling(21).std().rolling(200).std() * 0.035551
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc093_105d_base_v093_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc093_105d_base_v093_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc094_10d_base_v094_signal(liabilities, revenue):
    res = (((revenue / (liabilities + 7.6366)).rolling(63).std() - (revenue / (liabilities + 7.6366)).rolling(63).std().rolling(21).mean()) / (revenue / (liabilities + 7.6366)).rolling(63).std().rolling(21).std()).rolling(5).var() * 0.476063
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc094_10d_base_v094_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc094_10d_base_v094_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc095_84d_base_v095_signal(assets, liabilities):
    res = (liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(5).min().rolling(21).kurt().rolling(63).var() * 0.558459
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc095_84d_base_v095_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc095_84d_base_v095_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc096_84d_base_v096_signal(assets, liabilities):
    res = (liabilities.replace(0, np.nan) / assets.replace(0, np.nan)).rolling(84).std().rolling(84).skew() * 0.474606
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc096_84d_base_v096_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc096_84d_base_v096_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc097_5d_base_v097_signal(debt, ebitda):
    res = (((debt / (ebitda + 5.1841)) - (debt / (ebitda + 5.1841)).rolling(5).mean()) / (debt / (ebitda + 5.1841)).rolling(5).std()).rolling(126).var().rolling(200).skew().rolling(63).kurt() * 0.798745
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc097_5d_base_v097_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc097_5d_base_v097_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc098_63d_base_v098_signal(debt, revenue):
    res = (((debt / (revenue + 8.9380)).pct_change(105).rolling(252).mean().rolling(10).kurt() - (debt / (revenue + 8.9380)).pct_change(105).rolling(252).mean().rolling(10).kurt().rolling(21).mean()) / (debt / (revenue + 8.9380)).pct_change(105).rolling(252).mean().rolling(10).kurt().rolling(21).std()) * 0.161686
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc098_63d_base_v098_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc098_63d_base_v098_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc099_126d_base_v099_signal(debt, ebitda):
    res = (ebitda / (debt + 5.3597)).rolling(5).min().pct_change(105).rolling(150).kurt().rolling(21).skew() * 0.347775
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc099_126d_base_v099_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc099_126d_base_v099_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc100_84d_base_v100_signal(liabilities, revenue):
    res = (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).std().rolling(84).max().rolling(126).var().rolling(42).skew() * 0.781441
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc100_84d_base_v100_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc100_84d_base_v100_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc101_10d_base_v101_signal(liabilities, revenue):
    res = (((liabilities / (revenue + 3.1569)).rolling(84).skew() - (liabilities / (revenue + 3.1569)).rolling(84).skew().rolling(200).mean()) / (liabilities / (revenue + 3.1569)).rolling(84).skew().rolling(200).std()).rolling(252).var().rolling(10).min() * 0.017291
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc101_10d_base_v101_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc101_10d_base_v101_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc102_21d_base_v102_signal(ebitda, liabilities):
    res = ((liabilities.diff(15) / (ebitda.shift(10) + 4.6667)) / (liabilities.diff(15) / (ebitda.shift(10) + 4.6667)).rolling(126).max()).rolling(150).kurt().rolling(150).skew() * 0.466532
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc102_21d_base_v102_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc102_21d_base_v102_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc103_150d_base_v103_signal(assets, liabilities):
    res = (((liabilities / (assets + 9.8978)).rolling(84).min().rolling(200).skew() - (liabilities / (assets + 9.8978)).rolling(84).min().rolling(200).skew().rolling(105).mean()) / (liabilities / (assets + 9.8978)).rolling(84).min().rolling(200).skew().rolling(105).std()).diff(10) * 0.383565
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc103_150d_base_v103_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc103_150d_base_v103_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc104_105d_base_v104_signal(ebitda, liabilities):
    res = (((liabilities / (ebitda + 0.6226)).rolling(21).var().rolling(126).min() - (liabilities / (ebitda + 0.6226)).rolling(21).var().rolling(126).min().rolling(63).mean()) / (liabilities / (ebitda + 0.6226)).rolling(21).var().rolling(126).min().rolling(63).std()) * 0.755114
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc104_105d_base_v104_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc104_105d_base_v104_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc105_126d_base_v105_signal(debt, ebitda):
    res = (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean().rolling(10).min().rolling(84).max() - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean().rolling(10).min().rolling(84).max().rolling(200).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(63).mean().rolling(10).min().rolling(84).max().rolling(200).std()) * 0.442258
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc105_126d_base_v105_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc105_126d_base_v105_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc106_5d_base_v106_signal(liabilities, revenue):
    res = ((liabilities / (revenue + 1.6407)) / (liabilities / (revenue + 1.6407)).rolling(252).max()).rolling(105).kurt() * 0.676270
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc106_5d_base_v106_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc106_5d_base_v106_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc107_84d_base_v107_signal(debt, revenue):
    res = ((debt / (revenue + 9.8966)).rolling(63).kurt().diff(105) / (debt / (revenue + 9.8966)).rolling(63).kurt().diff(105).rolling(42).max()) * 0.224346
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc107_84d_base_v107_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc107_84d_base_v107_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc108_5d_base_v108_signal(debt, revenue):
    res = (revenue / (debt + 0.1757)).diff(252).pct_change(252).pct_change(10).rolling(21).std() * 0.323571
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc108_5d_base_v108_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc108_5d_base_v108_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc109_126d_base_v109_signal(ebitda, liabilities):
    res = (liabilities.diff(10) / (ebitda.shift(1) + 8.6531)).rolling(126).mean().rolling(42).mean().diff(200).rolling(126).var() * 0.921852
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc109_126d_base_v109_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc109_126d_base_v109_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc110_126d_base_v110_signal(debt, revenue):
    res = (debt.diff(13) / (revenue.shift(10) + 0.3304)).pct_change(126).rolling(21).min().rolling(126).skew().diff(84) * 0.361596
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc110_126d_base_v110_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc110_126d_base_v110_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc111_200d_base_v111_signal(debt, ebitda):
    res = (ebitda / (debt + 5.3798)).rolling(5).kurt().rolling(126).std().rolling(21).std() * 0.720343
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc111_200d_base_v111_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc111_200d_base_v111_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc112_42d_base_v112_signal(liabilities, revenue):
    res = (revenue / (liabilities + 8.5047)).rolling(10).min().rolling(84).var().rolling(105).mean().pct_change(63) * 0.350583
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc112_42d_base_v112_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc112_42d_base_v112_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc113_200d_base_v113_signal(assets, liabilities):
    res = (assets / (liabilities + 9.1024)).rolling(42).var().rolling(63).std() * 0.493172
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc113_200d_base_v113_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc113_200d_base_v113_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc114_126d_base_v114_signal(equity, liabilities):
    res = (equity / (liabilities + 5.5284)).diff(252).rolling(84).min().diff(5).diff(252) * 0.794687
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc114_126d_base_v114_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc114_126d_base_v114_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc115_21d_base_v115_signal(debt, ebitda):
    res = (((((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std()).rolling(200).skew() - (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std()).rolling(200).skew().rolling(105).mean()) / (((debt.replace(0, np.nan) / ebitda.replace(0, np.nan)) - (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).mean()) / (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std()).rolling(200).skew().rolling(105).std()).diff(10) * 0.036707
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc115_21d_base_v115_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc115_21d_base_v115_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc116_10d_base_v116_signal(debt, revenue):
    res = (debt.diff(20) / (revenue.shift(1) + 1.5051)).diff(84).rolling(5).var().rolling(150).kurt().rolling(5).var() * 0.077642
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc116_10d_base_v116_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc116_10d_base_v116_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc117_252d_base_v117_signal(assets, liabilities):
    res = (liabilities / (assets + 0.2676)).rolling(126).max().pct_change(150).rolling(200).mean() * 0.904476
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc117_252d_base_v117_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc117_252d_base_v117_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc118_252d_base_v118_signal(debt, revenue):
    res = (debt / (revenue + 0.5800)).rolling(252).skew().pct_change(84) * 0.859263
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc118_252d_base_v118_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc118_252d_base_v118_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc119_5d_base_v119_signal(debt, revenue):
    res = (revenue / (debt + 0.4452)).rolling(200).std().rolling(200).min().pct_change(200) * 0.083034
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc119_5d_base_v119_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc119_5d_base_v119_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc120_105d_base_v120_signal(debt, ebitda):
    res = (debt.diff(2) / (ebitda.shift(1) + 4.9124)).rolling(5).skew().rolling(21).kurt() * 0.421453
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc120_105d_base_v120_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc120_105d_base_v120_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc121_200d_base_v121_signal(liabilities, revenue):
    res = (((((liabilities.diff(9) / (revenue.shift(7) + 6.5306)) - (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).mean()) / (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).std()) - (((liabilities.diff(9) / (revenue.shift(7) + 6.5306)) - (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).mean()) / (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).std()).rolling(63).mean()) / (((liabilities.diff(9) / (revenue.shift(7) + 6.5306)) - (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).mean()) / (liabilities.diff(9) / (revenue.shift(7) + 6.5306)).rolling(105).std()).rolling(63).std()) * 0.652328
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc121_200d_base_v121_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc121_200d_base_v121_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc122_84d_base_v122_signal(debt, ebitda):
    res = ((((debt / (ebitda + 2.3377)) / (debt / (ebitda + 2.3377)).rolling(126).max()) - ((debt / (ebitda + 2.3377)) / (debt / (ebitda + 2.3377)).rolling(126).max()).rolling(150).mean()) / ((debt / (ebitda + 2.3377)) / (debt / (ebitda + 2.3377)).rolling(126).max()).rolling(150).std()).rolling(42).skew() * 0.851487
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc122_84d_base_v122_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc122_84d_base_v122_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc123_200d_base_v123_signal(liabilities, revenue):
    res = (liabilities.diff(3) / (revenue.shift(5) + 0.2121)).pct_change(105).rolling(42).var() * 0.928195
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc123_200d_base_v123_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc123_200d_base_v123_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc124_63d_base_v124_signal(debt, revenue):
    res = (revenue / (debt + 5.8195)).rolling(42).std().pct_change(42).pct_change(126).rolling(10).max() * 0.547762
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc124_63d_base_v124_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc124_63d_base_v124_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc125_63d_base_v125_signal(liabilities, revenue):
    res = (((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max() - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max().rolling(126).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).max().rolling(126).std()).rolling(105).skew() * 0.031309
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc125_63d_base_v125_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc125_63d_base_v125_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc126_105d_base_v126_signal(equity, liabilities):
    res = (equity / (liabilities + 7.3237)).rolling(150).mean().rolling(10).min().rolling(150).skew() * 0.153351
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc126_105d_base_v126_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc126_105d_base_v126_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc127_84d_base_v127_signal(equity, liabilities):
    res = (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(200).var().diff(84).rolling(150).kurt() * 0.538948
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc127_84d_base_v127_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc127_84d_base_v127_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc128_200d_base_v128_signal(ebitda, liabilities):
    res = (ebitda / (liabilities + 8.9146)).diff(5).rolling(150).max().rolling(200).kurt() * 0.718322
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc128_200d_base_v128_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc128_200d_base_v128_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc129_84d_base_v129_signal(ebitda, liabilities):
    res = (ebitda / (liabilities + 1.5659)).rolling(105).max().pct_change(5).pct_change(252) * 0.544997
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc129_84d_base_v129_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc129_84d_base_v129_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc130_126d_base_v130_signal(debt, ebitda):
    res = (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(126).std().rolling(105).min().rolling(105).kurt() * 0.741869
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc130_126d_base_v130_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc130_126d_base_v130_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc131_105d_base_v131_signal(liabilities, revenue):
    res = (((liabilities / (revenue + 1.6078)) - (liabilities / (revenue + 1.6078)).rolling(150).mean()) / (liabilities / (revenue + 1.6078)).rolling(150).std()).diff(150).rolling(21).mean() * 0.723697
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc131_105d_base_v131_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc131_105d_base_v131_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc132_105d_base_v132_signal(debt, revenue):
    res = (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).min().rolling(21).kurt().diff(21) * 0.600662
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc132_105d_base_v132_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc132_105d_base_v132_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc133_150d_base_v133_signal(liabilities, revenue):
    res = (revenue / (liabilities + 6.1980)).rolling(42).min().rolling(21).min().rolling(126).std().diff(10) * 0.205575
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc133_150d_base_v133_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc133_150d_base_v133_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc134_5d_base_v134_signal(ebitda, liabilities):
    res = (ebitda / (liabilities + 1.6583)).rolling(42).skew().rolling(10).var() * 0.427381
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc134_5d_base_v134_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc134_5d_base_v134_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc135_126d_base_v135_signal(debt, revenue):
    res = (((((debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std() - (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).std()).rolling(42).min() - (((debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std() - (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).std()).rolling(42).min().rolling(126).mean()) / (((debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std() - (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(10) + 0.5010)).rolling(126).std().rolling(200).std()).rolling(42).min().rolling(126).std()) * 0.950305
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc135_126d_base_v135_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc135_126d_base_v135_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc136_150d_base_v136_signal(equity, liabilities):
    res = (liabilities / (equity + 9.3424)).diff(200).rolling(63).kurt() * 0.196513
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc136_150d_base_v136_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc136_150d_base_v136_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc137_42d_base_v137_signal(debt, revenue):
    res = (((debt.diff(13) / (revenue.shift(5) + 3.0013)).pct_change(150).rolling(5).skew() - (debt.diff(13) / (revenue.shift(5) + 3.0013)).pct_change(150).rolling(5).skew().rolling(63).mean()) / (debt.diff(13) / (revenue.shift(5) + 3.0013)).pct_change(150).rolling(5).skew().rolling(63).std()) * 0.324559
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc137_42d_base_v137_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc137_42d_base_v137_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc138_150d_base_v138_signal(debt, ebitda):
    res = (debt.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(105).max().diff(42).rolling(42).mean() * 0.411813
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc138_150d_base_v138_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc138_150d_base_v138_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc139_105d_base_v139_signal(equity, liabilities):
    res = ((liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).mean() / (liabilities.replace(0, np.nan) / equity.replace(0, np.nan)).rolling(105).mean().rolling(252).max()).rolling(200).kurt().rolling(63).skew() * 0.794185
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc139_105d_base_v139_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc139_105d_base_v139_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc140_252d_base_v140_signal(liabilities, revenue):
    res = (((liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).skew() - (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).skew().rolling(5).mean()) / (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(126).skew().rolling(5).std()).rolling(200).skew() * 0.671988
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc140_252d_base_v140_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc140_252d_base_v140_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc141_200d_base_v141_signal(liabilities, revenue):
    res = (revenue / (liabilities + 2.3718)).rolling(42).skew().rolling(126).skew().diff(63).diff(200) * 0.573062
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc141_200d_base_v141_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc141_200d_base_v141_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc142_84d_base_v142_signal(debt, revenue):
    res = (debt.diff(15) / (revenue.shift(8) + 2.4193)).rolling(84).mean().rolling(5).skew().rolling(21).max() * 0.271486
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc142_84d_base_v142_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc142_84d_base_v142_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc143_10d_base_v143_signal(ebitda, liabilities):
    res = (liabilities.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(105).kurt().rolling(84).skew().pct_change(105) * 0.389605
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc143_10d_base_v143_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc143_10d_base_v143_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc144_126d_base_v144_signal(debt, revenue):
    res = (((debt.replace(0, np.nan) / revenue.replace(0, np.nan)) - (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).mean()) / (debt.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(63).std()).pct_change(10).diff(21) * 0.076106
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc144_126d_base_v144_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc144_126d_base_v144_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc145_63d_base_v145_signal(equity, liabilities):
    res = (liabilities.diff(10) / (equity.shift(2) + 6.7346)).rolling(200).var().diff(105) * 0.087865
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc145_63d_base_v145_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc145_63d_base_v145_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc146_252d_base_v146_signal(ebitda, liabilities):
    res = (liabilities / (ebitda + 4.7785)).rolling(252).kurt().rolling(42).skew() * 0.011452
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc146_252d_base_v146_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc146_252d_base_v146_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc147_5d_base_v147_signal(debt, revenue):
    res = (debt / (revenue + 6.7545)).pct_change(150).rolling(105).kurt() * 0.674534
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc147_5d_base_v147_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc147_5d_base_v147_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc148_5d_base_v148_signal(debt, revenue):
    res = (((debt.diff(13) / (revenue.shift(2) + 7.2969)).pct_change(84).rolling(252).kurt() - (debt.diff(13) / (revenue.shift(2) + 7.2969)).pct_change(84).rolling(252).kurt().rolling(200).mean()) / (debt.diff(13) / (revenue.shift(2) + 7.2969)).pct_change(84).rolling(252).kurt().rolling(200).std()) * 0.612497
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc148_5d_base_v148_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc148_5d_base_v148_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc149_150d_base_v149_signal(liabilities, revenue):
    res = (liabilities.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(42).kurt().rolling(42).mean().rolling(105).var().rolling(84).kurt() * 0.152179
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc149_150d_base_v149_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc149_150d_base_v149_signal

def f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc150_105d_base_v150_signal(debt, ebitda):
    res = (debt.diff(17) / (ebitda.shift(10) + 0.4355)).rolling(252).min().diff(84).rolling(105).var() * 0.048407
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc150_105d_base_v150_signal'] = f196l_f196_liabilities_to_ebitda_momentum_acceleration_calc150_105d_base_v150_signal


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
