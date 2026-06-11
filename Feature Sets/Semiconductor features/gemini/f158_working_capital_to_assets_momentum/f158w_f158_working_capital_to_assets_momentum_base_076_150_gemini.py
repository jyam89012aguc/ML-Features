import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f158w_f158_working_capital_to_assets_momentum_calc076_252d_skew_v076_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 252, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(252).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc076_252d_skew_v076_signal'] = f158w_f158_working_capital_to_assets_momentum_calc076_252d_skew_v076_signal

def f158w_f158_working_capital_to_assets_momentum_calc077_400d_pct_mean_v077_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 400, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(400).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc077_400d_pct_mean_v077_signal'] = f158w_f158_working_capital_to_assets_momentum_calc077_400d_pct_mean_v077_signal

def f158w_f158_working_capital_to_assets_momentum_calc078_252d_kurt_v078_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 252, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(252).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc078_252d_kurt_v078_signal'] = f158w_f158_working_capital_to_assets_momentum_calc078_252d_kurt_v078_signal

def f158w_f158_working_capital_to_assets_momentum_calc079_30d_rank_v079_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 30, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(30).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc079_30d_rank_v079_signal'] = f158w_f158_working_capital_to_assets_momentum_calc079_30d_rank_v079_signal

def f158w_f158_working_capital_to_assets_momentum_calc080_100d_q50_rel_v080_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 100, Operation: q50_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(100).quantile(0.5)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc080_100d_q50_rel_v080_signal'] = f158w_f158_working_capital_to_assets_momentum_calc080_100d_q50_rel_v080_signal

def f158w_f158_working_capital_to_assets_momentum_calc081_150d_q25_rel_v081_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: q25_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(150).quantile(0.25)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc081_150d_q25_rel_v081_signal'] = f158w_f158_working_capital_to_assets_momentum_calc081_150d_q25_rel_v081_signal

def f158w_f158_working_capital_to_assets_momentum_calc082_5d_rank_v082_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(5).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc082_5d_rank_v082_signal'] = f158w_f158_working_capital_to_assets_momentum_calc082_5d_rank_v082_signal

def f158w_f158_working_capital_to_assets_momentum_calc083_5d_abs_diff_mean_v083_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(5).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc083_5d_abs_diff_mean_v083_signal'] = f158w_f158_working_capital_to_assets_momentum_calc083_5d_abs_diff_mean_v083_signal

def f158w_f158_working_capital_to_assets_momentum_calc084_42d_skew_v084_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(42).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc084_42d_skew_v084_signal'] = f158w_f158_working_capital_to_assets_momentum_calc084_42d_skew_v084_signal

def f158w_f158_working_capital_to_assets_momentum_calc085_30d_diff_std_v085_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 30, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(30).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc085_30d_diff_std_v085_signal'] = f158w_f158_working_capital_to_assets_momentum_calc085_30d_diff_std_v085_signal

def f158w_f158_working_capital_to_assets_momentum_calc086_50d_q25_rel_v086_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 50, Operation: q25_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(50).quantile(0.25)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc086_50d_q25_rel_v086_signal'] = f158w_f158_working_capital_to_assets_momentum_calc086_50d_q25_rel_v086_signal

def f158w_f158_working_capital_to_assets_momentum_calc087_10d_pct_chg_v087_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(10)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc087_10d_pct_chg_v087_signal'] = f158w_f158_working_capital_to_assets_momentum_calc087_10d_pct_chg_v087_signal

def f158w_f158_working_capital_to_assets_momentum_calc088_42d_std_rel_v088_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(42).std() / ratio.rolling(42).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc088_42d_std_rel_v088_signal'] = f158w_f158_working_capital_to_assets_momentum_calc088_42d_std_rel_v088_signal

def f158w_f158_working_capital_to_assets_momentum_calc089_126d_pct_chg_v089_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 126, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(126)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc089_126d_pct_chg_v089_signal'] = f158w_f158_working_capital_to_assets_momentum_calc089_126d_pct_chg_v089_signal

def f158w_f158_working_capital_to_assets_momentum_calc090_3d_abs_diff_mean_v090_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(3).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc090_3d_abs_diff_mean_v090_signal'] = f158w_f158_working_capital_to_assets_momentum_calc090_3d_abs_diff_mean_v090_signal

def f158w_f158_working_capital_to_assets_momentum_calc091_63d_q50_rel_v091_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: q50_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(63).quantile(0.5)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc091_63d_q50_rel_v091_signal'] = f158w_f158_working_capital_to_assets_momentum_calc091_63d_q50_rel_v091_signal

def f158w_f158_working_capital_to_assets_momentum_calc092_63d_skew_v092_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(63).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc092_63d_skew_v092_signal'] = f158w_f158_working_capital_to_assets_momentum_calc092_63d_skew_v092_signal

def f158w_f158_working_capital_to_assets_momentum_calc093_5d_pct_mean_v093_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(5).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc093_5d_pct_mean_v093_signal'] = f158w_f158_working_capital_to_assets_momentum_calc093_5d_pct_mean_v093_signal

def f158w_f158_working_capital_to_assets_momentum_calc094_350d_pct_chg_v094_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(350)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc094_350d_pct_chg_v094_signal'] = f158w_f158_working_capital_to_assets_momentum_calc094_350d_pct_chg_v094_signal

def f158w_f158_working_capital_to_assets_momentum_calc095_80d_pct_chg_v095_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(80)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc095_80d_pct_chg_v095_signal'] = f158w_f158_working_capital_to_assets_momentum_calc095_80d_pct_chg_v095_signal

def f158w_f158_working_capital_to_assets_momentum_calc096_300d_std_rel_v096_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 300, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(300).std() / ratio.rolling(300).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc096_300d_std_rel_v096_signal'] = f158w_f158_working_capital_to_assets_momentum_calc096_300d_std_rel_v096_signal

def f158w_f158_working_capital_to_assets_momentum_calc097_7d_std_rel_v097_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(7).std() / ratio.rolling(7).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc097_7d_std_rel_v097_signal'] = f158w_f158_working_capital_to_assets_momentum_calc097_7d_std_rel_v097_signal

def f158w_f158_working_capital_to_assets_momentum_calc098_7d_med_abs_dev_v098_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(7).median()).abs().rolling(7).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc098_7d_med_abs_dev_v098_signal'] = f158w_f158_working_capital_to_assets_momentum_calc098_7d_med_abs_dev_v098_signal

def f158w_f158_working_capital_to_assets_momentum_calc099_7d_kurt_v099_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(7).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc099_7d_kurt_v099_signal'] = f158w_f158_working_capital_to_assets_momentum_calc099_7d_kurt_v099_signal

def f158w_f158_working_capital_to_assets_momentum_calc100_126d_rank_v100_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 126, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(126).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc100_126d_rank_v100_signal'] = f158w_f158_working_capital_to_assets_momentum_calc100_126d_rank_v100_signal

def f158w_f158_working_capital_to_assets_momentum_calc101_400d_med_abs_dev_v101_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 400, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(400).median()).abs().rolling(400).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc101_400d_med_abs_dev_v101_signal'] = f158w_f158_working_capital_to_assets_momentum_calc101_400d_med_abs_dev_v101_signal

def f158w_f158_working_capital_to_assets_momentum_calc102_5d_med_abs_dev_v102_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(5).median()).abs().rolling(5).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc102_5d_med_abs_dev_v102_signal'] = f158w_f158_working_capital_to_assets_momentum_calc102_5d_med_abs_dev_v102_signal

def f158w_f158_working_capital_to_assets_momentum_calc103_50d_skew_v103_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 50, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(50).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc103_50d_skew_v103_signal'] = f158w_f158_working_capital_to_assets_momentum_calc103_50d_skew_v103_signal

def f158w_f158_working_capital_to_assets_momentum_calc104_80d_kurt_v104_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(80).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc104_80d_kurt_v104_signal'] = f158w_f158_working_capital_to_assets_momentum_calc104_80d_kurt_v104_signal

def f158w_f158_working_capital_to_assets_momentum_calc105_200d_min_rel_v105_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: min_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(200).min()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc105_200d_min_rel_v105_signal'] = f158w_f158_working_capital_to_assets_momentum_calc105_200d_min_rel_v105_signal

def f158w_f158_working_capital_to_assets_momentum_calc106_200d_med_abs_dev_v106_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(200).median()).abs().rolling(200).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc106_200d_med_abs_dev_v106_signal'] = f158w_f158_working_capital_to_assets_momentum_calc106_200d_med_abs_dev_v106_signal

def f158w_f158_working_capital_to_assets_momentum_calc107_30d_diff_mean_v107_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 30, Operation: diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(30).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc107_30d_diff_mean_v107_signal'] = f158w_f158_working_capital_to_assets_momentum_calc107_30d_diff_mean_v107_signal

def f158w_f158_working_capital_to_assets_momentum_calc108_100d_zscore_v108_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 100, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(100).mean()) / ratio.rolling(100).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc108_100d_zscore_v108_signal'] = f158w_f158_working_capital_to_assets_momentum_calc108_100d_zscore_v108_signal

def f158w_f158_working_capital_to_assets_momentum_calc109_63d_std_rel_v109_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(63).std() / ratio.rolling(63).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc109_63d_std_rel_v109_signal'] = f158w_f158_working_capital_to_assets_momentum_calc109_63d_std_rel_v109_signal

def f158w_f158_working_capital_to_assets_momentum_calc110_3d_diff_std_v110_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(3).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc110_3d_diff_std_v110_signal'] = f158w_f158_working_capital_to_assets_momentum_calc110_3d_diff_std_v110_signal

def f158w_f158_working_capital_to_assets_momentum_calc111_63d_rank_v111_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(63).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc111_63d_rank_v111_signal'] = f158w_f158_working_capital_to_assets_momentum_calc111_63d_rank_v111_signal

def f158w_f158_working_capital_to_assets_momentum_calc112_80d_skew_v112_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(80).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc112_80d_skew_v112_signal'] = f158w_f158_working_capital_to_assets_momentum_calc112_80d_skew_v112_signal

def f158w_f158_working_capital_to_assets_momentum_calc113_3d_min_rel_v113_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: min_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(3).min()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc113_3d_min_rel_v113_signal'] = f158w_f158_working_capital_to_assets_momentum_calc113_3d_min_rel_v113_signal

def f158w_f158_working_capital_to_assets_momentum_calc114_350d_diff_v114_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(350)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc114_350d_diff_v114_signal'] = f158w_f158_working_capital_to_assets_momentum_calc114_350d_diff_v114_signal

def f158w_f158_working_capital_to_assets_momentum_calc115_10d_zscore_v115_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(10).mean()) / ratio.rolling(10).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc115_10d_zscore_v115_signal'] = f158w_f158_working_capital_to_assets_momentum_calc115_10d_zscore_v115_signal

def f158w_f158_working_capital_to_assets_momentum_calc116_14d_diff_std_v116_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(14).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc116_14d_diff_std_v116_signal'] = f158w_f158_working_capital_to_assets_momentum_calc116_14d_diff_std_v116_signal

def f158w_f158_working_capital_to_assets_momentum_calc117_5d_ema_rel_v117_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: ema_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.ewm(span=5).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc117_5d_ema_rel_v117_signal'] = f158w_f158_working_capital_to_assets_momentum_calc117_5d_ema_rel_v117_signal

def f158w_f158_working_capital_to_assets_momentum_calc118_14d_pct_chg_v118_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(14)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc118_14d_pct_chg_v118_signal'] = f158w_f158_working_capital_to_assets_momentum_calc118_14d_pct_chg_v118_signal

def f158w_f158_working_capital_to_assets_momentum_calc119_63d_ema_rel_v119_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: ema_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.ewm(span=63).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc119_63d_ema_rel_v119_signal'] = f158w_f158_working_capital_to_assets_momentum_calc119_63d_ema_rel_v119_signal

def f158w_f158_working_capital_to_assets_momentum_calc120_30d_kurt_v120_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 30, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(30).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc120_30d_kurt_v120_signal'] = f158w_f158_working_capital_to_assets_momentum_calc120_30d_kurt_v120_signal

def f158w_f158_working_capital_to_assets_momentum_calc121_3d_std_rel_v121_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(3).std() / ratio.rolling(3).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc121_3d_std_rel_v121_signal'] = f158w_f158_working_capital_to_assets_momentum_calc121_3d_std_rel_v121_signal

def f158w_f158_working_capital_to_assets_momentum_calc122_80d_q50_rel_v122_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: q50_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(80).quantile(0.5)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc122_80d_q50_rel_v122_signal'] = f158w_f158_working_capital_to_assets_momentum_calc122_80d_q50_rel_v122_signal

def f158w_f158_working_capital_to_assets_momentum_calc123_21d_rank_v123_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(21).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc123_21d_rank_v123_signal'] = f158w_f158_working_capital_to_assets_momentum_calc123_21d_rank_v123_signal

def f158w_f158_working_capital_to_assets_momentum_calc124_3d_skew_v124_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(3).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc124_3d_skew_v124_signal'] = f158w_f158_working_capital_to_assets_momentum_calc124_3d_skew_v124_signal

def f158w_f158_working_capital_to_assets_momentum_calc125_126d_diff_std_v125_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 126, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(126).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc125_126d_diff_std_v125_signal'] = f158w_f158_working_capital_to_assets_momentum_calc125_126d_diff_std_v125_signal

def f158w_f158_working_capital_to_assets_momentum_calc126_80d_diff_v126_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(80)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc126_80d_diff_v126_signal'] = f158w_f158_working_capital_to_assets_momentum_calc126_80d_diff_v126_signal

def f158w_f158_working_capital_to_assets_momentum_calc127_10d_vol_adj_mom_v127_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(10) / ratio.rolling(10).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc127_10d_vol_adj_mom_v127_signal'] = f158w_f158_working_capital_to_assets_momentum_calc127_10d_vol_adj_mom_v127_signal

def f158w_f158_working_capital_to_assets_momentum_calc128_21d_pct_mean_v128_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(21).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc128_21d_pct_mean_v128_signal'] = f158w_f158_working_capital_to_assets_momentum_calc128_21d_pct_mean_v128_signal

def f158w_f158_working_capital_to_assets_momentum_calc129_10d_med_abs_dev_v129_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(10).median()).abs().rolling(10).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc129_10d_med_abs_dev_v129_signal'] = f158w_f158_working_capital_to_assets_momentum_calc129_10d_med_abs_dev_v129_signal

def f158w_f158_working_capital_to_assets_momentum_calc130_400d_skew_v130_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 400, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(400).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc130_400d_skew_v130_signal'] = f158w_f158_working_capital_to_assets_momentum_calc130_400d_skew_v130_signal

def f158w_f158_working_capital_to_assets_momentum_calc131_150d_diff_v131_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(150)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc131_150d_diff_v131_signal'] = f158w_f158_working_capital_to_assets_momentum_calc131_150d_diff_v131_signal

def f158w_f158_working_capital_to_assets_momentum_calc132_150d_zscore_v132_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(150).mean()) / ratio.rolling(150).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc132_150d_zscore_v132_signal'] = f158w_f158_working_capital_to_assets_momentum_calc132_150d_zscore_v132_signal

def f158w_f158_working_capital_to_assets_momentum_calc133_80d_med_abs_dev_v133_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(80).median()).abs().rolling(80).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc133_80d_med_abs_dev_v133_signal'] = f158w_f158_working_capital_to_assets_momentum_calc133_80d_med_abs_dev_v133_signal

def f158w_f158_working_capital_to_assets_momentum_calc134_63d_diff_mean_v134_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(63).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc134_63d_diff_mean_v134_signal'] = f158w_f158_working_capital_to_assets_momentum_calc134_63d_diff_mean_v134_signal

def f158w_f158_working_capital_to_assets_momentum_calc135_80d_abs_diff_mean_v135_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(80).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc135_80d_abs_diff_mean_v135_signal'] = f158w_f158_working_capital_to_assets_momentum_calc135_80d_abs_diff_mean_v135_signal

def f158w_f158_working_capital_to_assets_momentum_calc136_150d_abs_diff_mean_v136_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(150).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc136_150d_abs_diff_mean_v136_signal'] = f158w_f158_working_capital_to_assets_momentum_calc136_150d_abs_diff_mean_v136_signal

def f158w_f158_working_capital_to_assets_momentum_calc137_21d_med_abs_dev_v137_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(21).median()).abs().rolling(21).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc137_21d_med_abs_dev_v137_signal'] = f158w_f158_working_capital_to_assets_momentum_calc137_21d_med_abs_dev_v137_signal

def f158w_f158_working_capital_to_assets_momentum_calc138_200d_skew_v138_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(200).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc138_200d_skew_v138_signal'] = f158w_f158_working_capital_to_assets_momentum_calc138_200d_skew_v138_signal

def f158w_f158_working_capital_to_assets_momentum_calc139_21d_zscore_v139_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(21).mean()) / ratio.rolling(21).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc139_21d_zscore_v139_signal'] = f158w_f158_working_capital_to_assets_momentum_calc139_21d_zscore_v139_signal

def f158w_f158_working_capital_to_assets_momentum_calc140_14d_diff_v140_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(14)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc140_14d_diff_v140_signal'] = f158w_f158_working_capital_to_assets_momentum_calc140_14d_diff_v140_signal

def f158w_f158_working_capital_to_assets_momentum_calc141_252d_med_abs_dev_v141_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 252, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(252).median()).abs().rolling(252).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc141_252d_med_abs_dev_v141_signal'] = f158w_f158_working_capital_to_assets_momentum_calc141_252d_med_abs_dev_v141_signal

def f158w_f158_working_capital_to_assets_momentum_calc142_5d_diff_std_v142_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(5).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc142_5d_diff_std_v142_signal'] = f158w_f158_working_capital_to_assets_momentum_calc142_5d_diff_std_v142_signal

def f158w_f158_working_capital_to_assets_momentum_calc143_350d_med_abs_dev_v143_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(350).median()).abs().rolling(350).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc143_350d_med_abs_dev_v143_signal'] = f158w_f158_working_capital_to_assets_momentum_calc143_350d_med_abs_dev_v143_signal

def f158w_f158_working_capital_to_assets_momentum_calc144_200d_std_rel_v144_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(200).std() / ratio.rolling(200).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc144_200d_std_rel_v144_signal'] = f158w_f158_working_capital_to_assets_momentum_calc144_200d_std_rel_v144_signal

def f158w_f158_working_capital_to_assets_momentum_calc145_50d_kurt_v145_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 50, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(50).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc145_50d_kurt_v145_signal'] = f158w_f158_working_capital_to_assets_momentum_calc145_50d_kurt_v145_signal

def f158w_f158_working_capital_to_assets_momentum_calc146_504d_kurt_v146_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 504, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(504).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc146_504d_kurt_v146_signal'] = f158w_f158_working_capital_to_assets_momentum_calc146_504d_kurt_v146_signal

def f158w_f158_working_capital_to_assets_momentum_calc147_42d_abs_diff_mean_v147_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(42).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc147_42d_abs_diff_mean_v147_signal'] = f158w_f158_working_capital_to_assets_momentum_calc147_42d_abs_diff_mean_v147_signal

def f158w_f158_working_capital_to_assets_momentum_calc148_14d_med_abs_dev_v148_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(14).median()).abs().rolling(14).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc148_14d_med_abs_dev_v148_signal'] = f158w_f158_working_capital_to_assets_momentum_calc148_14d_med_abs_dev_v148_signal

def f158w_f158_working_capital_to_assets_momentum_calc149_100d_kurt_v149_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 100, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(100).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc149_100d_kurt_v149_signal'] = f158w_f158_working_capital_to_assets_momentum_calc149_100d_kurt_v149_signal

def f158w_f158_working_capital_to_assets_momentum_calc150_252d_rank_v150_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 252, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(252).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc150_252d_rank_v150_signal'] = f158w_f158_working_capital_to_assets_momentum_calc150_252d_rank_v150_signal

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
