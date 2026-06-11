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
def _f40ccc_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f40ccc_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f40ccc_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f40ccc_diff(a, b):
    return a - b


# 21d signed cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_21d_base_v076_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_63d_base_v077_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_126d_base_v078_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_252d_base_v079_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_504d_base_v080_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_21d_base_v081_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_63d_base_v082_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_126d_base_v083_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_252d_base_v084_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_504d_base_v085_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of cash conversion cycle (DIO + DSO - DPO) (5 vs 21)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_21d_base_v086_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=5, adjust=False).mean() - M.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of cash conversion cycle (DIO + DSO - DPO) (21 vs 63)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_63d_base_v087_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of cash conversion cycle (DIO + DSO - DPO) (63 vs 126)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_126d_base_v088_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of cash conversion cycle (DIO + DSO - DPO) (126 vs 252)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_252d_base_v089_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of cash conversion cycle (DIO + DSO - DPO) (252 vs 504)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_504d_base_v090_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of cash conversion cycle (DIO + DSO - DPO) (21 vs 63)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_21d_base_v091_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of cash conversion cycle (DIO + DSO - DPO) (63 vs 126)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_63d_base_v092_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of cash conversion cycle (DIO + DSO - DPO) (126 vs 252)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_126d_base_v093_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of cash conversion cycle (DIO + DSO - DPO) (252 vs 504)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_252d_base_v094_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of cash conversion cycle (DIO + DSO - DPO) (504 vs 756)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_504d_base_v095_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.ewm(span=504, adjust=False).mean() - M.ewm(span=756, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs z-score magnitude of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_21d_base_v096_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs z-score magnitude of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_63d_base_v097_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d abs z-score magnitude of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_126d_base_v098_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs z-score magnitude of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_252d_base_v099_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs z-score magnitude of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_504d_base_v100_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_21d_base_v101_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_63d_base_v102_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_126d_base_v103_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_252d_base_v104_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_504d_base_v105_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_21d_base_v106_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_63d_base_v107_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_126d_base_v108_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_252d_base_v109_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_504d_base_v110_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    result = _mean(d.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_21d_base_v111_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 21) / _mean(M, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_63d_base_v112_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 63) / _mean(M, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_126d_base_v113_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_252d_base_v114_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 252) / _mean(M, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_504d_base_v115_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 504) / _mean(M, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log of abs cash conversion cycle (DIO + DSO - DPO) smoothed
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_21d_base_v116_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = np.log(M.abs().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log of abs cash conversion cycle (DIO + DSO - DPO) smoothed
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_63d_base_v117_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = np.log(M.abs().replace(0, np.nan)).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log of abs cash conversion cycle (DIO + DSO - DPO) smoothed
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_126d_base_v118_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = np.log(M.abs().replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of abs cash conversion cycle (DIO + DSO - DPO) smoothed
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_252d_base_v119_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of abs cash conversion cycle (DIO + DSO - DPO) smoothed
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_504d_base_v120_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = np.log(M.abs().replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_21d_base_v121_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_63d_base_v122_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_126d_base_v123_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_252d_base_v124_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_504d_base_v125_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_21d_base_v126_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_63d_base_v127_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pct change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_126d_base_v128_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_252d_base_v129_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pct change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_504d_base_v130_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross of cash conversion cycle (DIO + DSO - DPO) above its 63d mean (signed gap)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_21d_base_v131_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross of cash conversion cycle (DIO + DSO - DPO) above its 126d mean (signed gap)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_63d_base_v132_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cross of cash conversion cycle (DIO + DSO - DPO) above its 252d mean (signed gap)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_126d_base_v133_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross of cash conversion cycle (DIO + DSO - DPO) above its 504d mean (signed gap)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_252d_base_v134_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cross of cash conversion cycle (DIO + DSO - DPO) above its 756d mean (signed gap)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_504d_base_v135_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed sum of changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_21d_base_v136_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed sum of changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_63d_base_v137_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed sum of changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_126d_base_v138_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed sum of changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_252d_base_v139_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed sum of changes in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_504d_base_v140_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days cash conversion cycle (DIO + DSO - DPO) above its rolling median
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_21d_base_v141_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(21, min_periods=10).median()
    result = (M > med).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days cash conversion cycle (DIO + DSO - DPO) above its rolling median
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_63d_base_v142_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(63, min_periods=31).median()
    result = (M > med).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days cash conversion cycle (DIO + DSO - DPO) above its rolling median
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_126d_base_v143_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(126, min_periods=63).median()
    result = (M > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days cash conversion cycle (DIO + DSO - DPO) above its rolling median
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_252d_base_v144_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    result = (M > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days cash conversion cycle (DIO + DSO - DPO) above its rolling median
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_504d_base_v145_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    result = (M > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z (this + 5d z)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_21d_base_v146_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 21) + _z(M, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z (this + 21d z)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_63d_base_v147_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 63) + _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z (this + 63d z)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_126d_base_v148_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 126) + _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z (this + 126d z)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_252d_base_v149_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 252) + _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z (this + 252d z)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_504d_base_v150_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 504) + _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


