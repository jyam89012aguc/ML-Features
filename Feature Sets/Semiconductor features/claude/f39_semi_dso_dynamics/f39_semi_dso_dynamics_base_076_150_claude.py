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
def _f39dso_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f39dso_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f39dso_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f39dso_diff(a, b):
    return a - b


# 21d signed cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_21d_base_v076_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_63d_base_v077_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_126d_base_v078_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_252d_base_v079_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_504d_base_v080_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_21d_base_v081_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_63d_base_v082_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_126d_base_v083_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_252d_base_v084_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_504d_base_v085_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of days sales outstanding (DSO) (5 vs 21)
def f39dso_f39_semi_dso_dynamics_dsoemafast_21d_base_v086_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=5, adjust=False).mean() - M.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of days sales outstanding (DSO) (21 vs 63)
def f39dso_f39_semi_dso_dynamics_dsoemafast_63d_base_v087_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of days sales outstanding (DSO) (63 vs 126)
def f39dso_f39_semi_dso_dynamics_dsoemafast_126d_base_v088_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of days sales outstanding (DSO) (126 vs 252)
def f39dso_f39_semi_dso_dynamics_dsoemafast_252d_base_v089_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of days sales outstanding (DSO) (252 vs 504)
def f39dso_f39_semi_dso_dynamics_dsoemafast_504d_base_v090_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of days sales outstanding (DSO) (21 vs 63)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_21d_base_v091_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of days sales outstanding (DSO) (63 vs 126)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_63d_base_v092_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of days sales outstanding (DSO) (126 vs 252)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_126d_base_v093_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of days sales outstanding (DSO) (252 vs 504)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_252d_base_v094_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of days sales outstanding (DSO) (504 vs 756)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_504d_base_v095_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.ewm(span=504, adjust=False).mean() - M.ewm(span=756, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs z-score magnitude of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_21d_base_v096_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs z-score magnitude of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_63d_base_v097_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d abs z-score magnitude of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_126d_base_v098_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs z-score magnitude of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_252d_base_v099_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs z-score magnitude of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_504d_base_v100_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_21d_base_v101_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_63d_base_v102_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_126d_base_v103_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_252d_base_v104_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_504d_base_v105_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_21d_base_v106_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_63d_base_v107_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_126d_base_v108_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_252d_base_v109_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_504d_base_v110_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_21d_base_v111_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _std(M, 21) / _mean(M, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_63d_base_v112_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _std(M, 63) / _mean(M, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_126d_base_v113_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_252d_base_v114_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _std(M, 252) / _mean(M, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_504d_base_v115_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _std(M, 504) / _mean(M, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log of abs days sales outstanding (DSO) smoothed
def f39dso_f39_semi_dso_dynamics_dsologabs_21d_base_v116_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log of abs days sales outstanding (DSO) smoothed
def f39dso_f39_semi_dso_dynamics_dsologabs_63d_base_v117_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log of abs days sales outstanding (DSO) smoothed
def f39dso_f39_semi_dso_dynamics_dsologabs_126d_base_v118_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of abs days sales outstanding (DSO) smoothed
def f39dso_f39_semi_dso_dynamics_dsologabs_252d_base_v119_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of abs days sales outstanding (DSO) smoothed
def f39dso_f39_semi_dso_dynamics_dsologabs_504d_base_v120_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_21d_base_v121_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_63d_base_v122_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_126d_base_v123_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_252d_base_v124_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_504d_base_v125_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_21d_base_v126_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_63d_base_v127_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pct change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_126d_base_v128_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_252d_base_v129_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pct change in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_504d_base_v130_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross of days sales outstanding (DSO) above its 63d mean (signed gap)
def f39dso_f39_semi_dso_dynamics_dsoxover_21d_base_v131_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross of days sales outstanding (DSO) above its 126d mean (signed gap)
def f39dso_f39_semi_dso_dynamics_dsoxover_63d_base_v132_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cross of days sales outstanding (DSO) above its 252d mean (signed gap)
def f39dso_f39_semi_dso_dynamics_dsoxover_126d_base_v133_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross of days sales outstanding (DSO) above its 504d mean (signed gap)
def f39dso_f39_semi_dso_dynamics_dsoxover_252d_base_v134_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cross of days sales outstanding (DSO) above its 756d mean (signed gap)
def f39dso_f39_semi_dso_dynamics_dsoxover_504d_base_v135_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed sum of changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_21d_base_v136_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed sum of changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_63d_base_v137_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed sum of changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_126d_base_v138_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed sum of changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_252d_base_v139_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed sum of changes in days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_504d_base_v140_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days days sales outstanding (DSO) above its rolling median
def f39dso_f39_semi_dso_dynamics_dsohighmask_21d_base_v141_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(21, min_periods=10).median()
    result = (M > med).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days days sales outstanding (DSO) above its rolling median
def f39dso_f39_semi_dso_dynamics_dsohighmask_63d_base_v142_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(63, min_periods=31).median()
    result = (M > med).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days days sales outstanding (DSO) above its rolling median
def f39dso_f39_semi_dso_dynamics_dsohighmask_126d_base_v143_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(126, min_periods=63).median()
    result = (M > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days days sales outstanding (DSO) above its rolling median
def f39dso_f39_semi_dso_dynamics_dsohighmask_252d_base_v144_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    result = (M > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days days sales outstanding (DSO) above its rolling median
def f39dso_f39_semi_dso_dynamics_dsohighmask_504d_base_v145_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    result = (M > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z (this + 5d z)
def f39dso_f39_semi_dso_dynamics_dsocompositez_21d_base_v146_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 21) + _z(M, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z (this + 21d z)
def f39dso_f39_semi_dso_dynamics_dsocompositez_63d_base_v147_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 63) + _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z (this + 63d z)
def f39dso_f39_semi_dso_dynamics_dsocompositez_126d_base_v148_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 126) + _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z (this + 126d z)
def f39dso_f39_semi_dso_dynamics_dsocompositez_252d_base_v149_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 252) + _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z (this + 252d z)
def f39dso_f39_semi_dso_dynamics_dsocompositez_504d_base_v150_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    result = _z(M, 504) + _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


