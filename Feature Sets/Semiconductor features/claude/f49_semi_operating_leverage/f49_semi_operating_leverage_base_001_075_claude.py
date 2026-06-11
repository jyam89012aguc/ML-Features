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
def _f49ol_om(oi, rev):
    return oi / rev.replace(0, np.nan)


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


def _f49ol_q_growth_daily(g_q, idx):
    g = g_q.reindex(idx).ffill()
    d = g.diff()
    return g.where(d != 0).ffill()


def _f49ol_roll_beta(y, x, w):
    cov = y.rolling(w, min_periods=max(2, w // 2)).cov(x)
    var = x.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f49ol_roll_corr(y, x, w):
    return y.rolling(w, min_periods=max(2, w // 2)).corr(x)


def _f49ol_roll_cov(y, x, w):
    return y.rolling(w, min_periods=max(2, w // 2)).cov(x)


# 21d rolling correlation of OM and revenue (Pattern C)
def f49ol_f49_semi_operating_leverage_omcorr_21d_base_v001_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    result = _f49ol_roll_corr(om, rev, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of OM and revenue
def f49ol_f49_semi_operating_leverage_omcorr_63d_base_v002_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    result = _f49ol_roll_corr(om, rev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of OM and revenue
def f49ol_f49_semi_operating_leverage_omcorr_126d_base_v003_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    result = _f49ol_roll_corr(om, rev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of OM and revenue
def f49ol_f49_semi_operating_leverage_omcorr_252d_base_v004_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    result = _f49ol_roll_corr(om, rev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of OM and revenue
def f49ol_f49_semi_operating_leverage_omcorr_504d_base_v005_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    result = _f49ol_roll_corr(om, rev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta of OM on YoY revenue growth (Pattern B)
def f49ol_f49_semi_operating_leverage_oplevbeta_21d_base_v006_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta of OM on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevbeta_63d_base_v007_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta of OM on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevbeta_126d_base_v008_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta of OM on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevbeta_252d_base_v009_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta of OM on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevbeta_504d_base_v010_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(om, rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling covariance of OM and YoY revenue growth
def f49ol_f49_semi_operating_leverage_omrevcov_21d_base_v011_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_cov(om, rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling covariance of OM and YoY revenue growth
def f49ol_f49_semi_operating_leverage_omrevcov_63d_base_v012_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_cov(om, rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling covariance of OM and YoY revenue growth
def f49ol_f49_semi_operating_leverage_omrevcov_126d_base_v013_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_cov(om, rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling covariance of OM and YoY revenue growth
def f49ol_f49_semi_operating_leverage_omrevcov_252d_base_v014_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_cov(om, rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling covariance of OM and YoY revenue growth
def f49ol_f49_semi_operating_leverage_omrevcov_504d_base_v015_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_cov(om, rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta of YoY opinc growth on YoY revenue growth (true DOL)
def f49ol_f49_semi_operating_leverage_oplevoigrev_21d_base_v016_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta of YoY opinc growth on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevoigrev_63d_base_v017_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta of YoY opinc growth on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevoigrev_126d_base_v018_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta of YoY opinc growth on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevoigrev_252d_base_v019_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta of YoY opinc growth on YoY revenue growth
def f49ol_f49_semi_operating_leverage_oplevoigrev_504d_base_v020_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    result = _f49ol_roll_beta(og, rg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of quarter-boundary OM changes (Pattern A)
def f49ol_f49_semi_operating_leverage_omchgmean_21d_base_v021_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _mean(omc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgmean_63d_base_v022_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _mean(omc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgmean_126d_base_v023_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _mean(omc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgmean_252d_base_v024_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _mean(omc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgmean_504d_base_v025_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _mean(omc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling std of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgstd_21d_base_v026_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _std(omc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgstd_63d_base_v027_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _std(omc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling std of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgstd_126d_base_v028_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _std(omc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgstd_252d_base_v029_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _std(omc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of quarter-boundary OM changes
def f49ol_f49_semi_operating_leverage_omchgstd_504d_base_v030_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    result = _std(omc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of OM vs its rolling mean/std
def f49ol_f49_semi_operating_leverage_omz_21d_base_v031_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _z(om, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of OM
def f49ol_f49_semi_operating_leverage_omz_63d_base_v032_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _z(om, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of OM
def f49ol_f49_semi_operating_leverage_omz_126d_base_v033_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _z(om, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of OM
def f49ol_f49_semi_operating_leverage_omz_252d_base_v034_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _z(om, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of OM
def f49ol_f49_semi_operating_leverage_omz_504d_base_v035_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _z(om, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of OM from rolling peak
def f49ol_f49_semi_operating_leverage_omdd_21d_base_v036_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _max(om, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of OM from rolling peak
def f49ol_f49_semi_operating_leverage_omdd_63d_base_v037_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _max(om, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of OM from rolling peak
def f49ol_f49_semi_operating_leverage_omdd_126d_base_v038_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _max(om, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of OM from rolling peak
def f49ol_f49_semi_operating_leverage_omdd_252d_base_v039_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _max(om, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of OM from rolling peak
def f49ol_f49_semi_operating_leverage_omdd_504d_base_v040_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _max(om, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of OM above rolling trough
def f49ol_f49_semi_operating_leverage_omrun_21d_base_v041_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _min(om, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of OM above rolling trough
def f49ol_f49_semi_operating_leverage_omrun_63d_base_v042_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _min(om, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of OM above rolling trough
def f49ol_f49_semi_operating_leverage_omrun_126d_base_v043_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _min(om, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of OM above rolling trough
def f49ol_f49_semi_operating_leverage_omrun_252d_base_v044_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _min(om, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of OM above rolling trough
def f49ol_f49_semi_operating_leverage_omrun_504d_base_v045_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om - _min(om, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling range (max - min) of OM
def f49ol_f49_semi_operating_leverage_omrange_21d_base_v046_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _max(om, 21) - _min(om, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of OM
def f49ol_f49_semi_operating_leverage_omrange_63d_base_v047_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _max(om, 63) - _min(om, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling range of OM
def f49ol_f49_semi_operating_leverage_omrange_126d_base_v048_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _max(om, 126) - _min(om, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of OM
def f49ol_f49_semi_operating_leverage_omrange_252d_base_v049_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _max(om, 252) - _min(om, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of OM
def f49ol_f49_semi_operating_leverage_omrange_504d_base_v050_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = _max(om, 504) - _min(om, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of OM changes only when revenue growth > 0
def f49ol_f49_semi_operating_leverage_omchgposup_21d_base_v051_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    result = _mean(omc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of OM changes only when revenue growth > 0
def f49ol_f49_semi_operating_leverage_omchgposup_63d_base_v052_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    result = _mean(omc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of OM changes only when revenue growth > 0
def f49ol_f49_semi_operating_leverage_omchgposup_126d_base_v053_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    result = _mean(omc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of OM changes only when revenue growth > 0
def f49ol_f49_semi_operating_leverage_omchgposup_252d_base_v054_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    result = _mean(omc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of OM changes only when revenue growth > 0
def f49ol_f49_semi_operating_leverage_omchgposup_504d_base_v055_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    result = _mean(omc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of OM changes only when revenue growth < 0
def f49ol_f49_semi_operating_leverage_omchgnegdn_21d_base_v056_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg < 0)
    result = _mean(omc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of OM changes only when revenue growth < 0
def f49ol_f49_semi_operating_leverage_omchgnegdn_63d_base_v057_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg < 0)
    result = _mean(omc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of OM changes only when revenue growth < 0
def f49ol_f49_semi_operating_leverage_omchgnegdn_126d_base_v058_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg < 0)
    result = _mean(omc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of OM changes only when revenue growth < 0
def f49ol_f49_semi_operating_leverage_omchgnegdn_252d_base_v059_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg < 0)
    result = _mean(omc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of OM changes only when revenue growth < 0
def f49ol_f49_semi_operating_leverage_omchgnegdn_504d_base_v060_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg < 0)
    result = _mean(omc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asymmetric operating leverage: up-quarter OM chg minus down-quarter OM chg
def f49ol_f49_semi_operating_leverage_omchgasym_21d_base_v061_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 21)
    dn = _mean(omc.where(rg < 0), 21)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asymmetric operating leverage
def f49ol_f49_semi_operating_leverage_omchgasym_63d_base_v062_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 63)
    dn = _mean(omc.where(rg < 0), 63)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# 126d asymmetric operating leverage
def f49ol_f49_semi_operating_leverage_omchgasym_126d_base_v063_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 126)
    dn = _mean(omc.where(rg < 0), 126)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asymmetric operating leverage
def f49ol_f49_semi_operating_leverage_omchgasym_252d_base_v064_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 252)
    dn = _mean(omc.where(rg < 0), 252)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# 504d asymmetric operating leverage
def f49ol_f49_semi_operating_leverage_omchgasym_504d_base_v065_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 504)
    dn = _mean(omc.where(rg < 0), 504)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA crossover on OM (5d vs 21d)
def f49ol_f49_semi_operating_leverage_omema_5v21_base_v066_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om.ewm(span=5, adjust=False).mean() - om.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 63d EMA crossover on OM
def f49ol_f49_semi_operating_leverage_omema_21v63_base_v067_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om.ewm(span=21, adjust=False).mean() - om.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 126d EMA crossover on OM
def f49ol_f49_semi_operating_leverage_omema_63v126_base_v068_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om.ewm(span=63, adjust=False).mean() - om.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 252d EMA crossover on OM
def f49ol_f49_semi_operating_leverage_omema_126v252_base_v069_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om.ewm(span=126, adjust=False).mean() - om.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vs 504d EMA crossover on OM
def f49ol_f49_semi_operating_leverage_omema_252v504_base_v070_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    result = om.ewm(span=252, adjust=False).mean() - om.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of smoothed OM as pct change of rolling mean
def f49ol_f49_semi_operating_leverage_omslope_21d_base_v071_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 21)
    result = smooth.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of smoothed OM
def f49ol_f49_semi_operating_leverage_omslope_63d_base_v072_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 63)
    result = smooth.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of smoothed OM
def f49ol_f49_semi_operating_leverage_omslope_126d_base_v073_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 126)
    result = smooth.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of smoothed OM
def f49ol_f49_semi_operating_leverage_omslope_252d_base_v074_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 252)
    result = smooth.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of smoothed OM
def f49ol_f49_semi_operating_leverage_omslope_504d_base_v075_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 504)
    result = smooth.pct_change(504)
    return result.replace([np.inf, -np.inf], np.nan)
