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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f40ccc_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f40ccc_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f40ccc_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f40ccc_diff(a, b):
    return a - b


# 5d slope of 21d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_21d_slope_v001_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_21d_slope_v002_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_21d_slope_v003_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_21d_slope_v004_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d level of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevel_21d_slope_v005_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d levelrel of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_63d_slope_v006_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d levelrel of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_63d_slope_v007_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d levelrel of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_63d_slope_v008_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d levelrel of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_63d_slope_v009_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d levelrel of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclevelrel_63d_slope_v010_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_126d_slope_v011_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_126d_slope_v012_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_126d_slope_v013_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_126d_slope_v014_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d mean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmean_126d_slope_v015_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_252d_slope_v016_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_252d_slope_v017_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_252d_slope_v018_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_252d_slope_v019_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccz_252d_slope_v020_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d robz of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_504d_slope_v021_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d robz of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_504d_slope_v022_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d robz of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_504d_slope_v023_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robz of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_504d_slope_v024_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d robz of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrobz_504d_slope_v025_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_21d_slope_v026_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_21d_slope_v027_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_21d_slope_v028_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_21d_slope_v029_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d max of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmax_21d_slope_v030_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_63d_slope_v031_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _min(M, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_63d_slope_v032_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _min(M, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_63d_slope_v033_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _min(M, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_63d_slope_v034_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _min(M, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d min of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccmin_63d_slope_v035_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _min(M, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d rng of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_126d_slope_v036_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rng of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_126d_slope_v037_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d rng of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_126d_slope_v038_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d rng of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_126d_slope_v039_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d rng of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccrng_126d_slope_v040_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pos of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpos_252d_slope_v041_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pos of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpos_252d_slope_v042_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pos of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpos_252d_slope_v043_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pos of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpos_252d_slope_v044_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pos of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpos_252d_slope_v045_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d dd of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdd_504d_slope_v046_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d dd of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdd_504d_slope_v047_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d dd of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdd_504d_slope_v048_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dd of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdd_504d_slope_v049_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d dd of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdd_504d_slope_v050_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d up of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccup_21d_slope_v051_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d up of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccup_21d_slope_v052_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d up of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccup_21d_slope_v053_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d up of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccup_21d_slope_v054_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d up of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccup_21d_slope_v055_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_63d_slope_v056_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_63d_slope_v057_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_63d_slope_v058_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_63d_slope_v059_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccstd_63d_slope_v060_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_126d_slope_v061_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_126d_slope_v062_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_126d_slope_v063_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_126d_slope_v064_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d skew of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccskew_126d_slope_v065_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d kurt of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_252d_slope_v066_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d kurt of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_252d_slope_v067_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d kurt of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_252d_slope_v068_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d kurt of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_252d_slope_v069_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d kurt of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccckurt_252d_slope_v070_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d hits of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_504d_slope_v071_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d hits of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_504d_slope_v072_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d hits of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_504d_slope_v073_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d hits of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_504d_slope_v074_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d hits of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchits_504d_slope_v075_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d signcum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_21d_slope_v076_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d signcum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_21d_slope_v077_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d signcum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_21d_slope_v078_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d signcum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_21d_slope_v079_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d signcum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccsigncum_21d_slope_v080_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d cum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_63d_slope_v081_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_63d_slope_v082_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d cum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_63d_slope_v083_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d cum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_63d_slope_v084_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d cum of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccum_63d_slope_v085_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d emafast of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_126d_slope_v086_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d emafast of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_126d_slope_v087_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d emafast of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_126d_slope_v088_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d emafast of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_126d_slope_v089_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d emafast of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemafast_126d_slope_v090_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d emaslow of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_252d_slope_v091_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d emaslow of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_252d_slope_v092_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d emaslow of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_252d_slope_v093_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d emaslow of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_252d_slope_v094_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d emaslow of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccemaslow_252d_slope_v095_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d zabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_504d_slope_v096_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d zabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_504d_slope_v097_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d zabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_504d_slope_v098_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d zabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_504d_slope_v099_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d zabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccczabs_504d_slope_v100_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d posmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_21d_slope_v101_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d posmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_21d_slope_v102_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d posmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_21d_slope_v103_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d posmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_21d_slope_v104_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d posmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccposmean_21d_slope_v105_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d negmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_63d_slope_v106_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d negmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_63d_slope_v107_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d negmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_63d_slope_v108_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d negmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_63d_slope_v109_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d negmean of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccnegmean_63d_slope_v110_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d cvar of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_126d_slope_v111_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d cvar of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_126d_slope_v112_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cvar of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_126d_slope_v113_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d cvar of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_126d_slope_v114_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d cvar of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccvar_126d_slope_v115_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d logabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_252d_slope_v116_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d logabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_252d_slope_v117_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d logabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_252d_slope_v118_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d logabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_252d_slope_v119_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d logabs of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccclogabs_252d_slope_v120_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d diff of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_504d_slope_v121_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d diff of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_504d_slope_v122_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d diff of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_504d_slope_v123_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d diff of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_504d_slope_v124_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d diff of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccdiff_504d_slope_v125_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pctchg of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_21d_slope_v126_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pctchg of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_21d_slope_v127_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pctchg of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_21d_slope_v128_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pctchg of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_21d_slope_v129_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pctchg of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccpctchg_21d_slope_v130_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d xover of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_63d_slope_v131_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d xover of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_63d_slope_v132_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d xover of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_63d_slope_v133_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d xover of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_63d_slope_v134_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d xover of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_cccxover_63d_slope_v135_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d trend of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_126d_slope_v136_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d trend of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_126d_slope_v137_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d trend of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_126d_slope_v138_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d trend of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_126d_slope_v139_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d trend of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccctrend_126d_slope_v140_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d highmask of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_252d_slope_v141_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d highmask of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_252d_slope_v142_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d highmask of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_252d_slope_v143_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d highmask of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_252d_slope_v144_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d highmask of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccchighmask_252d_slope_v145_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d compositez of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_504d_slope_v146_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d compositez of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_504d_slope_v147_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d compositez of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_504d_slope_v148_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d compositez of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_504d_slope_v149_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d compositez of cash conversion cycle (DIO + DSO - DPO)
def f40ccc_f40_semi_cash_conv_cycle_ccccompositez_504d_slope_v150_signal(inventory, receivables, payables, revenue, closeadj):
    dio = _f40ccc_ratio(inventory, revenue) * 365
    dso = _f40ccc_ratio(receivables, revenue) * 365
    dpo = _f40ccc_ratio(payables, revenue) * 365
    M = dio + dso - dpo
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


