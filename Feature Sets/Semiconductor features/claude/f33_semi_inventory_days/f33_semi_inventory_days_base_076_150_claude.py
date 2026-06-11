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
def _f33id_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f33id_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f33id_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f33id_diff(a, b):
    return a - b


# 21d signed cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diosigncum_21d_base_v076_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diosigncum_63d_base_v077_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diosigncum_126d_base_v078_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diosigncum_252d_base_v079_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diosigncum_504d_base_v080_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = pd.Series(np.sign(M.diff()), index=M.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocum_21d_base_v081_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocum_63d_base_v082_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocum_126d_base_v083_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocum_252d_base_v084_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocum_504d_base_v085_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of days inventory outstanding (DIO) (5 vs 21)
def f33id_f33_semi_inventory_days_dioemafast_21d_base_v086_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=5, adjust=False).mean() - M.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of days inventory outstanding (DIO) (21 vs 63)
def f33id_f33_semi_inventory_days_dioemafast_63d_base_v087_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of days inventory outstanding (DIO) (63 vs 126)
def f33id_f33_semi_inventory_days_dioemafast_126d_base_v088_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of days inventory outstanding (DIO) (126 vs 252)
def f33id_f33_semi_inventory_days_dioemafast_252d_base_v089_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of days inventory outstanding (DIO) (252 vs 504)
def f33id_f33_semi_inventory_days_dioemafast_504d_base_v090_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of days inventory outstanding (DIO) (21 vs 63)
def f33id_f33_semi_inventory_days_dioemaslow_21d_base_v091_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=21, adjust=False).mean() - M.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of days inventory outstanding (DIO) (63 vs 126)
def f33id_f33_semi_inventory_days_dioemaslow_63d_base_v092_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of days inventory outstanding (DIO) (126 vs 252)
def f33id_f33_semi_inventory_days_dioemaslow_126d_base_v093_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=126, adjust=False).mean() - M.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of days inventory outstanding (DIO) (252 vs 504)
def f33id_f33_semi_inventory_days_dioemaslow_252d_base_v094_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of days inventory outstanding (DIO) (504 vs 756)
def f33id_f33_semi_inventory_days_dioemaslow_504d_base_v095_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.ewm(span=504, adjust=False).mean() - M.ewm(span=756, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs z-score magnitude of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diozabs_21d_base_v096_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs z-score magnitude of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diozabs_63d_base_v097_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d abs z-score magnitude of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diozabs_126d_base_v098_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs z-score magnitude of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diozabs_252d_base_v099_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs z-score magnitude of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diozabs_504d_base_v100_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dioposmean_21d_base_v101_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dioposmean_63d_base_v102_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dioposmean_126d_base_v103_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dioposmean_252d_base_v104_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dioposmean_504d_base_v105_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dionegmean_21d_base_v106_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dionegmean_63d_base_v107_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dionegmean_126d_base_v108_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dionegmean_252d_base_v109_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_dionegmean_504d_base_v110_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    d = M.diff()
    result = _mean(d.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d coefficient of variation of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocvar_21d_base_v111_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _std(M, 21) / _mean(M, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocvar_63d_base_v112_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _std(M, 63) / _mean(M, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocvar_126d_base_v113_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocvar_252d_base_v114_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _std(M, 252) / _mean(M, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diocvar_504d_base_v115_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _std(M, 504) / _mean(M, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log of abs days inventory outstanding (DIO) smoothed
def f33id_f33_semi_inventory_days_diologabs_21d_base_v116_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log of abs days inventory outstanding (DIO) smoothed
def f33id_f33_semi_inventory_days_diologabs_63d_base_v117_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log of abs days inventory outstanding (DIO) smoothed
def f33id_f33_semi_inventory_days_diologabs_126d_base_v118_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of abs days inventory outstanding (DIO) smoothed
def f33id_f33_semi_inventory_days_diologabs_252d_base_v119_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of abs days inventory outstanding (DIO) smoothed
def f33id_f33_semi_inventory_days_diologabs_504d_base_v120_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = np.log(M.abs().replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diodiff_21d_base_v121_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diodiff_63d_base_v122_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diodiff_126d_base_v123_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diodiff_252d_base_v124_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diodiff_504d_base_v125_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diopctchg_21d_base_v126_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diopctchg_63d_base_v127_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pct change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diopctchg_126d_base_v128_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diopctchg_252d_base_v129_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pct change in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diopctchg_504d_base_v130_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross of days inventory outstanding (DIO) above its 63d mean (signed gap)
def f33id_f33_semi_inventory_days_dioxover_21d_base_v131_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross of days inventory outstanding (DIO) above its 126d mean (signed gap)
def f33id_f33_semi_inventory_days_dioxover_63d_base_v132_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cross of days inventory outstanding (DIO) above its 252d mean (signed gap)
def f33id_f33_semi_inventory_days_dioxover_126d_base_v133_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross of days inventory outstanding (DIO) above its 504d mean (signed gap)
def f33id_f33_semi_inventory_days_dioxover_252d_base_v134_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cross of days inventory outstanding (DIO) above its 756d mean (signed gap)
def f33id_f33_semi_inventory_days_dioxover_504d_base_v135_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed sum of changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diotrend_21d_base_v136_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed sum of changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diotrend_63d_base_v137_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed sum of changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diotrend_126d_base_v138_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed sum of changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diotrend_252d_base_v139_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed sum of changes in days inventory outstanding (DIO)
def f33id_f33_semi_inventory_days_diotrend_504d_base_v140_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = M.diff().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days days inventory outstanding (DIO) above its rolling median
def f33id_f33_semi_inventory_days_diohighmask_21d_base_v141_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    med = M.rolling(21, min_periods=10).median()
    result = (M > med).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days days inventory outstanding (DIO) above its rolling median
def f33id_f33_semi_inventory_days_diohighmask_63d_base_v142_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    med = M.rolling(63, min_periods=31).median()
    result = (M > med).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days days inventory outstanding (DIO) above its rolling median
def f33id_f33_semi_inventory_days_diohighmask_126d_base_v143_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    med = M.rolling(126, min_periods=63).median()
    result = (M > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days days inventory outstanding (DIO) above its rolling median
def f33id_f33_semi_inventory_days_diohighmask_252d_base_v144_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    med = M.rolling(252, min_periods=126).median()
    result = (M > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days days inventory outstanding (DIO) above its rolling median
def f33id_f33_semi_inventory_days_diohighmask_504d_base_v145_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    med = M.rolling(504, min_periods=252).median()
    result = (M > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z (this + 5d z)
def f33id_f33_semi_inventory_days_diocompositez_21d_base_v146_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 21) + _z(M, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z (this + 21d z)
def f33id_f33_semi_inventory_days_diocompositez_63d_base_v147_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 63) + _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z (this + 63d z)
def f33id_f33_semi_inventory_days_diocompositez_126d_base_v148_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 126) + _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z (this + 126d z)
def f33id_f33_semi_inventory_days_diocompositez_252d_base_v149_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 252) + _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z (this + 252d z)
def f33id_f33_semi_inventory_days_diocompositez_504d_base_v150_signal(inventory, revenue, gp, closeadj):
    cogs = revenue - gp
    M = _f33id_ratio(inventory, cogs) * 365
    result = _z(M, 504) + _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


