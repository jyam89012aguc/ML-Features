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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt):
    nc = cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)
    return marketcap / nc.replace(0, np.nan).abs()


# 21d mean of mcap_to_netcash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_mean_21d_base_v001_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_to_netcash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_mean_63d_base_v002_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_to_netcash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_mean_126d_base_v003_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_to_netcash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_mean_252d_base_v004_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_to_netcash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_mean_504d_base_v005_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_to_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_mean_21d_base_v006_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_to_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_mean_63d_base_v007_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_to_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_mean_126d_base_v008_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_to_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_mean_252d_base_v009_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_to_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_mean_504d_base_v010_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_to_liqpool scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_mean_21d_base_v011_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_to_liqpool scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_mean_63d_base_v012_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_to_liqpool scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_mean_126d_base_v013_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_to_liqpool scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_mean_252d_base_v014_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_to_liqpool scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_mean_504d_base_v015_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netcash_to_mcap scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_mean_21d_base_v016_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netcash_to_mcap scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_mean_63d_base_v017_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netcash_to_mcap scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_mean_126d_base_v018_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netcash_to_mcap scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_mean_252d_base_v019_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netcash_to_mcap scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_mean_504d_base_v020_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_neg_box scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_mean_21d_base_v021_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_neg_box scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_mean_63d_base_v022_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_neg_box scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_mean_126d_base_v023_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_neg_box scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_mean_252d_base_v024_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_neg_box scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_mean_504d_base_v025_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_below_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_mean_21d_base_v026_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_below_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_mean_63d_base_v027_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_below_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_mean_126d_base_v028_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_below_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_mean_252d_base_v029_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_below_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_mean_504d_base_v030_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_minus_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_mean_21d_base_v031_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_minus_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_mean_63d_base_v032_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_minus_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_mean_126d_base_v033_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_minus_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_mean_252d_base_v034_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_minus_cash scaled by closeadj
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_mean_504d_base_v035_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_median_63d_base_v036_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_median_252d_base_v037_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_median_504d_base_v038_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_median_63d_base_v039_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_median_252d_base_v040_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_median_504d_base_v041_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_median_63d_base_v042_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_median_252d_base_v043_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_median_504d_base_v044_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_median_63d_base_v045_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_median_252d_base_v046_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_median_504d_base_v047_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_median_63d_base_v048_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_median_252d_base_v049_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_median_504d_base_v050_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_median_63d_base_v051_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_median_252d_base_v052_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_median_504d_base_v053_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_median_63d_base_v054_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_median_252d_base_v055_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_median_504d_base_v056_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_rmax_252d_base_v057_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_rmax_504d_base_v058_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_rmax_252d_base_v059_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_rmax_504d_base_v060_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_rmax_252d_base_v061_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_rmax_504d_base_v062_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_rmax_252d_base_v063_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_rmax_504d_base_v064_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_rmax_252d_base_v065_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_rmax_504d_base_v066_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_rmax_252d_base_v067_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_rmax_504d_base_v068_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_rmax_252d_base_v069_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_rmax_504d_base_v070_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_rmin_252d_base_v071_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_rmin_504d_base_v072_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_rmin_252d_base_v073_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_rmin_504d_base_v074_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_rmin_252d_base_v075_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

