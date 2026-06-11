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


# 21d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_21d_base_v001_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_63d_base_v002_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_126d_base_v003_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_252d_base_v004_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_504d_base_v005_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_21d_base_v006_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_63d_base_v007_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_126d_base_v008_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_252d_base_v009_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_504d_base_v010_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_21d_base_v011_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_63d_base_v012_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_126d_base_v013_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_252d_base_v014_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_504d_base_v015_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_21d_base_v016_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_63d_base_v017_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_126d_base_v018_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_252d_base_v019_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_504d_base_v020_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of cash conversion cycle (DIO + DSO - DPO) (median/MAD)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_21d_base_v021_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of cash conversion cycle (DIO + DSO - DPO) (median/MAD)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_63d_base_v022_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of cash conversion cycle (DIO + DSO - DPO) (median/MAD)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_126d_base_v023_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of cash conversion cycle (DIO + DSO - DPO) (median/MAD)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_252d_base_v024_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of cash conversion cycle (DIO + DSO - DPO) (median/MAD)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_504d_base_v025_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_21d_base_v026_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_63d_base_v027_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_126d_base_v028_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_252d_base_v029_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_504d_base_v030_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_21d_base_v031_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_63d_base_v032_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_126d_base_v033_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_252d_base_v034_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_504d_base_v035_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_21d_base_v036_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_63d_base_v037_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_126d_base_v038_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_252d_base_v039_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_504d_base_v040_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of cash conversion cycle (DIO + DSO - DPO) in rolling range
def f40ccc_f40_semi_cash_conv_cycle_cccpos_21d_base_v041_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of cash conversion cycle (DIO + DSO - DPO) in rolling range
def f40ccc_f40_semi_cash_conv_cycle_cccpos_63d_base_v042_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of cash conversion cycle (DIO + DSO - DPO) in rolling range
def f40ccc_f40_semi_cash_conv_cycle_cccpos_126d_base_v043_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of cash conversion cycle (DIO + DSO - DPO) in rolling range
def f40ccc_f40_semi_cash_conv_cycle_cccpos_252d_base_v044_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of cash conversion cycle (DIO + DSO - DPO) in rolling range
def f40ccc_f40_semi_cash_conv_cycle_cccpos_504d_base_v045_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of cash conversion cycle (DIO + DSO - DPO) from rolling peak
def f40ccc_f40_semi_cash_conv_cycle_cccdd_21d_base_v046_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of cash conversion cycle (DIO + DSO - DPO) from rolling peak
def f40ccc_f40_semi_cash_conv_cycle_cccdd_63d_base_v047_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of cash conversion cycle (DIO + DSO - DPO) from rolling peak
def f40ccc_f40_semi_cash_conv_cycle_cccdd_126d_base_v048_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of cash conversion cycle (DIO + DSO - DPO) from rolling peak
def f40ccc_f40_semi_cash_conv_cycle_cccdd_252d_base_v049_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of cash conversion cycle (DIO + DSO - DPO) from rolling peak
def f40ccc_f40_semi_cash_conv_cycle_cccdd_504d_base_v050_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of cash conversion cycle (DIO + DSO - DPO) above rolling trough
def f40ccc_f40_semi_cash_conv_cycle_cccup_21d_base_v051_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of cash conversion cycle (DIO + DSO - DPO) above rolling trough
def f40ccc_f40_semi_cash_conv_cycle_cccup_63d_base_v052_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of cash conversion cycle (DIO + DSO - DPO) above rolling trough
def f40ccc_f40_semi_cash_conv_cycle_cccup_126d_base_v053_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of cash conversion cycle (DIO + DSO - DPO) above rolling trough
def f40ccc_f40_semi_cash_conv_cycle_cccup_252d_base_v054_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of cash conversion cycle (DIO + DSO - DPO) above rolling trough
def f40ccc_f40_semi_cash_conv_cycle_cccup_504d_base_v055_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_21d_base_v056_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_63d_base_v057_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_126d_base_v058_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_252d_base_v059_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_504d_base_v060_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_21d_base_v061_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_63d_base_v062_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_126d_base_v063_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_252d_base_v064_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_504d_base_v065_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_21d_base_v066_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_63d_base_v067_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_126d_base_v068_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_252d_base_v069_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_504d_base_v070_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_21d_base_v071_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_63d_base_v072_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_126d_base_v073_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_252d_base_v074_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_504d_base_v075_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


