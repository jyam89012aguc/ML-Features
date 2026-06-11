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
def _f70_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f70_safe_pct(x, n):
    return x.pct_change(n)


def _f70_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f70_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 21d percent-change of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v076_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d percent-change of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v077_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d percent-change of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v078_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d percent-change of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v079_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d percent-change of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v080_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.pct_change(504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level-change (diff) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v081_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level-change (diff) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v082_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level-change (diff) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v083_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level-change (diff) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v084_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level-change (diff) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v085_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.diff(504)
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 5/21 - 1 of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_5d_base_v086_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    fastm = m.ewm(span=5, adjust=False).mean()
    slowm = m.ewm(span=21, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 21/63 - 1 of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v087_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    fastm = m.ewm(span=21, adjust=False).mean()
    slowm = m.ewm(span=63, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 63/126 - 1 of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v088_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    fastm = m.ewm(span=63, adjust=False).mean()
    slowm = m.ewm(span=126, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 126/252 - 1 of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v089_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    fastm = m.ewm(span=126, adjust=False).mean()
    slowm = m.ewm(span=252, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# EMA ratio 252/504 - 1 of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v090_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    fastm = m.ewm(span=252, adjust=False).mean()
    slowm = m.ewm(span=504, adjust=False).mean()
    result = fastm / slowm.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# 21d secondary metric (ni_oc) demeaned
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_base_v091_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = s2 - _mean(s2, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d secondary metric (ni_oc) demeaned
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_base_v092_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = s2 - _mean(s2, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d secondary metric (ni_oc) demeaned
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_base_v093_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = s2 - _mean(s2, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d secondary metric (ni_oc) demeaned
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_base_v094_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = s2 - _mean(s2, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d secondary metric (ni_oc) demeaned
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_base_v095_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = s2 - _mean(s2, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of secondary metric (ni_oc)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_base_v096_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = _z(s2, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of secondary metric (ni_oc)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_base_v097_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = _z(s2, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of secondary metric (ni_oc)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_base_v098_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = _z(s2, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of secondary metric (ni_oc)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_base_v099_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = _z(s2, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of secondary metric (ni_oc)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_base_v100_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    result = _z(s2, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative sum of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v101_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative sum of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v102_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d cumulative sum of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v103_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative sum of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v104_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d cumulative sum of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v105_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = m.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d drawdown of cumulative earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v106_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    cum = m.rolling(21, min_periods=10).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d drawdown of cumulative earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v107_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    cum = m.rolling(63, min_periods=31).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d drawdown of cumulative earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v108_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    cum = m.rolling(126, min_periods=63).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d drawdown of cumulative earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v109_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    cum = m.rolling(252, min_periods=126).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d drawdown of cumulative earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v110_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    cum = m.rolling(504, min_periods=252).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on rising days
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v111_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on rising days
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v112_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on rising days
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v113_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on rising days
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v114_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on rising days
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v115_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on falling days
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v116_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on falling days
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v117_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on falling days
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v118_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on falling days
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v119_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d conditional mean of earnings quality / accruals ((netinc - ocf) / assets) on falling days
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v120_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    d = m.diff()
    result = _mean(m.where(d < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling corr of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v121_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(21, min_periods=10).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling corr of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v122_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(63, min_periods=31).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling corr of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v123_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(126, min_periods=63).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling corr of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v124_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(252, min_periods=126).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling corr of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v125_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(504, min_periods=252).corr(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling cov of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v126_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(21, min_periods=10).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling cov of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v127_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(63, min_periods=31).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling cov of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v128_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(126, min_periods=63).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling cov of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v129_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(252, min_periods=126).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling cov of earnings quality / accruals ((netinc - ocf) / assets) vs closeadj return
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v130_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    px = closeadj.pct_change()
    result = m.rolling(504, min_periods=252).cov(px)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-level demeaned of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v131_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-level demeaned of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v132_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-level demeaned of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v133_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-level demeaned of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v134_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-level demeaned of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v135_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    lg = np.log(m.replace(0, np.nan).abs())
    result = lg - _mean(lg, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(21) + z(63) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v136_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = _z(m, 21) + _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(63) + z(126) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v137_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = _z(m, 63) + _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(126) + z(252) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v138_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = _z(m, 126) + _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(252) + z(504) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v139_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = _z(m, 252) + _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# composite z(21) + z(252) of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v140_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = _z(m, 21) + _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d composite z * positivity hit-ratio of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_base_v141_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(21, min_periods=10).mean()
    result = _z(m, 21) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 63d composite z * positivity hit-ratio of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v142_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(63, min_periods=31).mean()
    result = _z(m, 63) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 126d composite z * positivity hit-ratio of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v143_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _z(m, 126) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 252d composite z * positivity hit-ratio of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v144_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _z(m, 252) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 504d composite z * positivity hit-ratio of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_base_v145_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    hit = (m > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _z(m, 504) * hit
    return result.replace([np.inf, -np.inf], np.nan)

# 63d composite: z(m,63) - z(s2,63) for earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v146_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    s2 = (netinc - ocf)
    result = _z(m, 63) - _z(s2, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d composite: z(m,126) + z(s2,126) for earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_base_v147_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    s2 = (netinc - ocf)
    result = _z(m, 126) + _z(s2, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign(metric) * |s2| composite for earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v148_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    s2 = (netinc - ocf)
    result = pd.Series(np.sign(m), index=m.index) * s2.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d regime divergence of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_base_v149_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    short = np.sign(m.ewm(span=21, adjust=False).mean() - m.ewm(span=63, adjust=False).mean())
    long = np.sign(m.ewm(span=126, adjust=False).mean() - m.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=m.index)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trend-strength composite of earnings quality / accruals ((netinc - ocf) / assets)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_base_v150_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    result = _z(m, 63) + _z(m, 126) + _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)
