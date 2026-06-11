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
def _f31cpe_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f31cpe_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f31cpe_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f31cpe_diff(a, b):
    return a - b


# 21d signed cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_21d_base_v076_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_63d_base_v077_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_126d_base_v078_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_252d_base_v079_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_504d_base_v080_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_21d_base_v081_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_63d_base_v082_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_126d_base_v083_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_252d_base_v084_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_504d_base_v085_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of capex efficiency (capex/ppne) (5 vs 21)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_21d_base_v086_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=5, adjust=False).mean() - M.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of capex efficiency (capex/ppne) (21 vs 63)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_63d_base_v087_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of capex efficiency (capex/ppne) (63 vs 126)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_126d_base_v088_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of capex efficiency (capex/ppne) (126 vs 252)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_252d_base_v089_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of capex efficiency (capex/ppne) (252 vs 504)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_504d_base_v090_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of capex efficiency (capex/ppne) (21 vs 63)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_21d_base_v091_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of capex efficiency (capex/ppne) (63 vs 126)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_63d_base_v092_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of capex efficiency (capex/ppne) (126 vs 252)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_126d_base_v093_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of capex efficiency (capex/ppne) (252 vs 504)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_252d_base_v094_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of capex efficiency (capex/ppne) (504 vs 756)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_504d_base_v095_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.ewm(span=504, adjust=False).mean() - M.ewm(span=756, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs z-score magnitude of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_21d_base_v096_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs z-score magnitude of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_63d_base_v097_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d abs z-score magnitude of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_126d_base_v098_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs z-score magnitude of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_252d_base_v099_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs z-score magnitude of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_504d_base_v100_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_21d_base_v101_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_63d_base_v102_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_126d_base_v103_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_252d_base_v104_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_504d_base_v105_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_21d_base_v106_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_63d_base_v107_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_126d_base_v108_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_252d_base_v109_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_504d_base_v110_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    result = _mean(d.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_21d_base_v111_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 21) / _mean(M, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_63d_base_v112_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 63) / _mean(M, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_126d_base_v113_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_252d_base_v114_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 252) / _mean(M, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_504d_base_v115_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 504) / _mean(M, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log of abs capex efficiency (capex/ppne) smoothed
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_21d_base_v116_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = np.log(M.abs().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log of abs capex efficiency (capex/ppne) smoothed
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_63d_base_v117_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = np.log(M.abs().replace(0, np.nan)).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log of abs capex efficiency (capex/ppne) smoothed
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_126d_base_v118_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = np.log(M.abs().replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of abs capex efficiency (capex/ppne) smoothed
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_252d_base_v119_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of abs capex efficiency (capex/ppne) smoothed
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_504d_base_v120_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = np.log(M.abs().replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_21d_base_v121_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_63d_base_v122_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_126d_base_v123_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_252d_base_v124_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_504d_base_v125_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_21d_base_v126_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_63d_base_v127_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pct change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_126d_base_v128_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_252d_base_v129_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pct change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_504d_base_v130_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross of capex efficiency (capex/ppne) above its 63d mean (signed gap)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_21d_base_v131_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross of capex efficiency (capex/ppne) above its 126d mean (signed gap)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_63d_base_v132_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cross of capex efficiency (capex/ppne) above its 252d mean (signed gap)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_126d_base_v133_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross of capex efficiency (capex/ppne) above its 504d mean (signed gap)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_252d_base_v134_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cross of capex efficiency (capex/ppne) above its 756d mean (signed gap)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_504d_base_v135_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed sum of changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_21d_base_v136_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed sum of changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_63d_base_v137_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed sum of changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_126d_base_v138_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed sum of changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_252d_base_v139_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed sum of changes in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_504d_base_v140_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days capex efficiency (capex/ppne) above its rolling median
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_21d_base_v141_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(21, min_periods=10).median()
    result = (M > med).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days capex efficiency (capex/ppne) above its rolling median
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_63d_base_v142_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(63, min_periods=31).median()
    result = (M > med).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days capex efficiency (capex/ppne) above its rolling median
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_126d_base_v143_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(126, min_periods=63).median()
    result = (M > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days capex efficiency (capex/ppne) above its rolling median
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_252d_base_v144_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    result = (M > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days capex efficiency (capex/ppne) above its rolling median
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_504d_base_v145_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    result = (M > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z (this + 5d z)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_21d_base_v146_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 21) + _z(M, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z (this + 21d z)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_63d_base_v147_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 63) + _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z (this + 63d z)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_126d_base_v148_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 126) + _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z (this + 126d z)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_252d_base_v149_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 252) + _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z (this + 252d z)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_504d_base_v150_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 504) + _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


