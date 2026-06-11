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
def _f49ol_om_daily(oi, rev, idx):
    return (oi / rev.replace(0, np.nan)).reindex(idx).ffill()


def _f49ol_rev_daily(rev, idx):
    return rev.reindex(idx).ffill()


def _f49ol_oi_daily(oi, idx):
    return oi.reindex(idx).ffill()


def _f49ol_rev_yoy(rev):
    return rev.pct_change(4)


def _f49ol_rev_qoq(rev):
    return rev.pct_change(1)


def _f49ol_oi_yoy(oi):
    return oi.pct_change(4)


def _f49ol_oi_qoq(oi):
    return oi.pct_change(1)


def _f49ol_om_q_changes(om_daily):
    d = om_daily.diff()
    return d.where(d != 0).ffill()


def _f49ol_roll_beta(y, x, w):
    cov = y.rolling(w, min_periods=max(2, w // 2)).cov(x)
    var = x.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f49ol_roll_corr(y, x, w):
    return y.rolling(w, min_periods=max(2, w // 2)).corr(x)


# 21d rolling mean of |OM change at quarter boundaries|
def f49ol_f49_semi_operating_leverage_omabschg_21d_base_v076_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    result = _mean(omc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of |OM change|
def f49ol_f49_semi_operating_leverage_omabschg_63d_base_v077_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    result = _mean(omc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of |OM change|
def f49ol_f49_semi_operating_leverage_omabschg_126d_base_v078_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    result = _mean(omc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of |OM change|
def f49ol_f49_semi_operating_leverage_omabschg_252d_base_v079_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    result = _mean(omc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of |OM change|
def f49ol_f49_semi_operating_leverage_omabschg_504d_base_v080_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    result = _mean(omc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling sign run of OM changes (sum of signs)
def f49ol_f49_semi_operating_leverage_omsignrun_21d_base_v081_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    result = s.rolling(21, min_periods=max(2, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sign run of OM changes
def f49ol_f49_semi_operating_leverage_omsignrun_63d_base_v082_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    result = s.rolling(63, min_periods=max(2, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling sign run of OM changes
def f49ol_f49_semi_operating_leverage_omsignrun_126d_base_v083_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    result = s.rolling(126, min_periods=max(2, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sign run of OM changes
def f49ol_f49_semi_operating_leverage_omsignrun_252d_base_v084_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    result = s.rolling(252, min_periods=max(2, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sign run of OM changes
def f49ol_f49_semi_operating_leverage_omsignrun_504d_base_v085_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    result = s.rolling(504, min_periods=max(2, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling corr of OM and log(revenue)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_21d_base_v086_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    result = _f49ol_roll_corr(om, lr, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling corr of OM and log(revenue)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_63d_base_v087_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    result = _f49ol_roll_corr(om, lr, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling corr of OM and log(revenue)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_126d_base_v088_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    result = _f49ol_roll_corr(om, lr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling corr of OM and log(revenue)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_252d_base_v089_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    result = _f49ol_roll_corr(om, lr, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling corr of OM and log(revenue)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_504d_base_v090_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    result = _f49ol_roll_corr(om, lr, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating leverage beta times sign of YoY revenue growth (composite)
def f49ol_f49_semi_operating_leverage_oplevsign_21d_base_v091_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 21)
    result = b * np.sign(rg)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage beta times sign of revenue growth
def f49ol_f49_semi_operating_leverage_oplevsign_63d_base_v092_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 63)
    result = b * np.sign(rg)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d operating leverage beta times sign of revenue growth
def f49ol_f49_semi_operating_leverage_oplevsign_126d_base_v093_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 126)
    result = b * np.sign(rg)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage beta times sign of revenue growth
def f49ol_f49_semi_operating_leverage_oplevsign_252d_base_v094_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 252)
    result = b * np.sign(rg)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d operating leverage beta times sign of revenue growth
def f49ol_f49_semi_operating_leverage_oplevsign_504d_base_v095_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 504)
    result = b * np.sign(rg)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean level of OM
def f49ol_f49_semi_operating_leverage_omlevel_21d_base_v096_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _mean(om, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean level of OM
def f49ol_f49_semi_operating_leverage_omlevel_63d_base_v097_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _mean(om, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean level of OM
def f49ol_f49_semi_operating_leverage_omlevel_126d_base_v098_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _mean(om, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean level of OM
def f49ol_f49_semi_operating_leverage_omlevel_252d_base_v099_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _mean(om, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean level of OM
def f49ol_f49_semi_operating_leverage_omlevel_504d_base_v100_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _mean(om, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling std of OM
def f49ol_f49_semi_operating_leverage_omlevelstd_21d_base_v101_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _std(om, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of OM
def f49ol_f49_semi_operating_leverage_omlevelstd_63d_base_v102_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _std(om, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling std of OM
def f49ol_f49_semi_operating_leverage_omlevelstd_126d_base_v103_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _std(om, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of OM
def f49ol_f49_semi_operating_leverage_omlevelstd_252d_base_v104_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _std(om, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of OM
def f49ol_f49_semi_operating_leverage_omlevelstd_504d_base_v105_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _std(om, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling trend slope of OM via cov/var with time index
def f49ol_f49_semi_operating_leverage_omtrend_21d_base_v106_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(21, min_periods=max(2, 21 // 2)).cov(t)
    var = t.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling trend slope of OM
def f49ol_f49_semi_operating_leverage_omtrend_63d_base_v107_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(63, min_periods=max(2, 63 // 2)).cov(t)
    var = t.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling trend slope of OM
def f49ol_f49_semi_operating_leverage_omtrend_126d_base_v108_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(126, min_periods=max(2, 126 // 2)).cov(t)
    var = t.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling trend slope of OM
def f49ol_f49_semi_operating_leverage_omtrend_252d_base_v109_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(252, min_periods=max(2, 252 // 2)).cov(t)
    var = t.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling trend slope of OM
def f49ol_f49_semi_operating_leverage_omtrend_504d_base_v110_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(504, min_periods=max(2, 504 // 2)).cov(t)
    var = t.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta(OM on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoq_21d_base_v111_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta(OM on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoq_63d_base_v112_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta(OM on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoq_126d_base_v113_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta(OM on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoq_252d_base_v114_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta(OM on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoq_504d_base_v115_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of YoY revenue growth
def f49ol_f49_semi_operating_leverage_revgrowthz_21d_base_v116_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _z(rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of YoY revenue growth
def f49ol_f49_semi_operating_leverage_revgrowthz_63d_base_v117_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _z(rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of YoY revenue growth
def f49ol_f49_semi_operating_leverage_revgrowthz_126d_base_v118_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _z(rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of YoY revenue growth
def f49ol_f49_semi_operating_leverage_revgrowthz_252d_base_v119_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _z(rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of YoY revenue growth
def f49ol_f49_semi_operating_leverage_revgrowthz_504d_base_v120_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _z(rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of OM quarter-change series
def f49ol_f49_semi_operating_leverage_omgrowthz_21d_base_v121_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _z(omc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of OM quarter-change series
def f49ol_f49_semi_operating_leverage_omgrowthz_63d_base_v122_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _z(omc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of OM quarter-change series
def f49ol_f49_semi_operating_leverage_omgrowthz_126d_base_v123_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _z(omc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of OM quarter-change series
def f49ol_f49_semi_operating_leverage_omgrowthz_252d_base_v124_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _z(omc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of OM quarter-change series
def f49ol_f49_semi_operating_leverage_omgrowthz_504d_base_v125_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _z(omc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite: beta(OM on rev_yoy) times |rev growth|
def f49ol_f49_semi_operating_leverage_oplevcomp_21d_base_v126_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 21)
    result = b * rg.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: beta(OM on rev_yoy) times |rev growth|
def f49ol_f49_semi_operating_leverage_oplevcomp_63d_base_v127_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 63)
    result = b * rg.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite: beta(OM on rev_yoy) times |rev growth|
def f49ol_f49_semi_operating_leverage_oplevcomp_126d_base_v128_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 126)
    result = b * rg.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: beta(OM on rev_yoy) times |rev growth|
def f49ol_f49_semi_operating_leverage_oplevcomp_252d_base_v129_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 252)
    result = b * rg.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite: beta(OM on rev_yoy) times |rev growth|
def f49ol_f49_semi_operating_leverage_oplevcomp_504d_base_v130_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 504)
    result = b * rg.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta(QoQ opinc growth on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_21d_base_v131_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta(QoQ opinc growth on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_63d_base_v132_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta(QoQ opinc growth on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_126d_base_v133_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta(QoQ opinc growth on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_252d_base_v134_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta(QoQ opinc growth on QoQ revenue growth)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_504d_base_v135_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr of OM quarter-change and revenue YoY growth
def f49ol_f49_semi_operating_leverage_omchgrevcorr_21d_base_v136_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_corr(omc, rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr of OM quarter-change and revenue YoY growth
def f49ol_f49_semi_operating_leverage_omchgrevcorr_63d_base_v137_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_corr(omc, rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr of OM quarter-change and revenue YoY growth
def f49ol_f49_semi_operating_leverage_omchgrevcorr_126d_base_v138_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_corr(omc, rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr of OM quarter-change and revenue YoY growth
def f49ol_f49_semi_operating_leverage_omchgrevcorr_252d_base_v139_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_corr(omc, rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr of OM quarter-change and revenue YoY growth
def f49ol_f49_semi_operating_leverage_omchgrevcorr_504d_base_v140_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_corr(omc, rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d OM level times sign of revenue growth (regime-weighted OM)
def f49ol_f49_semi_operating_leverage_omxrevsign_21d_base_v141_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _mean(om * np.sign(rg), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d OM level times sign of revenue growth
def f49ol_f49_semi_operating_leverage_omxrevsign_63d_base_v142_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _mean(om * np.sign(rg), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d OM level times sign of revenue growth
def f49ol_f49_semi_operating_leverage_omxrevsign_126d_base_v143_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _mean(om * np.sign(rg), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OM level times sign of revenue growth
def f49ol_f49_semi_operating_leverage_omxrevsign_252d_base_v144_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _mean(om * np.sign(rg), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OM level times sign of revenue growth
def f49ol_f49_semi_operating_leverage_omxrevsign_504d_base_v145_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _mean(om * np.sign(rg), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew-proxy of OM quarter changes: (mean - median) / std
def f49ol_f49_semi_operating_leverage_omchgskew_21d_base_v146_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    mn = _mean(omc, 21)
    md = omc.rolling(21, min_periods=max(2, 21 // 2)).median()
    sd = _std(omc, 21)
    result = (mn - md) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew-proxy of OM quarter changes
def f49ol_f49_semi_operating_leverage_omchgskew_63d_base_v147_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    mn = _mean(omc, 63)
    md = omc.rolling(63, min_periods=max(2, 63 // 2)).median()
    sd = _std(omc, 63)
    result = (mn - md) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew-proxy of OM quarter changes
def f49ol_f49_semi_operating_leverage_omchgskew_126d_base_v148_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    mn = _mean(omc, 126)
    md = omc.rolling(126, min_periods=max(2, 126 // 2)).median()
    sd = _std(omc, 126)
    result = (mn - md) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew-proxy of OM quarter changes
def f49ol_f49_semi_operating_leverage_omchgskew_252d_base_v149_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    mn = _mean(omc, 252)
    md = omc.rolling(252, min_periods=max(2, 252 // 2)).median()
    sd = _std(omc, 252)
    result = (mn - md) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew-proxy of OM quarter changes
def f49ol_f49_semi_operating_leverage_omchgskew_504d_base_v150_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    mn = _mean(omc, 504)
    md = omc.rolling(504, min_periods=max(2, 504 // 2)).median()
    sd = _std(omc, 504)
    result = (mn - md) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
