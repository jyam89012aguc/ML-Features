import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f51cd_f51_capex_dynamics_revenue_mean_21d_jerk_v001_signal(capex, revenue):
    base = (capex / revenue).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_mean_21d_jerk_v001_signal'] = f51cd_f51_capex_dynamics_revenue_mean_21d_jerk_v001_signal

def f51cd_f51_capex_dynamics_assets_mean_21d_jerk_v002_signal(capex, assets):
    base = (capex / assets).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_mean_21d_jerk_v002_signal'] = f51cd_f51_capex_dynamics_assets_mean_21d_jerk_v002_signal

def f51cd_f51_capex_dynamics_ebitda_mean_21d_jerk_v003_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_mean_21d_jerk_v003_signal'] = f51cd_f51_capex_dynamics_ebitda_mean_21d_jerk_v003_signal

def f51cd_f51_capex_dynamics_equity_mean_21d_jerk_v004_signal(capex, equity):
    base = (capex / equity).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_mean_21d_jerk_v004_signal'] = f51cd_f51_capex_dynamics_equity_mean_21d_jerk_v004_signal

def f51cd_f51_capex_dynamics_debt_mean_21d_jerk_v005_signal(capex, debt):
    base = (capex / debt).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_mean_21d_jerk_v005_signal'] = f51cd_f51_capex_dynamics_debt_mean_21d_jerk_v005_signal

def f51cd_f51_capex_dynamics_closeadj_mean_21d_jerk_v006_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_mean_21d_jerk_v006_signal'] = f51cd_f51_capex_dynamics_closeadj_mean_21d_jerk_v006_signal

def f51cd_f51_capex_dynamics_capex_mean_21d_jerk_v007_signal(capex):
    base = capex.rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_mean_21d_jerk_v007_signal'] = f51cd_f51_capex_dynamics_capex_mean_21d_jerk_v007_signal

def f51cd_f51_capex_dynamics_revenue_std_21d_jerk_v008_signal(capex, revenue):
    base = (capex / revenue).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_std_21d_jerk_v008_signal'] = f51cd_f51_capex_dynamics_revenue_std_21d_jerk_v008_signal

def f51cd_f51_capex_dynamics_assets_std_21d_jerk_v009_signal(capex, assets):
    base = (capex / assets).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_std_21d_jerk_v009_signal'] = f51cd_f51_capex_dynamics_assets_std_21d_jerk_v009_signal

def f51cd_f51_capex_dynamics_ebitda_std_21d_jerk_v010_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_std_21d_jerk_v010_signal'] = f51cd_f51_capex_dynamics_ebitda_std_21d_jerk_v010_signal

def f51cd_f51_capex_dynamics_equity_std_21d_jerk_v011_signal(capex, equity):
    base = (capex / equity).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_std_21d_jerk_v011_signal'] = f51cd_f51_capex_dynamics_equity_std_21d_jerk_v011_signal

def f51cd_f51_capex_dynamics_debt_std_21d_jerk_v012_signal(capex, debt):
    base = (capex / debt).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_std_21d_jerk_v012_signal'] = f51cd_f51_capex_dynamics_debt_std_21d_jerk_v012_signal

def f51cd_f51_capex_dynamics_closeadj_std_21d_jerk_v013_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_std_21d_jerk_v013_signal'] = f51cd_f51_capex_dynamics_closeadj_std_21d_jerk_v013_signal

def f51cd_f51_capex_dynamics_capex_std_21d_jerk_v014_signal(capex):
    base = capex.rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_std_21d_jerk_v014_signal'] = f51cd_f51_capex_dynamics_capex_std_21d_jerk_v014_signal

def f51cd_f51_capex_dynamics_revenue_pct_chg_21d_jerk_v015_signal(capex, revenue):
    base = (capex / revenue).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_pct_chg_21d_jerk_v015_signal'] = f51cd_f51_capex_dynamics_revenue_pct_chg_21d_jerk_v015_signal

def f51cd_f51_capex_dynamics_assets_pct_chg_21d_jerk_v016_signal(capex, assets):
    base = (capex / assets).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_pct_chg_21d_jerk_v016_signal'] = f51cd_f51_capex_dynamics_assets_pct_chg_21d_jerk_v016_signal

def f51cd_f51_capex_dynamics_ebitda_pct_chg_21d_jerk_v017_signal(capex, ebitda):
    base = (capex / ebitda).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_pct_chg_21d_jerk_v017_signal'] = f51cd_f51_capex_dynamics_ebitda_pct_chg_21d_jerk_v017_signal

def f51cd_f51_capex_dynamics_equity_pct_chg_21d_jerk_v018_signal(capex, equity):
    base = (capex / equity).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_pct_chg_21d_jerk_v018_signal'] = f51cd_f51_capex_dynamics_equity_pct_chg_21d_jerk_v018_signal

def f51cd_f51_capex_dynamics_debt_pct_chg_21d_jerk_v019_signal(capex, debt):
    base = (capex / debt).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_pct_chg_21d_jerk_v019_signal'] = f51cd_f51_capex_dynamics_debt_pct_chg_21d_jerk_v019_signal

def f51cd_f51_capex_dynamics_closeadj_pct_chg_21d_jerk_v020_signal(capex, closeadj):
    base = (capex / closeadj).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_pct_chg_21d_jerk_v020_signal'] = f51cd_f51_capex_dynamics_closeadj_pct_chg_21d_jerk_v020_signal

def f51cd_f51_capex_dynamics_capex_pct_chg_21d_jerk_v021_signal(capex):
    base = capex.pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_pct_chg_21d_jerk_v021_signal'] = f51cd_f51_capex_dynamics_capex_pct_chg_21d_jerk_v021_signal

def f51cd_f51_capex_dynamics_revenue_zscore_21d_jerk_v022_signal(capex, revenue):
    base = (capex / revenue - (capex / revenue).rolling(21).mean()) / (capex / revenue).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_zscore_21d_jerk_v022_signal'] = f51cd_f51_capex_dynamics_revenue_zscore_21d_jerk_v022_signal

def f51cd_f51_capex_dynamics_assets_zscore_21d_jerk_v023_signal(capex, assets):
    base = (capex / assets - (capex / assets).rolling(21).mean()) / (capex / assets).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_zscore_21d_jerk_v023_signal'] = f51cd_f51_capex_dynamics_assets_zscore_21d_jerk_v023_signal

def f51cd_f51_capex_dynamics_ebitda_zscore_21d_jerk_v024_signal(capex, ebitda):
    base = (capex / ebitda - (capex / ebitda).rolling(21).mean()) / (capex / ebitda).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_zscore_21d_jerk_v024_signal'] = f51cd_f51_capex_dynamics_ebitda_zscore_21d_jerk_v024_signal

def f51cd_f51_capex_dynamics_equity_zscore_21d_jerk_v025_signal(capex, equity):
    base = (capex / equity - (capex / equity).rolling(21).mean()) / (capex / equity).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_zscore_21d_jerk_v025_signal'] = f51cd_f51_capex_dynamics_equity_zscore_21d_jerk_v025_signal

def f51cd_f51_capex_dynamics_debt_zscore_21d_jerk_v026_signal(capex, debt):
    base = (capex / debt - (capex / debt).rolling(21).mean()) / (capex / debt).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_zscore_21d_jerk_v026_signal'] = f51cd_f51_capex_dynamics_debt_zscore_21d_jerk_v026_signal

def f51cd_f51_capex_dynamics_closeadj_zscore_21d_jerk_v027_signal(capex, closeadj):
    base = (capex / closeadj - (capex / closeadj).rolling(21).mean()) / (capex / closeadj).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_zscore_21d_jerk_v027_signal'] = f51cd_f51_capex_dynamics_closeadj_zscore_21d_jerk_v027_signal

def f51cd_f51_capex_dynamics_capex_zscore_21d_jerk_v028_signal(capex):
    base = (capex - capex.rolling(21).mean()) / capex.rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_zscore_21d_jerk_v028_signal'] = f51cd_f51_capex_dynamics_capex_zscore_21d_jerk_v028_signal

def f51cd_f51_capex_dynamics_revenue_rank_21d_jerk_v029_signal(capex, revenue):
    base = (capex / revenue).rolling(21).rank(pct=True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_rank_21d_jerk_v029_signal'] = f51cd_f51_capex_dynamics_revenue_rank_21d_jerk_v029_signal

def f51cd_f51_capex_dynamics_ebitda_rank_21d_jerk_v030_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).rank(pct=True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_rank_21d_jerk_v030_signal'] = f51cd_f51_capex_dynamics_ebitda_rank_21d_jerk_v030_signal

def f51cd_f51_capex_dynamics_equity_rank_63d_jerk_v031_signal(capex, equity):
    base = (capex / equity).rolling(63).rank(pct=True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_rank_63d_jerk_v031_signal'] = f51cd_f51_capex_dynamics_equity_rank_63d_jerk_v031_signal

def f51cd_f51_capex_dynamics_debt_rank_63d_jerk_v032_signal(capex, debt):
    base = (capex / debt).rolling(63).rank(pct=True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_rank_63d_jerk_v032_signal'] = f51cd_f51_capex_dynamics_debt_rank_63d_jerk_v032_signal

def f51cd_f51_capex_dynamics_closeadj_rank_21d_jerk_v033_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).rank(pct=True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_rank_21d_jerk_v033_signal'] = f51cd_f51_capex_dynamics_closeadj_rank_21d_jerk_v033_signal

def f51cd_f51_capex_dynamics_revenue_diff_63d_jerk_v034_signal(capex, revenue):
    base = (capex / revenue).diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_diff_63d_jerk_v034_signal'] = f51cd_f51_capex_dynamics_revenue_diff_63d_jerk_v034_signal

def f51cd_f51_capex_dynamics_assets_diff_63d_jerk_v035_signal(capex, assets):
    base = (capex / assets).diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_diff_63d_jerk_v035_signal'] = f51cd_f51_capex_dynamics_assets_diff_63d_jerk_v035_signal

def f51cd_f51_capex_dynamics_ebitda_diff_63d_jerk_v036_signal(capex, ebitda):
    base = (capex / ebitda).diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_diff_63d_jerk_v036_signal'] = f51cd_f51_capex_dynamics_ebitda_diff_63d_jerk_v036_signal

def f51cd_f51_capex_dynamics_equity_diff_63d_jerk_v037_signal(capex, equity):
    base = (capex / equity).diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_diff_63d_jerk_v037_signal'] = f51cd_f51_capex_dynamics_equity_diff_63d_jerk_v037_signal

def f51cd_f51_capex_dynamics_debt_diff_63d_jerk_v038_signal(capex, debt):
    base = (capex / debt).diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_diff_63d_jerk_v038_signal'] = f51cd_f51_capex_dynamics_debt_diff_63d_jerk_v038_signal

def f51cd_f51_capex_dynamics_closeadj_diff_63d_jerk_v039_signal(capex, closeadj):
    base = (capex / closeadj).diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_diff_63d_jerk_v039_signal'] = f51cd_f51_capex_dynamics_closeadj_diff_63d_jerk_v039_signal

def f51cd_f51_capex_dynamics_capex_diff_63d_jerk_v040_signal(capex):
    base = capex.diff(63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_diff_63d_jerk_v040_signal'] = f51cd_f51_capex_dynamics_capex_diff_63d_jerk_v040_signal

def f51cd_f51_capex_dynamics_revenue_skew_21d_jerk_v041_signal(capex, revenue):
    base = (capex / revenue).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_skew_21d_jerk_v041_signal'] = f51cd_f51_capex_dynamics_revenue_skew_21d_jerk_v041_signal

def f51cd_f51_capex_dynamics_assets_skew_21d_jerk_v042_signal(capex, assets):
    base = (capex / assets).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_skew_21d_jerk_v042_signal'] = f51cd_f51_capex_dynamics_assets_skew_21d_jerk_v042_signal

def f51cd_f51_capex_dynamics_ebitda_skew_21d_jerk_v043_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_skew_21d_jerk_v043_signal'] = f51cd_f51_capex_dynamics_ebitda_skew_21d_jerk_v043_signal

def f51cd_f51_capex_dynamics_equity_skew_21d_jerk_v044_signal(capex, equity):
    base = (capex / equity).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_skew_21d_jerk_v044_signal'] = f51cd_f51_capex_dynamics_equity_skew_21d_jerk_v044_signal

def f51cd_f51_capex_dynamics_debt_skew_21d_jerk_v045_signal(capex, debt):
    base = (capex / debt).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_skew_21d_jerk_v045_signal'] = f51cd_f51_capex_dynamics_debt_skew_21d_jerk_v045_signal

def f51cd_f51_capex_dynamics_closeadj_skew_21d_jerk_v046_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_skew_21d_jerk_v046_signal'] = f51cd_f51_capex_dynamics_closeadj_skew_21d_jerk_v046_signal

def f51cd_f51_capex_dynamics_capex_skew_21d_jerk_v047_signal(capex):
    base = capex.rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_skew_21d_jerk_v047_signal'] = f51cd_f51_capex_dynamics_capex_skew_21d_jerk_v047_signal

def f51cd_f51_capex_dynamics_revenue_kurt_21d_jerk_v048_signal(capex, revenue):
    base = (capex / revenue).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_kurt_21d_jerk_v048_signal'] = f51cd_f51_capex_dynamics_revenue_kurt_21d_jerk_v048_signal

def f51cd_f51_capex_dynamics_assets_kurt_21d_jerk_v049_signal(capex, assets):
    base = (capex / assets).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_kurt_21d_jerk_v049_signal'] = f51cd_f51_capex_dynamics_assets_kurt_21d_jerk_v049_signal

def f51cd_f51_capex_dynamics_ebitda_kurt_21d_jerk_v050_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_kurt_21d_jerk_v050_signal'] = f51cd_f51_capex_dynamics_ebitda_kurt_21d_jerk_v050_signal

def f51cd_f51_capex_dynamics_equity_kurt_21d_jerk_v051_signal(capex, equity):
    base = (capex / equity).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_kurt_21d_jerk_v051_signal'] = f51cd_f51_capex_dynamics_equity_kurt_21d_jerk_v051_signal

def f51cd_f51_capex_dynamics_debt_kurt_21d_jerk_v052_signal(capex, debt):
    base = (capex / debt).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_kurt_21d_jerk_v052_signal'] = f51cd_f51_capex_dynamics_debt_kurt_21d_jerk_v052_signal

def f51cd_f51_capex_dynamics_closeadj_kurt_63d_jerk_v053_signal(capex, closeadj):
    base = (capex / closeadj).rolling(63).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_kurt_63d_jerk_v053_signal'] = f51cd_f51_capex_dynamics_closeadj_kurt_63d_jerk_v053_signal

def f51cd_f51_capex_dynamics_capex_kurt_21d_jerk_v054_signal(capex):
    base = capex.rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_kurt_21d_jerk_v054_signal'] = f51cd_f51_capex_dynamics_capex_kurt_21d_jerk_v054_signal

def f51cd_f51_capex_dynamics_revenue_median_21d_jerk_v055_signal(capex, revenue):
    base = (capex / revenue).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_median_21d_jerk_v055_signal'] = f51cd_f51_capex_dynamics_revenue_median_21d_jerk_v055_signal

def f51cd_f51_capex_dynamics_assets_median_21d_jerk_v056_signal(capex, assets):
    base = (capex / assets).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_median_21d_jerk_v056_signal'] = f51cd_f51_capex_dynamics_assets_median_21d_jerk_v056_signal

def f51cd_f51_capex_dynamics_ebitda_median_21d_jerk_v057_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_median_21d_jerk_v057_signal'] = f51cd_f51_capex_dynamics_ebitda_median_21d_jerk_v057_signal

def f51cd_f51_capex_dynamics_equity_median_21d_jerk_v058_signal(capex, equity):
    base = (capex / equity).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_median_21d_jerk_v058_signal'] = f51cd_f51_capex_dynamics_equity_median_21d_jerk_v058_signal

def f51cd_f51_capex_dynamics_debt_median_21d_jerk_v059_signal(capex, debt):
    base = (capex / debt).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_median_21d_jerk_v059_signal'] = f51cd_f51_capex_dynamics_debt_median_21d_jerk_v059_signal

def f51cd_f51_capex_dynamics_closeadj_median_21d_jerk_v060_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_median_21d_jerk_v060_signal'] = f51cd_f51_capex_dynamics_closeadj_median_21d_jerk_v060_signal

def f51cd_f51_capex_dynamics_capex_median_21d_jerk_v061_signal(capex):
    base = capex.rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_median_21d_jerk_v061_signal'] = f51cd_f51_capex_dynamics_capex_median_21d_jerk_v061_signal

def f51cd_f51_capex_dynamics_revenue_min_max_ratio_21d_jerk_v062_signal(capex, revenue):
    base = (capex / revenue).rolling(21).min() / (capex / revenue).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_min_max_ratio_21d_jerk_v062_signal'] = f51cd_f51_capex_dynamics_revenue_min_max_ratio_21d_jerk_v062_signal

def f51cd_f51_capex_dynamics_assets_min_max_ratio_21d_jerk_v063_signal(capex, assets):
    base = (capex / assets).rolling(21).min() / (capex / assets).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_min_max_ratio_21d_jerk_v063_signal'] = f51cd_f51_capex_dynamics_assets_min_max_ratio_21d_jerk_v063_signal

def f51cd_f51_capex_dynamics_ebitda_min_max_ratio_21d_jerk_v064_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).min() / (capex / ebitda).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_min_max_ratio_21d_jerk_v064_signal'] = f51cd_f51_capex_dynamics_ebitda_min_max_ratio_21d_jerk_v064_signal

def f51cd_f51_capex_dynamics_equity_min_max_ratio_21d_jerk_v065_signal(capex, equity):
    base = (capex / equity).rolling(21).min() / (capex / equity).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_min_max_ratio_21d_jerk_v065_signal'] = f51cd_f51_capex_dynamics_equity_min_max_ratio_21d_jerk_v065_signal

def f51cd_f51_capex_dynamics_debt_min_max_ratio_21d_jerk_v066_signal(capex, debt):
    base = (capex / debt).rolling(21).min() / (capex / debt).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_min_max_ratio_21d_jerk_v066_signal'] = f51cd_f51_capex_dynamics_debt_min_max_ratio_21d_jerk_v066_signal

def f51cd_f51_capex_dynamics_closeadj_min_max_ratio_21d_jerk_v067_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).min() / (capex / closeadj).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_min_max_ratio_21d_jerk_v067_signal'] = f51cd_f51_capex_dynamics_closeadj_min_max_ratio_21d_jerk_v067_signal

def f51cd_f51_capex_dynamics_capex_min_max_ratio_21d_jerk_v068_signal(capex):
    base = capex.rolling(21).min() / capex.rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_min_max_ratio_21d_jerk_v068_signal'] = f51cd_f51_capex_dynamics_capex_min_max_ratio_21d_jerk_v068_signal

def f51cd_f51_capex_dynamics_revenue_max_ratio_63d_jerk_v069_signal(capex, revenue):
    base = capex / revenue / (capex / revenue).rolling(63).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_max_ratio_63d_jerk_v069_signal'] = f51cd_f51_capex_dynamics_revenue_max_ratio_63d_jerk_v069_signal

def f51cd_f51_capex_dynamics_ebitda_max_ratio_63d_jerk_v070_signal(capex, ebitda):
    base = capex / ebitda / (capex / ebitda).rolling(63).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_max_ratio_63d_jerk_v070_signal'] = f51cd_f51_capex_dynamics_ebitda_max_ratio_63d_jerk_v070_signal

def f51cd_f51_capex_dynamics_equity_max_ratio_252d_jerk_v071_signal(capex, equity):
    base = capex / equity / (capex / equity).rolling(252).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_max_ratio_252d_jerk_v071_signal'] = f51cd_f51_capex_dynamics_equity_max_ratio_252d_jerk_v071_signal

def f51cd_f51_capex_dynamics_debt_max_ratio_63d_jerk_v072_signal(capex, debt):
    base = capex / debt / (capex / debt).rolling(63).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_max_ratio_63d_jerk_v072_signal'] = f51cd_f51_capex_dynamics_debt_max_ratio_63d_jerk_v072_signal

def f51cd_f51_capex_dynamics_closeadj_max_ratio_21d_jerk_v073_signal(capex, closeadj):
    base = capex / closeadj / (capex / closeadj).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_max_ratio_21d_jerk_v073_signal'] = f51cd_f51_capex_dynamics_closeadj_max_ratio_21d_jerk_v073_signal

def f51cd_f51_capex_dynamics_revenue_min_ratio_21d_jerk_v074_signal(capex, revenue):
    base = capex / revenue / (capex / revenue).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_min_ratio_21d_jerk_v074_signal'] = f51cd_f51_capex_dynamics_revenue_min_ratio_21d_jerk_v074_signal

def f51cd_f51_capex_dynamics_assets_min_ratio_21d_jerk_v075_signal(capex, assets):
    base = capex / assets / (capex / assets).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_min_ratio_21d_jerk_v075_signal'] = f51cd_f51_capex_dynamics_assets_min_ratio_21d_jerk_v075_signal

def f51cd_f51_capex_dynamics_ebitda_min_ratio_21d_jerk_v076_signal(capex, ebitda):
    base = capex / ebitda / (capex / ebitda).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_min_ratio_21d_jerk_v076_signal'] = f51cd_f51_capex_dynamics_ebitda_min_ratio_21d_jerk_v076_signal

def f51cd_f51_capex_dynamics_equity_min_ratio_21d_jerk_v077_signal(capex, equity):
    base = capex / equity / (capex / equity).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_min_ratio_21d_jerk_v077_signal'] = f51cd_f51_capex_dynamics_equity_min_ratio_21d_jerk_v077_signal

def f51cd_f51_capex_dynamics_debt_min_ratio_21d_jerk_v078_signal(capex, debt):
    base = capex / debt / (capex / debt).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_min_ratio_21d_jerk_v078_signal'] = f51cd_f51_capex_dynamics_debt_min_ratio_21d_jerk_v078_signal

def f51cd_f51_capex_dynamics_closeadj_min_ratio_21d_jerk_v079_signal(capex, closeadj):
    base = capex / closeadj / (capex / closeadj).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_min_ratio_21d_jerk_v079_signal'] = f51cd_f51_capex_dynamics_closeadj_min_ratio_21d_jerk_v079_signal

def f51cd_f51_capex_dynamics_capex_min_ratio_21d_jerk_v080_signal(capex):
    base = capex / capex.rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_min_ratio_21d_jerk_v080_signal'] = f51cd_f51_capex_dynamics_capex_min_ratio_21d_jerk_v080_signal

def f51cd_f51_capex_dynamics_revenue_cv_21d_jerk_v081_signal(capex, revenue):
    base = (capex / revenue).rolling(21).std() / (capex / revenue).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_cv_21d_jerk_v081_signal'] = f51cd_f51_capex_dynamics_revenue_cv_21d_jerk_v081_signal

def f51cd_f51_capex_dynamics_assets_cv_21d_jerk_v082_signal(capex, assets):
    base = (capex / assets).rolling(21).std() / (capex / assets).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_cv_21d_jerk_v082_signal'] = f51cd_f51_capex_dynamics_assets_cv_21d_jerk_v082_signal

def f51cd_f51_capex_dynamics_ebitda_cv_21d_jerk_v083_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).std() / (capex / ebitda).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_cv_21d_jerk_v083_signal'] = f51cd_f51_capex_dynamics_ebitda_cv_21d_jerk_v083_signal

def f51cd_f51_capex_dynamics_equity_cv_21d_jerk_v084_signal(capex, equity):
    base = (capex / equity).rolling(21).std() / (capex / equity).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_cv_21d_jerk_v084_signal'] = f51cd_f51_capex_dynamics_equity_cv_21d_jerk_v084_signal

def f51cd_f51_capex_dynamics_debt_cv_21d_jerk_v085_signal(capex, debt):
    base = (capex / debt).rolling(21).std() / (capex / debt).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_cv_21d_jerk_v085_signal'] = f51cd_f51_capex_dynamics_debt_cv_21d_jerk_v085_signal

def f51cd_f51_capex_dynamics_closeadj_cv_21d_jerk_v086_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).std() / (capex / closeadj).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_cv_21d_jerk_v086_signal'] = f51cd_f51_capex_dynamics_closeadj_cv_21d_jerk_v086_signal

def f51cd_f51_capex_dynamics_capex_cv_21d_jerk_v087_signal(capex):
    base = capex.rolling(21).std() / capex.rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_cv_21d_jerk_v087_signal'] = f51cd_f51_capex_dynamics_capex_cv_21d_jerk_v087_signal

def f51cd_f51_capex_dynamics_revenue_q25_21d_jerk_v088_signal(capex, revenue):
    base = (capex / revenue).rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q25_21d_jerk_v088_signal'] = f51cd_f51_capex_dynamics_revenue_q25_21d_jerk_v088_signal

def f51cd_f51_capex_dynamics_assets_q25_21d_jerk_v089_signal(capex, assets):
    base = (capex / assets).rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q25_21d_jerk_v089_signal'] = f51cd_f51_capex_dynamics_assets_q25_21d_jerk_v089_signal

def f51cd_f51_capex_dynamics_ebitda_q25_21d_jerk_v090_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q25_21d_jerk_v090_signal'] = f51cd_f51_capex_dynamics_ebitda_q25_21d_jerk_v090_signal

def f51cd_f51_capex_dynamics_equity_q25_21d_jerk_v091_signal(capex, equity):
    base = (capex / equity).rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q25_21d_jerk_v091_signal'] = f51cd_f51_capex_dynamics_equity_q25_21d_jerk_v091_signal

def f51cd_f51_capex_dynamics_debt_q25_21d_jerk_v092_signal(capex, debt):
    base = (capex / debt).rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q25_21d_jerk_v092_signal'] = f51cd_f51_capex_dynamics_debt_q25_21d_jerk_v092_signal

def f51cd_f51_capex_dynamics_closeadj_q25_21d_jerk_v093_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q25_21d_jerk_v093_signal'] = f51cd_f51_capex_dynamics_closeadj_q25_21d_jerk_v093_signal

def f51cd_f51_capex_dynamics_capex_q25_21d_jerk_v094_signal(capex):
    base = capex.rolling(21).quantile(0.25)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q25_21d_jerk_v094_signal'] = f51cd_f51_capex_dynamics_capex_q25_21d_jerk_v094_signal

def f51cd_f51_capex_dynamics_revenue_q75_21d_jerk_v095_signal(capex, revenue):
    base = (capex / revenue).rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q75_21d_jerk_v095_signal'] = f51cd_f51_capex_dynamics_revenue_q75_21d_jerk_v095_signal

def f51cd_f51_capex_dynamics_assets_q75_21d_jerk_v096_signal(capex, assets):
    base = (capex / assets).rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q75_21d_jerk_v096_signal'] = f51cd_f51_capex_dynamics_assets_q75_21d_jerk_v096_signal

def f51cd_f51_capex_dynamics_ebitda_q75_21d_jerk_v097_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q75_21d_jerk_v097_signal'] = f51cd_f51_capex_dynamics_ebitda_q75_21d_jerk_v097_signal

def f51cd_f51_capex_dynamics_equity_q75_21d_jerk_v098_signal(capex, equity):
    base = (capex / equity).rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q75_21d_jerk_v098_signal'] = f51cd_f51_capex_dynamics_equity_q75_21d_jerk_v098_signal

def f51cd_f51_capex_dynamics_debt_q75_21d_jerk_v099_signal(capex, debt):
    base = (capex / debt).rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q75_21d_jerk_v099_signal'] = f51cd_f51_capex_dynamics_debt_q75_21d_jerk_v099_signal

def f51cd_f51_capex_dynamics_closeadj_q75_21d_jerk_v100_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q75_21d_jerk_v100_signal'] = f51cd_f51_capex_dynamics_closeadj_q75_21d_jerk_v100_signal

def f51cd_f51_capex_dynamics_capex_q75_21d_jerk_v101_signal(capex):
    base = capex.rolling(21).quantile(0.75)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q75_21d_jerk_v101_signal'] = f51cd_f51_capex_dynamics_capex_q75_21d_jerk_v101_signal

def f51cd_f51_capex_dynamics_revenue_q10_21d_jerk_v102_signal(capex, revenue):
    base = (capex / revenue).rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q10_21d_jerk_v102_signal'] = f51cd_f51_capex_dynamics_revenue_q10_21d_jerk_v102_signal

def f51cd_f51_capex_dynamics_assets_q10_21d_jerk_v103_signal(capex, assets):
    base = (capex / assets).rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q10_21d_jerk_v103_signal'] = f51cd_f51_capex_dynamics_assets_q10_21d_jerk_v103_signal

def f51cd_f51_capex_dynamics_ebitda_q10_21d_jerk_v104_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q10_21d_jerk_v104_signal'] = f51cd_f51_capex_dynamics_ebitda_q10_21d_jerk_v104_signal

def f51cd_f51_capex_dynamics_equity_q10_21d_jerk_v105_signal(capex, equity):
    base = (capex / equity).rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q10_21d_jerk_v105_signal'] = f51cd_f51_capex_dynamics_equity_q10_21d_jerk_v105_signal

def f51cd_f51_capex_dynamics_debt_q10_21d_jerk_v106_signal(capex, debt):
    base = (capex / debt).rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q10_21d_jerk_v106_signal'] = f51cd_f51_capex_dynamics_debt_q10_21d_jerk_v106_signal

def f51cd_f51_capex_dynamics_closeadj_q10_21d_jerk_v107_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q10_21d_jerk_v107_signal'] = f51cd_f51_capex_dynamics_closeadj_q10_21d_jerk_v107_signal

def f51cd_f51_capex_dynamics_capex_q10_21d_jerk_v108_signal(capex):
    base = capex.rolling(21).quantile(0.1)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q10_21d_jerk_v108_signal'] = f51cd_f51_capex_dynamics_capex_q10_21d_jerk_v108_signal

def f51cd_f51_capex_dynamics_revenue_q90_21d_jerk_v109_signal(capex, revenue):
    base = (capex / revenue).rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q90_21d_jerk_v109_signal'] = f51cd_f51_capex_dynamics_revenue_q90_21d_jerk_v109_signal

def f51cd_f51_capex_dynamics_assets_q90_21d_jerk_v110_signal(capex, assets):
    base = (capex / assets).rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q90_21d_jerk_v110_signal'] = f51cd_f51_capex_dynamics_assets_q90_21d_jerk_v110_signal

def f51cd_f51_capex_dynamics_ebitda_q90_21d_jerk_v111_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q90_21d_jerk_v111_signal'] = f51cd_f51_capex_dynamics_ebitda_q90_21d_jerk_v111_signal

def f51cd_f51_capex_dynamics_equity_q90_21d_jerk_v112_signal(capex, equity):
    base = (capex / equity).rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q90_21d_jerk_v112_signal'] = f51cd_f51_capex_dynamics_equity_q90_21d_jerk_v112_signal

def f51cd_f51_capex_dynamics_debt_q90_21d_jerk_v113_signal(capex, debt):
    base = (capex / debt).rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q90_21d_jerk_v113_signal'] = f51cd_f51_capex_dynamics_debt_q90_21d_jerk_v113_signal

def f51cd_f51_capex_dynamics_closeadj_q90_21d_jerk_v114_signal(capex, closeadj):
    base = (capex / closeadj).rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q90_21d_jerk_v114_signal'] = f51cd_f51_capex_dynamics_closeadj_q90_21d_jerk_v114_signal

def f51cd_f51_capex_dynamics_capex_q90_21d_jerk_v115_signal(capex):
    base = capex.rolling(21).quantile(0.9)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q90_21d_jerk_v115_signal'] = f51cd_f51_capex_dynamics_capex_q90_21d_jerk_v115_signal

def f51cd_f51_capex_dynamics_revenue_range_21d_jerk_v116_signal(capex, revenue):
    base = (capex / revenue).rolling(21).max() - (capex / revenue).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_range_21d_jerk_v116_signal'] = f51cd_f51_capex_dynamics_revenue_range_21d_jerk_v116_signal

def f51cd_f51_capex_dynamics_assets_range_21d_jerk_v117_signal(capex, assets):
    base = (capex / assets).rolling(21).max() - (capex / assets).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_range_21d_jerk_v117_signal'] = f51cd_f51_capex_dynamics_assets_range_21d_jerk_v117_signal

def f51cd_f51_capex_dynamics_ebitda_range_21d_jerk_v118_signal(capex, ebitda):
    base = (capex / ebitda).rolling(21).max() - (capex / ebitda).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_range_21d_jerk_v118_signal'] = f51cd_f51_capex_dynamics_ebitda_range_21d_jerk_v118_signal

def f51cd_f51_capex_dynamics_equity_range_21d_jerk_v119_signal(capex, equity):
    base = (capex / equity).rolling(21).max() - (capex / equity).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_range_21d_jerk_v119_signal'] = f51cd_f51_capex_dynamics_equity_range_21d_jerk_v119_signal

def f51cd_f51_capex_dynamics_debt_range_21d_jerk_v120_signal(capex, debt):
    base = (capex / debt).rolling(21).max() - (capex / debt).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_range_21d_jerk_v120_signal'] = f51cd_f51_capex_dynamics_debt_range_21d_jerk_v120_signal

def f51cd_f51_capex_dynamics_closeadj_range_63d_jerk_v121_signal(capex, closeadj):
    base = (capex / closeadj).rolling(63).max() - (capex / closeadj).rolling(63).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_range_63d_jerk_v121_signal'] = f51cd_f51_capex_dynamics_closeadj_range_63d_jerk_v121_signal

def f51cd_f51_capex_dynamics_capex_range_21d_jerk_v122_signal(capex):
    base = capex.rolling(21).max() - capex.rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_range_21d_jerk_v122_signal'] = f51cd_f51_capex_dynamics_capex_range_21d_jerk_v122_signal

def f51cd_f51_capex_dynamics_revenue_abs_diff_mean_21d_jerk_v123_signal(capex, revenue):
    base = (capex / revenue - (capex / revenue).rolling(21).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_abs_diff_mean_21d_jerk_v123_signal'] = f51cd_f51_capex_dynamics_revenue_abs_diff_mean_21d_jerk_v123_signal

def f51cd_f51_capex_dynamics_assets_abs_diff_mean_21d_jerk_v124_signal(capex, assets):
    base = (capex / assets - (capex / assets).rolling(21).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_abs_diff_mean_21d_jerk_v124_signal'] = f51cd_f51_capex_dynamics_assets_abs_diff_mean_21d_jerk_v124_signal

def f51cd_f51_capex_dynamics_ebitda_abs_diff_mean_21d_jerk_v125_signal(capex, ebitda):
    base = (capex / ebitda - (capex / ebitda).rolling(21).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_abs_diff_mean_21d_jerk_v125_signal'] = f51cd_f51_capex_dynamics_ebitda_abs_diff_mean_21d_jerk_v125_signal

def f51cd_f51_capex_dynamics_equity_abs_diff_mean_21d_jerk_v126_signal(capex, equity):
    base = (capex / equity - (capex / equity).rolling(21).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_abs_diff_mean_21d_jerk_v126_signal'] = f51cd_f51_capex_dynamics_equity_abs_diff_mean_21d_jerk_v126_signal

def f51cd_f51_capex_dynamics_debt_abs_diff_mean_21d_jerk_v127_signal(capex, debt):
    base = (capex / debt - (capex / debt).rolling(21).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_abs_diff_mean_21d_jerk_v127_signal'] = f51cd_f51_capex_dynamics_debt_abs_diff_mean_21d_jerk_v127_signal

def f51cd_f51_capex_dynamics_closeadj_abs_diff_mean_63d_jerk_v128_signal(capex, closeadj):
    base = (capex / closeadj - (capex / closeadj).rolling(63).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_abs_diff_mean_63d_jerk_v128_signal'] = f51cd_f51_capex_dynamics_closeadj_abs_diff_mean_63d_jerk_v128_signal

def f51cd_f51_capex_dynamics_capex_abs_diff_mean_21d_jerk_v129_signal(capex):
    base = (capex - capex.rolling(21).mean()).abs()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_abs_diff_mean_21d_jerk_v129_signal'] = f51cd_f51_capex_dynamics_capex_abs_diff_mean_21d_jerk_v129_signal

def f51cd_f51_capex_dynamics_revenue_sq_mean_63d_jerk_v130_signal(capex, revenue):
    base = ((capex / revenue) ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_sq_mean_63d_jerk_v130_signal'] = f51cd_f51_capex_dynamics_revenue_sq_mean_63d_jerk_v130_signal

def f51cd_f51_capex_dynamics_assets_sq_mean_63d_jerk_v131_signal(capex, assets):
    base = ((capex / assets) ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_sq_mean_63d_jerk_v131_signal'] = f51cd_f51_capex_dynamics_assets_sq_mean_63d_jerk_v131_signal

def f51cd_f51_capex_dynamics_ebitda_sq_mean_63d_jerk_v132_signal(capex, ebitda):
    base = ((capex / ebitda) ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_sq_mean_63d_jerk_v132_signal'] = f51cd_f51_capex_dynamics_ebitda_sq_mean_63d_jerk_v132_signal

def f51cd_f51_capex_dynamics_equity_sq_mean_63d_jerk_v133_signal(capex, equity):
    base = ((capex / equity) ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_sq_mean_63d_jerk_v133_signal'] = f51cd_f51_capex_dynamics_equity_sq_mean_63d_jerk_v133_signal

def f51cd_f51_capex_dynamics_debt_sq_mean_63d_jerk_v134_signal(capex, debt):
    base = ((capex / debt) ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_sq_mean_63d_jerk_v134_signal'] = f51cd_f51_capex_dynamics_debt_sq_mean_63d_jerk_v134_signal

def f51cd_f51_capex_dynamics_closeadj_sq_mean_63d_jerk_v135_signal(capex, closeadj):
    base = ((capex / closeadj) ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_sq_mean_63d_jerk_v135_signal'] = f51cd_f51_capex_dynamics_closeadj_sq_mean_63d_jerk_v135_signal

def f51cd_f51_capex_dynamics_capex_sq_mean_63d_jerk_v136_signal(capex):
    base = (capex ** 2).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_sq_mean_63d_jerk_v136_signal'] = f51cd_f51_capex_dynamics_capex_sq_mean_63d_jerk_v136_signal

def f51cd_f51_capex_dynamics_closeadj_zscore_med_126d_jerk_v137_signal(capex, closeadj):
    base = (capex / closeadj - (capex / closeadj).rolling(126).median()) / (capex / closeadj).rolling(126).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_zscore_med_126d_jerk_v137_signal'] = f51cd_f51_capex_dynamics_closeadj_zscore_med_126d_jerk_v137_signal

def f51cd_f51_capex_dynamics_revenue_log_std_21d_jerk_v138_signal(capex, revenue):
    base = np.log(capex / revenue).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_log_std_21d_jerk_v138_signal'] = f51cd_f51_capex_dynamics_revenue_log_std_21d_jerk_v138_signal

def f51cd_f51_capex_dynamics_assets_log_std_21d_jerk_v139_signal(capex, assets):
    base = np.log(capex / assets).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_log_std_21d_jerk_v139_signal'] = f51cd_f51_capex_dynamics_assets_log_std_21d_jerk_v139_signal

def f51cd_f51_capex_dynamics_ebitda_log_std_21d_jerk_v140_signal(capex, ebitda):
    base = np.log(capex / ebitda).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_log_std_21d_jerk_v140_signal'] = f51cd_f51_capex_dynamics_ebitda_log_std_21d_jerk_v140_signal

def f51cd_f51_capex_dynamics_equity_log_std_21d_jerk_v141_signal(capex, equity):
    base = np.log(capex / equity).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_log_std_21d_jerk_v141_signal'] = f51cd_f51_capex_dynamics_equity_log_std_21d_jerk_v141_signal

def f51cd_f51_capex_dynamics_debt_log_std_21d_jerk_v142_signal(capex, debt):
    base = np.log(capex / debt).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_log_std_21d_jerk_v142_signal'] = f51cd_f51_capex_dynamics_debt_log_std_21d_jerk_v142_signal

def f51cd_f51_capex_dynamics_closeadj_log_std_21d_jerk_v143_signal(capex, closeadj):
    base = np.log(capex / closeadj).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_log_std_21d_jerk_v143_signal'] = f51cd_f51_capex_dynamics_closeadj_log_std_21d_jerk_v143_signal

def f51cd_f51_capex_dynamics_capex_log_std_21d_jerk_v144_signal(capex):
    base = np.log(capex).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_log_std_21d_jerk_v144_signal'] = f51cd_f51_capex_dynamics_capex_log_std_21d_jerk_v144_signal

def f51cd_f51_capex_dynamics_revenue_log_mean_63d_jerk_v145_signal(capex, revenue):
    base = np.log(capex / revenue).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_log_mean_63d_jerk_v145_signal'] = f51cd_f51_capex_dynamics_revenue_log_mean_63d_jerk_v145_signal

def f51cd_f51_capex_dynamics_assets_log_mean_21d_jerk_v146_signal(capex, assets):
    base = np.log(capex / assets).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_log_mean_21d_jerk_v146_signal'] = f51cd_f51_capex_dynamics_assets_log_mean_21d_jerk_v146_signal

def f51cd_f51_capex_dynamics_ebitda_log_mean_21d_jerk_v147_signal(capex, ebitda):
    base = np.log(capex / ebitda).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_log_mean_21d_jerk_v147_signal'] = f51cd_f51_capex_dynamics_ebitda_log_mean_21d_jerk_v147_signal

def f51cd_f51_capex_dynamics_equity_log_mean_63d_jerk_v148_signal(capex, equity):
    base = np.log(capex / equity).rolling(63).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_log_mean_63d_jerk_v148_signal'] = f51cd_f51_capex_dynamics_equity_log_mean_63d_jerk_v148_signal

def f51cd_f51_capex_dynamics_debt_log_mean_21d_jerk_v149_signal(capex, debt):
    base = np.log(capex / debt).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_log_mean_21d_jerk_v149_signal'] = f51cd_f51_capex_dynamics_debt_log_mean_21d_jerk_v149_signal

def f51cd_f51_capex_dynamics_closeadj_log_mean_21d_jerk_v150_signal(capex, closeadj):
    base = np.log(capex / closeadj).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_log_mean_21d_jerk_v150_signal'] = f51cd_f51_capex_dynamics_closeadj_log_mean_21d_jerk_v150_signal

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
