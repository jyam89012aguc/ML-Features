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
def _f12_gap(open_p, close_p):
    return open_p / close_p.shift(1) - 1.0


def _f12_gap_log(open_p, close_p):
    return np.log(open_p.replace(0, np.nan) / close_p.shift(1).replace(0, np.nan))


def _f12_intraday(open_p, close_p):
    return close_p / open_p - 1.0


def _f12_overnight_idx(open_p, close_p):
    g = open_p / close_p.shift(1) - 1.0
    return (1.0 + g).cumprod()


# 21d gap vs intraday return ratio
def f12og_f12_semi_overnight_gap_gapintraratio_21d_base_v076_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 21) / _mean(intra, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap vs intraday return ratio
def f12og_f12_semi_overnight_gap_gapintraratio_63d_base_v077_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 63) / _mean(intra, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap vs intraday return ratio
def f12og_f12_semi_overnight_gap_gapintraratio_126d_base_v078_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 126) / _mean(intra, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap vs intraday return ratio
def f12og_f12_semi_overnight_gap_gapintraratio_252d_base_v079_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 252) / _mean(intra, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap vs intraday return ratio
def f12og_f12_semi_overnight_gap_gapintraratio_504d_base_v080_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 504) / _mean(intra, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d overnight minus intraday return
def f12og_f12_semi_overnight_gap_ovniminusintra_21d_base_v081_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 21) - _mean(intra, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d overnight minus intraday return
def f12og_f12_semi_overnight_gap_ovniminusintra_63d_base_v082_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 63) - _mean(intra, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d overnight minus intraday return
def f12og_f12_semi_overnight_gap_ovniminusintra_126d_base_v083_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 126) - _mean(intra, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d overnight minus intraday return
def f12og_f12_semi_overnight_gap_ovniminusintra_252d_base_v084_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 252) - _mean(intra, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d overnight minus intraday return
def f12og_f12_semi_overnight_gap_ovniminusintra_504d_base_v085_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = _mean(g, 504) - _mean(intra, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorr of gap
def f12og_f12_semi_overnight_gap_gapac1_21d_base_v086_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(21, min_periods=10).corr(g.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorr of gap
def f12og_f12_semi_overnight_gap_gapac1_63d_base_v087_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(63, min_periods=31).corr(g.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorr of gap
def f12og_f12_semi_overnight_gap_gapac1_126d_base_v088_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(126, min_periods=63).corr(g.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorr of gap
def f12og_f12_semi_overnight_gap_gapac1_252d_base_v089_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(252, min_periods=126).corr(g.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorr of gap
def f12og_f12_semi_overnight_gap_gapac1_504d_base_v090_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(504, min_periods=252).corr(g.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr of gap with prev-day return
def f12og_f12_semi_overnight_gap_gapprevretcorr_21d_base_v091_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    r = closeadj.pct_change()
    result = g.rolling(21, min_periods=10).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr of gap with prev-day return
def f12og_f12_semi_overnight_gap_gapprevretcorr_63d_base_v092_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    r = closeadj.pct_change()
    result = g.rolling(63, min_periods=31).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr of gap with prev-day return
def f12og_f12_semi_overnight_gap_gapprevretcorr_126d_base_v093_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    r = closeadj.pct_change()
    result = g.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr of gap with prev-day return
def f12og_f12_semi_overnight_gap_gapprevretcorr_252d_base_v094_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    r = closeadj.pct_change()
    result = g.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr of gap with prev-day return
def f12og_f12_semi_overnight_gap_gapprevretcorr_504d_base_v095_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    r = closeadj.pct_change()
    result = g.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr of gap with same-day intraday
def f12og_f12_semi_overnight_gap_gapintracorr_21d_base_v096_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = g.rolling(21, min_periods=10).corr(intra)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr of gap with same-day intraday
def f12og_f12_semi_overnight_gap_gapintracorr_63d_base_v097_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = g.rolling(63, min_periods=31).corr(intra)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr of gap with same-day intraday
def f12og_f12_semi_overnight_gap_gapintracorr_126d_base_v098_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = g.rolling(126, min_periods=63).corr(intra)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr of gap with same-day intraday
def f12og_f12_semi_overnight_gap_gapintracorr_252d_base_v099_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = g.rolling(252, min_periods=126).corr(intra)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr of gap with same-day intraday
def f12og_f12_semi_overnight_gap_gapintracorr_504d_base_v100_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    result = g.rolling(504, min_periods=252).corr(intra)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of positive gaps only
def f12og_f12_semi_overnight_gap_meanposgap_21d_base_v101_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive gaps only
def f12og_f12_semi_overnight_gap_meanposgap_63d_base_v102_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of positive gaps only
def f12og_f12_semi_overnight_gap_meanposgap_126d_base_v103_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive gaps only
def f12og_f12_semi_overnight_gap_meanposgap_252d_base_v104_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of positive gaps only
def f12og_f12_semi_overnight_gap_meanposgap_504d_base_v105_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of negative gaps only
def f12og_f12_semi_overnight_gap_meanneggap_21d_base_v106_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative gaps only
def f12og_f12_semi_overnight_gap_meanneggap_63d_base_v107_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of negative gaps only
def f12og_f12_semi_overnight_gap_meanneggap_126d_base_v108_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative gaps only
def f12og_f12_semi_overnight_gap_meanneggap_252d_base_v109_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of negative gaps only
def f12og_f12_semi_overnight_gap_meanneggap_504d_base_v110_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g.where(g < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumdd_21d_base_v111_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(21, min_periods=11).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumdd_63d_base_v112_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumdd_126d_base_v113_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(126, min_periods=63).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumdd_252d_base_v114_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(252, min_periods=126).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumdd_504d_base_v115_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(504, min_periods=252).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumup_21d_base_v116_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(21, min_periods=11).sum()
    result = cum - _min(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumup_63d_base_v117_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    result = cum - _min(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumup_126d_base_v118_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(126, min_periods=63).sum()
    result = cum - _min(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumup_252d_base_v119_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(252, min_periods=126).sum()
    result = cum - _min(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of cumulative overnight return
def f12og_f12_semi_overnight_gap_ovncumup_504d_base_v120_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(504, min_periods=252).sum()
    result = cum - _min(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap-direction streak length
def f12og_f12_semi_overnight_gap_gapstreak_21d_base_v121_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    sign = (g > 0).astype(int) - (g < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(21, min_periods=11).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-direction streak length
def f12og_f12_semi_overnight_gap_gapstreak_63d_base_v122_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    sign = (g > 0).astype(int) - (g < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(63, min_periods=32).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap-direction streak length
def f12og_f12_semi_overnight_gap_gapstreak_126d_base_v123_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    sign = (g > 0).astype(int) - (g < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(126, min_periods=63).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap-direction streak length
def f12og_f12_semi_overnight_gap_gapstreak_252d_base_v124_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    sign = (g > 0).astype(int) - (g < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(252, min_periods=126).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap-direction streak length
def f12og_f12_semi_overnight_gap_gapstreak_504d_base_v125_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    sign = (g > 0).astype(int) - (g < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().abs()
    result = streak.rolling(504, min_periods=252).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap share of absolute total daily return
def f12og_f12_semi_overnight_gap_gapshare_21d_base_v126_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    result = _mean(num / den.replace(0, np.nan), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap share of absolute total daily return
def f12og_f12_semi_overnight_gap_gapshare_63d_base_v127_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    result = _mean(num / den.replace(0, np.nan), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap share of absolute total daily return
def f12og_f12_semi_overnight_gap_gapshare_126d_base_v128_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    result = _mean(num / den.replace(0, np.nan), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap share of absolute total daily return
def f12og_f12_semi_overnight_gap_gapshare_252d_base_v129_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    result = _mean(num / den.replace(0, np.nan), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap share of absolute total daily return
def f12og_f12_semi_overnight_gap_gapshare_504d_base_v130_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    result = _mean(num / den.replace(0, np.nan), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d info ratio of gap
def f12og_f12_semi_overnight_gap_gapir_21d_base_v131_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 21) / _std(g, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d info ratio of gap
def f12og_f12_semi_overnight_gap_gapir_63d_base_v132_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d info ratio of gap
def f12og_f12_semi_overnight_gap_gapir_126d_base_v133_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 126) / _std(g, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d info ratio of gap
def f12og_f12_semi_overnight_gap_gapir_252d_base_v134_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d info ratio of gap
def f12og_f12_semi_overnight_gap_gapir_504d_base_v135_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 504) / _std(g, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap EMA crossover 5v21
def f12og_f12_semi_overnight_gap_gapema_5v21_base_v136_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.ewm(span=5, adjust=False).mean() - g.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gap EMA crossover 21v63
def f12og_f12_semi_overnight_gap_gapema_21v63_base_v137_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.ewm(span=21, adjust=False).mean() - g.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gap EMA crossover 63v126
def f12og_f12_semi_overnight_gap_gapema_63v126_base_v138_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.ewm(span=63, adjust=False).mean() - g.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gap EMA crossover 126v252
def f12og_f12_semi_overnight_gap_gapema_126v252_base_v139_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.ewm(span=126, adjust=False).mean() - g.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gap EMA crossover 252v504
def f12og_f12_semi_overnight_gap_gapema_252v504_base_v140_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.ewm(span=252, adjust=False).mean() - g.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of cumulative gap
def f12og_f12_semi_overnight_gap_cumgapz_21d_base_v141_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(21, min_periods=11).sum()
    result = _z(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of cumulative gap
def f12og_f12_semi_overnight_gap_cumgapz_63d_base_v142_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    result = _z(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of cumulative gap
def f12og_f12_semi_overnight_gap_cumgapz_126d_base_v143_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(126, min_periods=63).sum()
    result = _z(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of cumulative gap
def f12og_f12_semi_overnight_gap_cumgapz_252d_base_v144_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(252, min_periods=126).sum()
    result = _z(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of cumulative gap
def f12og_f12_semi_overnight_gap_cumgapz_504d_base_v145_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(504, min_periods=252).sum()
    result = _z(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gap composite short (z21 + z63 + z126)
def f12og_f12_semi_overnight_gap_gapcompshort_63d_base_v146_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 21) + _z(g, 63) + _z(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gap composite long (z63 + z126 + z252)
def f12og_f12_semi_overnight_gap_gapcomplong_252d_base_v147_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 63) + _z(g, 126) + _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap regime divergence (short EMA cross vs long EMA cross)
def f12og_f12_semi_overnight_gap_gapregdiv_63d_base_v148_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    short = np.sign(g.ewm(span=21, adjust=False).mean() - g.ewm(span=63, adjust=False).mean())
    long = np.sign(g.ewm(span=126, adjust=False).mean() - g.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=g.index)
    return result.replace([np.inf, -np.inf], np.nan)


# gap quality 63d (IR x hit)
def f12og_f12_semi_overnight_gap_gapquality63_63d_base_v149_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    ir = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    hit = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# gap quality 252d (IR x hit)
def f12og_f12_semi_overnight_gap_gapquality252_252d_base_v150_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    ir = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    hit = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)
