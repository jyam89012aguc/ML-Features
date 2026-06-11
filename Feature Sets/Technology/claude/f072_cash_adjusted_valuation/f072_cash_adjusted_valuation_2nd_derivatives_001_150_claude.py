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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt):
    nc = cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)
    return marketcap / nc.replace(0, np.nan).abs()


# 21d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slope_21d_2d_v001_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slope_63d_2d_v002_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slope_126d_2d_v003_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slope_252d_2d_v004_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slope_504d_2d_v005_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slope_21d_2d_v006_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slope_63d_2d_v007_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slope_126d_2d_v008_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slope_252d_2d_v009_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slope_504d_2d_v010_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slope_21d_2d_v011_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slope_63d_2d_v012_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slope_126d_2d_v013_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slope_252d_2d_v014_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slope_504d_2d_v015_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slope_21d_2d_v016_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slope_63d_2d_v017_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slope_126d_2d_v018_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slope_252d_2d_v019_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slope_504d_2d_v020_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slope_21d_2d_v021_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slope_63d_2d_v022_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slope_126d_2d_v023_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slope_252d_2d_v024_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slope_504d_2d_v025_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slope_21d_2d_v026_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slope_63d_2d_v027_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slope_126d_2d_v028_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slope_252d_2d_v029_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slope_504d_2d_v030_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slope_21d_2d_v031_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slope_63d_2d_v032_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slope_126d_2d_v033_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slope_252d_2d_v034_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slope_504d_2d_v035_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sm21_sl21_2d_v036_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _mean(_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sm63_sl21_2d_v037_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _mean(_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sm63_sl63_2d_v038_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _mean(_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sm252_sl63_2d_v039_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _mean(_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sm252_sl126_2d_v040_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _mean(_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sm21_sl21_2d_v041_signal(ev, cashneq, closeadj):
    base = _mean(ev / cashneq.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sm63_sl21_2d_v042_signal(ev, cashneq, closeadj):
    base = _mean(ev / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sm63_sl63_2d_v043_signal(ev, cashneq, closeadj):
    base = _mean(ev / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sm252_sl63_2d_v044_signal(ev, cashneq, closeadj):
    base = _mean(ev / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sm252_sl126_2d_v045_signal(ev, cashneq, closeadj):
    base = _mean(ev / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sm21_sl21_2d_v046_signal(ev, cashneq, investmentsc, closeadj):
    base = _mean(ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sm63_sl21_2d_v047_signal(ev, cashneq, investmentsc, closeadj):
    base = _mean(ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sm63_sl63_2d_v048_signal(ev, cashneq, investmentsc, closeadj):
    base = _mean(ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sm252_sl63_2d_v049_signal(ev, cashneq, investmentsc, closeadj):
    base = _mean(ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sm252_sl126_2d_v050_signal(ev, cashneq, investmentsc, closeadj):
    base = _mean(ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sm21_sl21_2d_v051_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sm63_sl21_2d_v052_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sm63_sl63_2d_v053_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sm252_sl63_2d_v054_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sm252_sl126_2d_v055_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sm21_sl21_2d_v056_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sm63_sl21_2d_v057_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sm63_sl63_2d_v058_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sm252_sl63_2d_v059_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sm252_sl126_2d_v060_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sm21_sl21_2d_v061_signal(ev, cashneq, closeadj):
    base = _mean(((ev - cashneq) < 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sm63_sl21_2d_v062_signal(ev, cashneq, closeadj):
    base = _mean(((ev - cashneq) < 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sm63_sl63_2d_v063_signal(ev, cashneq, closeadj):
    base = _mean(((ev - cashneq) < 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sm252_sl63_2d_v064_signal(ev, cashneq, closeadj):
    base = _mean(((ev - cashneq) < 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sm252_sl126_2d_v065_signal(ev, cashneq, closeadj):
    base = _mean(((ev - cashneq) < 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sm21_sl21_2d_v066_signal(marketcap, cashneq, closeadj):
    base = _mean(marketcap - cashneq, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sm63_sl21_2d_v067_signal(marketcap, cashneq, closeadj):
    base = _mean(marketcap - cashneq, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sm63_sl63_2d_v068_signal(marketcap, cashneq, closeadj):
    base = _mean(marketcap - cashneq, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sm252_sl63_2d_v069_signal(marketcap, cashneq, closeadj):
    base = _mean(marketcap - cashneq, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sm252_sl126_2d_v070_signal(marketcap, cashneq, closeadj):
    base = _mean(marketcap - cashneq, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_pctslope_21d_2d_v071_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_pctslope_63d_2d_v072_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_pctslope_252d_2d_v073_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_pctslope_21d_2d_v074_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_pctslope_63d_2d_v075_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_pctslope_252d_2d_v076_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_pctslope_21d_2d_v077_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_pctslope_63d_2d_v078_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_pctslope_252d_2d_v079_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_pctslope_21d_2d_v080_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_pctslope_63d_2d_v081_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_pctslope_252d_2d_v082_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_pctslope_21d_2d_v083_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_pctslope_63d_2d_v084_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_pctslope_252d_2d_v085_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_pctslope_21d_2d_v086_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_pctslope_63d_2d_v087_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_pctslope_252d_2d_v088_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_pctslope_21d_2d_v089_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_pctslope_63d_2d_v090_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_pctslope_252d_2d_v091_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sgnslope_21d_2d_v092_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sgnslope_63d_2d_v093_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_sgnslope_252d_2d_v094_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sgnslope_21d_2d_v095_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sgnslope_63d_2d_v096_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_sgnslope_252d_2d_v097_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sgnslope_21d_2d_v098_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sgnslope_63d_2d_v099_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_sgnslope_252d_2d_v100_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sgnslope_21d_2d_v101_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sgnslope_63d_2d_v102_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_sgnslope_252d_2d_v103_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sgnslope_21d_2d_v104_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sgnslope_63d_2d_v105_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_sgnslope_252d_2d_v106_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sgnslope_21d_2d_v107_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sgnslope_63d_2d_v108_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_sgnslope_252d_2d_v109_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sgnslope_21d_2d_v110_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sgnslope_63d_2d_v111_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_sgnslope_252d_2d_v112_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_logmagslope_21d_2d_v113_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_logmagslope_63d_2d_v114_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_logmagslope_252d_2d_v115_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_logmagslope_21d_2d_v116_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_logmagslope_63d_2d_v117_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_logmagslope_252d_2d_v118_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_logmagslope_21d_2d_v119_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_logmagslope_63d_2d_v120_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_logmagslope_252d_2d_v121_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_logmagslope_21d_2d_v122_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_logmagslope_63d_2d_v123_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_logmagslope_252d_2d_v124_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_logmagslope_21d_2d_v125_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_logmagslope_63d_2d_v126_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_logmagslope_252d_2d_v127_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_logmagslope_21d_2d_v128_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_logmagslope_63d_2d_v129_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_logmagslope_252d_2d_v130_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_logmagslope_21d_2d_v131_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_logmagslope_63d_2d_v132_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_logmagslope_252d_2d_v133_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_to_netcash|
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_logslope_63d_2d_v134_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = np.log((_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_to_netcash|
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_logslope_252d_2d_v135_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = np.log((_f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_to_cash|
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_logslope_63d_2d_v136_signal(ev, cashneq, closeadj):
    base = np.log((ev / cashneq.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_to_cash|
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_logslope_252d_2d_v137_signal(ev, cashneq, closeadj):
    base = np.log((ev / cashneq.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_to_liqpool|
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_logslope_63d_2d_v138_signal(ev, cashneq, investmentsc, closeadj):
    base = np.log((ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_to_liqpool|
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_logslope_252d_2d_v139_signal(ev, cashneq, investmentsc, closeadj):
    base = np.log((ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_to_mcap|
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_logslope_63d_2d_v140_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = np.log(((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_to_mcap|
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_logslope_252d_2d_v141_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = np.log(((cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_neg_box|
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_logslope_63d_2d_v142_signal(ev, closeadj):
    base = np.log(((ev < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_neg_box|
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_logslope_252d_2d_v143_signal(ev, closeadj):
    base = np.log(((ev < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_below_cash|
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_logslope_63d_2d_v144_signal(ev, cashneq, closeadj):
    base = np.log((((ev - cashneq) < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_below_cash|
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_logslope_252d_2d_v145_signal(ev, cashneq, closeadj):
    base = np.log((((ev - cashneq) < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_minus_cash|
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_logslope_63d_2d_v146_signal(marketcap, cashneq, closeadj):
    base = np.log((marketcap - cashneq).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_minus_cash|
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_logslope_252d_2d_v147_signal(marketcap, cashneq, closeadj):
    base = np.log((marketcap - cashneq).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

