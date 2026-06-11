import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f37iat_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f37iat_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f37iat_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f37iat_diff(a, b):
    return a - b


# 21d signed cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_21d_base_v076_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_63d_base_v077_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_126d_base_v078_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_252d_base_v079_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_504d_base_v080_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_21d_base_v081_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_63d_base_v082_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_126d_base_v083_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_252d_base_v084_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_504d_base_v085_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of inventory to assets ratio (5 vs 21)
def f37iat_f37_semi_inventory_to_assets_invastemafast_21d_base_v086_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=5, adjust=False).mean() - M.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of inventory to assets ratio (21 vs 63)
def f37iat_f37_semi_inventory_to_assets_invastemafast_63d_base_v087_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of inventory to assets ratio (63 vs 126)
def f37iat_f37_semi_inventory_to_assets_invastemafast_126d_base_v088_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of inventory to assets ratio (126 vs 252)
def f37iat_f37_semi_inventory_to_assets_invastemafast_252d_base_v089_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of inventory to assets ratio (252 vs 504)
def f37iat_f37_semi_inventory_to_assets_invastemafast_504d_base_v090_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of inventory to assets ratio (21 vs 63)
def f37iat_f37_semi_inventory_to_assets_invastemaslow_21d_base_v091_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of inventory to assets ratio (63 vs 126)
def f37iat_f37_semi_inventory_to_assets_invastemaslow_63d_base_v092_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of inventory to assets ratio (126 vs 252)
def f37iat_f37_semi_inventory_to_assets_invastemaslow_126d_base_v093_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of inventory to assets ratio (252 vs 504)
def f37iat_f37_semi_inventory_to_assets_invastemaslow_252d_base_v094_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of inventory to assets ratio (504 vs 756)
def f37iat_f37_semi_inventory_to_assets_invastemaslow_504d_base_v095_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.ewm(span=504, adjust=False).mean() - M.ewm(span=756, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs z-score magnitude of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_21d_base_v096_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs z-score magnitude of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_63d_base_v097_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d abs z-score magnitude of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_126d_base_v098_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs z-score magnitude of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_252d_base_v099_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs z-score magnitude of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_504d_base_v100_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_21d_base_v101_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_63d_base_v102_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_126d_base_v103_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_252d_base_v104_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_504d_base_v105_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_21d_base_v106_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_63d_base_v107_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_126d_base_v108_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_252d_base_v109_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_504d_base_v110_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    result = _mean(d.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_21d_base_v111_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 21) / _mean(M, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_63d_base_v112_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 63) / _mean(M, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_126d_base_v113_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_252d_base_v114_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 252) / _mean(M, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_504d_base_v115_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 504) / _mean(M, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log of abs inventory to assets ratio smoothed
def f37iat_f37_semi_inventory_to_assets_invastlogabs_21d_base_v116_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = np.log(M.abs().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log of abs inventory to assets ratio smoothed
def f37iat_f37_semi_inventory_to_assets_invastlogabs_63d_base_v117_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = np.log(M.abs().replace(0, np.nan)).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log of abs inventory to assets ratio smoothed
def f37iat_f37_semi_inventory_to_assets_invastlogabs_126d_base_v118_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = np.log(M.abs().replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of abs inventory to assets ratio smoothed
def f37iat_f37_semi_inventory_to_assets_invastlogabs_252d_base_v119_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of abs inventory to assets ratio smoothed
def f37iat_f37_semi_inventory_to_assets_invastlogabs_504d_base_v120_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = np.log(M.abs().replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_21d_base_v121_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_63d_base_v122_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_126d_base_v123_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_252d_base_v124_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_504d_base_v125_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_21d_base_v126_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_63d_base_v127_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pct change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_126d_base_v128_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_252d_base_v129_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pct change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_504d_base_v130_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross of inventory to assets ratio above its 63d mean (signed gap)
def f37iat_f37_semi_inventory_to_assets_invastxover_21d_base_v131_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross of inventory to assets ratio above its 126d mean (signed gap)
def f37iat_f37_semi_inventory_to_assets_invastxover_63d_base_v132_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cross of inventory to assets ratio above its 252d mean (signed gap)
def f37iat_f37_semi_inventory_to_assets_invastxover_126d_base_v133_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross of inventory to assets ratio above its 504d mean (signed gap)
def f37iat_f37_semi_inventory_to_assets_invastxover_252d_base_v134_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cross of inventory to assets ratio above its 756d mean (signed gap)
def f37iat_f37_semi_inventory_to_assets_invastxover_504d_base_v135_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed sum of changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_21d_base_v136_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed sum of changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_63d_base_v137_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed sum of changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_126d_base_v138_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed sum of changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_252d_base_v139_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed sum of changes in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_504d_base_v140_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days inventory to assets ratio above its rolling median
def f37iat_f37_semi_inventory_to_assets_invasthighmask_21d_base_v141_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(21, min_periods=10).median()
    result = (M > med).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days inventory to assets ratio above its rolling median
def f37iat_f37_semi_inventory_to_assets_invasthighmask_63d_base_v142_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(63, min_periods=31).median()
    result = (M > med).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days inventory to assets ratio above its rolling median
def f37iat_f37_semi_inventory_to_assets_invasthighmask_126d_base_v143_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(126, min_periods=63).median()
    result = (M > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days inventory to assets ratio above its rolling median
def f37iat_f37_semi_inventory_to_assets_invasthighmask_252d_base_v144_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    result = (M > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days inventory to assets ratio above its rolling median
def f37iat_f37_semi_inventory_to_assets_invasthighmask_504d_base_v145_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    result = (M > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z (this + 5d z)
def f37iat_f37_semi_inventory_to_assets_invastcompositez_21d_base_v146_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 21) + _z(M, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z (this + 21d z)
def f37iat_f37_semi_inventory_to_assets_invastcompositez_63d_base_v147_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 63) + _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z (this + 63d z)
def f37iat_f37_semi_inventory_to_assets_invastcompositez_126d_base_v148_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 126) + _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z (this + 126d z)
def f37iat_f37_semi_inventory_to_assets_invastcompositez_252d_base_v149_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 252) + _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z (this + 252d z)
def f37iat_f37_semi_inventory_to_assets_invastcompositez_504d_base_v150_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 504) + _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


