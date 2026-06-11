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
def _f32cs_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f32cs_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f32cs_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f32cs_diff(a, b):
    return a - b


# 21d signed cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_21d_base_v076_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_63d_base_v077_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_126d_base_v078_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_252d_base_v079_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_504d_base_v080_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_21d_base_v081_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_63d_base_v082_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_126d_base_v083_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_252d_base_v084_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_504d_base_v085_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of capex surprise vs 4q rolling expectation (5 vs 21)
def f32cs_f32_semi_capex_surprise_cpsuremafast_21d_base_v086_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=5, adjust=False).mean() - M.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of capex surprise vs 4q rolling expectation (21 vs 63)
def f32cs_f32_semi_capex_surprise_cpsuremafast_63d_base_v087_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of capex surprise vs 4q rolling expectation (63 vs 126)
def f32cs_f32_semi_capex_surprise_cpsuremafast_126d_base_v088_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of capex surprise vs 4q rolling expectation (126 vs 252)
def f32cs_f32_semi_capex_surprise_cpsuremafast_252d_base_v089_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of capex surprise vs 4q rolling expectation (252 vs 504)
def f32cs_f32_semi_capex_surprise_cpsuremafast_504d_base_v090_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of capex surprise vs 4q rolling expectation (21 vs 63)
def f32cs_f32_semi_capex_surprise_cpsuremaslow_21d_base_v091_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of capex surprise vs 4q rolling expectation (63 vs 126)
def f32cs_f32_semi_capex_surprise_cpsuremaslow_63d_base_v092_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of capex surprise vs 4q rolling expectation (126 vs 252)
def f32cs_f32_semi_capex_surprise_cpsuremaslow_126d_base_v093_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of capex surprise vs 4q rolling expectation (252 vs 504)
def f32cs_f32_semi_capex_surprise_cpsuremaslow_252d_base_v094_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of capex surprise vs 4q rolling expectation (504 vs 756)
def f32cs_f32_semi_capex_surprise_cpsuremaslow_504d_base_v095_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.ewm(span=504, adjust=False).mean() - M.ewm(span=756, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs z-score magnitude of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_21d_base_v096_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs z-score magnitude of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_63d_base_v097_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d abs z-score magnitude of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_126d_base_v098_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs z-score magnitude of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_252d_base_v099_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs z-score magnitude of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_504d_base_v100_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_21d_base_v101_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_63d_base_v102_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_126d_base_v103_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_252d_base_v104_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_504d_base_v105_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_21d_base_v106_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_63d_base_v107_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_126d_base_v108_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_252d_base_v109_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_504d_base_v110_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    result = _mean(d.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_21d_base_v111_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 21) / _mean(M, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_63d_base_v112_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 63) / _mean(M, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_126d_base_v113_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_252d_base_v114_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 252) / _mean(M, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_504d_base_v115_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 504) / _mean(M, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log of abs capex surprise vs 4q rolling expectation smoothed
def f32cs_f32_semi_capex_surprise_cpsurlogabs_21d_base_v116_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = np.log(M.abs().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log of abs capex surprise vs 4q rolling expectation smoothed
def f32cs_f32_semi_capex_surprise_cpsurlogabs_63d_base_v117_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = np.log(M.abs().replace(0, np.nan)).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log of abs capex surprise vs 4q rolling expectation smoothed
def f32cs_f32_semi_capex_surprise_cpsurlogabs_126d_base_v118_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = np.log(M.abs().replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of abs capex surprise vs 4q rolling expectation smoothed
def f32cs_f32_semi_capex_surprise_cpsurlogabs_252d_base_v119_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of abs capex surprise vs 4q rolling expectation smoothed
def f32cs_f32_semi_capex_surprise_cpsurlogabs_504d_base_v120_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = np.log(M.abs().replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_21d_base_v121_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_63d_base_v122_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_126d_base_v123_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_252d_base_v124_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_504d_base_v125_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_21d_base_v126_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_63d_base_v127_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pct change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_126d_base_v128_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_252d_base_v129_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pct change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_504d_base_v130_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross of capex surprise vs 4q rolling expectation above its 63d mean (signed gap)
def f32cs_f32_semi_capex_surprise_cpsurxover_21d_base_v131_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross of capex surprise vs 4q rolling expectation above its 126d mean (signed gap)
def f32cs_f32_semi_capex_surprise_cpsurxover_63d_base_v132_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cross of capex surprise vs 4q rolling expectation above its 252d mean (signed gap)
def f32cs_f32_semi_capex_surprise_cpsurxover_126d_base_v133_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross of capex surprise vs 4q rolling expectation above its 504d mean (signed gap)
def f32cs_f32_semi_capex_surprise_cpsurxover_252d_base_v134_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cross of capex surprise vs 4q rolling expectation above its 756d mean (signed gap)
def f32cs_f32_semi_capex_surprise_cpsurxover_504d_base_v135_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed sum of changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_21d_base_v136_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed sum of changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_63d_base_v137_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed sum of changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_126d_base_v138_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed sum of changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_252d_base_v139_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed sum of changes in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_504d_base_v140_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days capex surprise vs 4q rolling expectation above its rolling median
def f32cs_f32_semi_capex_surprise_cpsurhighmask_21d_base_v141_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(21, min_periods=10).median()
    result = (M > med).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days capex surprise vs 4q rolling expectation above its rolling median
def f32cs_f32_semi_capex_surprise_cpsurhighmask_63d_base_v142_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(63, min_periods=31).median()
    result = (M > med).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days capex surprise vs 4q rolling expectation above its rolling median
def f32cs_f32_semi_capex_surprise_cpsurhighmask_126d_base_v143_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(126, min_periods=63).median()
    result = (M > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days capex surprise vs 4q rolling expectation above its rolling median
def f32cs_f32_semi_capex_surprise_cpsurhighmask_252d_base_v144_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    result = (M > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days capex surprise vs 4q rolling expectation above its rolling median
def f32cs_f32_semi_capex_surprise_cpsurhighmask_504d_base_v145_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    result = (M > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z (this + 5d z)
def f32cs_f32_semi_capex_surprise_cpsurcompositez_21d_base_v146_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 21) + _z(M, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z (this + 21d z)
def f32cs_f32_semi_capex_surprise_cpsurcompositez_63d_base_v147_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 63) + _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z (this + 63d z)
def f32cs_f32_semi_capex_surprise_cpsurcompositez_126d_base_v148_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 126) + _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z (this + 126d z)
def f32cs_f32_semi_capex_surprise_cpsurcompositez_252d_base_v149_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 252) + _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z (this + 252d z)
def f32cs_f32_semi_capex_surprise_cpsurcompositez_504d_base_v150_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 504) + _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


