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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


# ===== folder domain primitives =====
def _f49ol_om_daily(oi, rev, idx):
    return (oi / rev.replace(0, np.nan)).reindex(idx).ffill()


def _f49ol_rev_daily(rev, idx):
    return rev.reindex(idx).ffill()


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


def _f49ol_roll_cov(y, x, w):
    return y.rolling(w, min_periods=max(2, w // 2)).cov(x)


# 21d slope of rolling corr(OM, revenue) (21d window)
def f49ol_f49_semi_operating_leverage_omcorr_21d_slope_v001_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    base = _f49ol_roll_corr(om, rev, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling corr(OM, revenue) (63d window)
def f49ol_f49_semi_operating_leverage_omcorr_63d_slope_v002_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    base = _f49ol_roll_corr(om, rev, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling corr(OM, revenue) (126d window)
def f49ol_f49_semi_operating_leverage_omcorr_126d_slope_v003_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    base = _f49ol_roll_corr(om, rev, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling corr(OM, revenue) (252d window)
def f49ol_f49_semi_operating_leverage_omcorr_252d_slope_v004_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    base = _f49ol_roll_corr(om, rev, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling corr(OM, revenue) (504d window)
def f49ol_f49_semi_operating_leverage_omcorr_504d_slope_v005_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rev = _f49ol_rev_daily(revenue, closeadj.index)
    base = _f49ol_roll_corr(om, rev, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling beta(OM on YoY rev growth) (21d window)
def f49ol_f49_semi_operating_leverage_oplevbeta_21d_slope_v006_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling beta(OM on YoY rev growth) (63d window)
def f49ol_f49_semi_operating_leverage_oplevbeta_63d_slope_v007_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling beta(OM on YoY rev growth) (126d window)
def f49ol_f49_semi_operating_leverage_oplevbeta_126d_slope_v008_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling beta(OM on YoY rev growth) (252d window)
def f49ol_f49_semi_operating_leverage_oplevbeta_252d_slope_v009_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling beta(OM on YoY rev growth) (504d window)
def f49ol_f49_semi_operating_leverage_oplevbeta_504d_slope_v010_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling cov(OM, YoY rev growth) (21d window)
def f49ol_f49_semi_operating_leverage_omrevcov_21d_slope_v011_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_cov(om, rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling cov(OM, YoY rev growth) (63d window)
def f49ol_f49_semi_operating_leverage_omrevcov_63d_slope_v012_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_cov(om, rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling cov(OM, YoY rev growth) (126d window)
def f49ol_f49_semi_operating_leverage_omrevcov_126d_slope_v013_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_cov(om, rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling cov(OM, YoY rev growth) (252d window)
def f49ol_f49_semi_operating_leverage_omrevcov_252d_slope_v014_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_cov(om, rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling cov(OM, YoY rev growth) (504d window)
def f49ol_f49_semi_operating_leverage_omrevcov_504d_slope_v015_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_cov(om, rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling beta(opinc_yoy on rev_yoy) (21d window)
def f49ol_f49_semi_operating_leverage_oplevoigrev_21d_slope_v016_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling beta(opinc_yoy on rev_yoy) (63d window)
def f49ol_f49_semi_operating_leverage_oplevoigrev_63d_slope_v017_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling beta(opinc_yoy on rev_yoy) (126d window)
def f49ol_f49_semi_operating_leverage_oplevoigrev_126d_slope_v018_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling beta(opinc_yoy on rev_yoy) (252d window)
def f49ol_f49_semi_operating_leverage_oplevoigrev_252d_slope_v019_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling beta(opinc_yoy on rev_yoy) (504d window)
def f49ol_f49_semi_operating_leverage_oplevoigrev_504d_slope_v020_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling mean of quarter-boundary OM changes (21d window)
def f49ol_f49_semi_operating_leverage_omchgmean_21d_slope_v021_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _mean(omc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling mean of quarter-boundary OM changes (63d window)
def f49ol_f49_semi_operating_leverage_omchgmean_63d_slope_v022_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _mean(omc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling mean of quarter-boundary OM changes (126d window)
def f49ol_f49_semi_operating_leverage_omchgmean_126d_slope_v023_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _mean(omc, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling mean of quarter-boundary OM changes (252d window)
def f49ol_f49_semi_operating_leverage_omchgmean_252d_slope_v024_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _mean(omc, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling mean of quarter-boundary OM changes (504d window)
def f49ol_f49_semi_operating_leverage_omchgmean_504d_slope_v025_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _mean(omc, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling std of quarter-boundary OM changes (21d window)
def f49ol_f49_semi_operating_leverage_omchgstd_21d_slope_v026_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _std(omc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling std of quarter-boundary OM changes (63d window)
def f49ol_f49_semi_operating_leverage_omchgstd_63d_slope_v027_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _std(omc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling std of quarter-boundary OM changes (126d window)
def f49ol_f49_semi_operating_leverage_omchgstd_126d_slope_v028_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _std(omc, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling std of quarter-boundary OM changes (252d window)
def f49ol_f49_semi_operating_leverage_omchgstd_252d_slope_v029_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _std(omc, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling std of quarter-boundary OM changes (504d window)
def f49ol_f49_semi_operating_leverage_omchgstd_504d_slope_v030_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _std(omc, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of z-score of OM (21d window)
def f49ol_f49_semi_operating_leverage_omz_21d_slope_v031_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _z(om, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of z-score of OM (63d window)
def f49ol_f49_semi_operating_leverage_omz_63d_slope_v032_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _z(om, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of z-score of OM (126d window)
def f49ol_f49_semi_operating_leverage_omz_126d_slope_v033_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _z(om, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of z-score of OM (252d window)
def f49ol_f49_semi_operating_leverage_omz_252d_slope_v034_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _z(om, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of z-score of OM (504d window)
def f49ol_f49_semi_operating_leverage_omz_504d_slope_v035_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _z(om, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of drawdown of OM from rolling peak (21d window)
def f49ol_f49_semi_operating_leverage_omdd_21d_slope_v036_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _max(om, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of drawdown of OM from rolling peak (63d window)
def f49ol_f49_semi_operating_leverage_omdd_63d_slope_v037_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _max(om, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of drawdown of OM from rolling peak (126d window)
def f49ol_f49_semi_operating_leverage_omdd_126d_slope_v038_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _max(om, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of drawdown of OM from rolling peak (252d window)
def f49ol_f49_semi_operating_leverage_omdd_252d_slope_v039_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _max(om, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of drawdown of OM from rolling peak (504d window)
def f49ol_f49_semi_operating_leverage_omdd_504d_slope_v040_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _max(om, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of run-up of OM above rolling trough (21d window)
def f49ol_f49_semi_operating_leverage_omrun_21d_slope_v041_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _min(om, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of run-up of OM above rolling trough (63d window)
def f49ol_f49_semi_operating_leverage_omrun_63d_slope_v042_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _min(om, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of run-up of OM above rolling trough (126d window)
def f49ol_f49_semi_operating_leverage_omrun_126d_slope_v043_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _min(om, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of run-up of OM above rolling trough (252d window)
def f49ol_f49_semi_operating_leverage_omrun_252d_slope_v044_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _min(om, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of run-up of OM above rolling trough (504d window)
def f49ol_f49_semi_operating_leverage_omrun_504d_slope_v045_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om - _min(om, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of range of OM (21d window)
def f49ol_f49_semi_operating_leverage_omrange_21d_slope_v046_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _max(om, 21) - _min(om, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of range of OM (63d window)
def f49ol_f49_semi_operating_leverage_omrange_63d_slope_v047_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _max(om, 63) - _min(om, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of range of OM (126d window)
def f49ol_f49_semi_operating_leverage_omrange_126d_slope_v048_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _max(om, 126) - _min(om, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of range of OM (252d window)
def f49ol_f49_semi_operating_leverage_omrange_252d_slope_v049_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _max(om, 252) - _min(om, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of range of OM (504d window)
def f49ol_f49_semi_operating_leverage_omrange_504d_slope_v050_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _max(om, 504) - _min(om, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling mean OM change in up-rev quarters (21d window)
def f49ol_f49_semi_operating_leverage_omchgposup_21d_slope_v051_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    base = _mean(omc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling mean OM change in up-rev quarters (63d window)
def f49ol_f49_semi_operating_leverage_omchgposup_63d_slope_v052_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    base = _mean(omc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling mean OM change in up-rev quarters (126d window)
def f49ol_f49_semi_operating_leverage_omchgposup_126d_slope_v053_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    base = _mean(omc, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling mean OM change in up-rev quarters (252d window)
def f49ol_f49_semi_operating_leverage_omchgposup_252d_slope_v054_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    base = _mean(omc, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling mean OM change in up-rev quarters (504d window)
def f49ol_f49_semi_operating_leverage_omchgposup_504d_slope_v055_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om).where(rg > 0)
    base = _mean(omc, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asymmetric OM change up minus down (21d window)
def f49ol_f49_semi_operating_leverage_omchgasym_21d_slope_v056_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 21)
    dn = _mean(omc.where(rg < 0), 21)
    base = up - dn
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asymmetric OM change up minus down (63d window)
def f49ol_f49_semi_operating_leverage_omchgasym_63d_slope_v057_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 63)
    dn = _mean(omc.where(rg < 0), 63)
    base = up - dn
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of asymmetric OM change up minus down (126d window)
def f49ol_f49_semi_operating_leverage_omchgasym_126d_slope_v058_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 126)
    dn = _mean(omc.where(rg < 0), 126)
    base = up - dn
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of asymmetric OM change up minus down (252d window)
def f49ol_f49_semi_operating_leverage_omchgasym_252d_slope_v059_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 252)
    dn = _mean(omc.where(rg < 0), 252)
    base = up - dn
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of asymmetric OM change up minus down (504d window)
def f49ol_f49_semi_operating_leverage_omchgasym_504d_slope_v060_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    omc = _f49ol_om_q_changes(om)
    up = _mean(omc.where(rg > 0), 504)
    dn = _mean(omc.where(rg < 0), 504)
    base = up - dn
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling mean of |OM quarter change| (21d window)
def f49ol_f49_semi_operating_leverage_omabschg_21d_slope_v061_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    base = _mean(omc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling mean of |OM quarter change| (63d window)
def f49ol_f49_semi_operating_leverage_omabschg_63d_slope_v062_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    base = _mean(omc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling mean of |OM quarter change| (126d window)
def f49ol_f49_semi_operating_leverage_omabschg_126d_slope_v063_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    base = _mean(omc, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling mean of |OM quarter change| (252d window)
def f49ol_f49_semi_operating_leverage_omabschg_252d_slope_v064_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    base = _mean(omc, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling mean of |OM quarter change| (504d window)
def f49ol_f49_semi_operating_leverage_omabschg_504d_slope_v065_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om).abs()
    base = _mean(omc, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling sign-run of OM changes (21d window)
def f49ol_f49_semi_operating_leverage_omsignrun_21d_slope_v066_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    base = s.rolling(21, min_periods=max(2, 21 // 2)).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling sign-run of OM changes (63d window)
def f49ol_f49_semi_operating_leverage_omsignrun_63d_slope_v067_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    base = s.rolling(63, min_periods=max(2, 63 // 2)).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling sign-run of OM changes (126d window)
def f49ol_f49_semi_operating_leverage_omsignrun_126d_slope_v068_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    base = s.rolling(126, min_periods=max(2, 126 // 2)).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling sign-run of OM changes (252d window)
def f49ol_f49_semi_operating_leverage_omsignrun_252d_slope_v069_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    base = s.rolling(252, min_periods=max(2, 252 // 2)).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling sign-run of OM changes (504d window)
def f49ol_f49_semi_operating_leverage_omsignrun_504d_slope_v070_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    s = np.sign(_f49ol_om_q_changes(om))
    base = s.rolling(504, min_periods=max(2, 504 // 2)).sum()
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling corr(OM, log revenue) (21d window)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_21d_slope_v071_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    base = _f49ol_roll_corr(om, lr, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling corr(OM, log revenue) (63d window)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_63d_slope_v072_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    base = _f49ol_roll_corr(om, lr, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling corr(OM, log revenue) (126d window)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_126d_slope_v073_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    base = _f49ol_roll_corr(om, lr, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling corr(OM, log revenue) (252d window)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_252d_slope_v074_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    base = _f49ol_roll_corr(om, lr, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling corr(OM, log revenue) (504d window)
def f49ol_f49_semi_operating_leverage_omlogrevcorr_504d_slope_v075_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    lr = np.log(_f49ol_rev_daily(revenue, closeadj.index).replace(0, np.nan).abs())
    base = _f49ol_roll_corr(om, lr, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of beta times sign of rev growth (21d window)
def f49ol_f49_semi_operating_leverage_oplevsign_21d_slope_v076_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 21)
    base = b * np.sign(rg)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of beta times sign of rev growth (63d window)
def f49ol_f49_semi_operating_leverage_oplevsign_63d_slope_v077_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 63)
    base = b * np.sign(rg)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of beta times sign of rev growth (126d window)
def f49ol_f49_semi_operating_leverage_oplevsign_126d_slope_v078_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 126)
    base = b * np.sign(rg)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of beta times sign of rev growth (252d window)
def f49ol_f49_semi_operating_leverage_oplevsign_252d_slope_v079_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 252)
    base = b * np.sign(rg)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of beta times sign of rev growth (504d window)
def f49ol_f49_semi_operating_leverage_oplevsign_504d_slope_v080_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 504)
    base = b * np.sign(rg)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling mean OM (21d window)
def f49ol_f49_semi_operating_leverage_omlevel_21d_slope_v081_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _mean(om, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling mean OM (63d window)
def f49ol_f49_semi_operating_leverage_omlevel_63d_slope_v082_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _mean(om, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling mean OM (126d window)
def f49ol_f49_semi_operating_leverage_omlevel_126d_slope_v083_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _mean(om, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling mean OM (252d window)
def f49ol_f49_semi_operating_leverage_omlevel_252d_slope_v084_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _mean(om, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling mean OM (504d window)
def f49ol_f49_semi_operating_leverage_omlevel_504d_slope_v085_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _mean(om, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling std OM (21d window)
def f49ol_f49_semi_operating_leverage_omlevelstd_21d_slope_v086_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _std(om, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling std OM (63d window)
def f49ol_f49_semi_operating_leverage_omlevelstd_63d_slope_v087_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _std(om, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling std OM (126d window)
def f49ol_f49_semi_operating_leverage_omlevelstd_126d_slope_v088_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _std(om, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling std OM (252d window)
def f49ol_f49_semi_operating_leverage_omlevelstd_252d_slope_v089_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _std(om, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling std OM (504d window)
def f49ol_f49_semi_operating_leverage_omlevelstd_504d_slope_v090_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = _std(om, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling trend slope of OM (cov/var with time) (21d window)
def f49ol_f49_semi_operating_leverage_omtrend_21d_slope_v091_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(21, min_periods=max(2, 21 // 2)).cov(t)
    var = t.rolling(21, min_periods=max(2, 21 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling trend slope of OM (cov/var with time) (63d window)
def f49ol_f49_semi_operating_leverage_omtrend_63d_slope_v092_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(63, min_periods=max(2, 63 // 2)).cov(t)
    var = t.rolling(63, min_periods=max(2, 63 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling trend slope of OM (cov/var with time) (126d window)
def f49ol_f49_semi_operating_leverage_omtrend_126d_slope_v093_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(126, min_periods=max(2, 126 // 2)).cov(t)
    var = t.rolling(126, min_periods=max(2, 126 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling trend slope of OM (cov/var with time) (252d window)
def f49ol_f49_semi_operating_leverage_omtrend_252d_slope_v094_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(252, min_periods=max(2, 252 // 2)).cov(t)
    var = t.rolling(252, min_periods=max(2, 252 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling trend slope of OM (cov/var with time) (504d window)
def f49ol_f49_semi_operating_leverage_omtrend_504d_slope_v095_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    t = pd.Series(np.arange(len(om), dtype=float), index=om.index)
    cov = om.rolling(504, min_periods=max(2, 504 // 2)).cov(t)
    var = t.rolling(504, min_periods=max(2, 504 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling beta(OM on QoQ rev growth) (21d window)
def f49ol_f49_semi_operating_leverage_oplevqoq_21d_slope_v096_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling beta(OM on QoQ rev growth) (63d window)
def f49ol_f49_semi_operating_leverage_oplevqoq_63d_slope_v097_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling beta(OM on QoQ rev growth) (126d window)
def f49ol_f49_semi_operating_leverage_oplevqoq_126d_slope_v098_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling beta(OM on QoQ rev growth) (252d window)
def f49ol_f49_semi_operating_leverage_oplevqoq_252d_slope_v099_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling beta(OM on QoQ rev growth) (504d window)
def f49ol_f49_semi_operating_leverage_oplevqoq_504d_slope_v100_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(om, rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of z-score of YoY rev growth (21d window)
def f49ol_f49_semi_operating_leverage_revgrowthz_21d_slope_v101_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _z(rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of z-score of YoY rev growth (63d window)
def f49ol_f49_semi_operating_leverage_revgrowthz_63d_slope_v102_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _z(rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of z-score of YoY rev growth (126d window)
def f49ol_f49_semi_operating_leverage_revgrowthz_126d_slope_v103_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _z(rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of z-score of YoY rev growth (252d window)
def f49ol_f49_semi_operating_leverage_revgrowthz_252d_slope_v104_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _z(rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of z-score of YoY rev growth (504d window)
def f49ol_f49_semi_operating_leverage_revgrowthz_504d_slope_v105_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _z(rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of z-score of OM quarter-change series (21d window)
def f49ol_f49_semi_operating_leverage_omgrowthz_21d_slope_v106_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _z(omc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of z-score of OM quarter-change series (63d window)
def f49ol_f49_semi_operating_leverage_omgrowthz_63d_slope_v107_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _z(omc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of z-score of OM quarter-change series (126d window)
def f49ol_f49_semi_operating_leverage_omgrowthz_126d_slope_v108_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _z(omc, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of z-score of OM quarter-change series (252d window)
def f49ol_f49_semi_operating_leverage_omgrowthz_252d_slope_v109_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _z(omc, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of z-score of OM quarter-change series (504d window)
def f49ol_f49_semi_operating_leverage_omgrowthz_504d_slope_v110_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    base = _z(omc, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of beta(OM,rev_yoy) times |rev growth| (21d window)
def f49ol_f49_semi_operating_leverage_oplevcomp_21d_slope_v111_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 21)
    base = b * rg.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of beta(OM,rev_yoy) times |rev growth| (63d window)
def f49ol_f49_semi_operating_leverage_oplevcomp_63d_slope_v112_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 63)
    base = b * rg.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of beta(OM,rev_yoy) times |rev growth| (126d window)
def f49ol_f49_semi_operating_leverage_oplevcomp_126d_slope_v113_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 126)
    base = b * rg.abs()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of beta(OM,rev_yoy) times |rev growth| (252d window)
def f49ol_f49_semi_operating_leverage_oplevcomp_252d_slope_v114_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 252)
    base = b * rg.abs()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of beta(OM,rev_yoy) times |rev growth| (504d window)
def f49ol_f49_semi_operating_leverage_oplevcomp_504d_slope_v115_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    b = _f49ol_roll_beta(om, rg, 504)
    base = b * rg.abs()
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of beta(QoQ opinc on QoQ rev) (21d window)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_21d_slope_v116_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of beta(QoQ opinc on QoQ rev) (63d window)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_63d_slope_v117_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of beta(QoQ opinc on QoQ rev) (126d window)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_126d_slope_v118_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of beta(QoQ opinc on QoQ rev) (252d window)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_252d_slope_v119_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of beta(QoQ opinc on QoQ rev) (504d window)
def f49ol_f49_semi_operating_leverage_oplevqoqoi_504d_slope_v120_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_qoq(opinc).reindex(closeadj.index).ffill()
    rg = _f49ol_rev_qoq(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_beta(og, rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of corr(OM quarter-change, rev YoY) (21d window)
def f49ol_f49_semi_operating_leverage_omchgrevcorr_21d_slope_v121_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_corr(omc, rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of corr(OM quarter-change, rev YoY) (63d window)
def f49ol_f49_semi_operating_leverage_omchgrevcorr_63d_slope_v122_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_corr(omc, rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of corr(OM quarter-change, rev YoY) (126d window)
def f49ol_f49_semi_operating_leverage_omchgrevcorr_126d_slope_v123_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_corr(omc, rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of corr(OM quarter-change, rev YoY) (252d window)
def f49ol_f49_semi_operating_leverage_omchgrevcorr_252d_slope_v124_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_corr(omc, rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of corr(OM quarter-change, rev YoY) (504d window)
def f49ol_f49_semi_operating_leverage_omchgrevcorr_504d_slope_v125_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    omc = _f49ol_om_q_changes(om)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _f49ol_roll_corr(omc, rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mean of OM times sign(rev growth) (21d window)
def f49ol_f49_semi_operating_leverage_omxrevsign_21d_slope_v126_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(om * np.sign(rg), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mean of OM times sign(rev growth) (63d window)
def f49ol_f49_semi_operating_leverage_omxrevsign_63d_slope_v127_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(om * np.sign(rg), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mean of OM times sign(rev growth) (126d window)
def f49ol_f49_semi_operating_leverage_omxrevsign_126d_slope_v128_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(om * np.sign(rg), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of mean of OM times sign(rev growth) (252d window)
def f49ol_f49_semi_operating_leverage_omxrevsign_252d_slope_v129_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(om * np.sign(rg), 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of mean of OM times sign(rev growth) (504d window)
def f49ol_f49_semi_operating_leverage_omxrevsign_504d_slope_v130_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(om * np.sign(rg), 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA-fast minus EMA-slow on OM (window-scaled) (21d window)
def f49ol_f49_semi_operating_leverage_omema_fast_21d_slope_v131_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om.ewm(span=max(2, 21 // 3), adjust=False).mean() - om.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EMA-fast minus EMA-slow on OM (window-scaled) (63d window)
def f49ol_f49_semi_operating_leverage_omema_fast_63d_slope_v132_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om.ewm(span=max(2, 63 // 3), adjust=False).mean() - om.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EMA-fast minus EMA-slow on OM (window-scaled) (126d window)
def f49ol_f49_semi_operating_leverage_omema_fast_126d_slope_v133_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om.ewm(span=max(2, 126 // 3), adjust=False).mean() - om.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of EMA-fast minus EMA-slow on OM (window-scaled) (252d window)
def f49ol_f49_semi_operating_leverage_omema_fast_252d_slope_v134_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om.ewm(span=max(2, 252 // 3), adjust=False).mean() - om.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of EMA-fast minus EMA-slow on OM (window-scaled) (504d window)
def f49ol_f49_semi_operating_leverage_omema_fast_504d_slope_v135_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    base = om.ewm(span=max(2, 504 // 3), adjust=False).mean() - om.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of pct-slope of OM smoothed over window (21d window)
def f49ol_f49_semi_operating_leverage_omslope_21d_slope_v136_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 21)
    base = smooth.pct_change(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pct-slope of OM smoothed over window (63d window)
def f49ol_f49_semi_operating_leverage_omslope_63d_slope_v137_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 63)
    base = smooth.pct_change(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of pct-slope of OM smoothed over window (126d window)
def f49ol_f49_semi_operating_leverage_omslope_126d_slope_v138_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 126)
    base = smooth.pct_change(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of pct-slope of OM smoothed over window (252d window)
def f49ol_f49_semi_operating_leverage_omslope_252d_slope_v139_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 252)
    base = smooth.pct_change(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of pct-slope of OM smoothed over window (504d window)
def f49ol_f49_semi_operating_leverage_omslope_504d_slope_v140_signal(opinc, revenue, closeadj):
    om = _f49ol_om_daily(opinc, revenue, closeadj.index)
    smooth = _mean(om, 504)
    base = smooth.pct_change(504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling mean of YoY rev growth (21d window)
def f49ol_f49_semi_operating_leverage_revyoylevel_21d_slope_v141_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(rg, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling mean of YoY rev growth (63d window)
def f49ol_f49_semi_operating_leverage_revyoylevel_63d_slope_v142_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(rg, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling mean of YoY rev growth (126d window)
def f49ol_f49_semi_operating_leverage_revyoylevel_126d_slope_v143_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(rg, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling mean of YoY rev growth (252d window)
def f49ol_f49_semi_operating_leverage_revyoylevel_252d_slope_v144_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(rg, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling mean of YoY rev growth (504d window)
def f49ol_f49_semi_operating_leverage_revyoylevel_504d_slope_v145_signal(opinc, revenue, closeadj):
    rg = _f49ol_rev_yoy(revenue).reindex(closeadj.index).ffill()
    base = _mean(rg, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rolling mean of YoY opinc growth (21d window)
def f49ol_f49_semi_operating_leverage_oiyoylevel_21d_slope_v146_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    base = _mean(og, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rolling mean of YoY opinc growth (63d window)
def f49ol_f49_semi_operating_leverage_oiyoylevel_63d_slope_v147_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    base = _mean(og, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of rolling mean of YoY opinc growth (126d window)
def f49ol_f49_semi_operating_leverage_oiyoylevel_126d_slope_v148_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    base = _mean(og, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of rolling mean of YoY opinc growth (252d window)
def f49ol_f49_semi_operating_leverage_oiyoylevel_252d_slope_v149_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    base = _mean(og, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope of rolling mean of YoY opinc growth (504d window)
def f49ol_f49_semi_operating_leverage_oiyoylevel_504d_slope_v150_signal(opinc, revenue, closeadj):
    og = _f49ol_oi_yoy(opinc).reindex(closeadj.index).ffill()
    base = _mean(og, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)
