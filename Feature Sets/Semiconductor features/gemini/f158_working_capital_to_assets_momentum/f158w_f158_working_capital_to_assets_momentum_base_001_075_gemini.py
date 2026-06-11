import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f158w_f158_working_capital_to_assets_momentum_calc001_504d_rank_v001_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 504, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(504).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc001_504d_rank_v001_signal'] = f158w_f158_working_capital_to_assets_momentum_calc001_504d_rank_v001_signal

def f158w_f158_working_capital_to_assets_momentum_calc002_3d_vol_adj_mom_v002_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(3) / ratio.rolling(3).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc002_3d_vol_adj_mom_v002_signal'] = f158w_f158_working_capital_to_assets_momentum_calc002_3d_vol_adj_mom_v002_signal

def f158w_f158_working_capital_to_assets_momentum_calc003_42d_kurt_v003_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(42).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc003_42d_kurt_v003_signal'] = f158w_f158_working_capital_to_assets_momentum_calc003_42d_kurt_v003_signal

def f158w_f158_working_capital_to_assets_momentum_calc004_14d_rank_v004_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(14).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc004_14d_rank_v004_signal'] = f158w_f158_working_capital_to_assets_momentum_calc004_14d_rank_v004_signal

def f158w_f158_working_capital_to_assets_momentum_calc005_350d_zscore_v005_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(350).mean()) / ratio.rolling(350).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc005_350d_zscore_v005_signal'] = f158w_f158_working_capital_to_assets_momentum_calc005_350d_zscore_v005_signal

def f158w_f158_working_capital_to_assets_momentum_calc006_400d_q50_rel_v006_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 400, Operation: q50_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(400).quantile(0.5)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc006_400d_q50_rel_v006_signal'] = f158w_f158_working_capital_to_assets_momentum_calc006_400d_q50_rel_v006_signal

def f158w_f158_working_capital_to_assets_momentum_calc007_5d_diff_v007_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(5)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc007_5d_diff_v007_signal'] = f158w_f158_working_capital_to_assets_momentum_calc007_5d_diff_v007_signal

def f158w_f158_working_capital_to_assets_momentum_calc008_7d_skew_v008_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(7).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc008_7d_skew_v008_signal'] = f158w_f158_working_capital_to_assets_momentum_calc008_7d_skew_v008_signal

def f158w_f158_working_capital_to_assets_momentum_calc009_42d_diff_mean_v009_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(42).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc009_42d_diff_mean_v009_signal'] = f158w_f158_working_capital_to_assets_momentum_calc009_42d_diff_mean_v009_signal

def f158w_f158_working_capital_to_assets_momentum_calc010_450d_diff_v010_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 450, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(450)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc010_450d_diff_v010_signal'] = f158w_f158_working_capital_to_assets_momentum_calc010_450d_diff_v010_signal

def f158w_f158_working_capital_to_assets_momentum_calc011_350d_skew_v011_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(350).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc011_350d_skew_v011_signal'] = f158w_f158_working_capital_to_assets_momentum_calc011_350d_skew_v011_signal

def f158w_f158_working_capital_to_assets_momentum_calc012_150d_kurt_v012_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(150).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc012_150d_kurt_v012_signal'] = f158w_f158_working_capital_to_assets_momentum_calc012_150d_kurt_v012_signal

def f158w_f158_working_capital_to_assets_momentum_calc013_200d_pct_mean_v013_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(200).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc013_200d_pct_mean_v013_signal'] = f158w_f158_working_capital_to_assets_momentum_calc013_200d_pct_mean_v013_signal

def f158w_f158_working_capital_to_assets_momentum_calc014_50d_diff_v014_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 50, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(50)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc014_50d_diff_v014_signal'] = f158w_f158_working_capital_to_assets_momentum_calc014_50d_diff_v014_signal

def f158w_f158_working_capital_to_assets_momentum_calc015_21d_q50_rel_v015_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: q50_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(21).quantile(0.5)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc015_21d_q50_rel_v015_signal'] = f158w_f158_working_capital_to_assets_momentum_calc015_21d_q50_rel_v015_signal

def f158w_f158_working_capital_to_assets_momentum_calc016_80d_vol_adj_mom_v016_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(80) / ratio.rolling(80).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc016_80d_vol_adj_mom_v016_signal'] = f158w_f158_working_capital_to_assets_momentum_calc016_80d_vol_adj_mom_v016_signal

def f158w_f158_working_capital_to_assets_momentum_calc017_14d_skew_v017_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(14).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc017_14d_skew_v017_signal'] = f158w_f158_working_capital_to_assets_momentum_calc017_14d_skew_v017_signal

def f158w_f158_working_capital_to_assets_momentum_calc018_80d_rank_v018_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 80, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(80).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc018_80d_rank_v018_signal'] = f158w_f158_working_capital_to_assets_momentum_calc018_80d_rank_v018_signal

def f158w_f158_working_capital_to_assets_momentum_calc019_7d_abs_diff_mean_v019_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(7).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc019_7d_abs_diff_mean_v019_signal'] = f158w_f158_working_capital_to_assets_momentum_calc019_7d_abs_diff_mean_v019_signal

def f158w_f158_working_capital_to_assets_momentum_calc020_10d_ema_rel_v020_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: ema_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.ewm(span=10).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc020_10d_ema_rel_v020_signal'] = f158w_f158_working_capital_to_assets_momentum_calc020_10d_ema_rel_v020_signal

def f158w_f158_working_capital_to_assets_momentum_calc021_100d_med_abs_dev_v021_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 100, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(100).median()).abs().rolling(100).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc021_100d_med_abs_dev_v021_signal'] = f158w_f158_working_capital_to_assets_momentum_calc021_100d_med_abs_dev_v021_signal

def f158w_f158_working_capital_to_assets_momentum_calc022_50d_pct_chg_v022_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 50, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(50)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc022_50d_pct_chg_v022_signal'] = f158w_f158_working_capital_to_assets_momentum_calc022_50d_pct_chg_v022_signal

def f158w_f158_working_capital_to_assets_momentum_calc023_200d_diff_std_v023_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(200).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc023_200d_diff_std_v023_signal'] = f158w_f158_working_capital_to_assets_momentum_calc023_200d_diff_std_v023_signal

def f158w_f158_working_capital_to_assets_momentum_calc024_10d_abs_diff_mean_v024_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(10).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc024_10d_abs_diff_mean_v024_signal'] = f158w_f158_working_capital_to_assets_momentum_calc024_10d_abs_diff_mean_v024_signal

def f158w_f158_working_capital_to_assets_momentum_calc025_7d_diff_std_v025_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(7).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc025_7d_diff_std_v025_signal'] = f158w_f158_working_capital_to_assets_momentum_calc025_7d_diff_std_v025_signal

def f158w_f158_working_capital_to_assets_momentum_calc026_63d_med_abs_dev_v026_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(63).median()).abs().rolling(63).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc026_63d_med_abs_dev_v026_signal'] = f158w_f158_working_capital_to_assets_momentum_calc026_63d_med_abs_dev_v026_signal

def f158w_f158_working_capital_to_assets_momentum_calc027_100d_pct_mean_v027_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 100, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(100).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc027_100d_pct_mean_v027_signal'] = f158w_f158_working_capital_to_assets_momentum_calc027_100d_pct_mean_v027_signal

def f158w_f158_working_capital_to_assets_momentum_calc028_30d_zscore_v028_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 30, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(30).mean()) / ratio.rolling(30).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc028_30d_zscore_v028_signal'] = f158w_f158_working_capital_to_assets_momentum_calc028_30d_zscore_v028_signal

def f158w_f158_working_capital_to_assets_momentum_calc029_5d_kurt_v029_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(5).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc029_5d_kurt_v029_signal'] = f158w_f158_working_capital_to_assets_momentum_calc029_5d_kurt_v029_signal

def f158w_f158_working_capital_to_assets_momentum_calc030_63d_zscore_v030_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(63).mean()) / ratio.rolling(63).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc030_63d_zscore_v030_signal'] = f158w_f158_working_capital_to_assets_momentum_calc030_63d_zscore_v030_signal

def f158w_f158_working_capital_to_assets_momentum_calc031_42d_rank_v031_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(42).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc031_42d_rank_v031_signal'] = f158w_f158_working_capital_to_assets_momentum_calc031_42d_rank_v031_signal

def f158w_f158_working_capital_to_assets_momentum_calc032_126d_vol_adj_mom_v032_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 126, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(126) / ratio.rolling(126).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc032_126d_vol_adj_mom_v032_signal'] = f158w_f158_working_capital_to_assets_momentum_calc032_126d_vol_adj_mom_v032_signal

def f158w_f158_working_capital_to_assets_momentum_calc033_200d_ema_rel_v033_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: ema_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.ewm(span=200).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc033_200d_ema_rel_v033_signal'] = f158w_f158_working_capital_to_assets_momentum_calc033_200d_ema_rel_v033_signal

def f158w_f158_working_capital_to_assets_momentum_calc034_21d_ema_rel_v034_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: ema_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.ewm(span=21).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc034_21d_ema_rel_v034_signal'] = f158w_f158_working_capital_to_assets_momentum_calc034_21d_ema_rel_v034_signal

def f158w_f158_working_capital_to_assets_momentum_calc035_100d_skew_v035_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 100, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(100).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc035_100d_skew_v035_signal'] = f158w_f158_working_capital_to_assets_momentum_calc035_100d_skew_v035_signal

def f158w_f158_working_capital_to_assets_momentum_calc036_450d_std_rel_v036_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 450, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(450).std() / ratio.rolling(450).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc036_450d_std_rel_v036_signal'] = f158w_f158_working_capital_to_assets_momentum_calc036_450d_std_rel_v036_signal

def f158w_f158_working_capital_to_assets_momentum_calc037_350d_kurt_v037_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(350).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc037_350d_kurt_v037_signal'] = f158w_f158_working_capital_to_assets_momentum_calc037_350d_kurt_v037_signal

def f158w_f158_working_capital_to_assets_momentum_calc038_42d_min_rel_v038_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: min_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(42).min()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc038_42d_min_rel_v038_signal'] = f158w_f158_working_capital_to_assets_momentum_calc038_42d_min_rel_v038_signal

def f158w_f158_working_capital_to_assets_momentum_calc039_5d_min_rel_v039_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 5, Operation: min_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(5).min()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc039_5d_min_rel_v039_signal'] = f158w_f158_working_capital_to_assets_momentum_calc039_5d_min_rel_v039_signal

def f158w_f158_working_capital_to_assets_momentum_calc040_30d_q75_rel_v040_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 30, Operation: q75_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(30).quantile(0.75)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc040_30d_q75_rel_v040_signal'] = f158w_f158_working_capital_to_assets_momentum_calc040_30d_q75_rel_v040_signal

def f158w_f158_working_capital_to_assets_momentum_calc041_126d_q25_rel_v041_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 126, Operation: q25_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(126).quantile(0.25)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc041_126d_q25_rel_v041_signal'] = f158w_f158_working_capital_to_assets_momentum_calc041_126d_q25_rel_v041_signal

def f158w_f158_working_capital_to_assets_momentum_calc042_14d_vol_adj_mom_v042_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(14) / ratio.rolling(14).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc042_14d_vol_adj_mom_v042_signal'] = f158w_f158_working_capital_to_assets_momentum_calc042_14d_vol_adj_mom_v042_signal

def f158w_f158_working_capital_to_assets_momentum_calc043_14d_kurt_v043_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(14).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc043_14d_kurt_v043_signal'] = f158w_f158_working_capital_to_assets_momentum_calc043_14d_kurt_v043_signal

def f158w_f158_working_capital_to_assets_momentum_calc044_350d_diff_std_v044_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(350).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc044_350d_diff_std_v044_signal'] = f158w_f158_working_capital_to_assets_momentum_calc044_350d_diff_std_v044_signal

def f158w_f158_working_capital_to_assets_momentum_calc045_150d_pct_mean_v045_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(150).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc045_150d_pct_mean_v045_signal'] = f158w_f158_working_capital_to_assets_momentum_calc045_150d_pct_mean_v045_signal

def f158w_f158_working_capital_to_assets_momentum_calc046_300d_q75_rel_v046_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 300, Operation: q75_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(300).quantile(0.75)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc046_300d_q75_rel_v046_signal'] = f158w_f158_working_capital_to_assets_momentum_calc046_300d_q75_rel_v046_signal

def f158w_f158_working_capital_to_assets_momentum_calc047_7d_pct_chg_v047_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(7)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc047_7d_pct_chg_v047_signal'] = f158w_f158_working_capital_to_assets_momentum_calc047_7d_pct_chg_v047_signal

def f158w_f158_working_capital_to_assets_momentum_calc048_10d_mean_rel_v048_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 10, Operation: mean_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(10).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc048_10d_mean_rel_v048_signal'] = f158w_f158_working_capital_to_assets_momentum_calc048_10d_mean_rel_v048_signal

def f158w_f158_working_capital_to_assets_momentum_calc049_150d_med_abs_dev_v049_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(150).median()).abs().rolling(150).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc049_150d_med_abs_dev_v049_signal'] = f158w_f158_working_capital_to_assets_momentum_calc049_150d_med_abs_dev_v049_signal

def f158w_f158_working_capital_to_assets_momentum_calc050_200d_diff_mean_v050_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(200).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc050_200d_diff_mean_v050_signal'] = f158w_f158_working_capital_to_assets_momentum_calc050_200d_diff_mean_v050_signal

def f158w_f158_working_capital_to_assets_momentum_calc051_50d_diff_std_v051_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 50, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(50).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc051_50d_diff_std_v051_signal'] = f158w_f158_working_capital_to_assets_momentum_calc051_50d_diff_std_v051_signal

def f158w_f158_working_capital_to_assets_momentum_calc052_3d_rank_v052_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(3).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc052_3d_rank_v052_signal'] = f158w_f158_working_capital_to_assets_momentum_calc052_3d_rank_v052_signal

def f158w_f158_working_capital_to_assets_momentum_calc053_350d_vol_adj_mom_v053_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 350, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(350) / ratio.rolling(350).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc053_350d_vol_adj_mom_v053_signal'] = f158w_f158_working_capital_to_assets_momentum_calc053_350d_vol_adj_mom_v053_signal

def f158w_f158_working_capital_to_assets_momentum_calc054_150d_std_rel_v054_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: std_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(150).std() / ratio.rolling(150).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc054_150d_std_rel_v054_signal'] = f158w_f158_working_capital_to_assets_momentum_calc054_150d_std_rel_v054_signal

def f158w_f158_working_capital_to_assets_momentum_calc055_21d_diff_mean_v055_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(21).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc055_21d_diff_mean_v055_signal'] = f158w_f158_working_capital_to_assets_momentum_calc055_21d_diff_mean_v055_signal

def f158w_f158_working_capital_to_assets_momentum_calc056_450d_skew_v056_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 450, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(450).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc056_450d_skew_v056_signal'] = f158w_f158_working_capital_to_assets_momentum_calc056_450d_skew_v056_signal

def f158w_f158_working_capital_to_assets_momentum_calc057_21d_diff_std_v057_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(21).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc057_21d_diff_std_v057_signal'] = f158w_f158_working_capital_to_assets_momentum_calc057_21d_diff_std_v057_signal

def f158w_f158_working_capital_to_assets_momentum_calc058_300d_diff_v058_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 300, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(300)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc058_300d_diff_v058_signal'] = f158w_f158_working_capital_to_assets_momentum_calc058_300d_diff_v058_signal

def f158w_f158_working_capital_to_assets_momentum_calc059_252d_diff_v059_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 252, Operation: diff
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(252)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc059_252d_diff_v059_signal'] = f158w_f158_working_capital_to_assets_momentum_calc059_252d_diff_v059_signal

def f158w_f158_working_capital_to_assets_momentum_calc060_63d_kurt_v060_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(63).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc060_63d_kurt_v060_signal'] = f158w_f158_working_capital_to_assets_momentum_calc060_63d_kurt_v060_signal

def f158w_f158_working_capital_to_assets_momentum_calc061_400d_zscore_v061_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 400, Operation: zscore
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(400).mean()) / ratio.rolling(400).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc061_400d_zscore_v061_signal'] = f158w_f158_working_capital_to_assets_momentum_calc061_400d_zscore_v061_signal

def f158w_f158_working_capital_to_assets_momentum_calc062_7d_q75_rel_v062_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: q75_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(7).quantile(0.75)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc062_7d_q75_rel_v062_signal'] = f158w_f158_working_capital_to_assets_momentum_calc062_7d_q75_rel_v062_signal

def f158w_f158_working_capital_to_assets_momentum_calc063_14d_mean_rel_v063_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 14, Operation: mean_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.rolling(14).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc063_14d_mean_rel_v063_signal'] = f158w_f158_working_capital_to_assets_momentum_calc063_14d_mean_rel_v063_signal

def f158w_f158_working_capital_to_assets_momentum_calc064_252d_diff_std_v064_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 252, Operation: diff_std
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(252).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc064_252d_diff_std_v064_signal'] = f158w_f158_working_capital_to_assets_momentum_calc064_252d_diff_std_v064_signal

def f158w_f158_working_capital_to_assets_momentum_calc065_21d_vol_adj_mom_v065_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 21, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(21) / ratio.rolling(21).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc065_21d_vol_adj_mom_v065_signal'] = f158w_f158_working_capital_to_assets_momentum_calc065_21d_vol_adj_mom_v065_signal

def f158w_f158_working_capital_to_assets_momentum_calc066_300d_med_abs_dev_v066_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 300, Operation: med_abs_dev
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = (ratio - ratio.rolling(300).median()).abs().rolling(300).median()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc066_300d_med_abs_dev_v066_signal'] = f158w_f158_working_capital_to_assets_momentum_calc066_300d_med_abs_dev_v066_signal

def f158w_f158_working_capital_to_assets_momentum_calc067_150d_skew_v067_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 150, Operation: skew
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(150).skew()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc067_150d_skew_v067_signal'] = f158w_f158_working_capital_to_assets_momentum_calc067_150d_skew_v067_signal

def f158w_f158_working_capital_to_assets_momentum_calc068_63d_abs_diff_mean_v068_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 63, Operation: abs_diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().abs().rolling(63).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc068_63d_abs_diff_mean_v068_signal'] = f158w_f158_working_capital_to_assets_momentum_calc068_63d_abs_diff_mean_v068_signal

def f158w_f158_working_capital_to_assets_momentum_calc069_504d_ema_rel_v069_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 504, Operation: ema_rel
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio / ratio.ewm(span=504).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc069_504d_ema_rel_v069_signal'] = f158w_f158_working_capital_to_assets_momentum_calc069_504d_ema_rel_v069_signal

def f158w_f158_working_capital_to_assets_momentum_calc070_200d_rank_v070_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 200, Operation: rank
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(200).rank(pct=True)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc070_200d_rank_v070_signal'] = f158w_f158_working_capital_to_assets_momentum_calc070_200d_rank_v070_signal

def f158w_f158_working_capital_to_assets_momentum_calc071_3d_pct_mean_v071_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 3, Operation: pct_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change().rolling(3).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc071_3d_pct_mean_v071_signal'] = f158w_f158_working_capital_to_assets_momentum_calc071_3d_pct_mean_v071_signal

def f158w_f158_working_capital_to_assets_momentum_calc072_400d_kurt_v072_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 400, Operation: kurt
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.rolling(400).kurt()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc072_400d_kurt_v072_signal'] = f158w_f158_working_capital_to_assets_momentum_calc072_400d_kurt_v072_signal

def f158w_f158_working_capital_to_assets_momentum_calc073_504d_pct_chg_v073_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 504, Operation: pct_chg
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.pct_change(504)
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc073_504d_pct_chg_v073_signal'] = f158w_f158_working_capital_to_assets_momentum_calc073_504d_pct_chg_v073_signal

def f158w_f158_working_capital_to_assets_momentum_calc074_7d_diff_mean_v074_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 7, Operation: diff_mean
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff().rolling(7).mean()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc074_7d_diff_mean_v074_signal'] = f158w_f158_working_capital_to_assets_momentum_calc074_7d_diff_mean_v074_signal

def f158w_f158_working_capital_to_assets_momentum_calc075_42d_vol_adj_mom_v075_signal(assets, workingcapital):
    # Working Capital to Assets Momentum calculation
    # This is part of family f158 which measures the change in working capital efficiency relative to total assets
    # Window size: 42, Operation: vol_adj_mom
    v1 = assets
    v2 = workingcapital
    ratio = v2 / v1.replace(0, np.nan)
    res = ratio.diff(42) / ratio.rolling(42).std()
    v3 = res.replace([np.inf, -np.inf], np.nan)
    v4 = v3.ffill()
    v5 = v4.fillna(0)
    v6 = v5.replace([np.inf, -np.inf], np.nan)
    return v6
FEATURE_FUNCTIONS['f158w_f158_working_capital_to_assets_momentum_calc075_42d_vol_adj_mom_v075_signal'] = f158w_f158_working_capital_to_assets_momentum_calc075_42d_vol_adj_mom_v075_signal

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
