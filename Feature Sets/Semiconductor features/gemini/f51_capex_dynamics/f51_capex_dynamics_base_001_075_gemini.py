import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f51cd_f51_capex_dynamics_revenue_mean_21d_base_v001_signal(capex, revenue):
    res = (capex / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_mean_21d_base_v001_signal'] = f51cd_f51_capex_dynamics_revenue_mean_21d_base_v001_signal

def f51cd_f51_capex_dynamics_assets_mean_21d_base_v002_signal(capex, assets):
    res = (capex / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_mean_21d_base_v002_signal'] = f51cd_f51_capex_dynamics_assets_mean_21d_base_v002_signal

def f51cd_f51_capex_dynamics_ebitda_mean_21d_base_v003_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_mean_21d_base_v003_signal'] = f51cd_f51_capex_dynamics_ebitda_mean_21d_base_v003_signal

def f51cd_f51_capex_dynamics_equity_mean_21d_base_v004_signal(capex, equity):
    res = (capex / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_mean_21d_base_v004_signal'] = f51cd_f51_capex_dynamics_equity_mean_21d_base_v004_signal

def f51cd_f51_capex_dynamics_debt_mean_21d_base_v005_signal(capex, debt):
    res = (capex / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_mean_21d_base_v005_signal'] = f51cd_f51_capex_dynamics_debt_mean_21d_base_v005_signal

def f51cd_f51_capex_dynamics_closeadj_mean_21d_base_v006_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_mean_21d_base_v006_signal'] = f51cd_f51_capex_dynamics_closeadj_mean_21d_base_v006_signal

def f51cd_f51_capex_dynamics_capex_mean_21d_base_v007_signal(capex):
    res = capex.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_mean_21d_base_v007_signal'] = f51cd_f51_capex_dynamics_capex_mean_21d_base_v007_signal

def f51cd_f51_capex_dynamics_revenue_std_21d_base_v008_signal(capex, revenue):
    res = (capex / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_std_21d_base_v008_signal'] = f51cd_f51_capex_dynamics_revenue_std_21d_base_v008_signal

def f51cd_f51_capex_dynamics_assets_std_21d_base_v009_signal(capex, assets):
    res = (capex / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_std_21d_base_v009_signal'] = f51cd_f51_capex_dynamics_assets_std_21d_base_v009_signal

def f51cd_f51_capex_dynamics_ebitda_std_21d_base_v010_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_std_21d_base_v010_signal'] = f51cd_f51_capex_dynamics_ebitda_std_21d_base_v010_signal

def f51cd_f51_capex_dynamics_equity_std_21d_base_v011_signal(capex, equity):
    res = (capex / equity).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_std_21d_base_v011_signal'] = f51cd_f51_capex_dynamics_equity_std_21d_base_v011_signal

def f51cd_f51_capex_dynamics_debt_std_21d_base_v012_signal(capex, debt):
    res = (capex / debt).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_std_21d_base_v012_signal'] = f51cd_f51_capex_dynamics_debt_std_21d_base_v012_signal

def f51cd_f51_capex_dynamics_closeadj_std_21d_base_v013_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_std_21d_base_v013_signal'] = f51cd_f51_capex_dynamics_closeadj_std_21d_base_v013_signal

def f51cd_f51_capex_dynamics_capex_std_21d_base_v014_signal(capex):
    res = capex.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_std_21d_base_v014_signal'] = f51cd_f51_capex_dynamics_capex_std_21d_base_v014_signal

def f51cd_f51_capex_dynamics_revenue_pct_chg_21d_base_v015_signal(capex, revenue):
    res = (capex / revenue).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_pct_chg_21d_base_v015_signal'] = f51cd_f51_capex_dynamics_revenue_pct_chg_21d_base_v015_signal

def f51cd_f51_capex_dynamics_assets_pct_chg_21d_base_v016_signal(capex, assets):
    res = (capex / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_pct_chg_21d_base_v016_signal'] = f51cd_f51_capex_dynamics_assets_pct_chg_21d_base_v016_signal

def f51cd_f51_capex_dynamics_ebitda_pct_chg_21d_base_v017_signal(capex, ebitda):
    res = (capex / ebitda).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_pct_chg_21d_base_v017_signal'] = f51cd_f51_capex_dynamics_ebitda_pct_chg_21d_base_v017_signal

def f51cd_f51_capex_dynamics_equity_pct_chg_21d_base_v018_signal(capex, equity):
    res = (capex / equity).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_pct_chg_21d_base_v018_signal'] = f51cd_f51_capex_dynamics_equity_pct_chg_21d_base_v018_signal

def f51cd_f51_capex_dynamics_debt_pct_chg_21d_base_v019_signal(capex, debt):
    res = (capex / debt).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_pct_chg_21d_base_v019_signal'] = f51cd_f51_capex_dynamics_debt_pct_chg_21d_base_v019_signal

def f51cd_f51_capex_dynamics_closeadj_pct_chg_21d_base_v020_signal(capex, closeadj):
    res = (capex / closeadj).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_pct_chg_21d_base_v020_signal'] = f51cd_f51_capex_dynamics_closeadj_pct_chg_21d_base_v020_signal

def f51cd_f51_capex_dynamics_capex_pct_chg_21d_base_v021_signal(capex):
    res = capex.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_pct_chg_21d_base_v021_signal'] = f51cd_f51_capex_dynamics_capex_pct_chg_21d_base_v021_signal

def f51cd_f51_capex_dynamics_revenue_zscore_21d_base_v022_signal(capex, revenue):
    res = ((capex / revenue) - (capex / revenue).rolling(21).mean()) / (capex / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_zscore_21d_base_v022_signal'] = f51cd_f51_capex_dynamics_revenue_zscore_21d_base_v022_signal

def f51cd_f51_capex_dynamics_assets_zscore_21d_base_v023_signal(capex, assets):
    res = ((capex / assets) - (capex / assets).rolling(21).mean()) / (capex / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_zscore_21d_base_v023_signal'] = f51cd_f51_capex_dynamics_assets_zscore_21d_base_v023_signal

def f51cd_f51_capex_dynamics_ebitda_zscore_21d_base_v024_signal(capex, ebitda):
    res = ((capex / ebitda) - (capex / ebitda).rolling(21).mean()) / (capex / ebitda).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_zscore_21d_base_v024_signal'] = f51cd_f51_capex_dynamics_ebitda_zscore_21d_base_v024_signal

def f51cd_f51_capex_dynamics_equity_zscore_21d_base_v025_signal(capex, equity):
    res = ((capex / equity) - (capex / equity).rolling(21).mean()) / (capex / equity).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_zscore_21d_base_v025_signal'] = f51cd_f51_capex_dynamics_equity_zscore_21d_base_v025_signal

def f51cd_f51_capex_dynamics_debt_zscore_21d_base_v026_signal(capex, debt):
    res = ((capex / debt) - (capex / debt).rolling(21).mean()) / (capex / debt).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_zscore_21d_base_v026_signal'] = f51cd_f51_capex_dynamics_debt_zscore_21d_base_v026_signal

def f51cd_f51_capex_dynamics_closeadj_zscore_21d_base_v027_signal(capex, closeadj):
    res = ((capex / closeadj) - (capex / closeadj).rolling(21).mean()) / (capex / closeadj).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_zscore_21d_base_v027_signal'] = f51cd_f51_capex_dynamics_closeadj_zscore_21d_base_v027_signal

def f51cd_f51_capex_dynamics_capex_zscore_21d_base_v028_signal(capex):
    res = (capex - capex.rolling(21).mean()) / capex.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_zscore_21d_base_v028_signal'] = f51cd_f51_capex_dynamics_capex_zscore_21d_base_v028_signal

def f51cd_f51_capex_dynamics_revenue_rank_21d_base_v029_signal(capex, revenue):
    res = (capex / revenue).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_rank_21d_base_v029_signal'] = f51cd_f51_capex_dynamics_revenue_rank_21d_base_v029_signal

def f51cd_f51_capex_dynamics_ebitda_rank_21d_base_v030_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_rank_21d_base_v030_signal'] = f51cd_f51_capex_dynamics_ebitda_rank_21d_base_v030_signal

def f51cd_f51_capex_dynamics_equity_rank_63d_base_v031_signal(capex, equity):
    res = (capex / equity).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_rank_63d_base_v031_signal'] = f51cd_f51_capex_dynamics_equity_rank_63d_base_v031_signal

def f51cd_f51_capex_dynamics_debt_rank_63d_base_v032_signal(capex, debt):
    res = (capex / debt).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_rank_63d_base_v032_signal'] = f51cd_f51_capex_dynamics_debt_rank_63d_base_v032_signal

def f51cd_f51_capex_dynamics_closeadj_rank_21d_base_v033_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_rank_21d_base_v033_signal'] = f51cd_f51_capex_dynamics_closeadj_rank_21d_base_v033_signal

def f51cd_f51_capex_dynamics_revenue_diff_63d_base_v034_signal(capex, revenue):
    res = (capex / revenue).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_diff_63d_base_v034_signal'] = f51cd_f51_capex_dynamics_revenue_diff_63d_base_v034_signal

def f51cd_f51_capex_dynamics_assets_diff_63d_base_v035_signal(capex, assets):
    res = (capex / assets).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_diff_63d_base_v035_signal'] = f51cd_f51_capex_dynamics_assets_diff_63d_base_v035_signal

def f51cd_f51_capex_dynamics_ebitda_diff_63d_base_v036_signal(capex, ebitda):
    res = (capex / ebitda).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_diff_63d_base_v036_signal'] = f51cd_f51_capex_dynamics_ebitda_diff_63d_base_v036_signal

def f51cd_f51_capex_dynamics_equity_diff_63d_base_v037_signal(capex, equity):
    res = (capex / equity).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_diff_63d_base_v037_signal'] = f51cd_f51_capex_dynamics_equity_diff_63d_base_v037_signal

def f51cd_f51_capex_dynamics_debt_diff_63d_base_v038_signal(capex, debt):
    res = (capex / debt).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_diff_63d_base_v038_signal'] = f51cd_f51_capex_dynamics_debt_diff_63d_base_v038_signal

def f51cd_f51_capex_dynamics_closeadj_diff_63d_base_v039_signal(capex, closeadj):
    res = (capex / closeadj).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_diff_63d_base_v039_signal'] = f51cd_f51_capex_dynamics_closeadj_diff_63d_base_v039_signal

def f51cd_f51_capex_dynamics_capex_diff_63d_base_v040_signal(capex):
    res = capex.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_diff_63d_base_v040_signal'] = f51cd_f51_capex_dynamics_capex_diff_63d_base_v040_signal

def f51cd_f51_capex_dynamics_revenue_skew_21d_base_v041_signal(capex, revenue):
    res = (capex / revenue).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_skew_21d_base_v041_signal'] = f51cd_f51_capex_dynamics_revenue_skew_21d_base_v041_signal

def f51cd_f51_capex_dynamics_assets_skew_21d_base_v042_signal(capex, assets):
    res = (capex / assets).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_skew_21d_base_v042_signal'] = f51cd_f51_capex_dynamics_assets_skew_21d_base_v042_signal

def f51cd_f51_capex_dynamics_ebitda_skew_21d_base_v043_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_skew_21d_base_v043_signal'] = f51cd_f51_capex_dynamics_ebitda_skew_21d_base_v043_signal

def f51cd_f51_capex_dynamics_equity_skew_21d_base_v044_signal(capex, equity):
    res = (capex / equity).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_skew_21d_base_v044_signal'] = f51cd_f51_capex_dynamics_equity_skew_21d_base_v044_signal

def f51cd_f51_capex_dynamics_debt_skew_21d_base_v045_signal(capex, debt):
    res = (capex / debt).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_skew_21d_base_v045_signal'] = f51cd_f51_capex_dynamics_debt_skew_21d_base_v045_signal

def f51cd_f51_capex_dynamics_closeadj_skew_21d_base_v046_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_skew_21d_base_v046_signal'] = f51cd_f51_capex_dynamics_closeadj_skew_21d_base_v046_signal

def f51cd_f51_capex_dynamics_capex_skew_21d_base_v047_signal(capex):
    res = capex.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_skew_21d_base_v047_signal'] = f51cd_f51_capex_dynamics_capex_skew_21d_base_v047_signal

def f51cd_f51_capex_dynamics_revenue_kurt_21d_base_v048_signal(capex, revenue):
    res = (capex / revenue).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_kurt_21d_base_v048_signal'] = f51cd_f51_capex_dynamics_revenue_kurt_21d_base_v048_signal

def f51cd_f51_capex_dynamics_assets_kurt_21d_base_v049_signal(capex, assets):
    res = (capex / assets).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_kurt_21d_base_v049_signal'] = f51cd_f51_capex_dynamics_assets_kurt_21d_base_v049_signal

def f51cd_f51_capex_dynamics_ebitda_kurt_21d_base_v050_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_kurt_21d_base_v050_signal'] = f51cd_f51_capex_dynamics_ebitda_kurt_21d_base_v050_signal

def f51cd_f51_capex_dynamics_equity_kurt_21d_base_v051_signal(capex, equity):
    res = (capex / equity).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_kurt_21d_base_v051_signal'] = f51cd_f51_capex_dynamics_equity_kurt_21d_base_v051_signal

def f51cd_f51_capex_dynamics_debt_kurt_21d_base_v052_signal(capex, debt):
    res = (capex / debt).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_kurt_21d_base_v052_signal'] = f51cd_f51_capex_dynamics_debt_kurt_21d_base_v052_signal

def f51cd_f51_capex_dynamics_closeadj_kurt_63d_base_v053_signal(capex, closeadj):
    res = (capex / closeadj).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_kurt_63d_base_v053_signal'] = f51cd_f51_capex_dynamics_closeadj_kurt_63d_base_v053_signal

def f51cd_f51_capex_dynamics_capex_kurt_21d_base_v054_signal(capex):
    res = capex.rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_kurt_21d_base_v054_signal'] = f51cd_f51_capex_dynamics_capex_kurt_21d_base_v054_signal

def f51cd_f51_capex_dynamics_revenue_median_21d_base_v055_signal(capex, revenue):
    res = (capex / revenue).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_median_21d_base_v055_signal'] = f51cd_f51_capex_dynamics_revenue_median_21d_base_v055_signal

def f51cd_f51_capex_dynamics_assets_median_21d_base_v056_signal(capex, assets):
    res = (capex / assets).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_median_21d_base_v056_signal'] = f51cd_f51_capex_dynamics_assets_median_21d_base_v056_signal

def f51cd_f51_capex_dynamics_ebitda_median_21d_base_v057_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_median_21d_base_v057_signal'] = f51cd_f51_capex_dynamics_ebitda_median_21d_base_v057_signal

def f51cd_f51_capex_dynamics_equity_median_21d_base_v058_signal(capex, equity):
    res = (capex / equity).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_median_21d_base_v058_signal'] = f51cd_f51_capex_dynamics_equity_median_21d_base_v058_signal

def f51cd_f51_capex_dynamics_debt_median_21d_base_v059_signal(capex, debt):
    res = (capex / debt).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_median_21d_base_v059_signal'] = f51cd_f51_capex_dynamics_debt_median_21d_base_v059_signal

def f51cd_f51_capex_dynamics_closeadj_median_21d_base_v060_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_median_21d_base_v060_signal'] = f51cd_f51_capex_dynamics_closeadj_median_21d_base_v060_signal

def f51cd_f51_capex_dynamics_capex_median_21d_base_v061_signal(capex):
    res = capex.rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_median_21d_base_v061_signal'] = f51cd_f51_capex_dynamics_capex_median_21d_base_v061_signal

def f51cd_f51_capex_dynamics_revenue_min_max_ratio_21d_base_v062_signal(capex, revenue):
    res = (capex / revenue).rolling(21).min() / (capex / revenue).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_min_max_ratio_21d_base_v062_signal'] = f51cd_f51_capex_dynamics_revenue_min_max_ratio_21d_base_v062_signal

def f51cd_f51_capex_dynamics_assets_min_max_ratio_21d_base_v063_signal(capex, assets):
    res = (capex / assets).rolling(21).min() / (capex / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_min_max_ratio_21d_base_v063_signal'] = f51cd_f51_capex_dynamics_assets_min_max_ratio_21d_base_v063_signal

def f51cd_f51_capex_dynamics_ebitda_min_max_ratio_21d_base_v064_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).min() / (capex / ebitda).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_min_max_ratio_21d_base_v064_signal'] = f51cd_f51_capex_dynamics_ebitda_min_max_ratio_21d_base_v064_signal

def f51cd_f51_capex_dynamics_equity_min_max_ratio_21d_base_v065_signal(capex, equity):
    res = (capex / equity).rolling(21).min() / (capex / equity).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_min_max_ratio_21d_base_v065_signal'] = f51cd_f51_capex_dynamics_equity_min_max_ratio_21d_base_v065_signal

def f51cd_f51_capex_dynamics_debt_min_max_ratio_21d_base_v066_signal(capex, debt):
    res = (capex / debt).rolling(21).min() / (capex / debt).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_min_max_ratio_21d_base_v066_signal'] = f51cd_f51_capex_dynamics_debt_min_max_ratio_21d_base_v066_signal

def f51cd_f51_capex_dynamics_closeadj_min_max_ratio_21d_base_v067_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).min() / (capex / closeadj).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_min_max_ratio_21d_base_v067_signal'] = f51cd_f51_capex_dynamics_closeadj_min_max_ratio_21d_base_v067_signal

def f51cd_f51_capex_dynamics_capex_min_max_ratio_21d_base_v068_signal(capex):
    res = capex.rolling(21).min() / capex.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_min_max_ratio_21d_base_v068_signal'] = f51cd_f51_capex_dynamics_capex_min_max_ratio_21d_base_v068_signal

def f51cd_f51_capex_dynamics_revenue_max_ratio_63d_base_v069_signal(capex, revenue):
    res = (capex / revenue) / (capex / revenue).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_max_ratio_63d_base_v069_signal'] = f51cd_f51_capex_dynamics_revenue_max_ratio_63d_base_v069_signal

def f51cd_f51_capex_dynamics_ebitda_max_ratio_63d_base_v070_signal(capex, ebitda):
    res = (capex / ebitda) / (capex / ebitda).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_max_ratio_63d_base_v070_signal'] = f51cd_f51_capex_dynamics_ebitda_max_ratio_63d_base_v070_signal

def f51cd_f51_capex_dynamics_equity_max_ratio_252d_base_v071_signal(capex, equity):
    res = (capex / equity) / (capex / equity).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_max_ratio_252d_base_v071_signal'] = f51cd_f51_capex_dynamics_equity_max_ratio_252d_base_v071_signal

def f51cd_f51_capex_dynamics_debt_max_ratio_63d_base_v072_signal(capex, debt):
    res = (capex / debt) / (capex / debt).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_max_ratio_63d_base_v072_signal'] = f51cd_f51_capex_dynamics_debt_max_ratio_63d_base_v072_signal

def f51cd_f51_capex_dynamics_closeadj_max_ratio_21d_base_v073_signal(capex, closeadj):
    res = (capex / closeadj) / (capex / closeadj).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_max_ratio_21d_base_v073_signal'] = f51cd_f51_capex_dynamics_closeadj_max_ratio_21d_base_v073_signal

def f51cd_f51_capex_dynamics_revenue_min_ratio_21d_base_v074_signal(capex, revenue):
    res = (capex / revenue) / (capex / revenue).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_min_ratio_21d_base_v074_signal'] = f51cd_f51_capex_dynamics_revenue_min_ratio_21d_base_v074_signal

def f51cd_f51_capex_dynamics_assets_min_ratio_21d_base_v075_signal(capex, assets):
    res = (capex / assets) / (capex / assets).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_min_ratio_21d_base_v075_signal'] = f51cd_f51_capex_dynamics_assets_min_ratio_21d_base_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "capex": np.random.uniform(10, 100, n),
        "revenue": np.random.uniform(500, 2000, n),
        "assets": np.random.uniform(2000, 5000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "equity": np.random.uniform(1000, 3000, n),
        "debt": np.random.uniform(500, 1500, n),
        "closeadj": np.random.uniform(10, 100, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
        assert not res.isna().all(), f"{name} is all NaN"
        assert res.nunique() > 1, f"{name} is constant"
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f"WARNING: High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}")
    print(f"Self-test passed for {os.path.basename(__file__)}")

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
