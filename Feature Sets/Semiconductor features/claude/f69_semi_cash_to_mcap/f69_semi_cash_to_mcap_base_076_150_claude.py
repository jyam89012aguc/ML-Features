import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)



# ===== folder domain primitives =====
def _f69_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f69_safe_pct(x, n):
    return x.pct_change(n)


def _f69_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f69_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 21d percent-change of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v076_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d percent-change of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v077_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d percent-change of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v078_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d percent-change of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v079_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d percent-change of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v080_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.pct_change(504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level-change (diff) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v081_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level-change (diff) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v082_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level-change (diff) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v083_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level-change (diff) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v084_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level-change (diff) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v085_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.diff(504)
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 5/21 - 1 of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_5d_base_v086_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    fastm = m.ewm(span=5, adjust=False).mean()
    slowm = m.ewm(span=21, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 21/63 - 1 of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v087_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    fastm = m.ewm(span=21, adjust=False).mean()
    slowm = m.ewm(span=63, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 63/126 - 1 of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v088_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    fastm = m.ewm(span=63, adjust=False).mean()
    slowm = m.ewm(span=126, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 126/252 - 1 of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v089_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    fastm = m.ewm(span=126, adjust=False).mean()
    slowm = m.ewm(span=252, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 252/504 - 1 of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v090_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    fastm = m.ewm(span=252, adjust=False).mean()
    slowm = m.ewm(span=504, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# 21d secondary metric (cash_g) demeaned
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_base_v091_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = s2 - _mean(s2, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d secondary metric (cash_g) demeaned
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_base_v092_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = s2 - _mean(s2, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d secondary metric (cash_g) demeaned
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_base_v093_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = s2 - _mean(s2, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d secondary metric (cash_g) demeaned
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_base_v094_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = s2 - _mean(s2, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d secondary metric (cash_g) demeaned
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_base_v095_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = s2 - _mean(s2, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of secondary metric (cash_g)
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_base_v096_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = _z(s2, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of secondary metric (cash_g)
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_base_v097_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = _z(s2, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of secondary metric (cash_g)
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_base_v098_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = _z(s2, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of secondary metric (cash_g)
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_base_v099_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = _z(s2, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of secondary metric (cash_g)
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_base_v100_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    result = _z(s2, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative sum of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v101_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative sum of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v102_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d cumulative sum of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v103_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative sum of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v104_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d cumulative sum of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v105_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = m.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d drawdown of cumulative cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v106_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    cum = m.rolling(21, min_periods=10).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d drawdown of cumulative cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v107_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    cum = m.rolling(63, min_periods=31).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d drawdown of cumulative cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v108_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    cum = m.rolling(126, min_periods=63).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d drawdown of cumulative cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v109_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    cum = m.rolling(252, min_periods=126).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d drawdown of cumulative cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v110_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    cum = m.rolling(504, min_periods=252).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d conditional mean of cash to market cap (cashneq / marketcap) on rising days
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v111_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d conditional mean of cash to market cap (cashneq / marketcap) on rising days
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v112_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d conditional mean of cash to market cap (cashneq / marketcap) on rising days
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v113_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d conditional mean of cash to market cap (cashneq / marketcap) on rising days
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v114_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d conditional mean of cash to market cap (cashneq / marketcap) on rising days
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v115_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d conditional mean of cash to market cap (cashneq / marketcap) on falling days
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v116_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d conditional mean of cash to market cap (cashneq / marketcap) on falling days
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v117_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d conditional mean of cash to market cap (cashneq / marketcap) on falling days
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v118_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d conditional mean of cash to market cap (cashneq / marketcap) on falling days
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v119_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d conditional mean of cash to market cap (cashneq / marketcap) on falling days
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v120_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling corr of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v121_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(21, min_periods=10).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling corr of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v122_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(63, min_periods=31).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling corr of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v123_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(126, min_periods=63).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling corr of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v124_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(252, min_periods=126).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling corr of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v125_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(504, min_periods=252).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling cov of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v126_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(21, min_periods=10).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling cov of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v127_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(63, min_periods=31).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling cov of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v128_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(126, min_periods=63).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling cov of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v129_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(252, min_periods=126).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling cov of cash to market cap (cashneq / marketcap) vs closeadj return
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v130_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(504, min_periods=252).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-level demeaned of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v131_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-level demeaned of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v132_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-level demeaned of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v133_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-level demeaned of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v134_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-level demeaned of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v135_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(21) + z(63) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v136_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = _z(m, 21) + _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(63) + z(126) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v137_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = _z(m, 63) + _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(126) + z(252) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v138_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = _z(m, 126) + _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(252) + z(504) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v139_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = _z(m, 252) + _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(21) + z(252) of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v140_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = _z(m, 21) + _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d composite z * positivity hit-ratio of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_21d_base_v141_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(21, min_periods=10).mean()
    result = _z(m, 21) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 63d composite z * positivity hit-ratio of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v142_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(63, min_periods=31).mean()
    result = _z(m, 63) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 126d composite z * positivity hit-ratio of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v143_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _z(m, 126) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 252d composite z * positivity hit-ratio of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v144_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _z(m, 252) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 504d composite z * positivity hit-ratio of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_504d_base_v145_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _z(m, 504) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 63d composite: z(m,63) - z(s2,63) for cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v146_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    s2 = cashneq.pct_change(63)
    result = _z(m, 63) - _z(s2, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d composite: z(m,126) + z(s2,126) for cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_126d_base_v147_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    s2 = cashneq.pct_change(63)
    result = _z(m, 126) + _z(s2, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign(metric) * |s2| composite for cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v148_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    s2 = cashneq.pct_change(252)
    result = pd.Series(np.sign(m), index=m.index) * s2.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d regime divergence of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_63d_base_v149_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    short = np.sign(m.ewm(span=21, adjust=False).mean() - m.ewm(span=63, adjust=False).mean())
    long = np.sign(m.ewm(span=126, adjust=False).mean() - m.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=m.index)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trend-strength composite of cash to market cap (cashneq / marketcap)
def f69cm_f69_semi_cash_to_mcap_cm_252d_base_v150_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    result = _z(m, 63) + _z(m, 126) + _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)
