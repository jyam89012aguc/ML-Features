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
def _f10_own_ret(s):
    return s.pct_change()


def _f10_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f10_streak_up(r):
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    return sign.groupby(grp).cumsum().where(sign > 0, 0.0)


def _f10_streak_dn(r):
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    return (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)


def _f10_autocorr(r, w, lag):
    return r.rolling(w, min_periods=max(2, w // 2)).corr(r.shift(lag))


# 21d Kaufman efficiency ratio
def f10mp_f10_semi_momentum_persistence_ker_21d_base_v076_signal(closeadj):
    num = (closeadj - closeadj.shift(21)).abs()
    den = closeadj.diff().abs().rolling(21, min_periods=11).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Kaufman efficiency ratio
def f10mp_f10_semi_momentum_persistence_ker_63d_base_v077_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Kaufman efficiency ratio
def f10mp_f10_semi_momentum_persistence_ker_126d_base_v078_signal(closeadj):
    num = (closeadj - closeadj.shift(126)).abs()
    den = closeadj.diff().abs().rolling(126, min_periods=63).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Kaufman efficiency ratio
def f10mp_f10_semi_momentum_persistence_ker_252d_base_v079_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Kaufman efficiency ratio
def f10mp_f10_semi_momentum_persistence_ker_504d_base_v080_signal(closeadj):
    num = (closeadj - closeadj.shift(504)).abs()
    den = closeadj.diff().abs().rolling(504, min_periods=252).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d half-life proxy (1 - lag-1 autocorr)
def f10mp_f10_semi_momentum_persistence_halflife_21d_base_v081_signal(closeadj):
    r = closeadj.pct_change()
    result = 1.0 - r.rolling(21, min_periods=10).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d half-life proxy (1 - lag-1 autocorr)
def f10mp_f10_semi_momentum_persistence_halflife_63d_base_v082_signal(closeadj):
    r = closeadj.pct_change()
    result = 1.0 - r.rolling(63, min_periods=31).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d half-life proxy (1 - lag-1 autocorr)
def f10mp_f10_semi_momentum_persistence_halflife_126d_base_v083_signal(closeadj):
    r = closeadj.pct_change()
    result = 1.0 - r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d half-life proxy (1 - lag-1 autocorr)
def f10mp_f10_semi_momentum_persistence_halflife_252d_base_v084_signal(closeadj):
    r = closeadj.pct_change()
    result = 1.0 - r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d half-life proxy (1 - lag-1 autocorr)
def f10mp_f10_semi_momentum_persistence_halflife_504d_base_v085_signal(closeadj):
    r = closeadj.pct_change()
    result = 1.0 - r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R/S proxy (range/std)
def f10mp_f10_semi_momentum_persistence_rsproxy_21d_base_v086_signal(closeadj):
    r = closeadj.pct_change()
    cum = r.rolling(21, min_periods=11).sum()
    rng = r.rolling(21, min_periods=11).max() - r.rolling(21, min_periods=11).min()
    sd = r.rolling(21, min_periods=11).std()
    result = rng / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d R/S proxy (range/std)
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_base_v087_signal(closeadj):
    r = closeadj.pct_change()
    cum = r.rolling(63, min_periods=32).sum()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    result = rng / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d R/S proxy (range/std)
def f10mp_f10_semi_momentum_persistence_rsproxy_126d_base_v088_signal(closeadj):
    r = closeadj.pct_change()
    cum = r.rolling(126, min_periods=63).sum()
    rng = r.rolling(126, min_periods=63).max() - r.rolling(126, min_periods=63).min()
    sd = r.rolling(126, min_periods=63).std()
    result = rng / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R/S proxy (range/std)
def f10mp_f10_semi_momentum_persistence_rsproxy_252d_base_v089_signal(closeadj):
    r = closeadj.pct_change()
    cum = r.rolling(252, min_periods=126).sum()
    rng = r.rolling(252, min_periods=126).max() - r.rolling(252, min_periods=126).min()
    sd = r.rolling(252, min_periods=126).std()
    result = rng / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R/S proxy (range/std)
def f10mp_f10_semi_momentum_persistence_rsproxy_504d_base_v090_signal(closeadj):
    r = closeadj.pct_change()
    cum = r.rolling(504, min_periods=252).sum()
    rng = r.rolling(504, min_periods=252).max() - r.rolling(504, min_periods=252).min()
    sd = r.rolling(504, min_periods=252).std()
    result = rng / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d trend strength (|mean|/std)
def f10mp_f10_semi_momentum_persistence_trendstrength_21d_base_v091_signal(closeadj):
    r = closeadj.pct_change()
    result = _mean(r, 21).abs() / _std(r, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d trend strength (|mean|/std)
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_base_v092_signal(closeadj):
    r = closeadj.pct_change()
    result = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d trend strength (|mean|/std)
def f10mp_f10_semi_momentum_persistence_trendstrength_126d_base_v093_signal(closeadj):
    r = closeadj.pct_change()
    result = _mean(r, 126).abs() / _std(r, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend strength (|mean|/std)
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_base_v094_signal(closeadj):
    r = closeadj.pct_change()
    result = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d trend strength (|mean|/std)
def f10mp_f10_semi_momentum_persistence_trendstrength_504d_base_v095_signal(closeadj):
    r = closeadj.pct_change()
    result = _mean(r, 504).abs() / _std(r, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnaround count (sign changes)
def f10mp_f10_semi_momentum_persistence_turnct_21d_base_v096_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    result = sc.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnaround count (sign changes)
def f10mp_f10_semi_momentum_persistence_turnct_63d_base_v097_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    result = sc.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d turnaround count (sign changes)
def f10mp_f10_semi_momentum_persistence_turnct_126d_base_v098_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    result = sc.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnaround count (sign changes)
def f10mp_f10_semi_momentum_persistence_turnct_252d_base_v099_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    result = sc.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d turnaround count (sign changes)
def f10mp_f10_semi_momentum_persistence_turnct_504d_base_v100_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    result = sc.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d persistence index (max streak / w)
def f10mp_f10_semi_momentum_persistence_persidx_21d_base_v101_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(21, min_periods=11).max() / 21
    return result.replace([np.inf, -np.inf], np.nan)


# 63d persistence index (max streak / w)
def f10mp_f10_semi_momentum_persistence_persidx_63d_base_v102_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(63, min_periods=32).max() / 63
    return result.replace([np.inf, -np.inf], np.nan)


# 126d persistence index (max streak / w)
def f10mp_f10_semi_momentum_persistence_persidx_126d_base_v103_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(126, min_periods=63).max() / 126
    return result.replace([np.inf, -np.inf], np.nan)


# 252d persistence index (max streak / w)
def f10mp_f10_semi_momentum_persistence_persidx_252d_base_v104_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(252, min_periods=126).max() / 252
    return result.replace([np.inf, -np.inf], np.nan)


# 504d persistence index (max streak / w)
def f10mp_f10_semi_momentum_persistence_persidx_504d_base_v105_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(504, min_periods=252).max() / 504
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of mean positive to mean negative return
def f10mp_f10_semi_momentum_persistence_posnegavg_21d_base_v106_signal(closeadj):
    r = closeadj.pct_change()
    posm = _mean(r.where(r > 0), 21)
    negm = _mean(r.where(r < 0), 21).abs()
    result = posm / negm.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of mean positive to mean negative return
def f10mp_f10_semi_momentum_persistence_posnegavg_63d_base_v107_signal(closeadj):
    r = closeadj.pct_change()
    posm = _mean(r.where(r > 0), 63)
    negm = _mean(r.where(r < 0), 63).abs()
    result = posm / negm.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of mean positive to mean negative return
def f10mp_f10_semi_momentum_persistence_posnegavg_126d_base_v108_signal(closeadj):
    r = closeadj.pct_change()
    posm = _mean(r.where(r > 0), 126)
    negm = _mean(r.where(r < 0), 126).abs()
    result = posm / negm.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of mean positive to mean negative return
def f10mp_f10_semi_momentum_persistence_posnegavg_252d_base_v109_signal(closeadj):
    r = closeadj.pct_change()
    posm = _mean(r.where(r > 0), 252)
    negm = _mean(r.where(r < 0), 252).abs()
    result = posm / negm.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of mean positive to mean negative return
def f10mp_f10_semi_momentum_persistence_posnegavg_504d_base_v110_signal(closeadj):
    r = closeadj.pct_change()
    posm = _mean(r.where(r > 0), 504)
    negm = _mean(r.where(r < 0), 504).abs()
    result = posm / negm.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of distinct up-runs
def f10mp_f10_semi_momentum_persistence_uprunct_21d_base_v111_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r > 0) & (r.shift(1) <= 0)).astype(float)
    result = trans.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of distinct up-runs
def f10mp_f10_semi_momentum_persistence_uprunct_63d_base_v112_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r > 0) & (r.shift(1) <= 0)).astype(float)
    result = trans.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of distinct up-runs
def f10mp_f10_semi_momentum_persistence_uprunct_126d_base_v113_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r > 0) & (r.shift(1) <= 0)).astype(float)
    result = trans.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of distinct up-runs
def f10mp_f10_semi_momentum_persistence_uprunct_252d_base_v114_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r > 0) & (r.shift(1) <= 0)).astype(float)
    result = trans.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of distinct up-runs
def f10mp_f10_semi_momentum_persistence_uprunct_504d_base_v115_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r > 0) & (r.shift(1) <= 0)).astype(float)
    result = trans.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of distinct down-runs
def f10mp_f10_semi_momentum_persistence_dnrunct_21d_base_v116_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r < 0) & (r.shift(1) >= 0)).astype(float)
    result = trans.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of distinct down-runs
def f10mp_f10_semi_momentum_persistence_dnrunct_63d_base_v117_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r < 0) & (r.shift(1) >= 0)).astype(float)
    result = trans.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of distinct down-runs
def f10mp_f10_semi_momentum_persistence_dnrunct_126d_base_v118_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r < 0) & (r.shift(1) >= 0)).astype(float)
    result = trans.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of distinct down-runs
def f10mp_f10_semi_momentum_persistence_dnrunct_252d_base_v119_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r < 0) & (r.shift(1) >= 0)).astype(float)
    result = trans.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of distinct down-runs
def f10mp_f10_semi_momentum_persistence_dnrunct_504d_base_v120_signal(closeadj):
    r = closeadj.pct_change()
    trans = ((r < 0) & (r.shift(1) >= 0)).astype(float)
    result = trans.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d average run length
def f10mp_f10_semi_momentum_persistence_avgrunlen_21d_base_v121_signal(closeadj):
    r = closeadj.pct_change()
    tu = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(21, min_periods=11).sum()
    td = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(21, min_periods=11).sum()
    result = 21 / (tu + td).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d average run length
def f10mp_f10_semi_momentum_persistence_avgrunlen_63d_base_v122_signal(closeadj):
    r = closeadj.pct_change()
    tu = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(63, min_periods=32).sum()
    td = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(63, min_periods=32).sum()
    result = 63 / (tu + td).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d average run length
def f10mp_f10_semi_momentum_persistence_avgrunlen_126d_base_v123_signal(closeadj):
    r = closeadj.pct_change()
    tu = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(126, min_periods=63).sum()
    td = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(126, min_periods=63).sum()
    result = 126 / (tu + td).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d average run length
def f10mp_f10_semi_momentum_persistence_avgrunlen_252d_base_v124_signal(closeadj):
    r = closeadj.pct_change()
    tu = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(252, min_periods=126).sum()
    td = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(252, min_periods=126).sum()
    result = 252 / (tu + td).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d average run length
def f10mp_f10_semi_momentum_persistence_avgrunlen_504d_base_v125_signal(closeadj):
    r = closeadj.pct_change()
    tu = ((r > 0) & (r.shift(1) <= 0)).astype(float).rolling(504, min_periods=252).sum()
    td = ((r < 0) & (r.shift(1) >= 0)).astype(float).rolling(504, min_periods=252).sum()
    result = 504 / (tu + td).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d serial covariance of returns
def f10mp_f10_semi_momentum_persistence_serialcov_21d_base_v126_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(21, min_periods=10).cov(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d serial covariance of returns
def f10mp_f10_semi_momentum_persistence_serialcov_63d_base_v127_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=31).cov(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d serial covariance of returns
def f10mp_f10_semi_momentum_persistence_serialcov_126d_base_v128_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=63).cov(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d serial covariance of returns
def f10mp_f10_semi_momentum_persistence_serialcov_252d_base_v129_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(252, min_periods=126).cov(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d serial covariance of returns
def f10mp_f10_semi_momentum_persistence_serialcov_504d_base_v130_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(504, min_periods=252).cov(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of (EMA21 - EMA63)
def f10mp_f10_semi_momentum_persistence_emaspreadz_21d_base_v131_signal(closeadj):
    r = closeadj.pct_change()
    sp = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _z(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of (EMA21 - EMA63)
def f10mp_f10_semi_momentum_persistence_emaspreadz_63d_base_v132_signal(closeadj):
    r = closeadj.pct_change()
    sp = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _z(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of (EMA63 - EMA126)
def f10mp_f10_semi_momentum_persistence_emaspreadz_126d_base_v133_signal(closeadj):
    r = closeadj.pct_change()
    sp = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _z(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of (EMA126 - EMA252)
def f10mp_f10_semi_momentum_persistence_emaspreadz_252d_base_v134_signal(closeadj):
    r = closeadj.pct_change()
    sp = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    result = _z(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of (EMA252 - EMA504)
def f10mp_f10_semi_momentum_persistence_emaspreadz_504d_base_v135_signal(closeadj):
    r = closeadj.pct_change()
    sp = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    result = _z(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sum of lag1+lag5+lag21 autocorr
def f10mp_f10_semi_momentum_persistence_accomp_21d_base_v136_signal(closeadj):
    r = closeadj.pct_change()
    a1 = r.rolling(21, min_periods=10).corr(r.shift(1))
    a5 = r.rolling(21, min_periods=10).corr(r.shift(5))
    a21 = r.rolling(21, min_periods=10).corr(r.shift(21))
    result = a1 + a5 + a21
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of lag1+lag5+lag21 autocorr
def f10mp_f10_semi_momentum_persistence_accomp_63d_base_v137_signal(closeadj):
    r = closeadj.pct_change()
    a1 = r.rolling(63, min_periods=31).corr(r.shift(1))
    a5 = r.rolling(63, min_periods=31).corr(r.shift(5))
    a21 = r.rolling(63, min_periods=31).corr(r.shift(21))
    result = a1 + a5 + a21
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sum of lag1+lag5+lag21 autocorr
def f10mp_f10_semi_momentum_persistence_accomp_126d_base_v138_signal(closeadj):
    r = closeadj.pct_change()
    a1 = r.rolling(126, min_periods=63).corr(r.shift(1))
    a5 = r.rolling(126, min_periods=63).corr(r.shift(5))
    a21 = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = a1 + a5 + a21
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of lag1+lag5+lag21 autocorr
def f10mp_f10_semi_momentum_persistence_accomp_252d_base_v139_signal(closeadj):
    r = closeadj.pct_change()
    a1 = r.rolling(252, min_periods=126).corr(r.shift(1))
    a5 = r.rolling(252, min_periods=126).corr(r.shift(5))
    a21 = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = a1 + a5 + a21
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of lag1+lag5+lag21 autocorr
def f10mp_f10_semi_momentum_persistence_accomp_504d_base_v140_signal(closeadj):
    r = closeadj.pct_change()
    a1 = r.rolling(504, min_periods=252).corr(r.shift(1))
    a5 = r.rolling(504, min_periods=252).corr(r.shift(5))
    a21 = r.rolling(504, min_periods=252).corr(r.shift(21))
    result = a1 + a5 + a21
    return result.replace([np.inf, -np.inf], np.nan)


# 21d second-half vs first-half return mean delta
def f10mp_f10_semi_momentum_persistence_hhdelta_21d_base_v141_signal(closeadj):
    r = closeadj.pct_change()
    first = r.rolling(10, min_periods=max(1, 10 // 2)).mean().shift(10)
    second = r.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = second - first
    return result.replace([np.inf, -np.inf], np.nan)


# 63d second-half vs first-half return mean delta
def f10mp_f10_semi_momentum_persistence_hhdelta_63d_base_v142_signal(closeadj):
    r = closeadj.pct_change()
    first = r.rolling(31, min_periods=max(1, 31 // 2)).mean().shift(31)
    second = r.rolling(31, min_periods=max(1, 31 // 2)).mean()
    result = second - first
    return result.replace([np.inf, -np.inf], np.nan)


# 126d second-half vs first-half return mean delta
def f10mp_f10_semi_momentum_persistence_hhdelta_126d_base_v143_signal(closeadj):
    r = closeadj.pct_change()
    first = r.rolling(63, min_periods=max(1, 63 // 2)).mean().shift(63)
    second = r.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = second - first
    return result.replace([np.inf, -np.inf], np.nan)


# 252d second-half vs first-half return mean delta
def f10mp_f10_semi_momentum_persistence_hhdelta_252d_base_v144_signal(closeadj):
    r = closeadj.pct_change()
    first = r.rolling(126, min_periods=max(1, 126 // 2)).mean().shift(126)
    second = r.rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = second - first
    return result.replace([np.inf, -np.inf], np.nan)


# 504d second-half vs first-half return mean delta
def f10mp_f10_semi_momentum_persistence_hhdelta_504d_base_v145_signal(closeadj):
    r = closeadj.pct_change()
    first = r.rolling(252, min_periods=max(1, 252 // 2)).mean().shift(252)
    second = r.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = second - first
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed trend efficiency
def f10mp_f10_semi_momentum_persistence_signedeff_21d_base_v146_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 21)
    sd = _std(r, 21)
    result = pd.Series(np.sign(m), index=m.index) * (m.abs() / sd.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed trend efficiency
def f10mp_f10_semi_momentum_persistence_signedeff_63d_base_v147_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 63)
    sd = _std(r, 63)
    result = pd.Series(np.sign(m), index=m.index) * (m.abs() / sd.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed trend efficiency
def f10mp_f10_semi_momentum_persistence_signedeff_126d_base_v148_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 126)
    sd = _std(r, 126)
    result = pd.Series(np.sign(m), index=m.index) * (m.abs() / sd.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed trend efficiency
def f10mp_f10_semi_momentum_persistence_signedeff_252d_base_v149_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 252)
    sd = _std(r, 252)
    result = pd.Series(np.sign(m), index=m.index) * (m.abs() / sd.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed trend efficiency
def f10mp_f10_semi_momentum_persistence_signedeff_504d_base_v150_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 504)
    sd = _std(r, 504)
    result = pd.Series(np.sign(m), index=m.index) * (m.abs() / sd.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)
